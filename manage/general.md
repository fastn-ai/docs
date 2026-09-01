---
description: Your organisation and how people join it.
---

# General

**Settings → General**

<figure><img src="../.gitbook/assets/settings-general.jpg" alt="General settings"><figcaption></figcaption></figure>

### Organisation

| Field        | Notes                                                                                              |
| ------------ | ---------------------------------------------------------------------------------------------------- |
| **Name**     | Shown to your team and on invitations.                                                              |
| **Timezone** | Sets the default timezone for new schedules. Dates elsewhere are shown in your own timezone.        |

{% hint style="info" %}
The timezone here is the default offered when creating a [schedule trigger](../build/triggers.md), not a global rewrite. A schedule keeps whatever timezone it was saved with.
{% endhint %}

### Joining by email domain

Anyone signing up with this domain can ask to join instead of waiting for an invite.

| Field                                  | Notes                                                                                                              |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Email domain**                       | Must be a domain your organisation controls, not a mailbox provider.                                                |
| **Approve automatically**              | Off means an admin approves each request. Leave it off unless the domain is yours alone.                            |
| **Role people joining on this domain get** | Viewer, Developer, Operator or End User. A starting point, not a limit — you can still invite someone as anything you are allowed to assign. |

{% hint style="warning" %}
Never set a mailbox provider here. Auto-approve on a shared domain means anyone with an address there can join your workspace.
{% endhint %}

### Deleting an organisation

Deletion is deliberately not on this page.

To delete a **customer**, open it under [Customers](../operate/customers.md). Suspend it first — that is what its Danger zone asks for — then delete it there. Deleting a customer removes its connections, workflows and stored credentials, and cannot be undone.

To delete **this organisation**, contact fastn support. An organisation has to be suspended before it can be deleted, and only fastn can suspend a top-level organisation — so there is no self-serve path, by design rather than by omission.

### Saving

Changes are staged. The footer shows whether there are unsaved changes; **Save changes** commits and **Discard** reverts.
