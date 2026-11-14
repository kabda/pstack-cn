<a id="create-a-note"></a>

# 创建笔记

创建笔记功能让用户通过浏览器或 CLI 保存有标题的笔记，取消未完成草稿，并从第二个用户可见视图确认笔记已保存。

## Sub-features

子功能：

- `create-open`：从每个浏览器入口打开空白编辑器。
- `create-save`：持久保存标题和正文。
- `create-cancel`：丢弃未完成的浏览器草稿。
- `create-cli`：从终端创建相同结构的笔记。

## How to get to it (user POV)

用户入口：

- 选择浏览器工具栏的 `New note`（新建笔记）按钮。
- 浏览器焦点不在可编辑字段中时按 `n`。
- 在终端运行 `notes create --title <title> --body <body>`。

## Driving it with control-notes

Preconditions:

使用 control-notes 驱动；前置条件：

- Notes 在 `http://127.0.0.1:4173` 健康运行。
- 不存在标题为 `Release checklist`（发布检查表）的笔记。
- `control-notes doctor` 报告预期 URL 和一次性数据目录。

- **打开编辑器。** 选择 `New note`。运行 `control-notes browser click --role button --name "New note"`。出现名为 `Note editor`（笔记编辑器）的表单，焦点位于 `Title`（标题）文本框。
- **输入内容。** 输入标题和正文；正文 `Tag and publish` 意为“打标签并发布”。运行 `control-notes browser fill --role textbox --name "Title" --value "Release checklist"` 和 `control-notes browser fill --role textbox --name "Body" --value "Tag and publish"`。`Save note`（保存笔记）按钮变为可用。
- **保存笔记。** 选择 `Save note`。运行 `control-notes browser click --role button --name "Save note"`。出现名为 `Note saved`（笔记已保存）的状态，标题显示 `Release checklist`。
- **确认持久化。** 返回笔记列表并重新打开笔记。运行 `control-notes browser click --role link --name "All notes"` 和 `control-notes browser click --role link --name "Release checklist"`。编辑器展示两个已保存的值。
- **取消草稿。** 打开新笔记，输入 `Discard me`（丢弃我），选择 `Cancel`（取消）。运行 `control-notes browser click --role button --name "New note"`、`control-notes browser fill --role textbox --name "Title" --value "Discard me"` 和 `control-notes browser click --role button --name "Cancel"`。返回笔记列表，不存在 `Discard me` 链接。
- **CLI 入口。** 创建第二份笔记，标题 `CLI note` 意为“CLI 笔记”，正文 `Created from terminal` 意为“从终端创建”。运行 `control-notes cli -- notes create --title "CLI note" --body "Created from terminal" --format json`。退出码为 `0`，stdout 包含新笔记 ID 和标题。
- **证明。** 从 `All notes`（全部笔记）重新打开两份已保存笔记。运行 `control-notes browser snapshot --aria --path artifacts/create-note/list.aria.txt` 和 `control-notes browser screenshot --path artifacts/create-note/list.png`。产物显示 `Release checklist` 和 `CLI note`。

## Gotchas

注意事项：

- 文本框有焦点时，按 `n` 会输入字符，不会打开新编辑器。
- 保存时会去掉标题首尾空白。断言渲染后的标题，而非草稿输入值。
- 单独一个保存状态不足以证明成功，必须从列表重新打开笔记。
- 清理测试夹具时移除 `Release checklist` 和 `CLI note`，但保留其证明产物。
