# Ordered timeline and frame integrity

Read before freezing a local A-roll handoff and again when replacing/rendering it. Preserve the authoritative ChatCut edit, not merely its duration.

## Ordered occurrences, not a union

At constant FPS and unit speed, record each half-open clip as timeline `[start,end)` and source `[in,out)` in integer frames. Require contiguous timeline spans and `end-start == out-in`. Expected output frames are the **sum of ordered clip lengths**, not the number of unique source frames. Adjacent clips may legitimately share a source frame; reuse and source-time reordering are valid edits.

For example, source windows `[2533,2639)` then `[2638,2688)` need 156 output frames, including source frame 2638 twice. A union-based FFmpeg `select` expression emits only 155. Build/concatenate exact windows in playback order; do not sort by source time, merge overlaps or deduplicate frames.

Run `scripts/verify_frame_mapping.py --mapping aroll-mapping.json --video clean-aroll.mp4` for this simple mapping model. Each JSON row has integer `start`, `end`, `in`, `out`. It reports overlap/reuse as a diagnostic, checks contiguous spans and compares their sum against decoded video frame count. It does not prove pixel identity or audio sync. Speed changes, transitions, mixed FPS and other time transforms require an explicit supported mapping and separate validation; do not force them into this model.

## Validate independently

- Verify actual decoded **video** frames, FPS and duration, separately from container/audio duration. A longer audio stream can hide a short video stream. Decode the entire final file for corruption as well.
- Compare mapped source/handoff/final frames before and after risky overlap, reuse or reorder boundaries, then later and near the tail. Inspect lips, face and full framing; compare audio against the final mix separately. Identical audio correlation alone cannot establish picture sync.
- Use absolute timestamps with the shared FPS conversion, not sums of rounded durations. Keep the frame mapping alongside the EDL.
- Find the first divergence and repair the responsible handoff or mapping. Do not shorten the EDL, move captions, append an arbitrary last frame or retime speech to hide a missing frame. Regenerate affected downstream assets, replace all affected source references together and recheck.

## Render performance without changing the edit

Diagnose the bottleneck before building a huge full-resolution cache. Estimate disk needs, avoid repeatedly copying large media into bundles and reuse one supported browser instance for batch frame captures where available. Verify the current framework's behavior; a null public-directory setting may fall back to its default rather than disable copying. Dependent rendering waits for all required cache frames, dimensions and decoding to be verified.

If the intended final renderer is impractically slow, explain the alternate assembly route and record it in project documentation. A local native compositor may assemble the **same frozen EDL**, lossless HyperFrames frames/alpha, original-quality A-roll, captions and final mix without changing speech or reimplementing animation. Retain the editable Remotion timeline and validate actual final pixels, source offsets, frame count, alpha, color and audio. This is an assembly fallback, not permission to bypass unavailable-tool or upload rules. Never report that Remotion rendered a file produced by another path.
