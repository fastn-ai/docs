---
description: "The Cleveland Museum of Art shares open data on its collection. Search and look up artworks, creators and exhibitions."
hidden: true
---

# Cleveland Museum of Art Open Access

<img src="../../.gitbook/assets/connectors/lg/cleveland-museum-of-art.png" alt="Cleveland Museum of Art Open Access logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [clevelandart.org](https://clevelandart.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `clevelandMuseumOfArt` |

## Setup

Cleveland Museum of Art Open Access needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Cleveland Museum of Art Open Access from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Cleveland Museum of Art Open Access**.
2. Select **Connect** on the Cleveland Museum of Art Open Access card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Cleveland Museum of Art Open Access needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Cleveland Museum of Art Open Access's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Artwork</td><td><code>getArtwork</code></td><td>Get one artwork by its id or accession number, with full metadata and image links Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Get Creator</td><td><code>getCreator</code></td><td>Get one creator by id with biography and artworks Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Get Exhibition</td><td><code>getExhibition</code></td><td>Get one exhibition by id with venues and, optionally, its artworks Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Search Artworks</td><td><code>searchArtworks</code></td><td>Search the Cleveland Museum of Art collection (over 64,000 works) by keyword and many filters, with image links and paging Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Search Creators</td><td><code>searchCreators</code></td><td>Search artists and other creators by name, biography, nationality and birth/death years Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Search Exhibitions</td><td><code>searchExhibitions</code></td><td>Search exhibitions by title, organizer, venue and opening/closing dates Docs: https://openaccess-api.clevelandart.org/</td></tr></tbody></table>

