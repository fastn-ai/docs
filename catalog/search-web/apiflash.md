---
description: "ApiFlash captures screenshots of web pages. Render any page to a JPEG, PNG or WebP image and check your remaining quota."
hidden: true
---

# ApiFlash

<img src="../../.gitbook/assets/connectors/lg/apiflash.png" alt="ApiFlash logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Authentication** | Access key |
| **Slug** | `apiflash` |

## Setup

Your customers enter their access key for ApiFlash when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect ApiFlash from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **ApiFlash**.
2. Select **Connect** on the ApiFlash card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use ApiFlash's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Capture Screenshot</td><td><code>captureScreenshot</code></td><td>Captures a screenshot of a web page and returns either the image binary or a JSON document containing hosted links to the screenshot and any extracted HTML or text. Every capture that is not served from the cache counts against your monthly quota.</td></tr><tr><td>Capture Screenshot With Form Body</td><td><code>captureScreenshotForm</code></td><td>Captures a screenshot of a web page using the form-encoded POST form of the endpoint. Behaves identically to Capture Screenshot but carries the parameters in the request body, which suits long values such as injected CSS or JavaScript that would exceed URL length limits.</td></tr><tr><td>Get Quota</td><td><code>getQuota</code></td><td>Returns the screenshot allowance for the current billing period: the plan limit, the number of calls remaining, and when the allowance resets.</td></tr></tbody></table>

