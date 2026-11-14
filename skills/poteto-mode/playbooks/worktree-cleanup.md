<a id="worktree-and-simulator-cleanup"></a>

### 工作树与模拟器清理

1. 快照与审计。记录 `df -h /`，然后运行 `scripts/worktree-audit.sh [-b <pr-base-ref>] [repo-path]`（principle-build-the-lever）。没有 `-b` 时它对照 `origin/HEAD` 检查 `MERGED`，因此 PR 目标是其他分支时传 `-b origin/<branch>`。它从 `git worktree list` 读取路径，绝不手输，因为手输 `myrepo-worktrees/x` 会漏掉实际位于 `.cursor/worktrees/myrepo/x` 的工作树（principle-encode-lessons-in-structure）。它按大小、年龄、合并状态、未提交工作、PR 状态、最近触及它的聊天分类每个工作树，再建议归入哪一类。对话记录扫描很慢，因此放到后台。
2. 分类是建议，不是许可。置顶和活跃聊天才是真实依据（principle-prove-it-works）。从用户或侧边栏获得该集合，交叉核对每个候选。工具曾把用户已置顶聊天的工作树标为 `safe`，因此以置顶集合为准。
3. 删除前验证使用情况。对每条 `verify-recent-chat` 记录及任何存疑项，分发子代理读取对话记录，报告聊天是否置顶或仍在进行，以及它涉及哪些工作树（principle-guard-the-context-window，对话记录属于批量材料）。置顶聊天会通过后台子代理在兄弟工作树创建 arena 和复现树；即使它们的名称从未出现在侧边栏，仍属使用中。按“子代理”一节选择每个子代理的推理级别及 fast 或标准速度。
4. 不可逆丢失前暂停。`wip:N` 表示 N 项受跟踪的未提交编辑。先展示 diff 并取得决定，因为干净工作树可从分支恢复，未提交工作则会丢失。`scratch:N` 是未跟踪的可丢弃内容，可以安全丢弃，但要点明文件。按“自主权”，干净、已合并且未使用的内容直接推进；`wip` 和使用中项暂停。
5. 清理已确认集合。逐路径执行 `git worktree remove --force <path>`。目录因被忽略的构建产物仍存在时，对它执行 `rm -rf`，然后 `git worktree prune`。分支引用保留，因此不会丢失提交。用 `df -h /` 和重新列出列表确认。
6. 模拟器及其他回收项。模拟器通常是下一项最大收益。执行 `xcrun simctl --set testing delete all` 清理 XCTestDevices 克隆，`xcrun simctl delete unavailable` 清理不可用项，先 `xcrun simctl runtime list` 再 `runtime delete <id>` 清理旧运行时。需要时还可清理 Xcode `DerivedData` 和 `iOS DeviceSupport`、`~/Library/Application Support/Cursor` 中的 `state.vscdb.backup`，以及 `snapshots/roots/<root>`。其中以曾作为工作区打开的文件夹命名的 `<root>` 会膨胀。还包括包缓存，如 pnpm、uv、brew、yarn。只清理用户没有要求保留的缓存。

这是唯一会删除用户状态、且没有代码审查兜底捕捉失误的操作手册，因此上方门禁就是审查。

**回复：** 清理前后的 `df -h /` 和回收空间、已清理工作树、每个保留项一行原因，例如由哪个聊天使用或有未提交工作。
