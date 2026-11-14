<a id="multi-phase-or-multi-pr-plan"></a>

### 多阶段或多 PR 计划

**你负责计划，不负责代码。计划是负责人逐格执行、操作者根据证据审计的清单。** 交付物就是计划，不要实现。

1. 改动只有一两个文件且方案显然时，跳过计划，说明后停止。
2. 动笔前用原型解决开放问题。每个问题都运行 `playbooks/prototype.md`。为附录 A 保留分支、SHA 和截图。只为任何运行都不能决定的产品或偏好决策询问操作者。提供选项，参见 **never-block-on-the-human** 原则技能。
3. 通过子代理探索，使用 `subagent_type: "poteto-agent"`，按“子代理”一节明确设置模型，参见 **guard-the-context-window** 原则技能。按该节为每个子代理选择推理级别及 fast 或标准速度。各自返回文件指针、约定、测试命令和入口，不内联倾倒内容。
4. 将下方骨架复制到计划文件，填好每个占位符。操作者未指定路径时，写入智能体存储的 `docs/`。保留每个标题和子块，并按所示顺序排列。每 PR 一个章节。一个 PR 是一项带自身证据的改动，参见 **sequence-verifiable-units** 原则技能。在 **How to read this** 中点明执行操作手册。允许运行合并时选 `playbooks/autopilot-full.md`；操作者落地 PR 时选 `playbooks/autopilot-stack.md`；长期计划选 `playbooks/orchestrate.md`。
5. 完整遵循 `/technical-writing` 编写，再应用 `/unslop`。正文采用一种 Diátaxis 模式，即操作指南。附录放解释和参考。每个标题陈述任务或发现。不用长破折号，不用句中冒号。
6. 运行 `node pstack/skills/poteto-mode/scripts/check-plan.mjs <plan.md>`，修复它打印的每一行问题，参见 **encode-lessons-in-structure** 原则技能。
7. 交回。贴出计划路径和脚本输出，然后停止。只有操作者明确许可，才按计划指定的执行操作手册开始执行。

**验证。** 只有测试还不足以构成验证。PR 只有在 unit、live、perf 三类复选框全部勾选后才算已验证。这句话就是验证规则，每个验证块都以它开头。实时验证块不可缺少。按 **swarm** 技能，十条通道在 PR head 上通过控制技能操作真实界面，使用 `swarm workers` 模型，默认 `grok-4.7-xhigh-fast`。每条通道一格，包含具体场景、保存的截图和通过谓词。其中一条是 **Regression lane against trunk.（对主干的回归通道）**，在主干与 head 上运行同一关键场景。主干没有该功能时，记录该事实，门禁针对 diff 新增行为以及用户等待的最终状态，不编造主干结果。性能门禁必须双侧测量。主干和 head 都要产生具名指标。主干没有该功能时，还要隔离 diff 新增工作，并为它和用户等待的端到端状态设置绝对预算。不要为不同场景声称比率。性能块点明指标、交错运行的探测、先测的主干基线，以及包含失败数值的规则。改变交互的 PR 受审查门禁约束，合并前操作者在聊天中通过截图和视频审查。不改变交互的 PR 写 `**Review gate.** None. <PR id> is not review-gated.`，即无审查门禁，此 PR 无需该审查；下方不放复选框。

**控制技能。** 根据界面选择。浏览器、Electron 和 Web UI 用 `cursor-team-kit` 的 `control-ui`；CLI 和 TUI 用 `cursor-team-kit` 的 `control-cli`。原生移动端用仓库已有的模拟器控制技能。PR 涉及两种界面，两边都设通道。界面没有控制技能，是附录 C 中的一项风险，其实时验证块仍须点明各通道如何驱动。

以下模板中的英文标题、粗体块标签、验证规则原句，以及 Lane、Save、Pass when 等字样，受到 `check-plan.mjs` 精确匹配，因此保留原文，并在相邻位置给出中文说明。占位符保留原结构和内容，填写时按中文说明理解。

受保护模板名称的中文对照如下。填写计划时保留左列原文。

