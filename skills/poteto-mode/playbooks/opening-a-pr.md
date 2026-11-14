<a id="opening-a-pr"></a>

### 创建 PR

在其他每份操作手册末尾调用。

**Git 工作树。** 从 main 派生的 Git 工作树中开展工作，子代理继承它。同一分支上的多次 `Task` 调用各自使用独立工作树，或在两次调用之间运行 `git fetch && git reset --hard origin/<branch>`。脏分支中有无关工作时，先导出补丁，新建工作树，再应用。工作树纠缠不清时，从 main 重置后按最小范围重做。

**提交。** 勤做提交。创建 PR 前 rebase 成小而有序的提交。每个提交都是未来 PR，要可落地、顺序能讲清变化。修复属于刚完成的提交时 amend；可以分离时新建提交。提交正文不重述标题。

**PR。** 提交前对 diff 运行 `cursor-team-kit` 的 `/deslop`，审查前运行 `/no-comments`。每个 PR 标题、描述、提交正文都用 `/technical-writing` 编写，应用除 Diátaxis 之外的每层规则，并应用 STE 词汇规则：一个动作一个词、保留冠词、有合适普通动词时不用 `-ing`；之后应用 `/unslop`。

**标题。** 使用 Conventional Commits 的 `type(scope): subject`，末尾不加句号。type 例如 `feat`、`fix`、`docs`、`refactor`、`test`、`chore`、`perf`。scope 为所属区域，例如 `pstack` 或 `poteto-mode`。subject 简短、用祈使句；有真实符号能承载变化时点名，例如 `fix(pstack): retarget opening-a-pr babysit trigger`（调整 opening-a-pr 的 babysit 触发条件）。

**描述。** PR 正文面向已拿到 diff 的审查者，是一分钟简报，不是实验室笔记。说明为何改、排除什么、可能破坏什么，以及如何证明能工作。用简短朴素句子，少放标识符，不堆文字墙。正文会成为 squash 提交正文，因此将该提交控制在约 40 行以内。使用 `##` 标题而非粗体引导词，按以下顺序，无内容的章节省略。标题原文用于流程约定，含义如下：

- `## Why`：问题和方案，1–3 个短句。不写 SHA、rebase 谱系，或“基于 main”的开场白。
- `## What changed`：1–3 个简短列表项。只有承载变化时才点名真实符号或路径。重命名或改目标时写明两端。
- `## Scope`：始终保留。用 1–3 个简短项目说明覆盖什么、刻意排除什么，例如后续项或已知缺口。不写符号、路径，也不逐文件长篇叙述。
- `## Tradeoffs`：只写审查者原本会追问的已拒绝方案。没有真正选择时跳过。
- `## Blast Radius`：1–2 句说明影响谁或什么，以及为何安全或有风险。main 已红时，说明继续放任它红着的代价。
- `## Verification`：1–3 项，每项是真实运行路径和结果。性能内容只列一个主要数字和单位，使用 `before → after`，其余链接到 arena 或 swarm 目录。不写样本量方法论、swarm 通道逐一复述或指标表。

章节后，可在能证明主张时附视频或截图。完整 SHA、swarm 或 arena 通道逐一报告、杠杆工具修正长文、逐文件检查清单和 “CLEAN” 裁决，应放在链接的交付物中，不放正文。

**托管平台。** 首次 PR 操作前解析平台，之后创建、编辑、查看、监视、合并保持同一选择。默认 GitHub CLI（`gh`）。若 `command -v origin` 成功且 Origin 能解析仓库，优先 `origin pr ...`。Origin 不存在或不能解析仓库时继续用 `gh`，并记录回退。不要求 Graphite（`gt`）。

**内置 PR 工具。** 运行环境提供内置 PR 工具时，通过它创建、编辑、改目标和标记 ready，绝不用平台 CLI。CLI 创建的 PR 会缺少该工具跟踪的信息。工具不覆盖的操作使用已解析平台；运行环境没有此工具时，所有 PR 操作都用该平台。

**大小与 PR 栈。** 宁可五个聚焦 PR，也不要一个大 PR。PR 栈是基线分支链。栈根 PR 目标为主干。每个子分支 rebase 到父分支精确 tip，PR 目标指向父分支。父 PR 合并时，按 `playbooks/shipping.md` 第 4 步把子 PR 移到主干。没有内置 PR 工具时，根据已解析平台，创建子 PR 用 `origin pr create --status open --base <parent-branch>` 或 `gh pr create --base <parent-branch>`；改目标用 `origin pr edit <pr> --base <parent-branch>` 或 `gh pr edit <pr> --base <parent-branch>`。只有独立工作才从主干分支。实质性 PR 栈工作开始前先 rebase 到主干。

**就绪状态。** 每个 PR 都以 ready 创建，绝不用 draft。内置 PR 工具可能默认 draft，因此每次创建调用都设置 `draft: false`。Origin 传 `--status open`；`gh` 省略 `--draft`。如果 PR 仍以 draft 打开，用 PR 工具标记 ready，或按平台运行 `origin pr ready <number>` 或 `gh pr ready <number>`。提及 PR 状态之前，运行 `origin pr view <number>` 或 `gh pr view <number>`。

**Babysit（跟进 PR）。** 创建 PR 不启动 babysit。贴出 URL 后继续构建。先完成阶段或 PR 栈。只有整栈存在后用户要求时，才单独跟进。每创建一个 PR 就 babysit，会拖停构建，并把检查消耗在后续轮次又会重启的提交上。反馈偏离意图时提出异议。

创建 PR 的子代理运行 `/deslop` 和 `/no-comments`，贴出 URL。随后不 babysit，直接返回父智能体；Autopilot-full（完全自动驾驶） 或 Autopilot-stack（PR 栈自动驾驶） 负责人除外。该负责人的任务说明已分配 babysit 循环，也就是 `playbooks/babysit.md` 等待的请求。负责人在代码就绪报告后开始循环、报告可合并状态，不受本节及 `playbooks/babysit.md` 中“整栈构建完成才跟进”的规则限制。
