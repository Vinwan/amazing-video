# Premium 2.0 — visual journey

Use for “精剪视频”, “优美视频”, or an explicit 2.0 request. Keep classic behavior available under its existing triggers.

## Approved sample and evidence

- Creator: Yona呀. Title: 跟着一笔20美元的AI会员费，走完整个产业链.
- User link: https://v.douyin.com/q_pnuT5mEn4/
- Resolved page: https://www.douyin.com/video/7698318890425683251
- Reviewed on 2026-10-23 by sampling visible player frames across the approximately 6:07 video. Times below are approximate; this is a visual sampling analysis, not a frame-by-frame or audio analysis.
- Around 0:05–0:30: dark warm canvas, company nodes, a bright focal point, large two-line journey title, company-card bands framing it.
- Around 1:00: chapter capsule and a single large light company card.
- Around 1:31–2:13: branching gold paths, company nodes, dimmed infrastructure imagery, selected-node emphasis.
- Around 3:06–4:11: vertically connected supply-chain cards, camera following the relevant region, side-number annotations, chip and memory branches.
- Around 5:29–5:33: a light quantitative chart over a subdued map, then a container/flow metaphor for a cycle.
- Recurring appearance: near-black warm background, cream text, muted gold paths, rounded panels, restrained depth, bold compact lower captions. No talking-head picture-in-picture was visible in the sampled explainer frames.

Do not inherit the sample's financial claims or numerical values. Verify the current project's facts and source labels independently. Sound design and exact transition timing were not verified from these samples; the recommendations below are production choices.

## Narrative approach

Choose a concrete thread that can carry the viewer through the topic: a payment, request, document, user action, object, or decision. Establish its starting point, follow meaningful stages, and end with the whole system or consequence. Use this only when supported by the script; for non-linear topics, use a causal map or comparison with the same visual language.

Build this version as a hybrid talking-head film with visual explanations. Use the frozen human speech throughout, and plan meaningful full-frame appearances of the actual speaker. The reference supplies the visual-journey grammar; this user's delivery also requires real on-camera presence. A small picture-in-picture alone does not satisfy that requirement.

## Speaker presence and pacing

Choose shot changes from the transcript's argument and the speaker's recorded expression/gesture. Mark the following opportunities before authoring graphics:

- **Opening:** follow [opening rules](opening.md): moving full-frame A-roll with a prominent centered title from frame one. Keep the face and caption lane clear, then enter the explanation at a semantic beat. Graphics-only opening requires an explicit request.
- **Key judgment:** return to full-frame A-roll for a personal interpretation, surprising conclusion, rhetorical question, or emotionally delivered line. Let a simple caption or keyword support the performance.
- **Chapter handoff:** use the speaker to summarize the previous mechanism and pose the next question when that creates a natural transition.
- **Breathing room:** after a dense chain, return to a complete spoken thought on camera so viewers can absorb the information. Do not interrupt an unfinished diagram solely to show a face.
- **Ending:** normally show the speaker delivering the final takeaway or action, with a brief map recap before or beside that beat when helpful.

Use `speaker -> explanation -> speaker interpretation -> next explanation -> speaker close` as a starting rhythm, not a fixed shot sequence. Keep full-frame explanation where viewers need to follow a mechanism, and hold the speaker where their expression or argument carries the beat. Do not impose a fixed appearance percentage or cut every N seconds. Very short videos may combine opening, judgment, and close; do not add redundant returns to fill a quota.

Before rendering, review any long graphics-only passage for a suitable speaker return at its next semantic boundary. Keep an uninterrupted explanation when breaking it would harm comprehension, and record that scene's purpose in the EDL. Speaker appearances should last for a readable, complete thought rather than flash as one-second inserts.

Keep A-roll returns synchronized to the corresponding passage of the frozen cleaned source. Continue the same speech across visual switches without replaying, replacing, or retiming words. Preserve the existing source framing and natural skin color; do not force the dark/gold graphic palette onto the real footage. During explanation sections, default to a smaller circular picture-in-picture of the actual speaker over the explanatory background, following the layout contract below. Retain full-frame speaker beats.

Stock-video scenes are an exception: show only the stock footage, with no actual-presenter layer or circular PiP. Preserve the narration and ordinary captions; record `pip: false` in the EDL and verify entries/exits for presenter leakage. The circular treatment below applies to non-stock explanation backgrounds.

## Circular speaker over explanation backgrounds

For future premium-v2 videos, use the actual cleaned speaker in a circular picture-in-picture while the background shows the content being explained: product screenshots, evidence, diagrams, comparisons, or demonstrations. This is the user-approved default for explanation beats, not a requirement inherited from the reference sample. Keep opening, key judgments, and ending on full-frame A-roll when their performance carries the argument. Do not retroactively revise an already approved delivery unless requested.

