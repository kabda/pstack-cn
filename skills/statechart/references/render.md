<a id="render-a-chart"></a>

# 渲染图表

使用 npm 包 `pele@1.9.0` 渲染展示的每份 `.mmd` 文件，并将 SVG 交给用户。在仓库外安装一次 Pele。每份 SVG 写在对应 `.mmd` 旁边，使用相同文件名。API 位于 https://pele.run/api 。向 `render` 传入选项 `{ limit: 1_000_000, outputLimit: 8_000_000, maxEdges: 10_000 }`。Pele 默认限制可能小于含 500 个状态的图表所需。Pele 抛出 `PeleError` 时，向用户展示 Mermaid 文本和错误。

<a id="colors"></a>

## 颜色

Pele 忽略 Mermaid 的 `theme` 和 `themeVariables`。在 `.pele` 上设置其 `--pele-*` CSS 变量，列表见 https://pele.run/theming 。命令为每个状态赋予所属组的颜色 class，例如 `class sN teal`。它为每个不良状态标记 `class sN breaks` 或 `class sN mayBreak`，为到达缺陷的最短路径上每个状态标记 `class sN bugPath`，为 PROPERTY 反例中永远重复的状态标记 `class sN repeats`。Pele 把这些 class 放在状态节点上。使用 CSS 为其着色。

`.mmd` 文件为 `breaks` 和 `mayBreak` 各提供一条 `classDef`，让任何 Mermaid 查看器都能显示缺陷标记。组颜色、`bugPath` 和 `repeats` 没有 `classDef`。Pele 将每个 `classDef` 颜色写成节点的 `style` 属性，而 `style` 属性优先于普通 CSS 规则，因此下面的标记规则使用 `!important`。没有它，深色主题仍会保留浅色标记。缺陷标记设置填充色和文字颜色，`bugPath` 与 `repeats` 设置边框。把标记规则放在组颜色之后，使标记覆盖组颜色。

这些颜色只是建议，沿用旧技能的配色。把它们放在每份 SVG 开头的 `<style>` 元素中，每份 SVG 就会跟随查看器的明暗设置。

```css
.pele {
  --pele-bg: #ffffff;
  --pele-fg: #1c1c1c;
  --pele-muted: #656565;
  --pele-line: #808080;
  --pele-surface: #fcfcfc;
  --pele-surface-alt: #f1f1f1;
  --pele-border: #c9c9c9;
}
.pele .blue rect { fill: #c3e0ff; }
.pele .orange rect { fill: #f0d3bf; }
.pele .purple rect { fill: #e3d5ff; }
.pele .yellow rect { fill: #f0dcbf; }
.pele .teal rect { fill: #bfe3df; }
.pele .tan rect { fill: #e5d9ce; }
.pele .pink rect { fill: #ffcbe6; }
.pele .breaks rect {
  fill: #ffecee !important;
  stroke: #e72e3b !important;
  stroke-width: 2.5px !important;
}
.pele .breaks text {
  fill: #cd2834 !important;
}
.pele .mayBreak rect {
  fill: #fff3e6 !important;
  stroke: #e8730c !important;
  stroke-width: 2.5px !important;
}
.pele .mayBreak text {
  fill: #b85a06 !important;
}
.pele .bugPath rect {
  stroke: #1680f3 !important;
  stroke-width: 2.5px !important;
}
.pele .repeats rect {
  stroke: #9b35d6 !important;
  stroke-width: 2.5px !important;
  stroke-dasharray: 6 3;
}
@media (prefers-color-scheme: dark) {
  .pele {
    --pele-bg: #1f1f1f;
    --pele-fg: #f5f5f5;
    --pele-muted: #acacac;
    --pele-line: #939393;
    --pele-surface: #121212;
    --pele-surface-alt: #2c2c2c;
    --pele-border: #4e4e4e;
  }
  .pele .blue rect { fill: #1b3857; }
  .pele .orange rect { fill: #573117; }
  .pele .purple rect { fill: #3c2e57; }
  .pele .yellow rect { fill: #573d17; }
  .pele .teal rect { fill: #174641; }
  .pele .tan rect { fill: #3d3127; }
  .pele .pink rect { fill: #57233e; }
  .pele .breaks rect {
    fill: #2e2021 !important;
    stroke: #cf2b35 !important;
  }
  .pele .breaks text {
    fill: #ff6463 !important;
  }
  .pele .mayBreak rect {
    fill: #2e2619 !important;
    stroke: #d0700f !important;
  }
  .pele .mayBreak text {
    fill: #ffa257 !important;
  }
  .pele .bugPath rect {
    stroke: #116dd2 !important;
  }
  .pele .repeats rect {
    stroke: #9a3fcf !important;
  }
}
```
