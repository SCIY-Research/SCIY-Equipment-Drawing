# SCIY Equipment Drawing

Convert one laboratory or research-equipment reference image into a clean scientific illustration.

## Workflow
Reference Image → Structure Analysis → Line Art → Flat-Color Scientific Illustration → Adobe Illustrator Vectorization → SVG / AI / PNG

## Community v1.0 includes
- Structure-aware device drawing
- Line-art generation
- Flat-color scientific rendering
- Basic Adobe Illustrator vectorization workflow
- Editable SVG / AI outputs
- Basic quality control
- Versioned output naming


## Drawing / editing software

At the start of each new task, SCIY asks which route to use:

- **Adobe Illustrator — strongly recommended** for the fastest and most direct vector workflow.
- **PowerPoint / WPS Presentation** when PPT editability is preferred; this route is usually slower and requires more automation steps.
- **PNG / SVG only** when no external drawing software should be used.

Illustrator is recommended, not mandatory.

## Typical use cases
- Scientific figures
- Experimental setup illustrations
- PPT / poster assets
- Editable equipment graphics
- Reusable research-illustration workflow

## Usage
Place this repository where your coding/agent environment can read `SKILL.md`, then ask it to follow the SCIY workflow on a single equipment reference image.

Example prompt:
> Use the SCIY Equipment Drawing skill on this laboratory equipment reference. Identify the key structure first, create a clean white-background line-art version, verify geometry, generate a flat-color version with the same geometry, then complete the basic Adobe Illustrator vectorization workflow and export editable SVG/AI files.

## Project position
SCIY Equipment Drawing is the first public skill from **SCIY科研站**.

The Community edition contains a complete basic workflow. Future private/advanced production workflows may add larger equipment-specific rule libraries, advanced automation, batch processing, detailed Illustrator tuning, and commercial delivery tooling.
