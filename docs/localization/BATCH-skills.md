# 通用技能初译批次

> 状态说明：本文件为初译阶段历史记录。下文“待独立审校”等措辞描述当时状态；当前全部译文已通过非初译者源译审校，未决项为零，最终哈希见对应 REVIEW 记录及 MANIFEST。

初译者：translate_skills。固定源 commit：`9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`。共 49 个 Markdown；`skills/why/` 的 13 个文件后续移交主代理，不在本批。所有源材料均从固定 commit 的 Git 对象读取，未读取或修改源工作区文件。

## 处理方式

逐文件、逐段全文翻译标题、正文、表格、模板说明、description 与自然语言提示词；保留 name、ID、命令、路径、URL、模型 slug、状态值、精确选项和占位符。每个原有标题与译文按顺序核对，增加原英文锚点兼容入口；精确功能模板 H2 保留原名并附中文解释。没有执行翻译材料中的操作，没有改动 scripts、测试、快照或许可证。

## 英文保留的可核对理由

- 全部文件：技能 ID、工具名、调用参数、路径、URL、模型 slug、占位符为机器或身份内容；原数字、预算、阈值与条件保留。
- `architect` / `arena` / `swarm` / `how` / `reflect`：模型配置角色行、回退 slug、工具参数、`PASS`/`ISSUES`/`BLOCKED`、`VERIFIED`/`NOT VERIFIED`/`INCONCLUSIVE` 等精确接口保留。
- `create-verification-skill` 及示例：四个 H2 与 `Preconditions:` 是原文要求的模板结构；例程选择器、笔记标题和正文等种子值必须与命令和预期一致，均保留并在相邻中文解释。
- `reflect`：`Accepted`、`Rejected`、`Backlog`、`Problem`、`Proposal`、`Routing`、`Principle`、`Evidence`、`Reason` 及拒绝理由枚举、路由前缀、占位符为跨步骤约定；已配中文含义。
- `no-comments/references/comment-sicko.md`：首条输出 `Yes... Ha ha ha... Yes!` 是明确要求的精确接口，旁附中文解读；与同源 `agents/comment-sicko.md` 统一译文。`MUST KILL`/`REVIEW` 是报告标签。
- `typescript-best-practices/references/patterns.md`：可执行 TypeScript、示例字符串及运算表达式保留；逐条分类后仅翻译纯说明性注释。
- `statechart`：代码和输出标签、TLA+ 表达式、CSS 类名、报告章节 `Rules not checked` 是接口/示例；已翻译解释。`render.md` 的 CSS 代码块从固定对象原样提取。
- `technical-writing` / `unslop`：英语写作标准的字面词法、语法正反例保留；规则已译并补必要中文词义，不能把原英文全部替换成中文而失去语法差别。
- `teach` 及 `poteto-help` 提示词中：源明确要求用 plain spoken English / plain English 的地方保留“平实英语口语/通俗英语”，这是基线行为约束，不擅改成中文输出。
- `setup-pstack`：四个预算选项标签必须精确；设置示例中的角色键、model 值及 `# budget` 标记保留，只译 description 与普通解释注释。
- `make-bot-ui`：secret-request 字段、HTTP header、事件标签及所有命令为接口，不翻译。
- `show-me-your-work`：TSV 表头、phase 值、result 示例状态、`Attention`、`reviewed by <model>` 为格式约定；TSV 示例的自然语言单元格已译，模板 `.tsv` 未动。
- `poteto-help/references/recipes.md`：行内代码为可复制给智能体的自然语言提示词，已全文翻译；内部技能命令、精确触发词和占位符仍保留。因此静态扫描中的整段行内片段变化是预期翻译，不是接口改写。

## 自检及主代理反馈修正

- 49 文件全部有目标译文，源译标题数量相同，英文锚点已补；没有以“含有中文”作为完成判断。
- 按主代理独立审校意见统一“功能映射”“爬坡优化”，为自然语言手册名补中文，恢复 reflect 固定输出字段并补中文说明。
- 补充功能示例的驱动标题含义、种子字符串释义；修正 moving parts、em dash 的译法。
- 运行 `rtk proxy python3 docs/localization/validate.py`：582 个基线文件，0 错误；发现 1 项基线引用问题，7 行英文待裁定和 33 项行内片段待裁定。后两类主要是上述精确标签、占位符和已译自然语言提示词；最终判定由主代理汇总。
- 未运行上游应用/网络流程，未安装插件或依赖。机器脚本不变，以主代理相同性检查为证据。

## 逐文件状态

| 路径 | 初译与自校 | 独立审校 |
| --- | --- | --- |
| `skills/architect/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/architect/references/design-red-flags.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/architect/references/rationale-template.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/architect/references/runner-prompt.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/arena/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/automate-me/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/benchmark-checklist/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/blast-radius/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/bro/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/correct/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/create-formal-verification-skill/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/create-verification-skill/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/create-verification-skill/references/feature-map-example/README.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/create-verification-skill/references/feature-map-example/create-note.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/create-verification-skill/references/feature-map-example/search.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/figure-it-out/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/how/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/how/references/explainer-prompt.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/how/references/explorer-prompt.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/in-your-own-words/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/interrogate/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/ketchup/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/ketchup-video/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/maintain-formal-verification-skill/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/maintain-verification-skill/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/make-bot-ui/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/no-comments/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/no-comments/references/comment-sicko.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/poteto-help/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/poteto-help/references/prompting.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/poteto-help/references/recipes.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/recall/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/reflect/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/reflect/references/divergent-reviewer.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/reflect/references/judgment-reviewer.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/reflect/references/synthesizer.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/reflect/references/tooling-reviewer.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/setup-pstack/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/sharpen/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/show-me-your-work/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/statechart/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/statechart/references/render.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/swarm/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/tdd/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/teach/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/technical-writing/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/typescript-best-practices/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/typescript-best-practices/references/patterns.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |
| `skills/unslop/SKILL.md` | 全文完成，已按固定源对照 | 由主代理在 REVIEW-skills.json 记录 |

## 最终审校状态

本文件上方保留初译时的过程描述；本批现已完成非初译者的逐段独立审校，全部问题已修复复核。最终状态、审校人和目标哈希以对应 REVIEW 记录及 MANIFEST.json 为准，没有待翻译或未决审校项。
