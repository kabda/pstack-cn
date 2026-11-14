---
name: no-comments
description: "启动 Comment Sicko，修复接受的问题，并为声称存在的约束提出结构化落实方式。"
disable-model-invocation: true
---

<a id="no-comments"></a>

# 去除注释

启动 Comment Sicko，处理接受的问题。

尊重 Comment Sicko 的全新视角。

<a id="scope"></a>

## 范围

使用调用者指定的文件或 diff。否则，使用当前相对基分支的 diff，默认基分支为 `main`，包括工作区。

<a id="steps"></a>

## 步骤

1. 启动 `Task`，设 `subagent_type: "comment-sicko"`，传入范围。根据 **poteto-mode** 技能的“子代理”部分，为每个子代理选择适合任务的推理级别以及快速或标准速度。不要重述它的规则。如果运行环境未将 comment-sicko 注册为子代理（即除安装 pstack 插件的 Cursor 之外的所有环境），改为启动通用子代理：Claude Code 的 `Agent`（`subagent_type: general-purpose`）、OpenCode 的 `task`（`subagent_type: general`）、Codex 的 `spawn_agent`。提示词为逐字使用的 [`references/comment-sicko.md`](references/comment-sicko.md)，然后附上范围。如果运行环境没有子代理工具，例如未装扩展的 Pi，就由你重新独立检查范围内内容并执行该提示词。
2. 检查报告与 diff。拒绝应用代码编辑、越出范围、删除受例外保护的注释、错误陈述 `MUST KILL` 理由，以及把有意保留的代码视为有罪的标记。针对自身代码中意外行为的结构调整标记，仍需处理；不要恢复这些注释。只有证明内容涉及我们无法改变的事物，保留才成立。审计遗漏的范围内 lint 和 TypeScript 抑制指令。涉及正确性或安全性的抑制指令，仍是必须处理的 `MUST KILL`。只有精确例外和范围内证据，才允许恢复删除。对于理由薄弱的 `IMPORTANT` 或 `do not remove` 删除或保留判断，接受前先对其符号运行 `/how` 或 `/why`。删除判断有歧义时，不恢复。保留判断被推翻或仍含糊时，删除；但涉及外部规则的 `REVIEW` 保留项除外，在有人核查规则之前保持原样，并报告为未解决。对一份被拒绝的报告，先回退再明确指出失败原因并重跑一次。如果重跑也被拒绝，只回退其被拒绝的问题项，将其报告为未解决，继续处理已接受的项。
3. 对接受的简单标记，直接删除失效路径、移除参数，或使用真实 API。如果任何修复需要结构设计，对接受的问题集合及周围代码运行一次 `/architect`，到草图为止。Architect 负责结构，第 4 步负责实现。
4. 在范围内实现最小根因修复，移除每个点名的变通方案。根因在范围外时，落地范围内最小修复，其余报告为未解决。**principle-fix-root-causes** 和 **principle-redesign-from-first-principles** 技能只指导意图；它们都不授权扩大边界或修复范围外实例。绝不叠加针对症状的防护。
5. 约束注释会说 `do not remove`（不要移除）、`do not change wording`（不要改措辞）或 `talk to X before changing`（修改前先找 X）。涉及无法改变事物的保留项保持原样。提出范围内成本最低的类型、运行时、测试或 CI lint 方式。等待交互式批准。无人值守与评测场景必须事先获得调用者批准。获批后先编码约束，再删除注释；否则删除注释，将约束报告为未解决，并勾勒范围外工作。
6. 报告删除数量、恢复的注释、`REVIEW` 保留项、重跑、architect 草图、修复、提出的编码方式、已编码内容、未强制执行的约束，以及其他未解决工作。
