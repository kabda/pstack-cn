---
name: reflect
description: 在当前对话记录上并行启动三个审查子代理，提炼经验，并把每项经验落实为对现有技能的具体编辑。用户说 reflect 时使用。
disable-model-invocation: true
---

<a id="reflect"></a>

# 反思

从当前对话提炼长期有效的经验，再将其落实为技能编辑。

用户说“reflect”或“/reflect”时调用。对话琐碎、偏题，或已有技能明确覆盖且父代理正确遵循时跳过。一次性的情况不算经验。

<a id="1-locate-the-active-transcript"></a>

## 1. 定位当前对话记录

展开并行前，在当前工作区的会话目录中找到本次对话记录。不要跨所有项目目录搜索，否则会跨越工作区边界，读取无关项目的私人聊天。

记录位置取决于智能体运行环境：

- **Cursor：**系统提示词指定的 `agent-transcripts/` 目录。

  ```bash
  ls -t <agent-transcripts>/*.jsonl <agent-transcripts>/*/*.jsonl <agent-transcripts>/*/subagents/*.jsonl 2>/dev/null | head -10
  ```

  这覆盖旧版扁平布局（`<id>.jsonl`）、当前嵌套布局（`<id>/<id>.jsonl`）和子代理布局（`<parent>/subagents/<child>.jsonl`）。读取每个候选文件的第一行 JSONL，选择 `message.content[0].text` 包含对话首条用户提示词的文件。
- **Claude Code：**`~/.claude/projects/<slug>/<session-id>.jsonl`，其中 `<slug>` 将工作区路径中所有非字母数字字符替换为“-”。
- **Pi：**`~/.pi/agent/sessions/--<slug>--/*.jsonl`，其中 `<slug>` 去掉工作区路径开头的斜杠，再把每个“/”改为“-”。
- **Codex：**`~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`。只保留首行 `payload.cwd` 等于工作区路径的文件。
- **其他运行环境：**检查该工作区对应的运行环境会话目录。

Cursor 之外先看最新候选文件，在首条用户消息中找到本次对话开头提示词以确认。如果没有匹配项，改为提供精炼的会话摘要。

<a id="2-spawn-three-reviewers-in-parallel"></a>

## 2. 并行启动三个审查者

同一条消息中发起三个 `Task` 调用，使用 `subagent_type: generalPurpose`，采用智能体模式（`readonly: false`）。审查者需要 MCP 权限查询对话引用的工单、聊天线程和可观测性追踪，而只读模式会移除 MCP。

**其他智能体运行环境。** 本技能使用 Cursor 的 `Task` 工具启动子代理。其他环境使用各自的子代理工具：Claude Code 的 `Agent`（`subagent_type: general-purpose`）、OpenCode 的 `task`（`subagent_type: general`）、Codex 的 `spawn_agent`。保留提示词和模型，去掉工具没有的参数。如果运行环境没有子代理工具，例如未装扩展的 Pi，就由你逐个执行各角色。

每个审查者和综合者都对应 pstack 设置文件中的角色行与默认值（Cursor 为 `~/.cursor/rules/pstack-models.mdc`，Claude Code 为 `~/.claude/rules/pstack-models.md`，其他智能体运行环境为 `~/.agents/pstack-models.md`）。把 `model` 设为该行值，文件或该行缺失时使用默认值。值为 `auto` 或 `inherit-parent` 时不设 `model`。子代理工具拒绝 slug 时，使用默认值并说明；默认值也被拒绝时，从错误消息或运行环境模型列表中选择同系列最接近的有效 slug。根据 **poteto-mode** 技能的“子代理”部分，为每个子代理选择适合任务的推理级别以及快速或标准速度。

| 视角 | 角色行 | 默认 `model` | 提示词模板 |
|---|---|---|---|
| 判断 | `reflect judgment, divergent, synthesizer` | `claude-opus-5-5-xhigh` | `references/judgment-reviewer.md` |
| 工具 | `reflect tooling` | `grok-4.7-xhigh-fast` | `references/tooling-reviewer.md` |
| 发散 | `reflect judgment, divergent, synthesizer` | `claude-opus-5-5-xhigh` | `references/divergent-reviewer.md` |

逐字传入每份模板，在标记位置替换对话路径或摘要。审查者通过 `Task` 响应正文返回发现。

<a id="3-synthesize"></a>

## 3. 综合

一次 `Task` 调用，使用 `subagent_type: generalPurpose`，`model` 来自 `reflect judgment, divergent, synthesizer` 行（默认 `claude-opus-5-5-xhigh`），采用智能体模式（`readonly: false`）。综合者通过 MCP 抽查引用，而只读模式会移除 MCP。逐字传入 `references/synthesizer.md`，在标记位置内联各审查者的完整输出。它返回 Accepted（已接受）/ Rejected（已拒绝）/ Backlog（待办）列表。

<a id="4-structural-enforcement-check"></a>

## 4. 结构化强制检查

如果某个 Accepted 项用 lint 规则、脚本、元数据标志或运行时检查能更可靠执行，将它移到 Backlog。参见 **encode-lessons-in-structure** 原则技能。

<a id="5-apply"></a>

## 5. 应用

展示综合者完整的 Accepted / Rejected / Backlog 输出，应用任何 Accepted 编辑前等待用户明确批准。用户逐项选择，也可以调整落实位置。技能改动影响组织内未来每个智能体，不能自动应用。

每个 Backlog 项无需等待，直接登记到团队 devex 或待办跟踪系统。只有 Accepted 列表需要等批准。

绝不编辑 `plugins/cache/` 下的技能。批准前展示目标位置：Cursor 中为 `.cursor/skills/<skill>/` 或 `~/.cursor/skills/<skill>/`，其他环境为其项目或用户技能目录，例如 `.claude/skills/<skill>/` 或 `~/.agents/skills/<skill>/`。批准后把技能目录复制到目标位置，再编辑副本。绝不创建 PR 或推送。

严格遵循每个获批条目的 Routing（落实位置）：

- 现有技能的小编辑（单行列表项、收紧一句话、纠正过时事实）：父代理直接处理。
- 现有技能的实质编辑（新增章节、新模式表、约 10 行以上）：交给运行环境的技能编写技能，执行其起草 / 测试 / 迭代循环。Cursor 中是内置 `create-skill`，或使用 Anthropic 的 `skill-creator`。两者均无时，遵循 agentskills.io 的 Agent Skills 格式。下文的“`create-skill`”指你实际采用的这一工具。
- `tune description: <skill path>`（技能存在但该触发时没触发）：交给 `create-skill`，运行其 description 优化循环。
- `new skill via create-skill: <kebab-name>`：把创建任务交给 `create-skill`，不要临时发明结构。

如果环境提供 SKILL.md 验证器，在宣布完成前对每个触及的技能运行它。

<a id="6-summarize-for-the-user"></a>

## 6. 向用户总结

简短列表，无开场白：

- 已应用编辑：`<skill path>`。每项一行说明变化。
- 新建技能：`<skill path>`。每项一行（应当少见）。
- 已登记到 devex 跟踪系统的待办：`<issue title>`（`<tags>`）。每项一行。
- 已丢弃：每条被拒绝发现各一行，附综合者给出的原因。
