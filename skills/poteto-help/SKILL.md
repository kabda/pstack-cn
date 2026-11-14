---
name: poteto-help
description: 引导用户完成 pstack 设置、使用 /poteto-mode，并为任务选择技能、操作手册或原则。输入 /poteto-help 并附问题。
disable-model-invocation: true
---

<a id="poteto-help"></a>

# Poteto 帮助

回答用户关于 pstack 的问题，给一份可以发送的提示词，并链接答案来源文件。对于帮助问题，不要开始执行。用户问的是怎么做，而 pstack 运行会实际消耗 token，因此让他们自己发送提示词。

“用 pstack 修这个缺陷”这类要求工作的信息，不是帮助问题。阅读 [`poteto-mode`](../poteto-mode/SKILL.md)，按其要求完成工作，并提醒一次：Custom Mode（自定义模式）可以让它持续生效。

本文件把问题映射到持有答案的技能和指南页面，细节由那些文件负责。引用前先读目标文件；它与本映射不一致时，以它为准。这里的链接指向已安装插件，用户可能无法打开，因此提供文件公开副本：`https://github.com/cursor/plugins/blob/main/pstack/` 加该文件路径。

<a id="find-out-what-they-need"></a>

## 判断用户需要什么

从消息与对话推断需求。已明确情境，例如“哪个技能能审查 PR？”，直接转对应章节。仍不清楚时，只问一个多选题，选项如下，然后只回答其选择的章节：

- 完成设置
- 用 `/poteto-mode` 开始任务
- 为特定情境选择技能
- 纠正出错的运行
- 将 pstack 定制为自己的方式

检查会改变答案的状态，只有确实影响答案时才提：

- 没有 pstack 设置文件（Cursor 的 `~/.cursor/rules/pstack-models.mdc`、Claude Code 的 `~/.claude/rules/pstack-models.md`、其他环境的 `~/.agents/pstack-models.md`），表示该用户尚未运行 `/setup-pstack`，各角色都用默认模型。
- 项目没有 `verify-*` 技能或其他应用运行工具，表示智能体没有脚本化方式驱动应用。问题涉及证明改动有效时，提及 `/create-verification-skill`。
- 项目没有形式化验证技能，表示没有检查超出测试范围的性质。问题涉及竞态、不变量或测试很少到达的案例时，提及 `/create-formal-verification-skill`。已有技能，但覆盖代码在记录的上次同步 commit 之后变化时，若问题触及该代码，提及 `/maintain-formal-verification-skill`。

模型规则缺失且影响答案时，询问是否现在为各角色选择模型及推理预算。新用户、设置或费用问题，或答案依赖运行哪些模型时，都算影响。每聊天最多问一次。需求也不清时，把两个问题一起问。提供两个选项：

- 现在：给用户输入 `/setup-pstack`，同时回答原问题。
- 稍后：回答原问题，再加一行说明，运行 `/setup-pstack` 前各角色继续使用默认模型。

<a id="get-set-up"></a>

## 完成设置

1. 聊天中输入 `/add-plugin pstack` 安装，或从侧栏 Customize（自定义）安装。Cursor 外运行 `npx skills add backnotprop/pstack`，选择技能。
2. 运行 [`/setup-pstack`](../setup-pstack/SKILL.md)。它询问推理预算、为各角色映射模型并写规则，规则应用于新聊天。随后各提议一次生成项目验证技能和形式化验证技能，已有则跳过。
3. 用 `/poteto-mode` 开始真实任务，附目标和能通过或失败的检查。

安装后，直到用户调用技能才会产生作用。只有 `/setup-pstack` 会根据用户措辞自动加载。[README](../../README.md) 和[指南第 1 页](../../docs/guide/01-setup.md)提供细节。按 [`references/prompting.md`](references/prompting.md)，提议一起组织第一份提示词。

担心费用时，说明 token 花在哪里、如何少花。pstack 会额外消耗 token 在子代理和审查小组上。重跑 `/setup-pstack`，选择更小预算或更便宜模型。角色设为 `auto` 或 `inherit-parent` 会使用聊天模型，聊天使用 Auto 或低价模型时可节省 token。面板列表越短，子代理越少，每个条目一个。把 `/poteto-mode` 留给需要严谨处理的工作。

