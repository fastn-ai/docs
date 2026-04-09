---
description: >-
  Complete command-line interface reference for the Fastn SDK CLI. Covers
  authentication, connector management, flows, agent, and Connect Kit commands.
---

# CLI reference

The Fastn CLI is installed with `pip install fastn-ai[cli]` and provides commands for authentication, connector management, workflow automation, and AI-powered tool execution.

## Global options

```bash
fastn [--verbose] [--version] <command>
```

| Option | Description |
|--------|-------------|
| `-v`, `--verbose` | Show API calls and responses |
| `--version` | Show SDK version and exit |

## Command overview

| Command | Description |
|---------|-------------|
| `fastn login` | Authenticate and select a project |
| `fastn logout` | Clear saved credentials |
| `fastn whoami` | Show the current logged-in user |
| `fastn connector` | Install and run tools from 250+ connectors |
| `fastn flow` | Build and run automated workflows |
| `fastn kit` | Manage the Connect Kit |
| `fastn skill` | List skills in the current project |
| `fastn agent` | AI-powered tool discovery and execution |
| `fastn version` | Show SDK and registry version |

---

## Authentication commands

### `fastn login`

Authenticate with Fastn and select a project.

```bash
fastn login
```

This command:

1. Runs the OAuth 2.1 device authorization flow (RFC 8628).
2. Opens your browser to the Fastn authorization page.
3. Displays a verification code for manual entry.
4. Saves auth tokens to `.fastn/config.json`.
5. Prompts you to select a workspace/project.

{% hint style="info" %}
If browser-based login fails, you can use the `FASTN_API_KEY` environment variable as an alternative authentication method.
{% endhint %}

### `fastn logout`

Clear saved credentials while preserving `project_id` and `api_key`.

```bash
fastn logout
```

### `fastn whoami`

Display the current authenticated user's name, email, and user ID.

```bash
fastn whoami
```

---

## Connector commands

### `fastn connector ls`

List connectors, or show tools for a specific connector.

```bash
# List all available connectors
fastn connector ls

# Show tools for a specific connector
fastn connector ls slack

# Show only active connectors
fastn connector ls --active

# Show only locally installed connectors
fastn connector ls --installed

# Show tool schemas in detail
fastn connector ls slack --verbose
```

| Argument/Option | Type | Description |
|-----------------|------|-------------|
| `connector_name` | positional (optional) | Show tools for this connector |
| `--active` | flag | Show only connectors with active connections |
| `--installed` | flag | Show only locally installed connectors |
| `-v`, `--verbose` | flag | Show input/output schemas for each tool |

{% hint style="info" %}
You can use `fastn connector slack` as a shortcut for `fastn connector ls slack`.
{% endhint %}

### `fastn connector add`

Download full tool schemas for specific connectors. This enhances IDE autocomplete by generating type stubs.

```bash
# Add a single connector
fastn connector add slack

# Add multiple connectors
fastn connector add slack hubspot jira
```

| Argument | Type | Description |
|----------|------|-------------|
| `connector_names` | positional (one or more) | Connectors to add |

This command fetches tool schemas via GraphQL, caches them in `.fastn/registry.json`, adds connectors to the manifest, and regenerates `.pyi` type stubs for IDE autocomplete.

### `fastn connector remove`

Remove connector stubs and uninstall from the manifest.

```bash
fastn connector remove slack
```

### `fastn connector sync`

Sync all connectors, fetch tool schemas, and regenerate type stubs.

```bash
# Standard sync (preserves cached schemas)
fastn connector sync

# Force re-fetch all schemas
fastn connector sync --force
```

| Option | Description |
|--------|-------------|
| `--force` | Re-fetch all tool schemas even if cached |

The sync process fetches connectors from three scopes (workspace, organization, community), downloads tool schemas in parallel (10 concurrent workers), detects breaking changes, and generates migration records for backward compatibility.

### `fastn connector run`

Execute a connector tool from the command line.

```bash
# List available tools
fastn connector run slack

# Execute with inline parameters
fastn connector run slack send_message --channel general --text "Hello!"

# Execute with connection override
fastn connector run slack send_message --connection-id conn_abc --channel general --text "Hello!"

# Execute as a specific tenant
fastn connector run slack send_message tenant_123 --channel general --text "Hello!"
```

