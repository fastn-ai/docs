---
description: "Bitly is a URL shortening, QR code, and link analytics platform."
hidden: true
---

# Bitly

<img src="../../.gitbook/assets/connectors/lg/bitly.png" alt="Bitly logo">

Bitly is a URL shortening, QR code, and link analytics platform. This connector manages Bitlinks (create, retrieve, update, delete, expand, and view click analytics), Groups, QR Codes, and the connected user's account.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [bitly.com](https://bitly.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `bitly` |

## Use it

Add Bitly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bitly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Bitlink | `createBitlink` | Shortens a long URL into a new Bitlink. Supports assigning it to a specific group and domain, adding a title, tags, deep links, and an optional expiration timestamp. |
| Create QR Code | `createQrCode` | Creates a new QR Code in a group, pointing either at an existing Bitlink or a new long URL that Bitly will shorten automatically. |
| Delete Bitlink | `deleteBitlink` | Permanently deletes a Bitlink by its ID. Note: deleting a QR Code that was created against this Bitlink will also delete the Bitlink, so this action is primarily needed for Bitlinks that have no associated QR Code. |
| Delete QR Code | `deleteQrCode` | Permanently deletes a QR Code by its ID. |
| Expand Bitlink | `expandBitlink` | Decodes a Bitlink back into its original long destination URL. |
| Get Bitlink | `getBitlink` | Retrieves the full details of a single Bitlink by its ID (domain + hash, e.g. bit.ly/4ghvkrk), including its title, tags, archived state, and destination URL. |
| Get Bitlink Clicks by Date | `getBitlinkClicksByDate` | Retrieves a time-bucketed series of click counts for a Bitlink, one entry per unit of time (e.g. per day) over the requested window. |
| Get Bitlink Clicks Summary | `getBitlinkClicksSummary` | Retrieves the total click count for a Bitlink over a given time window (e.g. the last 7 days, or all time). |
| Get Current User | `getCurrentUser` | Retrieves the profile of the Bitly account authenticated by the connected access token, including login, name, email addresses, 2FA status, and the default group GUID. |
| Get Group | `getGroup` | Retrieves a single Bitly group by its GUID, including its name, role, organization, and active status. |
| Get QR Code | `getQrCode` | Retrieves the full details of a single QR Code by its ID, including its title, destination, type, and customization settings. |
| List Bitlinks by Group | `listBitlinksByGroup` | Retrieves the Bitlinks belonging to a group, with optional search, tag, and archived-state filters. Supports pagination via size and search_after. |
| List Groups | `listGroups` | Retrieves all Bitly groups the authenticated user belongs to, optionally filtered to a single organization. A group is the container used when creating Bitlinks and QR Codes. |
| List QR Codes by Group | `listQrCodesByGroup` | Retrieves the QR Codes belonging to a group, with optional search, tag, and archived-state filters. Supports pagination via size and search_after. |
| Update Bitlink | `updateBitlink` | Updates an existing Bitlink's title, tags, destination URL, archived state, deep links, or expiration timestamp. |
