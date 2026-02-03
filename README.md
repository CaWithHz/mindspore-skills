# MindSpore Skills

MindSpore development skills for AI coding agents. Build CPU/GPU/NPU operators and migrate models with guided workflows.

Compatible with **Claude Code**, **OpenCode**, **Gemini CLI**, and **Codex**.

## Installation

### Claude Code

Register the marketplace and install:

```
/plugin marketplace add vigo999/mindspore-skills
/plugin install mscode@mindspore-skills
```

Then use slash command:

```
/mscode:cpu-plugin-builder
/mscode:cpu-native-builder
/mscode:gpu-builder
/mscode:hf-diffusers-migrate
/mscode:hf-migrate
/mscode:hf-transformers-migrate
/mscode:migrate
/mscode:model-migrate
/mscode:npu-builder
/mscode:api-helper
```

### OpenCode

Clone to your global config:

```bash
git clone https://github.com/vigo999/mindspore-skills.git ~/.config/opencode/mindspore-skills
ln -s ~/.config/opencode/mindspore-skills/skills ~/.config/opencode/skills
ln -s ~/.config/opencode/mindspore-skills/commands ~/.config/opencode/commands
```

Or for a specific project:

```bash
git clone https://github.com/vigo999/mindspore-skills.git .opencode
```

Then in OpenCode:

```
/cpu-plugin-builder
```

See [OpenCode Skills docs](https://opencode.ai/docs/skills) for more details.

### Gemini CLI

Install as an extension:

```bash
gemini extensions install https://github.com/vigo999/mindspore-skills.git --consent
```

Or from local clone:

```bash
git clone https://github.com/vigo999/mindspore-skills.git
gemini extensions install ./mindspore-skills --consent
```

See [Gemini CLI extensions docs](https://geminicli.com/docs/extensions/) for more details.

### Codex

Clone to your project root:

```bash
git clone https://github.com/vigo999/mindspore-skills.git .mindspore-skills
```

Codex reads `AGENTS.md` automatically. Verify with:

```bash
codex "Summarize the MindSpore skills available."
```

See [Codex AGENTS guide](https://developers.openai.com/codex/guides/agents-md) for more details.

## Available Skills

### Operator Development

| Skill | Description |
|-------|-------------|
| `api-helper` | Find API call chains and operator wiring in MindSpore codebase |
| `cpu-plugin-builder` | Build CPU operators via ATen/libtorch adaptation |
| `cpu-native-builder` | Build native CPU kernels with Eigen/SLEEF |
| `gpu-builder` | Build GPU operators with CUDA |
| `npu-builder` | Build NPU operators for Huawei Ascend |

### Model Migration

| Skill | Description |
|-------|-------------|
| `hf-diffusers-migrate` | Migrate HF diffusers models to mindone.diffusers |
| `hf-transformers-migrate` | Migrate HF transformers models to mindone.transformers |
| `model-migrate` | Migrate PyTorch repos to MindSpore |

## Available Commands

### Operator Development

| Command | Description |
|---------|-------------|
| `/api-helper` | API chain discovery workflow |
| `/cpu-plugin-builder` | ATen adaptation workflow |
| `/cpu-native-builder` | Native kernel workflow |
| `/gpu-builder` | CUDA kernel workflow |
| `/npu-builder` | Ascend NPU workflow |

### Model Migration

| Command | Description |
|---------|-------------|
| `/migrate` | Migration router (HF/third-party), routing only |
| `/hf-migrate` | HF library router (diffusers/transformers), routing only |
| `/hf-diffusers-migrate` | HF diffusers migration workflow |
| `/hf-transformers-migrate` | HF transformers migration workflow |
| `/model-migrate` | PyTorch repo migration workflow |

## Usage Examples

### Build a CPU operator

```
/cpu-plugin-builder

> Help me implement the linspace operator for MindSpore CPU
```

## Repository Structure

```
mindspore-skills/
├── .claude-plugin/          # Claude Code plugin config
├── commands/                # Slash commands
│   ├── api-helper.md        # API chain discovery
│   ├── migrate.md           # Migration router
│   ├── hf-migrate.md        # HF library router
│   └── ...
├── skills/                  # Skill definitions
│   ├── cpu-plugin-builder/  # ATen/libtorch operators
│   ├── cpu-native-builder/  # Native CPU kernels
│   ├── gpu-builder/         # CUDA operators
│   ├── npu-builder/         # Ascend NPU operators
│   ├── hf-diffusers-migrate/   # HF diffusers migration
│   ├── hf-transformers-migrate/ # HF transformers migration
│   └── model-migrate/       # PyTorch repo migration
├── AGENTS.md                # Codex instructions
└── gemini-extension.json    # Gemini CLI config
```

## Contributing

1. Fork this repository
2. Add your skill to `skills/<skill-name>/SKILL.md`
3. Add a command to `commands/<command-name>.md`
4. Update `AGENTS.md` with the new skill
5. Run `python tools/check_consistency.py`
6. (Optional) Install git hooks with `python tools/install_git_hooks.py`
7. Submit a pull request

Tip: set up hooks with `make hooks` (see Makefile).

## License

Apache 2.0
