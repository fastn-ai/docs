---
description: "arXiv hosts millions of scholarly preprints. Search papers, read feeds and harvest article metadata."
hidden: true
---

# arXiv

<img src="../../.gitbook/assets/connectors/lg/arxiv.png" alt="arXiv logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [arxiv.org](https://arxiv.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `arxiv` |

## Setup

arXiv needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect arXiv from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **arXiv**.
2. Select **Connect** on the arXiv card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. arXiv needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use arXiv's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Atom Feed</td><td><code>getAtomFeed</code></td><td>Returns the latest daily announcement Atom feed for one or more categories. Docs: https://info.arxiv.org/help/rss.html</td></tr><tr><td>Get RSS Feed</td><td><code>getRssFeed</code></td><td>Returns the latest daily announcement RSS 2.0 feed for one or more categories (e.g. cs.AI or cs.AI+math.CO). Docs: https://info.arxiv.org/help/rss.html</td></tr><tr><td>OAI-PMH Get Record</td><td><code>oaiGetRecord</code></td><td>Returns the metadata record of one paper in the chosen format. Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>OAI-PMH Identify</td><td><code>oaiIdentify</code></td><td>Returns information about the arXiv OAI-PMH repository (name, base URL, earliest datestamp, granularity). Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>OAI-PMH List Identifiers</td><td><code>oaiListIdentifiers</code></td><td>Returns record headers (identifier, datestamp, sets) changed in a date range and/or set; page with resumptionToken. Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>OAI-PMH List Metadata Formats</td><td><code>oaiListMetadataFormats</code></td><td>Returns the metadata formats available (oai_dc, arXiv, arXivOld, arXivRaw), optionally for one record. Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>OAI-PMH List Records</td><td><code>oaiListRecords</code></td><td>Returns full metadata records changed in a date range and/or set; page with resumptionToken. Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>OAI-PMH List Sets</td><td><code>oaiListSets</code></td><td>Returns the arXiv sets (subject archives, e.g. cs, math, physics:hep-th) available for selective harvesting. Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>Search Articles</td><td><code>searchArticles</code></td><td>Searches arXiv papers with field prefixes (ti: title, au: author, abs: abstract, co: comment, jr: journal ref, cat: category, rn: report number, all:) and AND/OR/ANDNOT, or fetches papers by id; returns an Atom XML feed with title, authors, summary, dates, categories, DOI and PDF links. Docs: https://info.arxiv.org/help/api/user-manual.html</td></tr></tbody></table>

