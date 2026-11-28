---
description: "The Wayback Machine archives web pages. Check if a page is archived and search past captures."
hidden: true
---

# Wayback Machine

<img src="../../.gitbook/assets/connectors/lg/wayback-machine.png" alt="Wayback Machine logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [archive.org](https://archive.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `waybackMachine` |

## Setup

Wayback Machine needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Wayback Machine from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Wayback Machine**.
2. Select **Connect** on the Wayback Machine card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Wayback Machine needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Wayback Machine's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check URL Availability</td><td><code>checkAvailability</code></td><td>Check whether a web page is archived in the Wayback Machine and get the closest snapshot, optionally near a given time Pages with no capture return an empty archived_snapshots object. Docs: https://archive.org/help/wayback_api.php</td></tr><tr><td>Get Number of Pages</td><td><code>getNumberOfPages</code></td><td>Get how many pages a CDX query has under the pagination API Returns a single number. Docs: https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server</td></tr><tr><td>Search Captures</td><td><code>searchCaptures</code></td><td>Search the Wayback CDX index for captures of a URL, a URL prefix, a host or a whole domain, with date range, field filters, collapsing and paging The first row lists the field names; each later row is one capture. Docs: https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server</td></tr></tbody></table>

