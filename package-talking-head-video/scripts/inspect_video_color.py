#!/usr/bin/env python3
"""Inspect video color metadata and optional representative luma samples."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


METRICS = {"YMIN", "YLOW", "YAVG", "YHIGH", "YMAX", "SATAVG", "SATMAX"}


def binary(name: str) -> str:
    override = os.environ.get(name.upper())
    found = override or shutil.which(name)
    if not found:
        raise SystemExit(f"{name} not found. Put it on PATH or set {name.upper()}.")
    return found


def run_json(command: list[str]) -> dict:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def probe(path: Path, ffprobe: str) -> dict:
    data = run_json(
        [
            ffprobe,
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=codec_name,width,height,pix_fmt,r_frame_rate,color_range,color_space,color_transfer,color_primaries,side_data_list:format=duration,size",
            "-of",
            "json",
            str(path),
        ]
    )
    stream = (data.get("streams") or [{}])[0]
    return {"stream": stream, "format": data.get("format", {})}


def sample(path: Path, ffmpeg: str, timestamp: float, crop: str | None) -> dict:
    filters = []
    if crop:
        filters.append(f"crop={crop}")
    filters.extend(["signalstats", "metadata=print:file=-"])
    command = [
        ffmpeg,
        "-hide_banner",
        "-loglevel",
        "error",
        "-ss",
        str(timestamp),
        "-i",
        str(path),
        "-frames:v",
        "1",
        "-vf",
        ",".join(filters),
        "-f",
        "null",
        "-",
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    values: dict[str, float] = {}
    for key, value in re.findall(r"lavfi\.signalstats\.([A-Z]+)=([0-9.]+)", result.stdout):
        if key in METRICS:
            values[key] = float(value)
    return {"timestamp": timestamp, "crop": crop, "metrics": values}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--timestamps", default="", help="Comma-separated seconds, e.g. 4,12,50")
    parser.add_argument("--crop", help="Displayed-frame crop W:H:X:Y; use the same facial ROI across files")
    args = parser.parse_args()

    ffprobe = binary("ffprobe")
    timestamps = [float(x) for x in args.timestamps.split(",") if x.strip()]
    ffmpeg = binary("ffmpeg") if timestamps else None
    output = []

    for path in args.files:
        if not path.is_file():
            raise SystemExit(f"File not found: {path}")
        item = {"file": str(path.resolve()), **probe(path, ffprobe)}
        if ffmpeg:
            item["samples"] = [sample(path, ffmpeg, t, args.crop) for t in timestamps]
        output.append(item)

    json.dump(output, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
