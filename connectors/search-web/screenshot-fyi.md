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

## Use it

Add screenshot.fyi from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.screenshotFyi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Take Screenshot</td><td><code>takeScreenshot</code></td><td>Capture a screenshot of a public web page and return the hosted image URL on blob.screenshot.fyi. Supports viewport width/height, full-page capture, dark mode, png/jpg/jpeg output and automatic cookie-banner removal. BILLING: every successful call consumes one screenshot from the account's monthly quota (free plan: 100/month). The returned blob URL is publicly accessible to anyone who has it.</td></tr><tr><td>Verify Access Key</td><td><code>verifyAccessKey</code></td><td>Check that the stored screenshot.fyi access key is valid. Returns {"status":"ok"} for a valid key and 401 {"error":"Invalid access key"} otherwise. Consumes no screenshot quota, so it is the right connection health check.</td></tr></tbody></table>

## Events

screenshot.fyi has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
