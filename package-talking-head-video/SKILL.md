---
name: package-talking-head-video
description: Edit Chinese talking-head videos using ChatCut cleanup, HyperFrames shot planning and visuals, Pixabay stock footage, and Remotion assembly. 剪口播视频 or 简洁剪视频 selects classic floating overlays; 精剪视频, 精剪版, and 精剪视频2.1 select validated black-gold 2.1 with full-frame presenter information cards and complex visual explanations. Also use for captions and source-quality diagnosis.
---

# Package Talking-Head Video

## Scope and mode first

Determine the requested task before loading tool skills. Diagnosis is read-only; captions-only stops after verified captions; cover-only never rerenders the video. Full packaging in classic and premium-v2.1 must complete the same [matching cover workflow](references/cover.md) before delivery. Default to both 3:4 portrait and 4:3 landscape covers (width:height); follow explicit requests for a different set or no cover.
There are two current modes. Persist `editMode` in DESIGN.md and the EDL. New premium projects use `premium-v2.1`.

| Request | editMode | Visual authority |
| --- | --- | --- |
| 剪口播视频 / 简洁剪视频 / 简单剪视频 / 经典版 / 之前的方式 | classic | [Classic](references/style-system.md): continuous full-frame presenter; bounded floating cards, screenshots and clips only |
| 精剪视频 / 精剪版 / 精剪视频黑金版 / 优美视频 / 精剪视频2.1 / 精剪2.1 / 2.1 | premium-v2.1 | [Premium 2.1](references/premium-v2.1.md), with [black-gold foundations](references/premium-v2.md). Use full-frame presenter cards for sparse information and explanation canvases for complex content. |

The user validated 2.1 and promoted it to the default premium workflow on 2026-11-11. Both “精剪视频” and “精剪视频2.1” select the same workflow. Load the 2.1 reference for every new premium project. Its density-based presentation rules govern sparse scenes, while the inherited foundations govern complex explanations.

For existing projects, preserve recorded `premium-v2` or `premium-v2.1-experimental` modes and their approved presentation unless the user requests migration. An explicit request for legacy 2.0 uses `premium-v2` and its reference. The old “2.1实验版” phrase is an alias for current 2.1 when creating a new project.

2.1 also requires a first-mention-only image plan for named products and people during initial storyboarding; the second and later mentions of the same entity (including aliases) do not trigger another card. Show the exact proposed images for user confirmation before visual production; if no matching image is found, request an upload. Follow the explicit approval gate in [the 2.1 reference](references/premium-v2.1.md); it is an exception to the general no-routine-checkpoint guidance.

Unspecified packaging defaults to classic. Revisions inherit a supported project's mode; ask which remaining mode to use for an unsupported legacy project. Do not silently blend or migrate modes.
Latest explicit user instructions override defaults. Proposed color/geometry worksheets do not change the active style until the user approves them.

## Responsibilities and invariants

- ChatCut owns retained speech, cleanup, final transcript and lip sync. Freeze verified A-roll before downstream timing; speech changes invalidate affected captions/scenes.
- HyperFrames owns visual interpretation, graphic layout and internal animation. Remotion owns master FPS/canvas, placement, source offsets, captions, mix and final render. Never implement the same animation in both.
- Preserve the original file, display-conformed aspect ratio, complete A-roll framing, proportions and natural skin color. Only premium's localized circular PiP mask is an exception; full-frame returns stay intact. A different-ratio deliverable needs explicit authorization and a separate derivative.
- Use delivery-grade media, never upscale a preview proxy when a better source exists. Preserve detail with a lossless/visually lossless handoff and lossless frame capture; follow the delivery settings in [source fidelity](references/source-fidelity.md). Verify actual pixels and decoded media, not just export settings.
- Keep one dialogue stream; duplicate presenter/B-roll video layers are muted unless deliberately mixed.
- Prefer distinct Pixabay footage within each video; avoid reusing the same provider asset ID just with another trim. Seek another suitable shot first; record a deliberate repeat and its reason in the source ledger.
- During stock-video playback, show the footage alone with no actual-presenter layer, cutout or circular PiP; keep narration/captions as needed. This stock-only treatment applies to both modes and is the user-approved exception to classic continuous A-roll. Diagram-only explanations retain their mode’s presenter treatment.
- Keep stock footage visually clean: no automatic corner labels such as “示意”, “情景示意”, or “概念示意”; retain provenance in the source ledger. See [B-roll](references/broll-sourcing.md) for exceptions.
- Background music is a per-video choice, separate from semantic SFX. Follow the user’s choice for the current video; if unspecified, ask once whether to add music while continuing independent editing. Do not carry a previous video’s music decision or track into a new video automatically.
- Missing tools or unreadable assets must be reported; no silent role replacement or false completion.
- Default opening is moving full-frame presenter plus a prominent centered headline from frame one, protecting face and a separate caption lane. Default cover uses a faithful real frame, clear full head, separate large title, and topic-led imagery.
- Full packaging runs through verification and delivery; no routine extra approval checkpoints when unattended execution was requested.

## Load only the current stage

Honor each tool skill's prerequisites. Do not preload every plugin merely because this workflow mentions it.

