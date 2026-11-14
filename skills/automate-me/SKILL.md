---
name: automate-me
description: "用于 automate me、create/update/refresh my -mode skill（创建、更新或刷新个人模式技能）、turn/capture my preferences or working style into a skill（将偏好或工作风格转成技能），或希望智能体按用户方式工作时。通过 create-skill + unslop 起草或修订个人 -mode 技能，可选从近期对话获取新证据。"
disable-model-invocation: true
---

<a id="automate-me"></a>

# 将我的工作方式转为技能

引导用户把工作约定变成智能体会遵循的技能。输出一个为用户定制的 `-mode` 技能，例如 `jay-mode`、`priya-mode`。

本技能编排三项其他工作：内联历史挖掘（第 1 步）、运行环境的技能编写技能（编写），以及 **unslop** 技能（文字规范）。它负责安排顺序，不替代这些工作。

技能编写技能是 Cursor 内置 `create-skill`，或 Anthropic 的 `skill-creator`。两者均无时，遵循 agentskills.io 的 Agent Skills 格式。下文“`create-skill`”指实际采用的这一工具。

<a id="flow"></a>

## 流程

<a id="0-check-for-an-existing-skill"></a>

### 0. 检查现有技能

在运行环境的技能目录递归查找与用户标识匹配的 `*-mode/SKILL.md`。项目目录：`.cursor/skills/`（Cursor）、`.claude/skills/`（Claude Code）、`.pi/skills/`（Pi）、`.agents/skills/`（Codex、OpenCode 等）。用户目录：`~/.cursor/skills/`、`~/.claude/skills/`、`~/.pi/agent/skills/`、`~/.codex/skills/`、`~/.config/opencode/skills/`、`~/.agents/skills/`。模式技能可以位于个人分类目录（`<skills>/<handle>/`），不一定在顶层。如果存在，除非用户已经说“更新我的技能”或类似表达，否则用结构化提问工具（Cursor 的 `AskQuestion`、Claude Code 的 `AskUserQuestion`、OpenCode 的 `question`）确认意图：

- 更新现有技能（重复运行的默认选项）
- 从头开始（少见，先问原因再做）

更新模式会改变后续流程：
- 第 1 步只挖掘上次编辑技能以来的历史（`git log -1 --format=%cI <path>`）。
- 第 2 步问变化或缺失什么，而非从零问要捕获什么。
- 第 4 步原地编辑现有文件。保留用户未否定的章节，按新证据修订其他章节，只有确实新规则才新增章节。

<a id="1-mine-their-history"></a>

### 1. 挖掘历史

展开并行前定位当前工作区记录，只使用该工作区目录。不要跨每个项目目录搜索，否则会跨越工作区边界，读取无关项目的私人聊天。位置取决于运行环境：

- **Cursor：**系统提示词指定 `~/.cursor/projects/` 下该工作区的 `agent-transcripts/` 目录。
- **Claude Code：**`~/.claude/projects/<slug>/*.jsonl`，`<slug>` 将工作区路径所有非字母数字字符改为“-”。
- **Pi：**`~/.pi/agent/sessions/--<slug>--/*.jsonl`，`<slug>` 去掉工作区路径开头斜杠，再把每个“/”改为“-”。
- **Codex：**`~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`。只保留首行 `payload.cwd` 等于工作区路径的文件。
- **其他运行环境：**该环境中本工作区的会话目录。

在此范围调查近期智能体对话，寻找反复出现的模式。按历史分片并行运行多个子代理，例如过去 2–4 周分三片，让每片有足够材料。根据 **poteto-mode** 技能的“子代理”部分，为每个子代理选择适合任务的推理级别以及快速或标准速度。每个挖掘子代理从父代理提供的工作区限定路径读记录，寻找以下信号，返回带证据指针的简短结构化模式列表。默认值得寻找的信号：

- 回复偏好（长度、语气、格式、要求“说简单点”的纠正）
- 委派习惯（子代理、模型、专门工作流、并行）
- 验证态度（“完成”的含义、单元测试与实际复现、审查者）
- 代码和文字规范（风格、引用原则、lint 与格式工具）
- 流程约定（Git 工作树、提交、PR、审查与合并工具）
- 元层面偏好（任务中途修技能、提出新技能）

提升信号为规则前跨分片核对。两个或更多分片出现的模式可信度高。单独信号较弱，通常丢弃。