| 英文模板名称或标记 | 中文含义 |
| --- | --- |
| `How to read this` | 阅读方法 |
| `Program checklist` | 计划检查清单 |
| `Arm the program` | 准备执行计划 |
| `Spawn owners` | 启动负责人 |
| `PR mechanics, for every PR` | 每个 PR 的操作约定 |
| `Verdict and merge, for every PR` | 每个 PR 的裁决与合并 |
| `Boot recipe, for every live lane` | 每条实时验证通道的启动步骤 |
| `Depends on.` / `Files.` / `Build.` / `You see.` | 依赖／文件／构建／可见结果 |
| `Verify, unit.` / `Verify, live.` / `Verify, perf.` | 单元验证／真实运行验证／性能验证 |
| `Review gate.` / `Merge.` | 审查门禁／合并 |
| `Close the program` | 结束计划 |
| `Appendix A. Prototype evidence` | 附录 A：原型证据 |
| `Appendix B. Alternatives rejected` | 附录 B：被否决的方案 |
| `Appendix C. Risks` | 附录 C：风险 |
| `Appendix D. Links and reading list` | 附录 D：链接和阅读清单 |
| `Lane` / `Save` / `Pass when` | 通道／保存／通过条件 |
| `Metric.` / `Probe.` / `Baseline.` / `Rule.` | 指标／探测／基线／规则 |

````markdown
# <Program> 计划

<Under ten lines. What changes, for whom, the rule the program enforces, and the PR ids in order.>
（少于十行。说明改动、服务对象、计划执行的规则，以及依次排列的 PR ID。）

## How to read this

One box is one unit of work. Every box names the evidence that checks it. A nested box is a sub-step of the box above it. Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA.
每格是一项工作单元，点明勾选所需证据。嵌套格是上层格的子步骤。只有文件、日志行、截图、测试运行或 SHA 等证据存在时才勾选。正文是操作指南，附录负责解释与记录。

计划运行 `pstack/skills/poteto-mode/playbooks/<execution playbook>.md`。<Who merges, and which PR ids are the operator's items that stop at merge-ready.>
（说明谁合并，以及哪些 PR ID 由操作者负责，只推进到可合并。）

Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.
仅测试不足以构成验证。PR 只有在单元、实时、性能三类复选框全部勾选后才算已验证。

## Program checklist

### Arm the program

- [ ] 向操作者说明协议和本计划，然后停止。只有操作者明确许可才开始执行。
- [ ] 计划开始时从主干读取以下内容，每次心跳重读。
  - [ ] `git show origin/main:pstack/skills/poteto-mode/playbooks/<execution playbook>.md`
  - [ ] `git show origin/main:pstack/skills/swarm/SKILL.md`
  - [ ] `git show origin/main:<control skill path>`
  - [ ] `git show origin/main:pstack/skills/poteto-mode/playbooks/opening-a-pr.md`
  - [ ] `git show origin/main:pstack/skills/<each other leaf skill the program uses>`
- [ ] 操作者许可后，用下方心跳提示词启用 `/loop 1h` 审计心跳。绝不靠记忆维持节奏。
- [ ] 原样使用此心跳提示词。"从主干重读执行操作手册。对照它审计本次操作，并在本轮修复偏移。探测每条活动通道，只根据实际副作用判断进展。停止卡住的通道，立即派出替补。只有审计发现此前状态消息未报告的已跟踪变化时，才在聊天向操作者发布简短状态消息（status message），例如已创建 PR、代码就绪 head、轮次开启或结束、裁决、合并、智能体停滞及采取的措施、阻塞新增或解除，或只有操作者能作出的决策。只点明每项此类变化。不重复表格、已合并列表或未改变阻塞。未发现变化时，结束轮次且不回复文字。无论哪种情况，都在决策轨迹记录本次心跳行，写明已报告事项或 none。"
- [ ] 操作者要求保持或停止时，立即向每名负责人发出零写入指令。

### Spawn owners

- [ ] 每个 PR 创建一名负责人，职责覆盖执行操作手册指定的完整生命周期。
- [ ] 遵循此依赖图。依赖工作只在父项合并后开始；执行操作手册采用堆叠时，也可基于父分支。
  - [ ] <PR id> 和 <PR id> 互相独立，最先开始，都从 `main` 分支。
  - [ ] <PR id> 在 <PR id> 之后。
- [ ] 严守文件边界。<PR id or class> 只修改 `<glob>`。
- [ ] 严守审查门禁。<PR ids> 改变交互，合并前等待操作者在聊天通过截图和视频审查。

