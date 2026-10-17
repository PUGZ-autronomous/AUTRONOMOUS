# Optional Agent Reach for AUTRONOMOUS / Ultron

**Status:** Installation path prepared, **not installed or wired into the running agent**.
This setup deliberately preserves the Hermes core and the current fail-closed
module, tool, credential and MCP boundaries.

Agent Reach (https://github.com/Panniantong/Agent-Reach) is a selector,
installer and health checker for several third-party internet-research CLIs.
It is **not** a drop-in model, a general browsing API or a ChatGPT plugin.
After setup, an agent uses the *upstream* tools (for example yt-dlp, gh,
mcporter) subject to its own permissions.

## Safe host-side installation (macOS/Linux)

Do this **on the machine that will actually run AUTRONOMOUS**, never in CI.
Install `pipx` first if missing (https://pipx.pypa.io/stable/installation/).

From the repository root:

```bash
bash scripts/setup_agent_reach.sh
```

The script installs the named **GitHub project** into an isolated pipx
environment if absent, then runs the default **read-only** dependency check
and `agent-reach doctor`. It does **not** use sudo, install missing system
tools, request login cookies, change Ultron/Hermes configuration, or start
background jobs. Agent Reach state is kept outside this repository under
the home directory.

If `agent-reach` is already on PATH the script does not overwrite it.
Check its source: an unrelated PyPI package uses the same name. To install
manually, use the GitHub URL, not `pipx install agent-reach`:

```bash
pipx install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
agent-reach doctor
```

If the check identifies missing upstream tools, inspect the plan first:

```bash
agent-reach install --env=auto --dry-run
```

**Only with explicit host-owner approval**, to install/configure the core
external dependencies:

```bash
agent-reach install --env=auto --system
agent-reach doctor
```

Never pass `--channels=all` just to make diagnostic lights turn green.
Choose the individual platforms actually needed.

### Windows PowerShell

Follow the current upstream instructions in
https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md .
If Python Store aliases interfere, use `py -3` and an isolated virtual
environment instead of executing the bash script.

## How it should be integrated later (NOT enabled by this change)

1. Keep the core Hermes adapter untouched; use Ultron's explicit tool
   allowlist or read-only skill-reference surfaces.
2. Start with **read-only research** from a narrow allowlist (web, public
   GitHub, public YouTube and RSS); cap runtime, result sizes and rate.
3. Never give model-authored shell commands or arbitrary repository writes
   to this integration; wrap individual tools with structured arguments.
4. Treat fetched content as untrusted. Do not allow web page or social-post
   instructions to grant permissions, send money, write code or leak data.
5. Surface `agent-reach doctor --json` status in a worker health indicator,
   but distinguish *installed*, *configured* and *actually tested*.
6. Require separate human consent for credentials, browser sessions,
   account posting, purchases and any irreversible action. Keep all secrets
   out of GitHub, logs and UI. Use a secondary account where practical.
7. Add bounded integration tests before enabling tools for live workers.
   Failure should disable the research capability, not break the main app.

**Nothing here changes Ultron's live/fake adapter selection.** Installing
Agent Reach on a machine does not magically give the existing workers access
until a separate, reviewed integration is written.

## ChatGPT integration

ChatGPT cannot import this CLI from GitHub into a conversation. A separate
remote MCP service could expose approved research tools for ChatGPT, where
the ChatGPT plan and workspace permissions allow custom MCP servers. Agent
Reach itself is not that remote service. Do not expose local shell access or
browser cookies through an MCP server; publish only scoped, authenticated,
rate-limited read-only research operations.

Official guide: https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt
