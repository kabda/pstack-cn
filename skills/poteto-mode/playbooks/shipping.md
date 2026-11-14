<a id="shipping"></a>

### 交付

**落地内容由你负责。逐 PR 独立验证，只落地从栈根起连续通过验证的部分，之后不要再碰 PR 栈。**

1. **先解析托管平台，再在落地前逐 PR 独立验证。** 默认 GitHub CLI（`gh`）。若 `command -v origin` 成功且 Origin 能解析仓库，每项 PR 操作都用 `origin pr`；否则继续 `gh` 并记录回退。绝不要求 Graphite（`gt`）。每 PR 一名验证者，都是 Cursor 云端智能体，按用户使用方式，通过对应控制技能，例如 `cursor-team-kit` 的 `control-ui` 或 `control-cli`，对比父项与 head 运行改动，并在 PR 留下 `PASS`、`PASS+NOTES` 或 `FAIL`。只有未编写代码的智能体给出的裁决才算数，因为作者会按自己的构建意图检查。CI 全绿和机器人批准都不是裁决，因为二者都没有像用户一样运行改动。
2. **只落地从底部起连续通过验证的部分。** 从最底层未合并 PR 向上走，在首个没有 `PASS` 或 `PASS+NOTES` 的 PR 停止。它下方的 PR 构成可落地段，最上方一个是上限。未验证 PR 上面的已验证 PR 也要等，因为离开下方代码就无法落地。如果某 PR 的分支既不含也不需要下方代码，就可以移到主干独立落地，但先要新裁决，因为旧裁决是在下方代码存在时运行，主干没有那些代码。
3. **重查裁决是否仍对应代码。** 裁决覆盖一个补丁，链式 rebase 会使上方每个 PR 变成新 SHA，却不让任何检查失败。信任旧裁决前，比较裁决 SHA 和当前 head 的 `git patch-id`。补丁只在测试、文档或 lint 配置上不同时，如果某通道运行的内容在两个 SHA 构建结果相同，只有噪声差异，其结果仍有效。噪声是裁决 SHA 自身两次构建也出现的差异，或嵌入的提交 SHA。报告每类噪声及对应文件，便于读者核查判断。改动本身仍要重新检查并审查，因为旧裁决没见过它。没有构建输出的通道，例如开发服务器，无法证明这一点，要重跑；其他发生偏移的内容也重新验证。
4. **自底向上，每次落地一个 PR。** 始终合并该段最底层未合并 PR，使用 `origin pr merge <pr>` 或 `gh pr merge <pr> --squash`。Origin 的无额外选项命令也会合并指定 PR 下方全部 PR；GitHub 中，基线仍是父分支的 PR 会合入该分支，而非主干。回读 PR 确认结果，使用 `origin pr view <pr>` 或 `gh pr view <pr> --json state,mergedAt,baseRefName`，因为合并命令可能在队列仅入队时报告成功，要求自动合并也不等于已经合并。已落地 PR 显示 merged，基线为主干，而非父分支。仅在裁决覆盖当前 head 的 PR 上启用 `--auto`，包括 Origin 就绪后合并或 GitHub 自动合并，因为它会落地届时任何就绪 head。一次合并落地后，把原来以已合并分支为基线的 PR 改目标为主干，使用 `origin pr edit <pr> --base <trunk>` 或 `gh pr edit <pr> --base <trunk>`；将其补丁移到合并结果上，并以 `--force-with-lease` 推送。裁决覆盖补丁而非提交，因此由第 3 步 patch-id 规则决定能否保留裁决。检查通过且裁决仍有效后，再合并它。
5. **落地期间别动 PR 栈。** 第 4 步对下一个 PR 的移动，是唯一允许的分支或基线变更，因为合并会落地当时分支和基线所含的任何内容，不论有无裁决。GitHub 上，在 `/loop` 下用 `playbooks/babysit.md` 的 queued 监视器（`scripts/watch-pr/watch-pr --queued-stack --stack-prs <bottom-to-top>`）监视该段，直到在上限报告 `COMPLETE`。Origin 上，每次 `origin pr checks <pr> --watch` 返回后，用 `origin pr view <pr> --checks` 重读当前 PR，直到上限显示 merged。父项合并后基线移向主干是预期现象，不是要修复的损坏。如果合并停滞，先查清原因，再改任何东西。
6. **到上限就停。** 扩展可落地段需要新裁决，因此必须重新从第 1 步开始。

**回复：** 已验证段及上限、每个 PR 的裁决及作出者、落地了什么及如何确认、下一个缺口需要什么。
