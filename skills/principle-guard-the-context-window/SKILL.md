---
name: principle-guard-the-context-window
description: "上下文逐渐填满时适用，包括大量输出、长文件、反复读取、并行分发规划。批量材料交给子代理；主对话保留摘要，不放原始载荷。"
disable-model-invocation: true
---

<a id="guard-the-context-window"></a>

# 保护上下文窗口

**原因：** 上下文溢出降低推理质量，带来压缩失真，并阻停进展。

**做法：**
- **控制阶段大小并限定范围。** 限制每阶段文件数，设置轮次预算，计入机制成本。
