# 二十四条原则独立源译对照审校

审校者：translate_docs；初译者：translate_mode。审校者未参与本批初译，也没有直接修改译文。源固定 commit：`9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`；日期：2026-11-14。

## 方法与结论

全部 24 份 principle-*/SKILL.md 均从固定 Git 对象读取并与目标逐段对照，包括 frontmatter description、全部正文、应用条件、例外、警告、判断问题和停止边界。未以“包含中文”替代全文审校。两组审校问题已由主代理修复并逐项复核，当前无未决问题；目标哈希锁定于 REVIEW-principles.json。

| 编号 | 文件及定位 | 发现与修复 | 复核结果 |
| --- | --- | --- | --- |
| P1 | `principle-explain-the-number/SKILL.md` 的 description | regression 在测量语境误译为“回退”，与回滚动作混淆。主代理改为“性能退化”。 | 重新读取确认，关闭。 |
| P2 | `principle-separate-before-serializing-shared-state/SKILL.md` 的 description、第2和第3步 | source 的 one shared writer／one shared write target 中的单一约束应明确；canonical object 的“规范对象”可能误解为符合标准。主代理改为“单一共享写入者”“单一共享写入目标”“同一个权威对象”，并统一 race condition 为“竞态条件”。 | 已分别核对四项，关闭。 |

## 核对重点

- 所有 name 和 disable-model-invocation 与源相同，description 为中文；技能 ID、专名、调用和相对链接未改。
- “两个或更多修复在同一门禁失败后先检验前提”“只有简单任务可跳过工具”“只在边界验证”“只有单一共享写入目标确为不变量时才结构化串行访问”“不可逆操作仍须确认”等边界完整。
- 保留删除旧 API 的三项前提、计划性重写允许中间损坏的计划／范围／可逆约束、结束时完整静态和运行时验证，以及“真实产物而非代理证据”的要求。
- 幂等处理覆盖每个可能崩溃位置，保留三项检查问题；测试行为技能保留破坏行为与改变内部实现两种假想改动及外部服务／内部辅助函数的区别。
- 量化约束与例子完整：2-3 个原型、三个与十个功能、50 个全局变量、6 层适配器、30 秒、两次修复和第三次修复等均准确，未引入预算或改变阈值。
- must／should／only／never 等力度和条件未见遗漏或改写成新权限。材料中的提交、任务分派和外部动作仅作为译材审查，没有执行。

## 逐文件覆盖与锁定

