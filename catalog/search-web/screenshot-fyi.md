---
description: "screenshot.fyi captures web pages. Take a screenshot of any public page and get a hosted image link."
hidden: true
---

# screenshot.fyi

<img src="../../.gitbook/assets/connectors/lg/screenshot-fyi.png" alt="screenshot.fyi logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [screenshot.fyi](https://screenshot.fyi) |
| **Authentication** | API key |
| **Slug** | `screenshotFyi` |

## Setup

Your customers enter their API key for screenshot.fyi when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect screenshot.fyi from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **screenshot.fyi**.
2. Select **Connect** on the screenshot.fyi card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use screenshot.fyi's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Take Screenshot</td><td><code>takeScreenshot</code></td><td>Capture a screenshot of a public web page and return the hosted image URL on blob.screenshot.fyi. Supports viewport width/height, full-page capture, dark mode, png/jpg/jpeg output and automatic cookie-banner removal. BILLING: every successful call consumes one screenshot from the account's monthly quota (free plan: 100/month). The returned blob URL is publicly accessible to anyone who has it.</td></tr><tr><td>Verify Access Key</td><td><code>verifyAccessKey</code></td><td>Check that the stored screenshot.fyi access key is valid. Returns {"status":"ok"} for a valid key and 401 {"error":"Invalid access key"} otherwise. Consumes no screenshot quota, so it is the right connection health check.</td></tr></tbody></table>

