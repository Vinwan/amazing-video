# Speech Cleanup

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

Export or otherwise provide Remotion with the cleaned A-roll and caption timing. For a local Remotion workflow, read [A-roll download and recovery](aroll-download.md): render completion and in-editor playback do not prove a local file was saved. Verify the downloaded file before freezing it as downstream input; recover through the currently supported ChatCut export path when browser download stalls. Reuse existing cloud-upload/export authorization for the same material and destination rather than asking again.
