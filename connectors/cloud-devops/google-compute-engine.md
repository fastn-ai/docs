---
description: "Google Compute Engine API v1 (https://compute.googleapis.com/compute/v1)."
hidden: true
---

# Google Compute Engine

<img src="../../.gitbook/assets/connectors/lg/google-compute-engine.png" alt="Google Compute Engine logo">

List zones, list and inspect VM instances, list persistent disks, create and delete persistent disks, and poll zonal operations. OAuth 2.0 (Google) authorization-code auth with the compute and compute.readonly scopes.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [compute.googleapis.com](https://compute.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleComputeEngine` |

## Use it

Add Google Compute Engine from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleComputeEngine.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Disk</td><td><code>createDisk</code></td><td>Creates an empty, unattached persistent disk in a zone, for example a 10 GB pd-standard disk named fastn-demo-disk. Harmless and reversible: delete it afterwards with Delete Disk. Returns a zonal Operation; poll it with Get Zone Operation until status is DONE. Requires the https://www.googleapis.com/auth/compute scope.</td></tr><tr><td>Delete Disk</td><td><code>deleteDisk</code></td><td>Deletes a persistent disk from a zone, for example the demo disk made with Create Disk. The disk's data is permanently removed (snapshots are kept). The disk must not be attached to an instance. Returns a zonal Operation; poll it with Get Zone Operation. Requires the https://www.googleapis.com/auth/compute scope.</td></tr><tr><td>Get Instance</td><td><code>getInstance</code></td><td>Gets one Compute Engine VM instance by name, including machine type, status, network interfaces, attached disks, labels and metadata. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works).</td></tr><tr><td>Get Zone Operation</td><td><code>getZoneOperation</code></td><td>Gets the status of a zonal Compute Engine operation, such as the insert or delete operation returned by Create Disk and Delete Disk. Poll until status is DONE and check error. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works).</td></tr><tr><td>List Disks</td><td><code>listDisks</code></td><td>Lists the persistent disks in one zone of a Google Cloud project, with each disk's name, size, type, status and the instances it is attached to. Use a small maxResults. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works).</td></tr><tr><td>List Instances</td><td><code>listInstances</code></td><td>Lists the Compute Engine VM instances in one zone of a Google Cloud project, with each instance's name, machine type, status, network interfaces and disks. Use a small maxResults. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works).</td></tr><tr><td>List Zones</td><td><code>listZones</code></td><td>Lists the Compute Engine zones available to a Google Cloud project, with each zone's name, region and status. Use a small maxResults and an optional filter such as name = us-central1-a. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works).</td></tr></tbody></table>
