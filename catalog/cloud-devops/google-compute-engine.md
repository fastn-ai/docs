---
description: "Google Compute Engine runs virtual machines on Google Cloud. List zones, list and inspect instances, and create, list and delete disks."
hidden: true
---

# Google Compute Engine

<img src="../../.gitbook/assets/connectors/lg/google-compute-engine.png" alt="Google Compute Engine logo">

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [compute.googleapis.com](https://compute.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleComputeEngine` |

## Setup

Your customers sign in to Google Compute Engine through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Compute Engine from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Compute Engine**.
2. Select **Connect** on the Google Compute Engine card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Compute Engine and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Compute Engine's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Disk</td><td><code>createDisk</code></td><td>Creates an empty, unattached persistent disk in a zone, for example a 10 GB pd-standard disk named fastn-demo-disk. Harmless and reversible: delete it afterwards with Delete Disk. Returns a zonal Operation; poll it with Get Zone Operation until status is DONE. Requires the https://www.googleapis.com/auth/compute scope.</td></tr><tr><td>Delete Disk</td><td><code>deleteDisk</code></td><td>Deletes a persistent disk from a zone, for example the demo disk made with Create Disk. The disk's data is permanently removed (snapshots are kept). The disk must not be attached to an instance. Returns a zonal Operation; poll it with Get Zone Operation. Requires the https://www.googleapis.com/auth/compute scope.</td></tr><tr><td>Get Instance</td><td><code>getInstance</code></td><td>Gets one Compute Engine VM instance by name, including machine type, status, network interfaces, attached disks, labels and metadata. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works).</td></tr><tr><td>Get Zone Operation</td><td><code>getZoneOperation</code></td><td>Gets the status of a zonal Compute Engine operation, such as the insert or delete operation returned by Create Disk and Delete Disk. Poll until status is DONE and check error. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works).</td></tr><tr><td>List Disks</td><td><code>listDisks</code></td><td>Lists the persistent disks in one zone of a Google Cloud project, with each disk's name, size, type, status and the instances it is attached to. Use a small maxResults. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works).</td></tr><tr><td>List Instances</td><td><code>listInstances</code></td><td>Lists the Compute Engine VM instances in one zone of a Google Cloud project, with each instance's name, machine type, status, network interfaces and disks. Use a small maxResults. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works).</td></tr><tr><td>List Zones</td><td><code>listZones</code></td><td>Lists the Compute Engine zones available to a Google Cloud project, with each zone's name, region and status. Use a small maxResults and an optional filter such as name = us-central1-a. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works).</td></tr></tbody></table>

