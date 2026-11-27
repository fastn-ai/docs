---
description: "RxNorm is the US National Library of Medicine's naming system for clinical drugs. Find drug concepts by name or ID and look up related NDCs."
hidden: true
---

# RxNorm (RxNav)

<img src="../../.gitbook/assets/connectors/lg/rxnorm-rxnav.png" alt="RxNorm (RxNav) logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [nlm.nih.gov](https://nlm.nih.gov) |
| **Authentication** | No sign-in needed |
| **Slug** | `rxnormRxnav` |

## Setup

RxNorm (RxNav) needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect RxNorm (RxNav) from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **RxNorm (RxNav)**.
2. Select **Connect** on the RxNorm (RxNav) card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. RxNorm (RxNav) needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use RxNorm (RxNav)'s actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Filter Concept by Property</td><td><code>filterByProperty</code></td><td>Return the RXCUI only if the concept has the given property value, e.g. TTY in IN PIN Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.filterByProperty.html</td></tr><tr><td>Find Active Products</td><td><code>findActiveProducts</code></td><td>Find the active product concept(s) for an archived or inactive product RXCUI Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.findActiveProducts.html</td></tr><tr><td>Find Related NDCs</td><td><code>findRelatedNDCs</code></td><td>Find NDCs related to an NDC by concept, product or drug Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.findRelatedNDCs.html</td></tr><tr><td>Find RXCUI by Identifier</td><td><code>findRxcuiById</code></td><td>Find RxNorm concepts by an identifier of another type, e.g. an NDC, ATC or MeSH id Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.findRxcuiById.html</td></tr><tr><td>Find RXCUI by Name</td><td><code>findRxcuiByString</code></td><td>Find RxNorm concepts by exact or normalized name Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.findRxcuiByString.html</td></tr><tr><td>Get All Historical NDCs</td><td><code>getAllHistoricalNDCs</code></td><td>Get the NDCs ever associated with a drug product, with date ranges Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getAllHistoricalNDCs.html</td></tr><tr><td>Get All Properties</td><td><code>getAllProperties</code></td><td>Get properties of a concept by category: names, codes, attributes, sources Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getAllProperties.html</td></tr><tr><td>Get All Related Concepts</td><td><code>getAllRelatedInfo</code></td><td>Get all concepts directly or indirectly related to a concept, grouped by term type Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getAllRelatedInfo.html</td></tr><tr><td>Get Approximate Match</td><td><code>getApproximateMatch</code></td><td>Find concepts that approximately match a free-text drug string, ranked by score Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getApproximateMatch.html</td></tr><tr><td>Get Brands by Ingredients</td><td><code>getMultiIngredBrand</code></td><td>Get brand names that contain all the given ingredients Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getMultiIngredBrand.html</td></tr></tbody></table>

<details>

<summary>View 23 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Concept History Status</td><td><code>getRxcuiHistoryStatus</code></td><td>Get the status (active, remapped, obsolete...) and history of a concept, including remapping and attributes Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRxcuiHistoryStatus.html</td></tr><tr><td>Get Concept Name</td><td><code>getRxNormName</code></td><td>Get the RxNorm name of a concept Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRxNormName.html</td></tr><tr><td>Get Concept Properties</td><td><code>getRxConceptProperties</code></td><td>Get the basic properties of a concept: name, synonym, term type, language, suppress flag Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRxConceptProperties.html</td></tr><tr><td>Get Concept Property</td><td><code>getRxProperty</code></td><td>Get the value(s) of one property of a concept, e.g. ATC code Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRxProperty.html</td></tr><tr><td>Get Display Terms</td><td><code>getDisplayTerms</code></td><td>Get the list of names for auto-completion, about 0.75 MB Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getDisplayTerms.html</td></tr><tr><td>Get Drugs</td><td><code>getDrugs</code></td><td>Get the drug products (SBD, SCD, packs) for an ingredient, brand or dose form name, grouped by term type Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getDrugs.html</td></tr><tr><td>Get Generic Product</td><td><code>getGenericProduct</code></td><td>Get the generic (clinical) product of a branded product Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getGenericProduct.html</td></tr><tr><td>Get NDC Properties</td><td><code>getNDCProperties</code></td><td>Get properties of NDCs (packaging, labeler, SPL set id, marketing dates) by NDC, RXCUI or SPL set id Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getNDCProperties.html</td></tr><tr><td>Get NDC Status</td><td><code>getNDCStatus</code></td><td>Get the status and history of an NDC: active, obsolete, alien or unknown, with its concept Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getNDCStatus.html</td></tr><tr><td>Get NDCs</td><td><code>getNDCs</code></td><td>Get the active NDCs of a drug product Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getNDCs.html</td></tr><tr><td>Get Related by Relationship</td><td><code>getRelatedByRelationship</code></td><td>Get concepts related to a concept by relationship name(s) Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRelatedByRelationship.html</td></tr><tr><td>Get Related by Term Type</td><td><code>getRelatedByType</code></td><td>Get concepts related to a concept, limited to term type(s) Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRelatedByType.html</td></tr><tr><td>Get RxNorm Version</td><td><code>getRxNormVersion</code></td><td>Get the current RxNorm data version and API version Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRxNormVersion.html</td></tr><tr><td>Get Spelling Suggestions</td><td><code>getSpellingSuggestions</code></td><td>Get spelling suggestions for a possibly misspelled drug name Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getSpellingSuggestions.html</td></tr><tr><td>List Concepts by Term Type</td><td><code>getAllConceptsByTTY</code></td><td>List all concepts of one or more term types, e.g. BN (brand names) Large term types return about 1 MB. Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getAllConceptsByTTY.html</td></tr><tr><td>List Identifier Types</td><td><code>getIdTypes</code></td><td>List the identifier types usable with Find RXCUI by Identifier Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getIdTypes.html</td></tr><tr><td>List Property Categories</td><td><code>getPropCategories</code></td><td>List the property categories used by Get All Properties Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getPropCategories.html</td></tr><tr><td>List Property Names</td><td><code>getPropNames</code></td><td>List the property names Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getPropNames.html</td></tr><tr><td>List Reformulation Concepts</td><td><code>getReformulationConcepts</code></td><td>List the concepts that are reformulations of others Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getReformulationConcepts.html</td></tr><tr><td>List Relationship Paths</td><td><code>getRelaPaths</code></td><td>List the relationship paths between term types used by Get All Related Concepts Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRelaPaths.html</td></tr><tr><td>List Relationship Types</td><td><code>getRelaTypes</code></td><td>List RxNorm relationship names, e.g. tradename_of Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getRelaTypes.html</td></tr><tr><td>List Source Vocabularies</td><td><code>getSourceTypes</code></td><td>List the source vocabularies in RxNorm Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getSourceTypes.html</td></tr><tr><td>List Term Types</td><td><code>getTermTypes</code></td><td>List the RxNorm term types (TTY), e.g. IN, BN, SCD, SBD Docs: https://lhncbc.nlm.nih.gov/RxNav/APIs/api-RxNorm.getTermTypes.html</td></tr></tbody></table>

</details>

