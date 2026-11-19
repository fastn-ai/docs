---
description: "Google IAM Service Account Credentials API (iamcredentials.googleapis.com v1)."
hidden: true
---

# Google IAM Service Account Credentials

<img src="../../.gitbook/assets/connectors/lg/google-iam-credentials.png" alt="Google IAM Service Account Credentials logo">

Creates short-lived credentials for a Google Cloud service account: OAuth 2.0 access tokens (generateAccessToken), OpenID Connect ID tokens (generateIdToken) and signatures over arbitrary bytes (signBlob). These actions act only on service accounts the connected user is allowed to impersonate (the user needs roles/iam.serviceAccountTokenCreator on the target service account). Authorizes with Google OAuth 2.0 using the scope https://www.googleapis.com/auth/iam.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [iamcredentials.googleapis.com](https://iamcredentials.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleIamCredentials` |

## Use it

Add Google IAM Service Account Credentials from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleIamCredentials.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Access Token</td><td><code>generateAccessToken</code></td><td>Generates a short-lived OAuth 2.0 access token for a Google Cloud service account by impersonating it. Works only for service accounts the connected user can impersonate (the user needs roles/iam.serviceAccountTokenCreator on that service account). Returns the access token and its expiry; treat the token as a secret. Requires the Google OAuth scope https://www.googleapis.com/auth/iam.</td></tr><tr><td>Generate ID Token</td><td><code>generateIdToken</code></td><td>Generates a Google-signed OpenID Connect ID token for a Google Cloud service account, for calling services that verify ID tokens (for example Cloud Run or Cloud Functions with authentication). Works only for service accounts the connected user can impersonate (roles/iam.serviceAccountTokenCreator on that service account). Returns the ID token (a JWT). Requires the Google OAuth scope https://www.googleapis.com/auth/iam.</td></tr><tr><td>Sign Blob</td><td><code>signBlob</code></td><td>Signs arbitrary bytes with a Google Cloud service account's Google-managed private key (useful for signed URLs or custom signatures). Works only for service accounts the connected user can impersonate (roles/iam.serviceAccountTokenCreator on that service account). Returns the signature and the ID of the key used. Requires the Google OAuth scope https://www.googleapis.com/auth/iam.</td></tr></tbody></table>
