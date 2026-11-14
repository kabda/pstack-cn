<a id="pstack-in-claude-code"></a>

# 在 Claude Code 中使用 pstack

pstack 技能使用 Cursor 名称。在 Claude Code 中，每个会话读取本文件一次，再按下表映射技能中的各个 Cursor 名称。`<pstack>` 指包含 `skills/` 和 `docs/` 的文件夹。如果某个 Cursor 字段没有对应行，就省略并说明。绝不传入工具 schema 拒绝的字段或值。

<a id="tools"></a>

## 工具

| Cursor | Claude Code |
| --- | --- |
| `Task` | `Agent` |
| `AskQuestion` | `AskUserQuestion`。`-p` 模式中没有此工具，因此改用普通文字提问。 |
| 打开待办列表 | 会话提供 `TodoWrite` 时使用它；否则在回复中维护列表，并在每个阶段更新。 |
| 运行另一项 pstack 技能（`/name` 或“**name** 技能”） | 使用 `Read` 读取 `<pstack>/skills/<name>/SKILL.md` 并遵循它。`Skill` 工具会拒绝大多数 pstack 技能。告诉用户输入命令时，写 `/pstack:<name>`。 |
| `Grep`、`Glob` | 会话没有 `Grep` 或 `Glob` 时，通过 `Bash` 使用 `rg`。 |

<a id="subagent-fields"></a>

## 子代理字段

| Cursor | Claude Code |
| --- | --- |
| `subagent_type: generalPurpose` | `subagent_type: "general-purpose"` |
| `poteto-agent`、`comment-sicko` | `pstack:poteto-agent`、`pstack:comment-sicko` |
| `readonly: true` | `subagent_type: "Explore"`。它仍保留 `Bash`，因此任务说明还须写明“不要编辑文件”，并在之后检查 `git status`。 |
| `readonly: false` | `general-purpose`。它保留会话的 MCP 服务器。 |
| `environment: "cloud"` | `isolation: "worktree"`。指明工作代理要检出的分支或 commit。 |
| `environment: "local"` | 省略。 |
| `cloud_base_branch: <b>` | 告诉工作代理先检出 `<b>`。 |
| `run_in_background: true` | 省略。子代理默认在后台运行，并在完成时通知你。 |
| `resume` | 启动新智能体，把先前结果粘贴到任务说明中。 |
| `file_attachments` | 在任务说明中列出路径。 |

<a id="models"></a>

## 模型

| Cursor | Claude Code |
| --- | --- |
| `claude-<family>-<version>-<effort>[-fast]`，如 `claude-opus-5-5-xhigh` | `model: "opus"` 和 `effort: "xhigh"`。`model` 仅接受 `opus`、`sonnet`、`haiku`、`fable`。去掉 `-fast`。 |
| `grok-*`、`gpt-*` 或其他非 Claude slug | 省略 `model`，让智能体使用会话模型，并说明这一点。 |
| `auto` 或 `inherit-parent` | 省略 `model`。 |
| `pstack-models.mdc` 规则、`~/.cursor/rules/pstack-models.mdc` | `~/.claude/rules/pstack-models.md`。Claude Code 将其加载进每个新会话，因此角色行已在上下文中。如果没有，就读取文件。如果文件或角色对应行不存在，使用技能默认 slug。 |
| `<model> <effort>` 形式的角色值，如 `opus high` | `model: "opus"` 和 `effort: "high"`。 |

<a id="setup-pstack"></a>

## setup-pstack

Claude Code 会把 `~/.claude/rules/` 中的每个 `.md` 文件加载进每个新会话，因此 `setup-pstack` 在那里写入规则。遵循其步骤，但作以下映射：

- 检测。检测到的模型是 `Agent` 工具 schema 列出的 `model` 值，每个搭配其 `effort` 值之一。真实模型写为 `<model> <effort>`，例如 `opus xhigh`。推理强度位于最后一个 token，因此预算步骤可以按原方式工作。
- 默认值。按上表映射每个默认 slug：`claude-opus-5-5-xhigh` 为 `opus xhigh`，`grok-4.7-xhigh-fast` 为 `inherit-parent`。
- 写入。写入 `~/.claude/rules/pstack-models.md`，不含 frontmatter，然后依次写注释行、`# budget` 行，以及步骤 5 的每个角色一行。覆盖整个文件。绝不把角色行放进 `CLAUDE.md` 或 `AGENTS.md`。

<a id="paths"></a>

## 路径

| Cursor | Claude Code |
| --- | --- |
| `.cursor/skills/`、`~/.cursor/skills/` | `.claude/skills/`、`~/.claude/skills/` |
| `~/.cursor/plugins/`、`.cursor-plugin/plugin.json` | `~/.claude/plugins/`、`.claude-plugin/plugin.json` |
| `.cursor/rules/*.mdc`、始终应用的规则 | `CLAUDE.md`；不存在 `CLAUDE.md` 时用 `AGENTS.md`。Claude Code 从不读取 `.mdc` 文件。模型规则是例外，见模型部分。 |
| `https://github.com/cursor/plugins/blob/main/pstack/<path>` | 本地文件存在时用 `<pstack>/<path>`。插件随附技能、`docs/guide/` 和 `README.md`。读取本地副本，绝不抓取远程。用户需要链接时再给 URL。 |
| `~/.cursor/projects/<slug>/agent-transcripts/` 中的对话记录 | `~/.claude/projects/<slug>/<session>.jsonl`。slug 来自工作区路径，将每个 `/` 和 `.` 改为 `-`，因此 `/Users/you/proj` 变为 `-Users-you-proj`。直接位于该文件夹中的最新 `.jsonl` 是当前会话。其 `<session>/subagents/` 文件夹保存子代理记录。只读取当前工作区的文件夹。 |

<a id="cursor-only-features"></a>

## Cursor 专有功能

Claude Code 没有 Cursor Automations、Bugbot、Cursor 云端智能体或内置 PR 工具。某步骤需要其中之一时，在回复中写一行 `Skipped in Claude Code: <step>. <reason>.`（在 Claude Code 中跳过：步骤及原因），然后继续下一步。不要停止、提问或重试。如果后续步骤需要被跳过步骤的产物，例如 URL 或密钥，留下占位符，并在该行指出。

| Cursor | Claude Code |
| --- | --- |
| Cursor Automations：例程、`update_state` 例程调用、`api2.cursor.sh/automations` webhook、例程唤醒及 `SendToUser` 密钥请求 | 按上述格式说明并跳过。 |
| Bugbot | GitHub PR 上的 Bugbot 评论属于普通审查讨论，因此用步骤指定的代码托管命令分流。如果 PR 没有 Bugbot 检查或评论，则跳过启动、等待或配置 Bugbot 的步骤。 |
| Cursor 云端智能体 | 如子代理字段所述，`environment: "cloud"` 映射为工作树。需要云端智能体本身的步骤，例如控制面板状态或其独立机器，应跳过。 |
| 内置 PR 工具 | 使用步骤指定的代码托管命令，例如 `gh pr create`。这不算跳过，因此不写跳过说明。 |
