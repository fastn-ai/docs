---
description: How the embed token scopes the widget to one customer, and to one person at that customer
---

# Understanding Tenancy

Every widget session in fastn is scoped twice: to one **customer** (a company using your product), and to one **person** at that customer. Both come from the embed token your backend mints. Nothing in the iframe URL changes either of them.

### The customer

The customer is named when your backend mints the token, by the `x-org-id` header (or `orgId` in the body). Either value can be your own id for the customer (the external reference you registered it under) or fastn's id for it (see [Finding Your Org Identifier](finding-your-org-identifier.md)). A token always belongs to exactly one customer, and the widget shows that customer's integrations and connections only.

A token minted without a customer is refused (`400`, code `EMBED_TOKEN_REQUIRES_END_ORG_ID`) unless you explicitly ask for an organization-level token with `allowOrgLevel: true`. That kind of token is for previewing your own organization only; never hand one to a customer.

### The person

Within a customer, per-user isolation keys on the **user id**:

* send `userId` in the token request body, or
* send `x-user-id` on the token request, attested with an identity hash when the API key has identity verification turned on (see [API keys](../../manage/api-keys.md)).

`userEmail` and `userName` are for display only; they do not decide whose session it is. If you send no user id at all, each token gets a random `embed_usr…` id, so nothing a person does carries over to their next session. Send a stable id from your own user table.

### How it's set in the embed

The iframe takes the token, and only the token:

```
https://api.fastn.dev/api/v1/embed/iframe?token=<token>
```

The customer and the user are inside the token, put there when your backend minted it. You do not add a `tenant-id` parameter. If an older snippet still carries one, it must name the same customer as the token: when the two disagree, the widget refuses the session rather than guess. Drop the parameter and let the token name the customer.

### What this means for your backend

1. When a signed-in person opens the page that hosts the widget, look up which customer they belong to and their user id.
2. Mint a token for that customer and that user.
3. Hand only the token to the browser.

See [Generating Embed Tokens](generating-embed-tokens.md) for the full request.
