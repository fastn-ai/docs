---
description: "ApiFlash is a Chrome-based screenshot API that renders any web page to a JPEG, PNG or WebP image."
hidden: true
---

# ApiFlash

ApiFlash is a Chrome-based screenshot API that renders any web page to a JPEG, PNG or WebP image. This connector covers the full documented surface: the GET and form-POST forms of the screenshot endpoint with every documented capture parameter (viewport and full-page capture, element and crop targeting, load-wait strategies, ad, tracker and cookie-banner blocking, geolocation, time zone, header and cookie injection, HTML and text extraction, caching, and direct upload to S3-compatible storage), plus the quota endpoint.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Authentication** | Credentials you enter |
| **Actions** | 3 |
| **Events** | 0 |
| **Slug** | `apiflash` |

## Use it

Add ApiFlash from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.apiflash.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Capture Screenshot | `captureScreenshot` | Captures a screenshot of a web page and returns either the image binary or a JSON document containing hosted links to the screenshot and any extracted HTML or text. Every capture that is not served from the cache counts against your monthly quota. |
| Capture Screenshot With Form Body | `captureScreenshotForm` | Captures a screenshot of a web page using the form-encoded POST form of the endpoint. Behaves identically to Capture Screenshot but carries the parameters in the request body, which suits long values such as injected CSS or JavaScript that would exceed URL length limits. |
| Get Quota | `getQuota` | Returns the screenshot allowance for the current billing period: the plan limit, the number of calls remaining, and when the allowance resets. |
