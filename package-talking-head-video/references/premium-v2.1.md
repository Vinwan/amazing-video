# 精剪视频 — validated Premium 2.1

Status: validated and promoted by the user on 2026-11-11. This is the default for “精剪视频”, “精剪版”, “优美视频”, and “精剪视频2.1”. New projects record `editMode: premium-v2.1`. Inherit [black-gold foundations](premium-v2.md) for palette, narrative rhythm and complex explanation canvases. The density and layout rules here govern sparse information over the full-frame speaker.

## What the supplied references establish

The user supplied two screenshots of landscape talking-head videos displayed inside a portrait social app. In one, a large percentage and two short comparison bars sit to the speaker’s left, with supporting evidence at the right. In the other, milestone figures sit left and a supporting screenshot sits right, leaving the person as the main visual subject. The reusable idea is the spatial relationship: live person, original room, sparse evidence in available side space.

Use only that relationship. Keep this skill’s black-gold palette and semantic highlight colors. Do not copy the creator, exact typography, factual numbers, watermark, phone/app chrome, chapter bars or social controls. The attached screenshots are not redistributed with this reference. A portrait screenshot of a landscape video does not authorize a portrait master, letterboxing added for imitation, or a crop of the user’s video.

## Decide by information density and usable space

| Spoken content | Preferred 2.1 treatment |
| --- | --- |
| One fact, value, takeaway, or short label | One readable side annotation or compact card beside the full-frame speaker |
| One or two brief information cards or a short comparison | Place in a verified free region on one side, or on opposite sides if both remain clear; reveal sequentially when needed |
| A simple unbranched process, usually two or three short steps | Compact side flow with a real directional relationship, revealed with the narration |
| Dense text, detailed evidence, a complex mechanism/network, branching flow, or insufficient free space | Simplify or sequence first; if that still fails, use the inherited 2.0 explanation scene and record why |

Card count is a cue, not the decision by itself: two dense tables are not sparse; three tiny labels may still form one simple readable process. Do not shrink text, hide units, or squeeze a model into a narrow strip just to retain the side treatment.

## Information cards for key beats

Plan cards for consequential spoken numbers, short comparisons, and explanations that benefit from a visual cue. Keep the wording brief and reveal each item with the spoken point. Retain units, scope, and qualifiers that change the meaning, including whether a figure is an estimate or a forecast.

Use the approved dark translucent capsule: a thin luminous edge, soft highlight, and compact typography. A small circular icon can signal the subject. Use cream for the main text and the existing semantic accent colors for key values. Stagger related capsules when the narration introduces them one at a time.

These text cards explain the narration. First-mention product/person images follow the separate approval workflow below and display the approved image alone, including any original text in the image.

## First-mention product and person cards — required approval gate

During the initial storyboard, identify every named product/app and person in the narration and reserve a floating image-card beat only at each entity’s first spoken mention in the whole video. Merge full names, short names, aliases and alternate spellings that refer to the same entity. The second and every subsequent mention must not replay, re-enter or create another product/person introduction card; a new scene or chapter does not reset the first-mention count. Use the final retained speech to confirm the earliest occurrence after cleanup, rather than anchoring to a deleted take.

- Product/app: source a matching product image or interface image with its recognizable official logo/app icon. For a software product, a suitable official app icon/logo may itself be the image. Check the exact product/version; do not substitute a parent-company logo or an unrelated product merely because the names are similar.
- Person: source a verified photograph/portrait of that exact person. Resolve homonyms and spelling from the narration/context. Do not use a namesake, generic portrait, invented likeness, or AI reconstruction as a factual identity image.
- Prefer official product/brand sources and attributable, credible portrait sources. Inspect the actual downloaded candidate for identity, quality, watermark and rights information; a search thumbnail or title is not verification. Retain the source page, usable file and available attribution/license details.

Keep the plan in `entity-card-manifest.json`, referenced by the EDL. Each record identifies the entity and aliases, type (`product` or `person`), first spoken phrase and final start time, scene ID, exact selected local asset and source URL, any proposed display crop, and approval status (`proposed`, `awaiting-upload`, `approved`, `rejected`, or `waived-by-user`). Record the user message/decision and approved asset revision so a later change cannot silently inherit approval for a different image. Record any proposed display time differing from the first mention and any explicit timing/layout exception separately from image approval.

Before the storyboard advances to visual production, present a numbered preview/contact sheet of the actual selected images, with names, first-mention phrases/times, source links and intended card treatment. The user must confirm the image selections explicitly; batch confirmation is fine. A confident identity match, successful download, user upload, silence or elapsed time is not selection approval. An upload becomes approved only when the user explicitly chooses it for that entity (including an explicit instruction to use the uploaded file).

If a correct usable image cannot be found, identify the missing product/person and ask the user to upload an image. Use a host file/image picker if available, otherwise request an attachment in a normal message; a text-only question form cannot receive the file. Do not replace the missing image with a generic icon/portrait, omit the required card silently, or generate a substitute. Keep the storyboard provisional and record `awaiting-upload`.

Do not enter visual production or final timeline assembly until all required entities have approved assets or an explicit user waiver. Independent speech cleanup, source inspection and preparation may continue. This is a user-required approval step, overriding the inherited no-routine-approval default. When asking, explain that the selected 2.1 workflow requires image confirmation and link this reference; no repeated approval is needed for the same already-approved image. A replacement image, different identity/version or materially different crop needs renewed confirmation.

Place an approved card at the first spoken mention, beside the full-frame speaker using the layout rules below, and hold long enough to recognize the image and name. Preserve logo/icon shape, person likeness and image proportions; do not cover the face or captions. Plan these beats before stock/graphic placement. If the first mention would fall during stock footage, reserve a speaker-side introduction beat there rather than adding a card or presenter over the stock. If safe placement/readability is impossible, show the proposed alternative during storyboard confirmation instead of silently moving the introduction or retiming speech.

