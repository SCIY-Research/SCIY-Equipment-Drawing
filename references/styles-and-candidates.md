# Styles And Candidate Generation

## Supported Styles

### Academic Flat / 论文扁平风
Restrained colors, clear regions, little shading, suitable for papers and combined apparatus figures.

### Product Reference / 标准产品参考风
Clean white background, stronger volume/material cues, suitable as a high-fidelity master before line extraction.

### Technical Illustration / 技术插画风
Engineering-manual character, geometric construction, restrained material cues, especially suitable for mechanical/chemical/safety equipment.

### Lineart First / 线稿优先风
Minimal tonal complexity, high structural readability, optimized for later vectorization.

## Candidate Count

Supported: 1 / 2 / 4. Maximum 4 in v1.1.

If the user provides count, do not ask again. Otherwise ask concisely.

## Controlled Variation

Within one batch, keep constant:

- device identity;
- critical structure;
- main silhouette;
- key dimensions/proportions when known;
- required interfaces and components;
- chosen visual style.

Variation may include:

- small viewpoint changes;
- composition and scale within the canvas;
- local simplification;
- restrained light/shadow organization;
- non-critical edge/detail treatment.

Do not create unrelated device variants just to increase visual difference.

## Style Comparison Mode

Use only when the user explicitly asks to compare styles. Typical four-way comparison:

- Academic Flat × 1
- Product Reference × 1
- Technical Illustration × 1
- Lineart First × 1

Label it as a style comparison, not a normal multi-candidate batch.
