---
name: why
description: "用于‘为什么 X 这样工作’（why does X work this way）、‘为什么选择 Y’（why we picked Y）、设计依据、回归、事后复盘或有数据支撑的阈值。发现可用 MCP，并行查询每类证据（源代码管理、问题跟踪系统、长篇文档、实时聊天、基础设施可观测性、错误跟踪、产品分析数据仓库），然后给出带引用的决策与权衡解读。运行时行为请使用 how。"
disable-model-invocation: true
---

<a id="why"></a>
# 为什么

调查代码背后的动机与意图。配套的 `how` 技能回答代码做什么、如何工作；`why` 回答哪些因素促成了它现在的形态。

下文每次派生都会指定 pstack 设置文件中的一个角色行（Cursor 中为 `~/.cursor/rules/pstack-models.mdc`，Claude Code 中为 `~/.claude/rules/pstack-models.md`，其他运行环境中为 `~/.agents/pstack-models.md`）和一个默认值。将 `model` 设置为该行的值；文件或该行缺失时使用默认值。值为 `auto` 或 `inherit-parent` 时，不设置 `model`。如果子代理工具拒绝某个 slug，使用默认值并说明。如果默认值也被拒绝，从错误消息或运行环境的模型列表中选择同系列最接近的有效 slug。按照 **poteto-mode** 技能的子代理章节，为每个子代理选择适合任务的推理等级，以及快速或标准速度。

所有派生都使用 `generalPurpose` 和 `readonly: false`（agent 模式）。**不要使用 readonly/Ask 模式。** 它会移除 MCP 访问权限，导致依赖 MCP 的调查者及综合者的引用抽查失效。调查者仍然不应进行任何写入。

<a id="operating-posture"></a>
## 工作姿态

以**细致、谨慎、精确的调查者**身份工作。如实区分已知事实和自己的推断。阅读 `references/epistemics.md`，了解完整的置信框架和措辞指南。综合者必须遵循它。

<a id="step-1-understand-the-target-and-the-question"></a>
## 第 1 步：理解目标和问题

**目标**通常是一段代码、一种模式、一项功能，或一个有名称的设计决策。**问题**通常涉及设计依据、权衡、促成设计的边界情况、外部约束、死代码，或广泛的历史梳理。

如果目标模糊（如“为什么这样做？”却没有明确所指），根据会话上下文作最佳判断（打开的文件、近期修改、光标位置、刚讨论的内容）。简短说明你的理解，让用户在你偏离时能纠正，然后继续。

<a id="step-2-establish-the-code-anchor"></a>
## 第 2 步：建立代码锚点

派生调查者之前，直接构建种子上下文：文件路径和行范围、关键符号（函数、类、常量）、最近几次涉及目标的提交、合并提交中的 PR 编号（主题行中的 `(#1234)` 模式），以及关联的工单 ID。运行 `git blame -L <start>,<end> <file>` 查找最后修改的提交，运行 `git log --follow -p -- <file>` 查看跨重命名的完整补丁历史，运行 `git log --oneline -20 -- <file>` 查看带 PR 编号的近期提交，运行 `git log -1 --format=%B <commit>` 提取 PR 编号。然后为每个实质性提交获取 PR 正文和讨论：`gh pr view <number> --json title,body,author,createdAt,mergedAt,labels,closingIssuesReferences,comments,reviews`。将此锚点交给每个调查者和综合者。

<a id="step-3-spawn-parallel-investigators"></a>
## 第 3 步：派生并行调查者

**默认开展完整的并行调查。** 目标是完整的覆盖图，而不是最少搜索。记录空结果，不要跳过搜索。

<a id="discovery"></a>
### 发现

派生调查者之前，列出连接到运行环境的 MCP 服务器。如果存在可用工具映射，使用它。在 Cursor 中，还可检查其为已启用 MCP 服务器暴露的 `mcps/` 目录。在其他运行环境中，MCP 工具通常出现在工具列表中，工具名包含服务器名（例如 Claude Code 中的 `mcp__<server>__<tool>`）。

将每个可用 MCP 映射到一个证据类别：

1. 源代码管理历史
2. 问题／工单跟踪系统
3. 长篇文档
4. 团队实时聊天
5. 基础设施可观测性
6. 错误／异常跟踪
7. 产品分析数据仓库

源代码管理始终可通过 Git 和 `gh` 访问。其他六类根据 MCP 名称、服务器指令、工具名和资源描述符分类。如果 MCP 适合多个类别，选择与其主要证据匹配的类别。在覆盖图中记录有歧义的情况。

对每个具有匹配 MCP 的类别派生一个调查者，在同一条消息中完成全部派生，使其并行运行。每人恰好负责一个工具或 MCP。不要让同一智能体覆盖多个 MCP。`model`：`why investigators` 行，默认 `grok-4.7-xhigh-fast`。

