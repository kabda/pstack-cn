<a id="benny"></a>
# benny

benny 为 Slack 问题报告提供两个 Cursor 自动化。一个对每条报告进行分诊；另一个复现已确认的缺陷，并可准备一个小范围修复的草稿。

本目录中的文件是尚未启用的设置和自动化源材料。它们不会出现在斜杠技能列表中。

<a id="set-it-up"></a>
## 设置方法

1. 让 Cursor 阅读 [`FOR_AGENTS.md`](./FOR_AGENTS.md)，并指定目标仓库。
2. 让设置流程将整个目录合并到目标仓库的 `.cursor/automations/benny/`。它必须保留目标独有的文件，并审查冲突，不能覆盖本地修改。
3. 让设置流程在目标仓库的 `.cursor/settings.json` 中启用 pstack，以使用共享依赖：

```json
{
	"plugins": {
		"pstack": { "enabled": true }
	}
}
```

4. 将用户自有配置保存在复制的资料包之外，例如 `.cursor/benny/`。根据需要调整 [`configuration.example.yaml`](./templates/configuration.example.yaml) 和 [`feature-map.example.md`](./skills/reproduce-and-fix-issues/references/feature-map.example.md)。
5. 在启用任一自动化之前，提交 `.cursor/settings.json`、`.cursor/automations/benny/` 以及所有不含秘密信息的配置。
6. 审阅每个新自动化的草稿，或在编辑器中更新现有自动化。然后发送一条无害的测试报告，确认在来源频道发布的每条消息都留在原始线程中。
