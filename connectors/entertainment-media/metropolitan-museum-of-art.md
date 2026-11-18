---
description: "The Metropolitan Museum of Art Collection API: free, keyless access to 470,000+ open-access artwork records - search the collection, list object ids by…"
hidden: true
---

# Metropolitan Museum of Art

<img src="../../.gitbook/assets/connectors/lg/metropolitan-museum-of-art.png" alt="Metropolitan Museum of Art logo">

The Metropolitan Museum of Art Collection API: free, keyless access to 470,000+ open-access artwork records - search the collection, list object ids by department or update date, read full object records with images, artists and dates, and list curatorial departments.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [metmuseum.org](https://metmuseum.org) |
| **Authentication** | No authentication |
| **Slug** | `metropolitanMuseumOfArt` |

## Use it

Add Metropolitan Museum of Art from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.metropolitanMuseumOfArt.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Object | `getObject` | Returns the full open-access record of one object: title, artist, dates, medium, dimensions, department, culture, images, tags and links. Docs: https://metmuseum.github.io/ |
| List Departments | `listDepartments` | Returns all curatorial departments with their ids and names. Docs: https://metmuseum.github.io/ |
| List Object IDs | `listObjectIds` | Returns the ids of all objects in the collection, optionally only those updated after a date and/or in given departments. Without filters the list has ~500,000 ids. Docs: https://metmuseum.github.io/ |
| Search Objects | `searchObjects` | Searches the collection (v1.1, paginated) and returns the total and matching object ids; filter by highlight, title/tags/artist field, department, on view, medium, location, images and date range. Docs: https://metmuseum.github.io/ |
