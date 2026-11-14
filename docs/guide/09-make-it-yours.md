<a id="make-it-yours"></a>

# 按需定制

poteto-mode 是一个人的风格，但底层操作手册、路由和模型角色，同样适用于你的风格。本页涵盖生成个人模式、提炼会话教训、修正仓库以防智能体重复犯错、编写聚焦的技能，以及在信任技能改动前测试它。

从比你想象中更小的规模开始。第一天不需要很多技能，甚至不需要整个插件。直接说明要求，观察智能体在哪些地方失败；同一失败出现两次后，再增加技能或检查。

<a id="generate-your-own-mode-with-automate-me"></a>

## 用 `/automate-me` 生成个人模式

```text
/automate-me
```

不需要描述自己的风格，因为 [`/automate-me`](../../skills/automate-me/SKILL.md) 会从历史中读出它。它检索当前工作区的近期对话记录，寻找你对回复、委派、验证、代码、文字和流程的反复偏好，再询问哪些模式确实代表你。它通过 Cursor 内置 `create-skill` 流程起草 `.cursor/skills/<your-name>-mode/SKILL.md`，用 [`/unslop`](../../skills/unslop/SKILL.md) 清理草稿，并从工作树创建 PR，供你像其他改动一样审查。

习惯变化后可再次运行：

```text
/automate-me 用上次编辑以来的所有内容更新我的模式技能
```

更新模式只检索技能上次变更后的历史。它保留你没有否定过的规则，依据新证据修订相关规则，只有出现新模式时才增加章节。

<a id="capture-a-sessions-lessons-with-reflect"></a>

## 用 `/reflect` 提炼会话教训

刚完成一项让你有所收获的任务时，运行：

```text
/reflect 这花的时间太长了。记录我们学到的东西，避免下次重蹈覆辙。
```

[`/reflect`](../../skills/reflect/SKILL.md)把对话记录交给三个并行审查者，再由综合者将提案分为 `Accepted`（接受）、`Rejected`（拒绝）和 `Backlog`（待办），在任何技能改动前等待你的批准。只有能改变未来决策的提案才值得批准。一次古怪会话只是个例，不是规则。

<a id="fix-the-environment-with-correct"></a>

## 用 `/correct` 修正环境

当你反复纠正智能体同一个错误时，修复应落在仓库中，而不是下一条提示词里。按约束强度排列选项：

1. 通过架构或更好的数据结构，让错误不可能发生。
2. 用类型，或能在错误消息中指出修复方式的 lint、CI 检查阻止它。
3. 用测试抓到它。
4. 写成文档或智能体规则。智能体跳过规则时，没有任何东西会失败，所以它排最后。

人工审查不在清单中。审查者必须在每个 PR 中抓同样错误，正是这里要解决的问题。[`/correct`](../../skills/correct/SKILL.md)会执行这项工作：

```text
/correct 智能体总是直接调用数据库客户端，而不是经过 repository 层
```

它阅读近期提交、回退、审查评论和解释变通方案的注释，再将错误分组。某类错误发生两次后才算一个类别。它处理最频繁的类别，每类一个提交，采用有效的最高层级，并证明每项新检查都能在真实历史错误上失败。它还在智能体指令文件中维护一张表，将每条规则与强制执行机制配对，让没有约束机制的规则显露为重复问题。回复按类别列出证据、所选层级，以及更高层级为何不适用。

