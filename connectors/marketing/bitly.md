---
description: "Bitly is a URL shortening, QR code, and link analytics platform."
hidden: true
---

# Bitly

<img src="../../.gitbook/assets/connectors/lg/bitly.png" alt="Bitly logo">

This connector manages Bitlinks (create, retrieve, update, delete, expand, and view click analytics), Groups, QR Codes, and the connected user's account.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [bitly.com](https://bitly.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `bitly` |

## Use it

Add Bitly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bitly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Bitlink</td><td><code>createBitlink</code></td><td>Shortens a long URL into a new Bitlink. Supports assigning it to a specific group and domain, adding a title, tags, deep links, and an optional expiration timestamp.</td></tr><tr><td>Create QR Code</td><td><code>createQrCode</code></td><td>Creates a new QR Code in a group, pointing either at an existing Bitlink or a new long URL that Bitly will shorten automatically.</td></tr><tr><td>Delete Bitlink</td><td><code>deleteBitlink</code></td><td>Permanently deletes a Bitlink by its ID. Note: deleting a QR Code that was created against this Bitlink will also delete the Bitlink, so this action is primarily needed for Bitlinks that have no associated QR Code.</td></tr><tr><td>Delete QR Code</td><td><code>deleteQrCode</code></td><td>Permanently deletes a QR Code by its ID.</td></tr><tr><td>Expand Bitlink</td><td><code>expandBitlink</code></td><td>Decodes a Bitlink back into its original long destination URL.</td></tr><tr><td>Get Bitlink</td><td><code>getBitlink</code></td><td>Retrieves the full details of a single Bitlink by its ID (domain + hash, e.g. bit.ly/4ghvkrk), including its title, tags, archived state, and destination URL.</td></tr><tr><td>Get Bitlink Clicks by Date</td><td><code>getBitlinkClicksByDate</code></td><td>Retrieves a time-bucketed series of click counts for a Bitlink, one entry per unit of time (e.g. per day) over the requested window.</td></tr><tr><td>Get Bitlink Clicks Summary</td><td><code>getBitlinkClicksSummary</code></td><td>Retrieves the total click count for a Bitlink over a given time window (e.g. the last 7 days, or all time).</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Retrieves the profile of the Bitly account authenticated by the connected access token, including login, name, email addresses, 2FA status, and the default group GUID.</td></tr><tr><td>Get Group</td><td><code>getGroup</code></td><td>Retrieves a single Bitly group by its GUID, including its name, role, organization, and active status.</td></tr></tbody></table>

<details>

<summary>View 5 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get QR Code</td><td><code>getQrCode</code></td><td>Retrieves the full details of a single QR Code by its ID, including its title, destination, type, and customization settings.</td></tr><tr><td>List Bitlinks by Group</td><td><code>listBitlinksByGroup</code></td><td>Retrieves the Bitlinks belonging to a group, with optional search, tag, and archived-state filters. Supports pagination via size and search_after.</td></tr><tr><td>List Groups</td><td><code>listGroups</code></td><td>Retrieves all Bitly groups the authenticated user belongs to, optionally filtered to a single organization. A group is the container used when creating Bitlinks and QR Codes.</td></tr><tr><td>List QR Codes by Group</td><td><code>listQrCodesByGroup</code></td><td>Retrieves the QR Codes belonging to a group, with optional search, tag, and archived-state filters. Supports pagination via size and search_after.</td></tr><tr><td>Update Bitlink</td><td><code>updateBitlink</code></td><td>Updates an existing Bitlink's title, tags, destination URL, archived state, deep links, or expiration timestamp.</td></tr></tbody></table>

</details>
