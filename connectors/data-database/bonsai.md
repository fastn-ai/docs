---
description: "Bonsai is a fully managed Elasticsearch and OpenSearch hosting service."
hidden: true
---

# Bonsai

<img src="../../.gitbook/assets/connectors/lg/bonsai.png" alt="Bonsai logo">

Bonsai is a fully managed Elasticsearch and OpenSearch hosting service. This connector works directly against a Bonsai cluster's search REST API: create and manage indices, mappings, settings and aliases; index, get, update, bulk load and delete documents; run searches, counts, multi-searches, scrolls, point-in-time searches, explain and validation; analyze text; manage ingest pipelines, stored scripts, templates and data streams; and read cluster, node and cat health and statistics. Endpoints that Bonsai restricts on shared (multi-tenant) plans return a permission error explaining the restriction. Authenticates with the cluster access key and access secret over HTTP Basic auth.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [bonsai.io](https://bonsai.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `bonsai` |

## Use it

Add Bonsai from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bonsai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Index Block | `addIndexBlock` | Adds a write, read, read_only or metadata block to one or more indices. Bonsai blocks this API on shared plans; the equivalent index.blocks.* settings can be changed with Update Index Settings. |
| Analyze Text | `analyzeText` | Runs text through a built-in analyzer, or a custom combination of tokenizer and filters, and returns the resulting tokens. Useful for testing analysis without an index. |
| Analyze Text With Index Analyzer | `analyzeTextInIndex` | Runs text through the analyzer of a specific index field or a custom analyzer defined in that index, and returns the resulting tokens. |
| Bulk Document Operations | `bulkDocuments` | Performs many index, create, update and delete operations in one request using the newline-delimited JSON bulk format. Check the errors flag and per-item results in the response. |
| Cat Aliases | `catAliases` | Returns table rows of aliases with their index, filter, routing and write-index flag. |
| Cat Allocation | `catAllocation` | Returns table rows showing, per node, how many shards are allocated and how much disk is used and available. |
| Cat Cluster Manager | `catClusterManager` | Returns the id, host, IP and name of the elected cluster manager node. |
| Cat Count | `catCount` | Returns a one-row document count for one or more indices (or all indices). |
| Cat Health | `catHealth` | Returns a one-row summary of cluster health: status, node counts and shard counts. |
| Cat Indices | `catIndices` | Returns a compact table (as JSON rows) of indices with health, status, primary and replica counts, document counts and store size. |

<details>

<summary>See 82 more actions</summary>

