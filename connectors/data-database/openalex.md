---
description: "OpenAlex is the open catalog of the global research system."
hidden: true
---

# OpenAlex

<img src="../../.gitbook/assets/connectors/openalex.png" alt="OpenAlex logo" width="64">

OpenAlex is the open catalog of the global research system. This connector covers the OpenAlex REST API: works, authors, sources, institutions, publishers, funders, awards, topics and the rest of the subject hierarchy, keywords, SDGs, concepts, locations and every vocabulary endpoint, each with filtering, search, sorting, grouping, sampling and paging; plus autocomplete, OQL query execution and translation, the properties registry, usage and rate-limit status, full-text content downloads, private collections and author curations.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [openalex.org](https://openalex.org) |
| **Authentication** | Bearer token |
| **Slug** | `openalex` |

## Use it

Add OpenAlex from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openalex.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Collection Entities | `addCollectionEntities` | Bulk-adds entity IDs to one of the connected user's collections. IDs must match the collection's entity type; the cap is 1,000 entities. Requires an API key. |
| Admin Delete Collection | `adminDeleteCollection` | Hard-deletes any user's collection with cascade. OpenAlex admins only; other callers receive 403 "Admin only". |
| Admin Get Collection | `adminGetCollection` | Reads any user's collection by ID. OpenAlex admins only; other callers receive 403 "Admin only". |
| Admin List Collections | `adminListCollections` | Searches collections across all users. OpenAlex admins only; other callers receive 403 "Admin only". |
| Admin Update Collection | `adminUpdateCollection` | Updates any user's collection name, description or entity type. OpenAlex admins only; other callers receive 403 "Admin only". |
| Autocomplete | `autocomplete` | Returns fast type-ahead suggestions across all OpenAlex entity types for a partial name or an ID such as an ORCID, DOI or ROR. Autocomplete requests are free. |
| Autocomplete Entity | `autocompleteEntity` | Returns fast type-ahead suggestions for one OpenAlex entity type, optionally narrowed with filters or a search. Autocomplete requests are free. |
| Create Collection | `createCollection` | Creates a private named collection of OpenAlex entities of one type, optionally seeded with entity IDs. The returned col_ ID can be used in the collection: filter on list actions. Requires an API key. |
| Create Curation | `createCuration` | Submits one author curation: claim a work authorship, remove yourself from a work, or set/detach display_name, full_name or ORCID on an author profile. Only claimed-profile owners, organization curators or site curators may submit; others receive 403. Changes apply within about 24 hours. |
| Delete Collection | `deleteCollection` | Deletes one of the connected user's collections and all of its entity memberships. Requires an API key. |

<details>

<summary>See 77 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Download Work Grobid XML | `downloadWorkGrobidXml` | Downloads the Grobid TEI XML full text of a work from the OpenAlex content archive as a gzip file reference (name ending .xml.gz, base64 data). Only works with has_content.grobid_xml true are available; costs $0.01 per download. |
| Download Work PDF | `downloadWorkPdf` | Downloads the cached full-text PDF of a work from the OpenAlex content archive. Only works with has_content.pdf true are available; costs $0.01 per download. Returns a file reference with base64 data. |
| Get Author | `getAuthor` | Returns a single OpenAlex author by OpenAlex ID or ORCID. Single-entity lookups are free. |
| Get Award | `getAward` | Returns a single OpenAlex award (grant) by ID. Single-entity lookups are free. |
| Get Collection | `getCollection` | Returns the metadata of one collection by its col_ ID. Requires an API key; 403 for collections owned by another user. |
| Get Concept | `getConcept` | Returns a single OpenAlex legacy concept by ID, including ancestors and related concepts. Concepts are deprecated in favour of topics. Single-entity lookups are free. |
| Get Continent | `getContinent` | Returns a single OpenAlex continent by its Wikidata ID, with its countries and counts. Single-entity lookups are free. |
| Get Country | `getCountry` | Returns a single OpenAlex country by its ISO 3166-1 alpha-2 code, with continent and counts. Single-entity lookups are free. |
| Get Domain | `getDomain` | Returns a single OpenAlex top-level domain by ID, including its fields. Single-entity lookups are free. |
| Get Entity Properties | `getEntityProperties` | Returns the queryable column registry for one OpenAlex entity type, with operators, types and OQL names. Costs one list credit. |
| Get Field | `getField` | Returns a single OpenAlex field by ID, including its domain and subfields. Single-entity lookups are free. |
| Get Funder | `getFunder` | Returns a single OpenAlex funder by ID. Single-entity lookups are free. |
| Get Index | `getIndex` | Returns a single external index tracked by OpenAlex, such as crossref or pubmed, with its description and counts. Single-entity lookups are free. |
| Get Institution | `getInstitution` | Returns a single OpenAlex institution by OpenAlex ID or ROR ID. Single-entity lookups are free. |
| Get Institution Type | `getInstitutionType` | Returns a single OpenAlex institution type by ID with its description and counts. Single-entity lookups are free. |
| Get Keyword | `getKeyword` | Returns a single OpenAlex keyword by ID. Single-entity lookups are free. |
| Get Language | `getLanguage` | Returns a single OpenAlex language by its ISO 639-1 code, with counts. Single-entity lookups are free. |
| Get License | `getLicense` | Returns a single OpenAlex license by ID with its URL, description and counts. Single-entity lookups are free. |
| Get Location | `getLocation` | Returns a single raw OpenAlex work location by its namespaced native ID, such as a DOI location. Single-entity lookups are free. |
| Get Open Access Status | `getOpenAccessStatus` | Returns a single OpenAlex open access status, such as gold or green, with its description and counts. Single-entity lookups are free. |
| Get Parse Context | `getParseContext` | Returns what the OQL grammar expects at a cursor position in a partial query, with suggestions, for building autocomplete editors. Free. |
| Get Properties | `getProperties` | Returns the registry of every queryable OpenAlex entity and column, with operators, types and OQL names, for all 24 entities. Costs one list credit. |
| Get Publisher | `getPublisher` | Returns a single OpenAlex publisher by ID. Single-entity lookups are free. |
| Get Query Spec Artifact | `getQuerySpecArtifact` | Returns one OQL specification artifact by slug: Markdown text for cheatsheet, guide, api, oql and grammar, or JSON for the oqo schema. Free. |
| Get Random Entity | `getRandomEntity` | Returns one randomly chosen OpenAlex entity of the given type. This route is live but not listed in the OpenAlex endpoint index; for reproducible random sets use the Sample and Seed inputs on the list actions instead. |
| Get Rate Limit | `getRateLimit` | Returns the daily budget, usage, remaining credits, reset time and per-endpoint costs for the connected OpenAlex API key. Requires an API key. |
| Get SDG | `getSdg` | Returns a single UN Sustainable Development Goal entity from OpenAlex by ID. Single-entity lookups are free. |
| Get Source | `getSource` | Returns a single OpenAlex source by OpenAlex ID or ISSN. Single-entity lookups are free. |
| Get Source Type | `getSourceType` | Returns a single OpenAlex source type by ID with its description and counts. Single-entity lookups are free. |
| Get Subfield | `getSubfield` | Returns a single OpenAlex subfield by ID, including its field, domain and topics. Single-entity lookups are free. |
| Get Topic | `getTopic` | Returns a single OpenAlex topic by ID, including its keywords and its place in the domain, field and subfield hierarchy. Single-entity lookups are free. |
| Get Work | `getWork` | Returns a single OpenAlex work by OpenAlex ID or external ID such as a DOI or PMID. Single-entity lookups are free. |
| Get Work Type | `getWorkType` | Returns a single OpenAlex work type by ID with its description and counts. Single-entity lookups are free. |
| List Authors | `listAuthors` | Lists OpenAlex disambiguated author profiles, with filtering, full-text search, sorting, grouping, random sampling, field selection and page or cursor paging. List requests cost $0.0001 each and searches $0.001. |
| List Awards | `listAwards` | Lists OpenAlex grants and awards with their funder, amount, dates, investigators and funded outputs, with filtering, full-text search, sorting, grouping, random sampling, field selection and page or cursor paging. List requests cost $0.0001 each and searches $0.001. |
| List Collection Entities | `listCollectionEntities` | Returns a collection's metadata plus a page of its member entity IDs. Requires an API key. |
| List Concepts | `listConcepts` | Lists OpenAlex legacy concepts with their level and counts. Concepts are deprecated by OpenAlex in favour of topics but still served. Supports filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Continents | `listContinents` | Lists the seven OpenAlex continents with their countries and counts, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Countries | `listCountries` | Lists OpenAlex countries with their continent, Global South flag and counts, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Curations | `listCurations` | Lists author curations (claim work, remove from work, display_name, full_name, ORCID corrections) submitted by the connected OpenAlex user. Requires an API key. |
| List Domains | `listDomains` | Lists the four top-level OpenAlex subject domains with their fields, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Fields | `listFields` | Lists the 26 broad OpenAlex academic fields with their domain and subfields, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Funders | `listFunders` | Lists OpenAlex research funders, with filtering, full-text search, sorting, grouping, random sampling, field selection and page or cursor paging. List requests cost $0.0001 each and searches $0.001. |
| List Indexes | `listIndexes` | Lists the external indexes OpenAlex tracks works as indexed in, such as Crossref, PubMed, DataCite, DOAJ and arXiv, with their counts, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Institution Types | `listInstitutionTypes` | Lists the OpenAlex institution type vocabulary, such as education, company and government, with their counts, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Institutions | `listInstitutions` | Lists OpenAlex universities, companies and other research institutions, with filtering, full-text search, sorting, grouping, random sampling, field selection and page or cursor paging. List requests cost $0.0001 each and searches $0.001. |
| List Keywords | `listKeywords` | Lists OpenAlex keywords, short phrases derived from topics and assigned to works, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Languages | `listLanguages` | Lists the languages OpenAlex assigns to works, with their counts, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Licenses | `listLicenses` | Lists the content licenses OpenAlex recognizes on works, such as CC-BY, with their URL and counts, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Locations | `listLocations` | Lists raw OpenAlex work locations, the individual records from Crossref, repositories and other providers that are merged into works, with filtering, search, sorting, grouping, sampling, field selection and paging. List requests cost $0.0001 each. |
| List My Collections | `listMyCollections` | Lists the private saved collections owned by the connected OpenAlex user, optionally only those containing a given entity. Requires an API key. |
| List Open Access Statuses | `listOaStatuses` | Lists the OpenAlex open access status vocabulary (gold, green, hybrid, bronze, diamond, closed) with descriptions and counts, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Publishers | `listPublishers` | Lists OpenAlex publishing organizations, with filtering, full-text search, sorting, grouping, random sampling, field selection and page or cursor paging. List requests cost $0.0001 each and searches $0.001. |
| List Query Spec Artifacts | `listQuerySpecArtifacts` | Returns the index of OQL specification artifacts (cheat sheet, guide, API reference, spec, OQO JSON schema, grammar) with their slugs and URLs. Free. |
| List SDGs | `listSdgs` | Lists the 17 UN Sustainable Development Goals as OpenAlex entities with their work and citation counts, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Source Types | `listSourceTypes` | Lists the OpenAlex source type vocabulary, such as journal, repository and conference, with their counts, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Sources | `listSources` | Lists OpenAlex journals, repositories, conferences and other sources, with filtering, full-text search, sorting, grouping, random sampling, field selection and page or cursor paging. List requests cost $0.0001 each and searches $0.001. |
| List Subfields | `listSubfields` | Lists the 252 OpenAlex subfields with their field, domain and topics, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Topics | `listTopics` | Lists the roughly 4,500 fine-grained OpenAlex research topics with their subfield, field and domain, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Work Types | `listWorkTypes` | Lists the OpenAlex work type vocabulary, such as article, book and dataset, with their descriptions and counts, with filtering, search, sorting, grouping, sampling, field selection and paging. |
| List Works | `listWorks` | Lists OpenAlex scholarly works such as articles, books, datasets and theses, with filtering, full-text, exact or semantic search, sorting, grouping, random sampling, field selection, corpus choice and page or cursor paging. List requests cost $0.0001 each and searches $0.001. |
| Remove Collection Entities | `removeCollectionEntities` | Bulk-removes entity IDs from one of the connected user's collections. Requires an API key. |
| Remove Collection Entity | `removeCollectionEntity` | Removes a single entity from one of the connected user's collections by ID in the URL. Requires an API key. |
| Run OQL Query | `runOqlQuery` | Executes an OpenAlex Query Language (OQL) query at the API root, for example "works where year is (2020) group by type", and returns the standard entity list or group envelope. The query names its own entity. Costs the same as the equivalent classic list call. |
| Run OQO Query | `runOqoQuery` | Executes an OpenAlex Query Object (OQO), the JSON form of an OQL query, at the API root via GET and returns the standard entity list or group envelope. Costs the same as the equivalent classic list call. |
| Run Query (POST) | `runQueryPost` | Executes an OQL or OQO query via POST to the API root, with no request-line length limit. Send exactly one of OQL or OQO; sort, select, page, per_page and cursor ride as sibling keys. Returns the standard entity list or group envelope. |
| Tag Text | `tagText` | Tags a title and optional abstract with OpenAlex keywords and concepts in one GET request. Deprecated by OpenAlex and not recommended for new projects; costs $0.01 per request and is limited to 1 request per second. |
| Tag Text (POST) | `tagTextPost` | Tags a title and optional abstract with OpenAlex keywords and concepts in one POST request, for text too long for a URL. Deprecated by OpenAlex and not recommended for new projects; costs $0.01 per request and is limited to 1 request per second. |
| Tag Text Concepts | `tagTextConcepts` | Tags a title and optional abstract with OpenAlex concepts via GET. Deprecated by OpenAlex and not recommended for new projects; costs $0.01 per request and is limited to 1 request per second. |
| Tag Text Concepts (POST) | `tagTextConceptsPost` | Tags a title and optional abstract with OpenAlex concepts via POST, for text too long for a URL. Deprecated by OpenAlex and not recommended for new projects; costs $0.01 per request and is limited to 1 request per second. |
| Tag Text Keywords | `tagTextKeywords` | Tags a title and optional abstract with OpenAlex keywords via GET. Deprecated by OpenAlex and not recommended for new projects; costs $0.01 per request and is limited to 1 request per second. |
| Tag Text Keywords (POST) | `tagTextKeywordsPost` | Tags a title and optional abstract with OpenAlex keywords via POST, for text too long for a URL. Deprecated by OpenAlex and not recommended for new projects; costs $0.01 per request and is limited to 1 request per second. |
| Translate OQL | `translateOql` | Translates an OQL query into its OQO, classic URL and canonical OQL forms and validates it, without executing it. Free. |
| Translate OQO | `translateOqo` | Translates an OQO JSON query object into its OQL, classic URL and canonical OQO forms and validates it, without executing it. Free. |
| Translate Query (POST) | `translateQuery` | Translates a query given as OQL, OQO or a classic OpenAlex URL (oxurl) into all three forms and validates it, without executing it. Use this for the classic-URL form and for long queries. Send exactly one of the three. Free. |
| Update Collection | `updateCollection` | Updates the name, description or (only while empty) the entity type of one of the connected user's collections. Requires an API key. |
| Validate OQL | `validateOql` | Lints an OQL string and returns rich diagnostics with stable error codes, spans and fix-its. Always returns 200; check the valid flag. Free. |

</details>