| 文件 | 审校结论 | 目标 SHA-256 |
| --- | --- | --- |
| `skills/principle-attack-the-premise/SKILL.md` | 全文独立审校通过，无未决问题 | `2c58b5efb0792d3240222d70225549d64c6c8e8a7131a2a1da43fbd96bec7681` |
| `skills/principle-boundary-discipline/SKILL.md` | 全文独立审校通过，无未决问题 | `ccb277560b8faa26f656abb368d93272c0b8f3de0592b155a4a27272ad6359ae` |
| `skills/principle-build-the-lever/SKILL.md` | 全文独立审校通过，无未决问题 | `b5a7bd09867b65a0e76d613cccedc2d0a90b6c59d4ef65ba2acc604bfda10bbb` |
| `skills/principle-encode-lessons-in-structure/SKILL.md` | 全文独立审校通过，无未决问题 | `b69d9c02963a5ccb81295faa323ef6d38092dfba8bbfc526a4ee51c383a79f85` |
| `skills/principle-exhaust-the-design-space/SKILL.md` | 全文独立审校通过，无未决问题 | `a16a4ace870bfa565b38e2f829bb2b1a5ec4e02637ebf66443b1311ad6c22894` |
| `skills/principle-experience-first/SKILL.md` | 全文独立审校通过，无未决问题 | `c3b872b7f80d57af4aa12cd49f58ca62a84e8c80feed4b8d9f819f26bbaf761b` |
| `skills/principle-explain-the-number/SKILL.md` | 全文独立审校通过，无未决问题 | `d5e087cf282322e2a20899851df919577bbcfdfac0b7e0ed057e02b92d87083d` |
| `skills/principle-fix-root-causes/SKILL.md` | 全文独立审校通过，无未决问题 | `84ea48d7bfd27c97a1a5ace6221ec26683f8eb63cf6fefb9a4ef33cd72fcee4a` |
| `skills/principle-foundational-thinking/SKILL.md` | 全文独立审校通过，无未决问题 | `9c96650dc70c94a7ef9fb48d5201efc4a4a398593a6b08fe52a265b985e90d5f` |
| `skills/principle-guard-the-context-window/SKILL.md` | 全文独立审校通过，无未决问题 | `d9a5ad757abe7d10608f524758aee1b4884e67b9ced35306b8169c0f8e8ea934` |
| `skills/principle-laziness-protocol/SKILL.md` | 全文独立审校通过，无未决问题 | `b7d537769c7a9b6803c482463f616948d2d259ed0a5a1009d92201486688364f` |
| `skills/principle-make-operations-idempotent/SKILL.md` | 全文独立审校通过，无未决问题 | `235b55b53ffe1c2465b545bf143663738ab1aba36b60ddb944611402ea043925` |
| `skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md` | 全文独立审校通过，无未决问题 | `d250103a2e16c101c4873f6a68068df24581232204cd60c03ab7ab23bcba78e2` |
| `skills/principle-minimize-reader-load/SKILL.md` | 全文独立审校通过，无未决问题 | `6adda938f7b4dde30a329f0753d55fc10aba74b218d571711b6e5d8164c69920` |
| `skills/principle-model-the-domain/SKILL.md` | 全文独立审校通过，无未决问题 | `c6f061c4b446865e34771ae64d64eac42b7ffe0dbeda92331faeb8dbea29b02c` |
| `skills/principle-never-block-on-the-human/SKILL.md` | 全文独立审校通过，无未决问题 | `3507f91d18370f95ed03230903dc087c6026a2883e1a22f057265d46d19b4c58` |
| `skills/principle-outcome-oriented-execution/SKILL.md` | 全文独立审校通过，无未决问题 | `f7c77b236882689f37907628c2d4ea54f1435c58ee298ca295865932f205193b` |
| `skills/principle-prove-it-works/SKILL.md` | 全文独立审校通过，无未决问题 | `6ea4bff6b96f6fb661c54577156770884ea9ef10e3644ba7be03094c871c9bf6` |
| `skills/principle-redesign-from-first-principles/SKILL.md` | 全文独立审校通过，无未决问题 | `9873e5286881a54815116096ddaa024d0044afbbb96c65ef8f95a3136a84f090` |
| `skills/principle-separate-before-serializing-shared-state/SKILL.md` | 全文独立审校通过，无未决问题 | `7226d6b5f754b323a3a0158d10ae80e3cca641d8bbd0174e7b2856d4567465d7` |
| `skills/principle-sequence-verifiable-units/SKILL.md` | 全文独立审校通过，无未决问题 | `f6f8bd15dbd9017cef6f0b012bce1be6cc0b92cfecaf4689fec5cc6e021087b7` |
| `skills/principle-subtract-before-you-add/SKILL.md` | 全文独立审校通过，无未决问题 | `aa5ec66a91e15fa074062649560192ad2f3b24ebedf4a9fcd04d7b7da393582e` |
| `skills/principle-test-behavior-not-implementation/SKILL.md` | 全文独立审校通过，无未决问题 | `02f5b5d8e25f07f7b319a73bd995d009db399b203cc6a340477110be4b378cc3` |
| `skills/principle-type-system-discipline/SKILL.md` | 全文独立审校通过，无未决问题 | `9513fde2b41862aeef85e9d8c5d48bb4a8b8c7c987d440e3b39d95b98c43c60e` |

## 英文保留裁定

API、CLI、JSON、RPC、IPC、TypeScript、OpenAPI、GraphQL 等接口／规范／语言名；UserId、OrderId、lastX、state.json、indexer-state.json、metrics-state.json 等示例标识符和文件名；principle ID、技能 ID、nil、map、reducer、newtype、compare-and-swap 等技术词按上下文保留。英文标题以显式锚点保留，维持原引用兼容。普通说明自然语言均已翻译，没有未译段落。

本审校属于语义和静态兼容核对，不是运行这些原则指导的实际编程任务，也不据此宣称外部工具、宿主或模型路径已经运行通过。
