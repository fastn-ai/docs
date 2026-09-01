---
description: Every action taken in this organisation.
---

# Audit log

**Settings → Audit log**

<figure><img src="../.gitbook/assets/settings-audit-log.jpg" alt="The audit log"><figcaption></figcaption></figure>

A complete, filterable record of everything anyone — or anything — did.

### The table

| Column       | Notes                                                                                   |
| ------------ | ----------------------------------------------------------------------------------------- |
| **Who**      | A person, an API key (`apikey:7`), or a service (`agent-se`).                            |
| **Action**   | The action name, e.g. `workflow.execute`, `auth.login`, `connector.publish`.              |
| **Resource** | The object acted on, with its type underneath.                                           |
| **Customer** | The customer scope, or **Organisation-wide**.                                            |
| **Result**   | Success or failure.                                                                      |
| **When**     | Timestamp.                                                                               |

### Filters

Search by person, action or resource; then narrow by **people**, **actions**, **types**, and a date range. **Export** downloads the filtered set.

### Action families

Actions are namespaced, which makes filtering practical.

| Prefix                          | Covers                                                                   |
| ------------------------------- | -------------------------------------------------------------------------- |
| `auth.*`                        | Logins.                                                                   |
| `api_key.*`                     | create, delete, revoke, roll, update.                                     |
| `connection.*`, `credential.*`  | Connection lifecycle, token refresh, refresh failures, redaction.         |
| `connector.*`                   | create, publish, promote, import, soft_delete, restore.                   |
| `connector_update_proposal.*`   | Proposal creation, agent runs, decisions, apply, fan-out.                 |
| `workflow.*`                    | create, update, publish, deploy, execute, rollback, replay, edit_code.    |
| `workflow.sync.*`               | GitHub review flow: requested, merged, rejected, cancelled.               |
| `secret.*`, `config.*`          | Secret and config changes. Values are never recorded.                     |
| `user.*`, `membership.*`, `custom_roles.*` | Access changes.                                                |
| `environment.*`                 | Environment creation, deletion, review requirements.                      |
| `impersonation.start`           | Support access into a workspace.                                          |
| `oauth.*`                       | initiate, complete, reconnect.                                            |
| `widget.*`, `installation.*`    | Widget and installation changes.                                          |

### Who can read it

Restricted to account owners and admins. This is enforced by role at the API layer — `/api/v1/audit-log` — and cannot be granted or revoked per user. See [People and roles](roles.md).

### What to look for

| Question                                | Filter                                                                 |
| --------------------------------------- | ------------------------------------------------------------------------ |
| Who changed this workflow?              | Action `workflow.update`, resource = the workflow.                      |
| Why did a connection start failing?     | `credential.token_refresh_failed`, plus `connection.*` for that customer. |
| Who created that API key?               | `api_key.create`.                                                       |
| What did this key do?                   | Filter by the key under **All people**.                                 |
| Did anyone touch production last night? | `workflow.deploy` plus the date range.                                  |

{% hint style="info" %}
Volume is high — a working organisation accumulates hundreds of thousands of events. Filter before you scroll, and export when you need to analyse.
{% endhint %}
