---
description: Who can see and change things in this workspace.
---

# People

**Settings → People**

<figure><img src="../.gitbook/assets/settings-people.jpg" alt="The people list"><figcaption></figcaption></figure>

| Column     | Notes                                                            |
| ---------- | ------------------------------------------------------------------ |
| **Person** | Name and email.                                                  |
| **Role**   | Their assigned role. **Change role** edits it.                   |
| **Status** | Active, Invited, Disabled or Suspended.                          |
| **Added**  | When they joined.                                                |
| **Access** | Any scoping beyond the role.                                     |

Filter chips carry a count per role — Everyone, Owner, Admin and so on — and the dropdown on the right filters by status. Checkboxes on each row allow bulk actions.

### Inviting someone

**Invite someone** sends an invitation to an email address with a role attached. Until they accept, they appear with status **Invited**.

If you have set up [domain joining](general.md), people on that domain can request access instead of waiting for an invite, and the role you configured there is preselected when you invite them.

### Changing a role

**Change role** on any row. What you may assign is bounded by your own role — you cannot grant more than you hold.

The Owner's role cannot be changed from this screen. Ownership is transferred by the Owner, and there is exactly one per organisation.

### Removing someone

The trash icon removes a person from the workspace. Their audit-log history stays, so *who did what* remains answerable after they leave.

{% hint style="info" %}
Removing a person does not revoke API keys they created — keys belong to the workspace, not to a person. Check [API keys](api-keys.md) and rotate anything they had access to.
{% endhint %}

### Statuses

| Status        | Meaning                                       |
| ------------- | ----------------------------------------------- |
| **Active**    | Signed up and usable.                          |
| **Invited**   | Invitation sent, not yet accepted.             |
| **Disabled**  | Cannot sign in. Reversible.                    |
| **Suspended** | Access withdrawn pending a decision.           |

What each role can actually do is on the next page.

{% content-ref url="roles.md" %}[Roles](roles.md){% endcontent-ref %}
