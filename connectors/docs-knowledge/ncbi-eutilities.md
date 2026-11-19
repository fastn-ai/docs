---
description: "Connect NCBI E-utilities to your product with fastn."
hidden: true
---

# NCBI E-utilities

<img src="../../.gitbook/assets/connectors/lg/ncbi-eutilities.png" alt="NCBI E-utilities logo">

NCBI E-utilities (Entrez Programming Utilities) is the free public API to the 38 NCBI Entrez databases, including PubMed, PMC, Gene, Protein, Nucleotide and Taxonomy. Search databases, get summaries, fetch full records, find linked records, use the History server, check spelling and match citations to PubMed IDs. No API key needed (up to 3 requests per second).

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [ncbi.nlm.nih.gov](https://ncbi.nlm.nih.gov) |
| **Authentication** | No authentication |
| **Slug** | `ncbiEutilities` |

## Use it

Add NCBI E-utilities from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ncbiEutilities.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Fetch Records</td><td><code>fetchRecords</code></td><td>Download full records for UIDs or a History server set in the chosen format, e.g. PubMed abstracts as text or XML, GenBank or FASTA sequences (EFetch, GET efetch.fcgi). Returned as text. Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Find Linked Records</td><td><code>findLinkedRecords</code></td><td>Find records linked to UIDs within the same or another Entrez database, e.g. PMC articles citing a PubMed paper or related articles (ELink, GET elink.fcgi). Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Get Database Info</td><td><code>getDatabaseInfo</code></td><td>List all Entrez databases, or get one database's record count, last update, searchable fields and available links (EInfo, GET einfo.fcgi). Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Get Document Summaries</td><td><code>getDocumentSummaries</code></td><td>Get document summaries (title, authors, source, dates and more) for UIDs, or for a History server set (ESummary, GET esummary.fcgi). Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Get Spelling Suggestions</td><td><code>getSpellingSuggestions</code></td><td>Get spelling corrections for an Entrez query, e.g. asthmaa -&gt; asthma (ESpell, GET espell.fcgi). Returns XML text. Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Match Citations to PubMed IDs</td><td><code>matchCitations</code></td><td>Find PubMed IDs for citation strings (journal|year|volume|first page|author|key|), one or many separated by %0D (ECitMatch, GET ecitmatch.cgi). Returns text lines ending with the PMID. Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Post UIDs to History Server</td><td><code>postIdsToHistory</code></td><td>Upload a list of UIDs to the Entrez History server and get a WebEnv + query_key to use in later calls (EPost, POST epost.fcgi). Returns XML text. Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr><tr><td>Search Database</td><td><code>searchDatabase</code></td><td>Search an Entrez database with a text query and get matching UIDs, the count and the query translation; optionally store results on the History server (ESearch, GET esearch.fcgi). Docs: https://www.ncbi.nlm.nih.gov/books/NBK25499/</td></tr></tbody></table>
