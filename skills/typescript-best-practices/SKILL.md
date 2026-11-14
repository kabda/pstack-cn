---
name: typescript-best-practices
description: TypeScript 最佳实践。阅读或编辑任何 .ts 或 .tsx 文件时使用。
paths: ["**/*.ts", "**/*.tsx"]
disable-model-invocation: true
---

<a id="typescript-best-practices"></a>

# TypeScript 最佳实践

先应用 **type-system-discipline** 原则技能。

| 规则 | 摘要 |
|------|---------|
| 可辨识联合 | 用 `kind` 字面量判别字段表示变体，让不可能状态无法表达。不使用堆满可选字段的对象。 |
| 品牌类型 | 给原始类型附加 `& { readonly __brand: "X" }`，避免混用。在边界只验证一次。品牌来自真正验证的类型守卫（`input is AgentId`），绝不来自 `as`。 |
| 构造式建模 | 设计结构，让非法值根本无法构造。非空用 `[T, ...T[]]`，偶数长度用 `[T, T][]`，范围用 `start` 加 `duration`。不是运行时守卫，也不是期待细化类型。 |
| 最简单的全定义类型 | 只要对 `T[]` 的每项操作都对所有输入有定义，就保持 `T[]`。仅在宽松类型迫使代码使用 `!`、强制转换，或抛出“本不应发生”的异常时，才强化为 `NonEmpty<T>`。 |
| `unknown` 优于 `any` | 外部数据是 `unknown`。 |
| schema 优先于守卫 | 手写逐属性类型守卫前，先使用仓库的运行时 schema 库，从 schema 推导类型，例如 `z.infer`。 |
| 不用 `as` 强制转换 | 每个 `as` 都是潜在运行时崩溃。只在验证后转换。 |
| 收窄优先级 | 判别字段 switch > `in` 运算符 > `typeof`/`instanceof` > 用户自定义类型守卫 > `as`。 |
| 类型守卫 | 必须验证其断言。说谎的守卫比 `as` 更糟，因为缺陷躲在声称安全的名字后面。命名为 `isX` 或 `hasX`。 |
| 穷尽性 | 在 default 分支内联 `const _exhaustive: never = x;`，新增变体时让编译器报错。 |
| `satisfies` 优于 `as` | 验证值，同时不拓宽字面量类型。 |
| 边界验证 | 数据进入边界时解析为有名称的领域类型。`Record<string, unknown>`（无论如何拼写）到该解析为止。内部信任类型。参见 **boundary-discipline** 原则技能。 |
| schema 派生类型 | 声明新 interface 前，优先使用 `Pick`/`Omit`/`Parameters`/`ReturnType`/`Awaited`/`typeof`。 |
| 对象参数 | 传对象而非位置参数，让参数顺序不言自明。热点路径（逐帧渲染、词法分析器、解析器）除外。 |
| 真实测试 | 能真实运行就不要 mock。优先使用框架真实测试原语及泄漏、可释放资源检查，并在运行中的构建验证 UI。只 mock 无法本地运行的内容。 |
| 结构化遥测 | 优先使用带足够上下文的结构化日志诊断，让人能凭 ID 调试。交付代码里不使用 `console.log`。 |

示例：`references/patterns.md`。
