# 主代理批次独立源译对照审校

审校者：translate_docs；初译者：主代理。审校者未参与本批初译，也未直接修改本批译文。固定源 commit：`9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`。审校日期：2026-11-14。

## 覆盖范围与方法

全部逐段阅读、对照固定 Git 对象与目标文件：`automations/` 的 11 份 Markdown、`skills/why/` 的 13 份 Markdown，共 24 份；另审查配置 YAML 和 4 个代码文件内的 16 个注释块。未以“包含中文”或仅检查标题、description 代替全文审校。

重点核对条件和否定、必须／应当／可以的力度、步骤先后、用户批准、停止条件、任务委派、Slack 写权限和凭据隔离、根消息与线程回复边界、已有修复的只验证模式、两次独立 UI 复现、预算、证据、回退补偿、置信等级和跨来源调查边界。模板内自然语言已翻译，机器字段、占位符、协议标签、调用名称和数值保留。

## 问题与关闭记录

| 编号 | 路径／定位 | 审校发现 | 处理与复核 |
| --- | --- | --- | --- |
| M1 | `automations/benny/templates/configuration.example.yaml` 的 `tracker.source_link_title` | `Slack report` 是用户可见链接标题，不能仅因位于 YAML 就全部原样保留。 | 主代理核查固定基线的使用位置后译为 `Slack 报告`，并用 `CONFIG-CHANGES.json` 单独记录。已独立将这一项还原，确认其余全部字节与源对象一致，关闭。 |
| M2 | `automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md` 的精确 UI 标签 | Continue、Email、Password、Save、Item editor、Profile 已正确保留，但缺少中文解释。 | 主代理在首次出现处补“继续／电子邮件／密码／保存／条目编辑器／个人资料”，动作和选择器串保持原样；已复读检查，关闭。 |
| M3 | `skills/why/references/sources/incident-postmortem.md` 的 Git 检索线索 | 只译中文可能让英文历史检索词失效。 | 主代理保留 `fix for incident`、`add defensive check`、`revert`、`re-apply with...` 并配中文；已复核四项原词，关闭。 |
| M4 | `skills/why/references/sources/notion.md` 的文档章节线索 | Problem statement、Motivation、Alternatives considered、Rejected approaches、Why 应保留以对应英文来源章节。 | 主代理改为中英并列；已逐项复核，关闭。 |
| M5 | `skills/why/references/epistemics.md` 的保留措辞建议 | 将 the evidence suggests 译为“证据表明”，肯定程度略强。 | 主代理改为“证据提示”，已复核，关闭。 |
| M6 | `skills/why/references/sources/databricks.md` 的“公司专属表”条目 | “从从未确认存在的表中报告结果”读起来有歧义。 | 主代理已改为“使用未经确认存在的表报告结果”，已重新读取并确认，关闭。 |

除上表外，未发现遗漏的自然语言段落、被弱化／强化的权限或停止边界、数值错误、机器身份变化，或需重译的英文说明段落。

## 逐文件覆盖

以下 SHA-256 指向审校时的目标内容；全部审校问题已经关闭。所有源对象由固定 commit 和 MANIFEST 对应。

