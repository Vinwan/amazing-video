# Color Pipeline

## Diagnose first

Inspect the source, intermediate, and final independently. Capture codec, pixel format, range, primaries, transfer, matrix, HDR side data, and rotation.

Common HDR indicators:

- HLG: `arib-std-b67`
- PQ: `smpte2084`
- wide gamut: `bt2020`
- 10-bit formats such as `yuv420p10le`
- Dolby Vision side data or profile metadata

## Locate the stage of change

1. Extract or view the same timestamps from source, intermediate, and final.
2. Compare the same facial region, excluding captions and overlays.
3. Compare SDR intermediate against SDR final numerically.
4. Treat HDR-versus-SDR numeric luma comparisons as non-equivalent unless both are display-conformed through the same transform.
5. Search the composition for brightness, contrast, exposure, blend modes, and light overlays.

If the SDR intermediate is already too bright and the final is equal or darker, preprocessing caused the issue.

## HDR to SDR

Prefer a metadata-aware transform in DaVinci Resolve, Final Cut Pro, or Apple Compressor:

- explicitly set input to the detected HDR format;
- output Rec.709 with the chosen gamma, normally 2.4 for conventional video;
- use a color-managed tone mapper that understands HLG/PQ and Dolby Vision metadata;
- inspect waveform and skin tone instead of trusting a single monitor preview.

When using FFmpeg, do not blindly hardcode a nominal peak such as 100 nits. Establish source reference white/peak and output peak, choose a documented tone-mapping operator, preserve tags, and test stills before encoding the full video. A Dolby Vision base layer decoded without its dynamic metadata may not match Apple playback.

## Practical targets

Use targets as starting points, not absolutes:

- keep diffuse highlights below about 95 IRE for SDR;
- place normally lit facial skin roughly around 55–70 IRE;
- preserve forehead and curtain texture;
- avoid gamut clipping in warm skin and yellow graphics;
- convert once, then keep the graphics/render pipeline in Rec.709.

If the image is already baked too bright, test approximately −0.3 to −0.7 stop exposure on representative stills, then refine with scopes rather than applying a generic dark overlay.
