---
description: "Every REST endpoint you can call, generated from fastn's OpenAPI spec."
---

# REST API reference

This reference lists the REST endpoints you can call with an API key. It is generated from the platform's OpenAPI spec (release `v1.12.0`). To run workflows and mint embed tokens, start with the shorter [HTTP API](../api.md) guide.

* [Workflows](workflows.md): Create, publish, run and inspect workflows.
* [Installations and configs](installations.md): Each customer's setup of a widget, its triggers and its configuration values.
* [Widgets and embedding](widgets.md): Widgets, embed tokens, share links and setup links.
* [Triggers and events](triggers.md): Webhook, schedule and app event triggers, received events and the dead-letter queue.
* [Event subscriptions](event-subscriptions.md): Endpoints of yours that fastn delivers events to.
* [Connectors](connectors.md): Connectors, actions, auth methods, webhook configs and mock stubs.
* [Connections](connections.md): Connected accounts and how they are created.
* [Unified API](unified.md): Unified records, the catalog, and your own unified entities.
* [Alerts and observability](observability.md): Alert rules, traces and the audit log.
* [Environments and secrets](environments.md): Environments, their config values, and secrets.
* [Organization and access](organization.md): Customers, people, roles, teams and API keys.

## Base URL

```
https://api.fastn.dev
```

Paths here start with `/v1`. The same routes also answer under `/api/v1`, which is the form the [HTTP API](../api.md) guide uses.

## Authentication

Send an API key as a bearer token. Keys are created under [API keys and MCP](../../manage/api-keys.md).

```bash
curl https://api.fastn.dev/v1/installations \
  -H "Authorization: Bearer fsk_live_<your-key>"
```

A key can only do what its permissions allow, and a call can be limited further by your role, your plan or the customer it acts for. Some routes are meant for a person signed in to the dashboard or for an embed session, so they may refuse an API key with `401` or `403`.

To act for one of your customers, send `x-org-id` with fastn's id for that customer or your own id for it. A key that requires identity verification also needs `x-user-id` and `x-identity-hmac`. See [Authentication and API keys](../../tutorials/developer/authentication-and-api-keys.md).

## Responses and errors

Most routes wrap their result as `{ "data": ... }` and report a failure as `{ "error": "..." }` with an HTTP status code, often with a `code` you can match on. See [Errors and failure states](../errors.md). Rate limits are on the [HTTP API](../api.md#rate-limits) page.

## Operation names

Each endpoint lists its operation name. Where the endpoint is also a fastn MCP tool, the tool has the same name, so `listInstallations` here is `fastnPlatform__listInstallations` from your AI tool.

## Download the spec

The spec for everything on these pages, in OpenAPI 3.1 JSON, is at [openapi.json](https://raw.githubusercontent.com/fastn-ai/docs/main/reference/rest/openapi.json). Import it into Postman or a client generator.
