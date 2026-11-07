# Quality Checklist

## Editing version

- DESIGN.md and the EDL record classic or premium-v2 according to the user's wording; premium-v2 uses black-gold.
- Classic retains moving full-frame A-roll and the original background except for the user-approved stock-only video scenes in references/broll-sourcing.md. Every information card, screenshot, photograph, or diagram is a bounded floating overlay (`mode: overlay`); no full-screen replacement, opaque full-canvas panel, globally darkened/blurred explainer background, or presenter PiP is used without an explicit user exception. Inspect the densest graphic frame as well as entries and exits.
- Apply the house-style and human-reset checks below to classic. For premium-v2, use references/premium-v2.md for visual checks; shared fidelity, captions, export, and cover checks still apply.
- Premium-v2 includes meaningful full-frame appearances of the actual speaker, planned around the hook, judgments, breathing room, transitions, and close; picture-in-picture alone does not substitute for those beats. Verify the selected rhythm in the EDL and final playback without enforcing an arbitrary time ratio.

## Source and color

- Source metadata inspected before conversion.
- Display orientation resolved from rotation/display-matrix metadata, not encoded dimensions alone.
- Source canvas, full framing, and aspect ratio preserved through proxies, timeline layout, composition, and export.
- No crop, reframe, or aspect-ratio conversion performed except the localized premium-v2 PiP mask or an explicitly requested separate derivative; full-frame returns preserve the source framing.
- Speaker facial and body proportions and visible framing compared against the source after every canvas or proxy change.
- Timeline A-roll asset dimensions and readiness checked against the intended export resolution.
- Preview proxies clearly separated from delivery media; no reduced proxy is used in the final master when a higher-resolution source exists.
- High-resolution media bytes are remotely readable before cloud frame verification or export.
- HDR/SDR intent explicitly chosen.
- Display-conformed source, intermediate, and final compared at matching timestamps.
- Skin, highlights, and neutral background checked with scopes.
- Final color tags verified.
- Delivery uses the source-fidelity settings: lossless/visually lossless handoff, lossless frame capture, and a verified high-quality final encode. A clarity revision compares matching source/intermediate/final detail samples; source resolution limits are reported accurately.

## Transcript and captions

- Names, numbers, dates, and domain terms corrected.
- Empty/repeated/post-silence hallucinations removed.
- Caption pages follow speech and remain readable for their duration.
- No page exceeds two lines.
- Numbers and units do not split awkwardly.
- Caption JSON retained as the source of truth, including structured emphasis spans.
- Important spoken data is visibly highlighted in the final render, with qualifiers, values, and units preserved; ordinary words stay neutral.
- Multicolor caption highlights and cards share a consistent semantic color mapping; a necessary comparison may highlight two paired values.
- Selected foreground/background pairs pass contrast checks on actual footage, and highlights remain readable at phone size.

## Layout and motion

- Pixabay placements have been checked by provider asset ID for unnecessary repetition; a different trim of the same asset counts as reuse. Any deliberate repeat has a recorded reason.
- Every stock-video scene shows no actual presenter, including PiP, cutouts, underlying letterbox areas, and entry/exit overlaps. Narration may continue; stock scenes have `pip: false` in the EDL.
- Stock footage has no automatic corner “示意”/category labels. Inspect the actual composed excerpts, including both top corners; any requested or necessary exception is recorded. Source provenance remains in the ledger/credits.
- Background music follows the choice for this video; it is not inferred from a previous project or from the SFX default.
- Premium-v2 footage needs were assessed before visual production: concrete actions considered for real footage, abstract mechanisms for diagrams; search outcomes and omission reasons recorded. Accepted clips have a linked `broll-manifest.json`, verified sources/excerpts, and narration-matched entries/exits. An all-diagram treatment is a reasoned choice, not a skipped sourcing stage.