### PR mechanics, for every PR

- [ ] 只解析一次托管平台。默认 `gh`；若 `command -v origin` 成功且 Origin 能解析仓库，每项 PR 操作都用 `origin pr`。记录任何回退到 `gh` 的情况。绝不要求 `gt`。
- [ ] 按 **Opening a PR（创建 PR）** 以 ready 创建 PR，绝不用 draft。运行环境有内置 PR 工具时使用它，否则按平台用 `origin pr create --status open --base <base-branch>` 或 `gh pr create --base <base-branch>`。栈中子 PR 目标为父分支。
- [ ] 面向 PR 的推送前，运行一次仓库 lint 和 typecheck，推送时开启 hooks。
- [ ] 每次提交前运行 `/deslop`，审查前运行 `/no-comments`。
- [ ] 按 `../references/bugbot-triage.md` 分类每条 Bugbot 和安全审查者评论。
- [ ] 代码就绪报告和 babysit 前 rebase 到当前主干。修复轮次保留该合并基线。只在合并准备、`git merge-tree` 显示与主干冲突、主干改动导致 CI 失败，或已知并发改动落到相同文件时，再次 rebase。

### Verdict and merge, for every PR

- [ ] 完整 swarm 在代码就绪 head 上运行一次。只有新增行为、重新设计或大幅新增 diff 才再次完整运行。rebase、解决合并冲突或小修复只需一个验证器在新 head 验证，纯措辞修改不需要。每次完整 swarm 按 `pstack/skills/swarm/SKILL.md` 运行。包括一条门禁通道、PR 的 **Verify, live** 块中的十条实时通道、其 **Verify, perf** 块中的性能通道，以及至少两条各有重点的审计通道。审计通道读取 diff 和凭据，不信任 PR 正文。裁决前根智能体审计可合并报告中的凭据。
- [ ] 按执行操作手册的阻塞规则判断每项发现。没有阻塞才是干净裁决。标记为 `Regression lane against trunk.` 的通道中，主干行为失败记录到主干名下，不阻塞 PR。新 head 需要新裁决，符合 `playbooks/shipping.md` patch-id 规则而仍有效的结果除外。
- [ ] <The merge or handoff rule from the execution playbook, with the patch-id rule from `playbooks/shipping.md`.>
  （填写执行操作手册的合并或交接规则，并包含 `playbooks/shipping.md` 的 patch-id 规则。）

### Boot recipe, for every live lane

每条实时通道在 PR head 上使用独立云端虚拟机。通过 `cursor-team-kit` 的 `control-ui` 或 `control-cli` 操作。

- [ ] `git fetch origin <head-branch> && git checkout <head SHA>`。
- [ ] <Start the backend and the surface. Wait for ready.>
  （启动后端和对应界面，等待就绪。）
- [ ] <Deliver input only through the control skill's commands. Name the read-only diagnostics.>
  （只通过控制技能命令输入，点明只读诊断方式。）
- [ ] 每张截图保存到 `/tmp/swarm-<pr-id>/worker-<n>/<slug>.png`，随报告返回路径。

## <Task as a verb phrase> (<PR id>)

（标题用动词短语描述任务。）

**Depends on.** <PR id, or None.>
（依赖的 PR ID；没有依赖写 None。）

**Files.**

- [ ] 编辑 `<path>`。
- [ ] 创建 `<path>`。
- [ ] 删除 `<path>`。

**Build.**

- [ ] <One change. Name the symbol and the file.>
  （一项改动，点明符号和文件。）

**You see.**

- [ ] <One observable result, with the exact log line or screen state.>
  （一个可观察结果，附准确日志行或屏幕状态。）

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.
（单元验证。仅测试不足以构成验证；单元、实时、性能三类复选框全勾选才算通过。）

- [ ] <Test file and the case it gains.> 运行 `<command>`。
  （测试文件及新增用例。）

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on `<swarm workers model>` at the PR head，按启动步骤运行。
（实时验证。仍须满足完整验证规则；用指定模型在 PR head 上运行十条通道。下列 Lane 为通道编号，Save 指保存截图，Pass when 指通过谓词。）

