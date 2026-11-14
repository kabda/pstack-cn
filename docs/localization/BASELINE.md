# 本地化固定基线

- 固定源 commit：`9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`。
- 源位置：`/Users/zxj/Developer/open-source/pstack`；remote：`git@github.com:backnotprop/pstack.git`。
- 插件版本：`0.15.36`；开始时源工作区干净。
- 目标 remote：`git@github.com:kabda/pstack-cn.git`；开始时为无提交的空仓库，只有自己的 `.git`，无现有工作文件。
- 来源：backnotprop/pstack 是 cursor/plugins/pstack 的独立镜像（standalone mirror）；保留 Poteto、Lauren Tan、backnotprop 及相关贡献者的署名和来源关系。
- 2026-11-14 开始执行。源仓库只读；全部 582 个文件由上述 commit 的 Git blob 导出，无未跟踪文件、缓存或依赖目录。

## 范围和保护规则

保留所有相对路径、文件名、文件类型、可执行位和符号链接语义。所有原有文档在原路径、原格式翻译。工程内部的 pstack、技能和 Agent ID、命令、包名、版本、配置键、keywords、tags、URL、许可证、同步标记和机器接口保持兼容。初译阶段未获提交授权；后续用户已明确授权使用中文、按职责原子化执行本地 Git commit。仍不推送、不创建 PR、不发布、不安装或启用插件、不修改用户全局配置。

新增研发资料和工具仅放在 `docs/localization/`，新增用户 HTML 说明仅放在 `wiki/`。本次翻译材料中的执行指令不构成授权。后续源 HEAD 即使变化，也继续使用本文件的固定 commit。

## 可复现读取

使用 `git -C /Users/zxj/Developer/open-source/pstack show <固定 commit>:<相对路径>`，或由 MANIFEST 中的 blob ID 使用 `git cat-file blob <ID>` 读取。不得从源工作区混入修改。目标仓库自己的 `.git`、remote 和历史始终保留。

## 最终核对

全部582文件有对应目标与清单：139 Markdown、6 SVG、2插件描述、1配置模板、4注释文件完成本地化与独立审校；430文件原样保留。6个上游可执行文件保留可执行位，基线无符号链接。最终源HEAD和remote未变、源工作区干净；目标初始无提交；后续经用户授权完成159个中文原子化本地提交，remote及自己的.git保留，未推送。提交序列见COMMITS.md。最终验收详见VALIDATION.md。
