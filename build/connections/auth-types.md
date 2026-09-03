---
description: The two shapes a connection's credential takes: OAuth and Custom/INPUT.
---

# Auth types

The `Auth` column mixes display names and raw enum values for the same concepts — you will see `OAuth 2.0` and `OAUTH` for one, `Custom` and `INPUT` for the other. They are the same two shapes:

**OAuth** — the customer signed in with the provider. fastn holds the refresh token and renews access tokens on its own. Whether that is still working is visible on the connection's detail page, under **Token and activity**.

**Custom / INPUT** — the customer pasted a key, token or connection string. These do not expire on their own but do break when rotated upstream.
