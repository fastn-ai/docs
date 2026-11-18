---
description: "Google Compute Engine API v1 (https://compute.googleapis.com/compute/v1)."
hidden: true
---

# Google Compute Engine

<img src="../../.gitbook/assets/connectors/lg/google-compute-engine.png" alt="Google Compute Engine logo">

Google Compute Engine API v1 (https://compute.googleapis.com/compute/v1). List zones, list and inspect VM instances, list persistent disks, create and delete persistent disks, and poll zonal operations. OAuth 2.0 (Google) authorization-code auth with the compute and compute.readonly scopes.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [compute.googleapis.com](https://compute.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleComputeEngine` |

## Use it

Add Google Compute Engine from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleComputeEngine.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Disk | `createDisk` | Creates an empty, unattached persistent disk in a zone, for example a 10 GB pd-standard disk named fastn-demo-disk. Harmless and reversible: delete it afterwards with Delete Disk. Returns a zonal Operation; poll it with Get Zone Operation until status is DONE. Requires the https://www.googleapis.com/auth/compute scope. |
| Delete Disk | `deleteDisk` | Deletes a persistent disk from a zone, for example the demo disk made with Create Disk. The disk's data is permanently removed (snapshots are kept). The disk must not be attached to an instance. Returns a zonal Operation; poll it with Get Zone Operation. Requires the https://www.googleapis.com/auth/compute scope. |
| Get Instance | `getInstance` | Gets one Compute Engine VM instance by name, including machine type, status, network interfaces, attached disks, labels and metadata. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works). |
| Get Zone Operation | `getZoneOperation` | Gets the status of a zonal Compute Engine operation, such as the insert or delete operation returned by Create Disk and Delete Disk. Poll until status is DONE and check error. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works). |
| List Disks | `listDisks` | Lists the persistent disks in one zone of a Google Cloud project, with each disk's name, size, type, status and the instances it is attached to. Use a small maxResults. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works). |
| List Instances | `listInstances` | Lists the Compute Engine VM instances in one zone of a Google Cloud project, with each instance's name, machine type, status, network interfaces and disks. Use a small maxResults. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works). |
| List Zones | `listZones` | Lists the Compute Engine zones available to a Google Cloud project, with each zone's name, region and status. Use a small maxResults and an optional filter such as name = us-central1-a. Read-only; requires the https://www.googleapis.com/auth/compute.readonly scope (compute also works). |
