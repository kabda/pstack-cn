---
name: principle-redesign-from-first-principles
description: "将新需求整合到现有设计时适用。"
disable-model-invocation: true
---

<a id="redesign-from-first-principles"></a>

# 从第一性原理重新设计

整合改动时，不要把它硬接到现有设计上。像该需求从开始就是基础假设一样重新设计。

- 阅读所有受影响文件，理解当前设计
- 问：“如果从头编写，并带着这个新需求，我们会构建什么？”
- 让改动传播到每处引用，包括类型、文档、示例、设计理由章节
- 思考完整重新设计，再增量交付

这是在将变化整合到已有设计时，保留未来选择价值的方法。
