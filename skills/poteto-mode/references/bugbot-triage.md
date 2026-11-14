<a id="bugbot-triage"></a>

# Bugbot 分类处理

Babysit（跟进 PR） 操作手册（`../playbooks/babysit.md`）处理 Bugbot 或审查自动化评论时，使用本参考。目标不是默认忽略 Bugbot，而是不再把每条评论都当作必须改代码的要求。

<a id="decision-rubric"></a>

## 决策准则

行动前先分类每个 Bugbot 讨论：

- `fix`（修复）：评论指出可信的正确性、安全、隐私、数据丢失、认证、计费、迁移、幂等、竞态或已交付行为问题。在最底层所属 PR 修复，再回复提交 SHA 并解决讨论。
- `dismiss`（驳回）：评论符合有记录的低风险噪声模式，当前代码或上下文证明无需改代码。简短说明理由并解决讨论。
- `ask`（询问）：评论新颖、严重程度高、涉及安全 / 隐私 / 数据，或含义模糊。询问用户，不要猜。

拿不准就问。略过有噪声的代码质量评论代价很低；略过真实数据或安全缺陷代价很高。

<a id="learned-pattern-format"></a>

## 经验模式格式

将来的模式按以下形式添加。`candidate`、`recurring`、`strong` 是置信度值，保留原样：

```markdown
### <short pattern name>

- 置信度：candidate | recurring | strong
- 可跳过条件：<conditions that must be true>
- 不可跳过条件：<risk boundaries>
- 示例信号：<phrases or code context that identify the pattern>
- 来源：<PR/comment URL or short historical note>
```

模式名要简短；可跳过条件是必须成立的条件；不可跳过条件是风险边界；示例信号是识别模式的措辞或代码上下文；来源填 PR / 评论 URL 或简短历史说明。

只有一两个例子时用 `candidate`；多次真实驳回后用 `recurring`；只有模式范围窄、反复验证且低风险时才用 `strong`。

<a id="recurring-skip-candidates"></a>

## 反复出现的可跳过候选模式

<a id="intentional-ui-or-design-system-visual-changes"></a>

### 有意的 UI 或设计系统视觉变更

- 置信度：candidate
- 可跳过条件：PR 描述、截图、设计审查或附近代码已明确视觉改动，Bugbot 评论只是重述共享视觉默认值发生变化。
- 不可跳过条件：评论指出无障碍、焦点可见性、键盘导航、颜色对比度，或 PR 未有意修改的组件 API 契约。
- 示例信号：关于焦点轮廓、按钮尺寸、间距、共享组件视觉默认值的评论，而负责人回复 “intentional” 或 “intended”（有意如此）。

<a id="upstack-or-stack-local-usage-bugbot-cannot-see"></a>

### Bugbot 看不到的上层或栈内用法

- 置信度：candidate
- 可跳过条件：Bugbot 将导出、组件、辅助函数或文件标为未使用，而当前托管平台的 PR 列表和 diff、栈上层 diff 或 PR 上下文显示，栈中后续 PR 会使用它。
- 不可跳过条件：当前 PR 不属于 PR 栈，符号是公开 API，或所谓上层用法无法验证。
- 示例信号：“Exported component is never used”（导出组件从未使用），人类回复类似 “used upstack”（在栈上层使用）。

<a id="temporary-duplication-during-parallel-implementation"></a>

### 并行实现中的临时重复

- 置信度：candidate
- 可跳过条件：PR 有意重复少量代码，让新路径与即将删除、替换或验证的旧路径保持并行。
- 不可跳过条件：重复代码改变安全、计费、数据访问、API 行为，或长期共享抽象显然能降低风险。
- 示例信号：“Significant duplication”（大量重复）或 “duplicated validation logic”（重复校验逻辑），负责人解释旧路径将删除，或重复逻辑有意保持局部。

<a id="existing-framework-or-component-invariant-covers-the-warning"></a>

### 现有框架或组件不变量已覆盖警告

- 置信度：candidate
- 可跳过条件：担忧已由共享组件、框架契约、类型不变量或单一事实来源保证，且当前 diff 或附近代码可见。
- 不可跳过条件：不变量只是被假定而非强制，依赖时序，或跨越异步 / 状态边界，值可能发生分歧。
- 示例信号：共享弹出框已限制视口边界，评论却称内部弹出框缺 max-height；或本地检查的值与传入值来自同一来源，却对可空值提出担忧。

<a id="owner-declared-follow-up-or-deferred-cleanup"></a>

### 负责人声明的后续项或延后清理

- 置信度：candidate
- 可跳过条件：PR 负责人明确说明问题是已知后续项，当前 PR 未使行为更差，评论不涉及高风险区域。
- 不可跳过条件：智能体未获负责人意见就自行行动，问题属于中 / 高严重程度的产品行为，或延后会将新回归合并。
- 示例信号：“I'll worry about that later”（我稍后再处理）或 “we'll delete this eventually”（最终会删除它）。

<a id="self-withdrawn-or-explicit-false-positive-rule-comments"></a>

### 自行撤回或明确为误报的规则评论

