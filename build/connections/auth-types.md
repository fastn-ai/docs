---
description: "The values in the Auth column and on a connection's detail page, and what each one means for keeping the connection working."
---

# Auth types

The **Auth** column on the [Connections](README.md) page, and **Auth method** on a connection's detail page, show the type of auth method the connection was made with, as a display label. The stored value (what the API returns) is in the second column.

| Shown as | Stored value | What the user gave | What keeps it working |
| --- | --- | --- | --- |
| **OAuth 2.0** | `OAUTH_2` | Signed in to the app and approved access. | The access token expires, and fastn renews it with the refresh token. If renewal fails, the connection becomes `Expired`. |
| **API key** | `API_KEY` | An API key. | The key staying valid in the app. Deleting or rotating it there breaks the connection. |
| **Bearer token** | `BEARER` | A token, for example a personal access token. | The token staying valid in the app, including any expiry date the app sets. |
| **Basic auth** | `BASIC` | A username and password. | The password not changing. |
| **Digest auth** | `DIGEST` | A username and password. | The password not changing. |
| **Custom** | `INPUT` | The fields the connector defines, for example an account ID plus a key. | The entered values staying valid in the app. |
| **No auth** | `NO_AUTH` | Nothing. | Nothing to keep up. |
| **JWT bearer** | `JWT_BEARER` | The values the connector asks for to sign a JWT. | Those values staying valid in the app. |
| **AWS signature** | `AWS_SIGNATURE` | AWS credentials. | The credentials staying valid in AWS. |
| **OAuth 1.0** | `OAUTH_1` | Signed in to the app and approved access. | The app not revoking the grant. |

The detail page adds a plain-language note under the value, for example *Your customer signed in and approved access.* for **OAuth 2.0**.

For OAuth connections, check the **Token and activity** panel on the [detail page](inside-a-connection.md) to see when the token expires and when fastn last renewed it.

The full list of methods, and the fields each one asks for, is in [Creating a connector → Authentication](../connectors/creating-a-connector.md#authentication).
