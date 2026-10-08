---
description: "The values in the Auth column and on a connection's detail page, and what each one means for keeping the connection working."
---

# Auth types

The **Auth** column on the [Connections](README.md) page, and **Auth method** on a connection's detail page, show the type of auth method the connection was made with. They show the stored value, not a display name.

| Value | Method in the connect dialog | What the user gave | What keeps it working |
| --- | --- | --- | --- |
| `OAUTH_2` | OAuth 2.0 | Signed in to the app and approved access. | The access token expires, and fastn renews it with the refresh token. If renewal fails, the connection becomes `Expired`. |
| `API_KEY` | API Key | An API key. | The key staying valid in the app. Deleting or rotating it there breaks the connection. |
| `BEARER` | Bearer Token | A token, for example a personal access token. | The token staying valid in the app, including any expiry date the app sets. |
| `BASIC` | Basic Auth | A username and password. | The password not changing. |
| `DIGEST` | Digest Auth | A username and password. | The password not changing. |
| `INPUT` | Custom | The fields the connector defines, for example an account ID plus a key. | The entered values staying valid in the app. |
| `NO_AUTH` | No Auth | Nothing. | Nothing to keep up. |

The detail page adds a plain-language note under the value, for example *Your customer signed in and approved access.* for `OAUTH_2`.

For OAuth connections, check the **Token and activity** panel on the [detail page](inside-a-connection.md) to see when the token expires and when fastn last renewed it.

The full list of methods, and the fields each one asks for, is in [Creating a connector → Authentication](../connectors/creating-a-connector.md#authentication).
