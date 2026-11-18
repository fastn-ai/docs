---
description: "Wikidata is the free, collaborative knowledge base of the Wikimedia projects."
hidden: true
---

# Wikidata

Wikidata is the free, collaborative knowledge base of the Wikimedia projects. Its Wikibase REST API reads items, properties and lexemes with their labels, descriptions, aliases, sitelinks and statements (with language fallback), searches and suggests items and properties, and lists property data types. Read access needs no API key; Wikimedia asks for a descriptive User-Agent.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [wikidata.org](https://wikidata.org) |
| **Authentication** | No authentication |
| **Actions** | 32 |
| **Events** | 0 |
| **Slug** | `wikidata` |

## Use it

Add Wikidata from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wikidata.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Item | `getItem` | Retrieve a single Wikibase Item by ID. (GET /wikibase/v1/entities/items/{item_id}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Item Aliases | `getItemAliases` | Retrieve an Item's aliases. (GET /wikibase/v1/entities/items/{item_id}/aliases). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Item Aliases In Language | `getItemAliasesInLanguage` | Retrieve an Item's aliases in a specific language. (GET /wikibase/v1/entities/items/{item_id}/aliases/{language_code}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Item Description | `getItemDescription` | Retrieve an Item's description in a specific language. (GET /wikibase/v1/entities/items/{item_id}/descriptions/{language_code}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Item Description With Fallback | `getItemDescriptionWithFallback` | Retrieve an Item's description in a specific language, with language fallback. If a description is defined in the requested language, the API responds with a 200 status code and includes the description in the response payload. If a description only exists in a fallback language, the API returns a 307 status code and provides the location of the description. (GET /wikibase/v1/entities/items/{item_id}/descriptions_with_language_fallback/{language_code}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Item Descriptions | `getItemDescriptions` | Retrieve an Item's descriptions. (GET /wikibase/v1/entities/items/{item_id}/descriptions). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Item Label | `getItemLabel` | Retrieve an Item's label in a specific language. (GET /wikibase/v1/entities/items/{item_id}/labels/{language_code}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Item Label With Fallback | `getItemLabelWithFallback` | Retrieve an Item's label in a specific language, with language fallback. If a label is defined in the requested language, the API responds with a 200 status code and includes the label in the response payload. If a label only exists in a fallback language, the API returns a 307 status code and provides the location of the label. (GET /wikibase/v1/entities/items/{item_id}/labels_with_language_fallback/{language_code}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Item Labels | `getItemLabels` | Retrieve an Item's labels. (GET /wikibase/v1/entities/items/{item_id}/labels). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Item Statement | `getItemStatement` | Retrieve a single Statement from an Item. This endpoint is also accessible through `/statements/{statement_id}` (GET /wikibase/v1/entities/items/{item_id}/statements/{statement_id}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Item Statements | `getItemStatements` | Retrieve Statements from an Item. (GET /wikibase/v1/entities/items/{item_id}/statements). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Lexeme | `getLexeme` | Retrieve a single Lexeme by ID. (GET /wikibaselexeme/v0/entities/lexemes/{lexeme_id}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get OpenAPI Document | `getOpenApiDoc` | Retrieve the OpenAPI document. (GET /wikibase/v1/openapi.json). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property | `getProperty` | Retrieve a single Wikibase Property by ID. (GET /wikibase/v1/entities/properties/{property_id}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property Aliases | `getPropertyAliases` | Retrieve a Property's aliases. (GET /wikibase/v1/entities/properties/{property_id}/aliases). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property Aliases In Language | `getPropertyAliasesInLanguage` | Retrieve a Property's aliases in a specific language. (GET /wikibase/v1/entities/properties/{property_id}/aliases/{language_code}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property Data Types | `getPropertyDataTypes` | Retrieve the map of Property data types to value types. (GET /wikibase/v1/property-data-types). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property Description | `getPropertyDescription` | Retrieve a Property's description in a specific language. (GET /wikibase/v1/entities/properties/{property_id}/descriptions/{language_code}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property Description With Fallback | `getPropertyDescriptionWithFallback` | Retrieve a Property's description in a specific language, with language fallback. If a description is defined in the requested language, the API responds with a 200 status code and includes the description in the response payload. If a description only exists in a fallback language, the API returns a 307 status code and provides the location of the description. (GET /wikibase/v1/entities/properties/{property_id}/descriptions_with_language_fallback/{language_code}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property Descriptions | `getPropertyDescriptions` | Retrieve a Property's descriptions. (GET /wikibase/v1/entities/properties/{property_id}/descriptions). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property Label | `getPropertyLabel` | Retrieve a Property's label in a specific language. (GET /wikibase/v1/entities/properties/{property_id}/labels/{language_code}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property Label With Fallback | `getPropertyLabelWithFallback` | Retrieve a Property's label in a specific language, with language fallback. If a label is defined in the requested language, the API responds with a 200 status code and includes the label in the response payload. If a label only exists in a fallback language, the API returns a 307 status code and provides the location of the label. (GET /wikibase/v1/entities/properties/{property_id}/labels_with_language_fallback/{language_code}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property Labels | `getPropertyLabels` | Retrieve a Property's labels. (GET /wikibase/v1/entities/properties/{property_id}/labels). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property Statement | `getPropertyStatement` | Retrieve a single Statement from a Property. This endpoint is also accessible through `/statements/{statement_id}` (GET /wikibase/v1/entities/properties/{property_id}/statements/{statement_id}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Property Statements | `getPropertyStatements` | Retrieve Statements from a Property. (GET /wikibase/v1/entities/properties/{property_id}/statements). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Sitelink | `getSitelink` | Retrieve an Item's Sitelink. (GET /wikibase/v1/entities/items/{item_id}/sitelinks/{site_id}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Sitelinks | `getSitelinks` | Retrieve an Item's Sitelinks. (GET /wikibase/v1/entities/items/{item_id}/sitelinks). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Get Statement | `getStatement` | Retrieve a single Statement. This endpoint is also accessible through `/entities/items/{item_id}/statements/{statement_id}` and `/entities/properties/{property_id}/statements/{statement_id}` (GET /wikibase/v1/statements/{statement_id}). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Simple Item Search | `simpleItemSearch` | Simple Item search by label and aliases. (GET /wikibase/v1/search/items). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Simple Property Search | `simplePropertySearch` | Simple Property search by label and aliases. (GET /wikibase/v1/search/properties). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Suggest Items | `suggestItems` | Simple Item search by prefix, for labels and aliases. (GET /wikibase/v1/suggest/items). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
| Suggest Properties | `suggestProperties` | Simple Property search by prefix, for labels and aliases. (GET /wikibase/v1/suggest/properties). Docs: https://www.wikidata.org/wiki/Wikidata:REST_API |
