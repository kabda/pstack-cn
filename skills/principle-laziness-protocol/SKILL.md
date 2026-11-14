---
name: principle-laziness-protocol
description: "重构（refactoring）、评估 diff 大小，或想加入抽象、层次、信号传递时适用。倾向删除，并采用能解决问题的最小改动。"
disable-model-invocation: true
---

<a id="laziness-protocol"></a>

# 惰性协议

- **集中决策。** 不在多处重复同一选择。把它放到单一事实来源后面，将结果作为简单标记传递。
- **最小化 diff。** 做能解决问题的最小改动。更少代码行胜过“优雅”的样板。