- [ ] Lane 1. Regression lane against trunk. 在主干和 head 运行 <the same load-bearing scenario>。主干缺少功能时，记录事实，并对 <the behavior the diff adds plus the end state the user waits for> 设门禁。Save `<slug>.png`。Pass when <predicate>。
- [ ] Lane 2. <Scenario.> Save `<slug>.png`。Pass when <predicate>。
- [ ] Lane 3. <Scenario.> Save `<slug>.png`。Pass when <predicate>。
- [ ] Lane 4. <Scenario.> Save `<slug>.png`。Pass when <predicate>。
- [ ] Lane 5. <Scenario.> Save `<slug>.png`。Pass when <predicate>。
- [ ] Lane 6. <Scenario.> Save `<slug>.png`。Pass when <predicate>。
- [ ] Lane 7. <Scenario.> Save `<slug>.png`。Pass when <predicate>。
- [ ] Lane 8. <Scenario.> Save `<slug>.png`。Pass when <predicate>。
- [ ] Lane 9. <Scenario.> Save `<slug>.png`。Pass when <predicate>。
- [ ] Lane 10. <Scenario.> Save `<slug>.png`。Pass when <predicate>。

（第 1 条为主干回归通道，同一关键场景在两端运行。其余填写各自场景。主干缺少功能时，门禁针对 diff 新增行为和用户等待的最终状态。每条填写保存的截图文件名及通过条件。）

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.
（性能验证。仍须满足完整验证规则。）

- [ ] Metric. <What is measured at both trunk and head. If trunk lacks the feature, also name the diff-added work and the end-to-end state the user waits for.>
  （指标。点明主干和 head 都测量什么；主干缺少功能时，还要点明 diff 新增工作和用户等待的端到端状态。）
- [ ] Probe. <The command or procedure, run at trunk and at the head, interleaved. Both sides must produce the metric.>
  （探测。命令或流程在主干和 head 交错运行，两边都必须产生指标。）
- [ ] Baseline. 先记录主干 <value>。
  （基线。）
- [ ] Rule. <Head against trunk, with the number that fails. If the scenarios differ, add absolute budgets for the diff-added work and the user-visible end state instead of an invalid ratio.>
  （规则。比较 head 与主干并写明失败数值。场景不同时，为 diff 新增工作和用户可见最终状态设置绝对预算，不用无效比率。）

**Review gate.** 合并前由操作者审查。

- [ ] 将通道 <n> 的截图（screenshot）复制到 `<media path>/<pr-id>-review-<slug>.png`。
- [ ] 在通道虚拟机录制 30 到 60 秒的改动视频（video），保存为 `<media path>/<pr-id>-review.mp4`。
- [ ] 在聊天贴出截图和视频。停在可合并状态，等待操作者（operator）点击。

**Merge.**

- [ ] 根智能体针对精确 head SHA 的干净裁决。
- [ ] Bugbot 分类已完成。
- [ ] 裁决后 rebase 到当前主干，patch-id 不变。
- [ ] <The owner squash-merges its own PR, or the root appends it to the base-branch stack and the operator lands it bottom-up.>
  （负责人 squash 合并自己的 PR，或由根智能体追加到基线分支栈，操作者自底向上落地。）

## Close the program

- [ ] 上方每格都有证据且已勾选。
- [ ] 按执行操作手册指定的报告向操作者回复。

## Appendix A. Prototype evidence

<Each open question a prototype answered, with the branch, the SHA, and the artifact links. Each question that stays unproven.>
（逐项记录原型已回答的开放问题，附分支、SHA 和交付物链接；逐项记录仍未证明的问题。）

## Appendix B. Alternatives rejected

<Each approach weighed and why it lost.>
（每项考虑过的方案及落选原因。）

## Appendix C. Risks

<Each risk with the PR it lands in and what the owner watches.>
（每项风险、它落在哪个 PR、负责人监视什么。）

## Appendix D. Links and reading list

<Docs to read before editing. Which PRs get `pstack/skills/how/SKILL.md` and `pstack/skills/interrogate/SKILL.md`. The trail per `pstack/skills/show-me-your-work/SKILL.md`.>
（编辑前必读文档、哪些 PR 使用这两个技能，以及按 show-me-your-work 技能建立的轨迹。）
````

**回复：** 计划路径、PR ID 及其依赖和受审查门禁约束的集合、原型证明了什么及仍未证明什么、检查脚本输出。
