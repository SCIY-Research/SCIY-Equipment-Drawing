# Geometry-Locked Coloring And Lighting

## Rule Zero

Once the approved vector lineart exists, coloring must not alter geometry.

Coloring may change only visual properties or add separate style layers. It must not regenerate, retrace, simplify, reshape, or replace approved paths.

## Recommended Layers

```text
LINEART        locked, top
HIGHLIGHT
SHADOW
COLOR_BASE
```

## Base Color

Fill existing closed regions or copies derived from the exact approved geometry. Use a small restrained palette appropriate to the selected style.

Typical material separation may include:

- painted/metal body;
- flange/structural metal;
- fasteners/fittings;
- glass/window;
- handles/seals/controls.

Do not infer materials when the source does not support them.

## Lighting

Default light direction: upper-left.

For `Technical Illustration`, use restrained editable vector lighting:

- shadow opacity commonly about 4–12%;
- highlight opacity commonly about 5–12%;
- clipped vector ellipses/shapes;
- linear/radial gradients only when they remain clean and portable.

Prefer vector shading over raster blur or heavy effects.

## Glass

Use a restrained light blue/blue-gray fill, optional modest transparency, and a simple highlight. Do not redraw the glass outline.

## Geometry Integrity

Before coloring, record a geometry signature for `LINEART` when possible. Recheck after save/reopen.

A geometry-lock pass should compare at least:

- path count;
- path geometry data;
- anchor/control-point signature where accessible;
- bounding boxes.

If locked geometry changes unexpectedly, coloring fails and should be rolled back.
