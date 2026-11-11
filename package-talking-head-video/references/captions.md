# Shared Captions

## Caption grammar

- Treat captions as the speech layer, not as information cards.
- For Will's Premium 2.1 edits, follow the white-text default below. In other styles, choose Paper text with Ink support or Ink text on a Paper panel according to the footage. Use the semantic palette for selected spans and keep ordinary words neutral.
- Highlight the key data in spoken copy: quantities, percentages, prices, dates, durations, and before/after values when they carry the argument. Keep the value and unit together, and retain nearby qualifiers such as “近”, “超过”, currency, time period, and comparison direction. Do not highlight every incidental number.
- Normally emphasize one phrase per page. For a before/after comparison, two coordinated value spans are appropriate. Choose colored text, a marker block, underline, or a compact number badge; do not stack all treatments on one phrase.
- Example: in “Agent Skills 已经有 100 万个了”, highlight “100 万个” in Blue or on a yellow marker; in “近 2.8 亿次安装”, keep “近” and “次安装” attached to the value. Use the same data color in the corresponding evidence card. These are formatting examples, not facts to reuse in another video's copy.
- Save highlights as structured caption metadata, for example `emphasis: [{"text":"100 万个","colorRole":"data","treatment":"marker"}]`. Resolve roles to the project's selected palette. Match the exact phrase, specify its occurrence when ambiguous, and do not alter transcript text or speech timing to create emphasis. Render styled spans in the final composition; plain SRT retains the readable text while JSON keeps styling metadata.
- Review a key-data caption and a colored card in the final rendered output at phone size. If a highlight washes out against footage, add Ink/Paper support or use the corresponding contrast-safe palette variant.
- Prefer a quick baseline rise and opacity settle. Do not animate every character independently by default.
- Keep captions to two lines and one primary reading target.

## Will's introduction

Write the name as `Will说白了`, with no space or punctuation inside the name. The first caption reads 「大家好，我是Will说白了」. Start the next caption on the second spoken 「说白了」 and join it to the following clause with a comma. Keep both occurrences in the source speech and omit the ellipsis.

## Premium 2.1 default for Will

Use bold white caption text in the visual style of the opening title, with a heavy sans serif for Latin lettering. Place it directly over the footage with a soft neutral shadow where needed. Omit background plates and colored outlines. Emphasize key spans by changing the glyph color directly, using `treatment: "text-color"` and the appropriate semantic role. Check readability on bright footage and dark graphics at phone size. Use a contrast-safe color or adjust the neutral shadow when needed.