不带参数运行时，它会自行从历史中找出类别。`/reflect` 与 `/correct` 分工不同：`/reflect` 根据一次会话改进技能，`/correct` 改变仓库，让一类错误无法复发。如果修复涉及新边界，可配合 `/architect`。[并行运行多个项目](./07-overnight.md#run-many-projects-in-parallel)提供了在整个仓库中同时使用两者的提示词。

<a id="author-a-focused-skill"></a>

## 编写聚焦的技能

当你已经知道想固化的工作流时：

```text
/poteto-mode 编写一项技能，用于验证这个仓库的数据库迁移
```

编写技能会匹配[编写或修改技能操作手册](../../skills/poteto-mode/playbooks/authoring-a-skill.md)，通过 Cursor 内置 `create-skill`，验证 frontmatter 和链接，再通过创建 PR 操作手册交付。面向智能体的文字标准高于面向人的文字，因为一句无用的话会变成未来某个智能体遵循的指令。应让操作手册守住标准，而不是徒手写 `SKILL.md`。

两种特殊情况各有生成器。必须操作应用并证明行为的技能属于应用验证技能，应改用 [`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md) 和 [`/maintain-verification-skill`](../../skills/maintain-verification-skill/SKILL.md)。使用模型检查器、证明或其他验证器检查代码性质的技能属于形式化验证技能，应使用 [`/create-formal-verification-skill`](../../skills/create-formal-verification-skill/SKILL.md) 和 [`/maintain-formal-verification-skill`](../../skills/maintain-formal-verification-skill/SKILL.md)。[验证并交付](./06-verify-and-ship.md#prove-a-property-with-a-formal-verification-skill)介绍了这两类。

<a id="write-docs-to-a-standard-with-technical-writing"></a>

## 用 `/technical-writing` 按标准写文档

技能不是你唯一要交付的文字。对于文档、RFC、README、PR 描述和提交消息：

```text
/technical-writing 审查 readme 中的改动
```

[`/technical-writing`](../../skills/technical-writing/SKILL.md)应用分层标准，目标是让疲惫的工程师也能一遍读懂。它先选择文档模式（教程、操作指南、参考或解释），再逐句处理：谁做什么、每句一个想法、没有歧义。可以用它审查你或智能体刚写的内容，也可以在要求写文档时预先指定。

<a id="test-a-skill-change-blind"></a>

## 盲测技能改动

技能编辑会影响未来每次会话，因此要把它当作实验测试。采用他人的技能也一样。在保留之前，先确认它确实让智能体在你的工作上表现更好。

```text
/poteto-mode 对这项技能改动运行评估（eval）操作手册。两个变体使用同一任务，候选方保持盲测。
```

如果技能反复失误，而你知道它应如何表现，可在一个任务里同时修改和测试：

```text
/poteto-mode 更新审查技能，让它标记缺失的迁移，并评估改动。
```

事先要求评估能约束编辑。根据一次糟糕会话写出的修复容易过拟合，多次编辑后技能会漂移。评估会在交付前抓到漂移。

[评估操作手册](../../skills/poteto-mode/playbooks/eval.md)围绕一种失败模式构建：观察者效应。知道自己正在接受评估的智能体，行为会不同。因此，候选智能体在经过清理隔离的目录中收到看似自然的任务，绝不会看到“eval”或“candidate”，也不会知道彼此存在。一个裁判以中性标签给所有输出评分；指令链遵循情况依据各候选方实际读过哪些文件评定，而不是听它们声称。

接受结论前，亲自阅读每份输出。如果与裁判意见不同，先怀疑评分标准，再怀疑自己的判断。

<a id="build-a-bot-ui-with-make-bot-ui"></a>

## 用 `/make-bot-ui` 构建机器人界面

有一项情境性技能面向 Grok Bot 用户。[`/make-bot-ui`](../../skills/make-bot-ui/SKILL.md)构建一个小页面，按钮通过 webhook 例程唤醒机器人。例如，你可以滑动浏览审查队列，让每次滑动都要求机器人处理该条目。本机服务器持有 webhook 的发送方密钥，因此密钥绝不会到达浏览器或聊天。技能也涵盖通过 Tailscale 暴露页面。

**陷阱：** 不要因为技能表现不佳就在任务中途编辑它。在独立 PR 中修复，保持当前任务推进。技能编辑若与功能工作纠缠交付，审查时难以察觉，也无法评估。

下一页：[实用配方与常见陷阱](./10-recipes-and-pitfalls.md)。
