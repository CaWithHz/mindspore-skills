# Guardrails and expectations

## Scope and precedence
- This file contains repo-specific rules for the current target repo.
- If any rule conflicts with SKILL.md, follow this file.

## Guardrails
- Avoid custom compatibility wrappers unless required.
- Use diff-based insertion when updating auto maps.
- Keep changes minimal and aligned with existing MindOne patterns.
- `register_buffer` is supported in MindSpore; do not remove it as part of device-handling cleanup.
- Model coding standards:
  - Import MindSpore as `import mindspore` (avoid `import mindspore as ms`).
  - Use `from mindspore import nn` and define modules as `nn.Cell`.

## Response expectations
- List reference files consulted.
- Summarize edits and note any risks or TODOs.
- Suggest next tests when appropriate.
