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

## Use it

Add Cleveland Museum of Art Open Access from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clevelandMuseumOfArt.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Artwork</td><td><code>getArtwork</code></td><td>Get one artwork by its id or accession number, with full metadata and image links Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Get Creator</td><td><code>getCreator</code></td><td>Get one creator by id with biography and artworks Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Get Exhibition</td><td><code>getExhibition</code></td><td>Get one exhibition by id with venues and, optionally, its artworks Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Search Artworks</td><td><code>searchArtworks</code></td><td>Search the Cleveland Museum of Art collection (over 64,000 works) by keyword and many filters, with image links and paging Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Search Creators</td><td><code>searchCreators</code></td><td>Search artists and other creators by name, biography, nationality and birth/death years Docs: https://openaccess-api.clevelandart.org/</td></tr><tr><td>Search Exhibitions</td><td><code>searchExhibitions</code></td><td>Search exhibitions by title, organizer, venue and opening/closing dates Docs: https://openaccess-api.clevelandart.org/</td></tr></tbody></table>

## Events

Cleveland Museum of Art Open Access has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
