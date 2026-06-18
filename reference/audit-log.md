---
description: Audit log columns, filters, action types, and query patterns.
---

# Audit Log

The audit log records significant actions taken in your organization. It is found under **Settings → Audit Log**.

### Columns

| Column    | Description                                                                                   |
| --------- | --------------------------------------------------------------------------------------------- |
| TIMESTAMP | When the action occurred                                                                      |
| USER      | The actor that performed the action                                                           |
| ACTION    | A dotted event name (e.g., `workflow.execute.completed`, `workflow.publish`, `widget.create`) |
| RESOURCE  | The affected resource — an ID with a type sub-label (e.g., `workflow_executions`)             |

### Reading entries

Action values are structured event names. Some examples:

* `workflow.execute.completed` — A workflow execution finished
* `workflow.publish` — A workflow version was published
* `widget.create` — A widget was created

The RESOURCE cell shows the specific resource the action applied to, with its type beneath the ID.

Actions taken by AI agents are attributed to an agent actor rather than a human user.

### Related

* [Workflows](https://claude.ai/fastn/reference/workflows) — many audit entries reference workflow actions
* [RBAC & Security](https://claude.ai/fastn/reference/rbac-and-security) — who can perform which actions
