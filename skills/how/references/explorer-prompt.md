<a id="explorer-prompt-template"></a>

# 探索者提示词模板

使用此模板构建每个探索子代理的提示词，并填入占位符。

---

其他探索者正在并行调查同一子系统的不同切片。不要试图覆盖一切，聚焦分配给你的角度，深入探索。

<a id="question"></a>

## 问题

> {QUESTION}

<a id="your-exploration-angle"></a>

## 你的探索角度

{EXPLORATION_ANGLE}

<a id="output"></a>

## 输出

<a id="components-found"></a>

### 发现的组件

关键类型、服务、类和抽象。每项包含名称、文件路径，以及一句话职责说明。

<a id="flow"></a>

### 流程

逐步说明执行流程。每一步包含：运行的函数或方法、所在文件、所做工作、下一调用。包括步骤之间流动的数据。

<a id="files-read"></a>

### 已读文件

列出探索中读过的每个文件，以便讲解者引用。

<a id="boundaries"></a>

### 边界

子系统与代码库其他部分的连接位置，输入与输出。

<a id="non-obvious-things"></a>

### 不明显的事项

任何出人意料、有历史动机或容易出错的内容，以及看似应当以某种方式工作、实际上却不同的事项。

<a id="open-questions"></a>

### 待解问题

无法完全追踪或理解的内容。如实说明缺口。
