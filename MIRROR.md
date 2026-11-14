<a id="syncing-this-mirror"></a>

# 同步这个镜像

本仓库镜像自 [`cursor/plugins/pstack`](https://github.com/cursor/plugins/tree/main/pstack)，并加入自己的编辑：`README.md` 顶部内容，以及部分技能中不依赖特定智能体运行环境的改写。

两个分支保护这些编辑：

- `upstream` 原样保存 Cursor 文件，没有本地编辑。
- `main` 在 `upstream` 之上加入本镜像的编辑。

绝不要直接把 Cursor 文件复制到 `main`，那会抹掉这些编辑。

<a id="steps"></a>

## 步骤

1. 把 Cursor 最新的 `pstack/` 文件夹复制到 `upstream` 分支：

   ```bash
   git clone --depth 1 --filter=blob:none --sparse https://github.com/cursor/plugins.git /tmp/cursor-plugins
   git -C /tmp/cursor-plugins sparse-checkout set pstack
   git switch upstream
   rsync -a --delete --exclude .git --exclude MIRROR.md /tmp/cursor-plugins/pstack/ ./
   git add -A
   git commit -m "upstream: cursor/plugins/pstack @ $(git -C /tmp/cursor-plugins rev-parse --short HEAD)"
   ```

2. 合并到 `main`。Git 只应用上游变更，并保留镜像编辑：

   ```bash
   git switch main
   git merge upstream
   ```

   冲突意味着 Cursor 改了本镜像也修改过的行。保留 Cursor 的新含义，再重新应用不依赖特定运行环境的措辞。

   还应保留 `README.md` 中“这个镜像修改了什么”所列的社区修复，除非 Cursor 已交付同样修复。此时采用 Cursor 版本，并从清单删除该项。

   只携带缺陷修复。改变技能对智能体的指令，例如新增风格规则的 PR，应提交到 cursor/plugins 上游，在这里应拒绝。

3. 刷新随附的 Comment Sicko 提示词，然后检查是否引入新的 Cursor 专有指令：

   ```bash
   cp agents/comment-sicko.md skills/no-comments/references/comment-sicko.md
   git diff upstream@{1} upstream -- skills | grep -nE '\.cursor/|agent-transcripts|cursor-team-kit|create-skill|Task'
   ```

   以现有编辑相同的方式改写新匹配项。`skills/poteto-mode/SKILL.md` 的“运行环境（Harness）”部分列出了映射。

4. 在 `SYNC-LOG.md` 顶部添加一行，包含日期、上游版本和结果。即使上游没有变化，也应记录。

5. 推送两个分支：

   ```bash
   git push origin main upstream
   ```
