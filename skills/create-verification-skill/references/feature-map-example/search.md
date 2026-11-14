<a id="search-notes"></a>

# 搜索笔记

搜索功能让用户按标题或正文查找笔记，查看匹配笔记，并区分“没有匹配项”和“搜索不可用”。

## Sub-features

子功能：

- `search-open`：从每个受支持浏览器入口打开搜索。
- `search-match`：返回标题与正文匹配项，不修改笔记数据。
- `search-open-result`：在笔记编辑器中打开结果。
- `search-empty`：查询无匹配项时显示完整空状态。
- `search-clear`：移除查询，恢复最近笔记视图。
- `search-cli`：从终端返回相同匹配笔记。

## How to get to it (user POV)

用户入口：

- 选择浏览器工具栏的 `Search`（搜索）按钮。
- 浏览器焦点不在可编辑字段中时按 `/`。
- 在终端运行 `notes search <query>`。

## Driving it with control-notes

Preconditions:

使用 control-notes 驱动；前置条件：

- Notes 在 `http://127.0.0.1:4173` 健康运行。
- 一次性数据目录含有 `Quarterly plan`（季度计划），正文为 `Draft budget`（预算草稿）。
- `control-notes doctor` 报告预期 URL 和数据目录。

- **工具栏入口。** 选择 `Search`。运行 `control-notes browser click --role button --name "Search"`。出现名为 `Search notes`（搜索笔记）的对话框，焦点在搜索框。
- **键盘入口。** 关闭对话框，将焦点放在页面上，按 `/`。运行 `control-notes browser press --key "/"`。出现同一对话框，页面不插入斜杠。
- **标题匹配。** 输入 `quarterly`。运行 `control-notes browser fill --role searchbox --name "Search notes" --value "quarterly"`。`Search results`（搜索结果）列表包含 `Quarterly plan`，不包含 `Grocery list`。
- **正文匹配。** 把查询换为 `budget`。运行 `control-notes browser fill --role searchbox --name "Search notes" --value "budget"`。`Quarterly plan` 结果仍可见，并显示正文匹配摘要。
- **打开结果。** 选择 `Quarterly plan`。运行 `control-notes browser click --role link --name "Quarterly plan"`。对话框关闭，编辑器标题为 `Quarterly plan`。
- **空状态。** 重新打开搜索，输入 `volcano`。运行 `control-notes browser fill --role searchbox --name "Search notes" --value "volcano"`。搜索完成后出现名为 `No matching notes`（没有匹配笔记）的状态。
- **清空查询。** 选择 `Clear search`（清空搜索）。运行 `control-notes browser click --role button --name "Clear search"`。搜索框为空，`Recent notes`（最近笔记）区域替代结果列表。
- **CLI 匹配。** 从终端搜索。运行 `control-notes cli -- notes search "quarterly" --format json`。退出码为 `0`，stdout 包含一个标题为 `Quarterly plan` 的对象。
- **CLI 无匹配。** 搜索不存在的值。运行 `control-notes cli -- notes search "volcano" --format json`。退出码为 `0`，stdout 为 `[]`。
- **证明。** 捕获有结果的状态。运行 `control-notes browser snapshot --aria --path artifacts/search/results.aria.txt` 和 `control-notes browser screenshot --path artifacts/search/results.png`。两份产物都标明 Notes、查询和 `Quarterly plan`。

## Gotchas

注意事项：

- 编辑器或搜索框有焦点时，按 `/` 会插入文本，不会打开搜索。
- 结果在短暂防抖后更新。等待结果列表或空状态，不要固定休眠。
- 除非用户启用 `Include archived`（包含已归档），否则结果不含已归档笔记。
- CLI 默认输出供人阅读。用 `--format json` 获得稳定断言。
- 打开结果会改变浏览器状态。证明另一个查询前，重新打开搜索。
