# Shared Captions

## Caption grammar

- Treat captions as the speech layer, not as information cards.
- Use Paper text with Ink support or Ink text on a Paper panel according to the footage. Color selected spans with the semantic palette above; ordinary words stay neutral so emphasis remains visible.
- Highlight the key data in spoken copy: quantities, percentages, prices, dates, durations, and before/after values when they carry the argument. Keep the value and unit together, and retain nearby qualifiers such as “近”, “超过”, currency, time period, and comparison direction. Do not highlight every incidental number.
- Normally emphasize one phrase per page. For a before/after comparison, two coordinated value spans are appropriate. Choose colored text, a marker block, underline, or a compact number badge; do not stack all treatments on one phrase.
- Example: in “Agent Skills 已经有 100 万个了”, highlight “100 万个” in Blue or on a yellow marker; in “近 2.8 亿次安装”, keep “近” and “次安装” attached to the value. Use the same data color in the corresponding evidence card. These are formatting examples, not facts to reuse in another video's copy.
- Save highlights as structured caption metadata, for example `emphasis: [{"text":"100 万个","colorRole":"data","treatment":"marker"}]`. Resolve roles to the project's selected palette. Match the exact phrase, specify its occurrence when ambiguous, and do not alter transcript text or speech timing to create emphasis. Render styled spans in the final composition; plain SRT retains the readable text while JSON keeps styling metadata.
- Review a key-data caption and a colored card in the final rendered output at phone size. If a highlight washes out against footage, add Ink/Paper support or use the corresponding contrast-safe palette variant.
- Prefer a quick baseline rise and opacity settle. Do not animate every character independently by default.
- Keep captions to two lines and one primary reading target.
