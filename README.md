# SCIY Equipment Drawing

Turn laboratory equipment photos, reference images, sketches, or text descriptions into clean scientific illustrations.

SCIY uses a structure-first workflow to generate clean line-art and flat-color scientific equipment figures for papers, presentations, and research diagrams.

## Workflow

Reference Image / Photo / Sketch / Text  
→ Structure Analysis  
→ AI Candidate Master Selection<br>
→ Line Art  
→ Structural QC  
→ Illustrator Vectorization<br>
→ Geometry Lock Coloring<br>
→ Vector Shadow / Highlight<br>
→ AI / SVG / PNG

## v1.1: Styles and Candidates

Styles: Academic Flat, Product Reference, Technical Illustration, Lineart First.
Generate **1 / 2 / 4 AI candidate masters**: same device, same chosen style,
controlled variation—not randomly different devices. Style Comparison Mode
compares styles only when explicitly requested.

Public/custom/mixed routing prioritizes user photos and dimensions over generic
references. A Soft Gate permits progress with disclosed uncertainty.

## Geometry Lock Coloring

Confirmed LINEART → Geometry Lock → COLOR_BASE → SHADOW → HIGHLIGHT
→ LINEART on top → Geometry Integrity Check.

Coloring changes visual properties, not approved anchors or paths. Do not retrace
a color master to replace geometry. Straight stays straight; circle stays circular.
Avoid thick/wobbly tracing. Vector lighting defaults to the upper left.
Layers, top to bottom: LINEART (locked), HIGHLIGHT, SHADOW, COLOR_BASE.

## Export Targets

- Editable Master: layered `.ai` for continuing edits.
- Presentation Export: separate PowerPoint-compatible `.svg`; never overwrite
  the master. Avoid dependence on multiply blending or unstable masks.

Geometry Integrity QA is separate from actual PowerPoint insertion/appearance QA:
check color, outlines, white seams, part connections, and complete artboard.
See the included SVG audit and geometry-signature helpers in `scripts/`.

## Usage

Install the repository contents together under the skill folder
`equipment-image-drawing`. Invoke `$equipment-image-drawing` or “画一个离心机”.
The old public `$sciy-equipment-drawing` identifier is supported by installing the
same package under that name and setting SKILL.md frontmatter `name` accordingly;
keep only one installation active to avoid duplicate discovery.

Example: “$equipment-image-drawing 绘制离心机，Academic Flat，2 个候选，
输出可编辑 AI 和 PPT 兼容 SVG，保存到 <PROJECT_DIR>。”

See [SKILL.md](SKILL.md), [CHANGELOG.md](CHANGELOG.md), and
[TEST-CODEX.md](TEST-CODEX.md).

## Drawing Routes

SCIY supports three output routes:

### 1. Adobe Illustrator — Strongly Recommended

Recommended for the fastest and most direct workflow.

Suitable for:
- vector tracing
- path cleanup
- editable SVG
- AI files
- high-quality scientific figure refinement

### 2. PowerPoint / WPS Presentation

Also supported and convenient for researchers who prefer PPT editing.

However, complex equipment usually requires more object reconstruction and layout operations, so this route can be slower and consume more computational resources.

### 3. PNG / SVG Only

No additional drawing software is required.

Suitable for users who only need:
- clean line art
- flat-color figures
- basic SVG output

> Adobe Illustrator is strongly recommended, but it is not required.
