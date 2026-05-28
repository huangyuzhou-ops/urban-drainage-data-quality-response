from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - optional dependency fallback
    yaml = None


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        if path.suffix.lower() == ".json":
            cfg = json.load(f)
        else:
            if yaml is None:
                raise ModuleNotFoundError(
                    "PyYAML is required for YAML configuration files. "
                    "Install pyyaml or use the JSON configuration file."
                )
            cfg = yaml.safe_load(f)
    if not isinstance(cfg, dict):
        raise ValueError("Configuration file must contain a YAML mapping.")
    return cfg


def resolve_path(base: Path, value: str | Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return (base / path).resolve()


def read_table(path: Path) -> pd.DataFrame:
    """Read CSV-like files, with Excel fallback for files carrying a wrong extension."""
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.read_excel(path)


def stable_hash(value: str, salt: str) -> str:
    raw = (salt + "::" + value).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def build_id_map(sensor_ids: list[str], prefix: str, digits: int, salt: str) -> pd.DataFrame:
    unique_ids = sorted(set(str(x) for x in sensor_ids))
    hashed = [(sid, stable_hash(sid, salt)) for sid in unique_ids]
    hashed.sort(key=lambda item: item[1])
    rows = []
    for idx, (sid, digest) in enumerate(hashed, start=1):
        rows.append(
            {
                "sensor_id_original": sid,
                "sensor_id_public": f"{prefix}{idx:0{digits}d}",
                "sensor_hash_public": digest[:16],
            }
        )
    return pd.DataFrame(rows)


def rotate_scale_coordinates(
    x: pd.Series,
    y: pd.Series,
    angle_degrees: float,
    scale_factor: float,
    translate_x: float,
    translate_y: float,
    jitter_std: float,
    round_decimals: int,
) -> tuple[pd.Series, pd.Series, dict[str, float]]:
    x_num = pd.to_numeric(x, errors="coerce")
    y_num = pd.to_numeric(y, errors="coerce")
    cx = float(x_num.mean())
    cy = float(y_num.mean())
    theta = math.radians(angle_degrees)
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    x0 = x_num - cx
    y0 = y_num - cy
    xr = scale_factor * (x0 * cos_t - y0 * sin_t) + translate_x
    yr = scale_factor * (x0 * sin_t + y0 * cos_t) + translate_y
    if jitter_std > 0:
        rng = np.random.default_rng(20260528)
        xr = xr + rng.normal(0.0, jitter_std, size=len(xr))
        yr = yr + rng.normal(0.0, jitter_std, size=len(yr))
    return xr.round(round_decimals), yr.round(round_decimals), {"centroid_x": cx, "centroid_y": cy}


def transform_vertical_columns(df: pd.DataFrame, cfg: dict[str, Any]) -> pd.DataFrame:
    if not cfg.get("enabled", False):
        return df
    columns = [col for col in cfg.get("columns", []) if col in df.columns]
    if not columns:
        return df
    scale = float(cfg.get("scale_factor", 1.0))
    offset = float(cfg.get("offset", 0.0))
    decimals = int(cfg.get("round_decimals", 3))
    suffix = str(cfg.get("suffix", "_public"))
    if cfg.get("publish_transformed_vertical", False):
        for col in columns:
            values = pd.to_numeric(df[col], errors="coerce")
            center = float(values.median())
            df[col + suffix] = ((values - center) * scale + offset).round(decimals)
    if cfg.get("drop_original_columns", True):
        df = df.drop(columns=columns)
    return df


def find_timestamp_column(columns: list[str], candidates: list[str]) -> str | None:
    lower_map = {str(c).lower(): str(c) for c in columns}
    for cand in candidates:
        if cand in columns:
            return cand
        if cand.lower() in lower_map:
            return lower_map[cand.lower()]
    return None


def infer_value_columns(df: pd.DataFrame, timestamp_col: str | None) -> list[str]:
    blocked = {timestamp_col, "sensor_id", "scada_id", "node_id", "name", "id", None}
    numeric_cols = []
    for col in df.columns:
        if col in blocked:
            continue
        series = pd.to_numeric(df[col], errors="coerce")
        if series.notna().sum() > 0:
            numeric_cols.append(str(col))
    return numeric_cols[:1]


def transform_timeseries_values(df: pd.DataFrame, value_cols: list[str], cfg: dict[str, Any]) -> pd.DataFrame:
    out_col = str(cfg.get("public_value_column", "level_public"))
    scale = float(cfg.get("scale_factor", 10.0))
    offset = float(cfg.get("offset", 100.0))
    decimals = int(cfg.get("round_decimals", 4))
    if not value_cols:
        return df
    value = pd.to_numeric(df[value_cols[0]], errors="coerce")
    q01 = value.quantile(0.01)
    q99 = value.quantile(0.99)
    denom = float(q99 - q01)
    if not np.isfinite(denom) or denom == 0:
        denom = float(value.std())
    if not np.isfinite(denom) or denom == 0:
        denom = 1.0
    centered = value - float(value.median())
    df[out_col] = (centered / denom * scale + offset).round(decimals)
    keep = [out_col]
    return df[keep]


def anonymize_timeseries(
    catalog: pd.DataFrame,
    id_map: pd.DataFrame,
    cfg: dict[str, Any],
    base: Path,
    public_dir: Path,
) -> list[dict[str, Any]]:
    ts_cfg = cfg.get("timeseries_transform", {})
    if not ts_cfg.get("enabled", False):
        return []

    input_dir = resolve_path(base, cfg["inputs"]["monitoring_timeseries_dir"])
    output_dir = public_dir / cfg["outputs"].get("timeseries_dir", "timeseries_anonymized")
    output_dir.mkdir(parents=True, exist_ok=True)
    mapping = dict(zip(id_map["sensor_id_original"], id_map["sensor_id_public"]))
    file_rows = []

    for _, row in catalog.iterrows():
        sid = str(row["sensor_id"])
        public_id = mapping.get(sid)
        if not public_id:
            continue
        file_name = str(row.get("timeseries_file", f"{sid}.csv"))
        source = input_dir / file_name
        if not source.exists():
            matches = list(input_dir.glob(file_name))
            if not matches:
                continue
            source = matches[0]
        raw = read_table(source)
        ts_col = find_timestamp_column(list(raw.columns), ts_cfg.get("timestamp_columns", []))
        if ts_cfg.get("value_columns", "auto") == "auto":
            value_cols = infer_value_columns(raw, ts_col)
        else:
            value_cols = [col for col in ts_cfg.get("value_columns", []) if col in raw.columns]
        public = transform_timeseries_values(raw.copy(), value_cols, ts_cfg)
        public.insert(0, "sensor_id_public", public_id)
        if ts_cfg.get("replace_absolute_time_with_index", True):
            public.insert(1, "timestep_index", np.arange(len(public), dtype=int))
            minutes = int(ts_cfg.get("minutes_per_step", 5))
            public.insert(2, "minutes_from_start", np.arange(len(public), dtype=int) * minutes)
        elif ts_col is not None:
            public.insert(1, "timestamp", raw[ts_col])
        out_name = f"{public_id}.csv"
        public.to_csv(output_dir / out_name, index=False)
        file_rows.append({"sensor_id_public": public_id, "source_rows": int(len(raw)), "public_file": out_name})

    return file_rows


def assert_public_catalog_safe(df: pd.DataFrame, cfg: dict[str, Any]) -> None:
    qc = cfg.get("quality_control", {})
    if qc.get("fail_if_original_xy_in_public", True):
        forbidden = {"x", "y"}
        present = forbidden.intersection(df.columns)
        if present:
            raise ValueError(f"Public catalogue still contains original coordinate columns: {sorted(present)}")
    if qc.get("fail_if_any_coordinate_columns_in_public", False):
        coordinate_like = [
            col
            for col in df.columns
            if str(col).lower() in {"x", "y", "lon", "lat", "longitude", "latitude", "x_public", "y_public"}
            or str(col).lower().endswith(("_x", "_y"))
        ]
        if coordinate_like:
            raise ValueError(f"Public catalogue still contains coordinate-like columns: {coordinate_like}")
    if qc.get("fail_if_original_ids_in_public", True):
        id_pattern = re.compile(qc.get("allowed_public_identifier_pattern", r"^S[0-9]{4}$"))
        if "sensor_id_public" in df.columns:
            bad = [x for x in df["sensor_id_public"].astype(str).head(10) if not id_pattern.match(x)]
            if bad:
                raise ValueError(f"Public IDs do not match the configured pattern. Examples: {bad}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Anonymize urban drainage monitoring catalogue and optional time series.")
    parser.add_argument("--config", required=True, help="Path to anonymization YAML configuration.")
    args = parser.parse_args()

    config_path = Path(args.config).resolve()
    base = config_path.parent
    cfg = load_config(config_path)

    public_dir = resolve_path(base, cfg["outputs"]["public_dir"])
    public_dir.mkdir(parents=True, exist_ok=True)

    catalog_path = resolve_path(base, cfg["inputs"]["sensor_catalog"])
    catalog = read_table(catalog_path)
    if "sensor_id" not in catalog.columns:
        raise ValueError("Sensor catalogue must contain a 'sensor_id' column.")

    privacy = cfg.get("privacy", {})
    salt_env = str(privacy.get("id_salt_env", "RQ1_ANON_SALT"))
    salt = os.getenv(salt_env, str(privacy.get("fallback_public_salt", "")))
    if not salt:
        raise ValueError("A non-empty anonymization salt is required.")

    id_map = build_id_map(
        catalog["sensor_id"].astype(str).tolist(),
        prefix=str(privacy.get("id_prefix", "S")),
        digits=int(privacy.get("id_digits", 4)),
        salt=salt,
    )
    public_catalog = catalog.merge(id_map, left_on="sensor_id", right_on="sensor_id_original", how="left")

    spatial = cfg.get("spatial_transform", {})
    spatial_meta: dict[str, float] = {}
    if spatial.get("enabled", True):
        x_col = str(spatial.get("x_column", "x"))
        y_col = str(spatial.get("y_column", "y"))
        x_public, y_public, spatial_meta = rotate_scale_coordinates(
            public_catalog[x_col],
            public_catalog[y_col],
            angle_degrees=float(spatial.get("rotation_degrees", 37.0)),
            scale_factor=float(spatial.get("scale_factor", 3.7)),
            translate_x=float(spatial.get("translate_x", 0.0)),
            translate_y=float(spatial.get("translate_y", 0.0)),
            jitter_std=float(spatial.get("jitter_std", 0.0)),
            round_decimals=int(spatial.get("round_decimals", 2)),
        )
        if spatial.get("publish_transformed_coordinates", False):
            public_catalog[spatial.get("output_x_column", "x_public")] = x_public
            public_catalog[spatial.get("output_y_column", "y_public")] = y_public
        if spatial.get("drop_original_xy", True):
            public_catalog = public_catalog.drop(columns=[x_col, y_col], errors="ignore")
    elif spatial.get("drop_original_xy", True):
        public_catalog = public_catalog.drop(
            columns=[spatial.get("x_column", "x"), spatial.get("y_column", "y")],
            errors="ignore",
        )

    public_catalog = transform_vertical_columns(public_catalog, cfg.get("vertical_transform", {}))

    if privacy.get("drop_original_identifier_columns", True):
        public_catalog = public_catalog.drop(
            columns=[c for c in privacy.get("identifier_columns", []) if c in public_catalog.columns],
            errors="ignore",
        )
        public_catalog = public_catalog.drop(columns=["sensor_id_original"], errors="ignore")
    if not privacy.get("include_public_hash", False):
        public_catalog = public_catalog.drop(columns=["sensor_hash_public"], errors="ignore")
    public_catalog = public_catalog.drop(columns=privacy.get("drop_additional_columns", []), errors="ignore")

    # Keep the public ID as the first column.
    if "sensor_id_public" in public_catalog.columns:
        cols = ["sensor_id_public"] + [c for c in public_catalog.columns if c != "sensor_id_public"]
        public_catalog = public_catalog[cols]
    if privacy.get("shuffle_rows", True):
        public_catalog = public_catalog.sample(
            frac=1.0,
            random_state=int(privacy.get("shuffle_seed", 20260528)),
        ).reset_index(drop=True)

    assert_public_catalog_safe(public_catalog, cfg)
    catalog_out = public_dir / cfg["outputs"].get("sensor_catalog_out", "sensors_anonymized.csv")
    public_catalog.to_csv(catalog_out, index=False)

    if privacy.get("keep_private_id_map", False):
        private_dir = resolve_path(base, cfg["outputs"].get("private_dir", "../_private_anonymization"))
        private_dir.mkdir(parents=True, exist_ok=True)
        id_map.to_csv(private_dir / cfg["outputs"].get("private_id_map_out", "sensor_id_mapping_private.csv"), index=False)

    ts_files = anonymize_timeseries(catalog, id_map, cfg, base, public_dir)

    provenance = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "config_file": config_path.name,
        "input_sensor_catalog_file": catalog_path.name,
        "public_dir": public_dir.name,
        "sensor_count": int(len(catalog)),
        "public_sensor_catalog": catalog_out.name,
        "timeseries_files_written": len(ts_files),
        "spatial_transform": (
            {
                "coordinates_published": True,
                **{k: v for k, v in spatial.items() if k not in {"center"}},
                **spatial_meta,
            }
            if spatial.get("publish_transformed_coordinates", False)
            else {
                "coordinates_published": False,
                "drop_original_xy": bool(spatial.get("drop_original_xy", True)),
            }
        ),
        "vertical_transform": {
            "vertical_values_published": bool(cfg.get("vertical_transform", {}).get("publish_transformed_vertical", False)),
            "drop_original_columns": bool(cfg.get("vertical_transform", {}).get("drop_original_columns", True)),
        },
        "identifier_strategy": {
            "id_prefix": privacy.get("id_prefix", "S"),
            "id_digits": privacy.get("id_digits", 4),
            "salt_source": salt_env if os.getenv(salt_env) else "fallback_public_salt",
            "private_id_map_written": bool(privacy.get("keep_private_id_map", False)),
        },
    }
    with (public_dir / cfg["outputs"].get("provenance_out", "anonymization_provenance.json")).open(
        "w", encoding="utf-8"
    ) as f:
        json.dump(provenance, f, ensure_ascii=False, indent=2)

    print(json.dumps(provenance, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
