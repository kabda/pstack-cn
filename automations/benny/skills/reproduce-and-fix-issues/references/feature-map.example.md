<a id="feature-map-example"></a>
# 功能映射示例

映射 Benny 可能复现的每个面向用户的功能。操作应用前，阅读相关章节。映射应保持用户视角。运行时再发现内部实现和当前代码路径，不要在这里将其固定。

将此文件复制到 `.cursor/automations/benny/` 之外，例如 `.cursor/benny/feature-map.md`，并将 `control.feature_map_path` 指向副本。资料包刷新时绝不能覆盖它。

<a id="per-feature-template"></a>
## 单功能模板

### `<feature name>`

`<one-line user-visible purpose>`

<a id="how-a-user-gets-there"></a>
#### 用户如何到达

- 点击路径：`<screen> -> <menu, tab, or panel> -> <control>`
- 键盘快捷键：`<shortcut or none>`

<a id="how-the-control-adapter-drives-it"></a>
#### 控制适配器如何操作

- `<adapter action>` 带 `<inputs>` 应当产生 `<visible result>`。
- 重置：`<how the adapter returns to a fresh state>`。

<a id="stable-selectors"></a>
#### 稳定选择器

- `<role and accessible name>`
- `<ARIA relationship>`
- `<data-component or purpose-named data attribute>`

绝不使用生成的 CSS 或 StyleX 类、动态哈希、子元素索引或脆弱的 DOM 位置。

<a id="states-to-exercise"></a>
#### 要操作的状态

- Default（默认）、hover（悬停）、focus-visible（焦点可见）、active（激活）、disabled（禁用）
- Loading（加载中）、empty（空）、error（错误）
- Selected（已选）、open（打开）、expanded（展开）
- `<relevant feature-specific variants>`

标明不适用的状态。

<a id="preconditions-and-setup"></a>
#### 前置条件与设置

- 身份验证：`<account state>`
- 数据：`<fixture>`
- 权限：`<role>`
- 标志：`<flag or none>`
- 服务：`<required availability>`

<a id="evidence-and-cross-check"></a>
#### 证据与交叉核验

- 截图：`<app identity, feature, and discriminating state>`
- 视频：`<entry path, interaction, and final state>`
- 交叉核验：`<read-only state or value that confirms the UI>`

<a id="gotchas"></a>
#### 易错点

- `<known dead end or wrong surface>`
- `<safe environment translation>`

<a id="fictional-example"></a>
## 虚构示例

这些功能属于一个虚构的任务应用，仅为示例，不是 Benny 必须具备的功能。

<a id="sign-in"></a>
### 登录

让用户进入任务应用。

<a id="how-a-user-gets-there-1"></a>
#### 用户如何到达

- 打开应用，选择 `Sign in`（登录）。无快捷键。

<a id="how-the-control-adapter-drives-it-1"></a>
#### 控制适配器如何操作

- `open_app`、`click Sign in`、`fill credentials` 和 `click Continue`（点击“继续”）应打开条目列表。
- 通过退出登录并清除一次性会话来重置。

<a id="stable-selectors-1"></a>
#### 稳定选择器

- 按钮 `Sign in`，文本框 `Email`（电子邮件）和 `Password`（密码），`data-component="sign-in-form"`

<a id="states-to-exercise-1"></a>
#### 要操作的状态

- Default（默认）、focus-visible（焦点可见）、submitting（提交中）、disabled（禁用）、loading（加载中）、error（错误）

<a id="preconditions-and-setup-1"></a>
#### 前置条件与设置

- 一次性账号以及可用的身份验证服务

<a id="evidence-and-cross-check-1"></a>
#### 证据与交叉核验

- 录制从落地页到条目列表的过程。检查只读会话状态。

<a id="gotchas-1"></a>
#### 易错点

- 营销页面不是正确界面。缺少身份验证服务属于阻塞。

<a id="item-list-and-detail"></a>
### 条目列表和详情

让用户浏览并打开一个条目。

<a id="how-a-user-gets-there-2"></a>
#### 用户如何到达

- 打开 `Items`（条目）选项卡，然后选择一行。

