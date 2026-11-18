---
description: "MemberVault is an online course and membership platform."
hidden: true
---

# MemberVault

<img src="../../.gitbook/assets/connectors/lg/member-vault.png" alt="MemberVault logo">

MemberVault is an online course and membership platform. This connector covers the complete MemberVault public API: listing the products in an account, granting a member access to a product, removing product access, and permanently deleting a member.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [membervault.co](https://membervault.co) |
| **Authentication** | Credentials you enter |
| **Slug** | `memberVault` |

## Use it

Add MemberVault from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.memberVault.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add User To Product</td><td><code>addUserToProduct</code></td><td>Grants a member access to a product, creating the member first if that email is not yet in the account. Pass -1 as the Product ID to create the member without granting access to anything. Existing members are never duplicated; they are found by email and given the additional product.</td></tr><tr><td>Delete User</td><td><code>deleteUser</code></td><td>Permanently deletes a member from the account together with all of their data, progress and quiz answers. This cannot be undone. Note that MemberVault answers 'User Deleted' even when no member with that email existed, so the response does not confirm that a member was actually removed. To revoke access to a single product while keeping the member, use Remove User From Product instead.</td></tr><tr><td>List Products</td><td><code>listProducts</code></td><td>Returns every product in the MemberVault account with its id and title. Use the returned product id as the Product ID when granting or removing a member's access. The account always includes the synthetic product id -1, which represents adding a member without granting access to anything.</td></tr><tr><td>Remove User From Product</td><td><code>removeUserFromProduct</code></td><td>Removes a member's access to one product. The member and their data stay in the account; only the product access is revoked. Use Delete User to remove the member entirely.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Content Completed</td><td><code>content.completed</code></td><td>Fires when a member marks a lesson or the whole product as complete. MemberVault has no webhook-subscription API, so this must be wired by hand once per product: sign in to the MemberVault admin, open the product, go to the Actions tab, add an Action with the completion trigger you want, choose 'Call a webhook' and paste this trigger URL. Append a literal parameter named 'event' with the value 'content.completed'. Payload schema below is modelled from MemberVault's documented Actions webhook fields, not captured from a live delivery.</td></tr><tr><td>Member Added To Product</td><td><code>user.added</code></td><td>Fires when a member is granted access to a product. MemberVault has no webhook-subscription API, so this must be wired by hand once per product: sign in to the MemberVault admin, open the product, go to the Actions tab, add an Action with the trigger 'when a user is added to this product', choose 'Call a webhook' and paste this trigger URL. MemberVault sends no event-type discriminator, so append a literal query parameter or body field named 'event' with the value 'user.added' to the URL you paste - without it the event cannot be routed and is silently dropped. Payload schema below is modelled from MemberVault's documented Actions webhook fields, not captured from a live delivery.</td></tr><tr><td>Member Removed From Product</td><td><code>user.removed</code></td><td>Fires when a member's access to a product is revoked. MemberVault has no webhook-subscription API, so this must be wired by hand once per product: sign in to the MemberVault admin, open the product, go to the Actions tab, add an Action with the trigger 'when a user is removed from this product', choose 'Call a webhook' and paste this trigger URL. Append a literal parameter named 'event' with the value 'user.removed', because MemberVault sends no discriminator of its own. Payload schema below is modelled from MemberVault's documented Actions webhook fields, not captured from a live delivery.</td></tr><tr><td>Quiz Submitted</td><td><code>quiz.submitted</code></td><td>Fires when a member submits a quiz or form inside a product. MemberVault has no webhook-subscription API, so this must be wired by hand once per product: sign in to the MemberVault admin, open the product, go to the Actions tab, add an Action on the quiz trigger, choose 'Call a webhook' and paste this trigger URL. Append a literal parameter named 'event' with the value 'quiz.submitted'. Payload schema below is modelled from MemberVault's documented Actions webhook fields, not captured from a live delivery.</td></tr></tbody></table>
