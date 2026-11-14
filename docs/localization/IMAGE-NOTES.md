# 图像文字审查及中文解读原稿

本文件是研发验收记录及供 `wiki/index.html` 使用的中文解读原稿。所有原始 PNG/JPG 保持固定基线原字节，2026-11-14 已用 `view_image` 逐一检查，不只依据文件名推测。

| 原图 | 中文解读和关键文字 |
| --- | --- |
| `assets/logo.png` | 戴眼镜的长发卡通人物正在吃烤红薯；没有需要翻译的可见英文。它是品牌图像，不承载操作步骤。 |
| `docs/guide/images/router.jpg` | 调度员拨动道岔，将机器人车分派到不同入口。`/poteto-mode` 是统一入口；牌上的 `BUG FIX`、`FEATURE`、`INVESTIGATION` 分别是“缺陷修复”“功能开发”“调查”。`SAY THE GOAL` 意为“说明目标”；终端 `playbook: matched` 意为“操作手册：已匹配”。图意是告诉智能体目标，由它选择流程。 |
| `docs/guide/images/understanding.jpg` | 侦探研究蓝图，机器人整理证据。`/how` 对应“如何工作”，`/why` 对应“为何如此”。`TRACE IT FIRST` 意为“先追踪清楚”；终端 `evidence: cited` 意为“证据：已引用来源”。图意是改动前先读懂机制、历史并提供证据。 |
| `docs/guide/images/design.jpg` | 三个机器人各自制作桥梁方案，分别对应 `/architect`、`/arena` 和 `/interrogate`。前景裁判的 `BREAK IT` 意为“尝试击破它”，终端 `candidates: 3` 表示“三个候选方案”。图意是先设计、并行比较，再进行审慎的对抗审查。 |
| `docs/guide/images/verification.jpg` | 飞机真实穿过测试航线，有计时、录像和清单。`PROVE IT` 意为“证明它”；`REAL THING ONLY` 意为“只验证真实产物”；终端 `verify: pass` 表示“验证：通过”，`evidence: captured` 表示“证据：已捕获”。不能用编译成功代替真实行为证据。 |
| `docs/guide/images/overnight.jpg` | 人离开工厂后机器人继续工作并更新日志。`DECISION LOG` 是“决策日志”；`BUILD LOOP ACTIVE` 是“构建循环正在运行”；`DONE = CHECKS PASS` 是“完成 = 检查通过”；`/loop` 是原命令，`agents: 4 running` 表示“四个智能体正在运行”。图意是通过明确完成条件、持续检查和日志支持离开后的自主运行。 |
| `docs/guide/images/recipes.jpg` | 机器人按配方做菜，人检查成品。上方 `/how`、`/tdd`、`/loop` 保留为命令；`RECIPES` 是“配方”，`FOCUS BUILD REPEAT` 是“专注、构建、重复”，终端 `context: guarded` 表示“上下文：受到保护”。图意是复用明确提示词与工程习惯，反复执行并检查。 |

图片中的终端背景代码是装饰，关键可读文字已在上表解读；图中没有正文之外的必要流程或隐藏安装指令。命令保持英文，方便读者与正文和技能名称对应。

## SVG 可视检查

六份 `mirror-assets/*.svg` 的自然语言可见文字、`title` 和 `desc` 已翻译；pstack、Plannotator、Inbox、产品名、仓库路径、安装命令、链接和元素 ID 保持原样。两个 header 说明上游 `cursor/plugins/pstack` 同步至 `backnotprop/pstack`，再供多个智能体运行环境安装；赞助卡分别标注“赞助方”和“立即试用”。

使用系统已安装的 Swift/AppKit 离线渲染，命令为：

```bash
rtk proxy swift docs/localization/render-svg.swift mirror-assets/header-dark.svg mirror-assets/header-light.svg mirror-assets/sponsor-inbox-dark.svg mirror-assets/sponsor-inbox-light.svg mirror-assets/sponsor-plannotator-dark.svg mirror-assets/sponsor-plannotator-light.svg
```

实际结果：六图全部生成，header 为 960×244，赞助卡为 470×128；已逐图查看 `svg-previews/*.png`，中文标签在原图框内，无溢出、无中文裁切。保留图形布局、路径、颜色、字号、动画及关系，仅替换可翻译文本。

验证限制：Quick Look 缩略图生成器会裁去 header 右侧，已弃用其结果，由 Swift 结果覆盖。AppKit 的 SVG 渲染不完全支持原图中的八位十六进制半透明色，例如 `#5537eb14` 会呈黑底；这不由翻译引起，未修改上游图形或颜色。PNG 证据主要用于确认中文字形与边界，不把该渲染器效果当作浏览器兼容性结论。


## 最终浏览器复核补充

随后使用本机已安装 Ego Lite（Chromium）实际打开全部六份本地 SVG，按原始尺寸渲染，并核对所有 text 的客户端边界：全部处于视口内。逐图查看后确认中文无溢出或裁切，原有半透明颜色正常。`svg-previews/*.png` 已由这些实际浏览器截图覆盖，最终可视证据以浏览器结果为准。详见 `REVIEW-wiki.md` 和 `visual-check/svg-browser-check.json`。因此早期 AppKit/Quick Look 限制不影响最终浏览器可视检查结论。
