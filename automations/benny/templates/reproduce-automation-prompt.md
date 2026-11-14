<a id="reproduce-automation-prompt"></a>
# 复现自动化提示词

> 复制后设置流程所用的源材料。在内置 `automate` 确认复制的资料包已提交到自动化将运行的仓库后，将此意图转述为 `automate` 草稿。

本次运行应读取并遵循 `.cursor/automations/benny/skills/reproduce-and-fix-issues/SKILL.md`。

配置来源。只有该仓库相对路径已提交到同一个目标仓库时才包含它，否则应转述配置值。绝不使用插件源路径或缓存路径：

```text
{{BENNY_CONFIG_PATH}}
```

触发器：

```json
{
	"source_channel_id": "{{SLACK_CHANNEL_ID}}",
	"message_ts": "{{SLACK_MESSAGE_TS}}",
	"thread_ts": "{{SLACK_THREAD_TS_OR_EMPTY}}"
}
```

创建意图应将其描述为：配置的来源 Slack 频道中的新顶层报告。应包含配置的仓库、默认分支、问题跟踪系统、控制适配器、功能映射及草稿拉取请求能力。

将来源频道和根线程时间戳视为不可变。如果任一项缺失或与配置不符，应停止，不发消息。

在这个确切的线程中等待配置的分诊身份发出配置的分诊标记。仅当出现 `[benny:bug]` 或 `[benny:performance]` 时继续。

尝试复现之前，必须具备配置的控制适配器技能。通过真实 UI 将完全相同、能区分该问题的症状复现两次。验证现有拉取请求或提交，不在其基础上另行编写改动。只有确认复现并通过操作文件的修复门禁后，才尝试有明确边界的修复。

协调者是唯一的 Slack 发消息者。每个子代理提示词必须禁止 `SendSlackMessage`、`PostToSlack`、`chat.postMessage` 以及其他一切 Slack 写入。子代理只返回发现。

绝不在来源频道发布根消息。
