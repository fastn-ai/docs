---
description: >-
  Create, run, deploy, and manage automated workflows between your connected
  apps using the flows namespace.
---

# Flows

The flows namespace provides programmatic access to Fastn's workflow orchestration engine. Access it through `fastn.flows`.

## `flows.list()`

List all flows in the current project.

```python
flows = fastn.flows.list()
for flow in flows:
    print(f"{flow['name']} — {flow['status']}")

# Filter by status
deployed = fastn.flows.list(status="DEPLOYED")
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `status` | `str` or `None` | No | `None` | Filter by status: `"DEPLOYED"`, `"DRAFT"`, etc. |

**Returns:** `list[dict]` — Each flow contains:

| Field | Type | Description |
|-------|------|-------------|
| `flow_id` | `str` | Flow identifier |
| `name` | `str` | Flow name |
| `description` | `str` | Flow description |
| `status` | `str` | Current status |
| `version` | `str` | Version number |
| `updatedAt` | `str` | Last update timestamp |
| `deployedAt` | `str` | Last deployment timestamp |

## `flows.get()`

Fetch the full definition of a specific flow.

```python
flow = fastn.flows.get("my-workflow")
print(flow["name"])
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `flow_name` | `str` | Yes | Flow name or ID |

**Returns:** `dict` — Complete flow definition including steps, triggers, and configuration.

**Raises:** `FlowNotFoundError` if the flow does not exist.

## `flows.generate()`

Generate a new flow using the AI flow builder agent. Describe your workflow in plain English.

```python
result = fastn.flows.generate(
    prompt="When a new Jira ticket is created, send a Slack notification to #engineering",
)
print(result)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | `str` | Yes | Plain-English description of the workflow |
| `session_id` | `str` or `None` | No | Session ID for multi-turn conversations |

**Returns:** `dict` — Generated flow details including flow ID and name.

{% hint style="info" %}
Pass a `session_id` to continue a previous conversation with the flow builder agent. This enables iterative refinement of generated flows.
{% endhint %}

The `create()` method is an alias for `generate()`.

## `flows.run()`

Execute a flow with optional input data.

```python
result = fastn.flows.run(
    "my-workflow",
    input_data={"name": "hello", "count": 5},
    stage="LIVE",
)
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `flow_name` | `str` | Yes | — | Flow name or ID |
| `input_data` | `dict` or `None` | No | `None` | Input parameters for the flow |
| `stage` | `str` or `None` | No | `None` | Stage to run against: `"DRAFT"` or `"LIVE"` |

**Returns:** `Any` — Flow execution result.

## `flows.deploy()`

Deploy a flow to a specific stage.

```python
result = fastn.flows.deploy(
    "my-workflow",
    stage="LIVE",
    comment="Production release v2",
)
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `flow_name` | `str` | Yes | — | Flow name or ID |
| `stage` | `str` | No | `"LIVE"` | Target stage: `"DRAFT"` or `"LIVE"` |
| `comment` | `str` | No | `""` | Deployment comment |

**Returns:** `dict` — Deployment result.

## `flows.schema()`

Discover the input schema for a flow by parsing its steps.

```python
schema = fastn.flows.schema("my-workflow")
print(schema["fields"])
print(schema["schema"])
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `flow_name` | `str` | Yes | Flow name or ID |

**Returns:** `dict` with:

| Field | Type | Description |
|-------|------|-------------|
| `fields` | `list` | Discovered input fields |
| `schema` | `dict` | JSON Schema representation |

## `flows.get_run()`

Get the status of a flow run.

```python
status = fastn.flows.get_run(run_id="run_xyz")
print(status["status"])     # e.g., "completed"
print(status["result"])     # execution result
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `run_id` | `str` | Yes | Run identifier |

**Returns:** `dict` with:

| Field | Type | Description |
|-------|------|-------------|
| `run_id` | `str` | Run identifier |
| `status` | `str` | Run status |
| `steps` | `list` | Step execution details |
| `started_at` | `str` | Start timestamp |
| `completed_at` | `str` | Completion timestamp |
| `result` | `Any` | Execution result (on success) |
| `error` | `Any` | Error details (on failure) |

## `flows.update()`

Update an existing flow's configuration.

```python
# Update the prompt
fastn.flows.update("flow_abc", prompt="Updated workflow description")

# Set a schedule
fastn.flows.update("flow_abc", schedule="0 9 * * MON-FRI")

# Enable or disable
fastn.flows.update("flow_abc", enabled=False)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `flow_id` | `str` | Yes | Flow ID |
| `prompt` | `str` or `None` | No | New prompt to regenerate the flow |
| `schedule` | `str` or `None` | No | Cron schedule (e.g., `"0 9 * * MON-FRI"`) |
| `enabled` | `bool` or `None` | No | Enable or disable the flow |
| `answers` | `dict` or `None` | No | Answers for flow builder agent questions |

**Returns:** `dict` — Updated flow details.

## `flows.delete()`

Delete a flow. Automatically resolves versioned names to the base flow ID.

```python
fastn.flows.delete("flow_abc")
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `flow_id` | `str` | Yes | Flow ID |

**Returns:** `dict` — Deletion result.

## Async usage

All flow methods have async equivalents on `AsyncFastnClient`:

```python
async with AsyncFastnClient() as fastn:
    flows = await fastn.flows.list()
    result = await fastn.flows.run("my-workflow", input_data={"key": "value"})
    status = await fastn.flows.get_run(run_id="run_xyz")
```
