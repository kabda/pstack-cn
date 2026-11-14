---
name: setup-benny
description: 配置 Benny 并准备分诊和复现自动化。安装 Benny（setup Benny）或更改其 Slack、跟踪系统、仓库、路由、控制、模型或预算设置时使用。
disable-model-invocation: true
---

<a id="set-up-benny"></a>
# 设置 Benny

Benny 作为尚未启用的自动化资料包随 pstack 提供。插件清单仅暴露 pstack 的常规技能根目录；此文件和两个操作文件都不是斜杠技能。

用户通过让 Cursor 阅读资料包的 `FOR_AGENTS.md` 来进入设置流程。引导流程将整个资料包复制到目标仓库，然后直接读取 `.cursor/automations/benny/skills/setup-benny/SKILL.md` 处的此文件。

Benny 需要外部配置和两个实际启用的 Cursor 自动化。

在用户明确要求前，不要创建或更新自动化。绝不将秘密值放入插件文件、提示词或已提交的配置中。

<a id="1-copy-the-pack-and-enable-shared-pstack-skills"></a>
## 1. 复制资料包并启用共享 pstack 技能

在询问 Benny 配置和调用内置 `/automate` 技能之前，先完成此步骤。

询问将在哪个仓库运行自动化。源资料包是包含 `FOR_AGENTS.md` 的目录。目标位置为 `<target-repository>/.cursor/automations/benny/`。

将整个源资料包合并到目标位置：

1. 目标不存在时创建它。
2. 将每个源文件复制到相同相对路径。
3. 保留目标独有的文件。安装或刷新时绝不删除无关文件。
4. 将用户自有配置、功能映射和路由映射保存在目标目录之外。绝不覆盖它们。
5. 如果现有的源管理文件存在差异，检查差异并合并，不能丢弃本地修改。如果归属不明确，停止并在替换前询问。
6. 验证目标包含 `FOR_AGENTS.md`、此设置文件、两个操作文件、各自的参考材料和模板。

如果当前已从目标位置读取此文件，将复制视为完成，并在继续前进行相同验证。

将 pstack 加入目标仓库的 `.cursor/settings.json`。如果文件或 `.cursor` 目录不存在，创建它。

将以下条目合并到现有 JSON 或 JSONC 中：

```json
{
	"plugins": {
		"pstack": { "enabled": true }
	}
}
```

保留每个无关的顶层设置和其他插件条目。如果 `plugins.pstack` 已存在，仅更改其 `enabled` 值。文件使用 JSONC 时，保留注释和有效的 JSONC 语法。编辑后验证文件。

重新加载目标项目，或启动以该项目为根目录的全新智能体。验证以下共享 pstack 技能可从项目作用域解析：

- `how`
- `why`
- `tdd`
- `unslop`
- `principle-separate-before-serializing-shared-state`
- `principle-minimize-reader-load`
- `principle-guard-the-context-window`
- `principle-sequence-verifiable-units`
- `principle-fix-root-causes`
- `principle-prove-it-works`

不要将当前会话加载的技能或用户作用域插件计入结果。检查必须表明：目标仓库中的全新智能体通过项目设置获得了 pstack。

如果项目作用域插件安装不可用，或任何共享依赖无法解析，停止并解释失败。

Benny 文件直接从 `.cursor/automations/benny/` 读取。不要将此目录加入插件清单，也不要期待其 `SKILL.md` 文件出现在斜杠技能列表中。

告诉用户：启用任一自动化前，必须提交 `.cursor/settings.json`、`.cursor/automations/benny/` 和所有引用到的不含秘密信息的配置。除非用户要求，否则不要提交。

此检查通过后，实际自动化提示词可以通过稳定的仓库相对路径读取已提交的操作文件。它们绝不能嵌入插件缓存路径，也不能复制文件内容。

<a id="2-adapt-the-configuration"></a>
## 2. 调整配置

打开以下已复制的示例：

- `../../templates/configuration.example.yaml`
- `../reproduce-and-fix-issues/references/feature-map.example.md`

在 `.cursor/automations/benny/` 之外创建用户自有副本。这些是配置文件，不是资料包文件。示例位置：

- 项目配置，例如 `.cursor/benny/configuration.yaml`
- 项目功能映射，例如 `.cursor/benny/feature-map.md`
- 项目路由映射，例如 `.cursor/benny/routing.md`
- 用户配置，例如 `~/.config/benny/configuration.yaml`
- 用户功能映射，例如 `~/.config/benny/feature-map.md`