If the first mention occurs during the opening title, first adjust the title’s layout/timing to avoid competing with the first-mention card; do not automatically delay the card until the title exits. If no safe layout works, state the proposed timing/presentation exception in the preview and obtain the user’s explicit approval for that exception. Image approval alone does not approve a delay, omission or different presentation. Keep the true first-mention timestamp and the separately approved display plan in the manifest; do not retime speech to resolve the conflict.

## Layout and motion contract

- Use the matching moving full-frame cleaned A-roll and its original background. Do not shrink it into a circular/rectangular PiP, crop/reposition the person, generate a cutout, or pan the camera to manufacture empty space. Do not add a duplicate presenter circle over the full-frame speaker.
- Inspect source frames across the whole selected passage, including the widest gesture. Choose the clearest low-information region for each passage. Portrait footage can use open space above the presenter; landscape footage can use clear space to the left or right. Treat orientation as a starting point and verify the location against the actual composition throughout the card’s hold. Protect the complete head, eyes, mouth, meaningful gestures, products and the fixed caption lane.
- Information floats in local side regions with transparency outside its content. Use the existing cream/gold/data/risk colors and a restrained local Ink/Paper support when contrast needs it. No opaque full-canvas panel, global darkening/blur, or full-width card backdrop for a sparse beat.
- Make the evidence large enough to read on a phone while keeping the speaker recognizable and visually primary. A single number retains its qualifier and unit. Avoid duplicating the whole subtitle sentence in a second large heading.
- Prefer one coherent group and at most one or two brief cards visible together. For a short process, keep node identities and connector direction stable; introduce the current step at its spoken onset. If two-sided evidence crowds the person, reduce or sequence it.
- HyperFrames owns the bounded graphic and its internal reveal; Remotion places it over the uninterrupted A-roll. Export real alpha outside the graphic. For a transparent video, enable alpha-aware compositing in Remotion (for example `OffthreadVideo transparent`) and inspect the result for a black/opaque rectangle.
- Keep motion restrained: short settle entrance, stable reading hold, clear exit at the end of the thought. No drifting, constant pulsing, or decorative movement around the face. Sequence ordinary information cards around the opening title. Required first-mention cards follow their approved first-mention timing and layout above.

These rules apply only to information over the actual speaker. Stock-video scenes continue to show footage alone, with no actual presenter or side information cards. Keep the existing clean-footage/no-corner-label rule, prefer distinct Pixabay assets, and continue narration/captions as appropriate. Music remains a per-video choice. All source-fidelity, caption, tool-role and audio-sync rules still apply.

## Planning and handoff

Record root `editMode: premium-v2.1` in DESIGN.md and the EDL. Existing `premium-v2.1-experimental` projects retain their recorded mode during revisions unless migration is requested. Keep the existing `presentation` vocabulary: each selected side scene is `presentation: speaker`, `pip: false`, `mode: overlay`, with bounded asset dimensions/placement, protected regions and a short `beatReason`. The reason should identify both sparse content and the usable space. A complex fallback may use `presentation: hybrid` under inherited 2.0 rules; document the density/readability reason. Stock remains `presentation: explainer`, `pip: false` with no actual presenter. No new scene-presentation enum is required.

Example of a scene record, not fixed geometry:

```json
{
  "id": "one-fact",
  "startMs": 12000,
  "endMs": 17000,
  "presentation": "speaker",
  "mode": "overlay",
  "pip": false,
  "placement": {"side": "left", "verifiedFromSource": true},
  "protect": ["head", "face", "mouth", "gestures", "captions"],
  "beatReason": "One short fact; left side stays clear through the passage"
}
```

The final EDL must replace the planning placeholder with actual asset path, dimensions and pixel placement. Use the shared absolute millisecond/frame contract; do not retime speech for a card.

## Premium acceptance

Apply the shared technical, source, captions, sound and cover checklist. Verify sparse speaker-overlay scenes against this reference and complex explanation scenes against the inherited circle/readability rules. Accept `premium-v2.1` for new premium projects and recorded legacy modes for existing revisions.

- When applying the card layout to new footage, inspect representative single-fact, multi-card and simple-flow scenes before scaling the treatment across the video. Use only cases present in the script; do not invent extra content to fill a test quota.
- View actual composed entry, settled, widest-gesture, longest-text and exit frames at full size and phone size. The underlying moving person and room remain intact; there is no hidden face, gesture, caption collision, PiP duplicate or accidental full-frame black graphic layer.
- Read a value with its units/qualifiers, and follow the simple flow in narration order. If usable space is insufficient, simplify/sequence or use the recorded 2.0 fallback; do not solve it by cropping the speaker or reducing readability.
- Verify every stock interval still has no actual-presenter layer. Check diagram/stock/speaker transitions and audio continuity.
- Audit named products/people against `entity-card-manifest.json`: each first retained mention has its approved matching image card, a separately recorded user-approved timing/presentation exception, or an explicit user waiver. An exception still requires the image approval unless the user explicitly waived the card. Check the whole timeline by entity identity, including aliases: at most one introduction-card appearance per product/person, with no retrigger at the second or later mention. Verify the rendered logo/icon or portrait against the approved file/crop and display plan; no unapproved image or timing exception has entered the timeline.
- Record observed strengths/problems and any fallback in the project validation notes. Inspect actual composed footage for every project before marking its visual checks complete. Beyond the required entity-image confirmation above, do not add routine extra user approval checkpoints for an already authorized edit.

