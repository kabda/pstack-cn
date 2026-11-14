---
name: architect
description: "先勾勒类型、签名和模块结构，再在实现填充过程中持续参与。用于 /architect、'architect this'、'design this'，或直接写代码会固化错误结构的非简单任务。"
disable-model-invocation: true
---

<a id="architect"></a>

# 架构设计

用 `not implemented` 函数体和伪代码，勾勒类型、函数签名、类的形态及模块边界。综合多个模型的视角，再按选定草图填充代码。

<a id="start"></a>

## 开始

开始前创建待办清单，每个阶段一项。

1. 理解事实
2. 勾勒草图
3. 达成一致
4. 实现
5. 推翻重来

<a id="phase-a-ground-the-problem"></a>

## 阶段 A：理解问题的事实基础

为新代码触及的每个系统建立真实的心智模型。对相关子系统运行 **how** 技能。指出一个文件名不等于理解事实。产出 `how` 要求的架构说明。如果设计重新定义所有权或分层，还要对现有结构运行 **why** 技能，让原有设计理由成为约束，而不是猜测。

只有工作确实从零开始、没有需要集成的周边系统时，才能跳过阶段 A。

<a id="phase-b-sketch"></a>

## 阶段 B：勾勒草图

运行 **arena** 技能，提供设计草图任务和阶段 A 的事实基础产物。将 `references/runner-prompt.md` 作为每个执行者的提示词。

从 pstack 设置文件的 `architect runners` 行选择执行者（Cursor 为 `~/.cursor/rules/pstack-models.mdc`，Claude Code 为 `~/.claude/rules/pstack-models.md`，其他智能体运行环境为 `~/.agents/pstack-models.md`），替代 `arena runners` 行。文件或该行缺失时，使用 `claude-opus-5-5-xhigh` 和 `grok-4.7-xhigh-fast`。别名和被拒绝的条目按 **arena** 技能阶段 A 的执行者规则处理。

设计两次。即使首个方案看起来足够，也必须在综合前得到至少两个结构不同的候选方案。这是 **exhaust-the-design-space** 原则技能的具体落实。需要的是整体结构的备选方案，不是同一结构里的局部修补。

综合前，用 [`references/design-red-flags.md`](references/design-red-flags.md) 筛查每个候选方案。假定下一个贡献者是智能体，只能看到打开的文件，会照抄最近示例，并选择能够编译的最短路径。优先选择这样的设计：从单个文件看起来正确的改动，对整个仓库也正确。

按接口深度比较可行方案。优先选择以更小、更简单的公共接口隐藏更多复杂性的设计。功能丰富的接口可以集中能力，避免将其分散到各层，从而保持调用链简短。

Arena 返回一个综合设计包。其综合决策填写在设计理由的“综合决策”部分。

<a id="phase-c-agree-opt-in"></a>

## 阶段 C：达成一致（按需启用）

默认：根据综合设计直接进入实现，不设人工检查点。

只有调用者明确要求时才启用检查点，例如“/architect with checkpoint”、“stop and show me before implementing”或类似表达。此时展示综合设计，暂停等待批准。

无论是否设检查点，综合结果都可以单独作为一个提交交付，这对应 **foundational-thinking** 原则技能的“脚手架优先”模式。根据 **outcome-oriented-execution** 原则技能，填充过程中允许有计划、范围明确的暂时破坏。若要在实现前对设计施加对抗性检验，对综合草图运行 **interrogate** 技能。

如果人对结构提出异议（无论在检查点还是事后），将其视为阶段 A 的证据。在继续写代码前，重新理解事实并重跑阶段 B。

<a id="phase-d-implement-against-the-sketch"></a>

## 阶段 D：按草图实现

用代码替换 `not implemented` 函数体，用逻辑替换伪代码。综合草图就是约定。偏离草图是需要指出的信号，不应默默消化。如果一个函数需要草图未预计的参数，应判断是草图错误、遗漏需求，还是实现越界。

<a id="phase-e-scrap-when-the-architecture-is-wrong"></a>

## 阶段 E：架构错误时推翻草图

如果实现持续产生草图无法容纳的阻力，就丢弃草图。根据 **redesign-from-first-principles** 和 **fix-root-causes** 原则技能，不要在错误设计上不断叠加修补。

信号是反复出现的*模式*，不是单个案例。迹象包括：

- 不相关代码中反复出现相同形态的变通方案。
- 多个不相关边界情况都需要特殊分支。
- 类型必须借助逃生口（`any`、强制转换、实际总有值的可选字段）才能编译。
- 草图原本认为状态不共享，实际却下意识地说“需要加锁”。
- 调用者必须了解抽象的内部规则才能使用它。
- 整个实现中，阶段 D 出现两次或更多彼此独立、形态相同的偏离。

运用判断力。少数边界情况不意味着架构有问题。有些问题本身确实复杂。数据复杂，不等于设计复杂。

推翻时：

1. 对已经构建的内容重跑 **how** 技能。
2. 根据 redesign-from-first-principles，假定新约束从第一天就存在，重新设计。
3. 根据 **subtract-before-you-add** 原则技能，先做减法再做加法。新草图在扩充前应小于旧草图。
4. 回到阶段 B，重跑 arena。

<a id="outputs"></a>

## 输出

先写调用者的使用方式，再据此推导类型草图。小改动用一个文件列出新类型和签名；较大工作提供模块图和类型定义。设计理由随附，按 `references/rationale-template.md` 组织，包含使用草图和综合决策。
