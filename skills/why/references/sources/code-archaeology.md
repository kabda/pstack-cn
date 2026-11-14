<a id="code-archaeology-git--in-repo"></a>
# 代码考古（Git + 仓库内资料）

<a id="what-this-source-contains"></a>
## 此来源包含什么

- 提交历史（消息、日期、作者、差异）
- PR 描述、审查评论和讨论线程（通过 `gh`）
- 行内代码注释、TODO、FIXME、弃用说明
- ADR（架构决策记录），如果仓库维护了这些记录
- 测试，其名称和断言常记录促成改动的边界情况
- 同一提交修改的相关文件（共同变更信号）
- 仓库中的 CHANGELOG 条目和发布说明
- 提交消息和 PR 正文中的问题／工单 ID

这是最值得信赖、直接与代码关联且最完整的来源。所有经过仓库的内容都应在这里。

<a id="how-to-search-it"></a>
## 如何搜索

扩展种子提交列表：

```bash
# 跨重命名追踪历史
git log --follow --oneline -- <file>

# Pickaxe：添加或删除这段确切文本的提交
git log -S '<exact_string_from_code>' -- <file>

# 或按模式搜索：
git log -G '<regex>' -- <file>

# 每一行由谁在何时编写
git blame -L <start>,<end> <file>

# 单次提交的完整差异
git show <hash>

# 两个时间点之间影响此文件的提交
git log <old>..<new> -p -- <file>
```

寻找其他位置的文档：

```bash
# ADR 常位于 docs/adr/ 或类似目录
rg -l -i 'architecture.decision' --glob '*.md'

# 目标附近的 TODO 和 FIXME
rg -n -C2 '(TODO|FIXME|HACK|XXX|NOTE)' <target_file>

# 相关测试
rg -l '<symbol>' --glob '*test*'
```
