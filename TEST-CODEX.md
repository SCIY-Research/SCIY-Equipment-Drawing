# SCIY Community v1.0 — Codex Quick Test

## Test prompt
加载当前目录中的 `SKILL.md`，严格按照 SCIY Equipment Drawing Community v1.0 的工作流处理我接下来提供的一张科研设备参考图。

要求：
1. 在开始绘制前，先询问我选择 Adobe Illustrator、PowerPoint/WPS，还是仅 PNG/SVG；其中明确标注 Adobe Illustrator 为强烈推荐路线；
2. 先识别设备关键结构，不要直接画最终图；
3. 先生成白底线稿；
4. 检查结构是否缺失、错位或凭空增加；
5. 线稿确认后生成同构配色版本；
6. 若选择 Adobe Illustrator，则检测本机 Illustrator；
7. 若选择 Adobe Illustrator 且可用，执行基础矢量化：Image Trace → Expand → 清理 → SVG/AI 导出；
8. 不允许用整张嵌入位图冒充 SVG 矢量；
9. 输出前进行 Final QC；
10. 告诉我哪些结构确定、哪些结构不确定。

## Pass criteria
- 先结构分析，再开始绘制
- 没有凭空添加明显零件
- 线稿为白底、简洁科研风
- 配色图与线稿保持同一几何结构
- 尝试检测并使用 Illustrator
- SVG/AI 输出不是简单“改后缀”
- 对不确定结构进行明确说明
- 最终有 QC 总结

## Fail criteria
- 直接生成漂亮渲染图而跳过线稿
- 结构明显改变
- 配色版与线稿版不是同一设备几何
- 擅自增加接口、阀门、按钮或支架
- 完全忽略 Illustrator 环节
- 仅嵌位图后保存为 SVG
