---
description: Add Fastn to OpenAI Codex with one command, sign in, and build integrations from the Codex CLI or IDE extension.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Codex

Codex reads its MCP servers from `~/.codex/config.toml`. The Codex CLI and the Codex IDE extension share that file, so adding Fastn once covers both.

<figure><img src="../../.gitbook/assets/mcp-fastn-tab-codex.webp" alt="Fastn's MCP server page with the Codex tile selected, showing the command codex mcp add Fastn --url https://mcp.fastn.dev/fastn-workspace, the file ~/.codex/config.toml with an mcp_servers.fastn entry, and a note that the CLI and the VS Code extension read the same file"><figcaption>The Codex tile under <strong>Connect your AI tool</strong> in Fastn has the command and the file.</figcaption></figure>

## Add Fastn

{% stepper %}
{% step %}
#### Run the command

```
codex mcp add fastn --url https://mcp.fastn.dev/fastn-workspace
```

Codex detects that Fastn uses OAuth and starts the sign-in straight away. It prints *Authorize `fastn` by opening this URL in your browser* and opens the page.
{% endstep %}

{% step %}
#### Sign in to Fastn

In the browser, sign in to Fastn if asked. If you belong to more than one Fastn org, pick the workspace Codex works in and click **Connect**. When the terminal prints *Successfully logged in.*, you are done.

<figure><img src="../../.gitbook/assets/mcp-codex-choose-workspace.webp" alt="Fastn's page titled Which workspace should Codex (chatgpt.com) use?, with The org selected in Fastn chosen, a list of orgs and a Connect button"><figcaption><strong>The org selected in Fastn</strong> follows whichever org you have open in the Fastn dashboard; picking a named org pins Codex to it.</figcaption></figure>

If the browser does not open, copy the URL Codex printed. To sign in again later, run `codex mcp login fastn`.
{% endstep %}

{% step %}
#### Check it

```
codex mcp list
```

Fastn is listed with **Status** `enabled` and **Auth** `OAuth`:

```
Name   Url                                    Bearer Token Env Var  Status   Auth
fastn  https://mcp.fastn.dev/fastn-workspace  -                     enabled  OAuth
```
{% endstep %}
{% endstepper %}

The command writes this entry to `~/.codex/config.toml`. You can also add it by hand and then run `codex mcp login fastn`:

```
[mcp_servers.fastn]
url = "https://mcp.fastn.dev/fastn-workspace"
```

## Use it

Ask Codex to use Fastn by name the first time. For example:

```
codex "Use the fastn MCP server: call its whoami tool and tell me the org name."
```

Codex calls `fastnPlatform__whoami` and answers with the name of the org you picked when signing in. From there, ask for the integration in one sentence. See [Build from your AI tool](../building-from-your-ai-agent.md) for what happens next.

## Troubleshooting

* **Codex answers from the wrong org.** Run `codex mcp logout fastn`, then `codex mcp login fastn`, and pick the workspace again.
* **Fastn's tools are missing in the IDE extension.** The extension reads the same `~/.codex/config.toml`. Restart the extension after adding Fastn.
