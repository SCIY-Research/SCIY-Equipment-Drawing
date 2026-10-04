#!/usr/bin/env python3
"""Create a repeatable SVG LINEART geometry signature.

This is intended for before/after coloring checks. It hashes geometry-related
attributes inside elements whose id/label contains LINEART. If LINEART cannot
be isolated, it can optionally hash all vector geometry with --all.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
import xml.etree.ElementTree as ET

GEOM_ATTRS = ("d", "points", "x", "y", "x1", "y1", "x2", "y2", "cx", "cy", "r", "rx", "ry", "width", "height", "transform")
VECTOR_TAGS = {"path", "polygon", "polyline", "rect", "circle", "ellipse", "line"}


def lname(tag: str) -> str:
    return tag.split("}")[-1]


def is_lineart(elem: ET.Element) -> bool:
    txt = " ".join([
        elem.attrib.get("id", ""),
        elem.attrib.get("{http://www.inkscape.org/namespaces/inkscape}label", ""),
        elem.attrib.get("data-name", ""),
    ]).upper()
    return "LINEART" in txt


def canonical(elem: ET.Element) -> list[str]:
    out = []
    for e in elem.iter():
        tag = lname(e.tag)
        if tag not in VECTOR_TAGS:
            continue
        attrs = [f"{k}={e.attrib.get(k,'')}" for k in GEOM_ATTRS if k in e.attrib]
        out.append(tag + "|" + "|".join(attrs))
    return out


def signature(path: Path, use_all: bool = False) -> dict[str, object]:
    tree = ET.parse(path)
    root = tree.getroot()
    targets = []
    if not use_all:
        targets = [e for e in root.iter() if is_lineart(e)]
    if not targets:
        if not use_all:
            raise ValueError("No LINEART-labeled element found. Re-run with --all only if hashing all vector geometry is intended.")
        targets = [root]
    rows = []
    for t in targets:
        rows.extend(canonical(t))
    rows = sorted(rows)
    payload = "\n".join(rows).encode("utf-8")
    return {
        "file": str(path.resolve()),
        "scope": "all" if use_all else "LINEART",
        "vector_records": len(rows),
        "sha256": hashlib.sha256(payload).hexdigest().upper(),
    }


def main() -> None:
    p = argparse.ArgumentParser(description="Hash SVG LINEART geometry for before/after coloring checks.")
    p.add_argument("svg", type=Path)
    p.add_argument("--all", action="store_true", help="Hash all vector geometry instead of requiring a LINEART-labeled group.")
    a = p.parse_args()
    if not a.svg.is_file():
        p.error(f"SVG not found: {a.svg}")
    try:
        result = signature(a.svg, a.all)
    except ValueError as exc:
        p.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
