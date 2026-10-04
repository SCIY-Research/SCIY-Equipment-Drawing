# Changelog

## v1.1

### Added

- Four explicit visual styles: Academic Flat, Product Reference, Technical Illustration, and Lineart First.
- 1 / 2 / 4 controlled candidate generation with maximum 4.
- Style Comparison Mode.
- Public / modified / self-built / mixed-device routing with soft information gates.
- Evidence-priority and multi-reference fusion rules.
- Mechanical SVG geometry rules: straight stays straight, circle stays circular, symmetric stays symmetric, and no thick-paint tracing.
- Geometry-locked coloring: approved LINEART is the single geometry authority.
- `COLOR_BASE`, `SHADOW`, `HIGHLIGHT`, `LINEART` layer model.
- Restrained editable vector lighting with upper-left default light direction.
- Separate editable-master and PowerPoint-compatible SVG export targets.
- PowerPoint compatibility rules that avoid reliance on multiply/masks and require real PPT insertion checks.
- Separate geometry-integrity QA and PPT appearance QA.
- SVG geometry signature utility.

### Improved

- SVG straight-line/circular preservation, multi-reference fusion, and Illustrator workflow.
- Coloring stability and PowerPoint compatibility.

- Deprecated independent color Image Trace as the authoritative coloring pipeline because it can alter confirmed geometry.
- Coloring is now a style operation over locked geometry.
- Presentation compatibility conversions must be versioned separately and must never overwrite the editable AI master.
- Artboard/background/export dimensions must be kept consistent to prevent black/empty bands.

### Fixed

- Replaced coloring logic that could change approved geometry with geometry-locked styling.
- Added prevention and QA for PPT multiply rendering, white seams, and inconsistent artboard/background dimensions.
- Corrected `scripts/audit_svg.py` missing-file argument bug.
- Expanded SVG audit to detect compositing and presentation-risk features.

These are workflow safeguards; individual exports still require the documented QA.

## v1.0

- Original Community workflow remains in Git history and tag `1.0.0`.
