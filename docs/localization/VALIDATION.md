# 本地化验收记录

固定源 commit：`9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`；插件版本 `0.15.36`。验收日期：2026-11-14。

## 范围与实际结果

| 项目 | 实际检查与结果 |
| --- | --- |
| 完整清点 | Git 树全部 582 文件有目标及 MANIFEST 记录，包含隐藏 .cursor-plugin/plugin.json。无删除、改名、迁移或类型变化，可执行位保持。 |
| 分类 | 139 个 Markdown、6 个 SVG、2 个插件 description、1 个配置模板、4 个代码说明注释文件涉及本地化，共 152 文件；422 机器文件、7 位图、1 LICENSE 共 430 文件原字节保留。 |
| 机器兼容 | JSON 插件身份及全部非 description 字段相同；YAML 仅来源链接显示标题变化；4 个代码文件仅16块白名单注释变化，其余字节相同。 |
| 格式 | 全部 JSON 解析；Ruby/Psych 解析 YAML/frontmatter 并核对机器字段；Bun.markdown 解析所有基线及新增 Markdown；HTML 标签、SVG XML/属性/ID/节点关系、围栏及占位符检查通过。 |
| 引用 | Markdown、HTML 的文件/图片/href/src/srcset 及 SVG href/锚点差分检查通过，无本次新增失效引用；基线示例链接单独记录。 |
| 内容与英文 | 全部翻译文件由非初译者逐段源译对照；7 个英文候选、31 个行内变化、122 个围栏变化逐项裁定；数字短缺为0。详见 RETAINED.md 与 LITERAL-REVIEW.json。 |
| 字面量 | validate.py 每次实际重算30项混合片段机器部分比较；独立审校者另从 Git 对象复算30/30一致。 |
| 计划模板 | check_plan_template.py 抽取中文模板并填示例值，原检查器实际输出1 PR sections、27 boxes、10 live lanes、0 problems，退出0。未执行模板中的工作流。 |
| 必要离线测试 | 实际运行 check-plan.test.ts：7 pass、0 fail、25断言。未修改断言或预期。 |
| 代码语法 | 两个修改注释的 Bash 脚本 bash -n 退出0；两个 TypeScript 文件由 Bun 转译，语法通过且生成 JavaScript 与源对象相同。此项不等于真实工作流运行。 |
| 可视检查 | wiki 在本地 Chromium 的1280桌面、375窄屏及深浅色检查，无横向溢出、6图加载、5导航锚点可用；六SVG实际Chromium渲染文字无溢出。原7位图逐一查看并提供完整中文解读。 |
| 工作区边界 | 源最终HEAD仍为固定SHA，工作区干净、remote未变；目标初译验收时无提交，remote保留kabda/pstack-cn；用户后续授权原子化中文本地commit。新增文件只在docs/localization/与wiki/，未安装或启用插件、未改全局配置、未push/PR/发布。提交分批记录见COMMITS.md。 |

## 可复跑命令

在目标项目根目录运行，均不安装依赖、访问真实服务或更新快照：

```bash
rtk proxy python3 docs/localization/validate.py --final
rtk proxy python3 docs/localization/check_plan_template.py
rtk proxy bun test skills/poteto-mode/scripts/check-plan.test.ts
```

validate.py 会输出 CHECK-RESULTS.json 和重新计算的 LITERAL-PROOFS.json。最终模式还要求清单完成状态、目标哈希、明确基线、非初译者通过状态、未决问题为零，以及全部字面量裁定匹配。新增修改会使相应门禁失败，必须实际审校后更新记录。

## 独立审校与修复

- 文档/Agent/插件/SVG：translate_mode 审校 translate_docs 初译，25文件；另核对7位图。
- 自动化/why/配置/代码注释：translate_docs 审校 root 初译，29文件、16注释块。
- 通用技能：root 审校 translate_skills 初译，49文件。
- poteto-mode：translate_skills 审校 translate_mode 初译，25文件。
- 原则技能：translate_docs 审校 translate_mode 初译，24文件。
- wiki：translate_docs 独立内容与可视检查；静态工具亦经独立防漏审计。

验证工具另经独立只读重放与7个纯内存负例检查：未通过审校、错误目标哈希、错误审校基线、未决项、非独立审校、错误字面量基线、围栏裁定哈希漂移，均正确拒绝并退出1。实际证据见 REVIEW-validator-probes.json；最终审计V1–V5均已关闭。

具体文件和最终 SHA-256 在各 REVIEW-*.json。所有已发现问题均修复复核，包括人工边界、禁用门禁的改动、日志列名、竞态/性能退化/权威对象术语、数值限定、英语输出限定、自然提示词漏译、标签解释和原则名称一致性。

## 基线情况与验证限制

1. why/references/synthesizer-prompt.md 的 `[PR #123](url)` 是源模板的示例占位链接。静态检查按本地链接报告为缺失，源译均如此；不擅自创建url文件或改写原例。
2. 源README提到cursor/plugins父仓库的harness/pstack与scripts/generate-pstack-harness-trees.mjs，独立镜像没有这些父仓库资源。控制技能、Cursor专有功能、外部MCP和自动化服务也依赖宿主环境。未补造上游文件，未宣称在本机运行通过。
3. architect/references/rationale-template.md 的最后一节原文称Phase D sign-off，而主技能可选检查点在Phase C。这是固定基线的交叉表述，忠实翻译并保留，没有借本地化修设计。
4. 未运行整套watch-pr/statechart服务相关测试、TLC/Java模型检查或插件安装验收。相关机器代码、测试与预期结果完全相同，以字节核对为主要证据；未将未运行或静态验证表述为运行通过。
5. 外部URL保持来源语义，未联网验证链接当前可达性；本次引用门禁核验本地路径与锚点，无新增本地失效引用。
6. 早期Quick Look/AppKit存在裁切/配色渲染限制，最终已用Chromium重新渲染并逐图检查；最终图像证据采用浏览器结果，详见IMAGE-NOTES.md。

没有待翻译、占位译文或未决审校问题。源模板本来就有的占位符属于受保护接口，不是待完成译文。

## 用户授权后的原子化本地提交

用户在初译验收后授权中文本地Git提交。已按技能职责、工具组件、指南主题和33个完整测试案例拆成159次提交，MANIFEST条目随对应文件进入历史，避免单次导入巨型清单。仅两个上游完整测试文件的独立批次超过千行；未拆散文件，未改写预期。全部提交均核对暂存路径、对象哈希和权限，并复核提交后的Git对象。

提交阶段重新运行最终静态验收：错误0、新增失效引用0、原有引用问题1，194份Markdown解析通过。已验收译文、机器内容和预期未因提交变化；最终634文件全部进入提交树，目标工作区干净。源HEAD和remote未变且工作区干净，目标remote保留；未推送、创建PR或发布。完整序列见COMMITS.md。
