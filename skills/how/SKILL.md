---
name: how
description: "用于 how does X work（X 如何工作）、改动前的代码讲解，以及放置位置、所有权和分层问题（where should this live、which package owns this、is this the right layer）。说明子系统架构、运行时流程及入门所需心智模型。动机问题用 why。"
disable-model-invocation: true
---

<a id="how"></a>

# 如何工作

探索代码库，回答“X 如何工作？”这类问题。以资深工程师接手子系统所需的层次解释架构：足以建立可用心智模型，但不要写成逐行源码注解。

每次启动均为 `Task` 子代理，指定 `subagent_type: generalPurpose` 和 `readonly: true`。探索者使用 pstack 设置文件的 `how explorer` 行（Cursor 为 `~/.cursor/rules/pstack-models.mdc`，Claude Code 为 `~/.claude/rules/pstack-models.md`，其他智能体运行环境为 `~/.agents/pstack-models.md`），默认 `grok-4.7-xhigh-fast`；每个讲解者使用 `how explainer` 行，默认 `claude-opus-5-5-xhigh`。把 `model` 设为该行的值；文件或该行缺失时设为默认值。值为 `auto` 或 `inherit-parent` 时，不设置 `model`。子代理工具拒绝 slug 时，使用默认值并说明。默认值也被拒绝时，从错误消息或运行环境模型列表中选择同系列最接近的有效 slug。根据 **poteto-mode** 技能的“子代理”部分，为每个子代理选择适合任务的推理级别以及快速或标准速度。

<a id="1-assess-complexity"></a>

## 1. 评估复杂度

范围有歧义时，陈述你的理解后开始探索，用户可以调整方向。

- **简单**（单个模块、小工具，或“函数 X 如何工作”之类的窄问题）：不设探索者。启动一个讲解者，一次完成探索与解释，使用 `references/explainer-prompt.md` 构建提示词，去掉探索者发现部分。转到第 4 步。
- **复杂**（跨多个文件或服务的子系统、横切功能、完整架构概览）：转到第 2 步。

拿不准时，走简单路径。

**其他智能体运行环境。** 本技能使用 Cursor 的 `Task` 工具启动子代理。其他环境使用各自的子代理工具：Claude Code 的 `Agent`（`subagent_type: general-purpose`）、OpenCode 的 `task`（`subagent_type: general`）、Codex 的 `spawn_agent`。保留提示词和模型，去掉工具没有的参数。如果运行环境没有子代理工具，例如未装扩展的 Pi，就由你逐个执行各角色。

<a id="2-explore-complex-only"></a>

## 2. 探索（仅复杂问题）

把问题拆成 2 至 4 个角度，每个对应子系统的独立切片。在一条消息中启动所有探索者，分别提供 `references/explorer-prompt.md` 并填入其角度。

<a id="3-synthesize-complex-only"></a>

## 3. 综合（仅复杂问题）

所有探索者返回后，启动一个讲解者，提供 `references/explainer-prompt.md`，填入全部探索者的发现。

<a id="4-present"></a>

## 4. 展示

展示讲解者的输出。可以为清晰度或对话背景作轻微编辑，不要大幅重写。

<a id="output-format"></a>

## 输出格式

说明采用 `references/explainer-prompt.md` 定义的章节，不适用的章节省略：概览、关键概念、工作原理、文件位置、注意事项。
