---
description: The four sections of a connection's detail view.
---

# Inside a connection

Opening a row gives four sections.

**Connection** — `Customer`, `Connector`, `Auth method`, `Scope` and `Connection ID`. Scope reads `Account level` when the connection is shared across the workspace rather than belonging to one customer. The connection id has the form:

```
ucl:org_<org>:<env>:<connectorId>:<authId>:<tenant>
```

The page's own note on it is the operative one:

> Pass this to the API to act as this customer.

**Token and activity** — `Expires`, `Last refreshed`, `Last used`, `Created`, `Updated`. This is where you check whether a refresh is still succeeding.

**Recent activity** — the last calls made on this connection, with **View all** into [Activity](../../operate/README.md).

**Danger zone** — **Disconnect this customer**:

> Syncing stops immediately and the credential is deleted.
