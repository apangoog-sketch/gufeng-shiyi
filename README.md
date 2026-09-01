# 古风诗意

简体中文 | [English](README.en.md)

单 LOOK 独立 Skill · v1.0 · 仅供个人学习，不可商用

显示名称：**古风诗意**。安装文件夹和调用标识：`gufeng-shiyi`。
显示名称保留 LOOK 原名；底层标识使用兼容的英文小写/拼音。
本 Skill 已固定 LOOK，调用后无需再选风格。

## 功能

- 分析参考图的构图、镜头、光线、色彩、颗粒、光晕、材质与情绪。
- 将新场景套入“古风诗意”的视觉语言，保留用户明确指定的主体和内容。
- 建立完整画面参数，处理氛围、影调厚度和符合媒介的真实感。
- 仅在方向存在重要歧义或冲突时提供 LOOK CARD 确认。
- 适配 ImageGen、Midjourney、FLUX；默认输出提示词，明确要求时才生图。
- 自带全部规则与验证脚本，不依赖其他 Skill。

## 范围

只处理单张静帧与该 LOOK 的参考图分析、提示词和明确的生图请求。
不处理视频、运镜、多镜头连续性、故事板、三视图或表情表。
不是通用的 14 LOOK 选择器；指定其他 LOOK 时会先确认，不会暗中替换。

## 安装

需要支持本地 Skill 的 Agent。将解压后含 `SKILL.md` 的整个
`gufeng-shiyi` 文件夹复制到你的 Skills 目录，不要只复制入口文件。

Codex 默认安装位置：

```text
Windows: %USERPROFILE%\.codex\skills\gufeng-shiyi\SKILL.md
macOS / Linux: ~/.codex/skills/gufeng-shiyi/SKILL.md
```

如已自定义 Skills 目录，使用你的实际目录。已有同名文件夹时先备份，
不要直接覆盖个人修改。复制完成后新建任务；未显示时重启客户端。
其他 Agent 请使用其支持的 Skill 目录与加载方式。
验证脚本需 Python 3.9 或更新版本；使用 Skill 本身不需要 Python。
生图还需宿主提供兼容的工具和权限，本包不附模型、账号或 API 密钥。

## 使用方法

### 输出提示词（默认）

```text
$gufeng-shiyi
一名抄书人在秋日河亭晾起最后一页湿纸。2.39:1，适配 ImageGen，只输出完整提示词。
```

### 分析并迁移参考图

先上传一张或多张图片，再发送：

```text
$gufeng-shiyi
分析这些参考图。保持本 Skill 的 LOOK，以参考图提供构图和主体信息，
把场景改为：一名抄书人在秋日河亭晾起最后一页湿纸。适配 FLUX，只输出提示词。
```

如果参考图本身才是主风格，请明确说明。它与固定 LOOK 有重要冲突时，
Skill 会提出 LOOK CARD 让你确认；不要把未确认的混合方向当作纯 LOOK。

### 直接生图

```text
$gufeng-shiyi
一名抄书人在秋日河亭晾起最后一页湿纸。16:9，直接生成一张图片。
```

工具不可用时只返回可用提示词，并说明未生图。指定某模型但宿主不支持
时，不会把另一模型的输出冒充为该模型结果。只调用名称而未提供内容时，
会询问场景，不会显示其他 LOOK 菜单。

## LOOK

- 视觉核心：长卷式构图、建筑山水平衡、克制传统色、季节光线与留白。
- 构图与空间：横向远景，人小但叙事动作可读。
- 材质与影像：纸感柔和空气、木、水、石、丝绸与远处薄霭。
- 情绪：沉思、流逝、含蓄情绪。
- 避免：旅游海报、符号堆积、没有事件的空景美化。

完整单 LOOK 规则：[references/look.md](references/look.md)。
这些规则描述视觉机制，不要求复刻示例的角色、道具或构图。

## 项目结构

```text
gufeng-shiyi/
├─ SKILL.md
├─ agents/openai.yaml
├─ references/
│  ├─ look.md
│  ├─ params.md
│  └─ recipes.md
├─ adapters/general.md
├─ anti-slop-system.md
├─ scripts/validate_skill.py
├─ tests/cases.json
├─ skill.json
├─ README.md
├─ README.en.md
└─ LICENSE
```

每份安装包自带规则；无需安装总包或其他 LOOK。

## 验证

在本 Skill 文件夹内运行：

```bash
python scripts/validate_skill.py
```

检查入口与显示名称、单 LOOK 隔离、完整中英文说明、内部链接、许可证、
旧项目引用和测试场景。脚本仅做离线结构检查，不代表生图质量或模型行为
已得到验证，不会调用生图服务。

手动检查建议：

1. 运行“只输出提示词”，确认没有生图且完整保留本 LOOK。
2. 提供参考图，核对证据、角色分配与是否产生不必要的风格混合。
3. 明确要求生图，确认宿主工具可用后才生成。
4. 指定另一个 LOOK，确认先处理冲突，不静默套用错误规则。

场景用例：[tests/cases.json](tests/cases.json)。

## 许可证

采用 [AP Image 个人学习许可证 1.0](LICENSE)。

**仅供个人、非商业的学习、研究与实验，不可商用。**
允许免费分享原版或修改版，须保留许可证并标注修改。
禁止售卖、收费授权、商业接单、广告宣传、付费课程、商业 API/SaaS
或企业业务使用；不得将本 Skill 辅助生成的内容用于上述商业用途。
这是一份个人学习用途的源码分享许可，不是允许商用的宽松开源许可。
第三方素材、模型和平台仍受各自条款约束。

