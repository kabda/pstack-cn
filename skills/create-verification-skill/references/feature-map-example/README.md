<a id="notes-verification-map"></a>

# Notes 验证地图

本目录是持续维护的 Notes 用户行为验证来源。驱动应用前先读索引，再使用对应功能文件中的操作步骤。

<a id="baseline-preconditions"></a>

## 基线前置条件

- 使用一次性数据目录，在 `http://127.0.0.1:4173` 启动 Notes。
- 设置 `NOTES_DATA_DIR=/tmp/notes-verify-$RUN_ID`，避免并行运行共享状态。
- 播种标题为 `Quarterly plan`（季度计划）和 `Grocery list`（购物清单）的笔记。
- 将 `control-notes` 和 `notes` CLI 加入 `PATH`。
- 运行 `control-notes doctor`，要求 URL、数据目录和构建版本符合预期。
- 绝不驱动并非由本次验证启动的实例。

<a id="driving-conventions"></a>

## 驱动约定

- 除非前置条件另有说明，每份步骤都从基线状态开始。
- 优先使用 ARIA 角色和无障碍名称，而非 CSS 选择器或 DOM 位置。
- 所有命令均按字面执行。引号中的名称和参数保持原样。
- 浏览器动作通过 `control-notes browser` 运行。
- 终端动作通过 `control-notes cli -- <command>` 运行。
- 修改后恢复种子数据。清理时不要移除证明产物。

<a id="proof-and-skip-reporting"></a>

## 证明与跳过报告

- 捕获用户动作及结果状态，不能只有最终屏幕。
- UI 证明包含 ARIA 快照和能看到应用身份的截图。
- CLI 证明包含命令、stdout、stderr 和退出码。
- 修改证明包含通过第二个只读视图核对存储值的结果。
- 每份产物都记录功能 ID 和所用入口。
- 路径无法到达时，报告尝试的命令和未满足前置条件。
- 不要把跳过的入口描述为已由其他路径验证。

<a id="feature-entry-contract"></a>

## 功能条目约定

每份功能文件以 H1 标题和一个描述用户可见行为的段落开头。随后严格按顺序使用四个 H2 章节。

1. `Sub-features`（子功能）列出简短 ID，每个行为一行。
2. `How to get to it (user POV)`（用户如何进入）列出所有用户入口。
3. `Driving it with <harness>`（使用指定运行工具驱动）以 `Preconditions:`（前置条件）开头，使用带标签的列表项，将每个用户动作与精确命令、可观察结果配对。
4. `Gotchas`（注意事项）列出可能浪费验证时间或使验证失效的陷阱。

功能映射不写实现细节。只写用户路径、稳定定位方式、必要状态、命令和可观察证明。

<a id="features"></a>

## 功能

- [创建笔记](./create-note.md)：覆盖浏览器与 CLI 创建、取消、持久化和清理。
- [搜索笔记](./search.md)：覆盖工具栏、键盘与 CLI 搜索，以及匹配、空结果和清空状态。
