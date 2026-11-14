<a id="benny-automation-intent"></a>
# benny 自动化意图

<a id="what-i-want-to-automate"></a>
## 我想自动化的工作

我想要两个在同一个 Slack 问题频道中协同工作的 Cursor 自动化。

<a id="automation-1-triage-issue-reports"></a>
### 自动化 1：问题报告分诊

- 触发：当有人在我配置的来源 Slack 频道发布一条新的顶层报告时，我希望此自动化从该报告开始，并保留其原始线程坐标。
- 行为：我希望它读取线程和附件，将报告归类为缺陷或性能问题、功能请求、问题或反馈，或需要转交的报告，并在路由前追踪可能负责的层。
- 跟踪系统：我希望它在配置的问题跟踪系统中搜索重复项，更新有充分把握的重复项，仅为明确的新缺陷创建工单。
- 工具：我需要 Slack 线程读取和回复权限、配置的问题跟踪系统集成，以及可选的路由映射。
- 结果：我希望它在来源线程中恰好回复一次，包含简短结论以及 `[benny:bug]`、`[benny:performance]` 或 `[benny:other]`。缺陷或性能标记可以包含跟踪系统 URL。
- 边界：我绝不希望此自动化在来源频道中发布根消息。

<a id="automation-2-reproduce-and-fix-confirmed-bugs"></a>
### 自动化 2：复现并修复已确认的缺陷

- 触发：我希望此自动化从同一条新的顶层报告，或设置时选定的其他受支持触发器开始，然后在原始线程中等待可信的分诊标记。
- 门禁：当有人明确负责修复时，我希望它停止。如果现有拉取请求或已合并提交可能修复该报告，我希望它进行验证，而非另做一份相互竞争的改动。
- 行为：我希望它使用配置的控制适配器和功能映射，通过真实 UI 将完全相同的症状复现两次，并采集截图、视频以及只读状态交叉核验。
- 修复：我希望它验证现有拉取请求，不在其基础上另行编写改动。确认复现后，它可以尝试一次有明确边界的根因修复，在测试成本低时使用 TDD，对影响范围进行冒烟测试，并且只有前后对照证据通过后才打开草稿拉取请求。
- 工具：我需要 Slack 线程读取和回复权限、仓库及历史访问权限、草稿拉取请求创建权限、配置的问题跟踪系统，以及控制适配器。
- 结果：我希望它在来源线程或可选的运维线程中提供证据和已验证结果，还可附上草稿拉取请求。更新应简洁。
- 边界：我绝不希望此自动化在来源频道中发布根消息。

<a id="shared-rules"></a>
### 共同规则

- 我希望来源频道和根线程坐标在整个运行期间保持不变。
- 我将工具机器人和调试机器人视为证据，而非任务委派或修复归属。
- 我允许子代理协助，但它们不能向 Slack 发消息，也不能接收 Slack 凭据。
- 我希望将整个资料包提交到目标仓库的 `.cursor/automations/benny/`。其中的 `SKILL.md` 文件是直接供自动化使用的指令，而非注册的插件技能。
- 我希望仅通过目标仓库已提交的 `.cursor/settings.json` 启用 pstack，用于 `how`、`why`、`tdd`、`unslop` 及所需原则技能等共享依赖。
- 我希望每个实际启用的自动化提示词直接读取已提交的操作文件。我不希望使用插件缓存路径、复制的摘录或斜杠技能发现机制。
- 我将用户自有配置、功能映射、路由映射和秘密信息保存在 `.cursor/automations/benny/` 之外，以免资料包刷新时覆盖它们。
- 当频道坐标、跟踪系统访问权限、控制适配器或功能映射缺失或不确定时，我希望两个自动化都以关闭方式失败。
- 我只需要草稿拉取请求。不要合并或部署。

<a id="my-configuration"></a>
### 我的配置

- 来源 Slack 频道：`<channel>`
- 可选运维频道：`<channel or none>`
- 仓库和默认分支：`<repo>`、`<branch>`
- 跟踪系统：`<type, team, project, labels, intake status>`
- 路由映射：`<path or none>`
- 分诊身份：`<slack identity>`
- 控制技能：`<configured skill or adapter>`
- 功能映射：`<committed same-repo path outside the copied pack, or behavior to paraphrase>`
- 模型：`<triage, reproduce, code, media review>`
- 状态 emoji 字符串：`<seen, reproducing, reproduced, blocked, fixing, failed, pull request opened>`
- 预算：`<polling, verdict wait, follow-up, repro, rejection, fix>`
- 可选机器人令牌能力：`<none, file download, or editable operations status>`

从 [`configuration.example.yaml`](./templates/configuration.example.yaml) 和 [`feature-map.example.md`](./skills/reproduce-and-fix-issues/references/feature-map.example.md) 开始。将其复制到本资料包之外并填写，例如放在 `.cursor/benny/` 下。秘密值应保存在秘密管理器或环境中。

<a id="for-the-agent"></a>
## 给智能体的说明

用户通过让 Cursor 阅读此文件来进入设置流程。不要查找或调用通过发现机制找到的 benny 斜杠技能。

1. 询问将在哪个仓库运行自动化。
2. 将包含此 `FOR_AGENTS.md` 的目录视为源资料包。
3. 将整个源资料包合并到 `<target-repository>/.cursor/automations/benny/`。
4. 保留目标独有的每个文件。绝不删除无关文件，也不覆盖用户自有的配置、功能映射或路由映射。
5. 如果源管理路径上的现有目标文件与源不同，应审查差异并合并，不能丢弃本地修改。如果归属不明确，应停止，并在替换前询问。
6. 验证目标仓库中存在复制后的 `FOR_AGENTS.md` 和 `skills/setup-benny/SKILL.md`。
7. 直接从目标仓库读取并遵循 `.cursor/automations/benny/skills/setup-benny/SKILL.md`。

我希望你将以下条目合并到目标仓库的 `.cursor/settings.json`：

```json
{
	"plugins": {
		"pstack": { "enabled": true }
	}
}
```

保留所有无关设置和插件。当现有文件使用 JSONC 时，应保留注释及有效的 JSONC 语法。

我希望由一个以目标仓库为根目录的全新智能体验证。确认 pstack 的 `how`、`why`、`tdd`、`unslop` 及 benny 使用的原则技能能在项目作用域中解析。不要将当前会话加载的技能或用户作用域安装的技能计入结果。

如果项目作用域插件不可用，或任何共享依赖无法解析，应停止并解释失败原因。不要将 `.cursor/automations/benny/skills/` 加入插件清单，也不要期待这些文件出现在斜杠技能列表中。

告诉我：启用任一自动化前，必须提交 `.cursor/settings.json`、`.cursor/automations/benny/` 以及引用到的所有不含秘密信息的配置。在我明确要求前，不要创建或更新自动化。

首次创建时，对分诊以及复现与修复分别使用一次内置 `/automate`。开始第二个自动化前，应先完成第一个自动化的草稿审阅、批准、就绪检查以及 Automations 编辑器交接。

将此意图和已完成的配置转述到每份草稿中。分诊提示词必须读取并遵循 `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md`。复现提示词必须读取并遵循 `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md`。只有 `/automate` 确认这些仓库相对路径已提交到自动化将运行的仓库后，才能使用它们。

对于已有自动化，不要使用 `/automate` 检查或更新。验证配置后，使用复制后的设置文件中的简明字段清单，让我直接在各自编辑器中修改自动化。不要创建重复项。