<a id="how-the-control-adapter-drives-it-2"></a>
#### 控制适配器如何操作

- `select_tab Items` 和 `click <fixture item>` 应打开其详情。
- 关闭详情并清除选择以重置。

<a id="stable-selectors-2"></a>
#### 稳定选择器

- 名为 `Items` 的选项卡和列表、按测试夹具命名的行、`data-component="item-detail"`

<a id="states-to-exercise-2"></a>
#### 要操作的状态

- Loading（加载中）、empty（空）、error（错误）、selected（已选）、open（打开）、expanded（展开）

<a id="preconditions-and-setup-2"></a>
#### 前置条件与设置

- 有名称的测试夹具条目、读取权限、可用的条目服务

<a id="evidence-and-cross-check-2"></a>
#### 证据与交叉核验

- 展示选择和匹配的详情标题。检查所选条目 ID。

<a id="gotchas-2"></a>
#### 易错点

- 搜索结果看起来可能相似，但路径不同。

<a id="item-editor"></a>
### 条目编辑器

让用户创建或编辑条目。

<a id="how-a-user-gets-there-3"></a>
#### 用户如何到达

- 从详情选择 `Edit`（编辑），或从列表选择 `New item`（新建条目）。

<a id="how-the-control-adapter-drives-it-3"></a>
#### 控制适配器如何操作

- `click Edit`、`fill <field>` 和 `click Save`（点击“保存”）应更新详情。
- 恢复测试夹具以重置。

<a id="stable-selectors-3"></a>
#### 稳定选择器

- 按钮 `Edit`、`New item`、`Save`，表单 `Item editor`（条目编辑器），与标签关联的字段

<a id="states-to-exercise-3"></a>
#### 要操作的状态

- Default（默认）、focus-visible（焦点可见）、dirty（已修改）、validating（校验中）、disabled（禁用）、saving（保存中）、error（错误）、success（成功）

<a id="preconditions-and-setup-3"></a>
#### 前置条件与设置

- 可编辑测试夹具、写入权限、可用的保存服务

<a id="evidence-and-cross-check-3"></a>
#### 证据与交叉核验

- 展示从字段改动到详情更新的过程。只读检查已存储条目值。

<a id="gotchas-3"></a>
#### 易错点

- 不要注入表单状态。只读详情字段不是编辑器。

<a id="settings"></a>
### 设置

让用户修改个人偏好。

<a id="how-a-user-gets-there-4"></a>
#### 用户如何到达

- 打开个人资料菜单，然后选择 `Settings`（设置）。

<a id="how-the-control-adapter-drives-it-4"></a>
#### 控制适配器如何操作

- `open_menu Profile`（打开“个人资料”菜单）、`click Settings` 和 `toggle <preference>` 应更新控件。
- 恢复初始偏好以重置。

<a id="stable-selectors-4"></a>
#### 稳定选择器

- 按钮 `Profile`，菜单项 `Settings`，区域 `Settings`，按用途命名的偏好属性

<a id="states-to-exercise-4"></a>
#### 要操作的状态

- Closed（关闭）、open（打开）、selected（已选）、focus-visible（焦点可见）、disabled（禁用）、loading（加载中）、error（错误）

<a id="preconditions-and-setup-4"></a>
#### 前置条件与设置

- 已登录的测试账号、已知偏好、可用的偏好服务

<a id="evidence-and-cross-check-4"></a>
#### 证据与交叉核验

- 展示菜单路径和最终控件状态。只读检查偏好值。

<a id="gotchas-4"></a>
#### 易错点

- 操作系统设置是另一个界面。

<a id="completeness-checklist"></a>
## 完整性检查清单

- 每个可复现的面向用户的功能都有章节。
- 每章都列出用户路径、适配器操作和重置方法。
- 选择器使用角色、名称、ARIA、稳定组件标记或按用途命名的属性。
- 没有选择器使用生成的类或 DOM 位置。
- 覆盖相关交互、加载、空、错误、选中和展开状态。
- 明确身份验证、测试夹具、权限、标志和服务。
- 明确截图、视频及底层交叉核验要求。
- 列出错误界面、死路和安全的环境等效转换。
- 实现细节留待运行时发现。
