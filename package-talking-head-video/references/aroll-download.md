# Clean A-roll download and recovery

Read at the ChatCut -> local Remotion handoff. The observed failure was a completed export that played inside ChatCut while both download buttons produced no saved file. Treat rendering, download initiation, local save, and media validation as separate states.

## Preferred handoff

1. Load the installed ChatCut `export` skill and use its current supported export/status tools and schema. Confirm the frozen project/timeline, full edited range, source-supported delivery resolution, codec, and caption inclusion. Export clean A-roll without baked-in captions when Remotion owns subtitle styling, while retaining the corrected caption data separately.
2. Record the returned render ID and export mode. Track that same job to completion; do not submit a second render merely because downloading has not started. Preserve the frozen timeline and source offsets.
3. When a supported completed export returns a real download URL, download that exact URL to a collision-safe project-local `.part` file using an available file/HTTP tool. Preserve signed URL query parameters in the request, quote safely, follow redirects, fail on HTTP errors, and use bounded retries. Do not construct bucket URLs, scrape hidden endpoints, expose signed tokens in user-facing links, or treat browser blob URLs as externally downloadable files.
4. Check that the download process succeeded; compare bytes with the export's declared size when supplied. Probe the media for duration, dimensions, frame rate, video codec, and audio; compare with the frozen timeline and requested master. Inspect representative frames for the correct source, framing, and absence of unintended baked-in captions. Only then rename/promote the file and set the checkpoint to `clean-aroll-ready`.

For a long download, show elapsed progress and bytes when available. A growing `.part` file is progress, not completion. If progress stalls, inspect the process/HTTP failure and retry the same valid artifact once before changing export mode. Refresh an expired URL through the supported render/status mechanism rather than rerendering a successful job without cause.

## Browser download has no effect

- If a supported browser-render path was already used, inspect the actual download event/state and the expected save location. A completed in-editor preview is evidence of render success only. Do not mark the file saved based on clicking “下载/再次下载”.
- Allow one evidence-based retry of the existing artifact after inspecting the blocker. If it again produces no download/file, stop repeating the same button or asking the user to do so. Prefer a connector-provided downloadable artifact when the current tools support it; do not use UI export as a substitute where the installed plugin instructions forbid it.
- If recovery requires switching to cloud export or uploading locally linked source media, explain the specific source, destination, and upload requirement, and follow current tool/skill authorization rules. Reuse explicit authorization already granted for this source and destination; ask only when required authorization is missing or the action materially changes. A past approval for one video is not blanket permission for future uploads.
- After authorization, make the delivery-grade source remotely readable through ChatCut's supported import/upload flow and export the same frozen timeline. Track the new render ID, then download and validate as above. Do not replace speech cleanup with another editor, change the cut, or substitute a low-resolution proxy to bypass the download failure.
- If the supported fallback also fails, preserve the editable project and caption data, report the exact remaining blocker, and leave the stage incomplete. Do not claim a local A-roll or final package exists.

## Resume without repeated work

Persist the source identity, project/timeline IDs, frozen frame count/FPS, render ID/mode/status, existing authorization scope, expected byte count when supplied, local target path, and validation result. Keep temporary download credentials out of ordinary delivery documentation. On resume, inspect this checkpoint and the actual file before exporting again. Reuse a valid existing local file; otherwise resume the failed handoff. Downstream scene planning may continue while a download runs, but final assembly must wait for the verified A-roll.