pstack 为 Cursor 构建，也支持在 Claude Code 中先 `/plugin marketplace add cursor/plugins`，再 `/plugin install pstack@cursor-plugins` 安装。那里每个命令加 `pstack:` 前缀，例如 `/pstack:poteto-mode`。[Claude Code 适配器](../../docs/harness/claude-code.md)映射 Cursor 名称；需要 Cursor 专有能力（例如 Bugbot 或 Automations）的步骤跳过，附一行说明。

本镜像技能也可通过 `npx skills add backnotprop/pstack` 用于其他智能体运行环境，包括 Claude Code、Codex、Pi、OpenCode 等。[`poteto-mode`](../poteto-mode/SKILL.md) 的运行环境部分，将 Cursor 的子代理、提问、记录和设置路径映射为各环境自身形式。Custom Modes 是 Cursor 功能。

<a id="start-a-task-with-poteto-mode"></a>

## 用 `/poteto-mode` 开始任务

`/poteto-mode` 根据任务选择操作手册，将步骤复制到待办清单，再按步骤需要调用其他技能。跳过步骤仍留在清单，标成 `skip: <reason>`。好的提示词说明目标及完成判断，不列技能，因为手写顺序容易丢弃或重排操作手册会保留的步骤。帮助写提示词前，先读 [`references/prompting.md`](references/prompting.md)。[指南第 2 页](../../docs/guide/02-poteto-mode.md)有示例。

`/poteto-mode` 是否持续生效，取决于用户如何启动：

- 在 `/poteto-mode` 上按 Enter，只给一条消息附加技能。聊天推进后影响会减弱。
- Mac 的 Option+Enter、Windows 的 Alt+Enter，或技能条目的 Use as Mode（用作模式），会创建 Custom Mode。用户退出模式前，每回合都保留在上下文，闲聊回合则不介入。
- Cursor 文档说明 Agents Window（智能体窗口）和 CLI 支持 Custom Modes。其他位置，每个新任务都以 `/poteto-mode` 开头。

