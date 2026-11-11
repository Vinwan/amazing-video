# Supplementary footage / B-roll

After ChatCut freezes speech, the agent working under the HyperFrames skill owns shot planning, B-roll briefs and editorial selection. Pixabay supplies candidates, not editorial decisions. Remotion places accepted media on the frozen timeline. Do not install a new downloader or start paid generation automatically.

## User-approved premium default — AIHack V2

Approved on 2026-11-01 as the default for future “精剪视频”. Reference delivery: `/Users/will/Documents/one person company/video-package-aihack/AIHack-黑金精剪-画面优化版.mp4`; source decisions and timings: that project's `broll-manifest.json` and `revision-broll/edl-v2.json`. Apply its editorial approach, not its exact clips, four-shot count, or timestamps.

- Use relevant real footage for visible actions and concrete scenes; retain diagrams for abstract relationships, branching, model fallback, and value comparisons. Avoid making every explanation the same text-card stack.
- Cut to footage at the phrase that introduces the action. Reveal supporting information at the corresponding spoken detail, hold for reading, and return to the presenter when interpretation or advice carries the beat. Do not apply a fixed stagger or interval across unrelated scenes.
- Use an official release, documentation image or product screen when the picture needs to substantiate a specific claim. When a generic office photo only illustrates a narrated activity or industry, prefer relevant moving footage with an observable action, such as someone reviewing financial records for a finance example. Record the footage as illustrative in the ledger.
- Keep the established full-frame presenter/title opening, synchronized circular presenter during explanation, full-frame returns, black-gold default, semantic highlights/SFX, and matching cover.
- Prefer actual operation footage over generic locks, code rain, hacker silhouettes, or unrelated office activity. If the precise interface is unavailable, combine relevant real activity with a clearly labeled illustrative interface; record the limitation. Never present stock as the named malware's actual execution or as a confirmed victim.

Before visual production, save each useful footage need with its spoken phrase, absolute timeline range, intended action, search outcome, and selected treatment. Search promising needs; when none fit, record why A-roll or a diagram is preferable. Before delivery, check this record and the composed excerpts as well as technical quality. A package without accepted footage must have an explicit editorial or access reason; silent omission of this planning/search stage is not the default.

## 1. Plan needs from the frozen speech

Prefer visual variety within each video: search for distinct Pixabay asset IDs rather than repeating a selected clip. Another trim, crop or rendition of the same provider asset ID still counts as reuse. Reuse only for a deliberate callback or when suitable alternatives are unavailable; record the reason and repeated placements in the source ledger. This is a preference, not a clip quota or a ban on reusing assets across different projects.

For each useful footage beat, record scene ID, exact spoken phrase, timeline start/end in milliseconds, what the viewer should see, and whether it is factual evidence or generic illustration. Do not add stock merely to fill silence or decorate every sentence. Preserve supplied and approved footage before searching for substitutes.

Specific products, model versions, people, companies, or events require verified matching footage to serve as evidence. Generic stock can illustrate a concept but cannot establish that a named company owns the depicted facility or that a product has the depicted capability.

## 2. Search candidates

