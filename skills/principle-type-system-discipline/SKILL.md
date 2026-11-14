---
name: principle-type-system-discipline
description: "设计类型、审查函数签名，或使用任何静态类型语言编写代码时适用。让非法状态无法表达，为有语义的原始类型加品牌，在边界解析外部数据，穷尽变体，并从权威 schema 派生类型。"
disable-model-invocation: true
---

<a id="type-system-discipline"></a>

# 类型系统纪律

让编译器拒绝不可能状态、不匹配原始类型和未处理变体。优先通过定义消除错误与特例，而非不断增加处理器。TypeScript 语法见 `typescript-best-practices` 技能。

- **为有语义的原始类型加品牌。** `UserId` 和 `OrderId` 底层都是字符串，但不应互换。给它们各自的类型，例如 TypeScript 的品牌交叉类型，或其他语言的 newtype。创建时校验一次，后续信任类型。两个参数原始类型相同但含义不同，就加品牌。
- **外部数据在解析前都是无类型的。** 包括 RPC 载荷、JSON、IPC 消息、CLI 参数、配置文件、环境变量、数据库行。每个边界都有解析函数，把非结构化输入转成类型化模型。**boundary-discipline** 原则技能说明校验放在哪里。
- **从权威 schema 派生类型。** protocol buffer、OpenAPI 规范、GraphQL schema、数据库迁移、设计 token 文件或其他文件拥有某种形态时，从它派生，而非手工编写并行类型。见 **encode-lessons-in-structure** 原则技能。
