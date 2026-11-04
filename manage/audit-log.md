---
description: Every action taken in this organization.
---

# Audit log

**Settings → Audit log**

<figure><img src="../.gitbook/assets/settings-audit-log.jpg" alt="The Audit log with its event total in the header, over rows of connection.update attributed to apikey:8 and workflow.execute and auth.login attributed to people whose names are obscured, each Success, scoped to a customer id or Organization-wide"><figcaption>Filters for people, actions, types and a date range sit above the table, with Export top-right.</figcaption></figure>

A complete, filterable record of everything anyone (or anything) did. The header carries the total, which stops counting at 10,000: past that it reads **10,000+ events**.

### The table

| Column       | Notes                                                                                   |
| ------------ | ----------------------------------------------------------------------------------------- |
| **Who**      | A person, or an API key in the form `apikey:8`.                                          |
| **Action**   | The action name: `auth.login`, `workflow.execute`, `connection.update`.                 |
| **Resource** | The object acted on, with its type underneath.                                           |
| **Customer** | The customer scope, or **Organization-wide**.                                            |
| **Result**   | **Success**, **Failed**, or **Not recorded** when the entry carries no outcome.          |
| **When**     | Timestamp.                                                                               |

### Filters

**Search by person, action or resource** needs at least 3 letters or digits in a row before it searches. Then narrow by **All people**, **All actions**, **All types**, and a date range.

**Export** downloads a CSV of every row the current filters match, up to 5,000 rows. Its columns are Time, Person, Email, Action, Resource type, Resource, Customer and Outcome. Filter first if you need a specific slice of a large log.

### Action families

Actions are namespaced, which is what makes filtering practical: `auth.login`, `workflow.execute` and `workflow.execute.completed` are all confirmed, and the pattern is `<resource>.<verb>`, sometimes with a terminal state appended.

Beyond those, the surest way to see what your organization actually emits is the **All actions** dropdown on this page. It lists the real vocabulary. Expect namespaces along these lines, but confirm there before you build a filter or an alert on one:

| Prefix                          | Likely covers                                                            |
| ------------------------------- | -------------------------------------------------------------------------- |
| `auth.*`                        | Logins. `auth.login` confirmed.                                           |
| `workflow.*`                    | Workflow lifecycle and runs. `workflow.execute` and `workflow.execute.completed` confirmed. |
| `api_key.*`                     | Key creation, rotation and revocation.                                    |
| `connection.*`                  | Connection lifecycle. `connection.update` confirmed.                      |
| `connector.*`                   | Connector creation, publishing and deletion.                              |
| `secret.*`, `config.*`          | Secret and config changes, who and when, not values.                     |
| `user.*`, `membership.*`        | Access changes.                                                           |
| `environment.*`                 | Environment changes.                                                      |

### Who can read it

Restricted to account owners and admins. This is enforced by role at the API layer (`/api/v1/audit-log`) and cannot be granted or revoked per user. See [Roles](roles.md).

### What to look for

| Question                                | Where to start                                                          |
| --------------------------------------- | ------------------------------------------------------------------------ |
| Who changed this workflow?              | Filter to the workflow as the resource, then pick its update action.     |
| Why did a connection start failing?     | Filter to that customer, then to the connection actions.                 |
| Who created that API key?               | Filter to the key-creation action in **All actions**.                    |
| What did this key do?                   | Filter by the key. It appears under **All people** as `apikey:<n>`.     |
| Did anyone touch production last night? | The deploy action plus the date range.                                   |

{% hint style="info" %}
Filter before you scroll, and export when you need to analyze. At this volume, scrolling is not a search strategy.
{% endhint %}
