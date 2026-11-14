# example 计划

example
（少于十行。说明改动、服务对象、计划执行的规则，以及依次排列的 PR ID。）

## How to read this

One box is one unit of work. Every box names the evidence that checks it. A nested box is a sub-step of the box above it. Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA.
每格是一项工作单元，点明勾选所需证据。嵌套格是上层格的子步骤。只有文件、日志行、截图、测试运行或 SHA 等证据存在时才勾选。正文是操作指南，附录负责解释与记录。

计划运行 `pstack/skills/poteto-mode/playbooks/example.md`。example
（说明谁合并，以及哪些 PR ID 由操作者负责，只推进到可合并。）

Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.
仅测试不足以构成验证。PR 只有在单元、实时、性能三类复选框全部勾选后才算已验证。

## Program checklist

### Arm the program

- [ ] 向操作者说明协议和本计划，然后停止。只有操作者明确许可才开始执行。
- [ ] 计划开始时从主干读取以下内容，每次心跳重读。
  - [ ] `git show origin/main:pstack/skills/poteto-mode/playbooks/example.md`
  - [ ] `git show origin/main:pstack/skills/swarm/SKILL.md`
  - [ ] `git show origin/main:example`
  - [ ] `git show origin/main:pstack/skills/poteto-mode/playbooks/opening-a-pr.md`
  - [ ] `git show origin/main:pstack/skills/example`
- [ ] 操作者许可后，用下方心跳提示词启用 `/loop 1h` 审计心跳。绝不靠记忆维持节奏。
- [ ] 原样使用此心跳提示词。"从主干重读执行操作手册。对照它审计本次操作，并在本轮修复偏移。探测每条活动通道，只根据实际副作用判断进展。停止卡住的通道，立即派出替补。只有审计发现此前状态消息未报告的已跟踪变化时，才在聊天向操作者发布简短状态消息（status message），例如已创建 PR、代码就绪 head、轮次开启或结束、裁决、合并、智能体停滞及采取的措施、阻塞新增或解除，或只有操作者能作出的决策。只点明每项此类变化。不重复表格、已合并列表或未改变阻塞。未发现变化时，结束轮次且不回复文字。无论哪种情况，都在决策轨迹记录本次心跳行，写明已报告事项或 none。"
- [ ] 操作者要求保持或停止时，立即向每名负责人发出零写入指令。

### Spawn owners

- [ ] 每个 PR 创建一名负责人，职责覆盖执行操作手册指定的完整生命周期。
- [ ] 遵循此依赖图。依赖工作只在父项合并后开始；执行操作手册采用堆叠时，也可基于父分支。
  - [ ] example 和 example 互相独立，最先开始，都从 `main` 分支。
  - [ ] example 在 example 之后。
- [ ] 严守文件边界。example 只修改 `example`。
- [ ] 严守审查门禁。example 改变交互，合并前等待操作者在聊天通过截图和视频审查。

### PR mechanics, for every PR

- [ ] 只解析一次托管平台。默认 `gh`；若 `command -v origin` 成功且 Origin 能解析仓库，每项 PR 操作都用 `origin pr`。记录任何回退到 `gh` 的情况。绝不要求 `gt`。
- [ ] 按 **Opening a PR（创建 PR）** 以 ready 创建 PR，绝不用 draft。运行环境有内置 PR 工具时使用它，否则按平台用 `origin pr create --status open --base example` 或 `gh pr create --base example`。栈中子 PR 目标为父分支。
- [ ] 面向 PR 的推送前，运行一次仓库 lint 和 typecheck，推送时开启 hooks。
- [ ] 每次提交前运行 `/deslop`，审查前运行 `/no-comments`。
- [ ] 按 `../references/bugbot-triage.md` 分类每条 Bugbot 和安全审查者评论。
- [ ] 代码就绪报告和 babysit 前 rebase 到当前主干。修复轮次保留该合并基线。只在合并准备、`git merge-tree` 显示与主干冲突、主干改动导致 CI 失败，或已知并发改动落到相同文件时，再次 rebase。

### Verdict and merge, for every PR

- [ ] 完整 swarm 在代码就绪 head 上运行一次。只有新增行为、重新设计或大幅新增 diff 才再次完整运行。rebase、解决合并冲突或小修复只需一个验证器在新 head 验证，纯措辞修改不需要。每次完整 swarm 按 `pstack/skills/swarm/SKILL.md` 运行。包括一条门禁通道、PR 的 **Verify, live** 块中的十条实时通道、其 **Verify, perf** 块中的性能通道，以及至少两条各有重点的审计通道。审计通道读取 diff 和凭据，不信任 PR 正文。裁决前根智能体审计可合并报告中的凭据。
- [ ] 按执行操作手册的阻塞规则判断每项发现。没有阻塞才是干净裁决。标记为 `Regression lane against trunk.` 的通道中，主干行为失败记录到主干名下，不阻塞 PR。新 head 需要新裁决，符合 `playbooks/shipping.md` patch-id 规则而仍有效的结果除外。
- [ ] example
  （填写执行操作手册的合并或交接规则，并包含 `playbooks/shipping.md` 的 patch-id 规则。）

