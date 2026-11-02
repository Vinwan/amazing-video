---
name: package-talking-head-video
description: Edit Chinese talking-head videos with ChatCut cleanup, footage sourcing, HyperFrames visuals, and Remotion assembly. “剪口播视频” or “简洁剪视频” selects classic floating overlays; “精剪视频” or “2.0” selects premium-v2 black-gold or explicit colorful; “按照 v3.0 剪辑” selects presenter-led footage storytelling. Also use for captions, video packaging, and source-quality diagnosis.
---

# Package Talking-Head Video

Produce a readable, high-retention talking-head video through one ordered pipeline:

`ChatCut clean A-roll -> freeze speech timing -> plan footage needs -> search candidates -> inspect clips and sources -> download and trim -> HyperFrames package visuals -> Remotion assemble and render`

For every premium-v2 package, read [B-roll sourcing](references/broll-sourcing.md) after freezing speech and before authoring visuals. The user-approved AIHack V2 default combines rhythm-matched real footage for concrete actions with diagrams for abstract mechanisms. Plan and assess footage needs even when no clip is ultimately used; record search outcomes and omission reasons. Use ChatCut `search_stock_media` as the initial stock-search path. Add footage only when it clarifies the spoken idea; do not impose a stock-clip quota.

Do not let the three systems compete for the same responsibility.

## Select the editing version first

Use the user's latest explicit mode instruction and save `editMode` in the project DESIGN.md and EDL manifest:

| User wording | editMode | Treatment |
| --- | --- | --- |
| 按照 v3.0 剪辑 / v3.0 / V3.0 / 3.0版剪辑 | narrative-v3 | Read references/narrative-v3.md; presenter-led footage storytelling, not a premium-v2 color variant |
| 剪口播视频 / 简洁剪视频 / 简单剪视频 / 之前的方式 | classic | Existing Clear Signal Editorial workflow and style-system.md, including A-roll, Explainer, and Emphasis alternation |
| 精剪视频彩色版 | premium-v2 | Use `visualVariant: colorful`; read references/premium-colorful.md and the shared premium-v2 rules |
| 精剪视频黑金版 / 精剪视频 / 优美视频 / 2.0 | premium-v2 | Use `visualVariant: black-gold`; follow references/premium-v2.md |

Record `visualVariant` in DESIGN.md and the EDL for premium-v2. An explicit variant takes precedence; continuing revisions inherit their existing variant. Unqualified 精剪视频 / 优美视频 / 2.0 retain the established black-gold treatment. Both variants use the same established cover workflow; choosing a video variant never changes the cover design logic. Keep unspecified packaging requests on `classic`; continuing revisions inherit that project's mode. Do not blend versions automatically. For premium-v2 explanation sections, default to the actual speaker in a circular picture-in-picture over explanatory content; retain full-frame opening, judgment, and ending beats. Both modes retain the existing speech cleanup, source quality, caption accuracy, and matching-cover requirements. In `premium-v2`, its explicit palette, camera, and scene rules take precedence over conflicting classic style defaults; all technical/source-preservation rules remain shared.

For premium-v2, read [approved finishing](references/premium-finishing.md) before planning sound, caption highlights, or small explanatory animations. Reuse this user's approved Genie 4 treatment as the default: restrained semantic SFX, consistent colored emphasis, and short causal animations. Explicit silence or later style instructions override this default; colorful retains its own palette.

## Load the required skills

When the user explicitly selects v3.0, save `editMode: narrative-v3` in DESIGN.md and the EDL and read [v3.0 narrative rules](references/narrative-v3.md) before scene planning. Its presentation, typography hierarchy, footage and PiP rules override conflicting classic/premium-v2 visual instructions in steps 4–6 and their references. Shared speech, source fidelity, cover, tool roles, and delivery rules remain unchanged. V3.0 does not change the existing classic or unqualified 精剪视频 routing; continuing revisions inherit the project's mode unless explicitly changed.

Before acting, load:

- ChatCut: `chatcut-plugin-basics`, `asset-import` when needed, `transcription`, `talking-head-guide`, `verification`, and `export` when handing off a cleaned A-roll file;
- HyperFrames: `hyperframes` and `hyperframes-cli`;
- Remotion: `remotion-best-practices`, then `remotion-create`, `remotion-markup`, `remotion-captions`, `remotion-multimedia`, and `remotion-render` as applicable.

