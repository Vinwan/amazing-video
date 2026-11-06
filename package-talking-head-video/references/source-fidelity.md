# Source Fidelity

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

### Delivery settings that preserve detail

- Prefer a lossless cleaned A-roll handoff. When a lossless format cannot be decoded by the compositor, create a compatible lossless intermediate (for example H.264 QP 0 at the same dimensions/pixel format), retain the original, and verify aligned decoded frames. Avoid another lossy A-roll generation merely for compatibility.
- For Remotion delivery use PNG frame capture (`--image-format=png`) to avoid an additional JPEG compression stage. For H.264, use CRF 10 as the established high-quality starting point unless the user chooses a different size/quality target; inspect detail and file size rather than treating one bitrate or CRF as proof of quality.
- Source stock from the highest-quality useful available rendition, not automatically the smallest rendition that meets canvas width. Preserve its original; any delivery-size conversion keeps aspect ratio, color intent and useful detail, with no avoidable lossy generations.
- A low-resolution original remains detail-limited. Keep its native canvas unless another deliverable is requested; explain the actual source limit when relevant instead of calling an enlarged file recovered HD detail. Do not add sharpening or AI upscaling automatically.
- Before PNG/high-resolution rendering, check free space for frame/decoder caches. Use a spacious volume for process-local temporary/cache paths; do not alter global system settings. After completion or failure, remove only this task’s verified temporary files, preserving sources and editable artifacts.
- On a clarity revision, compare aligned face/hair/glasses regions from the same source time through the handoff and final output. PSNR/SSIM may support the comparison when framing, frame mapping and color match; record sample scope and visually inspect it. Do not turn this project’s measured scores into a universal acceptance threshold.

When repairing a timeline that used a low-resolution proxy, replace every affected A-roll item atomically while preserving timeline start, duration, source start offset, track, fit, fades, and audio behavior. Keep captions, Motion Graphics, and scene timing unchanged. Re-read the track afterward and confirm that every A-roll item references the high-resolution asset.
