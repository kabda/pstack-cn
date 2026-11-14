<a id="typescript-patterns"></a>

# TypeScript 模式

`SKILL.md` 每条规则的代码示例。底层原则与语言无关，参见 **type-system-discipline** 和 **boundary-discipline** 原则技能。

<a id="branded-types"></a>

## 品牌类型

给原始类型加品牌，避免混用。在边界只验证一次，下游代码信任类型。

```ts
type AgentId = string & { readonly __brand: "AgentId" };

function isAgentId(input: string): input is AgentId {
  return isUUID(input);
}

function parseAgentId(input: string): AgentId {
  if (!isAgentId(input)) throw new Error(`Invalid agent id: ${input}`);
  return input;
}

function focusAgent(id: AgentId): void {
  /* 输入可信 */
}
```

遵循 `readonly __brand: 'X'` 结构，不要发明新约定。

<a id="discriminated-unions"></a>

## 可辨识联合

使用字面量判别字段表示变体。每个变体使用相同字段名，且字段值各不相同，让不可能的组合无法表达。

```ts
// 错误：布尔值加可选字段允许矛盾状态存在。
type DiffState = { loading: boolean; diff?: GitDiff; error?: string };

// 正确：只有有效状态可以存在。
type DiffState =
  | { kind: "loading" }
  | { kind: "ready"; diff: GitDiff }
  | { kind: "error"; error: string };
```

选择一个判别字段名称（`kind`、`type`、`tag`）并保持一致。

<a id="constructive-modeling"></a>

## 构造式建模

用全部合法的组成部分构造类型，而不是靠运行时检查约束宽松类型。

用可变长度元组表示非空：

```ts
type NonEmpty<T> = [T, ...T[]];

// 错误：T[] 加上每个调用者都必须重复的长度检查
function pickWinner(entries: string[]): string {
  if (entries.length === 0) throw new Error("no entries");
  return entries[Math.floor(Math.random() * entries.length)];
}

// 正确：该类型不可能存在空值
function pickWinner(entries: NonEmpty<string>): string {
  return entries[Math.floor(Math.random() * entries.length)];
}
```

接收普通 `T[]` 时，用守卫收窄一次，此后事实随类型传递：

```ts
const isNonEmpty = <T>(arr: T[]): arr is NonEmpty<T> => arr.length > 0;
```

用成对元素表示偶数长度：

```ts
type Pairs<T> = [T, T][];
```

用起点加时长表示时间范围：

```ts
// 错误：靠注释维护不变量
type TimeRange = { start: Date; end: Date }; // start <= end

// 正确：无法写出负范围；需要时推导终点
type TimeRange = { start: Date; durationMs: number };
```

让 `durationMs` 保持普通数字。只有原始数字可能被错误传到需要时长的位置时，才按“品牌类型”加品牌，不要条件反射地加。选择使错误状态无法构造的表示，再在其上提供所需读取方式（`pairs.flat()`、`rangeEnd()` 辅助函数）。

<a id="simplest-total-type"></a>

## 最简单的全定义类型

不要强化一切。对每个输入都有定义的操作，保持 `T[]`：

```ts
const sum = (xs: number[]) => xs.reduce((a, b) => a + b, 0); // [] 的结果为 0，没有问题
```

宽松类型迫使使用处说谎时，才强化。迹象包括 `!`、`arr[0] as T`，以及“本不应发生”的异常：

```ts
// 错误：把部分输入无定义的问题偷偷绕过编译器
function newestSession(sessions: Session[]): Session {
  return sessions.at(0)!;
}

// 正确：强化输入，断言随之消失
function newestSession(sessions: NonEmpty<Session>): Session {
  return sessions[0];
}
```

将结果放宽为 `Session | undefined`，是另一种对所有输入都有定义的签名。

<a id="unknown-over-any"></a>

## `unknown` 优于 `any`

外部数据始终是 `unknown`，使用前先收窄。

```ts
// 错误
function handle(input: any) {
  return input.foo.bar;
}

// 正确
function handle(input: unknown) {
  if (typeof input === "object" && input !== null && "foo" in input) {
    // 已收窄；编译器验证访问
  }
}
```

外部来源包括 RPC 载荷、`JSON.parse`、`postMessage`、IPC、文件内容、环境变量和数据库结果。

<a id="schemas-before-hand-rolled-guards"></a>

## schema 优先于手写守卫

为外部数据逐属性手写类型守卫前，先查找仓库的运行时 schema 库和现有 schema。让一个 schema 负责验证，再据此派生 TypeScript 类型。不要同时维护可能相互漂移的 schema、重复 interface 和守卫。

```ts
import { z } from "zod";

const UserSchema = z.object({
  id: z.string().uuid(),
  role: z.enum(["admin", "member"]),
});

type User = z.infer<typeof UserSchema>;

function parseUser(input: unknown): User {
  return UserSchema.parse(input);
}
```

失败是预期分支时使用 `safeParse`。仓库使用其他 schema 库时，采用对应推导辅助工具。不要为一个守卫增加新 schema 依赖。本规则优先采用代码库已信任的 schema 系统。

<a id="no-as-casts"></a>

