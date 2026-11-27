---
description: "Lorem Picsum is a free placeholder photo service. List images and get image details by ID or seed."
hidden: true
---

# Lorem Picsum

<img src="../../.gitbook/assets/connectors/lg/lorem-picsum.png" alt="Lorem Picsum logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [picsum.photos](https://picsum.photos) |
| **Authentication** | No sign-in needed |
| **Slug** | `loremPicsum` |

## Setup

Lorem Picsum needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Lorem Picsum from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Lorem Picsum**.
2. Select **Connect** on the Lorem Picsum card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Lorem Picsum needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Lorem Picsum's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Image Details</td><td><code>getImageInfo</code></td><td>Get author, size and links for one image by its id Docs: https://picsum.photos/</td></tr><tr><td>Get Seeded Image Details</td><td><code>getSeedImageInfo</code></td><td>Get details of the image that a given seed always maps to Docs: https://picsum.photos/</td></tr><tr><td>List Images</td><td><code>listImages</code></td><td>List the images available on Lorem Picsum with author, size and links, 30 per page by default Docs: https://picsum.photos/</td></tr></tbody></table>

