<a id="incident--postmortem-context"></a>
# 事故与复盘背景

- **Linear**：查找带 `incident`、`sev-*`、`postmortem-action-item`、`reliability` 标签的工单
- **Slack**：在目标代码添加日期前后，搜索 `#sev-*` 和 `#incident-*` 频道
- **Git**：消息类似 “fix for incident”（事故修复）、“add defensive check”（添加防御性检查）、“revert”（回退），随后又有 “re-apply with...” （重新应用并……）的提交，是强烈信号
