---
description: "Algolia is a hosted search and discovery platform."
hidden: true
---

# Algolia

Algolia is a hosted search and discovery platform. This connector wraps the Algolia Search, Analytics, Insights and Monitoring REST APIs to manage indices, records, settings, synonyms, rules, dictionaries, API keys and user-ID clusters, to read search and conversion analytics, to send click and conversion events, and to read Algolia infrastructure status.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [algolia.com](https://algolia.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 89 |
| **Events** | 0 |
| **Slug** | `algolia` |

## Use it

Add Algolia from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.algolia.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Allowed Source | `appendSource` | Add a source. Adds a source to the list of allowed sources. |
| Add Or Replace Record | `addOrUpdateObject` | Add or replace a record. If a record with the specified object ID exists, the existing record is replaced. The record body is schemaless: pass each record attribute as a top-level input alongside the declared fields and it is sent verbatim in the request body. |
| Assign Multiple User IDs | `batchAssignUserIds` | Assign multiple userIDs. Assigns multiple user IDs to a cluster. |
| Assign User ID | `assignUserId` | Assign or move a user ID. Assigns or moves a user ID to a cluster. |
| Batch Dictionary Entries | `batchDictionaryEntries` | Add or delete dictionary entries. Adds or deletes multiple entries from your plurals, segmentation, or stop word dictionaries. |
| Batch Index Operations | `batchIndexOperations` | Batch indexing operations on one index. Adds, updates, or deletes records in one index with a single API request. |
| Batch Operations Across Indices | `batchOperationsAcrossIndices` | Batch indexing operations on multiple indices. Adds, updates, or deletes records in multiple indices with a single API request. |
| Browse Records | `browse` | Browse for records. Retrieves records from an index, up to 1,000 per request. |
| Clear Index Records | `clearObjects` | Delete all records from an index. Deletes only the records from an index while keeping settings, synonyms, and rules. |
| Clear Rules | `clearRules` | Delete all rules. Deletes all rules from the index. |
| Clear Synonyms | `clearSynonyms` | Delete all synonyms. Deletes all synonyms from the index. |
| Copy Or Move Index | `operationIndex` | Copy or move an index. Copies or moves (renames) an index within the same Algolia application. |
| Create API Key | `addApiKey` | Create an API key. Creates a new API key with specific permissions and restrictions. |
| Create Record | `createRecord` | Add a new record (with auto-generated object ID). Adds a record to an index or replaces it. The record body is schemaless: pass each record attribute as a top-level input alongside the declared fields and it is sent verbatim in the request body. |
| Delete Allowed Source | `deleteSource` | Delete a source. Deletes a source from the list of allowed sources. |
| Delete API Key | `deleteApiKey` | Delete an API key. Deletes the API key. |
| Delete Index | `deleteIndex` | Delete an index. Deletes an index and all its settings. |
| Delete Record | `deleteObject` | Delete a record. Deletes a record by its object ID. |
| Delete Records By Query | `deleteBy` | Delete records matching a filter. This operation doesn't accept empty filters. |
| Delete Rule | `deleteRule` | Delete a rule. Deletes a rule by its ID. |
| Delete Synonym | `deleteSynonym` | Delete a synonym. Deletes a synonym by its ID. |
| Delete User ID | `removeUserId` | Delete user ID. Deletes a user ID and its associated data from the clusters. |
| Delete User Token Events | `deleteUserToken` | Delete user token events. Deletes all events related to the specified user token from events metrics and analytics. |
| Get Add To Cart Rate | `getAddToCartRate` | Retrieve add-to-cart rate. Retrieves the add-to-cart rate for all your searches with at least one add-to-cart event, including a daily breakdown. |
| Get Analytics Update Status | `getAnalyticsUpdateStatus` | Retrieve update status. Retrieves the time when the Analytics data for the specified index was last updated. |
| Get API Key | `getApiKey` | Retrieve API key permissions. Gets the permissions and restrictions of an API key. |
| Get Application Task Status | `getAppTask` | Check application task status. Checks the status of a given application task. |
| Get Average Click Position | `getAverageClickPosition` | Retrieve average click position. Retrieves the average click position of your search results, including a daily breakdown. |
| Get Click Positions | `getClickPositions` | Retrieve click positions. Retrieves the positions in the search results and their associated number of clicks. |
| Get Click Through Rate | `getClickThroughRate` | Retrieve click-through rate. Retrieves the click-through rate (CTR) for all your searches with at least one click event, including a daily breakdown. |
| Get Cluster Status | `getClusterStatus` | Retrieve cluster status. Retrieves the status of selected clusters. |
| Get Cluster Status Overview | `getClusterStatusOverview` | Retrieve status of all clusters. Retrieves the status of all Algolia clusters and instances. |
| Get Conversion Rate | `getConversionRate` | Retrieve conversion rate. Retrieves the conversion rate (CR) for all your searches with at least one conversion event, including a daily breakdown. |
| Get Dictionary Settings | `getDictionarySettings` | Retrieve dictionary settings. Retrieves the languages for which standard dictionary entries are turned off. |
| Get Index Settings | `getSettings` | Retrieve index settings. Retrieves an object with non-null index settings. |
| Get Index Task Status | `getTask` | Check task status. Checks the status of a given task. |
| Get Indexing Latency | `getIndexingLatency` | Retrieve indexing monitoring latency. Retrieves indexing latency metrics for selected clusters. |
| Get Infrastructure Metrics | `getInfrastructureMetrics` | Retrieve metrics. Retrieves metrics related to your Algolia infrastructure, aggregated over a selected time window. |
| Get Multiple Records | `getObjects` | Retrieve records. Retrieves one or more records, potentially from different indices. |
| Get No Click Rate | `getNoClickRate` | Retrieve no click rate. Retrieves the fraction of searches that didn't lead to any click within a time range, including a daily breakdown. |
| Get No Results Rate | `getNoResultsRate` | Retrieve no results rate. Retrieves the fraction of searches that didn't return any results within a time range, including a daily breakdown. |
| Get Purchase Rate | `getPurchaseRate` | Retrieve purchase rate. Retrieves the purchase rate for all your searches with at least one purchase event, including a daily breakdown. |
| Get Record | `getObject` | Retrieve a record. Retrieves one record by its object ID. |
| Get Revenue | `getRevenue` | Retrieve revenue data. Retrieves revenue-related metrics, such as the total revenue or the average order value. |
| Get Rule | `getRule` | Retrieve a rule. Retrieves a rule by its ID. |
| Get Search Latency | `getSearchLatency` | Retrieve search latency times. Retrieves the average latency for search requests for selected clusters. |
| Get Searches Count | `getSearchesCount` | Retrieve number of searches. Retrieves the number of searches within a time range, including a daily breakdown. |
| Get Synonym | `getSynonym` | Retrieve a synonym. Retrieves a synonym by its ID. |
| Get Top User IDs | `getTopUserIds` | Get top user IDs. Get the IDs of the 10 users with the highest number of records per cluster. |
| Get User ID | `getUserId` | Retrieve user ID. Returns the user ID data stored in the mapping. |
| Get User ID Mapping Status | `hasPendingMappings` | Get migration and user mapping status. To determine when the time-consuming process of creating a large batch of users or migrating users from one cluster to another is complete, this operation retrieves the status of the process. |
| Get Users Count | `getUsersCount` | Retrieve number of users. Retrieves the number of unique users within a time range, including a daily breakdown. |
| List Allowed Sources | `getSources` | List allowed sources. Retrieves all allowed IP addresses with access to your application. |
| List API Keys | `listApiKeys` | List API keys. Lists all API keys associated with your Algolia application, including their permissions and restrictions. |
| List Cluster Incidents | `listClusterIncidents` | Retrieve cluster incidents. Retrieves known incidents for the selected clusters. |
| List Clusters | `listClusters` | List clusters. Lists the available clusters in a multi-cluster setup. |
| List Dictionary Languages | `getDictionaryLanguages` | List available languages. Lists supported languages with their supported dictionary types and number of custom entries. |
| List Incidents | `listIncidents` | Retrieve all incidents. Retrieves known incidents for all clusters. |
| List Indices | `listIndices` | List indices. Lists all indices in the current Algolia application. |
| List Logs | `getLogs` | Retrieve log entries. The request must be authenticated by an API key with the logs ACL. |
| List Searches Without Clicks | `listSearchesWithoutClicks` | Retrieve top searches without clicks. Retrieves the most popular searches that didn't lead to any clicks, from the 1,000 most frequent searches. |
| List Searches Without Results | `listSearchesWithoutResults` | Retrieve the most frequent searches without results. Retrieves the 1,000 most frequent searches that produced zero results. |
| List Servers | `listServers` | Retrieve servers. Retrieves the servers that belong to clusters. |
| List Top Countries | `listTopCountries` | Retrieve top countries. Retrieves the countries with the most searches in your index. |
| List Top Filter Attributes | `listTopFilterAttributes` | Retrieve top filters. Retrieves the 1,000 most frequently used filter attributes. |
| List Top Filter Values | `listTopFilterValues` | Retrieve top filter values. Retrieves the 1,000 most frequent filter (facet) values for a filter attribute. |
| List Top Filters Without Results | `listTopFiltersWithoutResults` | Retrieve top filters for a search without results. Retrieves the 1,000 most frequently used filters for a search that didn't return any results. |
| List Top Hits | `listTopHits` | Retrieve top search results. Retrieves the object IDs of the 1,000 most frequent search results. |
| List Top Searches | `listTopSearches` | Retrieve top searches. Returns the most popular searches. |
| List User IDs | `listUserIds` | List user IDs. Lists the userIDs assigned to a multi-cluster application. |
| Partially Update Record | `partialUpdateObject` | Add or update attributes. Adds new attributes to a record, or updates existing ones. The record body is schemaless: pass each record attribute as a top-level input alongside the declared fields and it is sent verbatim in the request body. |
| Replace Allowed Sources | `replaceSources` | Replace allowed sources. Replaces the list of allowed sources. |
| Restore API Key | `restoreApiKey` | Restore an API key. Restores a deleted API key. |
| Save Rule | `saveRule` | Create or replace a rule. If a rule with the specified object ID doesn't exist, it's created. |
| Save Rules | `saveRules` | Create or update rules. Create or update multiple rules. |
| Save Synonym | `saveSynonym` | Create or replace a synonym. If a synonym with the specified object ID doesn't exist, Algolia adds a new one. |
| Save Synonyms | `saveSynonyms` | Create or replace synonyms. If a synonym with the objectID doesn't exist, Algolia adds a new one. |
| Search Dictionary Entries | `searchDictionaryEntries` | Search dictionary entries. Searches for standard and custom dictionary entries. |
| Search Facet Values | `searchForFacetValues` | Search for facet values. Searches for values of a specified facet attribute. |
| Search Index | `searchSingleIndex` | Search an index. Searches a single index and returns matching search results as hits. |
| Search Multiple Indices | `searchMultipleIndices` | Search multiple queries. Runs multiple search queries against one or more indices in a single API request. |
| Search Rules | `searchRules` | Search for rules. Searches for rules in your index. |
| Search Synonyms | `searchSynonyms` | Search for synonyms. Searches for synonyms in your index. |
| Search User IDs | `searchUserIds` | Search for user IDs. Since it can take a few seconds to get the data from the different clusters, the response isn't real-time. |
| Send Events | `pushEvents` | Send events. Sends a list of events to the Insights API. |
| Test Cluster Reachability | `testClusterReachability` | Test the reachability of clusters. Test whether clusters are reachable or not. |
| Update API Key | `updateApiKey` | Update an API key. Replaces the permissions of an existing API key. |
| Update Dictionary Settings | `setDictionarySettings` | Update dictionary settings. Turns standard stop word dictionary entries on or off for a given language. |
| Update Index Settings | `setSettings` | Update index settings. Update the specified index settings. |
