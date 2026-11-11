# Approved premium finishing — sound, highlights, small animations

The user approved these three elements in the delivered Genie 4 / 世界模型 video on 2026-10-28 and asked to retain them in this skill. Use them as the default finishing language for future premium-v2 edits. Adapt to the new speech and topic; the example's 13 cues, timestamps, diagrams, and claims are not a template to copy unchanged. Keep classic routing intact.

## Semantic sound effects

Use a small recurring sound vocabulary at meaningful title landings, scene changes, inputs, discoveries, selected outcomes, and closing takeaways. Place cues against frozen speech and the visible action; leave ordinary speech and reading holds quiet. Do not infer a request for background music. Music is chosen separately for each new video: follow an explicit current-project choice; otherwise ask once whether it is wanted while continuing independent work. Do not make a previous project’s track or music-on setting the default. Explicit silence overrides the SFX default.

The actual five approved files are bundled in [assets/approved-sfx](../assets/approved-sfx/); `manifest.json` preserves their source-library descriptions and durations. They were copied from the HyperFrames bundled offline SFX library. Preserve source metadata; do not invent a license claim. Copy used files into each project's media folder so the editable package remains self-contained.

| File | Typical use | Starting linear gain from this approved mix |
| --- | --- | --- |
| `pop.mp3` | Title landing, completed physical action | 0.15–0.16 |
| `whoosh-short.mp3` | Enter a demonstration or a new explanatory space | 0.15–0.17 |
| `click-soft.mp3` | Input, detection, choosing a route | 0.22–0.24 |
| `ping.mp3` | Reveal a key concept or distinction | 0.14–0.17 |
| `chime.mp3` | A result, benefit, or closing resolution | about 0.15 |

These gains apply to these files, not arbitrary replacement recordings. Adjust against the actual voice level. Keep a single dialogue stream, mute duplicate video audio, preserve short sound tails, and keep speech intelligible. A sound must agree with the event: a cup caught in the explanation gets a light completion cue, not breaking glass. Avoid identical whooshes on every cut.

Save each cue's time, file, gain, narrative reason, and provenance in `sound-design.json`. Check the final mixed audio, not just the timeline: confirm the cues are present, speech stays clear, and true peaks do not clip. The approved mix measured -16.6 LUFS and -2.0 dBFS true peak; use these as a reference, not mandatory measurements for every source.

## Caption and diagram highlights

For the current premium style, use these approved colors on a dark support surface until the user approves a replacement palette.

| Role | Color | Meaning |
| --- | --- | --- |
| Ordinary text | `#FFF9EC` | Unemphasized speech |
| `data` | `#9CC9F5` | Evidence, quantities, prediction |
| `action` | `#E6C77D` | Main concept, action, takeaway |
| `benefit` | `#B3D6A2` | Planning, selected outcome, benefit |
| `risk` | `#FFAD99` | Cost, danger, loss, contradiction |

Keep the same role color in captions and its corresponding card or diagram. Normally highlight one primary phrase per page. A before/after comparison may highlight both values. Keep qualifiers, numbers and units together. Use the mode's baseline caption color for ordinary words.

Retain structured `emphasis` spans in caption JSON and verify they actually render. For Will's Premium 2.1 captions, use the [approved white-text treatment](captions.md#premium-21-default-for-will), including direct color emphasis. Adapt placement and size to the source composition and keep a stable, separate caption lane with at most two lines.

## Small animations that explain

Choose one visual model per explanatory beat. Establish the state, reveal the change or consequence, then hold the result. Reuse a simple object or stable diagram rather than replacing it with decorative scenes. Return to the full-frame presenter for interpretation.

- Nodes/cards: opacity 0→1 with a short 24 px rise, about 0.45 s, `power3.out`; about 0.55 s between reveals is a useful starting point. Align reveals to the actual spoken reasoning instead of applying a fixed stagger to every scene.
- Evidence rule: `scaleX: 0→1`, origin left, about 0.5 s. Keep headings already readable when first-frame title visibility is required.
- Physical analogy: one small movement makes the consequence visible; the approved cup example moved roughly 75 px right / 35 px down and rotated 17° over 0.7 s with `power2.inOut`, then revealed a catching hand over about 0.55 s. Reuse the state→prediction→response pattern, not the cup artwork for unrelated topics.
- Planning: show a few alternatives, then distinguish the chosen route with the green role and a restrained border/connector. Use narration to determine when the selection is revealed.

After each entrance, allow a stable reading hold. Avoid perpetual motion, bouncing PiP, busy particles, and effects unrelated to the explanation. Keep animation deterministic in the HyperFrames timeline; Remotion places the rendered unit and its corresponding sound without recreating its internal motion. Inspect start, reveal, settled, and exit frames together with the real speaker and captions.
