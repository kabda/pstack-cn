# 通用技能独立源译审校

初译者：translate_skills；审校者：主代理 root（非初译者）。固定源 commit：`9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`。

已分批逐段对照全部 49 个 Markdown。覆盖全部正文、标题、列表、表格、模板、代码围栏内的自然语言、注释以及 frontmatter。检查条件、例外、数值、模型选择与回退、并行和角色约束、人工批准、范围及停止条件；未以“有中文”替代审校。

## 修正并复核

1. 给少数英文操作手册与原则名补中文，并按叶子标题统一称谓。
2. 保留 reflect 的 Problem/Proposal/Routing 表头及 Principle/Evidence/Routing/Reason 输出字段，另解释中文；ASCII 字段分隔符保持原式。
3. 功能示例精确 H2 和 Preconditions: 不变，补驱动含义及种子内容解释。feature map 统一为“功能映射”。
4. no-comments 的参考与同源 agents/comment-sicko.md 统一，实际字节相同；固定开场和输出标记原样。
5. 保留技术写作的英语词法与语法正反例，补必要中文词义；精确区分长破折号和短破折号。
6. teach 的 moving parts 改为“相互作用的组成部分”，保留原文明确的英语输出要求，不借翻译变更设计。
7. 提示词配方中的自然语言已译，保留命令和占位符；必要的英文路由短语配中文解释。
8. poteto-help 的操作手册称谓按叶子标题统一，补 Agents Window、prove it works 等中文解释。

所有问题均已修复并复核，无未决项。逐文件覆盖及最终 SHA-256 见 REVIEW-skills.json；新编辑若使哈希变化，必须重新审校相应变化后更新记录。
