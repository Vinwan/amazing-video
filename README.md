# amazing-video

一套面向中文真人口播的视频剪辑与包装 Skill。让 Agent 按统一流程完成口播清理、字幕、信息卡、动态解释画面和成片交付。

本仓库提供工作流指令、视觉规范、设计模板、检查脚本和参考素材，**不是独立剪辑软件，也不是下载后就能直接渲染的视频工程**。实际制作需要支持 Skill 的 Agent，以及相应工具和权限。

## 选择你的剪辑方式

| 模式 | 怎么说 | 画面特点 |
| --- | --- | --- |
| 3.0 素材叙事版 | 按照 v3.0 剪辑 | 真人主导讲述，贴题素材承接情境，图解解释逻辑，概念大字帮助记忆；按语义安排真人回归，小窗可选 |
| 经典版 | 剪口播视频 / 简洁剪视频 / 简单剪视频 | 真人和原背景持续保留；信息卡、截图、图表仅做局部悬浮，不用全屏图解替换真人，也不把真人缩成小窗 |
| 2.0 黑金版 | 精剪视频 / 优美视频 / 2.0 / 精剪视频黑金版 | 深色、暖白与金色视觉；使用连续场景、关系链和有目的的镜头运动解释内容 |
| 2.0 彩色版 | 精剪视频彩色版 | 沿用 2.0 的结构与真人节奏，改用彩色分层面板和语义配色 |

未指定风格的普通包装请求默认经典版；未指定配色的精剪默认黑金版。继续修改已有项目时继承原模式，不自动混合风格。

2.0 不是纯图文幻灯片：开头、关键判断、转场和结尾保留有意义的全屏真人段落，解释段默认使用同步的圆形真人小窗。出现时机由内容节奏决定，不规定固定出镜比例。

### v3.0 使用示例

```text
使用 $package-talking-head-video，按照 v3.0 剪辑这段视频。
保持原比例，按口播寻找贴题素材，保留素材来源和授权记录。
```

v3.0 是独立叙事模式，不替换经典版或 2.0 的默认触发方式。真人负责观点与判断，素材负责对象、案例、情境和比喻，图形负责关系，概念大字不重复整句字幕。完整规范见 [narrative-v3.md](package-talking-head-video/references/narrative-v3.md)。当前已完成规则配置，尚未以 v3.0 实际成片验证。

## 工具分工与工作流

| 阶段 | 主要工具 | 任务与输出 |
| --- | --- | --- |
| 素材检查 | Agent、FFmpeg / ffprobe | 检查比例、旋转、清晰度、声音和色彩信息 |
| 口播清理 | ChatCut | 校正识别文字，删除重复与失败重录，压缩无意义停顿，对齐字幕 |
| 时间线冻结 | Agent | 确认清理后的真人素材，建立共享字幕与场景清单（EDL） |
| 视觉制作 | HyperFrames | 根据文案拆场景，制作信息卡、图解及其内部动画 |
| 最终合成 | Remotion | 管理画布、帧率、场景顺序、真人、字幕、视觉素材和声音 |
| 验收与交付 | Agent 与各工具 | 检查真实画面、清晰度、字幕、音画同步，并生成配套封面 |

素材流程：**口播清理并冻结 → 拆出素材需求 → ChatCut `search_stock_media` 搜索候选 → 检查实际片段与来源 → 下载、验证与截取 → HyperFrames 包装 → Remotion 合成**。优先使用已提供或已批准的素材；找不到合适素材时，记录原因并保留真人或图解，不硬塞无关镜头。经典版仍仅用悬浮视频卡，2.0 可融入解释场景，v3.0 按叙事任务选择全屏素材或局部呈现。

口播时间线冻结后，HyperFrames 和 Remotion 不独立修改讲话节奏。若口播有改动，受影响的字幕和场景时间也要同步更新。

工具不可用时，应说明缺少的依赖及已完成部分，不静默换工具并声称流程完成。

## 安装与开始使用

### 在 Codex 中使用

1. 点击仓库的 **Code → Download ZIP**，解压。
2. 将其中完整的 `package-talking-head-video` 文件夹放入 Codex 的 `skills` 目录。默认位置是 `~/.codex/skills/`；设置了 `CODEX_HOME` 时，使用对应目录下的 `skills/`。
3. 确认目录为 `skills/package-talking-head-video/SKILL.md`，避免多嵌套一层仓库文件夹。
4. 安装并配置 ChatCut、HyperFrames 和 Remotion 对应的工具或插件、配套 Skills，以及必要的运行环境。下载本仓库不会自动安装这些依赖。
5. 在新的会话中提供视频素材并调用 Skill。

已有同名 Skill 时，先备份并比较差异，避免覆盖自己的修改。

