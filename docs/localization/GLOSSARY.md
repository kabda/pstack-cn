# 简体中文术语表

| 英文 | 统一译法／保留规则 |
| --- | --- |
| agent / subagent | 智能体 / 子代理；作为 ID、配置值、专名时保留原文 |
| skill | 技能；技能名、ID、目录和命令保持英文 |
| harness | 智能体运行环境（harness）；指具体宿主产品时保留产品名 |
| playbook | 操作手册；文件名保持英文 |
| invariant | 不变量 |
| deadlock | 死锁 |
| liveness / safety | 活性 / 安全性 |
| statechart / state machine | 状态图 / 状态机 |
| verification / validation | 验证 / 确认（依语境说明） |
| evidence | 证据 |
| gate | 门禁（检查或验收条件） |
| worktree | Git 工作树；命令及路径中的 worktree 保留 |
| baseline / fixture / snapshot | 基线 / 测试夹具 / 快照 |
| probe / oracle | 探测 / 判定依据（oracle） |
| handoff | 交接 |
| reviewer | 审查者；本地化语境用审校者 |
| must / should / may / never | 必须 / 应当 / 可以 / 绝不；保留原有力度和条件 |
| API、CLI、MCP、JSON、YAML、TLA+、TLC、Mermaid、Git、GitHub | 规范、接口与产品专名保留英文 |
| Cursor、Claude Code、Codex、Poteto、Lauren Tan、backnotprop | 产品、人名与署名原样保留 |

保护身份字段、命令、模型 slug、状态、协议标签、正则、占位符、数值及预算。英文触发词可在中文 description 中以括号保留。许可证和参与测试或解析的文本不翻译。代码围栏按内容判断：自然语言提示词需要译，命令和精确输出保留。

## 原则的规范中文名称

以下名称与叶子技能标题一致；ID 和路径始终保留英文。

| 技能 ID | 中文名称 |
| --- | --- |
| `principle-attack-the-premise` | 质疑前提 |
| `principle-boundary-discipline` | 边界纪律 |
| `principle-build-the-lever` | 构建杠杆工具 |
| `principle-encode-lessons-in-structure` | 把经验编码进结构 |
| `principle-exhaust-the-design-space` | 充分探索设计空间 |
| `principle-experience-first` | 体验优先 |
| `principle-explain-the-number` | 解释数字 |
| `principle-fix-root-causes` | 修复根因 |
| `principle-foundational-thinking` | 基础性思考 |
| `principle-guard-the-context-window` | 保护上下文窗口 |
| `principle-laziness-protocol` | 惰性协议 |
| `principle-make-operations-idempotent` | 让操作幂等 |
| `principle-migrate-callers-then-delete-legacy-apis` | 迁移调用方后删除旧 API |
| `principle-minimize-reader-load` | 减轻阅读负担 |
| `principle-model-the-domain` | 领域建模 |
| `principle-never-block-on-the-human` | 绝不因等待人而阻塞 |
| `principle-outcome-oriented-execution` | 面向结果执行 |
| `principle-prove-it-works` | 证明它能工作 |
| `principle-redesign-from-first-principles` | 从第一性原理重新设计 |
| `principle-separate-before-serializing-shared-state` | 先隔离，再串行化共享状态 |
| `principle-sequence-verifiable-units` | 把工作拆为可验证单元 |
| `principle-subtract-before-you-add` | 先减后加 |
| `principle-test-behavior-not-implementation` | 测试行为，而非实现 |
| `principle-type-system-discipline` | 类型系统纪律 |

`why` 的置信等级统一为 Direct（直接证据）、Supported（证据支持）、Inferred（推断）、Speculative（猜测）、Unknown（未知）；方括号输出标签保持英文。

## 语境补充

- `feature map`：功能映射。
- `hillclimb`：爬坡优化。
- 测量语境的 `regression`：性能退化；代码行为语境：回归；`revert`：回退。
- 并发语境的 `race` / `race condition`：竞态／竞态条件；多个模型或工作者的 `race`：竞赛。
- `em dash` / `en dash`：长破折号／短破折号。
- `canonical object`：权威对象，不能译为符合规范的对象。