| Stage | Load when entering the stage | Output / completion gate |
| --- | --- | --- |
| Inspect source | [Source fidelity](references/source-fidelity.md); run scripts/inspect_video_color.py. Load [color pipeline](references/color-pipeline.md) for HDR/SDR, wide-gamut or exposure/color issues | Verified source metadata, framing/free regions, quality baseline |
| Clean speech | ChatCut basics, transcription, talking-head-guide; asset-import if importing. Read [cleanup](references/speech-cleanup.md) | Corrected final speech/captions; no clipped words, retakes or gaps |
| Freeze local handoff | ChatCut verification/export skills when used; [download](references/aroll-download.md) for local handoff | Complete decoded local A-roll and final timing, not a preview/export status |
| Plan scenes | HyperFrames skill; selected mode; [manifest contract](references/manifest.md); [opening](references/opening.md) for opening design | Stable-ID EDL, meaningful beats, protected regions, B-roll briefs |
| Source footage | [B-roll](references/broll-sourcing.md); Pixabay first; asset-import only when importing | HyperFrames-led clip selection based on inspected excerpts, with source/rights ledger |
| Author visuals | HyperFrames and CLI skills; selected visual mode; project DESIGN.md from assets/DESIGN.template.md | Settled hero layout first, then deterministic animations; validate/inspect assets |
| Compose | Remotion router and only applicable create/markup/captions/multimedia/render skills; [captions](references/captions.md) when caption work is needed | One canonical timeline; correct alpha, trim, placement, captions and audio |
| Premium finishing | [Finishing](references/premium-finishing.md) before sound/highlights/micro-animation decisions | Semantic restrained SFX and actual rendered emphasis; no implied music |
| Cover (both current modes) | [Cover](references/cover.md), local source frame and saved reference; built-in imagegen skill | Each required cover generated, checked for exact ratio and inspected at full size and phone-grid size, and saved with its source frame and prompt |
| Acceptance | [Checklist](references/quality-checklist.md), selected mode's acceptance items | Structural, pixel and audio checks pass; concise evidence report |

For premium, assess real-footage needs after speech freeze even if none are accepted; record search outcomes or editorial/access reasons. Classic searches only where footage use is planned. Never require a clip quota.
Create scenes when meaning changes, not per subtitle page. Use footage for concrete actions, diagrams for mechanisms, and full-frame presenter for judgments/handoffs/close. For sparse premium information, use full-frame presenter overlays under the 2.1 rules. For complex diagram-only explanations, premium PiP omission is a readability exception recorded in EDL. Stock-video scenes always use the stock-only treatment above, with `pip: false` recorded in the EDL.
Record each visual asset's path, dimensions, placement and lifetime. Bound classic information overlays to their content with alpha outside; full-frame stock footage follows the stock-only exception in both modes, while other opaque full-frame visuals belong to premium. Keep caption lane and face clear; simplify content instead of crowding.
Remotion derives frames from absolute millisecond timestamps; use the manifest contract. It places HyperFrames assets without recreating their internals. Layer source/background → visual assets → premium PiP → captions/marks; mix sounds once.

## Local revisions and economical reads

First inspect existing project state and requested delta. Reuse verified unchanged artifacts; do not restart completed stages automatically.

| Change | Rebuild / verify | Reuse |
| --- | --- | --- |
| Title, font, color or one card | Affected visual/caption assets and composition; inspect changed beat and transitions | Frozen speech, valid footage/source ledger, unaffected scenes |
| Cover only | Cover and cover acceptance | Video and timelines |
| Footage replacement | New excerpt, rights record, placement, affected scene/edges | Speech and unaffected captions/graphics |
| Speech timing | Recompute affected captions, EDL and downstream placements, including shifted later beats | Still-valid design and footage provenance |
| Proxy replacement | Replace all affected A-roll references atomically; preserve cuts, offsets, fit, tracks and audio; read back and compare pixels | Unchanged timing and graphics |

Do not weaken final checks: changed video output still needs duration/canvas/audio verification and representative playback. Scope deep visual checks to changed beats plus boundary/regression samples.
Read an unchanged reference once per active context, not once per scene. After context loss or file changes, reload only relevant rules. Request bounded transcript/timeline ranges and small candidate sets; expand only on evidence of a gap.
Keep canonical captions in captions.json, scene timing/assets in EDL, visual decisions in DESIGN.md, provenance in broll-manifest.json and cues in sound-design.json when used. Reference IDs instead of duplicating full transcripts and manifests in every document.
Batch independent read-only checks where supported; respect tool mutation/job restrictions. Use native progress mechanisms rather than repetitive polling. Do not echo full tool payloads or large code/files when a bounded result suffices.
A text-only design change does not justify regenerating media or re-searching stock. Check relevant existing assets before creating replacements.

## Acceptance and delivery

The checklist is the acceptance authority; mode references define style, not a competing technical standard. Inspect actual composed opening, dense text, important footage/action, scene edges, presenter returns and ending. Compare original-detail source/intermediate/final samples for face/hair/glasses; diagnose the first stage where degradation occurs.
Cover acceptance is a separate delivery gate in both current modes. Verify the cover against its real source frame and at phone-grid size. Preserve dimensions and authentic logos; do not infer relationships from decorative brand proximity.
For full packaging deliver final MP4, matching covers and source frame/time, editable Remotion, cleaned ChatCut project or A-roll, corrected caption data, EDL, HyperFrames sources/assets, source ledger/credits and sound cues when used, plus a concise validation summary.
Diagnosis returns evidence, cause, prioritized fixes and explicit confirmation that no video was regenerated. Report partial results and blockers accurately.
