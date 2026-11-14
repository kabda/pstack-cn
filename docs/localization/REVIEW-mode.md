# poteto-mode 独立源译审校

固定基线：`9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`。初译者：translate_mode；独立审校者：translate_skills。覆盖全部 25 个非 scripts Markdown，包括主 SKILL、23 份操作手册和 Bugbot 参考。

已完成所有文件的全文逐段源译对照。审校者未参与这些文件初译，未修改译文，问题交由主代理修复。全部审校问题均由主代理修复，审校者已复核闭环并锁定最终译文 SHA-256，无未解决问题。

## 审校重点

- 逐段对照 must/should/may/never、条件、例外、否定、顺序、模型预算与回退、人工批准、hold/stop、完成与退出边界。
- 主 SKILL 的模型级别与速度、拒绝 slug 回退、并行角色和复用边界完整；自动化两手册的合并授权、patch-id 复用、实时验证与根层会签完整。
- Babysit 的四种模式、GitHub/Origin 各自停止状态、单次重试与冻结队列完整；Shipping 的连续验证段、自底向上合并、实时状态回读完整。
- multi-phase-plan 的不实现约束、明确 go、十条实时通道、主干缺功能时绝对预算、双侧性能、截图与30–60秒视频审查门禁完整。
- 独立阅读 check-plan.mjs 的只读解析路径后，复跑 `rtk proxy python3 docs/localization/check_plan_template.py`，在最终修复后再次得到 `1 PR sections, 0 problems`，退出码0；不运行模板工作流。

## 问题闭环

| 编号 | 文件/范围 | 问题与修复 | 状态 |
| --- | --- | --- | --- |
| MODE-01 | `skills/poteto-mode/SKILL.md` | 将 land a green stack 译成落地主干，增加了原文没有的合并目标。 去除“主干”，改为落地或交付全绿 PR 栈。 | 已修复并复核 |
| MODE-02 | `skills/poteto-mode/playbooks/autopilot-full.md` | 禁用或软失败的检查必须去掉，可能被理解成删除检查本身；且 every case 误成任何情况。 明确移除禁用检查或把失败降为软失败的改动，表述为无法守住所有情况。 | 已修复并复核 |
| MODE-03 | `skills/poteto-mode/playbooks/babysit.md` | “不加这些选项”可能使读者误以为 --pretty 与 --status-only 都终止轮询。 忠实表述为直接运行裸命令会轮询到终局。 | 已修复并复核 |
| MODE-04 | `skills/poteto-mode/playbooks/hillclimb.md` | TSV列名 hypothesis/change 被译成中文，而其他列名原样，可能改变生成格式。 完整保留 id/hypothesis/change/before/after/delta/tests/verdict/note，并逐项附中文。 | 已修复并复核 |
| MODE-05 | `skills/poteto-mode/references/bugbot-triage.md` | fix 条目中的 race 译“竞争”会与模型竞赛混淆。 改为“竞态”。 | 已修复并复核 |
| MODE-06 | `skills/poteto-mode/playbooks/multi-phase-plan.md` | 精确解析标题保留英文，但可补完整中文映射提升不懂英文读者的可读性。 模板前已增加受保护标题与字段的中文对照表。 | 已补充并复核 |
| MODE-07 | `skills/poteto-mode/` | 自然语言手册引用标题在部分正文只有英文，建议统一旁配中文。 主代理逐行分类，在代码、ID、HTML之外36行补主要标题中文解释；完整规范名称映射见主SKILL，英文身份名称保留。已逐项复核。 | 已修复并复核 |

## 逐文件覆盖

| 文件 | 对照范围 | 英文保留理由 |
| --- | --- | --- |
| `skills/poteto-mode/SKILL.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/authoring-a-skill.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/autonomous-run.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/autopilot-full.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/autopilot-stack.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/babysit.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/bug-fix.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/eval.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/feature.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/hillclimb.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 TSV列名及kept/reverted为格式和值。 |
| `skills/poteto-mode/playbooks/investigation.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/multi-phase-plan.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 check-plan.mjs 精确匹配的标题、块标签、验证规则、Lane/Save/Pass when 等保留并提供中文对照；独立复跑模板检查通过。 |
| `skills/poteto-mode/playbooks/opening-a-pr.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/orchestrate.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/pause-safely.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/perf-issue.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/prototype.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/refactoring.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/runtime-forensics.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/session-pickup.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/shipping.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/trace-forensics.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/visual-parity.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/playbooks/worktree-cleanup.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 |
| `skills/poteto-mode/references/bugbot-triage.md` | 标题、正文、步骤、示例、回复要求全文 | 技能名、ID、调用命令、路径、URL、工具参数、配置角色行、模型 slug、状态值和占位符保留，正文逐段译审。 英文历史评论是识别信号引文，附中文释义；candidate/recurring/strong/fix/dismiss/ask 为分类值。 |

最终逐文件源/目标 SHA-256 见同目录 REVIEW-mode.json。脚本、锁文件、可执行接口及测试产物不属于本译文审校范围，由总验收相同性与注释专审覆盖。