为自动化可能复现的每个面向用户的功能填写一个功能映射章节。保持用户视角，不要在映射中固定实现细节或当前代码路径。

不要编辑复制包中的示例。资料包刷新在审查冲突后可以更新源管理文件，但绝不能触碰用户自有副本。

当全新的自动化检出需要读取这些文件时，优先使用目标仓库中已提交、不含秘密信息的文件。否则将所需值转述到实际提示词中。只有内置 `/automate` 技能确认文件已提交到自动化运行的仓库后，才能引用该仓库文件。

已提交的资料包和配置文件使用稳定的仓库相对路径。绝不在实际自动化中引用插件源目录或插件缓存路径。

<a id="3-fill-the-required-choices"></a>
## 3. 填写必需选项

询问或确认：

- 来源 Slack 频道 ID
- 可选的运维或状态频道 ID
- 仓库 URL 和默认分支
- 分诊身份或 Slack 用户 ID
- 问题跟踪系统类型、团队、项目、标签和受理状态
- 跟踪系统适配器技能或 MCP 操作
- 可选路由映射路径
- 必需的控制技能名称
- 必需的面向用户的功能映射路径
- 状态 emoji 字符串
- 拉取请求 URL 格式
- 轮询和投入预算
- 分诊、复现、代码工作和媒体审阅的模型 slug

仅使用用户 Cursor 模型选择器或受支持模型列表显示可用的模型 slug。不要猜测 slug，也不要沿用私有默认值。

来源频道、分诊身份、仓库、跟踪系统适配器、控制技能和功能映射必须明确。如果任何必需值仍有歧义，设置应失败。

保存前，对最终自动化名称、描述和提示词衔接层使用 pstack 的 `unslop` 技能。

<a id="4-check-integration-capabilities"></a>
## 4. 检查集成能力

分诊自动化需要：

- 对配置的来源 Slack 频道及其线程的读取权限
- 在该频道内回复线程的权限
- 报告包含媒体时所需的附件元数据和文件下载权限
- 通过配置的问题跟踪系统适配器进行搜索、读取、创建和更新的权限

复现自动化需要：

- 来源线程读取权限
- 来源频道内回复线程的权限
- 配置的运维频道中可选的发消息和编辑权限
- 仓库读取及历史访问权限
- 能打开草稿拉取请求的拉取请求操作
- 配置的控制适配器技能

读取和发消息优先使用配置的 Cursor Slack 操作。可选的 `BENNY_SLACK_BOT_TOKEN` 可以填补小范围能力缺口，例如编辑一条运维状态消息或下载附件。将值保存在秘密管理器或环境中，不放入 YAML。

不要使用无文档的集成端点。

<a id="5-prepare-the-routing-map"></a>
## 5. 准备路由映射

如果用户需要转交或 @ 负责人：

1. 将 `../triage-issue-reports/references/routing.example.md` 复制到 `.cursor/automations/benny/` 之外。
2. 用公开值或组织内部值替换每个占位符。
3. 默认保持负责人 @ 关闭。
4. 仅允许 @ 配置的功能负责人，或已确认很可能引入回归的作者。

如果未配置路由映射，分诊可以对报告分类，但绝不能猜测去向或负责人。

<a id="6-verify-the-control-adapter"></a>
## 6. 验证控制适配器

读取 `../reproduce-and-fix-issues/references/control-adapter.md` 和用户已完成的功能映射。

确认指定技能能够：

- 启动目标应用
- 通过真实 UI 导航到每个映射功能
- 通过声明的适配器操作来操作映射状态
- 检查状态而不强制制造结果
- 采集截图
- 开始和停止录屏
- 清理其进程和临时数据

如果任何能力缺失，保持复现自动化禁用。它必须以关闭方式失败，不能宣称完成了未执行的复现。

<a id="7-prepare-the-live-automations"></a>
## 7. 准备实际自动化

询问这是首次创建，还是配置已有自动化。

无论哪条路径，都读取复制资料包中的 `../../FOR_AGENTS.md`，作为主要用户意图来源。通过它理解两个触发器、工具、指令、结果和共同规则。

<a id="first-time-creation"></a>
### 首次创建

一次创建一个自动化。

对每个自动化：

