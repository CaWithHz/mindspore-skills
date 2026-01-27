# MindSpore Skills

You have additional SKILLs documented in directories containing a "SKILL.md" file.

**IMPORTANT**: You MUST read the SKILL.md file whenever the description of the skills matches the user intent, or may help accomplish their task.

## Available Skills

| Skill | Path | Description |
|-------|------|-------------|
| cpu-builder | skills/cpu-builder/ | Build MindSpore CPU operators by adapting ATen (libtorch) operators |

## Activation Triggers

Load the appropriate SKILL.md when users mention:

- **cpu-builder**: `mint.*`, `Tensor.*`, "cpu operator", "kernel .cc", "operator adaptation", "op_plugin", "ATen operator"

## Usage

When a user's request matches a skill description:

1. Read the corresponding `SKILL.md` file
2. Follow the instructions in that file
3. Use any reference materials in the `reference/` subdirectory

## Compatibility

This repository is compatible with:
- **Claude Code**: `/plugin marketplace add mindspore-ai/mindspore-skills`
- **OpenAI Codex**: Reads this AGENTS.md automatically
- **Gemini CLI**: Use with MCP server or direct file access
- **Cursor/Windsurf**: Add as custom rules