| Argument/Option | Type | Description |
|-----------------|------|-------------|
| `connector_name` | positional | Connector name |
| `tool_name` | positional (optional) | Tool to execute |
| `tenant_id` | positional (optional) | Tenant ID |
| `--connection-id` | string | Connection ID override |
| `--tenant` | string | Tenant ID override |
| `--key value` | extra args | Tool parameters as key-value pairs |

Without a `tool_name`, the command lists available tools. Without extra arguments, it prompts interactively for required and optional fields.

**Parameter parsing:**

| Input | Parsed as |
|-------|-----------|
| `--channel general` | `{"channel": "general"}` |
| `--count 5` | `{"count": 5}` |
| `--verbose true` | `{"verbose": true}` |
| `--tags '["a","b"]'` | `{"tags": ["a", "b"]}` |
| `--flag` (no value) | `{"flag": true}` |

### `fastn connector schema`

Show raw JSON Schema for a connector's tools.

```bash
# All tools for a connector
fastn connector schema slack

# Single tool
fastn connector schema slack send_message
```

---

## Flow commands

### `fastn flow ls`

List all flows in the current project.

```bash
# List all flows
fastn flow ls

# Filter by status
fastn flow ls --status deployed

# Verbose output
fastn flow ls -v
```

| Option | Description |
|--------|-------------|
| `--status`, `-s` | Filter by status: `deployed`, `draft`, `pending` |
| `-v`, `--verbose` | Show API calls and responses |

### `fastn flow generate`

Generate a flow using the AI flow builder agent.

```bash
fastn flow generate --prompt "When a Jira ticket is created, notify Slack"
```

| Option | Type | Required | Description |
|--------|------|----------|-------------|
| `--prompt`, `-p` | string | Yes | Plain-English description of the workflow |

This starts an interactive session with the flow builder agent. You can refine the flow through follow-up prompts. The session ends on empty input or Ctrl+C.

### `fastn flow run`

Execute a flow.

```bash
# Interactive mode (prompts for input fields)
fastn flow run my-workflow

# With inline input data
fastn flow run my-workflow --input '{"name": "hello"}'

# Specify stage
fastn flow run my-workflow --stage DRAFT
```

| Argument/Option | Type | Description |
|-----------------|------|-------------|
| `flow_name` | positional | Flow name or ID |
| `--stage`, `-s` | `DRAFT` or `LIVE` | Deployment stage |
| `--input`, `-d` | JSON string | Input data |

Without `--input`, the command auto-discovers the flow's input schema and prompts interactively for each field.

### `fastn flow deploy`

Deploy a flow to a stage.

```bash
fastn flow deploy my-workflow --stage LIVE --comment "Production release"
```

| Argument/Option | Type | Default | Description |
|-----------------|------|---------|-------------|
| `flow_name` | positional | — | Flow name or ID |
| `--stage`, `-s` | `DRAFT` or `LIVE` | `LIVE` | Target stage |
| `--comment`, `-m` | string | `""` | Deployment comment |

### `fastn flow schema`

Show the input/output schema of a flow in AI tool format.

```bash
fastn flow schema my-workflow
```

Returns JSON with `name`, `description`, `toolId`, `inputSchema`, and `outputSchema` — ready for LLM tool calling.

### `fastn flow update`

Update an existing flow.

```bash
# Update the prompt
fastn flow update flow_abc --prompt "Updated workflow description"

# Set a schedule
fastn flow update flow_abc --schedule "0 9 * * MON-FRI"

# Disable
fastn flow update flow_abc --disabled
```

| Argument/Option | Type | Description |
|-----------------|------|-------------|
| `flow_id` | positional | Flow ID |
| `--prompt`, `-p` | string | New prompt to regenerate the flow |
| `--schedule` | string | Cron schedule expression |
| `--enabled` / `--disabled` | flag | Enable or disable the flow |

### `fastn flow delete`

Delete a flow.

```bash
# With confirmation prompt
fastn flow delete flow_abc

# Skip confirmation
fastn flow delete flow_abc --yes
```

| Option | Description |
|--------|-------------|
| `--yes`, `-y` | Skip the confirmation prompt |

---

## Connect Kit commands

### `fastn kit ls`

List Connect Kit connectors in the current project.

```bash
# List all
fastn kit ls

# Search
fastn kit ls --query slack
```

| Option | Type | Description |
|--------|------|-------------|
| `--query`, `-q` | string | Search query to filter connectors |

### `fastn kit get`

