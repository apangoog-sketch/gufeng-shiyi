# 古风诗意 — Ancient Poetic

[简体中文](README.md) | English

Standalone single-LOOK Skill · v1.0 · Personal study only · No commercial use

Display name: **古风诗意**. Folder and invocation identifier: `gufeng-shiyi`.
The displayed title retains the original LOOK name; the compatible technical
identifier uses lowercase letters and hyphens. This LOOK is selected by default.

## Features

- Analyze reference composition, lens behavior, light, color, grain, halation,
  materials, and mood.
- Apply the Ancient Poetic visual language to a new scene while preserving explicit
  user content and constraints.
- Resolve complete image parameters, atmosphere, tonal depth, and medium realism.
- Offer a LOOK CARD only for meaningful ambiguity or conflict.
- Adapt prompts to ImageGen, Midjourney, and FLUX; render only on explicit request.
- Include all rules and an offline validator without depending on another Skill.

## Scope

One still image within this LOOK: reference analysis, prompts, and explicit
render requests. Excludes video, camera movement, multi-shot continuity,
storyboards, turnarounds, and expression sheets. This is not a 14-LOOK picker;
a request for a different LOOK is clarified rather than silently overridden.

## Installation

Use an agent that supports local Skills. Copy the complete `gufeng-shiyi`
folder containing `SKILL.md`, not just the entry file, into the Skills directory.

Default Codex destinations:

```text
Windows: %USERPROFILE%\.codex\skills\gufeng-shiyi\SKILL.md
macOS / Linux: ~/.codex/skills/gufeng-shiyi/SKILL.md
```

Use your actual directory if customized. Back up an existing same-name folder
before replacing it. Start a new task after copying; restart the client if needed.
For other agents, follow their compatible Skill loading conventions.
Validation needs Python 3.9 or later; using the Skill does not require Python.
Rendering additionally needs a compatible host tool and authorization. No model,
account, or API key is bundled.

## Usage

### Prompt only (default)

```text
$gufeng-shiyi
A copyist hangs the last damp page to dry in an autumn riverside pavilion. 2.39:1, adapt for ImageGen. Return the complete prompt only.
```

### Analyze and transfer references

Upload the image(s), then send:

```text
$gufeng-shiyi
Analyze these references. Keep this Skill's LOOK; use the references for
composition and subject information. New scene: A copyist hangs the last damp page to dry in an autumn riverside pavilion.
Adapt for FLUX and return a prompt only.
```

Explicitly say if a reference should instead define the primary style. A material
conflict with the fixed LOOK triggers a LOOK CARD; an unresolved blend is not an
exact preset match.

### Render

```text
$gufeng-shiyi
A copyist hangs the last damp page to dry in an autumn riverside pavilion. 16:9. Generate one image.
```

When no compatible tool is available, the Skill returns a ready prompt and says
no image was rendered. It does not label another model's output as the requested
model. A bare invocation asks for a scene, not for another LOOK choice.

## LOOK

- Identity: scroll-like compositions, architecture and landscape in balance,
  restrained traditional colors, seasonal light and meaningful emptiness.
- Framing: wide horizontal staging; people remain small but narratively legible.
- Texture: paper-soft atmosphere, timber, water, stone, silk and distant haze.
- Mood: contemplative, transient, quietly emotional.
- Avoid: tourism posters, symbol piles, empty beauty without a narrative moment.

Full single-LOOK rules: [references/look.md](references/look.md).
These define visual mechanisms, not a fixed character, prop, or composition template.

## Project structure

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

Each package is self-contained; the collection and other LOOKs are not required.

## Validation

From this Skill folder:

```bash
python scripts/validate_skill.py
```

Checks entry/display identity, single-LOOK isolation, bilingual sections, internal
links, license, stale references, and test fixtures. These are offline structural
checks, not evidence of image quality or model behavior. No image service is called.

Manual checks:

1. Request a prompt only and verify no rendering and correct LOOK retention.
2. Supply references and inspect evidence, assigned roles, and unnecessary blending.
3. Explicitly request an image and verify a compatible host tool is available.
4. Request another LOOK and verify the conflict is handled rather than hidden.

Test scenarios: [tests/cases.json](tests/cases.json).

## License

[AP Image Personal Study License 1.0](LICENSE).

**Personal, non-commercial learning, research, and experimentation only.
Commercial use is prohibited.** Free sharing is allowed with the complete license
retained and modifications marked. Sales, paid licensing, commissioned work,
advertising, paid courses, commercial APIs/SaaS, and business operations are
prohibited; Skill-assisted output may not be used for those commercial purposes.
This is personal-study source sharing, not a permissive commercial-use open-source
license. Third-party assets, models, and platforms retain their own terms.

