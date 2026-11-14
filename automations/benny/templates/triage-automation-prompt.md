<a id="triage-automation-prompt"></a>
# 分诊自动化提示词

> 复制后设置流程所用的源材料。在内置 `automate` 确认复制的资料包已提交到自动化将运行的仓库后，将此意图转述为 `automate` 草稿。

本次运行应读取并遵循 `.cursor/automations/benny/skills/triage-issue-reports/SKILL.md`。

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

创建意图应将其描述为：配置的来源 Slack 频道中的新顶层报告。

将来源频道和根线程时间戳视为不可变。如果任一项缺失或与配置不符，应停止，不发消息，也不写入问题跟踪系统。

已提交的操作文件负责分类、附件审阅、原因追踪、路由、去重、跟踪系统写入和最终结论。不要发布进度消息。绝不在来源频道发布根消息。

协调者是唯一的 Slack 发消息者。任何受委派的工作者必须只读，只返回发现，并且收到明确禁止所有 Slack 写入操作的指令。

在唯一一次结论回复的末尾，添加恰好一个配置的标记：

```text
[benny:bug]
[benny:performance]
[benny:other]
```

缺陷或性能标记可以添加 `tracker=<URL>`。