- Clear Signal Editorial remains recognizable: Ink/Paper reading surfaces, controlled multicolor semantic emphasis, editorial cards, evidence markers or index chips, and decisive settle motion.
- External creator styling has not replaced the house typography, palette, geometry, caption semantics, or motion grammar.
- Important text stays inside the platform safe area.
- No graphic covers the speaker's eyes or mouth.
- Hook, caption, data card, and CTA do not compete.
- Default opening shows the actual speaker's full-frame moving A-roll plus a large centered headline from the first frame. Inspect title entry, hold and exit at phone size: the face, mouth, complete head and separate caption lane remain clear; no still portrait, circular PiP, or graphics-only card substitutes for the live opening. Adapt placement below the chin when needed rather than reducing the title to a narrow top strip.
- If the user explicitly requested an illustrated title instead, recognizable subjects and one supported visual relationship convey the topic alongside a short headline; logos remain accurate and artwork does not crowd the face or captions.
- Entrance animation is visible but shorter than the reading time.
- Camera punch-ins affect graphic assets only unless A-roll reframing is explicitly authorized; full-frame presenter framing remains intact.
- Representative frames inspected at hook, first data point, longest caption, steps, and CTA.
- Landscape information cards use verified low-information side regions and do not reuse oversized portrait placement.
- Every scene has one primary reading target; decorative motion and redundant cards have been removed.
- Selected accents mark decisive information or consistent categories; colored card panels and caption spans add variety without random rainbow coloring.
- A-roll, Explainer, and Emphasis modes switch at semantic boundaries rather than arbitrary intervals.
- Dense explanation clusters return to the full-frame speaker for interpretation or breathing room.
- Explainer mode presents one central relationship, loop, evidence image, or comparison instead of a generic collection of icons.
- Premium-v2 circular speaker picture-in-picture stays stable, remains recognizable, avoids evidence and captions, and matches the frozen speech with only one dialogue audio stream. Premium-v2 defaults to this treatment during explanations; any omission has a readability reason recorded in the EDL. Classic retains the full-frame speaker instead.
- Oversized emphasis copy is short, selective, and visually separate from the ordinary caption lane.
- Diagram nodes and connectors reveal in causal order; the explanation is not dumped onto the frame at once.

## Cover acceptance

Full packaging in classic, premium-v2, and premium-v2.1-experimental requires this check unless the user explicitly excludes the cover. Verify the local frame and timestamp, ImageGen output for new or redesigned covers, and saved generation prompt.

Record each applicable item below with pass/fail and brief visual evidence in the project's validation report; explain not-applicable items. Inspect the actual final image, not only the prompt or layout code. Resolve failures before declaring the cover complete, including after revisions. Do not replace this review with a single “size correct / face clear” summary.

- DESIGN.md contains the cover plan, including the inspected cover reference, source frame/time, headline, portrait placement, background, topic assets and supported relationships.
- The final image is compared beside the approved reference and source frame; the established cover composition has not been replaced by the video's black-gold styling, an oversized indoor screenshot, or a title-card layout unless explicitly requested.
- Source likeness is checked in the result: face, glasses, hair, clothing and expression remain faithful. Generated product illustrations are distinguishable from documentary product imagery.
- The chosen source frame has a calm, natural expression at thumbnail size, with open eyes and a relaxed mouth. Compare alternate frames before accepting a tense speaking expression.

- A matching screenshot-led cover is delivered with the video; the selected frame comes from this video's A-roll, the user's face is recognizable and unobscured, and the short title reads clearly at thumbnail size.
- The cover headline matches the video, its source frame/timestamp is saved, and any cover-only crop leaves the video master unchanged.
- The portrait is scaled/repositioned to leave a visible gap below the headline; the entire hair silhouette, ears, glasses, and face are clear of text, cards, glow, and title-background fades.
- The background color and setting fit the video's specific story. At phone-grid size, the main visual conveys the subject and the headline and face stay clear.
- Relevant company/product elements improve recognition and stay secondary to title and person; no unrelated logos are added as decoration. Names, logos, and proportions have been inspected.
- Contextual ecosystem brands are not presented as donors, partners, endorsers, owners, or compatible products without source support; any relationship symbol conveys the actual claim.
- The final cover has been checked at phone-grid thumbnail size for headline readability, likeness, and uncluttered brand placement; source frame, revision, and editable layout or prompt are retained.

## Audio and export

- Cleaned A-roll handoff is a complete, readable local file when local assembly requires it; a render status, preview, or download click alone is insufficient.
- Downloaded file identity, byte count when supplied, duration, dimensions, and audio match the frozen ChatCut timeline; partial downloads are not used downstream.
- Original dialogue remains synchronized.
- Audio is present once, without doubling or phase issues.
- Duration, resolution, frame rate, and codec verified after export.
- Export resolution is supported by equal-or-higher-resolution timeline media rather than proxy upscaling.
- Timeline structure re-read after any proxy-to-master replacement; every affected A-roll item points to the delivery-grade asset while preserving cuts and source offsets.
- Original-detail composed frames compared with matching source moments for facial texture, hair, glasses, text edges, and background seams.
- Full framework lint/layout/runtime checks pass.
- Final MP4 plays from beginning, middle, and end.
