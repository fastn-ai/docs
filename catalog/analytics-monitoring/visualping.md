---
description: "Visualping watches web pages for changes. Create, update, list and delete monitoring jobs, and read change reports."
hidden: true
---

# Visualping

<img src="../../.gitbook/assets/connectors/lg/visualping.png" alt="Visualping logo">

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [visualping.io](https://visualping.io) |
| **Authentication** | Access token |
| **Slug** | `visualping` |

## Setup

Your customers enter their access token for Visualping when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Visualping from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Visualping**.
2. Select **Connect** on the Visualping card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Visualping's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Job</td><td><code>createJob</code></td><td>Create a new monitoring job (monitor) for a URL. Pass notification.webhook to register a webhook destination for page-change events.</td></tr><tr><td>Delete Job</td><td><code>deleteJob</code></td><td>Delete a monitoring job. Used by webhook unsubscription to remove the monitor backing a subscription.</td></tr><tr><td>Get Job</td><td><code>getJob</code></td><td>Retrieve a monitoring job by id.</td></tr><tr><td>Get Report Page</td><td><code>getReportPage</code></td><td>Reverse-chronological activity feed across every job in a workspace. All body fields are required — pass null for ones you don't want to filter on.</td></tr><tr><td>List Jobs</td><td><code>listJobs</code></td><td>List monitoring jobs with optional active-state filter and pagination.</td></tr><tr><td>Update Job</td><td><code>updateJob</code></td><td>Update a monitoring job's configuration.</td></tr></tbody></table>

