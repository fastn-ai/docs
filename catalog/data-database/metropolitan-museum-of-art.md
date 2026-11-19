---
description: "The Metropolitan Museum of Art shares open data on its collection. Search objects, list departments and get artwork details."
hidden: true
---

# Metropolitan Museum of Art

<img src="../../.gitbook/assets/connectors/lg/metropolitan-museum-of-art.png" alt="Metropolitan Museum of Art logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [metmuseum.org](https://metmuseum.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `metropolitanMuseumOfArt` |

## Setup

Metropolitan Museum of Art needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Metropolitan Museum of Art from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.metropolitanMuseumOfArt.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Object</td><td><code>getObject</code></td><td>Returns the full open-access record of one object: title, artist, dates, medium, dimensions, department, culture, images, tags and links. Docs: https://metmuseum.github.io/</td></tr><tr><td>List Departments</td><td><code>listDepartments</code></td><td>Returns all curatorial departments with their ids and names. Docs: https://metmuseum.github.io/</td></tr><tr><td>List Object IDs</td><td><code>listObjectIds</code></td><td>Returns the ids of all objects in the collection, optionally only those updated after a date and/or in given departments. Without filters the list has ~500,000 ids. Docs: https://metmuseum.github.io/</td></tr><tr><td>Search Objects</td><td><code>searchObjects</code></td><td>Searches the collection (v1.1, paginated) and returns the total and matching object ids; filter by highlight, title/tags/artist field, department, on view, medium, location, images and date range. Docs: https://metmuseum.github.io/</td></tr></tbody></table>

## Events

Metropolitan Museum of Art has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
