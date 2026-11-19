---
description: "Connect arXiv to your product with fastn."
hidden: true
---

# arXiv

<img src="../../.gitbook/assets/connectors/lg/arxiv.png" alt="arXiv logo">

arXiv APIs: free, keyless access to 2.5M+ scholarly preprints in physics, mathematics, computer science and more - search papers (Atom XML), harvest metadata through OAI-PMH, and read daily RSS/Atom announcement feeds per category. arXiv asks clients to wait 3 seconds between calls. Responses are XML, returned as text.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [arxiv.org](https://arxiv.org) |
| **Authentication** | No authentication |
| **Slug** | `arxiv` |

## Use it

Add arXiv from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.arxiv.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Atom Feed</td><td><code>getAtomFeed</code></td><td>Returns the latest daily announcement Atom feed for one or more categories. Docs: https://info.arxiv.org/help/rss.html</td></tr><tr><td>Get RSS Feed</td><td><code>getRssFeed</code></td><td>Returns the latest daily announcement RSS 2.0 feed for one or more categories (e.g. cs.AI or cs.AI+math.CO). Docs: https://info.arxiv.org/help/rss.html</td></tr><tr><td>OAI-PMH Get Record</td><td><code>oaiGetRecord</code></td><td>Returns the metadata record of one paper in the chosen format. Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>OAI-PMH Identify</td><td><code>oaiIdentify</code></td><td>Returns information about the arXiv OAI-PMH repository (name, base URL, earliest datestamp, granularity). Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>OAI-PMH List Identifiers</td><td><code>oaiListIdentifiers</code></td><td>Returns record headers (identifier, datestamp, sets) changed in a date range and/or set; page with resumptionToken. Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>OAI-PMH List Metadata Formats</td><td><code>oaiListMetadataFormats</code></td><td>Returns the metadata formats available (oai_dc, arXiv, arXivOld, arXivRaw), optionally for one record. Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>OAI-PMH List Records</td><td><code>oaiListRecords</code></td><td>Returns full metadata records changed in a date range and/or set; page with resumptionToken. Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>OAI-PMH List Sets</td><td><code>oaiListSets</code></td><td>Returns the arXiv sets (subject archives, e.g. cs, math, physics:hep-th) available for selective harvesting. Docs: https://info.arxiv.org/help/oa/index.html</td></tr><tr><td>Search Articles</td><td><code>searchArticles</code></td><td>Searches arXiv papers with field prefixes (ti: title, au: author, abs: abstract, co: comment, jr: journal ref, cat: category, rn: report number, all:) and AND/OR/ANDNOT, or fetches papers by id; returns an Atom XML feed with title, authors, summary, dates, categories, DOI and PDF links. Docs: https://info.arxiv.org/help/api/user-manual.html</td></tr></tbody></table>
