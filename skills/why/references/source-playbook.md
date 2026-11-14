<a id="source-playbooks"></a>
# 来源操作手册

why 技能为每个可用证据类别派生一名调查者，各自阅读下面唯一的来源专属操作手册。这些手册是常见 MCP 的具体示例。同类别的其他 MCP 可以据此调整。

| 类别 | 操作手册 | 手册记录的示例 MCP |
|---|---|---|
| 源代码管理历史 | [`code-archaeology.md`](./sources/code-archaeology.md) | Git、`gh` |
| 问题／工单跟踪系统 | [`linear.md`](./sources/linear.md) | Linear（可调整用于 Jira、GitHub Issues、Plane、Shortcut） |
| 长篇文档 | [`notion.md`](./sources/notion.md) | Notion（可调整用于 Confluence、Google Docs、Coda） |
| 团队实时聊天 | [`slack.md`](./sources/slack.md) | Slack（可调整用于 Discord、Microsoft Teams、Mattermost） |
| 基础设施可观测性 | [`datadog.md`](./sources/datadog.md) | Datadog（可调整用于 New Relic、Honeycomb、Grafana、Splunk） |
| 错误／异常跟踪 | [`sentry.md`](./sources/sentry.md) | Sentry（可调整用于 Rollbar、Bugsnag、Airbrake） |
| 产品分析数据仓库 | [`databricks.md`](./sources/databricks.md) | Databricks SQL（可调整用于 Snowflake、BigQuery、ClickHouse、dbt） |

跨类别补充：

- [`incident-postmortem.md`](./sources/incident-postmortem.md)。目标代码看起来具有防御性时加入（空值检查、重试、超时、限流、功能标志、出站防护、OOM 处理器）。
