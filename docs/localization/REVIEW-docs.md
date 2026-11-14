# 文档与图像批次独立审校

固定基线：`9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`。初译者为 `translate_docs`，本次独立审校者为 `translate_mode`。审校者未初译或编辑本批译文，问题由主代理修复。

## 方法与覆盖

逐文件从固定 commit 读取源文，与目标正文、列表、表格、frontmatter、模板、提示词、图片 alt 和图表对照，检查信息完整性、条件、否定、权限、次数、数值、步骤顺序、人工门禁及停止边界。不是根据“有中文”判定完成。全部长文完整阅读全文；输出被工具截断的 02-poteto-mode 源文已单独重读，未以截断输出作覆盖证据。

同时核对 URL、占位符、两个插件非 description 字段，六 SVG 的全部元素与属性。所有源 URL 均保留，HTML alt 的变化为预期翻译。JSON 除 description 外字段与源完全相等。六 SVG 只有文字变化，元素属性与源逐项一致。七原始位图逐一查看，与 IMAGE-NOTES 的中文解读交叉核对。

## 逐文件审校

| 文件 | 覆盖与结论 |
| --- | --- |
| `README.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `MIRROR.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `SYNC-LOG.md` | 逐历史条目对照，日期、版本、SHA、编号、结论与限定均保留。 |
| `agents/comment-sicko.md` | 全文对照角色、路径查找、只读边界、保留例外、标记和停止条件。 |
| `agents/poteto-agent.md` | 全文对照角色、路径查找、只读边界、保留例外、标记和停止条件。 |
| `docs/harness/claude-code.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `docs/guide/01-setup.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `docs/guide/02-poteto-mode.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `docs/guide/03-understand.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `docs/guide/04-design.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `docs/guide/05-build-and-clean.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `docs/guide/06-verify-and-ship.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `docs/guide/07-overnight.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `docs/guide/08-principles.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `docs/guide/09-make-it-yours.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `docs/guide/10-recipes-and-pitfalls.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `docs/guide/README.md` | 全文源译对照，含自然提示词、依赖、条件、例外、顺序与完成边界。 |
| `plugin.json` | description 准确自然，其他身份、来源、版本、分类和兼容字段相等。 |
| `.cursor-plugin/plugin.json` | description 准确自然，其他身份、来源、版本、分类和兼容字段相等。 |
| `mirror-assets/header-dark.svg` | 已逐项对照 title、desc、可见文字，保留品牌/URL/命令，查看离线渲染确认中文字形和边界。 |
| `mirror-assets/header-light.svg` | 已逐项对照 title、desc、可见文字，保留品牌/URL/命令，查看离线渲染确认中文字形和边界。 |
| `mirror-assets/sponsor-inbox-dark.svg` | 已逐项对照 title、desc、可见文字，保留品牌/URL/命令，查看离线渲染确认中文字形和边界。 |
| `mirror-assets/sponsor-inbox-light.svg` | 已逐项对照 title、desc、可见文字，保留品牌/URL/命令，查看离线渲染确认中文字形和边界。 |
| `mirror-assets/sponsor-plannotator-dark.svg` | 已逐项对照 title、desc、可见文字，保留品牌/URL/命令，查看离线渲染确认中文字形和边界。 |
| `mirror-assets/sponsor-plannotator-light.svg` | 已逐项对照 title、desc、可见文字，保留品牌/URL/命令，查看离线渲染确认中文字形和边界。 |

## 原样位图与中文解读覆盖

- `assets/logo.png`：逐图查看，并验证目标 SHA-256 等于固定基线；中文解读与图像相符。
- `docs/guide/images/design.jpg`：逐图查看，并验证目标 SHA-256 等于固定基线；中文解读与图像相符。
- `docs/guide/images/overnight.jpg`：逐图查看，并验证目标 SHA-256 等于固定基线；中文解读与图像相符。
- `docs/guide/images/recipes.jpg`：逐图查看，并验证目标 SHA-256 等于固定基线；中文解读与图像相符。
- `docs/guide/images/router.jpg`：逐图查看，并验证目标 SHA-256 等于固定基线；中文解读与图像相符。
- `docs/guide/images/understanding.jpg`：逐图查看，并验证目标 SHA-256 等于固定基线；中文解读与图像相符。
- `docs/guide/images/verification.jpg`：逐图查看，并验证目标 SHA-256 等于固定基线；中文解读与图像相符。

## 发现与主代理处理

| 文件 | 位置 | 问题 | 状态 |
| --- | --- | --- | --- |
| `README.md` | 示例 /tdd implement | 自然提示词 implement 未翻译 | 已修复并复核 |
| `README.md` | 为什么没有规划技能 | 单纯 限定原文无此项，弱化原意 | 已修复并复核 |
| `README.md` | 安装与自定义模式段 | marketplaces、Agents Window 缺少中文释义 | 已修复并复核 |
| `README.md` | 操作手册表及原则表 | 部分手册和原则名仅英文或与叶子标题不一致 | 主代理已统一，已对照叶子标题复核 |
| `MIRROR.md` | 步骤3后 Harness 引用 | 译后章节名称缺中文 | 已修复并复核 |
| `agents/poteto-agent.md` | description 与正文 Principles/Subagents | 译后章节名称缺中文 | 已修复并复核 |
| `docs/guide/01-setup.md` | 第一个任务末段 Agents Window | 缺中文释义 | 已修复并复核 |
| `docs/guide/05-build-and-clean.md` | tdd 与 unslop 示例 | implement 未译；破折号 比 emdashes 范围宽 | 已修复并复核 |
| `docs/guide/07-overnight.md` | 早晨审计段 | 可以提交 将有条件的命令弱化为可选 | 已修复并复核 |
| `docs/guide/08-principles.md` | 原则清单和引导示例 | 11项同义异译需与叶子标题一致 | 主代理已统一，已复核 |
| `docs/guide/09-make-it-yours.md` | 两个 eval 自然提示词 | 做 eval 未提供中文译法 | 已修复并复核 |
| `docs/guide/10-recipes-and-pitfalls.md` | unslop 示例 | 破折号 比 emdashes 范围宽 | 已修复并复核 |

## 保留英文项的独立判断

- pstack、Poteto、Lauren Tan、backnotprop、Comment Sicko、Plannotator 等为身份、品牌和署名；URL 和安装命令仍指原来源。中文译本声明明确正文已翻译，未宣称中文仓库安装已验证。
- mirror:start / mirror:end 整条同步注释受保护，包括其英文与 unchanged；README 开头已解释其为英文基线事实。
- CLI 命令、技能/Agent ID、模型 slug、路径、配置键、schema、keywords/tags、数值、占位符保留。MIRROR 中英文提交说明在可复制上游命令内，非本次提交，不执行。
- marketplace 界面选项、预算/状态值、Launch/Doctor/Drive/Evidence/Cleanup/Helpers、Accepted/Rejected/Backlog、Skipped in Claude Code 等是精确界面、约定标题或输出标签，译文提供中文解释。
- Comment Sicko 首次输出 Yes... Ha ha ha... Yes!，以及 MUST KILL、REVIEW、IMPORTANT 等精确输出或检索线索原样，语义已有译解。
- Markdown 原英文锚点与 Mermaid 语法、节点 ID 保留；图表展示标签中文。SVG 产品名、仓库路径与命令保留。
- 原始位图英文不改，IMAGE-NOTES 已完整解读关键内容。亲自查看七图后，确认无遗漏关键操作信息。

## 可视检查与限制

独立查看六份 `docs/localization/svg-previews/*.svg.png`，中文可读且无溢出或裁切，图形关系未改。此结果来自本机 AppKit 离线渲染，不等于浏览器渲染通过。其半透明色支持限制已如实记录在 IMAGE-NOTES。未运行插件安装、上游同步、自动化、真实服务、PR 或提交操作。

全部问题已由主代理修复，并经本审校者复核关闭。最终文件哈希记录在 REVIEW-docs.json，审校结论为通过，无未解决问题。后续译文变更需复核并更新哈希。

## 最终语言约束复核

主代理最终审计发现两份相同提示词将 `in plain english` 译成“以通俗语言”，遗漏了要求使用英语的约束。已对照固定 Git commit `9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6` 的 `docs/guide/02-poteto-mode.md` 源第 64 行与 `docs/guide/10-recipes-and-pitfalls.md` 源第 18 行，复核当前目标第 72 行、第 24 行均为“以通俗英语”，与原文语言要求一致。只更新 REVIEW-docs.json 中这两个目标文件的 SHA-256，其他审校记录和文件锁保持原样。此问题已关闭，无未决项。