例如：

```text
使用 $package-talking-head-video，简洁剪这个视频。
保持原比例，信息卡和截图只做悬浮叠加，不遮挡人脸和字幕。
```

```text
使用 $package-talking-head-video，精剪这个视频，采用黑金版。
根据讲述节奏安排全屏真人与解释场景。
```

```text
使用 $package-talking-head-video，精剪视频彩色版。
保持原视频画幅，并交付可编辑工程和配套封面。
```

### 交给其他 Agent

提供完整的 Skill 文件夹，让 Agent 先阅读 [SKILL.md](package-talking-head-video/SKILL.md)，再按任务加载相应参考规范。

其他平台需使用该平台支持的 Skill 加载方式；不能仅凭放入文件夹就保证自动识别。工具接口、配套 Skills 和权限也需要在目标环境中确认。

## 横屏、竖屏与素材保护

- 横屏和竖屏均适用，默认保持源视频的实际显示比例和完整构图。
- 不因为平台习惯就自动裁切、拉伸、改成另一种画幅。
- 经典版在画面空闲区域放悬浮卡；空间不足时简化、拆分卡片或截取截图重点，不覆盖整个画面。
- 2.0 的圆形小窗仅对局部呈现使用遮罩，不改变全屏真人母版。
- 不用低清预览代理充当最终素材；导出分辨率高不代表恢复了源画质。
- 默认开头采用动态真人加醒目标题，保护人脸、口型和字幕区域。
- 视频比例和封面比例独立：封面默认 3:4，需要 16:9 等规格时请明确说明。

## 字幕、颜色和字体

字幕以清理后的口播为准，按语义断句；重点数据保留数值、单位和限定条件。颜色用于区分数据、概念、行动、风险和收益，不随机给每个字上色。

在项目 `DESIGN.md` 中记录字体、配色、卡片样式、安全区域和动效。可从 [设计模板](package-talking-head-video/assets/DESIGN.template.md) 开始，根据素材调整，不照搬固定坐标。

仓库未附字体包。使用前请在制作环境中安装所选字体，并确认对应使用授权。

## 默认交付

完整包装任务包含：

- 最终 MP4 与一张配套封面；
- 封面选用的真人原始帧及时间点；
- 可编辑 Remotion 工程；
- 清理后的 ChatCut 项目或真人视频；
- 校正后的字幕数据和场景清单；
- HyperFrames 视觉源文件及渲染素材；
- 简洁的验收说明。

仅诊断画质或色彩时，只检查并报告，不自动重新剪辑或渲染。

## 文件导航

| 文件或目录 | 用途 |
| --- | --- |
| [SKILL.md](package-talking-head-video/SKILL.md) | Agent 入口、模式选择和完整流程 |
| [style-system.md](package-talking-head-video/references/style-system.md) | 经典版视觉、字幕、标题与封面规范 |
| [broll-sourcing.md](package-talking-head-video/references/broll-sourcing.md) | 素材搜索、片段核对、来源授权记录与合成 |
| [premium-v2.md](package-talking-head-video/references/premium-v2.md) | 2.0 黑金版、场景设计与真人节奏 |
| [premium-colorful.md](package-talking-head-video/references/premium-colorful.md) | 2.0 彩色版差异 |
| [premium-finishing.md](package-talking-head-video/references/premium-finishing.md) | 精剪音效、强调色和微动画 |
| [quality-checklist.md](package-talking-head-video/references/quality-checklist.md) | 成片与封面验收 |
| [color-pipeline.md](package-talking-head-video/references/color-pipeline.md) | HDR / SDR 与色彩处理 |
| [aroll-download.md](package-talking-head-video/references/aroll-download.md) | 清理后素材下载与完整性确认 |
| [scripts/](package-talking-head-video/scripts/) | 视频色彩与元数据检查脚本，需 Python 3 和 ffprobe |
| [assets/](package-talking-head-video/assets/) | 设计模板、参考图片及音效 |
| [agents/openai.yaml](package-talking-head-video/agents/openai.yaml) | Codex 界面与调用配置 |

## 使用与授权说明

本仓库尚未声明开源许可证。公开可访问不等于已授予任意复制、修改、分发或商业使用的许可；需要相应授权时，请先联系仓库作者。

参考图片、品牌标识、音效及外部链接内容可能涉及第三方权利。音效的来源记录见 [manifest.json](package-talking-head-video/assets/approved-sfx/manifest.json)，来源记录本身不构成再分发许可。使用或再分发相关素材前，应核实授权范围；不确定时替换为自己有权使用的素材。

Skill 中的参考样例用于解释视觉方法，不代表可以复制其他创作者的身份、作品或未经核实的事实。

