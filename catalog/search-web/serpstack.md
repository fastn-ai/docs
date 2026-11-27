---
description: "Serpstack returns Google search results as structured data. Run Google searches and look up supported locations."
hidden: true
---

# Serpstack

<img src="../../.gitbook/assets/connectors/lg/serpstack.png" alt="Serpstack logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [serpstack.com](https://serpstack.com) |
| **Authentication** | API key |
| **Slug** | `serpstack` |

## Setup

Your customers enter their API key for Serpstack when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Serpstack from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Serpstack**.
2. Select **Connect** on the Serpstack card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Serpstack's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Google Results</td><td><code>searchGoogleResults</code></td><td>Runs a real-time Google search and returns structured SERP data: organic results, local results, answer box, related searches and questions, and pagination. Supports web, image, and news search modes plus device, location, language, and date-range targeting. Output can be returned as JSON or CSV.</td></tr><tr><td>Search Locations</td><td><code>searchLocations</code></td><td>Looks up canonical Serpstack location strings matching a free-text place name, for use as the location parameter on Search Google Results. Returns each match's display name, canonical name, country code, target type, and reach.</td></tr></tbody></table>

