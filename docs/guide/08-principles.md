<a id="steer-with-principle-names"></a>

# 用原则名称引导工作

pstack 将 24 条原则分别作为独立技能提供。`/poteto-mode` 在每个多步骤任务开始时阅读它们的索引，应用任务所触发的原则，并在回复中说出每条已应用原则及它改变的决策。

你无需调用原则，只需用名称引导。每个名称都指向智能体已经读过的一条完整规则，因此一个短语比一段指令更能精确调整方向。

<a id="steering-in-practice"></a>

## 实际引导方式

假设智能体正准备在三个已有适配器上再加一个：

```text
运用“先减后加”。先删除过时适配器，再设计余下部分。
```

假设它因为构建通过就宣告成功：

```text
应用“证明它能工作”。运行真实导入流程，展示写入的记录。
```

假设两次并行尝试即将写入同一个分支：

```text
先隔离，再串行化共享状态。每次尝试各用一个工作树，不要加锁。
```

这些短语有效，是因为背后的规则具体。智能体仍必须在回复中说明规则改变了哪项决策。只引用原则却说不出相应决策，意味着它只是叫出了名字，并未应用。

<a id="the-24-briefly"></a>

## 24 条原则简述

核心原则决定构建多少，以及何时重新思考设计：

- [惰性协议（Laziness Protocol）](../../skills/principle-laziness-protocol/SKILL.md)优先删除，并作出能解决问题的最小改动。
- [基础性思考（Foundational Thinking）](../../skills/principle-foundational-thinking/SKILL.md)在写逻辑前选择核心数据结构。
- [从第一性原理重新设计（Redesign from First Principles）](../../skills/principle-redesign-from-first-principles/SKILL.md)整合新需求，仿佛它从第一天起就存在。
- [质疑前提（Attack the Premise）](../../skills/principle-attack-the-premise/SKILL.md)写出两次或更多失败修复共有的前提，并在下一次修复前直接检验。
- [先减后加（Subtract Before You Add）](../../skills/principle-subtract-before-you-add/SKILL.md)在其上构建前先去掉冗余负担。
- [减轻阅读负担（Minimize Reader Load）](../../skills/principle-minimize-reader-load/SKILL.md)合并读者必须记在脑中的层次和隐藏状态。
- [面向结果执行（Outcome-Oriented Execution）](../../skills/principle-outcome-oriented-execution/SKILL.md)让重写收敛到目标设计，而非保留一次性的兼容状态。
- [体验优先（Experience First）](../../skills/principle-experience-first/SKILL.md)优先考虑用户结果，而非实现方便。
- [充分探索设计空间（Exhaust the Design Space）](../../skills/principle-exhaust-the-design-space/SKILL.md)在没有先例时构建两到三个相互竞争的原型。
- [构建杠杆工具（Build the Lever）](../../skills/principle-build-the-lever/SKILL.md)编写执行或证明工作的脚本，让审查者可以重跑。当智能体反复手动做同一件事时，让它编写自己想要的工具或技能。如果脚本能每次以同样方式执行一个步骤，就用脚本，把智能体留给需要判断的决定。

架构原则决定状态、验证和兼容应放在哪里：

- [领域建模（Model the Domain）](../../skills/principle-model-the-domain/SKILL.md)把重复规则编码进一个结构，而非散落的条件判断。
- [边界纪律（Boundary Discipline）](../../skills/principle-boundary-discipline/SKILL.md)在边界验证，信任内部类型。
- [类型系统纪律（Type System Discipline）](../../skills/principle-type-system-discipline/SKILL.md)让非法状态无法表示。
- [让操作幂等（Make Operations Idempotent）](../../skills/principle-make-operations-idempotent/SKILL.md)让重试收敛到相同终态。
- [迁移调用方后删除旧 API（Migrate Callers Then Delete Legacy APIs）](../../skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md)在同一轮完成迁移与删除。
- [先隔离，再串行化共享状态（Separate Before Serializing Shared State）](../../skills/principle-separate-before-serializing-shared-state/SKILL.md)先消除共享，再增加协调机制。

验证原则定义什么算证明：

- [证明它能工作（Prove It Works）](../../skills/principle-prove-it-works/SKILL.md)验证真实产物，而非替代物。
- [修复根因（Fix Root Causes）](../../skills/principle-fix-root-causes/SKILL.md)在改代码前先复现并追踪到原因。
- [把工作拆为可验证单元（Sequence Work into Verifiable Units）](../../skills/principle-sequence-verifiable-units/SKILL.md)每个小单元结束时先检查，再开始下一个。
- [测试行为，而非实现（Test Behavior, Not Implementation）](../../skills/principle-test-behavior-not-implementation/SKILL.md)断言代码用户可观察的内容，让测试在行为破坏时失败，在内部实现变化后仍然成立。
- [解释数字（Explain the Number）](../../skills/principle-explain-the-number/SKILL.md)在任何人信任或报告测量数字前，说出限制因素，并排除测量了其他事物的可能。[`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md)把它变成七个需用真实运行回答的问题。

委派原则让并行工作保持有序：

- [保护上下文窗口（Guard the Context Window）](../../skills/principle-guard-the-context-window/SKILL.md)把大批阅读交给子代理，主聊天保留发现。
- [绝不因等待人而阻塞（Never Block on the Human）](../../skills/principle-never-block-on-the-human/SKILL.md)继续推进可逆工作并展示结果。

还有一条元原则：

- [把经验编码进结构（Encode Lessons in Structure）](../../skills/principle-encode-lessons-in-structure/SKILL.md)把重复两次的建议转为 lint、检查或脚本。[`/correct`](../../skills/correct/SKILL.md)将它应用于整个仓库，见[按需定制](./09-make-it-yours.md#fix-the-environment-with-correct)。

不必背下清单。现在浏览一遍，当你发现智能体正在做某件本可被某个原则名称阻止的事时，再回来查阅。词汇就是这样通过使用积累的。

下一页：[按需定制](./09-make-it-yours.md)。
