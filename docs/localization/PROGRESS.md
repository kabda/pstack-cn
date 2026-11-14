# 本地化进度

## 当前状态

固定基线 `9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`，插件 `0.15.36`。全部582文件已覆盖：152文件完成本地化与独立审校，430文件原样核验通过。源项目只读、目标remote与Git历史保留。初译交付已完成。用户随后授权使用中文、按职责拆分本地Git提交，已完成159个原子化提交；目标工作区干净，未推送、创建PR或发布。提交记录见COMMITS.md。

## 已完成批次

- 文档/Agent/插件/SVG：25文件，translate_docs初译、translate_mode独立审校；7原始位图及中文解读一并检查。
- poteto-mode：25 Markdown，translate_mode初译、translate_skills独立审校。
- 原则：24 Markdown，translate_mode初译、translate_docs独立审校。
- 通用技能：49 Markdown，translate_skills初译、root独立审校。
- 自动化/why：24 Markdown与1配置模板，以及4代码文件16说明注释块，root初译、translate_docs独立审校。
- wiki中文HTML入口、图像解读、术语表、全部清单、审校及验收工具完成。

## 最终检查

结构、身份、原样字节、格式、引用、占位符和数字检查通过。英文及混合片段逐项裁定。必要的7项离线测试、模板实际检查和可视检查通过；未运行项目全套外部环境测试，明确记录于VALIDATION.md。所有审校问题修复且复核，最终文件SHA-256锁定，无未决项。

## 后续维护与恢复

本任务没有剩余翻译工作。检查资料依次为BASELINE、GLOSSARY、MANIFEST、VALIDATION及各REVIEW记录。后续编辑仍使用本固定基线，除非用户明确授权更换；不要自动跟随源HEAD，不要将源未提交内容混入。validate.py --final可重复核验当前交付；新增翻译变更必须重新独立审校并更新目标哈希，不能以重新生成预期或自动接受裁定来通过。