Follow each loaded skill's tool-specific constraints. If one plugin is unavailable, report the missing dependency and complete only the stages that remain verifiable; do not silently replace its role with another system.

## Respect scope

- For diagnosis-only requests, inspect and report without editing or rendering.
- For captions-only requests, use ChatCut and stop after verified caption delivery unless the user asks for composition.
- For full packaging, run the pipeline end to end. If the user explicitly requests unattended execution, do not pause at ordinary checkpoints.
- Preserve the source file. Work from project assets, copies, or generated intermediates.
- For this user's future videos, default to the approved live-presenter-plus-title opening: show the actual speaker full-frame from the first frame with a short, large centered headline, keeping the face and ordinary captions clear. Follow the opening-title guidance and approved Gemini 4 Carbon reference in `references/style-system.md`. Use an illustrated or graphics-only opening only when the user explicitly requests it.
- Every completed video package also includes one matching cover by default: use a faithful frame of the user at a scale that leaves the whole head clear, a separate large topic-specific title, a topic-led background, and relevant company/product elements. Follow the cover guidance in `references/style-system.md`; deliver it alongside the video without a separate cover request.
- Use the selected version's saved visual language. For classic, preserve Clear Signal Editorial. For premium-v2 black-gold, use the approved Yona sample analysis in references/premium-v2.md. For colorful, read references/premium-colorful.md in addition to the shared premium-v2 rules; its palette and card treatments override only the conflicting black-gold visual identity. Extract reusable scene and motion techniques while keeping artwork, titles, and topic relationships original.

## Establish the authority model

- **ChatCut owns speech truth:** retained words, removed retakes, pause lengths, source-to-edited timing, lip sync, and corrected transcript.
- **HyperFrames owns visual truth:** scene interpretation, design system, information cards, diagrams, title beats, overlays, and their internal animation.
- **Remotion owns delivery truth:** master frame rate, canvas, ordered sequences, layer structure, integration of A-roll/captions/visual assets, audio routing, and final render.

After ChatCut A-roll cleanup is approved or verified, freeze it. Never edit speech timing independently in HyperFrames or Remotion. If speech changes later, invalidate downstream timings and regenerate the affected scene plan, captions, and composition.

## 1. Inspect the source

Inspect content, duration, dimensions, rotation, frame rate, codec, audio, and representative frames before editing. Run `scripts/inspect_video_color.py` on local source and final files. Read `references/color-pipeline.md` for HDR, HLG, PQ, Dolby Vision, BT.2020, 10-bit media, or exposure/color complaints.

Identify the face, mouth, gestures, products, existing text, and low-information regions that graphics may safely occupy. Inherit the source video's display-conformed canvas and aspect ratio by default. Decide duration and pacing from the request or source context.

Preserve the source canvas and displayed aspect ratio throughout the entire workflow. Resolve rotation/display-matrix metadata before deciding orientation; do not infer orientation from encoded width and height alone. A 16:9 source stays 16:9 and a 9:16 source stays 9:16 unless the user explicitly requests a separate aspect-ratio variant.

Do not crop, reframe, stretch, squash, or convert the source to a different aspect ratio merely because a target platform commonly uses another format. The localized circular speaker mask in premium-v2 is an explicit exception for PiP presentation only; follow references/premium-v2.md and preserve the full-frame master and returns. Never force source media into target width and height independently. Keep aspect-ratio locking enabled in ChatCut, HyperFrames media wrappers, Remotion, proxy generation, and final export. Make proxies and final canvases match the display-conformed source ratio. Inspect a representative frame after every canvas or proxy change and compare the full framing and the speaker's proportions with the source before continuing.

Only when the user explicitly requests another aspect-ratio version, create it as a separate derivative timeline/composition and obtain the intended crop-versus-contain treatment. Never replace the source-ratio master with that derivative.

### Protect source resolution and clarity

Treat preview proxies and delivery media as different classes of asset.

