---
description: "The Cleveland Museum of Art Open Access API offers CC0 data on over 64,000 artworks and images for over 37,000 of them."
hidden: true
---

# Cleveland Museum of Art Open Access

<img src="../../.gitbook/assets/connectors/lg/cleveland-museum-of-art.png" alt="Cleveland Museum of Art Open Access logo">

The Cleveland Museum of Art Open Access API offers CC0 data on over 64,000 artworks and images for over 37,000 of them. Search artworks with rich filters, get an artwork by id or accession number, and search or get creators and exhibitions. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [clevelandart.org](https://clevelandart.org) |
| **Authentication** | No authentication |
| **Slug** | `clevelandMuseumOfArt` |

## Use it

Add Cleveland Museum of Art Open Access from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clevelandMuseumOfArt.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Artwork</td><td><code>getArtwork</code></td><td>Get one artwork by its id or accession number, with full metadata and image links (GET /api/artworks/{id}). Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Get Creator</td><td><code>getCreator</code></td><td>Get one creator by id with biography and artworks (GET /api/creators/{id}). Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Get Exhibition</td><td><code>getExhibition</code></td><td>Get one exhibition by id with venues and, optionally, its artworks (GET /api/exhibitions/{id}). Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Search Artworks</td><td><code>searchArtworks</code></td><td>Search the Cleveland Museum of Art collection (over 64,000 works) by keyword and many filters, with image links and paging (GET /api/artworks/). Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Search Creators</td><td><code>searchCreators</code></td><td>Search artists and other creators by name, biography, nationality and birth/death years (GET /api/creators/). Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Search Exhibitions</td><td><code>searchExhibitions</code></td><td>Search exhibitions by title, organizer, venue and opening/closing dates (GET /api/exhibitions/). Docs: https://openaccess-api.clevelandart.org/</td></tr></tbody></table>
