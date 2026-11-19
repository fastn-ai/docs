---
description: "Generic HTTP request tools for calling any HTTPS REST endpoint that has no dedicated connector: GET, POST, PUT, PATCH and DELETE."
hidden: true
---

# HTTP API

<img src="../../.gitbook/assets/connectors/lg/http-api.png" alt="HTTP API logo">

Each action takes a host (for example api.example.com) and a path (for example /v1/users/42). GET sends every extra input field as a query parameter; POST, PUT and PATCH send a JSON body. Authentication lives on the connection, not on each call: connect with No Authentication for public APIs, or with Custom Header or Bearer Token to send one header on every request - either a header you name yourself (for example X-API-Key) with its value, or an Authorization: Bearer token. HTTPS only.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [fastn.ai](https://fastn.ai) |
| **Authentication** | Credentials you enter, No authentication |
| **Slug** | `httpApi` |

## Use it

Add HTTP API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.httpApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>DELETE Request</td><td><code>deleteRequest</code></td><td>Sends an HTTP DELETE request to any HTTPS endpoint and returns the response. Give the host (for example api.example.com) and the path of the resource to delete (starting with a slash). No request body is sent. Headers such as an Authorization token come from the connection, not from this action.</td></tr><tr><td>GET Request</td><td><code>getRequest</code></td><td>Sends an HTTP GET request to any HTTPS endpoint and returns the response. Give the host (for example api.example.com) and the path (starting with a slash, for example /v1/users). Every other input field you pass is sent as a query parameter, so add whatever parameters the API expects (for example limit=10). Headers such as an Authorization token come from the connection, not from this action.</td></tr><tr><td>PATCH Request</td><td><code>patchRequest</code></td><td>Sends an HTTP PATCH request with a JSON body to any HTTPS endpoint and returns the response. Give the host (for example api.example.com), the path (starting with a slash) and the JSON body to send. Headers such as an Authorization token come from the connection, not from this action.</td></tr><tr><td>POST Request</td><td><code>postRequest</code></td><td>Sends an HTTP POST request with a JSON body to any HTTPS endpoint and returns the response. Give the host (for example api.example.com), the path (starting with a slash) and the JSON body to send. Headers such as an Authorization token come from the connection, not from this action.</td></tr><tr><td>PUT Request</td><td><code>putRequest</code></td><td>Sends an HTTP PUT request with a JSON body to any HTTPS endpoint and returns the response. Give the host (for example api.example.com), the path (starting with a slash) and the JSON body to send. Headers such as an Authorization token come from the connection, not from this action.</td></tr></tbody></table>
