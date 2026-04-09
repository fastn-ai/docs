---
description: >-
  Configure the SDK with environment variables, config files, or constructor
  parameters. Understand the .fastn directory structure.
---

# Configuration

The SDK resolves configuration from multiple sources with a clear priority order. This page covers the `FastnConfig` dataclass, environment variables, and the `.fastn/` directory structure.

## Configuration priority

Configuration is resolved in this order (highest priority wins):

1. **Constructor parameters** — Values passed directly to `FastnClient()`
2. **Environment variables** — System environment variables
3. **Config file** — `.fastn/config.json` (created by `fastn login`)

## Environment variables

| Variable | Description | Example |
|----------|-------------|---------|
| `FASTN_API_KEY` | Platform API key | `fk_live_abc123...` |
| `FASTN_PROJECT_ID` | Project/workspace ID | `proj_xyz789...` |
| `FASTN_AUTH_TOKEN` | JWT access token | `eyJhbGciOi...` |
| `FASTN_TENANT_ID` | Default tenant ID | `acme-corp` |
| `FASTN_STAGE` | Deployment stage | `LIVE` |

For the agentic CLI (`fastn agent`), LLM provider keys are also read from the environment:

| Variable | Provider |
|----------|----------|
| `OPENAI_API_KEY` | OpenAI |
| `ANTHROPIC_API_KEY` | Anthropic |
| `GEMINI_API_KEY` | Google Gemini |

## FastnConfig

The `FastnConfig` dataclass holds all SDK configuration. It is created internally by the client but can be loaded directly for inspection.

```python
from fastn.config import load_config

config = load_config()
print(config.api_key)
print(config.project_id)
```

### Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `api_key` | `str` | `""` | Fastn platform API key |
| `project_id` | `str` | `""` | Project/workspace ID |
| `tenant_id` | `str` | `""` | Default tenant ID |
| `stage` | `str` | `"LIVE"` | Deployment stage: `"LIVE"`, `"STAGING"`, `"DEV"` |
| `timeout` | `float` | `30.0` | HTTP request timeout in seconds |
| `auth_token` | `str` | `""` | JWT access token |
| `refresh_token` | `str` | `""` | JWT refresh token |
| `token_expiry` | `str` | `""` | ISO-8601 token expiry timestamp |
| `llm_provider` | `str` | `""` | LLM provider: `"openai"`, `"anthropic"`, or `"gemini"` |
| `llm_api_key` | `str` | `""` | API key for the LLM provider |
| `llm_model` | `str` | `""` | Model name override |

### Methods

| Method | Description |
|--------|-------------|
| `validate()` | Raises `ConfigError` if no credentials or project ID are present |
| `to_dict()` | Serialize configuration to a dictionary |
| `resolve_project_id()` | Resolve project ID from field value or extract from JWT |
| `get_headers()` | Build the HTTP headers dictionary for API requests |

## Config file functions

The `fastn.config` module provides these utility functions:

| Function | Description |
|----------|-------------|
| `load_config(config_path=None)` | Load config from env vars + file. Optionally specify an explicit file path. |
| `save_config(config, directory=None)` | Save config to `.fastn/config.json` (permissions: `0o600`) |
| `find_fastn_dir(start_path=None)` | Walk up the directory tree to find `.fastn/` (like `.git` discovery) |
| `load_registry(fastn_dir=None)` | Load the connector registry from `.fastn/registry.json` |
| `save_registry(registry, fastn_dir=None)` | Save the connector registry |
| `load_manifest(fastn_dir=None)` | Load the connector manifest from `.fastn/manifest.json` |
| `save_manifest(manifest, fastn_dir=None)` | Save the connector manifest |
| `load_migrations(fastn_dir=None)` | Load migration records from `.fastn/migrations.json` |
| `save_migrations(migrations, fastn_dir=None)` | Save migration records |
| `get_installed_connectors(fastn_dir=None)` | Get list of installed connector names from the manifest |
| `add_connector_to_manifest(connector_name, version, fastn_dir=None)` | Add a connector to the installed list |
| `remove_connector_from_manifest(connector_name, fastn_dir=None)` | Remove a connector. Returns `True` if found. |
| `ensure_gitignore(directory=None)` | Ensure `.fastn/config.json` is in `.gitignore` |
| `infer_provider_from_model(model_name)` | Detect LLM provider from model name prefix |

## The `.fastn/` directory

The `fastn login` and `fastn connector sync` commands create a `.fastn/` directory in your project:

```
.fastn/
├── config.json       # Credentials and settings (chmod 0600)
├── registry.json     # Cached tool registry (connector definitions + schemas)
├── manifest.json     # Installed connectors with versions
└── migrations.json   # Backward-compatibility migration rules
```

{% hint style="warning" %}
The `config.json` file contains sensitive credentials. The SDK sets file permissions to `0600` (owner read/write only) and automatically adds it to `.gitignore`.
{% endhint %}

### Config discovery

The SDK searches for `.fastn/` by walking up the directory tree from the current working directory, similar to how Git finds the `.git/` directory. You can override this with the `config_path` constructor parameter.

## LLM provider configuration

The `fastn agent` CLI command supports three LLM providers:

| Provider | Default model | Available models |
|----------|---------------|------------------|
| OpenAI | `gpt-4.1-mini` | `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`, `o3`, `o3-mini`, `o4-mini`, `o1`, `o1-mini`, `o1-pro` |
| Anthropic | `claude-sonnet-4-20250514` | `claude-sonnet-4-20250514`, `claude-haiku-4-20250514`, `claude-opus-4-20250514`, `claude-3.5-sonnet-20241022`, `claude-3.5-haiku-20241022` |
| Google Gemini | `gemini-2.5-flash` | `gemini-2.5-pro`, `gemini-2.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite` |

Configure with environment variables or interactively via `fastn agent --setup`.

## API constants

| Constant | Value |
|----------|-------|
| `API_BASE_URL` | `https://live.fastn.ai/api/ucl` |
| `FLOWS_API_URL` | `https://live.fastn.ai/api/flows` |
| `FLOW_RUN_API_URL` | `https://live.fastn.ai/api/v1` |
| `FLOW_BUILDER_URL` | `https://live.fastn.ai/api/v1/flowBuilderAgent` |
| `CONNECTIONS_API_URL` | `https://live.fastn.ai/api/connections` |
| `GRAPHQL_URL` | `https://live.fastn.ai/api/graphql` |
| `DEFAULT_TIMEOUT` | `30.0` seconds |
| `MAX_RETRIES` | `3` |
| `BACKOFF_FACTOR` | `0.5` |