每个调查者的提示词使用填好的 `references/investigator-prompt.md`，再附上：
- 所选 MCP 的类别操作手册 `references/sources/<source>.md`，根据 `references/source-playbook.md` 中的示例调整
- **如果目标代码看起来具有防御性**（空值检查、重试逻辑、超时处理、限流、功能标志、出站防护、OOM 处理器），附上 `references/sources/incident-postmortem.md`
- 代码锚点和用户的原始问题

**其他运行环境。** 此技能的派生使用 Cursor 的 `Task` 工具。在其他运行环境中，使用对应的子代理工具：Claude Code 的 `Agent`（`subagent_type: general-purpose`）、OpenCode 的 `task`（`subagent_type: general`）、Codex 的 `spawn_agent`。保留提示词和模型，删除工具不具备的参数。如果运行环境没有子代理工具，例如未安装扩展的 Pi，则自行依次执行每个调查者的工作。

<a id="investigator-roster-one-per-available-evidence-category"></a>
### 调查者名单：每个可用证据类别一人

下列每类证据都独特地擅长揭示一种“为什么”，列在“最擅长”后。用它判断预期返回什么，在某类结果为空时说明缺口；只有极少数能证明无关的情况下，才用它说明跳过理由。

1. **源代码管理**（Git 历史、用 `gh` 查看 PR、代码注释、测试）。始终派生，是唯一保证可用的来源。最擅长揭示*审查期间记录的实现时依据*。
2. **问题／工单跟踪系统**（例如 Linear、Jira、GitHub Issues、Plane、Shortcut MCP）。最擅长揭示*推动工作的产品或业务因素*。当原因在工程之外时最有力。
3. **长篇文档**（例如 Notion、Confluence、Google Docs、Coda MCP）。最擅长揭示*在代码形成前写下的长篇设计依据*。
4. **团队实时聊天**（例如 Slack、Discord、Microsoft Teams、Mattermost MCP）。最擅长揭示*从未进入文档的实时讨论*。当源代码管理、工单和文档的书面线索稀少时，尤其重要。
5. **基础设施可观测性**（例如 Datadog、New Relic、Honeycomb、Grafana、Splunk MCP）。最擅长揭示*促成代码的基础设施及运行时现实*。当目标响应基础设施信号（超时、重试、限流、熔断器）时最有力。
6. **错误／异常跟踪**（例如 Sentry、Rollbar、Bugsnag、Airbrake MCP）。最擅长揭示*促成防御性或纠正性代码的具体异常及错误轨迹*。最适用于 catch 块、空值保护、类型检查、重试及其他防御措施。
7. **产品分析数据仓库**（例如 Databricks、Snowflake、BigQuery、ClickHouse、dbt、Redshift MCP）。最擅长揭示*塑造代码的产品和数据现实*。最适用于功能标志控制的代码、实验驱动的交付、数据迁移及“这个数字从哪里来”的问题。

<a id="when-to-skip-an-investigator"></a>
### 何时跳过调查者

只有提供**明确的书面理由**才可跳过，并将理由写入最终“查阅的来源”。两种有效理由：

- 此环境中**没有该类别的可用 MCP**。将其标为缺口，而非选择：“跳过团队实时聊天。没有可匹配的 MCP，因此无法搜索会话记录。”
- **可以证明来源无关**，不能只是“可能无关”。门槛很高：“跳过错误／异常跟踪。目标是构建时脚本，没有运行时代码路径。”

如果范围评估表明目标很简单、只涉及单次提交，且 PR 描述已包含完整答案，则**只有确认全部七类可用类别的搜索都会重复已有信息后**，才可直接回答。明确说明这一点。这种情况应当很少。

<a id="step-4-synthesize"></a>
## 第 4 步：综合

派生一个综合者。`model`：`why synthesizer` 行，默认 `claude-opus-5-5-xhigh`。它接收：
1. 调查者的发现，包括所有空结果及有理由跳过的类别
2. 代码锚点
3. 用户的原始问题
4. `references/epistemics.md` 中的认知与置信框架
5. `references/synthesizer-prompt.md` 中的综合者提示词模板

<a id="step-5-present"></a>
## 第 5 步：呈现

向用户呈现综合者的输出。可以稍作编辑以使其清晰，或补充会话上下文，但**不要改写置信措辞**。

<a id="output-format"></a>
## 输出格式

采用 `references/synthesizer-prompt.md` 中的结构：问题、所讨论的代码、发现的事实、合理推断、竞争假设、尚不清楚的内容、查阅的来源、置信度总结。可按需调整，但必须完整区分置信等级；“查阅的来源”保持每个调查者一行，包括返回空结果或被跳过的调查者，并说明原因。

在“查阅的来源”之后，如果用户提出 `why` 问题是为了后续修改代码，将历史脉络发现转化为“保留／更改／避免／风险”约束集，用于改动规划。

<a id="common-failure-modes-to-avoid"></a>
## 要避免的常见失败模式

- **近因偏差**。以为最新提交最具权威。当前形态往往是许多早期决策累积而成的。向前追溯。
