---
description: "Google Service Management tracks managed API services on Google Cloud. List services, read service configs and list service operations."
hidden: true
---

# Google Service Management

<img src="../../.gitbook/assets/connectors/lg/google-service-management.png" alt="Google Service Management logo">

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [servicemanagement.googleapis.com](https://servicemanagement.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleServiceManagement` |

## Setup

Your customers sign in to Google Service Management through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Service Management from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Service Management**.
2. Select **Connect** on the Google Service Management card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Service Management and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Service Management's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Service</td><td><code>getService</code></td><td>Gets a managed service by name from Google Service Management, returning its service name and producer project ID. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/service.management.readonly (or service.management).</td></tr><tr><td>Get Service Config</td><td><code>getServiceConfig</code></td><td>Gets a service configuration (the API definition: title, APIs, HTTP rules, authentication, quota, documentation) for a managed service. Without configId it returns the latest configuration; pass configId (from List Service Configs) for a specific version and view=FULL to include source files. Configs can be large. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/service.management.readonly (or service.management).</td></tr><tr><td>List Service Configs</td><td><code>listServiceConfigs</code></td><td>Lists the history of service configurations for a managed service, newest first (each item is a full service config with its id). Use pageSize=1 to fetch only the latest. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/service.management.readonly (or service.management).</td></tr><tr><td>List Service Operations</td><td><code>listServiceOperations</code></td><td>Lists Google Service Management long-running operations (service config submissions, rollouts, service create/delete/undelete) for one managed service. The filter must name the service, for example 'serviceName=my-api.endpoints.my-project.cloud.goog', optionally combined with AND status=done|in_progress|failed or startTime&gt;="2026-01-01T00:00:00Z". Read-only call, but Google requires the management scope https://www.googleapis.com/auth/service.management for it.</td></tr><tr><td>List Services</td><td><code>listServices</code></td><td>Lists managed services known to Google Service Management: public Google APIs plus services the user can read (for example their own Cloud Endpoints or API Gateway services). Pass producerProjectId to list only the services a given project produces. Returns service names and producer project IDs. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/service.management.readonly (or service.management).</td></tr></tbody></table>