* **Cat Node Attributes** `catNodeAttributes`: Returns table rows of custom node attributes (such as zone or region) for each node.
* **Cat Nodes** `catNodes`: Returns table rows of cluster nodes with IP, heap and RAM usage, CPU, load averages, roles and whether each is the cluster manager.
* **Cat Plugins** `catPlugins`: Returns table rows of plugins installed on each node, with component name and version.
* **Cat Recovery** `catRecovery`: Returns table rows of shard recoveries (ongoing and completed) for one or more indices with type, stage, source, target and progress.
* **Cat Segments** `catSegments`: Returns table rows of Lucene segments per shard for one or more indices, with document counts, size and committed/searchable flags.
* **Cat Templates** `catTemplates`: Returns table rows of index templates with their index patterns, order, version and composed-of component templates.
* **Cat Thread Pool** `catThreadPool`: Returns table rows of thread pool usage per node (active, queued and rejected tasks), optionally for specific pools such as search or write.
* **Clear Index Cache** `clearIndexCache`: Clears the query, request and fielddata caches of one or more indices.
* **Clear Scroll** `clearScroll`: Releases one or more scroll contexts before their keep-alive expires, freeing cluster resources.
* **Close Index** `closeIndex`: Closes one or more indices, blocking reads and writes while keeping the data on disk. Closed indices can be reopened with Open Index.
* **Count Documents** `countDocuments`: Counts the documents in one or more indices that match an optional Query DSL query. Use _all to count across every index.
* **Create Data Stream** `createDataStream`: Creates a data stream for append-only time-series data. A composable index template with data_stream enabled must match the name first; on Bonsai shared plans composable templates are restricted, so creation fails with 'no matching index template'.
* **Create Document** `createDocument`: Creates a document with a specific id only if no document with that id exists; returns a version conflict error otherwise.
* **Create Index** `createIndex`: Creates a new index on the Bonsai cluster with optional settings (shards, replicas, analysis), field mappings and aliases.
* **Create Or Update Alias** `putAlias`: Adds an alias to one or more indices, optionally with a filter, routing or as the write index.
* **Create Or Update Ingest Pipeline** `putIngestPipeline`: Creates or replaces an ingest pipeline: an ordered list of processors (set, rename, remove, date, grok, script, etc.) that transform documents before indexing.
* **Create Or Update Legacy Index Template** `putLegacyTemplate`: Creates or replaces a legacy index template that applies settings, mappings and aliases to new indices whose names match its patterns. Composable index templates are restricted on Bonsai shared plans, but legacy templates are allowed.
* **Create Or Update Stored Script** `putStoredScript`: Stores a Painless script (or search template) under an id so it can be referenced in searches, updates and aggregations.
* **Create Point In Time** `createPointInTime`: Opens a point-in-time (PIT) snapshot of one or more indices so consistent paginated searches can be run with search_after. Returns the PIT id.
* **Delete Alias** `deleteAlias`: Removes an alias from one or more indices. The indices themselves are not affected.
* **Delete Data Stream** `deleteDataStream`: Deletes a data stream and all of its backing indices.
* **Delete Document** `deleteDocument`: Deletes a document by id from an index. Returns result not_found (HTTP 404) when the document does not exist.
* **Delete Documents By Query** `deleteByQuery`: Deletes every document in an index that matches a query. Bonsai blocks this on shared multi-tenant plans (permission error); it is available on dedicated Business and Enterprise clusters.
* **Delete Index** `deleteIndex`: Permanently deletes one or more indices and all their documents. Bonsai does not allow deleting everything at once with _all or *; name the indices explicitly.
* **Delete Ingest Pipeline** `deleteIngestPipeline`: Deletes an ingest pipeline by id.
* **Delete Legacy Index Template** `deleteLegacyTemplate`: Deletes a legacy index template by name. Existing indices are not affected.
* **Delete Points In Time** `deletePointsInTime`: Closes one or more point-in-time (PIT) contexts by id, freeing their resources.
* **Delete Stored Script** `deleteStoredScript`: Deletes a stored script or search template by id.
* **Evaluate Search Ranking** `rankEval`: Evaluates the quality of ranked search results for a set of typical queries against rated documents using a metric such as precision or recall. Bonsai blocks this on shared multi-tenant plans.
* **Explain Document Score** `explainDocument`: Explains whether a specific document matches a query and how its relevance score is computed.
* **Explain Shard Allocation** `explainShardAllocation`: Explains why a shard is unassigned or why it remains on its current node. With no shard specified, explains the first unassigned shard; returns an error when every shard is assigned.
* **Flush Index** `flushIndex`: Flushes one or more indices, committing in-memory operations to disk. On Bonsai shared plans the shard-level flush is refused and reported as shard failures inside an HTTP 200 response; check _shards.failed.
* **Force Merge Index** `forceMergeIndex`: Merges the Lucene segments of one or more indices to reduce segment count and reclaim space from deleted documents.
* **Get Alias** `getAlias`: Returns the indices an alias (or comma-separated aliases / wildcard) points to, with each alias's filter and routing.
* **Get Cluster Health** `getClusterHealth`: Returns the health status (green, yellow or red) of the cluster or specific indices, with node and shard counts. Can wait for a target status.
* **Get Cluster Info** `getClusterInfo`: Returns basic information about the Bonsai cluster: node name, cluster name and UUID, search engine distribution (Elasticsearch or OpenSearch), version and build details.
* **Get Cluster Settings** `getClusterSettings`: Returns persistent and transient cluster-level settings, optionally including defaults. Cluster settings are read-only on Bonsai.
* **Get Cluster State** `getClusterState`: Returns cluster state metadata such as the elected cluster manager, nodes, index metadata and routing table, optionally limited to specific metrics and indices.
* **Get Cluster Stats** `getClusterStats`: Returns cluster-wide statistics: index and shard counts, document counts, store size, and node OS, JVM, filesystem and plugin summaries.
* **Get Composable Index Templates** `getIndexTemplates`: Returns composable index templates by name or wildcard. Bonsai restricts composable index and component templates on shared multi-tenant plans (permission error); use the legacy template actions there.
* **Get Data Streams** `getDataStreams`: Lists data streams on the cluster, or those matching a name or wildcard, with their backing indices, generation, template and health status.
* **Get Document** `getDocument`: Retrieves a document by id from an index, including its source, version, sequence number and whether it was found.
* **Get Document Source** `getDocumentSource`: Returns only the source fields of a document by id, without metadata.
* **Get Field Capabilities** `getFieldCapabilities`: Returns the type and whether each field is searchable and aggregatable across one or more indices.
* **Get Field Mapping** `getFieldMapping`: Returns the mapping definition of specific fields in one or more indices.
* **Get Index** `getIndex`: Returns the aliases, mappings and settings of one or more indices. The response is keyed by index name.
* **Get Index Mapping** `getMapping`: Returns the field mappings of one or more indices, keyed by index name.
* **Get Index Recovery** `getIndexRecovery`: Returns information about ongoing and completed shard recoveries for one or more indices, including stage, source, target and progress.
* **Get Index Segments** `getIndexSegments`: Returns low-level Lucene segment information (generation, document counts, size, committed and searchable flags) for the shards of one or more indices.
* **Get Index Settings** `getIndexSettings`: Returns the settings of one or more indices, keyed by index name, optionally filtered to specific setting names.
* **Get Index Stats** `getIndexStats`: Returns statistics for one or more indices: document counts, store size, indexing, search, merge, refresh and cache metrics.
* **Get Ingest Pipeline** `getIngestPipeline`: Returns the definition of one or more ingest pipelines by id (comma-separated ids or wildcards). Use * to list all pipelines; the cluster returns 404 with an empty object when none match.
* **Get Legacy Index Template** `getLegacyTemplate`: Returns one or more legacy index templates by name (comma-separated or wildcard). Use * to list all.
* **Get Multiple Term Vectors** `getMultipleTermVectors`: Returns term vectors for several documents of an index in one request.
* **Get Nodes Info** `getNodesInfo`: Returns static information about cluster nodes, such as settings, OS, process, JVM, thread pools, transport, HTTP, plugins and ingest processors, for selected nodes and metrics.
* **Get Nodes Stats** `getNodesStats`: Returns runtime statistics for cluster nodes, such as indices, OS, process, JVM, thread pool, filesystem, transport, HTTP, breaker and ingest metrics, for selected nodes and metrics.
* **Get Search Shards** `getSearchShards`: Returns the nodes and shards a search request against the given indices would be executed on.
* **Get Shard Stores** `getShardStores`: Returns store information about shard copies of one or more indices. By default only shards with unassigned or problematic copies are listed, so a healthy index returns an empty result.
* **Get Stored Script** `getStoredScript`: Retrieves a stored script or search template by id.
* **Get Term Vectors** `getTermVectors`: Returns term information and statistics (term frequency, positions, offsets) for the fields of a stored document.
* **Index Document** `indexDocument`: Adds or replaces a document with a specific id in an index. The document body is free-form JSON because each index defines its own fields.
* **Index Document With Generated ID** `indexDocumentAutoId`: Adds a new document to an index and lets the cluster generate its id. Returns the generated id.
* **List Index Aliases** `listIndexAliases`: Lists all aliases defined on one or more indices. Use _all to list every alias on the cluster.
* **List Points In Time** `listPointsInTime`: Lists all open point-in-time (PIT) contexts on the cluster with their ids, creation time and keep-alive.
* **List Tasks** `listTasks`: Lists tasks currently running on cluster nodes, optionally filtered by action pattern and grouped. Bonsai disables the Tasks API on shared multi-tenant plans (permission error); it is available by request on Business and Enterprise.
* **Multi Get Documents** `multiGetDocuments`: Retrieves several documents in one request, each identified by index and id, possibly across different indices.
* **Multi Search** `multiSearch`: Runs several searches in one request using newline-delimited JSON pairs of header and query lines. Returns one response per search in order.
* **Open Index** `openIndex`: Reopens one or more closed indices so they can be searched and written again.
* **Refresh Index** `refreshIndex`: Refreshes one or more indices so recently indexed documents become visible to search.
* **Resize Index** `resizeIndex`: Copies a read-only index into a new index with the same (clone), fewer (shrink) or more (split) primary shards. Bonsai blocks index resizing on shared multi-tenant plans.
* **Resolve Index** `resolveIndex`: Resolves index names, aliases, data streams and wildcard patterns to the concrete indices, aliases and data streams they match.
* **Roll Over Alias To New Index** `rolloverIndex`: Creates a new index for a write alias and switches the alias to it, optionally only when conditions such as maximum age, document count or size are met.
* **Scroll Search Results** `scrollSearch`: Fetches the next batch of hits for a scroll context opened by Search Documents with a scroll keep-alive, extending the context for another interval.
* **Search Documents** `searchDocuments`: Runs a Query DSL search against one or more indices or aliases, with paging, sorting, source filtering, aggregations and highlighting. Use _all as the index to search every index.
* **Search With Template** `searchTemplate`: Runs a search defined by a Mustache search template (inline source or stored template id) with parameters. Bonsai blocks search templates on shared multi-tenant plans.
* **Simulate Ingest Pipeline** `simulateIngestPipeline`: Runs sample documents through an inline pipeline definition and returns the transformed documents, without indexing anything.
* **Update Aliases** `updateAliases`: Atomically adds and removes index aliases in a single request, for example to swap an alias from an old index to a new one.
* **Update Document** `updateDocument`: Partially updates a document by merging fields, running a Painless script, or upserting when the document does not exist.
* **Update Documents By Query** `updateByQuery`: Updates every document in an index that matches a query, optionally applying a Painless script to each. Bonsai may restrict this on some plans.
* **Update Index Mapping** `putMapping`: Adds new fields to an index mapping or updates compatible options of existing fields. Existing field types cannot be changed.
* **Update Index Settings** `updateIndexSettings`: Changes dynamic settings of one or more indices, such as refresh interval, number of replicas or max result window.
* **Validate Query** `validateQuery`: Checks whether a Query DSL query is valid for an index without running it, optionally explaining why it is invalid or how it is rewritten.

</details>