## 不用 `as` 强制转换

每个 `as` 都是潜在运行时崩溃。只有类型系统已验证断言后，才强制转换。

```ts
import { z } from "zod";

// 错误
const user = data as User;

// 错误
function isUser(data: unknown): data is User {
  return typeof data === "object" && data !== null && "id" in data;
}

// 正确
const userSchema = z.object({ id: z.string(), name: z.string() });
type User = z.infer<typeof userSchema>;

function parseUser(data: unknown): User {
  return userSchema.parse(data);
}
```

类型先存在时，用其要证明的类型注解验证器。这样验证器证明不足时，编译器会拒绝。把下面对象的 `name` 移除，赋值就无法编译。

```ts
type User = { id: string; name: string };

const userSchema: z.ZodType<User> = z.object({ id: z.string(), name: z.string() });
```

重构现有代码以移除 `as` 时，先确认 TypeScript 无法推断的原因：

- 缺少判别字段：增加字段，改用可辨识联合。
- 源类型过宽（例如 `Record<string, unknown>`）：收窄它。
- 边界无类型：用负责该结构的 schema 解析。只有尚不存在 schema 时才新增。
- 确实无法表达：使用品牌类型或 `satisfies`。

<a id="narrowing-hierarchy"></a>

## 收窄优先级

从最佳到最后手段：

1. **可辨识联合 switch / if。** 编译器自动收窄。
2. **`in` 运算符。** `"key" in obj` 收窄为包含该键的变体。
3. **`typeof` / `instanceof`。** 用于原始值和类实例。
4. **用户自定义类型守卫。** 以上不足时使用。
5. **`as` 强制转换。** 仅在验证后使用。

```ts
function area(s: Shape): number {
  if ("radius" in s) return Math.PI * s.radius ** 2; // 收窄为圆形
  return s.width * s.height; // 收窄为矩形
}
```

<a id="type-guards"></a>

## 类型守卫

守卫必须真正验证其断言。说谎的守卫比 `as` 更糟。

```ts
function isCircle(s: Shape): s is Shape & { kind: "circle" } {
  return s.kind === "circle";
}
```

尽可能优先使用判别字段收窄。

<a id="exhaustiveness"></a>

## 穷尽性

在 default 分支中，把判别字段赋给 `never` 类型的局部变量。

```ts
// 返回值的 switch
function area(s: Shape): number {
  switch (s.kind) {
    case "circle":
      return Math.PI * s.radius ** 2;
    case "rect":
      return s.width * s.height;
    default: {
      const _exhaustive: never = s;
      return _exhaustive;
    }
  }
}

// 无返回值的 switch
function handle(s: Shape): void {
  switch (s.kind) {
    case "circle":
      drawCircle(s);
      break;
    case "rect":
      drawRect(s);
      break;
    default: {
      const _exhaustive: never = s;
      void _exhaustive;
    }
  }
}
```

返回值的 switch 使用 return 风格，语句型 switch 使用 void 风格。

<a id="satisfies-over-as"></a>

## `satisfies` 优于 `as`

`satisfies` 验证值，不拓宽字面量类型。

```ts
// 错误：拓宽并丢失字面量类型。
const config = { theme: "dark", cols: 3 } as Config;

// 正确：验证并保留字面量类型。
const config = { theme: "dark", cols: 3 } satisfies Config;
// config.theme 是字面量 "dark"，不是 string
```

<a id="boundary-validation"></a>

## 边界验证

在数据进入的边界验证一次，内部信任类型。参见 **boundary-discipline** 原则技能。

- **线协议格式**（proto、JSON-RPC）：解析使用 `ignoreUnknownFields`，让向前兼容的变化不破坏旧客户端。
- **持久化 JSON：** 带版本的 blob，解析用 try/catch 包围。
- **不要在调用链深处重复验证。**

<a id="schema-derived-types"></a>

## schema 派生类型

`.proto`、OpenAPI 规格、GraphQL schema 或数据库迁移已定义结构时，从生成类型派生，不重复定义。

```ts
// 错误：重复结构，schema 变化时会漂移。
type CheckSummary = {
  totalCount: number;
  checks: { name: string; status: string }[];
};
function renderChecks(s: CheckSummary) {
  /* ... */
}

// 正确：从生成的 schema 类型派生。
import type { ChecksMessage } from "<generated module>";
function renderChecks(s: Pick<ChecksMessage, "totalCount" | "checks">) {
  /* ... */
}
```

编写新 interface 前，优先使用 `Pick`、`Omit`、`Parameters`、`ReturnType`、`Awaited`、`typeof`。

<a id="object-args"></a>

## 对象参数

```ts
// 错误：交换两个参数仍能编译。
openFile(uri, {
  startLineNumber: 10,
  startColumn: 1,
  endLineNumber: 10,
  endColumn: 1,
});

// 正确：与顺序无关，用法不言自明。
openFile({
  uri,
  selection: {
    startLineNumber: 10,
    startColumn: 1,
    endLineNumber: 10,
    endColumn: 1,
  },
});
```

热点路径除外：逐帧渲染、词法分析器、解析器，以及分配成本重要的任何紧密循环。
