# PowerPoint SVG Compatibility

## Separate Deliverable

Treat PowerPoint SVG as a presentation derivative, not the editable engineering master.

Keep:

- editable master: `.ai` (and normal SVG if useful);
- presentation derivative: `_PPT兼容.svg`.

Never overwrite the editable master during compatibility conversion.

## Known Fragile Features

PowerPoint SVG rendering may mishandle or differ from Illustrator/browser rendering for:

- `mix-blend-mode`, especially `multiply`;
- SVG masks;
- some filters/blur/effects;
- complex compositing stacks.

Do not depend on these features for essential visible color/outline structure.

## Outline Preservation

A compatibility export must preserve the **actual visible outline**. Do not merely add strokes to COLOR_BASE regions, because that can remove connection contours and create white seams between valves, fittings, flange parts, and supports.

When required, derive a presentation-safe visible outline by vector Boolean composition of the source lineart:

- combine visible black regions;
- subtract white/negative-space regions in stacking order;
- place the resulting visible outline above COLOR_BASE/SHADOW/HIGHLIGHT;
- avoid multiply and mask dependencies.

This conversion may legitimately reorganize path structure. Therefore do **not** reuse the editable-master path-count/hash expectation for the PPT-compatible derivative.

## PPT Acceptance

A compatibility SVG passes only after a real PowerPoint insertion/render check verifies:

- colors are visible;
- full artboard is present;
- no black/empty export band;
- no white seams at component connections;
- valves/fittings/flanges retain their visible boundaries;
- shading/highlights remain acceptable;
- no raster image is embedded when pure vector is promised.

Geometry-lock QA and PowerPoint appearance QA are separate checks and must be recorded separately.
