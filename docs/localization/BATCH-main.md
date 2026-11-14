# 主代理初译批次

> 状态说明：本文件为初译阶段历史记录。下文“待独立审校”等措辞描述当时状态；当前全部译文已通过非初译者源译审校，未决项为零，最终哈希见对应 REVIEW 记录及 MANIFEST。

## 自动化资料

已逐段初译 automations/benny/ 下全部 11 个 Markdown：FOR_AGENTS、README、setup-benny、triage-issue-reports 及 routing.example、reproduce-and-fix-issues 及其 3 个参考、2 个自动化提示词模板。保留所有坐标、协议标记、变量、路径、配置字段、UI 选择器和状态标签，状态及 UI 标签旁补中文解释。YAML 配置无说明注释；独立审校指出 source_link_title 是可翻译的用户可见标题，经固定基线 git grep 确认无精确匹配依赖后已译为 Slack 报告，其他值原样保留。精确变更见 CONFIG-CHANGES.json。

## 代码注释分类

检查全部非测试脚本的行注释和块注释。共 4 个文件中的 16 个纯说明块已译，精确源译映射见 COMMENT-CHANGES.json；验证从固定 blob 仅应用这些替换，要求与目标字节完全相同。没有翻译 shebang、TypeScript 编译指令或测试语料。worktree-audit.sh 第 2–12 行虽为注释，却被 sed 直接用于 --help 输出，按接口保护。

## 当前验证

validate.py 已首次执行，检查结构、字节、JSON、Ruby/Psych YAML/frontmatter、SVG、围栏、占位符及差分引用。首次结果含尚未初译的文件，尚不代表最终验收；CHECK-RESULTS.json 会随复跑更新。尚待全部独立审校。

## 最终审校状态

本文件上方保留初译时的过程描述；本批现已完成非初译者的逐段独立审校，全部问题已修复复核。最终状态、审校人和目标哈希以对应 REVIEW 记录及 MANIFEST.json 为准，没有待翻译或未决审校项。