Get full details for a Connect Kit connector by name.

```bash
fastn kit get slack
```

Returns the complete JSON with actions, events, connected connectors, and metadata.

### `fastn kit config`

Show or update Connect Kit configuration.

```bash
# Show current config
fastn kit config

# Update configuration
fastn kit config --data '{"showFilterBar": true, "isRBACEnabled": true}'
```

| Option | Type | Description |
|--------|------|-------------|
| `--data`, `-d` | JSON string | Configuration fields to update |

Supported fields: `authenticationApi`, `isCustomAuthenticationEnabled`, `showFilterBar`, `showLabels`, `styles`, `labelsLayout`, `disableFor`, `filterWidgets`, `isRBACEnabled`, `advancedSettings`.

---

## Other commands

### `fastn skill`

List all agent skills in the current project.

```bash
fastn skill
```

Displays a table with Name, Description, and ID columns.

### `fastn agent`

Give a goal in plain English — the agent discovers tools, calls an LLM, and executes tool calls in a loop.

```bash
# Basic usage
fastn agent Send a welcome message to #general on Slack

# Scoped to a connector
fastn agent --connector slack "List all channels"

# Scoped to a specific tool
fastn agent --tool slack_send_message "Send hello to #general"

# Auto-confirm tool calls
fastn agent -y "Create a Jira ticket for the login bug"

# Custom model
fastn agent --model gpt-4o "Summarize open GitHub issues"

# Re-run LLM setup
fastn agent --setup "Send a message"
```

| Argument/Option | Type | Default | Description |
|-----------------|------|---------|-------------|
| `prompt` | positional | — | Natural language task description |
| `--connector` | string | `None` | Scope tool discovery to a connector |
| `--tool` | string | `None` | Scope discovery to a specific tool |
| `--connection-id` | string | `None` | Connection ID for multi-connection connectors |
| `--max-turns` | int | `10` | Maximum agentic loop iterations |
| `-y`, `--yes` | flag | `False` | Skip confirmation prompts |
| `--eval` | flag | `False` | Evaluate whether the agent selected the right tools |
| `--max-errors` | int | `2` | Stop after this many consecutive errors |
| `--max-tools` | int | `5` | Maximum tools sent to the LLM |
| `--model` | string | `None` | Override LLM model |
| `--setup` | flag | `False` | Re-run LLM provider/model setup |
| `--tenant` | string | `None` | Tenant ID override |

**First-time setup:** If no LLM is configured, the agent command runs an interactive setup to select a provider (OpenAI, Anthropic, Gemini) and model, then prompts for an API key. Configuration is saved to `.fastn/config.json`.

**Evaluation mode (`--eval`):** Uses the LLM as a QA judge to verify intent, tool selection, target accuracy, and result. Outputs a PASS/FAIL verdict.

{% hint style="warning" %}
The agentic loop currently supports OpenAI models only. Anthropic and Gemini are supported for parameter extraction but not the full agent loop.
{% endhint %}

### `fastn version`

Show the SDK version and registry sync status.

```bash
fastn version
```

Output:

```
Fastn SDK v0.3.7
Registry version: <version or "not synced">
Last synced: <timestamp or "never">
```

---

## Complete command tree

```
fastn [--verbose] [--version]
├── login
├── logout
├── whoami
├── connector
│   ├── ls [CONNECTOR] [--active] [--installed] [-v]
│   ├── add CONNECTOR [CONNECTOR ...]
│   ├── remove CONNECTOR
│   ├── sync [--force]
│   ├── run CONNECTOR [TOOL] [TENANT] [--connection-id] [--tenant] [--key value]
│   └── schema CONNECTOR [TOOL]
├── flow [-v]
│   ├── ls [--status STATUS] [-v]
│   ├── generate --prompt TEXT
│   ├── run FLOW [--stage] [--input JSON]
│   ├── deploy FLOW [--stage] [--comment TEXT]
│   ├── schema FLOW
│   ├── update FLOW_ID [--prompt] [--schedule] [--enabled|--disabled]
│   └── delete FLOW_ID [--yes]
├── kit
│   ├── ls [--query TEXT]
│   ├── get NAME
│   └── config [--data JSON]
├── skill
├── agent PROMPT [--connector] [--tool] [--connection-id] [--max-turns]
│         [-y] [--eval] [--max-errors] [--max-tools] [--model] [--setup] [--tenant]
└── version
```
