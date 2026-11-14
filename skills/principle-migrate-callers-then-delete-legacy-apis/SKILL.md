---
name: principle-migrate-callers-then-delete-legacy-apis
description: "旧调用方仍存在时引入新内部 API 适用。在同一轮迁移调用方并删除旧 API，不保留兼容层。"
disable-model-invocation: true
---

<a id="migrate-callers-then-delete-legacy-apis"></a>

# 迁移调用方后删除旧 API

- 更新测试以断言新契约，并删除只保护重构前实现细节的测试

**适用条件：**
- 没有外部用户依赖向后兼容
- 项目能承受协调一致的破坏性变更
- 新 API 是简化或重构计划的一部分
