<a id="authoring-or-modifying-a-skill"></a>

### 编写或修改技能

**技能的表达风格由你负责。**

1. 使用技能编写技能。Cursor 中为内置 **create-skill**，其他环境用 Anthropic 的 `skill-creator`。两者都没有时，遵循 agentskills.io 的 Agent Skills 格式。
2. 验证技能。frontmatter 有 `name` 和 `description`，引用的文件存在，跨技能链接能解析。
3. 结构性内容要有测试用例。主观内容跳过。
4. 执行 **Opening a PR（创建 PR）**。

拿不准时就删除。只保留能改变决策的文字。告诉它做什么，省去理由。只有缺少理由就难以理解规则时才解释。语气与范围相配。按 **encode-lessons-in-structure** 原则技能，指向结构化来源，例如类型、README、配置。通过路径委派给其他技能，不要重述。经常遇到却尚未收录的工作流 → 提议新技能。

**回复：** 技能摘要、关键设计决策、验证说明。