- Use a lower-resolution proxy only for temporary inspection, transcription, or rough editorial work when necessary. Label it as a proxy and never silently promote it to the final master.
- Before final assembly or export, compare the display-conformed source dimensions and byte size with every A-roll asset actually referenced by the timeline. The final A-roll must use the highest-quality ready source or a delivery-grade intermediate at the intended output resolution.
- Never upscale a 540p, 720p, or otherwise reduced proxy into a 1080p/4K master when a higher-resolution source exists. Selecting a 1080p export preset does not restore detail lost in the timeline source.
- Keep proxies and delivery intermediates at the source aspect ratio. Resolution reduction never permits crop, stretch, or orientation changes.
- Wait for the high-resolution asset to become remotely readable before frame verification or export. A registered placeholder, thumbnail, transcript-ready state, or asset-library entry alone does not prove that the media bytes are export-ready.
- A 1080p file can still lose fine detail during upload preparation, cloud export, and final encoding. When those steps transcode the source, inspect the actual uploaded media and compare aligned, full-resolution face/hair/glasses regions from source → upload → cleaned A-roll → final; verify more than one representative moment before delivery. Avoid unnecessary lossy generations and prefer a validated original-quality local handoff. If the supported handoff forces a visibly softened intermediate, report it and resolve or obtain direction rather than claiming source-quality delivery. Bitrates across different codecs or scene contents are clues, not proof by themselves.
- If a high-resolution upload fails, keep the current timeline intact, explain the upload blocker, and resume replacement only after a ready high-resolution asset is available. Do not export the known low-resolution proxy as the final deliverable.

When repairing a timeline that used a low-resolution proxy, replace every affected A-roll item atomically while preserving timeline start, duration, source start offset, track, fit, fades, and audio behavior. Keep captions, Motion Graphics, and scene timing unchanged. Re-read the track afterward and confirm that every A-roll item references the high-resolution asset.

## 2. Clean the A-roll in ChatCut

Import or identify the source, wait for transcription readiness, and use transcript-driven Script editing rather than manual destructive cuts.

Perform cleanup in this order:

1. Correct names, numbers, domain terms, punctuation, and obvious ASR errors at the transcript source.
2. Remove clear filler sounds, failed starts, abandoned fragments, and redundant takes while preserving complete meaning.
3. Compress long meaningless pauses; default to roughly 0.3 seconds rather than zero. Preserve breaths and rhetorical pauses that support natural delivery.
4. Prefer the best complete take. Do not stitch unrelated half-sentences or delete connective words that carry logic.
5. Apply the edited script, then run audio smoothing after the last timing change.
6. Generate or update captions only from the cleaned transcript and final A-roll timeline.

Read the ChatCut project back and inspect composed frames. Confirm there are no black gaps, clipped words, duplicated phrases, lip-sync drift, stale captions, or audible pops.

Export or otherwise provide Remotion with the cleaned A-roll and caption timing. For a local Remotion workflow, read [A-roll download and recovery](references/aroll-download.md): render completion and in-editor playback do not prove a local file was saved. Verify the downloaded file before freezing it as downstream input; recover through the currently supported ChatCut export path when browser download stalls. Reuse existing cloud-upload/export authorization for the same material and destination rather than asking again.

## 3. Create the edit decision list

Convert the cleaned transcript into one shared, time-based manifest. Use milliseconds for interchange and derive frames only inside Remotion.

```json
{
  "version": 1,
  "fps": 30,
  "canvas": {"width": 1920, "height": 1080},
  "aRoll": "media/clean-aroll.mp4",
  "captions": [{"id":"cap-001","startMs":0,"endMs":1680,"text":"已经有 100 万个 Skills","emphasis":[{"text":"100 万个","colorRole":"data","treatment":"marker"}]}],
  "scenes": [{
    "id":"scene-001","startMs":0,"endMs":3200,"purpose":"hook",
    "spokenText":"已经有 100 万个 Skills",
    "visualBrief":"100 万个作为证据主数字，与字幕数据使用同一强调色",
    "mode":"overlay","protect":["face","mouth","captions"]
  }]
}
```

Require stable IDs. Use half-open intervals `[startMs, endMs)` and a single formula in Remotion: `frame = round(ms * fps / 1000)`. Prevent cumulative drift by converting absolute timestamps, never by adding rounded scene durations.

## 4. Split the copy into visual scenes

Create a new scene only when the viewer's mental model changes: hook, claim, evidence, comparison, process step, example, objection, conclusion, or call to action. Do not turn every caption page into a scene.

For each scene, define:

- purpose and exact time range;
- the single idea the visual must clarify;
- treatment: transparent overlay, side card, full-screen information beat, diagram, number emphasis, or no extra graphic;
- protected regions and caption-safe area;
- entrance, emphasis, and exit/transition intent;
- asset/output contract for Remotion.

