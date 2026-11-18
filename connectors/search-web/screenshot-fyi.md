---
description: "screenshot.fyi is a simple hosted screenshot API: one call renders any public web page and returns a hosted image URL on blob.screenshot.fyi."
hidden: true
---

# screenshot.fyi

<img src="../../.gitbook/assets/connectors/screenshot-fyi.png" alt="screenshot.fyi logo" width="64">

screenshot.fyi is a simple hosted screenshot API: one call renders any public web page and returns a hosted image URL on blob.screenshot.fyi. This connector covers the complete public API surface at https://www.screenshot.fyi/api — the screenshot capture endpoint with every supported option (viewport width and height, full-page capture, dark mode, image format png/jpg/jpeg, and automatic cookie-banner removal) and the access-key verification endpoint. Captures are metered against the account plan (free plan: 100 screenshots/month).

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [screenshot.fyi](https://screenshot.fyi) |
| **Authentication** | API key |
| **Slug** | `screenshotFyi` |

## Use it

Add screenshot.fyi from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.screenshotFyi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Take Screenshot | `takeScreenshot` | Capture a screenshot of a public web page and return the hosted image URL on blob.screenshot.fyi. Supports viewport width/height, full-page capture, dark mode, png/jpg/jpeg output and automatic cookie-banner removal. BILLING: every successful call consumes one screenshot from the account's monthly quota (free plan: 100/month). The returned blob URL is publicly accessible to anyone who has it. |
| Verify Access Key | `verifyAccessKey` | Check that the stored screenshot.fyi access key is valid. Returns {"status":"ok"} for a valid key and 401 {"error":"Invalid access key"} otherwise. Consumes no screenshot quota, so it is the right connection health check. |
