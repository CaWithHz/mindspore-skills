# MindSpore Skills

Agent skills for MindSpore deep learning framework development. Compatible with Claude Code, Codex, Gemini CLI, and other AI coding assistants.

## Quick Start

### Claude Code

```bash
# Register as marketplace
/plugin marketplace add mindspore-ai/mindspore-skills

# Install a skill
/plugin install cpu-builder@mindspore-skills
```

### OpenAI Codex

```bash
# Clone to your project
git clone https://github.com/mindspore-ai/mindspore-skills.git .mindspore-skills

# Codex will automatically read AGENTS.md
```

### Other Tools (Cursor, Aider, etc.)

```bash
# Use OpenSkills universal loader
npm i -g openskills
openskills install mindspore-ai/mindspore-skills
openskills sync
```

## Available Skills

| Skill | Description |
|-------|-------------|
| [cpu-builder](skills/cpu-builder/) | Build MindSpore CPU operators by adapting ATen (libtorch) operators |

## Skill Structure

```
mindspore-skills/
├── .claude-plugin/
│   └── marketplace.json      # Claude Code marketplace registry
├── AGENTS.md                 # Universal agent instructions
├── skills/
│   └── cpu-builder/
│       ├── .claude-plugin/
│       │   └── plugin.json   # Plugin metadata
│       ├── SKILL.md          # Main skill instructions
│       └── reference/        # Additional documentation
└── README.md
```

## Creating New Skills

1. Create a new directory under `skills/`
2. Add `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: my-skill
   description: When to use this skill...
   ---
   # Instructions...
   ```
3. Add `.claude-plugin/plugin.json`
4. Update `AGENTS.md` with the new skill
5. Update `.claude-plugin/marketplace.json`

## Contributing

1. Fork this repository
2. Create your skill following the structure above
3. Test with Claude Code: `/plugin install ./path/to/skill`
4. Submit a pull request

## License

Apache 2.0
