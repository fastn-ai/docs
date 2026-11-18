---
description: "MemberVault is an online course and membership platform."
---

# MemberVault

MemberVault is an online course and membership platform. This connector covers the complete MemberVault public API: listing the products in an account, granting a member access to a product, removing product access, and permanently deleting a member.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [membervault.co](https://membervault.co) |
| **Authentication** | Credentials you enter |
| **Actions** | 4 |
| **Events** | 4 |
| **Slug** | `memberVault` |

## Use it

Add MemberVault from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.memberVault.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add User To Product | `addUserToProduct` | Grants a member access to a product, creating the member first if that email is not yet in the account. Pass -1 as the Product ID to create the member without granting access to anything. Existing members are never duplicated; they are found by email and given the additional product. |
| Delete User | `deleteUser` | Permanently deletes a member from the account together with all of their data, progress and quiz answers. This cannot be undone. Note that MemberVault answers 'User Deleted' even when no member with that email existed, so the response does not confirm that a member was actually removed. To revoke access to a single product while keeping the member, use Remove User From Product instead. |
| List Products | `listProducts` | Returns every product in the MemberVault account with its id and title. Use the returned product id as the Product ID when granting or removing a member's access. The account always includes the synthetic product id -1, which represents adding a member without granting access to anything. |
| Remove User From Product | `removeUserFromProduct` | Removes a member's access to one product. The member and their data stay in the account; only the product access is revoked. Use Delete User to remove the member entirely. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Content Completed | `content.completed` | Fires when a member marks a lesson or the whole product as complete. MemberVault has no webhook-subscription API, so this must be wired by hand once per product: sign in to the MemberVault admin, open the product, go to the Actions tab, add an Action with the completion trigger you want, choose 'Call a webhook' and paste this trigger URL. Append a literal parameter named 'event' with the value 'content.completed'. Payload schema below is modelled from MemberVault's documented Actions webhook fields, not captured from a live delivery. |
| Member Added To Product | `user.added` | Fires when a member is granted access to a product. MemberVault has no webhook-subscription API, so this must be wired by hand once per product: sign in to the MemberVault admin, open the product, go to the Actions tab, add an Action with the trigger 'when a user is added to this product', choose 'Call a webhook' and paste this trigger URL. MemberVault sends no event-type discriminator, so append a literal query parameter or body field named 'event' with the value 'user.added' to the URL you paste - without it the event cannot be routed and is silently dropped. Payload schema below is modelled from MemberVault's documented Actions webhook fields, not captured from a live delivery. |
| Member Removed From Product | `user.removed` | Fires when a member's access to a product is revoked. MemberVault has no webhook-subscription API, so this must be wired by hand once per product: sign in to the MemberVault admin, open the product, go to the Actions tab, add an Action with the trigger 'when a user is removed from this product', choose 'Call a webhook' and paste this trigger URL. Append a literal parameter named 'event' with the value 'user.removed', because MemberVault sends no discriminator of its own. Payload schema below is modelled from MemberVault's documented Actions webhook fields, not captured from a live delivery. |
| Quiz Submitted | `quiz.submitted` | Fires when a member submits a quiz or form inside a product. MemberVault has no webhook-subscription API, so this must be wired by hand once per product: sign in to the MemberVault admin, open the product, go to the Actions tab, add an Action on the quiz trigger, choose 'Call a webhook' and paste this trigger URL. Append a literal parameter named 'event' with the value 'quiz.submitted'. Payload schema below is modelled from MemberVault's documented Actions webhook fields, not captured from a live delivery. |