For classic, keep the moving full-frame A-roll and its original background visible throughout. Information cards, screenshots, photographs, comparisons, and diagrams are floating overlays only: no full-screen replacements, opaque full-canvas panels, dark explainer canvases, or shrinking the speaker into PiP. Place compact graphics in verified free regions without covering the face, mouth, gestures, or captions. If content will not fit legibly, extract the relevant screenshot detail, simplify, split into sequential cards, or omit it; do not cover the footage to make room. Record classic graphic scenes as `mode: overlay` in the EDL. A user-requested full-screen exception must be explicit, not inferred from information density.

Also assign one narrative mode; full-frame Explainer treatment below applies to premium-v2 only. In classic, explanation remains a floating overlay over full-frame A-roll:

- **A-roll mode:** keep the speaker full-frame for claims, emotion, rhetorical questions, transitions, and breathing room;
- **Explainer mode:** use a full-frame visual explanation for relationships, mechanisms, timelines, comparisons, archival evidence, or data, while retaining the speaker in a small circular picture-in-picture when it helps continuity;
- **Emphasis mode:** stay on A-roll but introduce one oversized keyword or short conclusion for less than a full explanation beat.

Alternate modes by meaning, not on a timer. Enter Explainer mode when the spoken idea would be easier to understand as a spatial model; return to A-roll after the explanation resolves so the video does not become a continuous slide deck.

Keep the speaker dominant. Avoid repeating the same sentence simultaneously in captions and an information card. Use graphics for structure, evidence, comparison, or memory anchors.

Map each beat to the house visual grammar instead of inventing a new treatment every time:

- **Claim:** a short editorial headline with one signal-marked phrase;
- **Evidence:** a compact evidence card with source/context label and one dominant datum;
- **Comparison:** two aligned fields with a single highlighted difference;
- **Process:** numbered index chips connected by a restrained directional cue;
- **Definition:** keyword, plain-language explanation, then one example;
- **Conclusion:** return to the opening visual motif and reduce the frame to one takeaway.

Adapt information-card geometry to the actual source composition. For a centered speaker in a 16:9 shot, prefer a compact card in a verified low-information side region instead of a large centered panel. Preserve the face, head, mouth, shoulders, and bottom caption band. Reposition and proportionally resize existing cards after any canvas change; do not assume portrait placements remain valid in landscape.

## 5. Build visuals in HyperFrames

Before building visuals that use supplementary video, complete the sourcing, inspection, download, and trim workflow in [B-roll sourcing](references/broll-sourcing.md). Link accepted local assets and their source ranges to the frozen EDL; classic uses floating video cards only, while premium-v2 may integrate footage into explanation scenes.

Read `references/style-system.md` and create a project `DESIGN.md`, optionally from `assets/DESIGN.template.md`, before composition HTML. Include the Matching Cover plan; video style decisions alone do not satisfy the cover brief. For classic, start from `Clear Signal Editorial / 清晰证据流`; for premium-v2, apply references/premium-v2.md and, for the colorful variant, references/premium-colorful.md to the visual decisions in steps 4–6. Follow the HyperFrames visual identity gate.

Build the fully visible hero frame before animation. Use transparent backgrounds outside floating cards; opaque card surfaces are allowed within the bounded card only. In classic, export bounded overlays only and never an opaque full-frame visual asset. Premium-v2 may use opaque backgrounds for intentional full-screen beats. Keep each overlay's canvas tightly bounded to its content; use full-frame dimensions only for premium-v2 full-screen scenes.

Preserve the house signatures across the video: ink-and-paper contrast, controlled semantic color emphasis, squared editorial cards, index chips, evidence rules, restrained depth, and decisive settle motion. Use deterministic GSAP timelines and no wall-clock or random behavior.

For premium-v2 full-frame explainers, use the default circular-speaker treatment and exception criteria in references/premium-v2.md. Classic keeps the original full-frame speaker instead of PiP. Prefer relationship maps, loop diagrams, archival-image cards, and simple comparison bars over generic icon grids.

Export visual units with stable scene IDs and transparent alpha when required. Record each asset's path, intrinsic size, start/end time, placement intent, and whether Remotion should treat it as overlay or full-screen media. HyperFrames animation stays inside the asset; Remotion controls only its placement and lifetime.

Run HyperFrames lint, validation, inspection, and representative hero-frame checks before integration.

## 6. Assemble the canonical timeline in Remotion

Create or reuse a Remotion project and make the manifest the composition input. Keep timing, content, theme tokens, and component code separate.

Use this layer order unless the shot requires otherwise:

