---
name: equipment-image-drawing
description: Reconstruct editable scientific-equipment illustrations from photos, papers, CAD references, or existing images using evidence-aware research, controlled AI candidate generation, geometry-locked coloring, Adobe Illustrator vectorization, and separate editable/PPT-compatible exports.
---

# SCIY Equipment Drawing v1.1

Create technically credible, editable scientific-equipment illustrations. Default to one isolated device. Do not expand into a complete experimental workflow unless the user asks for one.

## Core Principle

Treat the workflow as four distinct stages:

1. **Understand the real device** — route the input, research only when useful, and identify geometry-critical evidence.
2. **Generate candidate masters** — choose a visual style, generate controlled alternatives, and select one geometry authority.
3. **Vectorize without changing identity** — line master to Illustrator, Expand to true vectors, then lock approved geometry.
4. **Style the locked geometry** — color, shadow, highlight, and compatibility export must not silently redraw the device.

Read the matching reference file before each stage:

- [references/routing-and-research.md](references/routing-and-research.md)
- [references/styles-and-candidates.md](references/styles-and-candidates.md)
- [references/prompts.md](references/prompts.md)
- [references/geometry-rules.md](references/geometry-rules.md)
- [references/illustrator.md](references/illustrator.md)
- [references/coloring-and-lighting.md](references/coloring-and-lighting.md)
- [references/ppt-svg-compatibility.md](references/ppt-svg-compatibility.md)
- [references/quality-review.md](references/quality-review.md)

## Route The Input

- **Public/standard equipment:** user evidence first; official model pages, manuals, dimensions, and multi-view images may supplement missing structure.
- **Self-built/modified equipment:** user photos, dimensions, sketches, and explanations are authoritative. Internet material may support only standard subcomponents unless the user explicitly says otherwise.
- **Mixed system:** separate standard commercial components from custom geometry, then recombine.
- **Existing approved line art:** treat it as the geometry authority.

Use a **soft gate**. Unless the source is genuinely unusable, continue and disclose uncertainty rather than refusing. Ask only for information that would materially improve fidelity.

## Visual Style And Candidate Count

If the user already specifies style or count, do not ask again. Otherwise offer concise choices.

Supported v1.1 styles:

1. `Academic Flat` / 论文扁平风
2. `Product Reference` / 标准产品参考风
3. `Technical Illustration` / 技术插画风
4. `Lineart First` / 线稿优先风

Candidate count: **1 / 2 / 4**, maximum 4.

Default candidate behavior is:

> same device + same chosen style + controlled variation

Do not turn four candidates into four unrelated devices. If the user explicitly asks to compare styles, use Style Comparison Mode instead.

Candidates are **AI master candidates**, not final AI/SVG deliverables. Normally select one candidate before vectorization.

## Candidate Selection

Prefer the candidate with:

1. correct device identity;
2. faithful critical structure;
3. coherent proportions and interfaces;
4. clean geometry suitable for line extraction;
5. only then visual polish.

Do not choose a prettier candidate that invents or removes functional parts.

## Line Master And Vectorization

After candidate selection:

1. derive a clean line master from the selected geometry;
2. preserve critical components, supports, interfaces, windows, controls, and functional internals;
3. use Illustrator Black and White Image Trace with `Ignore White`, then `Expand`;
4. validate that AI/SVG contain editable vector objects and zero embedded raster images where vector output is promised.

Image Trace may produce closed filled contours rather than centerline strokes. That is acceptable. Do not spend unlimited effort converting everything to centerline strokes.

## Geometry Lock

Once a line/vector result is approved, it becomes the **geometry authority**.

During coloring and lighting, do not:

- Image Trace again;
- Expand again;
- Simplify approved paths;
- regenerate the device;
- move anchors or control handles;
- replace approved geometry with a newly traced color image.

Coloring is a **style operation**, not a geometry-generation operation.

Record a geometry signature before and after coloring when practical. Use [scripts/geometry_signature.py](scripts/geometry_signature.py) for SVG-based checks.

## Coloring And Lighting

Preferred layer order:

```text
LINEART        top, locked
HIGHLIGHT
SHADOW
COLOR_BASE
```

Fill existing closed regions or geometry-matched copies. Use restrained scientific-illustration colors. Add volume with editable vector shading, not by redrawing the equipment.

Preferred light source: upper-left unless the user specifies otherwise.

Use gradients/opacity/vector clipping only when needed. Avoid heavy blur, raster effects, or photorealistic texture in the default technical workflow.

## SVG Geometry Rules

Mechanical geometry should stay mechanical:

- straight stays straight;
- circle stays circular;
- symmetric stays symmetric;
- repeated fasteners should remain regular;
- use clean arcs, circles, ellipses, rectangles, rounded rectangles, and deliberate Bézier curves;
- avoid thick-paint tracing, duplicated black borders, wobbly edges, and unnecessary anchors.

Structure correctness outranks path-count reduction.

## Two Export Targets

v1.1 distinguishes two deliverables:

### Editable Master

Use the `.ai` project file as the continuing-edit master. Preserve editable layers and geometry-lock evidence.

### Presentation SVG

Create a separate SVG for PowerPoint/presentation use when required. Do not overwrite the editable master.

PowerPoint-compatible SVG should avoid relying on unsupported or fragile compositing behavior such as `mix-blend-mode: multiply`, masks, or effects that render differently in PowerPoint. Preserve the actual visible outline rather than replacing it with crude COLOR_BASE strokes.

Read [references/ppt-svg-compatibility.md](references/ppt-svg-compatibility.md) before producing presentation SVG.

## Non-Negotiable Invariants

- Preserve equipment identity and experiment-critical geometry.
- User-supplied real-device evidence outranks generic internet references.
- Keep the device fully visible with safe margins unless the user requests a crop.
- Do not silently add labels, arrows, pipes, sensors, or fittings.
- Do not mechanically delete every white fill; some encode valid structure/negative space.
- Do not claim a centerline-stroke result unless inspection proves it.
- Do not report success from code generation alone. Required software operations must actually run and exported previews must be inspected.
- Never overwrite the editable engineering master with a presentation-compatibility conversion.

## Recommended Naming

Use the actual Chinese equipment name plus role and ASCII version marker:

```text
设备名称_原始参考_v01.png
设备名称_候选01_v01.png
设备名称_选定母版_v01.png
设备名称_线稿母版_v01.png
设备名称_线稿_v01.ai/.svg/_预览.png
设备名称_技术插画风_上色_v01.ai/.svg/_preview.png
设备名称_技术插画风_上色_v01_PPT兼容.svg
```

Preserve user-requested filenames when explicitly provided.

## Completion Report

Report only verified facts relevant to the requested deliverable, including where applicable:

- source type and research decision;
- chosen style and candidate count;
- selected candidate and why;
- Illustrator version and Image Trace/Expand status;
- path/image counts and vector validation;
- geometry-lock result;
- coloring/shadow/highlight method;
- editable-master vs presentation-SVG status;
- PowerPoint appearance check, including crop, color, white seams, component connections, and full artboard.

Use [scripts/audit_svg.py](scripts/audit_svg.py) for SVG audits and [scripts/geometry_signature.py](scripts/geometry_signature.py) for repeatable geometry checks.
