---
name: setup-pstack
description: 配置 pstack 各角色使用的模型及推理预算。检测可用模型并写入始终应用的规则，覆盖技能默认值。用于 /setup-pstack、configure pstack models（配置 pstack 模型）、pstack budget（pstack 预算），或更改 pstack 模型选择时。
---

<a id="setup-pstack"></a>

# 配置 pstack

写入 pstack 模型设置，每个角色一个模型：

- **Cursor：**`~/.cursor/rules/pstack-models.mdc`，始终应用的规则。
- **Claude Code：**`~/.claude/rules/pstack-models.md`。Claude Code 会在每个新会话加载 `~/.claude/rules/` 内全部文件。
- **其他所有智能体运行环境**（Codex、Pi、OpenCode 等）：`~/.agents/pstack-models.md`。这些环境不会自行加载，pstack 技能选择模型时会读取它。

下文“设置文件”指当前运行环境对应的文件。在 Claude Code 中，如果该文件缺失，改读 `~/.agents/pstack-models.md`，这是本技能旧版本写入的位置。

<a id="steps"></a>

## 步骤

<a id="1-detect-available-models"></a>

### 1. 检测可用模型

枚举本会话可传给子代理的模型 slug（Cursor 的 `Task`、Claude Code 的 `Agent`、OpenCode 的 `task`、Codex 的 `spawn_agent`），这是可靠来源。如果运行环境另有列出用户模型的命令，优先使用以求完整，例如 `opencode models` 或 `pi --list-models`。无法检测任何模型时，请用户粘贴有权使用的 slug。绝不写入未经确认可用的真实 slug。`inherit-parent` 和 `auto` 别名始终有效，尽管它们不是检测到的 slug。

<a id="2-load-current-state"></a>

### 2. 加载当前状态

默认角色与模型映射见下方第 5 步规则结构。设置文件已存在时，读取并把 `# budget` 行及角色值视为当前选择；否则从默认值开始。第 5 步没有的角色行，例如 `how critics`，属于退役角色，移除它。

<a id="3-budget-map-and-confirm"></a>

### 3. 选择预算、映射并确认

**(a) 询问预算。** 优先使用结构化提问工具（Cursor 的 `AskQuestion`、Claude Code 的 `AskUserQuestion`、OpenCode 的 `question`），而非自由文本。提供以下四个选项，标签必须精确保持原样；规则记录当前预算时也要说明。没有规则时，说明 `large` 与技能默认值一致。

- `unlimited — max reasoning`：无限预算，最高推理级别。
- `large — xhigh reasoning`：大预算，xhigh 推理级别。
- `medium — high reasoning`：中预算，high 推理级别。
- `small — medium reasoning`：小预算，medium 推理级别。

**(b) 应用预算。** 从技能默认值构建工作表；重新运行时，保留你曾按系列、列表或别名（`inherit-parent`、`auto`）调整的角色。`unlimited`、`large`、`medium`、`small` 将每个真实 slug（包括面板条目）的推理级别 token 分别设为 `max`、`xhigh`、`high`、`medium`。推理 token 是最后一个 token，或末尾 `fast` 前的 token，级别顺序为 `max` > `xhigh` > `high` > `medium` > `low`。如果结果不是已检测 slug，选择同系列已检测 slug 中不超过目标的最高级别；没有则把该角色标为需要选择。`inherit-parent` 和 `auto` 不变。因此 `unlimited` 把 `claude-opus-5-5-xhigh` 改为 `claude-opus-5-5-max`。Grok slug 最高为 `xhigh`，所以 `unlimited` 的回退将 Grok 设为 `xhigh`，`grok-4.7-xhigh-fast` 保持不变。`large` 保持两个默认值。`small` 将它们改为 `claude-opus-5-5-medium` 和 `grok-4.7-medium-fast`。

