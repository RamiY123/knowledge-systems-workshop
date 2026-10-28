# Participant preparation

Bring your laptop and charger. Use any installed AI coding environment that can
read project files and execute local commands. Sign in and confirm it responds.
Use Windows PowerShell or macOS Terminal for the commands below. No Docker,
database server, local embedding model, or GPU is required.

## 1. Open the project

The trainer shares the repository URL. Sign in to GitHub, create your own fork,
and clone your fork. You need read access and permission to fork; write access to
the trainer repository is unnecessary. If forking is blocked, ask the trainer.
Open the cloned root folder in your AI environment. You should see README.md,
sources/, steps/, and requirements.txt. Get your source assignment from the trainer.

## 2. Ask your AI to prepare the environment

```text
Read PREPARATION.md and README.md. Prepare only the environment, not the workshop
steps. Check Git and Python. Install missing tools from official sources, asking
for permissions required by this environment. Use Python 3.12–3.14 and create
.venv in this project without replacing system Python. If suitable Python is
missing, use uv from Astral's official installer to obtain Python 3.12.
Install requirements.txt in .venv. Do not install format extras unless my assigned
source needs them. Run tools/doctor.py and explain actual results. Check command
adapter files exist. Do not run collect or any subsequent step yet.
Never read .env or display a key. Tell me how to enter the trainer-provided key
privately in the ignored .env file. Do not make an API call during setup.
```

If Python is already installed, the minimal manual path is below. Open a terminal
in the project folder; run each line separately and wait for it to finish.

### Windows

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe tools/doctor.py
```

If `python` is unavailable but the Python launcher exists, use `py -3.12` for the
first two commands. Otherwise ask your AI to install Python/uv using official
instructions. Reopen the terminal after installation to refresh PATH.

### macOS

```bash
python3 --version
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python tools/doctor.py
```

Confirm the first command reports a supported Python. Do not use an older system
Python. For either OS, `uv venv --python 3.12 .venv` is an alternative when uv is
installed; use `uv pip install --python <venv-python-path> -r requirements.txt`.
No activation is required with the explicit executable paths shown here.

The sample sources use HTML/Markdown. If the trainer assigns PDF/DOCX/XLSX files,
install requirements-formats.txt using the same pip command with that filename.
Image-only scans need separate OCR handling and are not part of the default setup.

## 3. Enter the OpenAI key privately

The trainer supplies a key with access to embeddings. API billing is separate
from your AI coding tool's subscription. Do not paste the key into an AI chat.

1. Copy `.env.example` to `.env` locally (do not overwrite an existing file).
2. Open `.env` yourself in a local editor and enter the key after `OPENAI_API_KEY=`.
3. Save and close it. It is ignored by Git. Never attach or commit it.
4. Run tools/doctor.py. It reports only whether a key is configured, not its value.

An existing OPENAI_API_KEY environment variable takes precedence over .env.
Do not ask the agent to read either value. The helper loads it internally.
Doctor does not authenticate the key or spend API credits. The trainer should
verify account access in advance; actual embedding runs occur when instructed.

## 4. Verify manual commands

- Claude Code: `.claude/skills/` supplies `/collect source-01` and the other steps.
- Codex: `.agents/skills/` supplies `$collect source-01`; skills are explicit-only.
- VS Code Copilot: `.github/prompts/` supplies `/collect source-01` in supported
  Local/agent sessions. Select the prompt-file command if multiple entries appear.

Reload the session if needed. Check that the command appears without running it.
VS Code alone is an editor; the chosen AI extension must support these commands.
Fallback: ask the agent to follow WORKSHOP_MODE.md and the requested step guide.

## Readiness

- [ ] Supported Python and isolated .venv available.
- [ ] tools/doctor.py passes the extraction smoke check.
- [ ] AI environment responds and can operate on local files.
- [ ] Manual commands are discoverable, or the guide-based fallback is available.
- [ ] Assigned source known; original source files remain unchanged.
- [ ] Key configured privately before Stage 2.

Share errors and tool versions with the trainer if blocked, without credentials.
Keep completed work in workspace/<source>/. The agent should explain each step
and stop for your inspection before you invoke the next one.

Official setup references:
- https://www.python.org/downloads/
- https://docs.astral.sh/uv/getting-started/installation/
- https://github.com/microsoft/markitdown
- https://developers.openai.com/api/docs/guides/embeddings