| 文件 | 审校结论 | 目标 SHA-256 |
| --- | --- | --- |
| `automations/benny/FOR_AGENTS.md` | 逐段对照通过；保留项已裁定 | `f958ec535efb482919f0c82bab43c44b293c702807911830eec618c67c88519d` |
| `automations/benny/README.md` | 逐段对照通过；保留项已裁定 | `edfcd0c170393fdc95ee9262dcd2b77a2d1abd904709f0ee5b0ee6178bbdbe37` |
| `automations/benny/skills/reproduce-and-fix-issues/SKILL.md` | 逐段对照通过；保留项已裁定 | `e068fe96c1f61027b367d792a29feede66532a04fba010ea20fdb95872eb38f9` |
| `automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md` | 逐段对照通过；保留项已裁定 | `b2864183e10ec60c7761d8b4af07cee29b96d0634a1d51f6ae7572626d95b56c` |
| `automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md` | 逐段对照通过；保留项已裁定 | `88dff468af02ff26837cf911bc40c032f20517c7e30deb303dc9c09bf625588a` |
| `automations/benny/skills/reproduce-and-fix-issues/references/verify-existing-fix.md` | 逐段对照通过；保留项已裁定 | `eab072f07a1072de961995ae316e6f73e5d4a6acf42cb61827ca3d67e31b94db` |
| `automations/benny/skills/setup-benny/SKILL.md` | 逐段对照通过；保留项已裁定 | `5a4976e677f51f28fa23b6c64772d8e7e611d31d50b1eca2c0048659bd7c241a` |
| `automations/benny/skills/triage-issue-reports/SKILL.md` | 逐段对照通过；保留项已裁定 | `c8b01700d25a09acc46a68db5d4c50f16a0ad641baadca24d0463c4f36d406a0` |
| `automations/benny/skills/triage-issue-reports/references/routing.example.md` | 逐段对照通过；保留项已裁定 | `ecb0aa8794b87eb815e77bb7bfda367ad75fef73f53f6b6ea08a388513a3d5fb` |
| `automations/benny/templates/reproduce-automation-prompt.md` | 逐段对照通过；保留项已裁定 | `5a094e7157714bdf3280131ff2723ec0c9db9cc09da28025f04824823092f17d` |
| `automations/benny/templates/triage-automation-prompt.md` | 逐段对照通过；保留项已裁定 | `b55fc5d5db866beaab0ae0800ff37c350f186c6b5b7f7631fe890fa121399a95` |
| `skills/why/SKILL.md` | 逐段对照通过；保留项已裁定 | `589ea5774faf28acebeef68ffa90b38596292d92a79b361a2f9ed08cfaaad752` |
| `skills/why/references/epistemics.md` | 逐段对照通过；保留项已裁定 | `3277883691a420d461664fa910b62dd815bb1d46cd42ba73c708a2566c5f44ec` |
| `skills/why/references/investigator-prompt.md` | 逐段对照通过；保留项已裁定 | `608549b7597ab6ef491d0d386404e023eac1fab02fa878a50e3766ce662f0a5a` |
| `skills/why/references/source-playbook.md` | 逐段对照通过；保留项已裁定 | `8b735fd9ba8062e8a9e2eea5020b7c751bcde1be170de192bbc860604cf36a31` |
| `skills/why/references/sources/code-archaeology.md` | 逐段对照通过；保留项已裁定 | `5c3e302ae515a58fa6249d9bc6082ebf0d977bd671948ecdf65559209fdd99f7` |
| `skills/why/references/sources/databricks.md` | 逐段对照通过；M6 已修复复核 | `ee7c905303c74110e1575bd7045ca50620e748d36ecfc7b919d02b876f367377` |
| `skills/why/references/sources/datadog.md` | 逐段对照通过；保留项已裁定 | `474ef2ee97bc1bae464d28223095b8a16fd774c5687fd5492d5bdc54acac2ad2` |
| `skills/why/references/sources/incident-postmortem.md` | 逐段对照通过；保留项已裁定 | `973159713e1954c21d2d135ee3657b5ddf7fc5cd3b571988d46090ae15fa1ca4` |
| `skills/why/references/sources/linear.md` | 逐段对照通过；保留项已裁定 | `6d1df452a198b54bbc552467e1eb77b9b13016a36ed8b064dcd25575be61eedf` |
| `skills/why/references/sources/notion.md` | 逐段对照通过；保留项已裁定 | `a3e1e06d76e7ee224e7adf9f5bdecdc1fff2f5a85d501576a9c4a7ea4dda93db` |
| `skills/why/references/sources/sentry.md` | 逐段对照通过；保留项已裁定 | `ea22007ad221e76ada22c319341a4a9de58ac984dcc03b2b36d9e7ffef5be3fc` |
| `skills/why/references/sources/slack.md` | 逐段对照通过；保留项已裁定 | `ffe57180ea6f701a2de824687231f4c96d39d865f94a576946f2c4a9cccab9c2` |
| `skills/why/references/synthesizer-prompt.md` | 逐段对照通过；保留项已裁定 | `70852eede4ced896d4c900bd4ea6a90f96126aa0cd15688685f59ab00cbaacf5` |
| `automations/benny/templates/configuration.example.yaml` | 单一显示标题获准翻译，其余字节一致 | `3b2772a34a7d2aee1306aae9bb0a464f8bedcf584c9ffc6b6e49e235d1bb0b92` |
| `skills/poteto-mode/scripts/watch-pr/github.ts` | 全部获准注释块对照通过；还原后与固定源字节一致 | `92d610e313613d9c273d1ec41b4b1c084722bfda5882fb2ae41c15241ca69bc0` |
| `skills/poteto-mode/scripts/watch-pr/types.ts` | 全部获准注释块对照通过；还原后与固定源字节一致 | `3411c34838276e59bbce1b78ce3aec6aa09edf6d5de467b26168cc5f71f7253e` |
| `skills/poteto-mode/scripts/worktree-audit.sh` | 全部获准注释块对照通过；还原后与固定源字节一致 | `1ad7f8c31a18ff2700be00a1e807d9824bcc60e11c44c16140b0d132ac9bec91` |
| `skills/show-me-your-work/scripts/log.sh` | 全部获准注释块对照通过；还原后与固定源字节一致 | `fa053acbd2b20892932bceccfac95eb88fd98d5dd9550cca7782340f7c7b1203` |

