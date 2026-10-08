---
description: "What you can change on a connector your workspace owns: editing it, adding actions, publishing versions, restoring versions and deleting it."
---

# Editing, publishing and deleting

Everything on this page applies to connectors your workspace **owns**: ones you created with **Create connector** or brought in with **Import**. Managed connectors (badged `managed`, *Managed by Fastn*) are read-only in your workspace. To change one of their actions, use [Propose an update](action-detail.md#platform-owned-actions-and-propose-an-update).

### Edit a connector

Open the connector, then **⋯ → Edit** in the header. The **Edit connector** dialog has the same fields as [Create a connector](creating-a-connector.md): name, slug, description, protocol, domain, icon and auth methods. Save to apply the change. Saving creates a new version in **Test** (see below).

### Add, edit and delete actions

* **Add action** in the connector rail opens a form with **Name** (for example `Create Contact`) and **Slug** (derived from the name, for example `create-contact`; lowercase letters, numbers, hyphens and underscores). The slug cannot be changed after the action is created.
* Open an action to edit it in the [action editor](action-detail.md).
* Actions can be grouped into folders in the rail; a folder's **Add action to folder** button adds an action straight into it.
* Deleting an action is a soft delete by default, with an option to delete it permanently, the same as for connectors below.

### Manage auth providers

On the **Auth** tab of a connector you own, the providers button reads **Add provider** (no providers yet) or **Manage providers**. From there you can add your own OAuth app, and **Edit** or **Delete** an existing provider. **Delete** is disabled while a provider is in use; hovering it shows *In use by n connections*.

### Publish a version

Each save creates a new version in **Test**. Customers keep running the **Live** version until you publish.

1. Open the connector's **Overview** tab and scroll to **Versions**.
2. With **Test** selected, find the version and click **Publish this version**.
3. Confirm in the **Publish to live?** dialog:

   > *vX.Y* becomes the version your customers run. Connections and pins keep working; anyone not pinned moves to it immediately.

Customers pinned to another version (see [Version pins](inside-a-connector.md#version-pins)) stay on it.

### Restore a version

To roll back, find the earlier version under **Versions** and click **Restore this version**, then confirm in the **Restore Version** dialog. The connector returns to that version's definition.

### Delete a connector

**⋯ → Delete** opens **Delete Connector**:

> Are you sure you want to delete *&lt;name&gt;*?
>
> By default this is a soft delete — the connector is hidden but can be restored. Connected accounts are disconnected for good either way: restoring brings back the connector, not its credentials, so they have to be reconnected. Tick the box below to remove it permanently.

* **Soft delete** (the default): the connector disappears from the catalogue and can be restored. Every connection on it is disconnected and its credentials are deleted.
* **Permanently delete (cannot be undone)**: tick this box to remove the connector for good.

{% hint style="danger" %}
Either way, every workflow and trigger that uses the connector's connections stops working. Check who uses it on the **Connections** tab before deleting.
{% endhint %}