谈及此项时链接 [Cursor 技能文档](https://cursor.com/docs/skills)。聊天中途说“new task”（新任务），会让模式重新匹配操作手册。`/poteto-mode` 已为其步骤启动的子代理使用 `poteto-agent`。自建子代理若想使用相同风格，以 `subagent_type: "poteto-agent"` 启动。

<a id="pick-a-skill"></a>

## 选择技能

默认答案是 `/poteto-mode`，它会在步骤需要时运行大多数其他技能。用户希望某部分比操作手册更多或更少时，直接点名技能。推荐前先读技能，并给一个提示词示例。

| 用户希望 | 技能 |
|---|---|
| 严谨地完成任何非简单任务 | [`/poteto-mode`](../poteto-mode/SKILL.md) |
| 开始前确认智能体理解目标和问题 | [`/in-your-own-words`](../in-your-own-words/SKILL.md) |
| 发送前把提示词改得更深而非更大：顶尖专业人士会补什么、用哪些原始材料和方法、如何外部检验；返回提示词，不执行任务 | [`/sharpen`](../sharpen/SKILL.md) |
| 了解代码现在如何工作，或新代码应放哪里 | [`/how`](../how/SKILL.md) |
| 了解代码为什么这样设计，或某个数值从何而来 | [`/why`](../why/SKILL.md) |
| 通过通俗讲解理解改动或子系统 | [`/teach`](../teach/SKILL.md) |
| 回顾自己近期在某主题上的工作 | [`/recall`](../recall/SKILL.md) |
| 用通俗话和小图示了解本聊天自上一条消息以来的变化，逐项列出等待事项，仅凭回复即可决定 | [`/ketchup`](../ketchup/SKILL.md) |
| 像 `/ketchup` 一样补进展，但用简短带字幕幻灯片视频，视频下方文字列出待决策事项 | [`/ketchup-video`](../ketchup-video/SKILL.md) |
| 了解小型 diff 可能破坏哪些外部内容 | [`/blast-radius`](../blast-radius/SKILL.md) |
| 编写跨函数边界的代码前确定类型和模块结构 | [`/architect`](../architect/SKILL.md) |
| 对同一任务尝试多次，合成最佳结果 | [`/arena`](../arena/SKILL.md) |
| 以云端智能体按分片并行检查，或竞赛 | [`/swarm`](../swarm/SKILL.md) |
| 让不同模型审查 diff 并尝试破坏它 | [`/interrogate`](../interrogate/SKILL.md) |
| 有低成本本地测试时先测试再修缺陷 | [`/tdd`](../tdd/SKILL.md) |
| 对 `.ts` 或 `.tsx` 工作应用 TypeScript 规则 | [`/typescript-best-practices`](../typescript-best-practices/SKILL.md) |
| 审查前由没有写过注释的审查者去除注释 | [`/no-comments`](../no-comments/SKILL.md) |
| 清除文字中的 AI 痕迹 | [`/unslop`](../unslop/SKILL.md) |
| 按标准写文档、RFC、README、PR 描述或提交消息 | [`/technical-writing`](../technical-writing/SKILL.md) |
| 用通俗语言重新听一遍上一条回复 | [`/bro`](../bro/SKILL.md) |
| 给智能体脚本化驱动应用并证明行为的方法 | [`/create-verification-skill`](../create-verification-skill/SKILL.md) |
| 使验证技能和功能映射重新与应用一致 | [`/maintain-verification-skill`](../maintain-verification-skill/SKILL.md) |
| 形式化验证竞态、不变量或测试难覆盖的性质 | [`/create-formal-verification-skill`](../create-formal-verification-skill/SKILL.md) |
| 覆盖代码变化后恢复形式化验证同步，并判断失败属于漂移还是缺陷 | [`/maintain-formal-verification-skill`](../maintain-formal-verification-skill/SKILL.md) |
| 以 TLA+ 模型检查过的图，向 PM 或设计师展示用户所见，并给出到达每个违规状态的最短路径 | [`/statechart`](../statechart/SKILL.md) |
| 报告性能数值或据此行动前核查测量 | [`/benchmark-checklist`](../benchmark-checklist/SKILL.md) |
| 执行大型、横切改动，或人离开后回来审查的工作 | [`/figure-it-out`](../figure-it-out/SKILL.md) |
| 执行中保留决策日志，事后审查 | [`/show-me-your-work`](../show-me-your-work/SKILL.md) |
| 为各角色选择模型和推理预算 | [`/setup-pstack`](../setup-pstack/SKILL.md) |
| 把自己的工作习惯转成个人模式技能 | [`/automate-me`](../automate-me/SKILL.md) |
| 把已完成任务的经验落实为技能编辑 | [`/reflect`](../reflect/SKILL.md) |
| 防止智能体在仓库重复同样错误 | [`/correct`](../correct/SKILL.md) |
| 构建按钮能通过 webhook 唤醒 Grok Bot 的页面 | [`/make-bot-ui`](../make-bot-ui/SKILL.md) |
| 找到 pstack 的使用路径 | `/poteto-help` |

相邻技能目录未列入表时，阅读其 frontmatter，按 description 选择。`principle-*` 目录见下面原则部分。

容易混淆的情况：

- `/how` 解释代码做什么，`/why` 解释原因，`/teach` 运行一个或两个并通俗讲结果。
- `/arena` 向每个工作者发相同任务说明并合并优点；`/swarm` 将工作分片或组织竞赛，返回一份报告。
- `/architect` 设计确定后立即实现。加“with checkpoint”（设检查点），才会在写代码前让人审查设计。
- `/interrogate` 审查 diff；`/blast-radius` 找 diff 外的破坏，并证明使改动安全的关键事实。
- `/recall` 重建近期多聊天上下文；`/ketchup` 仅覆盖本聊天自用户上一条消息以来的内容。恢复特定聊天或分支用会话接续（Session pickup）操作手册。
- `/figure-it-out` 设计一次严谨执行。编排（Orchestrate）操作手册管理跨数天、多个 PR 的项目；自主运行（Autonomous run）操作手册把单项任务推进到结束条件。

不属于 pstack 的内容：

- `/deslop`、`control-cli`、`control-ui` 由 `cursor-team-kit` 插件提供。
- `/loop`、`/create-skill` 是 Cursor 内置功能。
- pstack 没有 `/orchestrate` 技能。编排（Orchestrate）是 `/poteto-mode` 的操作手册。斜杠菜单有 `/orchestrate`，说明来自其他插件。

<a id="playbooks-and-principles"></a>

## 操作手册与原则

操作手册是 `/poteto-mode` 内的步骤列表，不是技能，因此没有斜杠命令。在 `/poteto-mode` 中，描述任务即可选定手册，以下短语可直接点名：

- “babysit this pr”或“check on pr 123”运行跟进 PR（Babysit）。它把 PR 推进到可合并并停止；只有用户要求 merge（合并）、land（落地）或 ship（交付） 时才合并。
- “land the stack”运行交付（Shipping）。
- “take over this branch”运行会话接续（Session pickup）。
- “pause safely”运行安全暂停（Pause safely）。
- “full autopilot on this queue”运行 完全自动驾驶（Autopilot-full）；“autopilot, don't merge”运行 PR 栈自动驾驶（Autopilot-stack）。
- “run the eval playbook”运行评估（Eval）。

未使用 `/poteto-mode` 时，“babysit this pr”之类措辞可能转而触发 Cursor 自身完成同类工作的技能。[`poteto-mode`](../poteto-mode/SKILL.md) 的操作手册部分列出所有手册及使用时机。[指南第 6 页](../../docs/guide/06-verify-and-ship.md)涵盖创建、照看和落地 PR。

pstack 没有规划技能。Cursor 的 Plan Mode 可与它配合。跨多个阶段或堆叠 PR 的工作，请 `/poteto-mode` 制定计划，会运行[多阶段计划操作手册](../poteto-mode/playbooks/multi-phase-plan.md)，它只写计划，不实现。设计问题先用原型（Prototype）操作手册或 `/architect` 在代码里确定。

原则是只含一条规则的技能，`/poteto-mode` 会阅读并在回复引用。用户很少直接调用，而是用名称调整方向，例如“应用 prove it works（证明它能工作），展示真实输出”。输入 `/principle-<name>` 仍可按需加载。[指南第 8 页](../../docs/guide/08-principles.md)列出全部原则。

<a id="fix-a-run-that-went-wrong"></a>

## 纠正出错的运行

| 症状 | 修正 |
|---|---|
| 模式几回合后不再生效 | 它以 Enter 启动。改为 Custom Mode，或每个任务以 `/poteto-mode` 开头。 |
| 问题被视为上一任务的下一步 | 说“new task”，或说明本回合不需要模式。 |
| 新模型选择没效果 | `/setup-pstack` 规则应用于新聊天，开一个新聊天。 |
| 费用高于预期 | 见“完成设置”中的费用段落。 |
| 技能没有自动加载 | 只有 `/setup-pstack` 根据用户措辞加载。其他技能由用户输入或 `/poteto-mode` 调用，且模式并不运行每个技能。 |
| 并行智能体相互覆盖 | 每个智能体使用独立 Git 工作树，或使用各自有独立机器的云端智能体。 |
| 通宵运行一直在动却没完成任何事 | `/loop` 需要能通过或失败的检查，而不是时长。见[指南第 7 页](../../docs/guide/07-overnight.md)。 |
| 回复凭构建通过就宣称成功 | 要求真实命令、流程、存储值或性能分析，这是 prove-it-works（证明它能工作）原则。 |

运行偏离时，[`references/prompting.md`](references/prompting.md)有一行式调整指令。[指南第 10 页](../../docs/guide/10-recipes-and-pitfalls.md)有更多陷阱和可复制提示词。

<a id="make-pstack-my-own"></a>

## 将 pstack 定制为自己的方式

- [`/automate-me`](../automate-me/SKILL.md) 从用户自身历史起草个人模式技能，与 `/poteto-mode` 配合。
- 会话后用 [`/reflect`](../reflect/SKILL.md)，将经验落实为需用户批准的技能编辑。
- `/poteto-mode 为 <workflow> 编写技能` 会运行技能编写操作手册。评估操作手册对技能改动做盲测。
- 出问题的技能应在独立 PR 修复，不夹在导致问题的功能工作中。

[指南第 9 页](../../docs/guide/09-make-it-yours.md)逐项介绍。

<a id="reply"></a>

## 回复

先回答问题。最多给一个代码块提示词示例，合适时改编自 [`references/recipes.md`](references/recipes.md)，再链接来源文件。除非用户要求完整地图，否则保持简短。
