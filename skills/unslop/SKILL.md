---
name: unslop
description: 去除任何文字中暴露 AI 写作痕迹的表达。
disable-model-invocation: true
---

<a id="unslop"></a>

# 去除 AI 腔

编辑文字，移除 AI 写作模式。扫描下列模式再重写，保留含义，匹配预期语气。

<a id="patterns-to-detect-and-fix"></a>

## 需要识别并修正的模式

规则编号是其他技能引用的稳定 ID。删除规则后保留编号空缺。下面的英文词句用于精确说明英文写作模式。

<a id="content"></a>

### 内容

3. **空泛的 -ing 短语。** 例如 "highlighting..."（突显）、"ensuring..."（确保）、"reflecting..."（体现）、"showcasing..."（展示）、"fostering..."（促进）。删除，或用真实来源充实。
5. **含糊归因。** 例如“专家认为”“行业报告表明”“一些批评者主张”。明确指出来源，否则删除。

<a id="language"></a>

### 语言

7. **AI 常用词。** Additionally、crucial、delve、enduring、enhance、fostering、garner、interplay、intricate、landscape（抽象用法）、pivotal、showcase、tapestry（抽象用法）、testament、underscore、vibrant。改用平实词语。
8. **花哨地表达“是”。** 如 "serves as"、"stands as"、"boasts"、"features"。直接说 "is"（是）或 "has"（有）。
9. **“不仅是 X，更是 Y”。** 改为直接陈述观点。
10. **强凑三项。** 不要强行把观点归成三组，按内容自然数量组织。
11. **轮换同义词。** 同一段中把主角交替写成 protagonist、main character、central figure、hero。选一个，重复使用。
12. **虚假范围。** X 与 Y 不在有意义的尺度上，却写“从 X 到 Y”。直接列出主题。

<a id="style"></a>

### 风格

13. **过度使用长破折号。** 完全避免长破折号（em dash）。只用句号或逗号，不用括号、短破折号（en dash），也不用连字符冒充破折号。需要分隔意思时，结束句子或用逗号。
14. **过度使用冒号。** 列表或示例前可用冒号，不要把它当句中连接符。“如果你来自传统自动化：你不再注册事件处理器，而是描述条件”里的冒号毫无帮助。重写成独立成立的观点，不用对比式框架：“用直白英语描述调度器何时应触发，效果最好。”含义相同，无需依赖标点。
15. **过度加粗。** 不要把每个专名或缩略词都加粗。
16. **行内标题列表。** 暴露痕迹的是加粗标签加冒号，而且重复后文：“**性能：**性能得到提升……”。改为正文。如果加粗引导语以句号结束、点明项目，后接真正的新细节，例如“**TypeScript 中的 schema。**表集中在一个文件里。”，则没有问题。
17. **标题式大写。** 英文标题采用句首大写。
18. **装饰性 emoji。** 从标题与列表项中移除。
19. **弯引号。** 使用直引号。

<a id="communication-artifacts"></a>

### 聊天式残留

20. **聊天机器人套话。** 如“希望这有帮助！”“如果……请告诉我”“当然！”“没问题！”“找到铁证了！”。删除。
22. **迎合语气。** “好问题！你完全正确！”直接回应。

<a id="filler"></a>

### 冗余

23. **填充短语。** "In order to" 改为 "To"，"Due to the fact that" 改为 "Because"，删除 "It is important to note that"。中文分别直接写目的、原因，省去“值得注意的是”。
24. **过度保留语气。** "could potentially possibly be argued that it might" 改为 "may"，不要堆叠“可能、潜在、也许”。
25. **空泛结论。** “未来一片光明。”改为具体计划或事实。

<a id="jargon"></a>

### 行话

26. **抽象隐喻名词。** substrate（改为 base，基础）、wedge、wedge in（改为 add，添加）、vector（改为 way、method，方式或方法）、locus、vantage、nexus、用作名词的 primitive、隐喻性 harness、"API surface" 中的 surface、bedrock、隐喻性 scaffolding、modality、paradigm、gold-plating（超出任务需要）、隐喻性 ratchet（使用机制真实名称，或写“只能收紧的限制”）、用 evacuate 表示移动代码（改为 move out）、endgame（改为最后阶段）、north star、flywheel。这些词看似技术性强，通常却有更平实具体的词可用。选择具体词。

<a id="plain-speech"></a>

### 直白表达

27. **说清它做什么，而非感觉如何。** “数据库近在手边”“读得懂的 SQL”“跟随 schema 的类型”描述的是感觉。改为机制或数值：“`.toSQL()` 返回发送给数据库的精确字符串”“列重命名会让构建失败”。先问这句话告诉读者要做什么或知道什么，再写出来。如果无法改成具体指令、事实或数字，就删除。再检查一次：若一句话能原封不动放进另一个项目的文档，它就没说明本项目的任何信息，删除。
28. **缩短或拆开密集句子。** 读者需要回头读才能解析句子时，拆成两句或删减从句。一句一个意思。
29. **主动语态。** 优先使用。识别 "is/are/was/were + 过去分词"，明确行动者：“查询被验证”改为“编译器验证查询”，“文件由加载器解析”改为“加载器解析文件”。只有行动者未知或确实不重要时才用被动语态。
30. **删除副词，或改用更有力的动词。** “运行得很快”改为“速度快”或具体数值，“显著提升”改为实测变化量。需要副词支撑的弱动词，说明动词选错了。
31. **优先选平实词。** "utilize"、"leverage" 改为 "use"，"facilitate" 改为 "help"，"numerous" 改为 "many"，"in the event that" 改为 "if"。华丽同义词很少更清楚。
32. **刻意做作的文字。** 明明有直白说法，却使用隐喻或修饰：警句（“接上它，否则删掉它”）、为效果而写的残句、拟人化代码（“计划握着它”）、比喻动词（“搭便车”“立足于”）、固定框架套话。“值得转动的旋钮”改为“值得调整的参数”。直接说出含义。规则 26 覆盖隐喻名词。
33. **过度压缩。** 省略冠词、没有动词的碎句、符号化表达和缩略语，让读者解码而非阅读。“Parser rejects bad date → exit 2, no write”改为“The parser rejects a bad date, exits with code 2, and writes nothing.”，即“解析器拒绝无效日期，以代码 2 退出，并且不写入任何内容”。使用带完整冠词和动词的句子，把箭头与缩略语写清楚。
