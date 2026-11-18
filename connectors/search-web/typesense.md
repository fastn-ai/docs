---
description: "Typesense is an open-source, typo-tolerant search engine."
---

# Typesense

Typesense is an open-source, typo-tolerant search engine. This connector wraps the Typesense Server API (v30.x) for managing collections, documents (index/upsert/update/import/export/search/multi_search), aliases, API keys, synonym sets, curation/override sets, stopwords, analytics rules and events, and cluster operations. Base URL is per-cluster; supply your cluster host and API key.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [typesense.org](https://typesense.org) |
| **Authentication** | Credentials you enter |
| **Actions** | 82 |
| **Events** | 0 |
| **Slug** | `typesense` |

## Use it

Add Typesense from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.typesense.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Clear Cache | `clearCache` | Clear the in-memory search query cache. POST /operations/cache/clear |
| Compact Database | `compactDatabase` | Compact the underlying RocksDB database on disk. POST /operations/db/compact |
| Create Analytics Event | `createAnalyticsEvent` | Submit a single analytics event (click, conversion, query, visit) tied to an existing rule. POST /analytics/events |
| Create Analytics Rule | `createAnalyticsRule` | Create an analytics rule (popular_queries, nohits_queries, counter or log). POST /analytics/rules |
| Create API Key | `createApiKey` | Create an API key with fine-grained actions and collection scopes. POST /keys. The key value is only returned once. |
| Create Collection | `createCollection` | Create a new collection with a schema of fields. POST /collections |
| Create Conversation Model | `createConversationModel` | Create a conversational (RAG) model that powers conversational search, backed by an LLM and a conversation history collection. |
| Create NL Search Model | `createNlSearchModel` | Create a new NL search model. POST /nl_search_models |
| Create Snapshot | `createSnapshot` | Create a point-in-time snapshot of the data directory for backups. POST /operations/snapshot?snapshot_path=... |
| Debug | `debug` | Print debugging information including the Typesense server version. GET /debug |
| Delete Alias | `deleteAlias` | Delete an alias. DELETE /aliases/{aliasName} |
| Delete Analytics Rule | `deleteAnalyticsRule` | Delete an analytics rule by name. DELETE /analytics/rules/{ruleName} |
| Delete API Key | `deleteApiKey` | Delete an API key by id. DELETE /keys/{keyId} |
| Delete Conversation Model | `deleteConversationModel` | Delete a conversational (RAG) model by id. |
| Delete Curation Set | `deleteCurationSet` | Delete a curation set and all its items. DELETE /curation_sets/{curationSetName} |
| Delete Curation Set Item | `deleteCurationItem` | Delete a single curation item (override rule) from a set. DELETE /curation_sets/{curationSetName}/items/{itemId} |
| Delete Document | `deleteDocument` | Delete a single document by id. DELETE /collections/{collectionName}/documents/{documentId} |
| Delete Documents By Filter | `deleteDocumentsByFilter` | Delete all documents matching a filter_by condition (or truncate the collection). DELETE /collections/{collectionName}/documents?filter_by=... |
| Delete NL Search Model | `deleteNlSearchModel` | Delete a Natural Language Search model by id. |
| Delete Preset | `deletePreset` | Delete a search preset by name. |
| Delete Stemming Dictionary | `deleteStemmingDictionary` | Delete a stemming dictionary by its ID. Collections whose fields reference the dictionary should be updated first. |
| Delete Stopwords Set | `deleteStopwordsSet` | Delete a stopwords set. DELETE /stopwords/{setId} |
| Delete Synonym Set | `deleteSynonymSet` | Delete a synonym set and all its items. DELETE /synonym_sets/{synonymSetName} |
| Delete Synonym Set Item | `deleteSynonymItem` | Delete a single synonym item from a set. DELETE /synonym_sets/{synonymSetName}/items/{itemId} |
| Drop Collection | `dropCollection` | Permanently drop a collection and all its documents. DELETE /collections/{collectionName} |
| Export Documents | `exportDocuments` | Export all documents in a collection as newline-delimited JSON. GET /collections/{collectionName}/documents/export |
| Flush Analytics | `flushAnalytics` | Flush buffered analytics events/aggregations to their destination collections immediately. POST /analytics/flush |
| Get Alias | `getAlias` | Retrieve a single alias. GET /aliases/{aliasName} |
| Get Analytics Events | `getAnalyticsEvents` | Retrieve the most recent analytics events for a user and rule. GET /analytics/events |
| Get Analytics Rule | `getAnalyticsRule` | Retrieve a single analytics rule by name. GET /analytics/rules/{ruleName} |
| Get Analytics Status | `getAnalyticsStatus` | Retrieve the status of the analytics subsystem. GET /analytics/status |
| Get API Key | `getApiKey` | Retrieve metadata about a single API key by id (value is masked). GET /keys/{keyId} |
| Get Collection | `getCollection` | Retrieve the details of a single collection. GET /collections/{collectionName} |
| Get Conversation Model | `getConversationModel` | Retrieve a single conversational (RAG) model by id. |
| Get Curation Set | `getCurationSet` | Retrieve a single curation set with all its items. GET /curation_sets/{curationSetName} |
| Get Curation Set Item | `getCurationItem` | Retrieve a single curation item (override rule) by id. GET /curation_sets/{curationSetName}/items/{itemId} |
| Get Document | `getDocument` | Fetch a single document by id. GET /collections/{collectionName}/documents/{documentId} |
| Get Metrics | `getMetrics` | Get current system metrics (CPU, memory, disk, network) of the node. GET /metrics.json |
| Get NL Search Model | `getNlSearchModel` | Retrieve a single Natural Language Search model by id. |
| Get Preset | `getPreset` | Retrieve a single search preset by name. |
| Get Schema Changes | `getSchemaChanges` | Get the status of in-progress collection schema change operations. GET /operations/schema_changes |
| Get Stats | `getStats` | Get current API request statistics (latencies, request counts per endpoint). GET /stats.json |
| Get Stemming Dictionary | `getStemmingDictionary` | Retrieve a single stemming dictionary by id, including its word/root mappings. |
| Get Stopwords Set | `getStopwordsSet` | Retrieve a single stopwords set. GET /stopwords/{setId} |
| Get Synonym Set | `getSynonymSet` | Retrieve a single synonym set with all its items. GET /synonym_sets/{synonymSetName} |
| Get Synonym Set Item | `getSynonymItem` | Retrieve a single synonym item by id within a set. GET /synonym_sets/{synonymSetName}/items/{itemId} |
| Health Check | `health` | Check whether the Typesense node is healthy. GET /health |
| Import Documents | `importDocuments` | Bulk import documents formatted as newline-delimited JSON (JSONL). POST /collections/{collectionName}/documents/import. Body is the raw JSONL string. |
| Import Stemming Dictionary | `importStemmingDictionary` | Upsert a stemming dictionary of word -&gt; root mappings. Body is JSONL (one mapping per line). The dictionary id is supplied as a query param. |
| Index Document | `indexDocument` | Index a single document into a collection. The document is sent as a JSON object whose fields must match the collection's own schema. |
| List Aliases | `listAliases` | List all aliases and the collections they map to. GET /aliases |
| List Analytics Rules | `listAnalyticsRules` | Retrieve all analytics rules, optionally filtered by rule_tag. GET /analytics/rules |
| List API Keys | `listApiKeys` | Retrieve metadata about all API keys (values are masked). GET /keys |
| List Collections | `listCollections` | Retrieve a summary of all collections. GET /collections |
| List Conversation Models | `listConversationModels` | Retrieve all conversational (RAG) models. |
| List Curation Set Items | `listCurationItems` | List all items (override rules) within a curation set. GET /curation_sets/{curationSetName}/items |
| List Curation Sets | `listCurationSets` | List all curation (overrides) sets. GET /curation_sets |
| List NL Search Models | `listNlSearchModels` | Retrieve all Natural Language Search models. |
| List Presets | `listPresets` | Retrieve all registered search presets. |
| List Stemming Dictionaries | `listStemmingDictionaries` | Retrieve the ids of all stemming dictionaries. |
| List Stopwords Sets | `listStopwordsSets` | List all stopwords sets. GET /stopwords |
| List Synonym Set Items | `listSynonymItems` | List all items within a synonym set. GET /synonym_sets/{synonymSetName}/items |
| List Synonym Sets | `listSynonymSets` | List all synonym sets. GET /synonym_sets |
| Multi Search | `multiSearch` | Run multiple search queries in a single HTTP request for performance. POST /multi_search |
| Reset Peers | `resetPeers` | Reset the Raft peer list of this node from its nodes configuration, used to recover a cluster that has lost quorum. Disruptive cluster operation; run only during recovery. |
| Search Documents | `searchDocuments` | Search a collection for documents. GET /collections/{collectionName}/documents/search. q and query_by are required. |
| Trigger Vote | `triggerVote` | Trigger a Raft leader re-election on this node. POST /operations/vote |
| Update Analytics Rule | `updateAnalyticsRule` | Update (replace) an analytics rule by name. PUT /analytics/rules/{ruleName} |
| Update Collection | `updateCollection` | Update a collection's schema in place to alter, drop or add fields. PATCH /collections/{collectionName} |
| Update Config | `updateConfig` | Enable or disable slow request logging. Set logSlowRequestsTimeMs to -1 to disable, or a positive integer to log requests slower than that many ms. POST /config |
| Update Conversation Model | `updateConversationModel` | Update an existing conversational (RAG) model by id. |
| Update Document | `updateDocument` | Partially update a single document by its id. Only the fields present in the supplied JSON object are changed; every other field on the document is left untouched. |
| Update Documents by Filter | `updateDocumentsByFilter` | Partially update every document matching a filter condition. Only the fields present in the supplied JSON object are changed on the matched documents. |
| Update NL Search Model | `updateNlSearchModel` | Update an existing Natural Language Search model by id. |
| Upsert Alias | `upsertAlias` | Create or update an alias mapping to a collection. PUT /aliases/{aliasName} |
| Upsert Curation Set | `upsertCurationSet` | Create or update a curation (overrides) set - top-level, shareable across collections (v30+). PUT /curation_sets/{curationSetName} |
| Upsert Curation Set Item | `upsertCurationItem` | Create or update a single curation item (override rule) within a set. PUT /curation_sets/{curationSetName}/items/{itemId} |
| Upsert Document | `upsertDocument` | Upsert a document into a collection, creating it if the id is new and replacing it if the id already exists. The document is sent as a JSON object whose fields must match the collection's own schema. |
| Upsert Preset | `upsertPreset` | Create or update a search preset (named, reusable set of search parameters) by name. |
| Upsert Stopwords Set | `upsertStopwordsSet` | Create or update a stopwords set. PUT /stopwords/{setId} |
| Upsert Synonym Set | `upsertSynonymSet` | Create or update a synonym set (top-level, shareable across collections, v30+). PUT /synonym_sets/{synonymSetName} |
| Upsert Synonym Set Item | `upsertSynonymItem` | Create or update a single synonym item within a set. PUT /synonym_sets/{synonymSetName}/items/{itemId} |
