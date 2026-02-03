---
name: hf-transformers-migrate-test
description: Generate minimal MindOne transformer tests and validation scaffolds for migrated models.
metadata:
  short-description: MindOne transformers test generation and execution
---

# Skill: ms-transformers-test-generation

## Purpose
Create minimal test scaffolds for migrated MindOne transformer models from huggingface transformers, focusing on fast smoke coverage.

## Use when
The task is to draft or update/generate tests for MindOne transformer model migrations.

## Inputs to collect
- `model_name`

## Steps

1. Check the target repo of `mindone/tests/transformers_tests/models/` as the model test layouts 
2. Learn the template of the model test under this skills folder `/test-template/cohere`, or learn the template of other model test from target repo model test `mindone/tests/transformers_tests/models/`.
3. If any issues or confusion arise, review additional testing files in `mindone/tests/transformers_tests/models/` for patterns and expected behaviors.
4. For small configs and input shapes, refer to the original HF test file at
`transformers/tests/transformers_tests/models/{model_name}/test_modeling_{model_name}.py`.
5. If no fast test exists there, create a minimal config by shrinking model dimensions. Instantiate the model with a small config.
(e.g., hidden size, heads, layers) and use tiny dummy inputs that satisfy required shapes.

## Guardrails
<MUST>Any configurations and tokenizations should be directly import from huggingface transformers. Learn about the imports chain from the test template or other model tests.</MUST>


## Test execution

Testing command under target repo `mindone`:
```
python -m pytest tests/transformers_tests/models/<model_name>
```

These tests compare HF transformers outputs with migrated MindOne outputs using the same config.

Common issue sources and triage:
- Environment mismatch (MindSpore version, hardware backend, or missing deps). Verify env first.
- Migration modeling script regressions. Re-check the migrated `modeling_*.py` against HF.
- Component compatibility gaps between HF and MindOne. Compare the corresponding component files and diff key ops.
Debug approach:
- Compare the HF and MindOne modeling files side by side and diff the relevant blocks.


## Output
- Test file path(s).
- Any required config tweaks.
- Suggested test command.