### Boot recipe, for every live lane

每条实时通道在 PR head 上使用独立云端虚拟机。通过 `cursor-team-kit` 的 `control-ui` 或 `control-cli` 操作。

- [ ] `git fetch origin example && git checkout example`。
- [ ] example
  （启动后端和对应界面，等待就绪。）
- [ ] example
  （只通过控制技能命令输入，点明只读诊断方式。）
- [ ] 每张截图保存到 `/tmp/swarm-example/worker-example/example.png`，随报告返回路径。

## example (example)

（标题用动词短语描述任务。）

**Depends on.** example
（依赖的 PR ID；没有依赖写 None。）

**Files.**

- [ ] 编辑 `example`。
- [ ] 创建 `example`。
- [ ] 删除 `example`。

**Build.**

- [ ] example
  （一项改动，点明符号和文件。）

**You see.**

- [ ] example
  （一个可观察结果，附准确日志行或屏幕状态。）

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.
（单元验证。仅测试不足以构成验证；单元、实时、性能三类复选框全勾选才算通过。）

- [ ] example 运行 `example`。
  （测试文件及新增用例。）

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on `example` at the PR head，按启动步骤运行。
（实时验证。仍须满足完整验证规则；用指定模型在 PR head 上运行十条通道。下列 Lane 为通道编号，Save 指保存截图，Pass when 指通过谓词。）

- [ ] Lane 1. Regression lane against trunk. 在主干和 head 运行 example。主干缺少功能时，记录事实，并对 example 设门禁。Save `example.png`。Pass when example。
- [ ] Lane 2. example Save `example.png`。Pass when example。
- [ ] Lane 3. example Save `example.png`。Pass when example。
- [ ] Lane 4. example Save `example.png`。Pass when example。
- [ ] Lane 5. example Save `example.png`。Pass when example。
- [ ] Lane 6. example Save `example.png`。Pass when example。
- [ ] Lane 7. example Save `example.png`。Pass when example。
- [ ] Lane 8. example Save `example.png`。Pass when example。
- [ ] Lane 9. example Save `example.png`。Pass when example。
- [ ] Lane 10. example Save `example.png`。Pass when example。

（第 1 条为主干回归通道，同一关键场景在两端运行。其余填写各自场景。主干缺少功能时，门禁针对 diff 新增行为和用户等待的最终状态。每条填写保存的截图文件名及通过条件。）

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.
（性能验证。仍须满足完整验证规则。）

- [ ] Metric. example
  （指标。点明主干和 head 都测量什么；主干缺少功能时，还要点明 diff 新增工作和用户等待的端到端状态。）
- [ ] Probe. example
  （探测。命令或流程在主干和 head 交错运行，两边都必须产生指标。）
- [ ] Baseline. 先记录主干 example。
  （基线。）
- [ ] Rule. example
  （规则。比较 head 与主干并写明失败数值。场景不同时，为 diff 新增工作和用户可见最终状态设置绝对预算，不用无效比率。）

**Review gate.** 合并前由操作者审查。

- [ ] 将通道 example 的截图（screenshot）复制到 `example/example-review-example.png`。
- [ ] 在通道虚拟机录制 30 到 60 秒的改动视频（video），保存为 `example/example-review.mp4`。
- [ ] 在聊天贴出截图和视频。停在可合并状态，等待操作者（operator）点击。

**Merge.**

- [ ] 根智能体针对精确 head SHA 的干净裁决。
- [ ] Bugbot 分类已完成。
- [ ] 裁决后 rebase 到当前主干，patch-id 不变。
- [ ] example
  （负责人 squash 合并自己的 PR，或由根智能体追加到基线分支栈，操作者自底向上落地。）

## Close the program

- [ ] 上方每格都有证据且已勾选。
- [ ] 按执行操作手册指定的报告向操作者回复。

## Appendix A. Prototype evidence

example
（逐项记录原型已回答的开放问题，附分支、SHA 和交付物链接；逐项记录仍未证明的问题。）

## Appendix B. Alternatives rejected

example
（每项考虑过的方案及落选原因。）

## Appendix C. Risks

example
（每项风险、它落在哪个 PR、负责人监视什么。）

## Appendix D. Links and reading list

example
（编辑前必读文档、哪些 PR 使用这两个技能，以及按 show-me-your-work 技能建立的轨迹。）