1. background/matte;
2. cleaned A-roll video;
3. HyperFrames visual assets: floating overlays only in classic; full-screen or overlay in premium-v2;
4. synchronized circular speaker PiP for premium-v2 explanation scenes when used;
5. captions and keyword emphasis;
6. persistent identity marks or progress UI;
7. optional sound effects and music.

Use Remotion `Sequence`/series structures for scene boundaries and one master FPS/canvas. Do not recreate HyperFrames internals in Remotion. Do not trim the A-roll to make a graphic fit. Keep video playback muted when a dedicated extracted audio track is used, and avoid double audio.

Group captions into semantic pages, generally 1.2–2.5 seconds, 8–18 Chinese characters per line, and at most two lines. Keep numbers with units and fixed phrases indivisible. Use the multicolor semantic palette and caption/data-highlight rules in `references/style-system.md` for both captions and HyperFrames cards. Highlight important spoken quantities, percentages, prices, dates, and before/after values as readable spans; preserve their qualifiers and units. Store emphasis text, color role, and treatment beside the caption timing and render those spans in Remotion. Emphasize one primary phrase per page by default; a necessary before/after comparison may highlight the paired values. Verify actual colored output rather than leaving emphasis only in the design brief.

## 7. Validate the integrated result

Read `references/quality-checklist.md`. Validate structurally and visually at the hook, each scene boundary, every full-screen beat, dense caption moments, and the ending.

Confirm:

- the final speech matches the cleaned ChatCut timeline exactly;
- captions align with audible words and contain no deleted speech;
- HyperFrames assets begin and end on the intended semantic beats;
- face, mouth, gestures, captions, and important source objects remain unobstructed;
- no alpha matte, blank frame, overflow, orphaned unit, awkward wrap, or duplicated information appears;
- final canvas and framing match the display-conformed source; no crop, reframe, aspect-ratio conversion, face stretch, or body compression was introduced except the authorized localized premium-v2 PiP mask or an explicitly requested separate derivative;
- every final A-roll item references a delivery-grade source at or above the intended output resolution; no low-resolution preview proxy is being upscaled in the master;
- final duration, resolution, FPS, audio, codec, and color tags match delivery requirements.

Do not validate clarity from export settings alone. Inspect the current timeline structure, then render and visually inspect representative composed frames at original detail. Compare facial texture, hair, glasses, text edges, and background seams with matching source frames. Check the hook, at least one ordinary speaking frame, dense information-card moments, a late cut, and the ending. Only submit the final export after both structural and pixel-level verification pass.

When exposure differs, measure source -> cleaned intermediate -> final. Do not blame Remotion overlays if the shift was already baked into the cleaned intermediate.

## 8. Create the matching cover

After the cut is final, select a clean frame from the actual A-roll where the user's face is sharp, eyes are open, and the expression or gesture supports the topic. Prefer a frame without baked-in captions or information cards. Follow the matching-cover guidance and revised reference in `references/style-system.md`: scale/reposition the person to leave a visible gap between the headline and the complete hair silhouette; for technology topics, use a restrained technology background with relevant brand elements. Retain the selected frame and timestamp and create one finished cover with a short, large headline. Inspect the result at thumbnail size for legibility, likeness, full-head clearance, accurate brands, and truthful relationship symbols. A cover crop is a separate image asset and does not change the video's source-ratio master.

Before creating the cover, visually inspect the saved cover reference and selected source frame, then complete the cover plan in DESIGN.md using the plan → production → acceptance procedure in `references/style-system.md`. Black-gold video packaging does not authorize replacing the established cover treatment with a black background and large indoor screenshot. Before delivery, record each applicable Cover acceptance check from `references/quality-checklist.md` against the actual final image. Resolve failed checks before declaring completion; dimensions, a clear face, a successful generation, or greater resemblance to the reference alone do not establish acceptance. Apply the same checks to revisions without introducing a routine user-approval checkpoint.

## Deliverables

For full packaging, return:

- final MP4;
- one matching screenshot-led cover image, plus its selected source frame/timestamp and editable title/layout when available;
- editable Remotion project;
- cleaned ChatCut project or cleaned A-roll export;
- corrected caption data;
- scene/EDL manifest;
- HyperFrames visual sources and rendered assets;
- a concise validation summary.

For diagnosis-only work, return the evidence-backed cause, the stage where it appeared, prioritized fixes, additional packaging advice, and explicit confirmation that no video was regenerated.
