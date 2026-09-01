# General Image Model Adapter

Use one adapter only.

## ImageGen / GPT Image

- Write natural, connected prose.
- Put the subject and requested change early.
- When references are supplied, explicitly separate:
  - preserve: visible lighting, palette, contrast, texture and atmosphere;
  - change: subject, setting, action, props and composition.
- Pass the real reference images to the render tool.
- Prefer physical outcomes over camera-brand keyword stacks.
- Keep defect controls concise and scene-specific.

Suggested response:

```text
画面理解：<brief>
最终 Prompt：<natural prose>
避免内容：<targeted constraints>
```

## Midjourney

- Compress the visual identity and scene into a dense but readable paragraph.
- Keep the most important subject, action and lighting in the first half.
- Put supported parameters after the prompt body.
- Use an integer aspect ratio such as `--ar 16:9` or `--ar 21:9`.
- Use current raw styling only when appropriate; do not mix syntax from other models.

## FLUX

- Put subject, action and core visual identity first.
- Use direct descriptions with concrete materials and lighting consequences.
- Avoid long camera-brand lists and contradictory negatives.
- For FLUX.2, rewrite negatives as positive results:
  - “natural skin texture” instead of “no plastic skin”;
  - “clean deep shadows with retained structure” instead of “no noisy blacks”;
  - “coherent hands and joints” instead of “no bad hands”.
- Use JSON only when the request has many independently controlled elements.

## Model-neutral

- Use the canonical prose order from [params.md](../references/params.md).
- Do not include platform parameters.
- Keep the prompt transferable and identify the desired aspect ratio in prose.

