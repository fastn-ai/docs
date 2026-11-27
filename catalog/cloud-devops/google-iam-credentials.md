---
description: "Google IAM Service Account Credentials creates short-lived credentials. Generate access and ID tokens for a service account and sign data."
hidden: true
---

# Google IAM Service Account Credentials

<img src="../../.gitbook/assets/connectors/lg/google-iam-credentials.png" alt="Google IAM Service Account Credentials logo">

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [iamcredentials.googleapis.com](https://iamcredentials.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleIamCredentials` |

## Setup

Your customers sign in to Google IAM Service Account Credentials through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google IAM Service Account Credentials from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google IAM Service Account Credentials**.
2. Select **Connect** on the Google IAM Service Account Credentials card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google IAM Service Account Credentials and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google IAM Service Account Credentials's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Access Token</td><td><code>generateAccessToken</code></td><td>Generates a short-lived OAuth 2.0 access token for a Google Cloud service account by impersonating it. Works only for service accounts the connected user can impersonate (the user needs roles/iam.serviceAccountTokenCreator on that service account). Returns the access token and its expiry; treat the token as a secret. Requires the Google OAuth scope https://www.googleapis.com/auth/iam.</td></tr><tr><td>Generate ID Token</td><td><code>generateIdToken</code></td><td>Generates a Google-signed OpenID Connect ID token for a Google Cloud service account, for calling services that verify ID tokens (for example Cloud Run or Cloud Functions with authentication). Works only for service accounts the connected user can impersonate (roles/iam.serviceAccountTokenCreator on that service account). Returns the ID token (a JWT). Requires the Google OAuth scope https://www.googleapis.com/auth/iam.</td></tr><tr><td>Sign Blob</td><td><code>signBlob</code></td><td>Signs arbitrary bytes with a Google Cloud service account's Google-managed private key (useful for signed URLs or custom signatures). Works only for service accounts the connected user can impersonate (roles/iam.serviceAccountTokenCreator on that service account). Returns the signature and the ID of the key used. Requires the Google OAuth scope https://www.googleapis.com/auth/iam.</td></tr></tbody></table>

