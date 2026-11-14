<a id="prompts-worth-copying"></a>

# 值得复制的提示词

替换为真实路径、技能和完成检查。非正式措辞也有效。占位符保留原样，替换后再使用。

<a id="understand"></a>

## 理解

- `/poteto-mode 阅读 <thread>。先用自己的话，以通俗英语重述根本问题。`
- `/in-your-own-words <long or messy ask>`
- `/sharpen <the prompt you're about to send>`
- `/poteto-mode 调查为什么出现 <symptom>。说明已知事实、所用数据、最佳假设。暂时不要改代码。`
- `用 /how 理解 <subsystem>。再用 /why 查明它最近为什么损坏。`
- `/recall 回顾我上周在 <topic> 上的工作，再阅读 <issue>。`
- `/teach 解释为什么这样实现，而不用 <other way>。作了哪些取舍？`
- `/poteto-mode 接手此分支。读决策日志，找出完成内容，继续推进。不要重做已完成工作。`

<a id="build"></a>

## 构建

- 缺陷：`/poteto-mode <symptom>。先复现，再修复并验证。`
- 应用缺陷：`/poteto-mode 用 /verify-<app> 复现此问题。如果 main 上可复现，修复并给我视频作为证明。`
- 有低成本测试的缺陷：`/poteto-mode 先复现 <bug>。如果有低成本测试路径，用 /tdd，再修复、重跑。`
- 功能：`/poteto-mode 添加 <behavior>。<current output> 必须逐字节不变。两者都要验证。`
- 重构：`/poteto-mode 把 <code> 移入一个模块，行为零变化。先记录当前输出，之后证明未变。`
- 性能：`/poteto-mode <operation> 在 <fixture> 上耗时 <time>。追踪，修复实测原因，展示改动前后。`

<a id="design-and-plan"></a>

## 设计与计划

- `/poteto-mode 为 <feature> 做几个选项原型。拍截图或视频供我比较。`
- `/poteto-mode 我们需要 <feature>。先用 /architect 设计，用原型回答开放问题。继续前让我审查。`
- `/poteto-mode 先写我会如何使用 <new package> 的教程。再用 /teach 向我解释它为什么优于当前方案。`
- `向 /arena 征求对本线程和当前方案的第二意见。`
- `/poteto-mode 把设计转成计划。拆成小型、可验证 PR，每个有自己的验证步骤。`
- `/poteto-mode 计划把 <library> 迁移到 <target>。拆成小型、可验证 PR。结果必须精确匹配原版，包括原有缺陷。`

<a id="review-and-ship"></a>

## 审查与交付

- `/interrogate 带怀疑态度审查整个分支。先不要改动。除非是真缺陷或回归，否则不要吹毛求疵。` 也要阅读 Dropped（丢弃项）列表。
- `/create-formal-verification-skill 证明 <property> 在 <module> 中成立，即使 <steps> 交错或重试。` 该代码合并或重构后使用 `/maintain-formal-verification-skill`。
- `/swarm 按各包检查脚本，检查 <dir> 下每个包。每包一个工作者，一份报告。`
- `/poteto-mode 创建 PR。小型、有序提交，在描述中放证据。`
- `/poteto-mode 持续照看此 PR，让检查通过。` 仅查状态用：`/poteto-mode 查看 PR <number>，还有未完成事项吗？`
- `/poteto-mode 落地整个堆栈。`

<a id="away-and-back"></a>

## 离开与回来

- `/poteto-mode im going to bed（我要睡觉了）。要在基于 <base> 的新 Git 工作树完成 <goal>。完成意味着 <checks>。记录决策日志。提交前不用问我。用 /loop 推进到完成。几小时后如果确实仍被阻塞，停止并写明原因。`
- `/show-me-your-work 告诉我昨晚你做了什么。` 先读其 Attention（注意事项）部分。
- `/ketchup` 说明本聊天自你上一条消息以来的进展，列出所有等待你的决定。
- `/poteto-mode 对这个队列 full autopilot（全自动驾驶），每项彼此独立。`
- `/poteto-mode autopilot（自动驾驶）这些改动，但不要合并，我会落地。`
- `/reflect 记录经验，让下次不再重复。` 只批准能改变未来决策的编辑。
- `/bro` 用通俗语言重述上一条回复。