1. 读取对应的已复制提示词模板，作为次要内部源材料。
2. 将 `FOR_AGENTS.md`、已完成的 Benny 配置和模板意图转化为完整的自然语言请求。
3. 指示实际提示词读取并遵循 `.cursor/automations/benny/` 下确切的已提交操作文件。
4. 使用稳定的仓库相对路径，不用插件源路径或缓存路径。不要将操作文件内容复制到实际提示词中。
5. 读取并遵循内置 `automate` 技能。
6. 让 `automate` 发现 Slack 频道、仓库和已连接集成。
7. 让 `automate` 确认复制的资料包及所有被引用的配置文件已提交到自动化将运行的同一个仓库中。
8. 让 `automate` 展示草稿表、取得批准、询问就绪情况，并打开 Automations 编辑器。
9. 完成这个自动化的编辑器交接后，才开始下一个。

向 `automate` 提供以下完整分诊意图，值从配置填写：

- 名称为 `benny-triage`。
- 每次运行读取并遵循 `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md`。
- 由配置的来源 Slack 频道中每条新的顶层报告触发。
- 读取触发线程，只在该线程内回复。
- 使用配置的问题跟踪系统集成。
- 分类、检查证据、追踪原因、去重，仅为明确的新缺陷创建工单。
- 在线程内唯一一次结论的末尾加上配置的 `[benny:bug]`、`[benny:performance]` 或 `[benny:other]` 标记，以及可选跟踪系统 URL。
- 绝不发布来源频道根消息。

完成分诊编辑器交接后，向 `automate` 提供以下完整复现与修复意图：

- 名称为 `benny-reproduce`。
- 每次运行读取并遵循 `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md`。
- 由配置的来源 Slack 频道中同样的新顶层报告触发。
- 使用配置的仓库和默认分支。
- 读取来源线程，只在该线程内回复。
- 包含拉取请求创建权限，以及配置的跟踪系统、控制适配器和功能映射要求。除非 `automate` 确认同一仓库中有符合条件的已提交文件，否则应转述映射的用户路径和状态。
- 行动前等待可信的分诊标记。
- 通过映射的真实 UI 将确切症状复现两次，并采集证据。
- 验证现有修复，不在其基础上另行编写改动。
- 仅在确认复现后尝试可选的有限修复，再于证据和检查通过后打开草稿拉取请求。
- 绝不发布来源频道根消息。

不要重复 `automate` 所负责的 Slack、仓库、集成、完整性、身份验证、草稿审阅、批准、就绪或编辑器交接工作。

<a id="existing-automations"></a>
### 已有自动化

内置 `automate` 技能仅用于创建。不要用它搜索、检查或更新已有自动化。

完成配置、路由、控制适配器和功能映射验证。然后向用户提供以下简明编辑器清单。

对已有分诊自动化，更新：

- 名称和描述
- 直接读取 `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md` 的指令
- 新顶层 Slack 报告触发器及来源频道
- Slack 线程读取和回复能力
- 问题跟踪系统集成
- 转述后的分诊指令、仅在线程内发消息的规则和 Benny 结论标记

对已有复现自动化，更新：

- 名称和描述
- 直接读取 `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md` 的指令
- 匹配的 Slack 触发器及来源频道
- 仓库和默认分支
- Slack 线程读取和回复能力
- 拉取请求操作
- 跟踪系统、控制适配器和功能映射要求
- 转述后的标记等待、证据、验证和有限修复指令

让用户直接在各自的 Automations 编辑器中更新已有自动化。不要创建替代项或重复项。

<a id="creation-boundary"></a>
### 创建边界

绝不调用直接的自动化后端服务或后端自动化工具。绝不使用携带草稿字段的浏览器 URL。绝不构建或打开 Cursor 协议深链接。对于新自动化，唯一的完成路径是内置 `automate` 技能经过审阅的 Automations 编辑器交接。

编辑器保存后，在通过线程安全测试之前，不要启用任一自动化。

<a id="8-test-thread-safety"></a>
## 8. 测试线程安全

使用测试频道或无害测试报告。

测试前，确认目标仓库的 `.cursor/settings.json`、`.cursor/automations/benny/` 和所有引用到的不含秘密信息的配置文件，已提交到自动化检出所用的分支。确认两个实际提示词都指向各自确切的已提交操作文件。任何检查失败，都应停止。告诉用户自动化尚不能启用。

验证：

1. 分诊保存根 `thread_ts`，并且恰好发布一次结论，形式为回复。
2. 结论包含一个配置的标记。
3. 复现仅接受配置的分诊身份发出的标记。
4. 复现保留相同的不可变来源坐标。
5. 没有出现来源频道根消息。
6. 受委派工作者无法使用任何 Slack 写入操作。
7. 坐标缺失、父消息已删除或预检失败时，不发消息，也不创建跟踪工单。

只有七项检查全部通过后，才启用正常流量。
