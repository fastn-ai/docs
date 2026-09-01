---
description: Deleted connectors, actions and workflows, kept until you remove them.
---

# Trash

**Settings → Trash**

<figure><img src="../.gitbook/assets/settings-trash.jpg" alt="The trash page"><figcaption></figcaption></figure>

> Deleted connectors land here, so a mistake is a restore rather than a rebuild.

Three tabs: **Connectors**, **Actions**, **Workflows**.

### What restore gives you back

Anything here is restored with its slug and history intact. That matters — a workflow that referenced a connector by slug keeps working after a restore, which would not be true if you rebuilt it from scratch.

### Nothing expires

Nothing is removed automatically. Items stay until you use **Delete permanently** to clear one for good.

{% hint style="danger" %}
**Delete permanently** cannot be undone. There is no second trash.
{% endhint %}

### What does not come here

> Other resources — widgets and their integrations among them — are deleted immediately and cannot be restored from this page.

So the recoverable set is exactly connectors, connector actions and workflows. Deleting a widget, a customer, a connection, a trigger or a secret is immediate and final.

### In the audit log

Soft deletes and restores are recorded distinctly, which is what lets you reconstruct what happened:

| Action                   | Meaning                          |
| ------------------------ | -------------------------------- |
| `connector.soft_delete`  | Moved to trash.                  |
| `connector.restore`      | Brought back.                    |
| `connector.delete`       | Removed permanently.             |
| `workflow.soft_delete`   | Moved to trash.                  |
| `workflow.restore`       | Brought back.                    |
| `action.delete`          | Connector action removed.        |
| `action.restore`         | Connector action brought back.   |

See [Audit log](audit-log.md).
