<a id="build-the-change-and-clean-the-diff"></a>

# 构建改动并清理差异

构建操作手册共享一种纪律：说清观察到什么，让操作手册要求证据。本页展示每种常见构建任务的提示词应写什么，以及如何通过清理习惯保持差异易于审查。

<a id="prompt-each-build-playbook-with-what-you-know"></a>

## 用已知信息提示各构建操作手册

缺陷提示词说明症状，要求先复现：

```text
/poteto-mode 这条命令在重试后会输出两条记录。先复现，再修复并验证。
```

功能提示词说明行为，以及什么必须保持不变：

```text
/poteto-mode 增加 --json 标志。文本输出必须逐字节保持一致。验证两种形式。
```

重构提示词在调整结构前固定行为：

```text
/poteto-mode 把解析逻辑移到一个模块中，行为完全不变。先记录当前输出，再证明改动后没有变化。
```

性能提示词给出测量，而非印象：

```text
/poteto-mode 在这份测试夹具上启动耗时 1.8s。追踪它，修复测量得到的原因，展示前后对比。
```

这些提示分别路由到对应操作手册（[缺陷修复](../../skills/poteto-mode/playbooks/bug-fix.md)、[功能开发](../../skills/poteto-mode/playbooks/feature.md)、[重构](../../skills/poteto-mode/playbooks/refactoring.md)、[性能问题](../../skills/poteto-mode/playbooks/perf-issue.md)）。操作手册会补上你没写出的步骤：修复前复现、实现前说明数据形态、重构前固定行为、优化前分析性能。

若要持续改善一个数字，可以使用[爬坡优化操作手册](../../skills/poteto-mode/playbooks/hillclimb.md)。给出指标、目标和最少尝试次数，它会冻结测量运行环境，每次循环检验一个假设。保留有效改进，回退其他一切。

两份性能操作手册都会用 [`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) 审核数字。性能问题操作手册审核基线及此后每个数字；爬坡优化操作手册在冻结前审核测量运行环境。[验证并交付](./06-verify-and-ship.md#vet-a-measured-number-with-benchmark-checklist)介绍了何时应该自行输入它。

有时你想先知道原因，不急着修复。对于泄漏、空闲时 CPU 空转或视觉异常等实时症状，[运行时取证操作手册](../../skills/poteto-mode/playbooks/runtime-forensics.md)会为运行中的进程添加观测手段。对于已经捕获的性能剖析，[跟踪取证操作手册](../../skills/poteto-mode/playbooks/trace-forensics.md)会读取产物，把热点栈帧映射到源码。两者都返回诊断，而非修复：

```text
/poteto-mode 这里有一份启动缓慢时的 cpuprofile。告诉我时间花在哪里，以及由哪些源码行负责。先不要修复。
```

<a id="write-the-failing-test-first-with-tdd"></a>

## 用 `/tdd` 先写失败测试

如果缺陷有低成本的本地测试路径，整个提示词可以只有两个词：

```text
/tdd 实现
```

这里直接要求“实现”。在已有上下文中，这就够了。[`/tdd`](../../skills/tdd/SKILL.md) 先写因预期原因而失败的最小测试，再写修复，然后重新运行测试。如果测试需要大规模环境搭建或脆弱的 mock，技能会明确说明，并改用最接近的可执行检查。当真实命令能提供更强证据时，不要强行写测试。

<a id="load-the-typescript-rules-by-name"></a>

## 按名称加载 TypeScript 规则

[`typescript-best-practices`](../../skills/typescript-best-practices/SKILL.md)把类型系统原则落实为具体规则：可辨识联合类型、边界处使用 `unknown`、穷尽变体，以及从 schema 派生类型。它不会自行加载，因此任务涉及 `.ts` 或 `.tsx` 文件时，请输入 `/typescript-best-practices`。

<a id="clean-before-you-commit"></a>

## 提交前先清理

[创建 PR 操作手册](../../skills/poteto-mode/playbooks/opening-a-pr.md)会在每次提交前对差异运行 `/deslop`，并对 PR 描述和提交正文使用 [`/unslop`](../../skills/unslop/SKILL.md)。`/deslop` 由 `cursor-team-kit` 插件提供，不属于 pstack。如果没有它，就用普通语言要求同样的结果：去掉复述代码的注释、无依据的防御检查、失效的兼容路径和无关改动。

处理文字时，向 `/unslop` 提供目标及额外规则：

```text
/unslop readme 中的改动，不要用长破折号
```

你会逐渐形成自己的简写。像 `unslop that, tighten it`（清理那段文字，再紧凑些）这样的简短提示，技能也能准确理解意图。

<a id="strip-the-comments-with-no-comments"></a>

## 用 `/no-comments` 清理注释

注释需要单独检查，而且不能由写它们的智能体来检查。作者会像你捍卫自己的注释一样为其辩护。因此在审查前，请换一双眼睛：

```text
/no-comments 检查差异
```

[`/no-comments`](../../skills/no-comments/SKILL.md)会启动 [Comment Sicko](../../agents/comment-sicko.md)，这是一位只读审查者，保留清单很短：许可证头、公共 API 文档注释、解释代码无法表达之约束的链接，以及无法重塑的外部依赖强制产生的行为。其余都要删除。自己代码中的意外行为没有这种豁免；注释会以重构标记的形式返回，`/no-comments` 则从根因修复它接受的标记。当注释声称存在约束，例如“不要删除”时，技能会提议将其编码成类型、测试或 lint。无论哪种方式，注释都会移除。

要记清分工：`/deslop` 清理代码中的冗余杂质，`/unslop` 清理文字，`/no-comments` 则把注释交给没有写过它们的审查者。

**陷阱：** 清理不是可有可无的润色。带有复述代码的注释和无用防御代码的差异，在审查者看来仍未完成；多余代码也正是下一个缺陷的藏身处。如果差异显得臃肿，请在提交前说 `deslop it`（清理冗余），而不是等审查指出后再做。

下一页：[验证并交付](./06-verify-and-ship.md)。