- HyperFrames authors the explanation background and reserves a safe region for the circle. Remotion composites the synchronized speaker above that background and below captions. Keep one authoritative dialogue audio stream; mute duplicate video layers.
- Use the corresponding absolute time in the frozen cleaned A-roll. An explanation's circle must show the same spoken moment, with no restarted clip, lip-sync drift, or timing changes.
- Keep the circle large enough for the face, glasses, and expression to remain recognizable on a phone. Choose its corner and size from each scene's evidence layout; avoid captions, numbers, source labels, and the active diagram path. Keep its position stable within a beat and move at semantic boundaries when needed.
- Preserve natural proportions and color. Prefer a proportionally contained source inside a circular frame; when the face would be too small, a face-centered circular mask may hide surrounding background/torso. This localized PiP mask is authorized for this treatment; it does not authorize cropping full-frame returns, changing the master aspect ratio, stretching the person, or generating a replacement face.
- Use a restrained border that separates the person from the background. Avoid bouncing, pulsing, or decorative effects on the circle. If no readable safe placement exists, first rearrange the background; omit the circle for that beat only when necessary to keep evidence readable, and record the reason.
- Record each hybrid scene's PiP visibility, position, diameter, framing, and any exception in the EDL. Inspect both circle/background composition and transitions at final resolution and phone size, including mouth sync and caption clearance.

## Scene and camera design

- Build one coherent world/map for a connected explanation, with stable node IDs and positions. Reuse it across scenes rather than replacing every sentence with an unrelated slide.
- Alternate overview -> current stage -> local evidence -> next connection -> final overview. Mark chapters with a compact stage capsule and a short label.
- Guide attention through camera pan/zoom along the active path. Settle before introducing the main text; keep the current node and its immediate context readable.
- Reveal nodes and connectors in narration order. Dim inactive branches, illuminate the selected path, and reserve a moving token or pulse for a meaningful transfer.
- Use close views for important quantities and light evidence/chart panels; restore context after each detail.
- Animate the graphic world's camera only. Do not crop or distort A-roll, change the source-ratio master, or stretch source footage to match the sample.
- Avoid constant camera movement. Leave stable holds for reading, then move at a semantic handoff. Exact timing follows the speech and information density.

## Visual identity

- Base: warm near-black `#12110C`; text: cream `#F5F0DE`; path/accent: muted gold `#C7A65E`; selected light panel: `#FFF9EC`.
- Use restrained gold edge light and soft depth on active paths/cards; avoid flashing glows or decorative particles. Authentic brands retain their own colors. A second semantic color may distinguish a genuinely different flow.
- Cards share a consistent radius, border, spacing, and typography. Use high-contrast light cards for the current major subject and quieter dark cards for context.
- Use subdued relevant photographs or textures behind infrastructure/evidence beats. Keep them subordinate to diagrams and text.
- Use bold, compact sans-serif titles and lower captions. A slight oblique display treatment is optional if Chinese glyphs remain clear; readability takes priority.
- Keep the ordinary caption lane stable. Use side annotations for values and units, stage labels for structure, and chart panels for evidence. Avoid repeating the entire caption in the diagram.
- Adapt the opening to this palette. The separate cover follows [cover rules](cover.md), not the video's black-gold title-card treatment. Create topic-specific assets and compositions.

## Production handoff

ChatCut finalizes speech and captions as before. HyperFrames owns the map, node reveals, graphic camera, depth, and visual scene assets. Remotion owns master sequences, caption rendering, A-roll returns, and the final mix/render; do not animate the same map camera in both engines.

Assign each EDL scene a `presentation` of `speaker`, `explainer`, or `hybrid`, with a brief `beatReason` describing its narrative role. Extend map scenes with `worldId`, `focusNodeId`, `cameraIntent`, and `transitionIntent`; keep their absolute speech timestamps. Record speaker-return beats and palette/component choices in DESIGN.md. Apply the user's [approved finishing](premium-finishing.md) for semantic SFX, caption emphasis, and small explanatory animations. Music remains optional; do not describe this sound treatment as observed in the Yona sample.

## Version-specific review

- Follow the same thread from start to finish; every path has an understandable relationship/direction.
- Check overview, detail, and camera-transition frames: captions remain fixed/readable; no nodes clip accidentally; the current stage retains context.
- Verify important numbers, units, dates, and source labels against the project's evidence. If path width represents quantity, scale it from data; otherwise declare it illustrative and avoid implying numerical precision.
- Keep the active path distinct and inactive content quiet; provide reading holds.
- Verify meaningful full-frame speaker presence in the opening section, selected interpretation/transition beats, and normally the closing takeaway. Combine these roles for short videos where appropriate.
- Review graphics-only stretches for reading fatigue and speaker-return opportunities; each return follows a complete thought, shows the matching real performance, and preserves uninterrupted audio/lip sync.
- Confirm that extended graphics are intentional in premium-v2, while classic requests still use the established workflow.