## 英文保留项裁定

- `name`、布尔值、模型 slug、角色行名、工具／MCP 名称、API、SQL、Git 命令、正则、代码标识符、路径、URL、工单和 PR 编号、时间戳字段、数值和预算：接口或精确匹配内容，保留。
- `[benny:bug]`、`[benny:performance]`、`[benny:other]`、`tracker=<URL>`、`SOURCE_THREAD_TS` 等：线程协议及机器字段，保留。
- `Could not reproduce`、`Blocked`、`Attempting bounded fix` 等状态串，`Direct`、`Supported`、`Inferred` 等置信标签：保持输出与角色匹配，已配中文解释。
- `<...>`、`{...}`、`{{...}}` 内原有占位符：模板结构和含义受保护，保持原样，外围要求已经翻译。
- UI 英文标签、文档标题线索、事故检索词、Linear 标签：按精确选择器或检索／分类意义保留，中文解释补全。
- Cursor、Slack、Benny、GitHub、Linear、Notion、Databricks、Datadog、Sentry、Seer 等品牌、产品、标准及专名保留。
- YAML 其余字符串为用户须替换的配置占位值、环境变量名、协议、标签或枚举；只有链接标题属于可译显示文字，已在 M1 修复。
- 16 个普通说明性代码注释块获准翻译；按记录逐项还原后，4 个文件与源对象逐字节一致。shell 脚本 shebang、用于 `sed` 提取 `--help` 的顶部注释、运行输出接口、代码逻辑及测试均保持不变。

## 验证证据与限制

独立执行的还原核对：读取 `COMMENT-CHANGES.json`，要求每个 target 片段在所属文件中唯一，逐项替换回 source 后，与 `git show <固定 commit>:<path>` 完全相同；4 文件全部通过。配置同样将 `Slack 报告` 还原为 `Slack report` 后，整份 YAML 与固定源相同。已查看 worktree-audit.sh 的帮助提取边界，翻译块都在该边界之外。

这是静态和语义审校，不是自动化、Slack、数据库查询、模型调度、实际应用或真实服务运行验证。没有启动自动化、发送消息、安装环境、更新快照或写入外部系统；这些均非本次翻译授权。基线材料对宿主、插件、MCP 和外部服务的依赖仍为基线事实。
