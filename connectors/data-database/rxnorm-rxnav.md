---
description: "RxNorm (via the NLM RxNav REST API) is the US National Library of Medicine's normalized naming system for clinical drugs."
hidden: true
---

# RxNorm (RxNav)

<img src="../../.gitbook/assets/connectors/lg/rxnorm-rxnav.png" alt="RxNorm (RxNav) logo">

RxNorm (via the NLM RxNav REST API) is the US National Library of Medicine's normalized naming system for clinical drugs. Find drug concepts (RXCUI) by name, NDC or other ids, approximate match and spelling suggestions, get drug products, brands, generics, related concepts, properties, NDCs and their status and history, plus reference lists of term types, relationships and sources. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [nlm.nih.gov](https://nlm.nih.gov) |
| **Authentication** | No authentication |
| **Slug** | `rxnormRxnav` |

## Use it

Add RxNorm (RxNav) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rxnormRxnav.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Filter Concept by Property | `filterByProperty` | Return the RXCUI only if the concept has the given property value, e.g. TTY in IN PIN (GET /rxcui/{rxcui}/filter.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.filterByProperty.html |
| Find Active Products | `findActiveProducts` | Find the active product concept(s) for an archived or inactive product RXCUI (GET /rxcui/{rxcui}/active.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.findActiveProducts.html |
| Find Related NDCs | `findRelatedNDCs` | Find NDCs related to an NDC by concept, product or drug (GET /relatedndc.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.findRelatedNDCs.html |
| Find RXCUI by Identifier | `findRxcuiById` | Find RxNorm concepts by an identifier of another type, e.g. an NDC, ATC or MeSH id (GET /rxcui.json?idtype=&id=). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.findRxcuiById.html |
| Find RXCUI by Name | `findRxcuiByString` | Find RxNorm concepts by exact or normalized name (GET /rxcui.json?name=). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.findRxcuiByString.html |
| Get All Historical NDCs | `getAllHistoricalNDCs` | Get the NDCs ever associated with a drug product, with date ranges (GET /rxcui/{rxcui}/allhistoricalndcs.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getAllHistoricalNDCs.html |
| Get All Properties | `getAllProperties` | Get properties of a concept by category: names, codes, attributes, sources (GET /rxcui/{rxcui}/allProperties.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getAllProperties.html |
| Get All Related Concepts | `getAllRelatedInfo` | Get all concepts directly or indirectly related to a concept, grouped by term type (GET /rxcui/{rxcui}/allrelated.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getAllRelatedInfo.html |
| Get Approximate Match | `getApproximateMatch` | Find concepts that approximately match a free-text drug string, ranked by score (GET /approximateTerm.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getApproximateMatch.html |
| Get Brands by Ingredients | `getMultiIngredBrand` | Get brand names that contain all the given ingredients (GET /brands.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getMultiIngredBrand.html |

<details>

<summary>See 23 more actions</summary>

* **Get Concept History Status** `getRxcuiHistoryStatus`: Get the status (active, remapped, obsolete...) and history of a concept, including remapping and attributes (GET /rxcui/{rxcui}/historystatus.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRxcuiHistoryStatus.html
* **Get Concept Name** `getRxNormName`: Get the RxNorm name of a concept (GET /rxcui/{rxcui}.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRxNormName.html
* **Get Concept Properties** `getRxConceptProperties`: Get the basic properties of a concept: name, synonym, term type, language, suppress flag (GET /rxcui/{rxcui}/properties.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRxConceptProperties.html
* **Get Concept Property** `getRxProperty`: Get the value(s) of one property of a concept, e.g. ATC code (GET /rxcui/{rxcui}/property.json?propName=). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRxProperty.html
* **Get Display Terms** `getDisplayTerms`: Get the list of names for auto-completion, about 0.75 MB (GET /displaynames.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getDisplayTerms.html
* **Get Drugs** `getDrugs`: Get the drug products (SBD, SCD, packs) for an ingredient, brand or dose form name, grouped by term type (GET /drugs.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getDrugs.html
* **Get Generic Product** `getGenericProduct`: Get the generic (clinical) product of a branded product (GET /rxcui/{rxcui}/generic.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getGenericProduct.html
* **Get NDC Properties** `getNDCProperties`: Get properties of NDCs (packaging, labeler, SPL set id, marketing dates) by NDC, RXCUI or SPL set id (GET /ndcproperties.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getNDCProperties.html
* **Get NDC Status** `getNDCStatus`: Get the status and history of an NDC: active, obsolete, alien or unknown, with its concept (GET /ndcstatus.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getNDCStatus.html
* **Get NDCs** `getNDCs`: Get the active NDCs of a drug product (GET /rxcui/{rxcui}/ndcs.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getNDCs.html
* **Get Related by Relationship** `getRelatedByRelationship`: Get concepts related to a concept by relationship name(s) (GET /rxcui/{rxcui}/related.json?rela=). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRelatedByRelationship.html
* **Get Related by Term Type** `getRelatedByType`: Get concepts related to a concept, limited to term type(s) (GET /rxcui/{rxcui}/related.json?tty=). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRelatedByType.html
* **Get RxNorm Version** `getRxNormVersion`: Get the current RxNorm data version and API version (GET /version.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRxNormVersion.html
* **Get Spelling Suggestions** `getSpellingSuggestions`: Get spelling suggestions for a possibly misspelled drug name (GET /spellingsuggestions.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getSpellingSuggestions.html
* **List Concepts by Term Type** `getAllConceptsByTTY`: List all concepts of one or more term types, e.g. BN (brand names) (GET /allconcepts.json). Large term types return about 1 MB. Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getAllConceptsByTTY.html
* **List Identifier Types** `getIdTypes`: List the identifier types usable with Find RXCUI by Identifier (GET /idtypes.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getIdTypes.html
* **List Property Categories** `getPropCategories`: List the property categories used by Get All Properties (GET /propCategories.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getPropCategories.html
* **List Property Names** `getPropNames`: List the property names (GET /propnames.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getPropNames.html
* **List Reformulation Concepts** `getReformulationConcepts`: List the concepts that are reformulations of others (GET /reformulationConcepts.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getReformulationConcepts.html
* **List Relationship Paths** `getRelaPaths`: List the relationship paths between term types used by Get All Related Concepts (GET /relapaths.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRelaPaths.html
* **List Relationship Types** `getRelaTypes`: List RxNorm relationship names, e.g. tradename_of (GET /relatypes.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRelaTypes.html
* **List Source Vocabularies** `getSourceTypes`: List the source vocabularies in RxNorm (GET /sourcetypes.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getSourceTypes.html
* **List Term Types** `getTermTypes`: List the RxNorm term types (TTY), e.g. IN, BN, SCD, SBD (GET /termtypes.json). Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getTermTypes.html

</details>
