# SVG And Vector Geometry Rules

## Geometry Priorities

1. device structure is correct;
2. geometry is clean and readable;
3. vector remains editable;
4. only then reduce path/anchor count.

## Mechanical Rules

- **Straight stays straight.** Near-straight mechanical edges should not become soft waves.
- **Circle stays circular.** Prefer circle/ellipse/clean arcs for flanges, windows, holes, knobs, and pipe sections.
- **Symmetric stays symmetric.** Preserve deliberate symmetry and repeated spacing.
- **Repeated parts stay regular.** Bolts and repeated ports should share size/orientation unless the source proves otherwise.
- **No thick-paint tracing.** Avoid bulky doubled borders and brush-like black masses.
- **No anchor inflation.** More anchors are not automatically more accurate.

## Cleanup

High-confidence cleanup may:

- remove tiny isolated noise paths;
- simplify obviously over-dense curves;
- standardize nearly horizontal/vertical segments;
- replace clearly circular approximations with clean circles/ellipses;
- remove duplicate coincident edges.

Do not perform aggressive cleanup that alters device identity or functional boundaries.