- 置信度：recurring
- 可跳过条件：评论正文或稍后的 Bugbot 回复明确说发现已撤回、符合规则或是误报，且智能体能本地验证相关规则。
- 不可跳过条件：唯一证据是有人对高风险问题只说“误报”，没有解释。
- 示例信号：文件命名规则评论的正文称文件已符合规范。

<a id="ask-by-default"></a>

## 默认询问

以下类别不得自动跳过，即使之前 PR 曾驳回类似问题：

- 安全、隐私、认证、计费、数据保留、训练数据和权限边界发现。
- 高严重程度发现。
- 迁移、schema、幂等、并发和跨系统行为发现。
- 建议修复很小，能明确降低风险且不改变产品意图的评论。

历史数据表明人类有时会驳回安全 / 数据流评论。应把这视为负责人的判断，不是全团队跳过规则。

<a id="candidate-learnings-from-recent-babysits"></a>

## 近期跟进中的候选经验

跟进期间或结束后，可在此追加看起来有助团队、但尚未成熟的新候选经验。多份 PR 确认模式后，优先将反复出现的候选提升到上方章节。

<a id="manual-reimplementations-of-native-browser-behavior"></a>

### 手工重新实现浏览器原生行为

- 置信度：candidate
- 可跳过条件：几乎从不。当 diff 用手工等价实现替换浏览器原生行为，例如原生 sticky → JS 定位克隆、原生滚动定位 → 转发 wheel/touch 事件、绘制顺序遮挡 → masks/clip-path，Bugbot 对此类代码提出的逻辑缺陷一直都确实成立。
- 不可跳过条件：发现涉及此类代码中的事件转发缺口，例如 wheel deltaMode、触摸平移、边缘滚动链、轻触容差，遮罩 / 裁剪的命中测试差异，或 observer 与 React 状态的时序竞态。默认修复。
- 示例信号：“masks do not affect hit-testing”（遮罩不影响命中测试）、“overlay blocks wheel scroll”（覆盖层阻挡滚轮滚动）、“ignores deltaMode”（忽略 deltaMode）、“runs in the IntersectionObserver callback before React applies state”（在 React 应用状态前于 IntersectionObserver 回调执行）。
- 来源：一个 sticky 遮挡 PR，六轮 Bugbot，约十八项发现，全都修复而非驳回。

<a id="contract-test-drift-claims-are-cheaply-verifiable--run-the-test-first"></a>

### 契约测试偏移的主张验证很便宜，先运行测试

- 置信度：candidate
- 可跳过条件：绝不跳过验证本身，只需一条命令。PR 交付的契约测试固定协议或文档文字，例如对 SKILL.md 做正则匹配、文档措辞快照，而 Bugbot 称“测试不再匹配文档”或反之时，分类前在 PR tip 运行该测试。运行红灯以实证确认主张，绿灯则是驳回回复的具体反证。
- 不可跳过条件：n/a，此为验证捷径，不是驳回模式。注意“多轮后倾向驳回”的启发式会在此误判，因为固定文字的测试恰恰会因先前修复轮次编辑文字而偏移。
- 示例信号：PR 较早修复提交改写被固定段落后，评论称 “Contract test omits the pre-fix wait”（契约测试遗漏修复前等待）；tip 上测试恰好在所指断言失败。
- 来源：一个固定文字的 PR，八轮 Bugbot；即使此前各轮全都修复并解决，第 7 轮的主张仍真实。

<a id="stale-security-review-finding-already-fixed-later-in-the-same-pr"></a>

### 同一 PR 后续已修复的陈旧安全审查发现

- 置信度：candidate
- 可跳过条件：智能体安全审查或类似审查声称缺少授权 / 校验调用，而当前 PR tip 明确已有该精确门禁并有测试，通常是审查后追加的加固提交。
- 不可跳过条件：对正在讨论的主体，所引辅助函数实际不做任何事；检查在受保护副作用之后运行；或缺少所涉主体的覆盖。
- 示例信号：一项 HIGH 的 “missing authorization check”（缺少授权检查）发现，但 tip 上已经在副作用之前调用了准确防护。
- 来源：一个 webhook 端点 PR，其加固提交晚于审查运行。

<a id="widening-a-deliberately-narrow-error-condition-would-mask-the-real-error"></a>

### 扩大刻意收窄的错误条件会掩盖真实错误

- 置信度：candidate
- 可跳过条件：发现要求把窄错误条件，例如特定 `errno`、错误码或状态类别，扩大为兜底捕获，而该窄条件编码了真实区别。典型形态是以 `ENOENT` 为门禁的依赖回退：“二进制未安装”不同于“命令运行后失败”。任何非零退出都重试，会把合法失败，例如未找到、认证过期、网络故障，交给回退再次运行，再报告回退错误，掩盖真实原因。
- 不可跳过条件：窄条件遗漏同一类别中的情况，例如另一种“二进制不可用” errno，如 `EACCES`，或另一种传输层失败；未处理路径会丢数据或留下部分状态；或重试幂等且原始错误仍被呈现。
- 示例信号：“only retries when X fails with ENOENT … never tries the fallback even when a working Y exists”（仅 X 以 ENOENT 失败时重试，即使有可用 Y 也不尝试回退），指向的是为缺依赖而非操作失败设置的回退代码。
- 来源：一个 CLI 重命名 PR，其回退为缺失二进制而设，而非失败命令。
