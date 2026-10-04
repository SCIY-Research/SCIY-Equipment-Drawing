# Illustrator Vectorization And Export v1.1

## Line Trace Starting Point

```text
Mode: Black and White
Threshold: 155
Path Fitting: 1.5
Corner Angle: 45
Noise Fidelity: 18
Ignore White: true
Expand: true
```

Tune per device when needed. Place the expanded result in `LINEART`.

Image Trace commonly represents visible black lines as closed filled contours. That is a valid vector result. Do not claim centerline strokes unless SVG/AI inspection proves they exist.

## Do Not Re-Trace For Coloring

The previous workflow of independently tracing a color master can change geometry and is **not** the authoritative coloring method in v1.1.

After line geometry is approved:

- lock `LINEART`;
- color existing closed regions or geometry-matched copies;
- never use a newly traced color image to replace the approved structure.

## Background / Artboard

Keep Illustrator artboard, SVG viewBox, and any explicit background rectangle consistent. Mismatched dimensions can create black/empty bands in exported PNG previews.

When a white presentation background is needed, ensure it covers the complete artboard/viewBox. For transparent SVG, omit the background intentionally.

## Layer Order

```text
LINEART       top, locked
HIGHLIGHT
SHADOW
COLOR_BASE
```

## Editable Master Outputs

Prefer versioned names:

```text
设备名称_线稿_v01.ai/.svg/_预览.png
设备名称_技术插画风_上色_v01.ai/.svg/_preview.png
```

Do not overwrite earlier versions.

## Validation

- Illustrator was actually invoked and version recorded.
- Image Trace and Expand actually completed.
- AI reopens with editable vector objects.
- SVG contains real vector elements and zero `<image>` elements where full vector output is promised.
- Preview is visually inspected for crop, artboard mismatch, missing components, duplicated outlines, and geometry drift.
- Coloring must pass geometry-lock validation before being accepted.
