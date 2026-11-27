---
description: "Make GET, POST, PUT, PATCH and DELETE requests to any web service that has no dedicated app in Fastn."
hidden: true
---

# HTTP API

<img src="../../.gitbook/assets/connectors/lg/http-api.png" alt="HTTP API logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [fastn.ai](https://fastn.ai) |
| **Authentication** | API key or token |
| **Slug** | `httpApi` |

## Setup

Your customers enter their API key or token for HTTP API when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect HTTP API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **HTTP API**.
2. Select **Connect** on the HTTP API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use HTTP API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>DELETE Request</td><td><code>deleteRequest</code></td><td>Sends an HTTP DELETE request to any HTTPS endpoint and returns the response. Give the host (for example api.example.com) and the path of the resource to delete (starting with a slash). No request body is sent. Headers such as an Authorization token come from the connection, not from this action.</td></tr><tr><td>GET Request</td><td><code>getRequest</code></td><td>Sends an HTTP GET request to any HTTPS endpoint and returns the response. Give the host (for example api.example.com) and the path (starting with a slash, for example /v1/users). Every other input field you pass is sent as a query parameter, so add whatever parameters the API expects (for example limit=10). Headers such as an Authorization token come from the connection, not from this action.</td></tr><tr><td>PATCH Request</td><td><code>patchRequest</code></td><td>Sends an HTTP PATCH request with a JSON body to any HTTPS endpoint and returns the response. Give the host (for example api.example.com), the path (starting with a slash) and the JSON body to send. Headers such as an Authorization token come from the connection, not from this action.</td></tr><tr><td>POST Request</td><td><code>postRequest</code></td><td>Sends an HTTP POST request with a JSON body to any HTTPS endpoint and returns the response. Give the host (for example api.example.com), the path (starting with a slash) and the JSON body to send. Headers such as an Authorization token come from the connection, not from this action.</td></tr><tr><td>PUT Request</td><td><code>putRequest</code></td><td>Sends an HTTP PUT request with a JSON body to any HTTPS endpoint and returns the response. Give the host (for example api.example.com), the path (starting with a slash) and the JSON body to send. Headers such as an Authorization token come from the connection, not from this action.</td></tr></tbody></table>

