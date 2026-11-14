# 中文用户入口与图像可视复核

审校者：translate_docs；HTML 作者：root；源 commit：`9cd6939b766cb920f1c44970d7c7ee1ec28bd0d6`。2026-11-14 完成，无未决问题。逐文件审校哈希见 `REVIEW-wiki.json`。

## 中文内容与来源核对

已完整阅读 `wiki/index.html`，确认固定 commit 和插件版本准确，正确说明 backnotprop/pstack 是 cursor/plugins/pstack 的独立镜像，保留 Poteto、Lauren Tan、backnotprop 及贡献者署名，没有误把镜像维护者当作全部内容原作者。

中文使用差异明确：本次是本地工作区交付；内部身份和调用命名空间保持 pstack；原安装命令指向原插件／原镜像，不声称能安装中文译本；没有承诺已验证各宿主的中文安装路径。Markdown 原路径阅读入口、许可证、镜像维护资料和本地化记录均有链接。

对照实际逐张查看的位图，六张 JPG 的所有关键可读英文均有完整中文解读；logo 无可译英文。保留英文理由准确区分接口、精确标签、品牌、许可证和测试产物。README 同步标记的 unchanged 历史含义及中文正文经过翻译的事实说明清楚。

## 静态 HTML 检查

独立使用 Python HTMLParser 检查标签栈闭合、ID 唯一、页面内导航目标、所有本地链接目标存在，以及全部六张图的 alt；全部通过。HTML 声明 `lang="zh-CN"`、UTF-8 和 viewport，表头具有 scope，导航具有中文无障碍名称。

## 实际浏览器可视检查

按 ego-browser 技能使用本机已安装 Ego Lite，仅打开本地 `file://` 页面，没有访问外部服务，没有安装或启用插件。检查完已关闭本次独立浏览器空间。

- 桌面 1280×960：页面宽度与视口同为 1280，无横向溢出；六张本地图片均加载成功；五个导航锚点均存在。
- 窄屏 375×812：页面滚动宽度为 375，网格变为一列（335px），DOM 边界扫描没有越出视口的元素。
- 已分别捕获并查看桌面深色、桌面浅色及窄屏整页截图；标题、链接、长路径、表格、图像解读均可读，无文字重叠或裁切。
- 六份修改过的 SVG 均按其原始尺寸在 Chromium 实际渲染，检查全部 text 的客户端边界，全部位于视口内；已逐图查看，无中文裁切。图形关系、配色和半透明色在浏览器中正常。

证据：`visual-check/wiki-desktop.png`、`visual-check/wiki-light.png`、`visual-check/wiki-mobile.png`、`visual-check/svg-browser-check.json`，以及已用浏览器结果覆盖的 `svg-previews/*.png`。

先前 AppKit 不支持八位十六进制半透明色、Quick Look 缩略图裁切的问题，已通过实际 Chromium 渲染排除为浏览器中的问题；不需要改动上游图形。浏览器检查未运行技能、自动化、远程安装或真实服务集成，不将静态和可视检查表述为这些运行路径已经验证。


## 最终语言说明段增量复核

wiki 仅在英文保留说明中新增一段：technical-writing／unslop 的英语写作正反例保留并给中文解读；teach 及部分提示词原文明示英语表达，译文保留原语言策略。已直接对照固定源：teach 最后一段明确要求 plain spoken English，poteto-help/references/prompting.md 的上下文加载要求 plain English；technical-writing 有英语句式及 Global English 层，unslop 有英语正反例。因此该段准确。已重新解析 HTML，标签完整；仅增加普通段落，没有改变布局或样式，本轮不重复此前截图。已更新 REVIEW-wiki.json 当前内容哈希，无未决问题。
