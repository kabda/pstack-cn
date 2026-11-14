# 英文残留与围栏专项复核

复核者：translate_docs；固定 commit：`9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`。范围：poteto-mode、principle-*、根文档、agents、docs/guide、docs/harness、automations/benny 和 skills/why。通用技能初译中的文件不据此宣称通过。本人初译的文档在这里仅作补充检查，正式独立源译审校由其他审校者负责。

## 自动队列逐项裁定

读取本轮 CHECK-RESULTS.json 后，已分配且完成的范围只有以下两项英文候选：

| 路径／定位 | 英文 | 裁定及理由 |
| --- | --- | --- |
| `agents/comment-sicko.md` 固定开场 | Yes... Ha ha ha... Yes! | 保留。源文明确要求第一条输出必须准确为此句，属于精确输出接口；后面已给中文释义。相同 blob 的 no-comments 参考副本也应保持一致。 |
| `skills/why/references/synthesizer-prompt.md` 的未搜索来源槽位 | `{SKIPPED_SOURCES_WITH_REASONS}` | 保留。模板占位符，不是未译正文；外围提示和标题已译。 |

其他通用技能队列中的 feature-map H2 应由对应初译／审校者根据生成技能的四标题契约裁定，不在本轮越权标为遗漏。英文语法正反例只有在英语语法本身是教学对象、并有中文说明时才应保留；不要把普通自然提示词归到此类。

## 补充围栏扫描与真实来源核对

自动英文扫描会去掉围栏，因此另逐行检查范围内全部围栏中不含中文、至少四个英文单词的行，并对多阶段模板及 check-plan.mjs 的相关精确匹配规则逐项核对。

- `MIRROR.md` 中 Git／rsync／grep 命令、URL、正则、同步标记和既有英文 commit message：原始维护命令，保持其复制含义。没有在本次实际执行这些命令；未来本次任务的提交消息使用中文，与源材料不混淆。
- README 和指南中的安装命令、slash command、命令命名空间：机器调用内容，保留。`automate-me` 等示例标签为技能 ID，保留。
- 自动化模板的 JSON、YAML 路由示例、`[benny:*] tracker=...`：字段、枚举、占位值及协议示例，保留；中文外围说明完整。配置中唯一可译显示标题已译为 Slack 报告。
- why 中 Git、SQL、工具名称、标识符、`SHOW TABLES`、错误查询中的符号名：机器调用／精确查询部分，保留；命令注释与调用说明已译。事故搜索英文短语和 Notion 章节名已按审校意见恢复英文并附中文。
- `multi-phase-plan.md` 的模板不是普通英文正文：check-plan.mjs 精确匹配 How to read this、Program checklist、Arm the program、Spawn owners、PR mechanics、Verdict and merge、Boot recipe、Close the program、Appendix、Prototype evidence；粗体子块 Depends on./Files./Build./You see./Verify, unit./Verify, live./Verify, perf./Review gate./Merge.；性能项目 Metric./Probe./Baseline./Rule.；Lane N.、Save、Pass when；以及完整 RULE 原句和 HOW_TO_READ_MARKERS 中的三项句段。保留这些英文是维持模板可被检查器解析，不能仅为中文化删除。相邻中文已经解释内容。
- 同一模板中的 `<...>` 原占位符按用户要求保留结构和内容，旁边有中文说明或对重复通道集中解释。Ten lanes on `<swarm workers model>` at the PR head 的结构也是检查器正则所需。screenshot、video、operator、status message 被检查器检索，已保留并附中文。

没有将整个代码围栏一概保留。自然语言任务提示、心跳提示、说明性 Mermaid 标签和可安全修改的说明注释均已翻译；机器模板则通过原文加完整中文解释兼顾精确匹配。

## 发现的补齐项

E1：README 示例和 `docs/guide/05-build-and-clean.md` 的 `/tdd implement` 中，implement 是自然语言请求，未发现必须原样匹配的代码或协议依据。虽然 doc5 已解释中文含义，按“复制给智能体的自然提示需要翻译”的严格要求，建议改为 `/tdd 实现`，并把 doc5 后面的释义改成正常衔接。主代理已将两处改为 `/tdd 实现`，并同步说明；docs 独立审校者已复核并锁定 REVIEW-docs.json。本专项重新读取当前两文件，确认 implement 提示已替换，问题关闭。

E1 已关闭；本轮未发现上述范围仍需补译的英文自然段。合法保留项仍须在最终逐项裁定队列中关联当前内容和具体理由，不能仅因文件含有中文就通过。


## 最终英语限定语补漏复核

E2：核对 wiki 新增语言说明时，进一步搜索固定源的 plain English，发现指南 02 和 10 的同一复述示例仅译成“通俗语言”，遗漏“英语”。主代理已改为“通俗英语”，原 docs 独立审校者负责复核两文件并更新哈希；同源 unslop 第14项例句的语言限定也由主代理修正为“直白英语”。本专项重新读取指南两处，确认英语限定已恢复；原 teach 和 prompting 的英语输出要求均忠实保留。该问题关闭，不改写原技能语言策略。
