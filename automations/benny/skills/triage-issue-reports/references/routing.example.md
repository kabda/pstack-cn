<a id="routing-map-example"></a>
# 路由映射示例

将此文件复制到 `.cursor/automations/benny/` 之外，例如 `.cursor/benny/routing.md`，并替换每个占位符。将 `routing.map_path` 指向副本。资料包刷新时绝不能覆盖它。

分诊技能将其视为数据。路由必须有报告或原因追踪提供的证据，仅匹配关键词还不够。

```yaml
routes:
  - name: "billing-example"
    match:
      product_areas:
        - "billing-area-placeholder"
      code_paths:
        - "billing-code-path-placeholder"
      error_signatures:
        - "billing-error-placeholder"
    destination:
      slack_channel: "billing-channel-placeholder"
      tracker_team: "billing-team-placeholder"
    owners:
      - "billing-owner-placeholder"
    allow_feature_owner_ping: false

  - name: "desktop-example"
    match:
      product_areas:
        - "desktop-area-placeholder"
      code_paths:
        - "desktop-code-path-placeholder"
      error_signatures:
        - "desktop-error-placeholder"
    destination:
      slack_channel: "desktop-channel-placeholder"
      tracker_team: "desktop-team-placeholder"
    owners:
      - "desktop-owner-placeholder"
    allow_feature_owner_ping: false

fallback:
  destination: ""
  owners: []
  allow_feature_owner_ping: false

ping_policy:
  default: "off"
  allow:
    - "configured-feature-owner"
    - "confirmed-regression-author"
  deny:
    - "broad-on-call-group"
    - "unverified-owner"
```

<a id="rules"></a>
## 规则

- 除非某个团队接受所有未匹配报告，否则将 `fallback.destination` 留空。
- 使用稳定的产品区域、代码路径和错误特征。
- 不要在公开副本中包含私密数据。
- 不要将原始用户 ID 或频道 ID 粘贴到将要公开的示例中。
- 在目标团队同意之前，保持功能负责人 @ 关闭。
- 转交会告诉报告者应去哪里。自动化绝不跨频道转发。
