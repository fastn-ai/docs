---
description: Every runnable code sample in these docs, grouped by task, with its language.
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

# Code samples

Find a sample by what you want to do. Each link opens the page that holds the code and explains it.

## Runnable examples

Complete projects you can clone and run, in [fastn-ai/docs/examples](https://github.com/fastn-ai/docs/tree/main/examples):

| Example | What it does | Language |
| --- | --- | --- |
| [embed-node](https://github.com/fastn-ai/docs/tree/main/examples/embed-node) | A web page with the widget, and the backend route that mints its embed token | Node.js (Express) |
| [token-server-python](https://github.com/fastn-ai/docs/tree/main/examples/token-server-python) | A backend route that mints an embed token with signed identity headers | Python (Flask) |
| [crm-contacts-node](https://github.com/fastn-ai/docs/tree/main/examples/crm-contacts-node) | Finds or creates a contact in a customer's CRM, then adds a note | Node.js, `@fastn-ai/sdk` |
| [webhook-event-node](https://github.com/fastn-ai/docs/tree/main/examples/webhook-event-node) | Sends your product's event to a webhook trigger, signed for one customer | Node.js |

## Embed the widget

| Task | Languages | Sample |
| --- | --- | --- |
| Mint an embed token from your backend | curl, Node.js | [Embedding quickstart](../tutorials/developer/embedding-quickstart.md) |
| Mint a token with signed identity headers | curl, Node.js | [Generating embed tokens](../tutorials/developer/generating-embed-tokens.md) |
| Compute the identity hash | Node.js | [Verify caller identity](../manage/identity-verification.md) |
| Render the widget in an iframe | HTML | [Iframe](../embed/embedding/iframe.md) |
| Render the widget with the SDK, including React | HTML, JavaScript, React | [SDK](../embed/embedding/sdk.md) |
| Register a customer and create a connection for them | curl, JavaScript | [Integration flow](../embed/embedding/integration-flow.md) |
| Refresh a token | HTTP | [Tokens](../embed/embedding/token-api.md) |
| Create a customer MCP URL | curl | [Customer MCP URL](../embed/embedding/customer-mcp-url.md) |
| Handle widget callbacks | JSON payloads | [Widget callbacks](widget-callbacks.md) |

## Call Fastn from your backend

| Task | Languages | Sample |
| --- | --- | --- |
| Read and write a customer's CRM records | TypeScript, curl | [Read and write a customer's CRM records](../how-to/crm-records.md) |
| Run a workflow for one customer and read the result | curl | [Run an integration for one customer](../how-to/run-for-a-customer.md) |
| Send your product's events to a webhook trigger | Node.js | [Start an integration from your product's events](../how-to/events-from-your-product.md) |
| Build an integration end to end with the SDK | TypeScript | [SDK: end to end](sdk/end-to-end.md) |
| Manage customers | TypeScript | [SDK: customers](sdk/customers.md) |
| Connect apps for a customer | TypeScript | [SDK: connecting apps](sdk/connecting-apps.md) |
| Calendar and CRM records | TypeScript | [SDK: calendar and CRM](sdk/calendar-and-crm.md) |
| Any unified entity | TypeScript | [SDK: unified records](sdk/unified-records.md) |
| Call an app's own action directly | TypeScript | [SDK: direct app actions](sdk/app-actions.md) |
| Subscribe to events | TypeScript | [SDK: events](sdk/events.md) |
| Handle errors and retries | TypeScript | [SDK: errors, retries and options](sdk/errors-and-options.md) |
| Any other platform operation | TypeScript | [SDK: any other operation](sdk/any-operation.md) |

## Write workflows

| Task | Languages | Sample |
| --- | --- | --- |
| Read input, call connectors, use state, secrets, and configs | JavaScript | [Workflow runtime API](workflow-runtime.md) |
| Write a workflow in code | JavaScript | [Write a workflow in code](../tutorials/saas-admin/configuring-a-workflow-in-code.md) |
| Idempotent syncs, change detection, large volumes, backfills | JavaScript | [Common patterns](../build/patterns.md) |

## Connect an AI tool

| Task | Languages | Sample |
| --- | --- | --- |
| Add the Fastn MCP server to Claude Code | CLI, JSON | [Claude Code](../build/mcp-gateway/claude-code.md) |
| List and run your workspace's tools by name, for one customer | TypeScript | [SDK: workspace tools](sdk/workspace-tools.md) |
