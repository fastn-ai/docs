---
description: How your backend, your frontend and your customers authenticate with Fastn, and where to start.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Authentication

Your backend holds an API key and uses it for every call to Fastn. Your frontend only ever gets a short-lived embed token for one customer. Fastn keeps each customer's sign-in to their apps, so your code never handles them.

<figure><img src="../../.gitbook/assets/diagrams/auth-flow.svg" alt="How authentication works: your backend mints an embed token from Fastn with your API key, passes only the token to your frontend, which opens the widget; the customer signs in to their app and Fastn saves the credential."><figcaption><p>Your API key stays on your backend. Only the short-lived token reaches the browser.</p></figcaption></figure>

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>How authentication works</strong></td><td>The credentials Fastn uses, where each one lives, how a call names a customer, and the difference between Test and Live keys.</td><td><a href="how-authentication-works.md">how-authentication-works.md</a></td></tr>
<tr><td><strong>Set up authentication</strong></td><td>Create an API key, choose an environment, make your first authenticated request, and switch to a Live key.</td><td><a href="set-up-authentication.md">set-up-authentication.md</a></td></tr>
</tbody></table>

### Related

* [API keys](../../manage/api-keys.md): every option in the **Create an API key** dialog, and how to rotate and revoke keys.
* [Environments and GitHub](../../manage/environments.md): the stages your workflows deploy to.
* [Verify caller identity](../../manage/identity-verification.md): sign each call, so it can't claim to be another customer.
* [Generate embed tokens](generating-embed-tokens.md): get, refresh and use the token that opens the widget.
* [HTTP API authentication](../../reference/api.md#authentication): the headers each endpoint reads.
