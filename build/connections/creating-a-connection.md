---
description: "Making a connection yourself with New connection: the system picker, key-based methods, OAuth with providers and scopes, and when to use it."
---

# Creating a connection

**New connection** on the Connections page connects an app for **your organization**. Use it for accounts your organization owns, such as your own Slack workspace or data warehouse, which your workflows then use. It is also the quickest way to test a connector end to end.

Your **customers'** connections should not be made here. Customers connect their own accounts through the [widget](../../embed/README.md) you embed, which keeps their credentials theirs.

### 1. Pick the system

**New connection** opens **Connect a system** · *Pick the system your customers use. You can add more later.*

Type in **Search systems** to narrow the grid, then click the system. The footer counts how many systems match. The list can take a few seconds to load (*Loading systems...*).

### 2. Give the credential

The dialog changes to **Connect &lt;system&gt;**, tagged with the selected auth method. **←** goes back to the picker.

#### Keys and tokens

For API key, bearer token, basic auth and custom methods, the dialog shows the fields the connector asks for. The placeholder usually says where to find the value.

Fill them in and click **Connect**.

#### Connecting with OAuth

| Part | Meaning |
| --- | --- |
| **Auth Method** | Shown when the connector offers more than one method. Starts on the default. |
| **Auth provider** | The OAuth app that sends you to the consent screen. **Default** marks the connector's preferred provider. If there are several, **⋯ → Change provider** picks another. See [Auth methods and providers](../connectors/auth-methods.md). |
| **Scopes** | With the default provider: *These are the permissions this connection will ask for on the consent screen. Pick only what you need - you can reconnect with more later.* With any other provider: *Pick only what your OAuth app has enabled - asking for a scope it was not granted makes the consent screen reject the whole connection.* With nothing selected (**All scopes (default)**), every scope the provider declares is requested, and the dialog warns: *Nothing selected, so every scope this provider declares will be requested.* |

Click **Authorise**. A new window opens on the app's sign-in and consent page. Sign in, approve access, and the window returns to fastn. *Nothing is stored here until you come back.*

#### Switching method

If the connector offers more than one method, changing **Auth Method** changes the form. For example, Airtable's **Bearer Token** method replaces the OAuth sign-in with a single **Bearer Token** field.

### 3. Check the result

The new connection appears in the **My organization** view and on the connector's **Connections** tab with the status `Active`.

{% hint style="info" %}
Every credential is *Stored encrypted and scoped to this organization. Your customers never see it, and you can revoke it at any time.* To revoke it, open the connection and click **Disconnect**.
{% endhint %}
