# SCIY v1.1 — Codex Acceptance Scenarios

Manual behavioral tests; they do not prove software operations have run.

## Simple invocation

“$equipment-image-drawing 画一个离心机”

Pass: recognize the device task, offer missing choices concisely, and avoid inventing a full experimental system.

## Controlled candidates

“根据自建设备照片，Technical Illustration，4 个候选。”

Pass: user evidence has priority; same device/style with controlled variation; disclose uncertainty rather than substituting a generic device.

## Geometry lock and export

“给已确认 LINEART 上色，输出可编辑 AI 和 PPT 兼容 SVG。”

Pass: no retrace, moved anchors, or replacement geometry during coloring; LINEART/HIGHLIGHT/SHADOW/COLOR_BASE layers; upper-left default lighting. Check geometry integrity separately from actual PPT insertion: colors, full artboard, white seams, and connections.

Fail: raster passed off as vectors, changed approved geometry, or PPT compatibility claimed from browser preview alone.
