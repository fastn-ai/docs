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

## Use it

Add ApiFlash from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.apiflash.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Capture Screenshot</td><td><code>captureScreenshot</code></td><td>Captures a screenshot of a web page and returns either the image binary or a JSON document containing hosted links to the screenshot and any extracted HTML or text. Every capture that is not served from the cache counts against your monthly quota.</td></tr><tr><td>Capture Screenshot With Form Body</td><td><code>captureScreenshotForm</code></td><td>Captures a screenshot of a web page using the form-encoded POST form of the endpoint. Behaves identically to Capture Screenshot but carries the parameters in the request body, which suits long values such as injected CSS or JavaScript that would exceed URL length limits.</td></tr><tr><td>Get Quota</td><td><code>getQuota</code></td><td>Returns the screenshot allowance for the current billing period: the plan limit, the number of calls remaining, and when the allowance resets.</td></tr></tbody></table>

## Events

ApiFlash has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
