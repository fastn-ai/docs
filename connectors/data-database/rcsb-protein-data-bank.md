---
description: "The RCSB Protein Data Bank (PDB) offers free APIs for 3D structures of proteins, nucleic acids and complexes."
hidden: true
---

# RCSB Protein Data Bank

<img src="../../.gitbook/assets/connectors/lg/rcsb-protein-data-bank.png" alt="RCSB Protein Data Bank logo">

The RCSB Protein Data Bank (PDB) offers free APIs for 3D structures of proteins, nucleic acids and complexes. Get entries, assemblies, entities, chains, interfaces, ligands (chemical components), DrugBank, PubMed and UniProt annotations, groups, repository holdings and data schemas; run GraphQL queries and search structures by text, attributes, sequence or chemistry. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [rcsb.org](https://rcsb.org) |
| **Authentication** | No authentication |
| **Slug** | `rcsbProteinDataBank` |

## Use it

Add RCSB Protein Data Bank from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rcsbProteinDataBank.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Execute GraphQL Query | `executeGraphQLQuery` | Run a GraphQL query against the RCSB PDB Data API to fetch exactly the fields you need for entries, entities, instances, assemblies, chemical components and more (POST /graphql). Docs: https://data.rcsb.org/redoc/index.html and https://data.rcsb.org/graphql/index.html |
| Get Assembly | `getAssembly` | Get structural assembly description by ENTRY ID and ASSEMBLY ID. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/assembly/{entry_id}/{assembly_id}) |
| Get Assembly Schema | `getAssemblySchema` | Get assembly schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/assembly) |
| Get Branched Entity | `getBranchedEntity` | Get branched entity description by ENTRY ID and ENTITY ID. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/branched_entity/{entry_id}/{entity_id}) |
| Get Branched Entity Instance | `getBranchedEntityInstance` | Get branched entity instance description by ENTRY ID and ASYM ID. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/branched_entity_instance/{entry_id}/{asym_id}) |
| Get Branched Entity Instance Schema | `getBranchedEntityInstanceSchema` | Get branched instance schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/branched_entity_instance) |
| Get Branched Entity Schema | `getBranchedEntitySchema` | Get branched entity schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/branched_entity) |
| Get Chem Comp Schema | `getChemCompSchema` | Get chemical component/BIRD schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/chem_comp) |
| Get Chemical Component | `getChemicalComponent` | Get chemical component (ligands, small molecules and monomers) by CCD ID. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/chemcomp/{comp_id}) |
| Get DrugBank Annotations | `getDrugBankAnnotations` | Get DrugBank annotations (integrated from DrugBank resource) for a given chemical component (identified by CHEM COMP ID) . Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/drugbank/{comp_id}) |
| Get Drugbank Schema | `getDrugbankSchema` | Get DrugBank (integrated data) schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/drugbank) |
| Get Entries Status | `getEntriesStatus` | Get the status and status code of a list of entry IDs. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/holdings/status) |
| Get Entry | `getEntry` | Get structure by ENTRY ID. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/entry/{entry_id}) |
| Get Entry Group | `getEntryGroup` | Get a group object that aggregates all entries associated with the specified PDB Group Deposition ID. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/entry_groups/{group_id}) |
| Get Entry Schema | `getEntrySchema` | Get entry schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/entry) |
| Get Entry Status | `getEntryStatus` | Get the status and status code of a structure. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/holdings/status/{entry_id}) |
| Get Group Provenance | `getGroupProvenance` | Describes aggregation method used to create groups. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/group_provenance/{group_provenance_id}) |
| Get Non-Polymer Entity | `getNonPolymerEntity` | Get non-polymer entity data by ENTRY ID and ENTITY ID. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/nonpolymer_entity/{entry_id}/{entity_id}) |
| Get Non-Polymer Entity Instance | `getNonPolymerEntityInstance` | Get non-polymer entity instance description by ENTRY ID and ASYM ID (label_asym_id). Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/nonpolymer_entity_instance/{entry_id}/{asym_id}) |
| Get Nonpolymer Entity Instance Schema | `getNonpolymerEntityInstanceSchema` | Get non-polymer instance schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/nonpolymer_entity_instance) |
| Get Nonpolymer Entity Schema | `getNonpolymerEntitySchema` | Get non-polymer entity schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/nonpolymer_entity) |
| Get Polymer Entity | `getPolymerEntity` | Get polymer entity data by ENTRY ID and ENTITY ID. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/polymer_entity/{entry_id}/{entity_id}) |
| Get Polymer Entity Group | `getPolymerEntityGroup` | Get a group object that aggregates all polymer entities associated with the specified UniProt ID or sequence cluster ID. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/polymer_entity_groups/{group_id}) |
| Get Polymer Entity Instance (Chain) | `getPolymerEntityInstance` | Get polymer entity instance (a.k.a chain) data by ENTRY ID and ASYM ID (label_asym_id). Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/polymer_entity_instance/{entry_id}/{asym_id}) |
| Get Polymer Entity Instance Schema | `getPolymerEntityInstanceSchema` | Get polymer instance schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/polymer_entity_instance) |
| Get Polymer Entity Schema | `getPolymerEntitySchema` | Get polymer entity schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/polymer_entity) |
| Get Polymeric Interface | `getInterface` | Get pairwise polymeric interface description by ENTRY ID, ASSEMBLY ID and INTERFACE ID. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/interface/{entry_id}/{assembly_id}/{interface_id}) |
| Get PubMed Annotations | `getPubMedAnnotations` | Get PubMed annotations (data integrated from PubMed) for a given entry's primary citation. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/pubmed/{entry_id}) |
| Get Pubmed Schema | `getPubmedSchema` | Get PubMed (integrated data) schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/pubmed) |
| Get Removed Entry | `getRemovedEntry` | Get the description of the structure that was removed from the PDB repository. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/holdings/removed/{entry_id}) |
| Get UniProt Annotations | `getUniProtAnnotations` | Get UniProt annotations for a given macromolecular entity (identified by ENTRY ID and ENTITY ID). Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/core/uniprot/{entry_id}/{entity_id}) |
| Get Uniprot Schema | `getUniprotSchema` | Get UniProt (integrated data) schema. Returns the JSON schema. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/schema/uniprot) |
| Get Unreleased Entries | `getUnreleasedEntries` | Get a list of unreleased structures with descriptions. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/holdings/unreleased) |
| Get Unreleased Entry | `getUnreleasedEntry` | Get the description of unreleased structure that is being processed or on hold waiting for release. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/holdings/unreleased/{entry_id}) |
| List Current BIRD (PRD) IDs | `listCurrentPrdIds` | Get the list of current PRD IDs for BIRD entries. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/holdings/current/prd_ids) |
| List Current Chemical Component IDs | `listCurrentCcdIds` | Get the list of current CCD IDs. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/holdings/current/ccd_ids) |
| List Current Entry IDs | `listCurrentEntryIds` | Get the list of current entry IDs. About 1.8 MB. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/holdings/current/entry_ids) |
| List Removed Entry IDs | `listRemovedEntryIds` | Get the list of removed entry IDs. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/holdings/removed/entry_ids) |
| List Unreleased Entry IDs | `listUnreleasedEntryIds` | Get the list of unreleased entry IDs. Docs: https://data.rcsb.org/redoc/index.html (GET /rest/v1/holdings/unreleased/entry_ids) |
| Search Structures | `searchStructures` | Search the PDB with the RCSB Search API: full text, attribute, sequence, structure, sequence motif, chemical and grouped queries, with paging, sorting and facets (POST /rcsbsearch/v2/query). Returns matching identifiers and scores. Docs: https://search.rcsb.org/ |
