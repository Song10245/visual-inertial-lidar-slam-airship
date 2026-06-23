#!/usr/bin/env python3
"""Compute percentage error between reference and observed map measurements.

CSV format:
measurement,metres
width,10.0
length,20.0

The script matches rows by measurement name and reports absolute percentage error.
"""

import argparse
import pandas as pd


def load_measurements(path):
    df = pd.read_csv(path)
    required = {"measurement", "metres"}
    if not required.issubset(df.columns):
        raise ValueError(f"{path} must contain columns: {required}")
    return df.set_index("measurement")["metres"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", required=True, help="CSV containing ground-truth or reference dimensions")
    parser.add_argument("--observed", required=True, help="CSV containing map-derived dimensions")
    args = parser.parse_args()

    reference = load_measurements(args.reference)
    observed = load_measurements(args.observed)
    common = reference.index.intersection(observed.index)
    if common.empty:
        raise ValueError("No matching measurement names found.")

    rows = []
    for name in common:
        ref = reference.loc[name]
        obs = observed.loc[name]
        error_pct = abs(obs - ref) / ref * 100.0 if ref != 0 else float("nan")
        rows.append({"measurement": name, "reference_m": ref, "observed_m": obs, "error_pct": error_pct})

    out = pd.DataFrame(rows)
    print(out.to_string(index=False, float_format=lambda x: f"{x:.3f}"))
    print(f"\nMean absolute percentage error: {out['error_pct'].mean():.3f}%")


if __name__ == "__main__":
    main()
