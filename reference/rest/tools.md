---
description: "Download Fastn's OpenAPI spec and a Postman collection, and call the REST API from Postman or Bruno."
---

# OpenAPI spec and Postman collection

At the end of this page you can call any endpoint in the [REST API reference](README.md) from Postman or Bruno, with your API key filled in once.

## Before you start

* You need a Fastn API key. Create one under [API keys](../../manage/api-keys.md). Use a test key (`fsk_test_…`) while you explore.
* Your role and the key's permissions decide which calls succeed. A call the key is not allowed to make is answered `401` or `403`.

{% hint style="info" %}
Test keys act on real data. See [API keys](../../manage/api-keys.md).
{% endhint %}

## Downloads

| File | What it is |
| --- | --- |
| [openapi.json](https://raw.githubusercontent.com/fastn-ai/docs/main/reference/rest/openapi.json) | The OpenAPI 3.1 spec for every endpoint in the REST API reference. Use it with a client generator, a mock server or any tool that reads OpenAPI. |
| [fastn.postman\_collection.json](https://raw.githubusercontent.com/fastn-ai/docs/main/reference/rest/fastn.postman_collection.json) | A Postman collection (v2.1) generated from that spec: one request per endpoint, grouped in folders by resource. |

Both are generated from the same release as the reference pages, so they list the same endpoints.

## Import the collection into Postman

1. In Postman, select **Import**, then paste the collection link from [Downloads](#downloads) or drop in the downloaded file.

   **You should see:** a collection named **Fastn REST API** with a folder per resource, such as **Workflows** and **Connectors**.
2. Open the collection, select the **Variables** tab, and set `apiKey` to your test key. Save.

   **You should see:** three variables: `baseUrl` (`https://api.fastn.dev`), `apiKey` (your key) and `testMode` (`true`).
3. Open **Workflows**, pick a `GET` request that lists workflows, and select **Send**.

   **You should see:** a `200` response with your workflows under `data`.

## Import the collection into Bruno

Bruno imports Postman collections.

1. Download `fastn.postman_collection.json` from [Downloads](#downloads).
2. In Bruno, choose **Import Collection**, then **Postman Collection**, and pick the file.
3. Open the collection settings and set `apiKey` under its variables. If the import did not bring the variables over, add `baseUrl`, `apiKey` and `testMode` yourself with the values in the table below.

   **You should see:** the same list request returns `200`.

## Variables and headers

Every request sends the key and the test-mode flag as headers, so there is no auth to configure per request.

| Variable | Default | Sent as |
| --- | --- | --- |
| `baseUrl` | `https://api.fastn.dev` | The start of every request URL. Paths start with `/v1`. |
| `apiKey` | Empty | `X-API-Key: {{apiKey}}` |
| `testMode` | `true` | `X-fastn-Test-Mode: {{testMode}}`. A test key is refused with `403` without it. A live key ignores it. |

To act for one of your customers, add an `x-org-id` header to the request or the collection. A key that requires identity verification also needs `x-user-id` and `x-identity-hmac`. See [Verify caller identity](../../manage/identity-verification.md).

Path parameters such as `:workflowId` and example bodies come from the spec. Replace the placeholder values, like `<string>`, before you send a request that writes. Optional query parameters and headers are in each request but turned off: tick one to send it.

## Try requests in the browser

The reference pages do not have a built-in request console. Use the collection, or `curl` as shown on the [REST API reference](README.md#authentication) overview.

## What's next

* [REST API reference](README.md): every endpoint, its fields and responses.
* [HTTP API](../api.md): run workflows and mint embed tokens.
* [Errors and failure states](../errors.md): what a failed call returns.
