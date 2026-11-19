---
description: "Google Service Management API (servicemanagement.googleapis.com v1)."
hidden: true
---

# Google Service Management

<img src="../../.gitbook/assets/connectors/lg/google-service-management.png" alt="Google Service Management logo">

List managed API services (Google APIs and your own Cloud Endpoints / API Gateway services), read a service and its active or historical service configurations, and list the Service Management operations (config rollouts, service create/delete) for a service. Authorizes with Google OAuth 2.0 using the scopes service.management.readonly (read services and configs) and service.management (list service operations).

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [servicemanagement.googleapis.com](https://servicemanagement.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleServiceManagement` |

## Use it

Add Google Service Management from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleServiceManagement.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Service</td><td><code>getService</code></td><td>Gets a managed service by name from Google Service Management, returning its service name and producer project ID. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/service.management.readonly (or service.management).</td></tr><tr><td>Get Service Config</td><td><code>getServiceConfig</code></td><td>Gets a service configuration (the API definition: title, APIs, HTTP rules, authentication, quota, documentation) for a managed service. Without configId it returns the latest configuration; pass configId (from List Service Configs) for a specific version and view=FULL to include source files. Configs can be large. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/service.management.readonly (or service.management).</td></tr><tr><td>List Service Configs</td><td><code>listServiceConfigs</code></td><td>Lists the history of service configurations for a managed service, newest first (each item is a full service config with its id). Use pageSize=1 to fetch only the latest. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/service.management.readonly (or service.management).</td></tr><tr><td>List Service Operations</td><td><code>listServiceOperations</code></td><td>Lists Google Service Management long-running operations (service config submissions, rollouts, service create/delete/undelete) for one managed service. The filter must name the service, for example 'serviceName=my-api.endpoints.my-project.cloud.goog', optionally combined with AND status=done|in_progress|failed or startTime&gt;="2026-01-01T00:00:00Z". Read-only call, but Google requires the management scope https://www.googleapis.com/auth/service.management for it.</td></tr><tr><td>List Services</td><td><code>listServices</code></td><td>Lists managed services known to Google Service Management: public Google APIs plus services the user can read (for example their own Cloud Endpoints or API Gateway services). Pass producerProjectId to list only the services a given project produces. Returns service names and producer project IDs. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/service.management.readonly (or service.management).</td></tr></tbody></table>