Search Pixabay first. Use the [Pixabay video API](https://pixabay.com/api/docs/#api_search_videos) at `https://pixabay.com/api/videos/` when `PIXABAY_API_KEY` is available from the local secret environment. Send the key only to this official HTTPS endpoint; never write it into the Skill, GitHub, logs, manifests, browser history, or command arguments. Use URL-encoded `q`, a small `per_page` (start at 5), and inspect rendition width/height for orientation. Save only non-secret fields such as asset ID, source page and rendition metadata. If the direct API is unavailable, use ChatCut `search_stock_media` scoped to Pixabay when available, without passing the personal key to ChatCut. If neither path works, report the limitation and use verified existing media, A-roll or a diagram.

Translate each shot brief into concrete searches: subject + visible action + setting. Judge candidates from actual footage against the brief, not title or thumbnail alone. Keep the set small; refine only if needed.

Read each candidate's title, description, tags, page URL, license, and attribution fields. Returned metadata and thumbnails are leads, not proof of clip content or usage rights. Stock search need not find a named product's official demonstration; if none is suitable, report the gap and retain A-roll or a diagram rather than substituting a false match. Official footage or self-recording can be proposed as a separate source path.

## 3. Inspect content and source

Review the actual preview when available, including the intended action and beginning/middle/end of the proposed excerpt. Confirm identity, version/context where relevant, visible action, quality, watermarks, and whether a misleading association would result. Verify provider usage terms for the intended use and retain the license URL, attribution requirement, and check date. Missing or unclear rights do not become permission merely because a download URL exists; exclude the candidate until resolved.

If preview access is insufficient, make a permitted inspection download, inspect it locally, and only then accept the clip. Do not claim visual verification from a title, thumbnail, or inaccessible preview.

## 4. Download, verify, and trim

Use the selected result's current download URL and suggested filename. Save within the project's media directory, not inside this Skill. Verify a complete decodable file, duration, dimensions, frame rate, orientation, and the actual selected excerpt. Load the applicable ChatCut asset-import skill before importing into ChatCut. Local Remotion assembly requires a verified local asset; a remote asset card alone is insufficient.

Select the highest-quality useful available rendition; do not default to the smallest version whose width happens to meet the canvas. Follow [source fidelity](source-fidelity.md) for any delivery-size conversion.

Keep the downloaded original and create a separate excerpt when needed. Record source in/out independently of placement on the frozen speech timeline. Preserve aspect ratio; default to contain within the card or scene, without stretching. Do not crop or retime A-roll to accommodate footage. Prefer selecting a shorter appropriate excerpt over unexplained looping, reversal, or speed changes. Stock sound is muted by default; deliberate source sound must not duplicate or overwhelm the dialogue.

## 5. Package and assemble


- Both modes: when stock video plays, show the footage directly, filling the master canvas with its aspect ratio preserved (`contain` as needed), with no actual-presenter background, cutout or PiP visible. Use an opaque backing so letterbox regions do not reveal the presenter. Continue the same narration and ordinary captions; stock audio stays muted unless deliberately selected. End the stock scene before returning to the presenter.
- This is the user-approved stock-footage exception to classic continuous A-roll; other classic information cards remain bounded overlays. Premium diagram-only explanations retain their synchronized circular presenter default.
- HyperFrames owns card geometry, labels, transitions, and internal graphic animation. Remotion owns final placement, source offsets, duration, and audio routing. If HyperFrames renders video into an asset, record the baked source range and do not apply that trim twice. Otherwise use the same EDL ranges for Remotion's video layer and the HyperFrames frame/overlay.
- Fetch media before rendering; final renders use local verified assets rather than expiring search URLs.
- Keep stock scenes clean by default. Do not automatically overlay “示意”, “情景示意”, “概念示意”, footage-category chips, or similar labels in the upper left, upper right, or another corner. Ordinary speech captions remain. Store illustration status, limitations and attribution in `broll-manifest.json` and the credits/source document. Add an on-screen identifier only when the user requests it, a selected asset requires visible attribution, or a specific factual claim would otherwise mislead; prefer a more suitable asset or clear narration over a generic corner disclaimer. Never imply that generic stock is actual historical/event footage.

## Source ledger and acceptance

Keep a project `broll-manifest.json` linked from the EDL, with each accepted clip's ID, scene ID, spoken phrase, evidence/illustration role, provider and provider asset ID, source page URL, license URL and check date, attribution text when required, original/local excerpt paths, source in/out, timeline start/end, dimensions, fit/placement, and audio treatment. Record any identity or access limitation instead of inventing metadata.

Before delivery group placements by provider and asset ID to detect repeats; verify that any retained repeat has a reason. Inspect stock entries, middles and exits to confirm no presenter is visible, including under letterbox regions or during a transition.

Before delivery inspect the actual composed excerpt, entry, and exit: it matches the narration, retains readable detail and correct identity, respects the mode's presenter treatment, does not imply unsupported facts, and leaves captions unobstructed. Include the source ledger and required credits with the project. Never claim that technical download success proves editorial suitability or permission.