<a id="2-ask-the-user-directly"></a>

### 2. 直接询问用户

挖掘会漏掉尚未表达的意图。使用结构化提问工具（结构化多选：Cursor 的 `AskQuestion`、Claude Code 的 `AskUserQuestion`、OpenCode 的 `question`），不要让用户从头自己打字。运行环境没有此工具时，在聊天中给出编号选项。

形式：一两个问题，每题 4–6 个选项；分类问题允许多选（Cursor 中 `allow_multiple: true`）。从宽问题开始（“哪些领域最重要？”），再对所选领域追问具体选项。结构化提问后，用一个自由文本聊天问题捕捉选项遗漏的内容。

不要一次抛出 20 个问题。

<a id="3-cluster-findings"></a>

### 3. 聚合发现

将合并信号归入章节。常见章节如下，只用适用项：

- **回复风格：**长度、语气、格式。
- **自主性：**无需询问可做多少、MCP 工具使用。
- **先理解：**界定或调查改动时使用哪些技能。
- **子代理：**默认设置、并行、模型与任务匹配、专门工作流。
- **文字与代码规范：**原则、lint 工具、风格指南。
- **审查与验证：**复现态度、验证技能、实际测试工具。
- **流程：**Git 工作树、提交、PR、审查与合并工具。
- **技能：**编写习惯、先修技能、提议新技能。

**poteto-mode** 技能展示了结构，阅读以把握粒度，不复制内容。用户规则与 poteto-mode 并不相同。

<a id="4-draft-the-skill"></a>

### 4. 起草技能

用技能编写技能（`create-skill`）编写。放置规则：

- 路径：保留现有模式技能的分类。新模式若仓库已有该用户的个人分类，采用 `<skills>/<handle>/<handle>-mode/SKILL.md`；否则默认放项目的 `<skills>/<handle>-mode/SKILL.md`，或按用户偏好放用户级技能目录。`<skills>` 是第 0 步对应的运行环境技能目录。
- 标识：用户名字或选择的标识符。
- frontmatter `description`：以用户名称、`/<handle>-mode` 和“按其风格工作”触发，而非“写代码”“审查 PR”等通用关键词。
- frontmatter 格式：遵循 `create-skill` 的 YAML 规则。`description` 保持单个 YAML 标量，标点或换行需要时加引号，或用 `description: >-` 加缩进续行。
- frontmatter 默认 `disable-model-invocation: true`。只有用户明确希望模式每回合都应用时，才取消此默认。

<a id="5-iterate-on-prose"></a>

### 5. 迭代文字

逐行应用 **unslop** 技能和 `create-skill` 写作指南。

向用户展示草稿并吸收反馈，预计会多次迭代。果断删减，模式技能不是操作手册。

<a id="6-land-it"></a>

### 6. 落地

在从 main 创建的 Git 工作树中工作，提交并创建 PR。不要直接推送 main。

<a id="guardrails"></a>

## 边界要求

- **不要过拟合单次对话。** 某偏好一次表达、另一次否定，就是噪声。必须有多次实例才固化。
- **不要耍聪明。** 重述其他技能内容、发明隐喻、给智能体写“诗意”文字，只增成本没有收益。保持可操作。
- **引用，不内联。** 用户依赖的其他技能以路径引用出现，不粘贴摘录；其他位置维护的原则文档也一样。
- **章节尽量少。** 只有用户在某方面有具体且非默认规则时才加章节。“清晰沟通”不算章节；“短段落。比较选项时用表格。只有事项确实并列时才用列表。”才算。
- **称谓保持通用。** 指令里用“用户”或“人”，不用作者的名字。
- **不要强求对称。** 用户没有值得记录的流程规则，就完全省略“流程”章节。

<a id="evaluation"></a>

## 评估

`-mode` 技能是主观输出，`create-skill` 式测试、迭代基准循环在这里没有用。与用户确认感觉：读起来像他们吗？遗漏什么吗？然后交付。

只有技能触发准确度在实际使用中成为问题时，才运行 description 优化循环。

<a id="when-not-to-use"></a>

## 不适用情况

- 用户想要面向特定任务的技能，而非工作约定：仅用 `create-skill`，无需挖掘。
- 用户想捕获一个狭窄工作流，例如“我如何写提交消息”：那是普通技能，不是模式技能。
