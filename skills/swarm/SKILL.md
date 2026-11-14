---
name: swarm
description: "并行启动 N 个工作者，等待其全部结束，再返回一份报告。用于 /swarm、'swarm this'，或并行覆盖、竞赛、多轮考验和探索。"
disable-model-invocation: true
---

<a id="swarm"></a>

# 并行工作群

<a id="start"></a>

## 开始

启动任何工作之前，先建立待办清单，每个阶段一项。

1. 界定任务
2. 展开并行
3. 汇总
4. 报告

<a id="phase-a-frame"></a>

## 阶段 A：界定任务

1. 陈述完成谓词，以及工作群必须返回的产物或报告。
2. 选择组织方式。可以分片，可以让 N 个工作者根据相同任务说明竞赛，也可以混合两者。若采用竞赛或混合方式，在启动前声明 `first pass`（首个通过）、`rank all`（全部排序）或 `best-of`（择优）。
3. 从 pstack 设置文件中的 `swarm workers` 行选择工作者模型（Cursor 为 `~/.cursor/rules/pstack-models.mdc`，Claude Code 为 `~/.claude/rules/pstack-models.md`，其他智能体运行环境为 `~/.agents/pstack-models.md`）。文件或该行缺失时，使用 `grok-4.7-xhigh-fast`。值为 `auto` 或 `inherit-parent` 时，省略 `model`，使工作者继承父模型。如果子代理工具拒绝某个 slug，使用默认值并说明。如果默认值也被拒绝，就从错误消息或运行环境模型列表中，选同系列最接近的有效 slug。模型竞赛应提前列明每个参赛分支的模型。根据 **poteto-mode** 技能的“子代理”部分，为每个子代理选择适合任务的推理级别以及快速或标准速度。
4. 工作者需要写入时，为每个工作者提供独立的可写输出。验证或测量提交时，每份任务说明都要给出精确 SHA。测量任务说明还应指定方法（样本数量、一个样本的定义、顺序）。工作者在结果中记录这两项。

<a id="phase-b-fan-out"></a>

## 阶段 B：展开并行

在同一条消息中启动全部 N 个工作者，指定 `subagent_type: generalPurpose`、`environment: "cloud"`、`run_in_background: true`，以及第 3 步选择的模型；若为 `auto` 或 `inherit-parent`，则不设模型。只有工作者需要访问用户电脑上的内容时，才使用 `environment: "local"`。

工作者必须从已推送的非默认分支开始时，传入 `cloud_base_branch`。

**其他智能体运行环境。** 这些参数属于 Cursor 的 `Task` 工具；`environment: "cloud"` 会运行 Cursor 云端智能体。在其他运行环境中，使用其子代理工具：Claude Code 的 `Agent`（`subagent_type: general-purpose`）、OpenCode 的 `task`（`subagent_type: general`）、Codex 的 `spawn_agent`。这些环境中的工作者在本地运行，因此为每个工作者提供独立的 Git 工作树或输出路径。保留任务说明和模型，去掉工具不支持的参数。如果运行环境没有子代理工具，例如没有扩展的 Pi，就由你逐个执行这些工作者的任务。

每份任务说明必须独立完整。包括目标、范围、准确的分片或参赛分支、验证方法和报告要求。报告采用 `PASS`、`ISSUES` 或 `BLOCKED`，并附证据。能证明缺陷的工作者报告 `ISSUES`，并列出能够证明的每一个问题，不能只列第一个。

如果某个工作者中途退出，继续以 N-1 个工作者推进并注明。

<a id="phase-c-aggregate"></a>

## 阶段 C：汇总

阅读最终结果。如果结果没有记录任务说明所要求的 SHA 和方法，丢弃该结果，并重新启动该工作者一次。第二次仍遗漏，就记录为缺口。缺口不算通过。覆盖任务的每个必要分片都必须有结果。竞赛则应用事先声明的选择规则：首个通过、全部排序或择优。不要直接粘贴工作者的原始输出。

<a id="phase-d-report"></a>

## 阶段 D：报告

在聊天中返回一份合并后的报告，包含结果表、每个问题的一句话说明、缺口或退出情况，以及采用竞赛时使用的规则。
