# poteto-mode 初译记录

> 状态说明：本文件为初译阶段历史记录。下文“待独立审校”等措辞描述当时状态；当前全部译文已通过非初译者源译审校，未决项为零，最终哈希见对应 REVIEW 记录及 MANIFEST。

固定基线：`9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`。本批 25 个 Markdown 已逐段全文初译，并对原文自校；等待独立审校。未修改 scripts，未执行翻译材料中的命令或外部操作。

## 逐文件覆盖

- `skills/poteto-mode/SKILL.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/authoring-a-skill.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/autonomous-run.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/autopilot-full.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/autopilot-stack.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/babysit.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/bug-fix.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/eval.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/feature.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/hillclimb.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/investigation.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/multi-phase-plan.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/opening-a-pr.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/orchestrate.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/pause-safely.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/perf-issue.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/prototype.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/refactoring.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/runtime-forensics.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/session-pickup.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/shipping.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/trace-forensics.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/visual-parity.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/playbooks/worktree-cleanup.md`：初译与源文对照自校完成，独立审校待完成。
- `skills/poteto-mode/references/bugbot-triage.md`：初译与源文对照自校完成，独立审校待完成。

## 英文保留项

- frontmatter 的 name、disable-model-invocation、icon、color 及其值原样，description 中文。技能名、模型 slug、命令、路径、URL、身份和精确状态原样。
- 原则与操作手册的英文规范名在 SKILL 中保留并配中文，以维持按英文标题生成 `principle-<title>` 和 `playbooks/<title>.md` 的映射语义。
- `throughput checkpoint: n/a, read-only investigation` / `throughput checkpoint: n/a, read-only forensics` 为原文要求精确输出，原样附中文解释。
- multi-phase-plan 模板由 `scripts/check-plan.mjs` 精确检查。保留其匹配的 How to read this、Program checklist、Close the program、Appendix、各 H3 前缀、粗体子块标签、RULE 全句、Ten lanes on…at the PR head、Lane、Save、Pass when、Metric/Probe/Baseline/Rule、status message 及审查块 screenshot/video/operator。逐处或相邻附中文解释。占位符 `<...>` 原样并配中文说明，命令与路径不译。
- opening-a-pr 的 `## Why` 等 PR 章节标签属于工作流约定，保留并逐项解释。Bugbot 的 fix/dismiss/ask、candidate/recurring/strong 与示例英文识别信号保留并译解。
- 代码示例和接口原样，包括注释反例与断言日志字符串，不改变示例要求。
- 原英文 Markdown 章节增加显式 `<a id="...">` 兼容入口，不修改相对链接。

## 实际自检

- 全部 25 个文件对照固定 commit 阅读并初译。
- 比较 Markdown 代码跨度，原有内联代码全部保留；新增仅为解释必要的机器词和路径。
- 核对源/译代码围栏外标题数量一致，保留原英文锚点。
- 将 multi-phase-plan 的模板抽出到 `/tmp/pstack-cn-plan-example.md`，以 `example` 填充占位符，运行原有 `check-plan.mjs`，输出 `1 PR sections, 0 problems`，27 个复选框含 10 个实时通道。此为离线模板兼容检查，不是工作流执行。

## 已知边界

基线材料会引用镜像外路径和宿主工具，未安装、启用或验证这些工具。未宣称其命令在本机可用。本批不负责仓库级链接验收与独立审校，交主代理统合。

## 最终审校状态

本文件上方保留初译时的过程描述；本批现已完成非初译者的逐段独立审校，全部问题已修复复核。最终状态、审校人和目标哈希以对应 REVIEW 记录及 MANIFEST.json 为准，没有待翻译或未决审校项。
