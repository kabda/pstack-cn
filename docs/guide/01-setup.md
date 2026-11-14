<a id="set-up-pstack"></a>

# 设置 pstack

本页介绍如何安装插件、选择 pstack 使用的模型，以及运行第一个任务。设置过程只需一条命令和一段简短对话。

<a id="install-the-plugin"></a>

## 安装插件

在 Cursor 聊天中运行：

```text
/add-plugin pstack
```

Cursor 会确认插件已安装。

在 Claude Code 中，先运行 `/plugin marketplace add cursor/plugins`，再运行 `/plugin install pstack@cursor-plugins`。Claude Code 会给插件命令添加前缀，因此本指南中的每条命令在那里都要加上 `pstack:`，例如 `/pstack:setup-pstack`；它会把模型规则写入 `~/.claude/rules/pstack-models.md`。[Claude Code 适配说明](../harness/claude-code.md)介绍了其他差异。

<a id="pick-your-models"></a>

## 选择模型

运行：

```text
/setup-pstack
```

[`/setup-pstack`](../../skills/setup-pstack/SKILL.md) 会检测你有权使用的模型，询问推理预算，展示各个角色（代码任务子代理、判断、各审查小组），并询问你的选择。回答这些问题后，它会写入 `~/.cursor/rules/pstack-models.mdc`，这是每项 pstack 技能都会读取的一份简短规则。

默认采用 `xhigh` 推理强度，与 `large` 预算相同。`unlimited` 将每个模型提升到其最高档位，上限为 `max`。Opus 会升到 `max`；Grok 的上限是 `xhigh`，因此保持不变。`medium` 和 `small` 会降低推理强度，减少 token 消耗。

你只需覆盖在意的选项。规则中未列出的角色会继续使用技能默认值。要恢复默认值，删除该角色所在的行。重新运行 `/setup-pstack` 时，会保留模型与默认值不同的角色。当默认值变更时，变更前写入的规则仍会锁定旧默认值，因此应删除这些角色行，或删除整个文件，然后再次运行 `/setup-pstack`。

如果使用 Auto，会发生什么？将角色设为 `inherit-parent` 或 `auto` 后，pstack 会省略子代理的 `model` 字段，让子代理继承父聊天的模型。这两个值含义相同，都不是模型 slug。对于审查小组角色，值是一个列表，每个条目运行一个子代理，因此列表长度决定小组规模。设置过程还会配置 `swarm workers`，作为每个 `/swarm` 工作代理的默认模型；竞赛为每一组明确指定模型时除外。

<a id="accept-the-verification-offers-or-dont"></a>

## 接受或拒绝验证建议

设置结束时，`/setup-pstack` 会寻找项目中证明应用行为的方法：`verify-*` 技能或已有运行环境。如果两者都没有，它会通过 [`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md) 提议生成一项验证技能，只询问一次。

同意后，它会写入 `.cursor/skills/verify-<app>/`，这项项目内技能会教智能体像用户一样操作应用。交付前，它会先证明该技能能正常工作。拒绝后，设置会继续。你随时可以自行运行 `/create-verification-skill`。[验证并交付](./06-verify-and-ship.md#create-a-project-verification-skill)有详细介绍。

如果你刚开始使用 pstack，建议接受。能检查自己工作的智能体，会继续推进直到检查通过；不能检查的智能体，则会把每个结果交回给你手动确认。本指南介绍的内容中，验证技能带来的收益最大。

然后，除非项目已有形式化验证技能，否则设置会通过 [`/create-formal-verification-skill`](../../skills/create-formal-verification-skill/SKILL.md) 提议生成一项，也只询问一次。测试检查人们想到并写出的用例；形式化验证技能则在明确范围内的每一种情况下，检查代码的一项关键性质，例如“同一个作业绝不会同时运行两次”。如果代码涉及并发、重试、状态机或解析器，缺陷代价高，而测试很少触及出错情形，就应接受。否则可以拒绝，情况变化后再运行。[验证并交付](./06-verify-and-ship.md#prove-a-property-with-a-formal-verification-skill)对此也有介绍。

设置后，请新建聊天。模型规则对新会话生效。

<a id="keep-the-cost-in-check"></a>

## 控制成本

pstack 会在子代理和审查小组上多消耗一些 token，这是严谨性的代价。要降低消耗，可以：

- 重新运行 `/setup-pstack`，选择较小的推理预算或更便宜的模型。主聊天使用强模型，代码角色使用更便宜、更快的模型，是一种合理分配。
- 把角色设为 `auto` 或 `inherit-parent`，让它使用聊天自身的模型。
- 缩短审查小组列表。每个条目会运行一个子代理。
- 把 `/poteto-mode` 留给需要严谨处理的工作。简单明确的小改动不需要它。

<a id="run-your-first-task"></a>

## 运行第一个任务

选一个真实但规模小的任务，像对同事一样描述：

```text
/poteto-mode 给这条命令增加 --json 标志。文本输出必须逐字节保持一致。验证两种输出。
```

观察待办列表。最前面的条目是从匹配的操作手册复制来的步骤；上述提示会匹配功能开发操作手册。如果 `/poteto-mode` 跳过一步，该步骤仍会留在列表中，标注 `skip: <reason>`，让你看到它选择了不做什么。

此后，你可以像平时一样继续对话。要让 `/poteto-mode` 在整个聊天中持续生效，请从 `/` 菜单选择它，并按 Option+Enter（Mac）或 Alt+Enter（Windows），而不是 Enter。这样会把它设为[自定义模式（Custom Mode）](https://cursor.com/docs/skills#using-a-skill-as-a-custom-mode)，在你退出之前，每一轮对话都会将它保留在上下文中。自定义模式可用于 Agents Window（智能体窗口）和 CLI。只按 Enter 会把技能附加到一条消息，随着聊天继续，它会逐渐淡出上下文。

下一页：[通过 `/poteto-mode` 分派工作](./02-poteto-mode.md)。
