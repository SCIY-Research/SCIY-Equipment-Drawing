#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def _first_attr(text: str, element: str, attr: str):
    m = re.search(rf"<{element}\b[^>]*\b{attr}\s*=\s*['\"]([^'\"]+)['\"]", text, re.I)
    return m.group(1) if m else None


def audit(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="replace")
    colors = sorted(set(re.findall(r"#[0-9A-Fa-f]{6}\b", text)))
    return {
        "file": str(path.resolve()),
        "bytes": path.stat().st_size,
        "viewBox": _first_attr(text, "svg", "viewBox"),
        "width": _first_attr(text, "svg", "width"),
        "height": _first_attr(text, "svg", "height"),
        "path": len(re.findall(r"<path\b", text)),
        "polygon": len(re.findall(r"<polygon\b", text)),
        "rect": len(re.findall(r"<rect\b", text)),
        "circle": len(re.findall(r"<circle\b", text)),
        "ellipse": len(re.findall(r"<ellipse\b", text)),
        "image": len(re.findall(r"<image\b", text)),
        "mask": len(re.findall(r"<mask\b", text)),
        "filter": len(re.findall(r"<filter\b", text)),
        "clipPath": len(re.findall(r"<clipPath\b", text)),
        "stroke_mentions": len(re.findall(r"(?:stroke\s*=|stroke\s*:)", text)),
        "mix_blend_mode_mentions": len(re.findall(r"mix-blend-mode", text, re.I)),
        "multiply_mentions": len(re.findall(r"(?:mix-blend-mode\s*:\s*multiply|mix-blend-mode\s*=\s*['\"]multiply)", text, re.I)),
        "explicit_colors": colors,
        "explicit_color_count": len(colors),
        "has_color_base": "COLOR_BASE" in text,
        "has_shadow": "SHADOW" in text,
        "has_highlight": "HIGHLIGHT" in text,
        "has_lineart": "LINEART" in text,
        "ppt_risk": {
            "has_mix_blend_mode": "mix-blend-mode" in text.lower(),
            "has_mask": bool(re.search(r"<mask\b|mask\s*=|mask\s*:", text, re.I)),
            "has_filter": bool(re.search(r"<filter\b|filter\s*=|filter\s*:", text, re.I)),
            "has_embedded_image": bool(re.search(r"<image\b", text, re.I)),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit an Illustrator-exported scientific-equipment SVG.")
    parser.add_argument("svg", type=Path)
    args = parser.parse_args()
    if not args.svg.is_file():
        parser.error(f"SVG not found: {args.svg}")
    print(json.dumps(audit(args.svg), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
