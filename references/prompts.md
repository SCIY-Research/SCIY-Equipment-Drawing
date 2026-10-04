# Master Image Prompts v1.1

## Candidate Master

Use the strongest available device evidence. State critical parts explicitly. Require:

- one isolated scientific device, centered and fully visible;
- correct device identity and technically plausible construction;
- preservation of all function-critical components;
- no invented fittings, sensors, labels, arrows, or decorative hardware;
- clean background and safe margins;
- geometry suitable for later line extraction.

For multiple candidates, generate controlled variations of the same device and same chosen style. Do not treat candidate count as permission to redesign the equipment.

## Line Master From Selected Candidate

Use the selected candidate as the geometry authority. Require:

- identical viewpoint, crop, silhouette, component count, interfaces, supports, windows, controls, and proportions;
- pure white background;
- precise dark-gray/black contours with moderate line density;
- no color fill, shading, texture, hatching, labels, arrows, or surrounding apparatus;
- smooth boundaries suitable for Illustrator Black and White Image Trace;
- no large black masses unless they are genuinely part of the visible structure.

For mechanical devices, explicitly require straight edges to remain straight, circular features to remain regular, repeated fasteners to remain consistent, and symmetrical structures to remain symmetrical.

## Coloring Prompt / Instruction

Do **not** regenerate the device. Coloring begins only after approved geometry exists.

Use the existing vector geometry as authority and apply:

- restrained base fills;
- optional low-opacity vector shadow/highlight layers;
- material distinction only where useful;
- geometry-preserving region fills.

Do not use color Image Trace as a replacement for approved line geometry.

## Visual QA Before Illustrator

Reject/regenerate a master when it has:

- cropped parts;
- missing supports or interfaces;
- impossible connections;
- unexplained extra fittings;
- changed window/port count;
- inconsistent perspective;
- wobbly mechanical edges;
- distorted circles/flanges;
- severe asymmetry in repeated parts.
