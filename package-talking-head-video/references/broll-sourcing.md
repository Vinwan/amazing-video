# Supplementary footage / B-roll

Use this after ChatCut speech cleanup and timing freeze, before HyperFrames visual production. Start with ChatCut `search_stock_media`; do not install a new downloader or start paid generation automatically.

## User-approved premium default — AIHack V2

Approved on 2026-11-01 as the default for future “精剪视频”. Reference delivery: `/Users/will/Documents/one person company/video-package-aihack/AIHack-黑金精剪-画面优化版.mp4`; source decisions and timings: that project's `broll-manifest.json` and `revision-broll/edl-v2.json`. Apply its editorial approach, not its exact clips, four-shot count, or timestamps.

- Use relevant real footage for visible actions and concrete scenes; retain diagrams for abstract relationships, branching, model fallback, and value comparisons. Avoid making every explanation the same text-card stack.
- Cut to footage at the phrase that introduces the action. Reveal supporting information at the corresponding spoken detail, hold for reading, and return to the presenter when interpretation or advice carries the beat. Do not apply a fixed stagger or interval across unrelated scenes.
- Keep the established full-frame presenter/title opening, synchronized circular presenter during explanation, full-frame returns, black-gold default, semantic highlights/SFX, and matching cover.
- Prefer actual operation footage over generic locks, code rain, hacker silhouettes, or unrelated office activity. If the precise interface is unavailable, combine relevant real activity with a clearly labeled illustrative interface; record the limitation. Never present stock as the named malware's actual execution or as a confirmed victim.

Before visual production, save each useful footage need with its spoken phrase, absolute timeline range, intended action, search outcome, and selected treatment. Search promising needs; when none fit, record why A-roll or a diagram is preferable. Before delivery, check this record and the composed excerpts as well as technical quality. A package without accepted footage must have an explicit editorial or access reason; silent omission of this planning/search stage is not the default.

## 1. Plan needs from the frozen speech

For each useful footage beat, record scene ID, exact spoken phrase, timeline start/end in milliseconds, what the viewer should see, and whether it is factual evidence or generic illustration. Do not add stock merely to fill silence or decorate every sentence. Preserve supplied and approved footage before searching for substitutes.

Specific products, model versions, people, companies, or events require verified matching footage to serve as evidence. Generic stock can illustrate a concept but cannot establish that a named company owns the depicted facility or that a product has the depicted capability.

## 2. Search candidates

Discover the live `search_stock_media` schema before calling it. Use `kind: video`, initially Pexels/Pixabay, and orientation appropriate to the intended card or scene. Turn abstract Chinese concepts into concrete visual search phrases, including English alternatives when useful: subject + visible action + setting. Search a small candidate set and refine based on actual results rather than downloading everything.

Read each candidate's title, description, tags, page URL, license, and attribution fields. Returned metadata and thumbnails are leads, not proof of clip content or usage rights. Stock search need not find a named product's official demonstration; if none is suitable, report the gap and retain A-roll or a diagram rather than substituting a false match. Official footage or self-recording can be proposed as a separate source path.

## 3. Inspect content and source

Review the actual preview when available, including the intended action and beginning/middle/end of the proposed excerpt. Confirm identity, version/context where relevant, visible action, quality, watermarks, and whether a misleading association would result. Verify provider usage terms for the intended use and retain the license URL, attribution requirement, and check date. Missing or unclear rights do not become permission merely because a download URL exists; exclude the candidate until resolved.

If preview access is insufficient, make a permitted inspection download, inspect it locally, and only then accept the clip. Do not claim visual verification from a title, thumbnail, or inaccessible preview.

## 4. Download, verify, and trim

Use the selected result's current download URL and suggested filename. Save within the project's media directory, not inside this Skill. Verify a complete decodable file, duration, dimensions, frame rate, orientation, and the actual selected excerpt. Load the applicable ChatCut asset-import skill before importing into ChatCut. Local Remotion assembly requires a verified local asset; a remote asset card alone is insufficient.

Keep the downloaded original and create a separate excerpt when needed. Record source in/out independently of placement on the frozen speech timeline. Preserve aspect ratio; default to contain within the card or scene, without stretching. Do not crop or retime A-roll to accommodate footage. Prefer selecting a shorter appropriate excerpt over unexplained looping, reversal, or speed changes. Stock sound is muted by default; deliberate source sound must not duplicate or overwhelm the dialogue.

## 5. Package and assemble

- Narrative-v3: follow [v3.0](narrative-v3.md) for presenter, footage and diagram alternation. Full-frame footage is allowed; PiP is optional by narrative value, not required for every explanation. Keep shared sourcing, rights, timing and audio checks below.

- Classic: a bounded floating video card over continuous full-frame presenter and original background. Never turn the card into a full-screen replacement or shrink the presenter into PiP. Protect face, gestures, and captions; simplify or omit the card if there is no readable safe placement.
- Premium-v2: footage may occupy an explanation scene with synchronized circular presenter PiP and planned full-frame presenter returns. Retain the selected black-gold or colorful identity.
- HyperFrames owns card geometry, labels, transitions, and internal graphic animation. Remotion owns final placement, source offsets, duration, and audio routing. If HyperFrames renders video into an asset, record the baked source range and do not apply that trim twice. Otherwise use the same EDL ranges for Remotion's video layer and the HyperFrames frame/overlay.
- Fetch media before rendering; final renders use local verified assets rather than expiring search URLs.

## Source ledger and acceptance

Keep a project `broll-manifest.json` linked from the EDL, with each accepted clip's ID, scene ID, spoken phrase, evidence/illustration role, provider and provider asset ID, source page URL, license URL and check date, attribution text when required, original/local excerpt paths, source in/out, timeline start/end, dimensions, fit/placement, and audio treatment. Record any identity or access limitation instead of inventing metadata.

Before delivery inspect the actual composed excerpt, entry, and exit: it matches the narration, retains readable detail and correct identity, respects the mode's presenter treatment, does not imply unsupported facts, and leaves captions unobstructed. Include the source ledger and required credits with the project. Never claim that technical download success proves editorial suitability or permission.
