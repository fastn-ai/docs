---
description: "NCBI E-utilities searches PubMed and other NCBI databases. Search databases, fetch records and summaries, and find linked records."
hidden: true
---

# NCBI E-utilities

<img src="../../.gitbook/assets/connectors/lg/ncbi-eutilities.png" alt="NCBI E-utilities logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [ncbi.nlm.nih.gov](https://ncbi.nlm.nih.gov) |
| **Authentication** | No sign-in needed |
| **Slug** | `ncbiEutilities` |

## Setup

NCBI E-utilities needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect NCBI E-utilities from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **NCBI E-utilities**.
2. Select **Connect** on the NCBI E-utilities card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. NCBI E-utilities needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use NCBI E-utilities's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Fetch Records</td><td><code>fetchRecords</code></td><td>Download full records for UIDs or a History server set in the chosen format, e.g. PubMed abstracts as text or XML, GenBank or FASTA sequences (EFetch, GET efetch.fcgi). Returned as text. Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Find Linked Records</td><td><code>findLinkedRecords</code></td><td>Find records linked to UIDs within the same or another Entrez database, e.g. PMC articles citing a PubMed paper or related articles (ELink, GET elink.fcgi). Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Get Database Info</td><td><code>getDatabaseInfo</code></td><td>List all Entrez databases, or get one database's record count, last update, searchable fields and available links (EInfo, GET einfo.fcgi). Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Get Document Summaries</td><td><code>getDocumentSummaries</code></td><td>Get document summaries (title, authors, source, dates and more) for UIDs, or for a History server set (ESummary, GET esummary.fcgi). Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Get Spelling Suggestions</td><td><code>getSpellingSuggestions</code></td><td>Get spelling corrections for an Entrez query, e.g. asthmaa -&gt; asthma (ESpell, GET espell.fcgi). Returns XML text. Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Match Citations to PubMed IDs</td><td><code>matchCitations</code></td><td>Find PubMed IDs for citation strings (journal|year|volume|first page|author|key|), one or many separated by %0D (ECitMatch, GET ecitmatch.cgi). Returns text lines ending with the PMID. Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Post UIDs to History Server</td><td><code>postIdsToHistory</code></td><td>Upload a list of UIDs to the Entrez History server and get a WebEnv + query_key to use in later calls (EPost, POST epost.fcgi). Returns XML text. Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Search Database</td><td><code>searchDatabase</code></td><td>Search an Entrez database with a text query and get matching UIDs, the count and the query translation; optionally store results on the History server (ESearch, GET esearch.fcgi). Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr></tbody></table>