**(c) 展示角色并确认。** 展示每个角色及模型，不在检测集合的真实 slug 标为需要选择。还要列出第 2 步移除的每行。询问原样接受还是更改指定角色，选项为已检测模型加 `inherit-parent`、`auto`（两者都表示该角色使用父聊天模型，让 Auto 用户继续使用 Auto）。优先使用结构化提问工具，而非自由文本。面板角色（arena runners、architect runners、interrogate reviewers）的值为列表，每个条目启动一个子代理，别名条目也包括在内，因此列表长度决定数量。`arena cross-judge pool` 也是列表，但 Arena 只运行一个评判者。它按列表顺序，仅尝试与父模型不同系列的值，因此按偏好排序。`inherit-parent` 或 `auto` 绝不担任评判。`swarm workers` 是所有工作者的默认模型，除非竞赛或对比为每个参赛分支指定不同模型。

<a id="4-validate"></a>

### 4. 验证

写入的每个真实 slug 必须在检测集合中。`inherit-parent`、`auto` 始终通过。所选真实 slug 不可用时，停止并重新询问。

<a id="5-write-the-rule"></a>

### 5. 写入规则

写入设置文件，包含记录所选标签及目标级别的 `# budget` 行；每个角色一行，采用与 poteto-mode 相同的标签。Cursor 中包含下面 frontmatter，设 `alwaysApply: true`。其他运行环境省略 frontmatter，从首个 `#` 行开始。覆盖整个文件，使重跑保持幂等。结构如下：

```
---
description: pstack 各角色模型选择（覆盖技能默认值）
alwaysApply: true
---
# pstack 模型配置。每个角色一行。删除某行即可回退到技能默认值。
# 值为 `inherit-parent` 或 `auto` 时，该角色使用父聊天模型（省略子代理 `model`）。面板列表中的别名条目仍计入并行数量。
# budget: large (xhigh)
feature, refactoring: grok-4.7-xhigh-fast
bug-fix: grok-4.7-xhigh-fast
perf-issue: grok-4.7-xhigh-fast
hillclimb: grok-4.7-xhigh-fast
judgment and prose: claude-opus-5-5-xhigh
hardest tasks: claude-opus-5-5-xhigh
how explorer: grok-4.7-xhigh-fast
how explainer: claude-opus-5-5-xhigh
why investigators: grok-4.7-xhigh-fast
why synthesizer: claude-opus-5-5-xhigh
reflect tooling: grok-4.7-xhigh-fast
reflect judgment, divergent, synthesizer: claude-opus-5-5-xhigh
arena runners: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
arena cross-judge pool: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
swarm workers: grok-4.7-xhigh-fast
architect runners: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
interrogate reviewers: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
```

<a id="6-confirm"></a>

### 6. 确认

告诉用户写入哪个文件。Cursor 和 Claude Code 中，新会话生效。其他运行环境中，pstack 技能选择模型时读取 `~/.agents/pstack-models.md`。重跑本技能会更新它。

<a id="7-offer-a-verification-skill-optional"></a>

### 7. 提议验证技能（可选）

检查项目是否有驱动真实应用来提供证明的方式（`verify-*` 技能或现有运行工具）。没有时只提议一次：“要一个项目本地验证技能吗？让智能体像用户一样驱动应用，证明改动有效。我可以用 /create-verification-skill 生成。”同意则调用 `/create-verification-skill`，按 pstack 实际安装位置解析（工作区、用户或插件）；拒绝则继续，不再催促。

<a id="8-offer-a-formal-verification-skill-optional"></a>

### 8. 提议形式化验证技能（可选）

检查项目是否已有形式化验证技能（对代码运行模型检查器、证明或其他验证器的项目技能）。没有时只提议一次：“要一个形式化验证技能吗？让智能体证明代码关键性质在范围内每种情况都成立，而不只覆盖测试能到达的案例。我可以用 /create-formal-verification-skill 生成。”同意则调用 `/create-formal-verification-skill`，按 pstack 实际安装位置解析（工作区、用户或插件）；拒绝则继续，不再催促。
