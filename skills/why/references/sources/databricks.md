<a id="databricks-analytics--system-tables"></a>
# Databricks 分析与系统表

<a id="what-this-source-contains"></a>
## 此来源包含什么

Databricks 是产品分析、数据管道和数据仓库遥测这一层，与 Datadog 互补。Datadog 提供*基础设施／运行时*视角，Databricks 提供*产品／数据*视角（用户做了什么、运行了哪些实验、功能使用如何变化、阈值常量从何而来）。

- **产品分析事件。** `your_warehouse.events.analytics_track_event`（原始表），以及 `<your_analytics_db>.<schema>.<table>` 中已类型化、去重的逐事件 dbt 模型。用户行为包括功能调用、点击、接受／拒绝、提交、客户端报告的错误。
- **使用与计费事件。** `your_warehouse.events.usage_event` / `<your_analytics_db>.<schema>.stg_usage_events`，`your_warehouse.events.raw_model_event` / `<your_analytics_db>.<schema>.stg_raw_model_events`。用于由成本或规模推动的决策。
- **实验／功能标志数据。** 曝光和结果表。**schema 因公司而异。** 假设表名之前，先用 `SHOW TABLES` 探测。
- **系统表。** `system.query.history`、`system.compute.warehouses`、`system.billing.*`、`system.access.audit`。回答“这个查询是否昂贵”“有人运行它的频率如何”“数据仓库负载何时激增”。
- **dbt 血缘。** `<your_analytics_db>.<schema>` 中的模型揭示哪些管道依赖某表／字段。上游变化经常促成消费方代码改动。
- **Databricks 笔记本。** 工程师在代码变更前编写的探索分析。**不能通过 SQL MCP 查询。** 如果怀疑依据在笔记本里，将其记为缺口。

<a id="how-to-search-it"></a>
## 如何搜索

使用 Databricks SQL MCP。主要工具为 `execute_sql_read_only`。如果返回 `statement_id`，使用 `poll_sql_result` 轮询，而非重新运行。

**查询前先定位。** schema 因公司而异。信任某个表名之前先探测：

```sql
SHOW TABLES IN <your_analytics_db>.<schema> LIKE '*<keyword>*';
DESCRIBE TABLE <your_analytics_db>.<schema>.stg_<event>;
```

**每个查询都限定时间。** 这些表非常大，无约束扫描会超时。按 `_timestamp`（事件）或 `start_time`（`system.query.history`）筛选交付日期前后的窗口，通常前后各约 30 天，只有充分理由才扩大。

**优先使用类型化的 dbt 模型，而非原始表。** `<your_analytics_db>.<schema>.<table>` 已去重、类型化并采用 Liquid Clustering。`your_warehouse.events.analytics_track_event` 有重复项，且 `properties_json` 未类型化。模型名模式为 `stg_<source>_<event_name_with_underscores>`，其中 `<source>` 为 `app`、`backend`、`website` 或 `cli`。仅凭模式不能确定时，用 `SHOW TABLES` 确认精确模型名。只有尚无 dbt 模型，或需要 dbt 刷新延迟期间的事件时，才退回原始表。

**类型化 dbt 模型的列约定**（了解后可避免额外一次 `DESCRIBE`）：

- `_timestamp`、`_id`、`_auth_id`、`_request_id`、`event_name`。每个模型的标准列
- `properties_<name>`。有类型、下划线命名的事件属性（`properties_entrypoint`、`properties_size_bytes` 等）
- `context_team_id`、`context_client_version`、`context_country`、`context_client_os`。预先提取的客户端上下文

<a id="investigation-patterns-that-tend-to-pay-off"></a>
### 通常有用的调查模式

选择与目标匹配的表和列组合：

1. **事件使用轨迹。** 在 PR 合并前后 ±30d 的窗口内，对相关 `stg_*` 模型按天计数。合并后一两天内从零跃迁到稳定数量，是该 PR 上线功能的有力旁证。降至零则暗示弃用或删除。
2. **防护／防御性检查的来源。** 查看 PR *之前* 14 天相关 `properties_<name>` 列的分布（中位数／p99／最大值）。p99 与目标阈值常量匹配，暗示该数值是依据数据选定的。
3. **实验／功能标志查找。** 用 `SHOW TABLES ... LIKE '*experiment*'` 找到曝光表，然后在 PR 日期附近，按变体获取相关标志键的曝光计数。
4. **迁移、回填或性能重写的查询历史证据。** 用 `statement_text ILIKE '%<table_or_symbol>%'` 和严格的 `start_time` 窗口筛选 `system.query.history`，可发现很可能促成改动的昂贵查询（按 `total_duration_ms` 排序，或聚合 `SUM(read_bytes)`、`COUNT(*)`）。
5. **dbt 血缘。** 如果目标读写 `<your_analytics_db>.<schema>` 模型，模型自身的 Git 历史（本仓库内）常包含依据。将线索交回 Git 调查者，不要自己越界追踪。

<a id="what-good-evidence-looks-like-here"></a>
## 此处的优质证据

除上述模式外：

- 对错误分类的事件计数，在防御性代码 PR 后几天降至接近零，暗示该 PR 解决了这类错误
- 曝光表某行指明目标的功能标志键，在 PR 交付日期附近有 “shipped”（已交付）／“concluded”（已结束）决策

<a id="common-pitfalls"></a>
## 常见陷阱

- **有埋点不等于有因果。** 事件存在说明有人关心到愿意记录它，不代表目标代码*因为*它而存在。声称因果关系前，搭配 Git 调查者提供的 PR／提交引用。
- **静默埋点变化。** 事件量阶跃可能意味着开始记录新事件，不代表用户行为变化。将增长解读为功能上线信号前，检查同一窗口的埋点 PR。
- **schema 漂移。** 事件属性会演变。今天类型化 dbt 模型中的某列，在目标编写时未必存在。旧数据可能仅在原始 `properties_json` 中带有该属性。
- **dbt 刷新延迟。** `<your_analytics_db>.<schema>.*` 按计划重建（通常每小时／每天）。针对最近几小时的事件，退回 `your_warehouse.events.*` 并按 `_id` 去重。
- **公司专属表。** 实验、功能标志、计费和使用表因公司而异。使用未经确认存在的表报告结果，是典型失败模式。先用 `SHOW TABLES` / `DESCRIBE TABLE` 探测。
- **保留截止点。** 如果相关窗口早于表的保留期或 dbt 模型创建日期，这是*缺口*，不是空结果。明确说明，避免综合者将“无结果”理解为“无活动”。
- **笔记本不可查询。** SQL MCP 看不到 Databricks 笔记本。如果怀疑依据在其中，返回缺口。

<a id="what-to-return"></a>
## 返回内容

对每项相关发现：
- 类型（产品事件／实验曝光／使用或计费事件／系统表行／dbt 模型）
- 完全限定表名，以及实际运行的精确查询
- 查询的时间窗口
- 简洁的数值摘要（计数、百分位、首次／最后出现时间戳）。**不要倾倒原始行。**
- 与目标交付日期的时间相关性（例如“首行为 2024-08-15，PR #49074 于 2024-08-14 合并”）
- 相关性及强度：直接／旁证／弱
