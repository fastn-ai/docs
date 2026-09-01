---
description: Which Postgres your workflows read and write through.
---

# Database

**Settings → Database**

<figure><img src="../.gitbook/assets/settings-database.jpg" alt="Database settings, shared versus your own"><figcaption></figcaption></figure>

Workflows can persist data with `fastn.db`. This page decides where that data lands.

> Every `fastn.db` call from this organisation goes here. Rows are never copied between the two, so switching changes where new reads and writes go and nothing else.

The banner shows the active schema name, in the form `ws_<32 hex characters>`.

### Two options

| | **Shared** — fastn runs it | **Your own** — you run it |
| --- | --- | --- |
| **Backups** | fastn | You |
| **Capacity** | fastn | You |
| **Uptime** | fastn | You |
| **Network setup** | None | Allow our runners |

**Shared** — fastn handles backups, patching, upgrades and capacity. Your workspace sits in its own schema, isolated from everyone else.

**Your own** — workflows connect to a Postgres you operate. You keep full control of the data and full responsibility for it. You will need to allow fastn's runners through your network.

### Reasons to bring your own

Data residency requirements, a compliance regime that will not accept a processor's database, or an existing warehouse you want workflow data to land in directly.

If none of those apply, Shared is less work and one fewer thing to page you at 3am.

{% hint style="danger" %}
Switching changes where **new** reads and writes go. Rows are never copied between the two. If a workflow depends on data written before the switch, it will not find it. Migrate deliberately, or not at all.
{% endhint %}

### Using it from a workflow

```javascript
await fastn.db.query(`
  CREATE TABLE IF NOT EXISTS sync_log (
    id SERIAL PRIMARY KEY,
    source_id TEXT,
    synced_at TIMESTAMP DEFAULT NOW()
  )
`);

await fastn.db.query(
  `INSERT INTO sync_log (source_id) VALUES ($1)`,
  [record.id]
);
```

Database access is customer-scoped: each customer gets an isolated context, so a query cannot read another customer's rows. See [Workflow runtime API](../reference/workflow-runtime.md).
