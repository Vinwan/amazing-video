# Shared Manifest

Record editMode at the root. New projects use `classic` or `premium-v2.1`. Both 精剪视频 and 精剪视频2.1 select `premium-v2.1`. Revisions preserve recorded legacy modes unless migration is requested. Premium entity introductions reference `entity-card-manifest.json` for approved assets and first-mention timing. Captions may be stored in captions.json and referenced by path rather than duplicated in each scene. Scene records carry stable asset IDs, placement and timing; provenance remains in broll-manifest.json. The compact inline example below illustrates the timing contract, not a requirement to duplicate caption text across project files.

## 3. Create the edit decision list

Convert the cleaned transcript into one shared, time-based manifest. Use milliseconds for interchange and derive frames only inside Remotion.

```json
{
  "version": 1,
  "editMode": "premium-v2.1",
  "fps": 30,
  "canvas": {"width": 1920, "height": 1080},
  "aRoll": "media/clean-aroll.mp4",
  "captions": [{"id":"cap-001","startMs":0,"endMs":1680,"text":"已经有 100 万个 Skills","emphasis":[{"text":"100 万个","colorRole":"data","treatment":"marker"}]}],
  "scenes": [{
    "id":"scene-001","startMs":0,"endMs":3200,"purpose":"hook",
    "spokenText":"已经有 100 万个 Skills",
    "visualBrief":"100 万个作为证据主数字，与字幕数据使用同一强调色",
    "mode":"overlay","protect":["face","mouth","captions"]
  }]
}
```

Require stable IDs. Use half-open intervals `[startMs, endMs)` and a single formula in Remotion: `frame = round(ms * fps / 1000)`. Prevent cumulative drift by converting absolute timestamps, never by adding rounded scene durations.
