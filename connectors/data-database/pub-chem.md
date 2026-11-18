---
description: "PubChem (NCBI) is the world's largest free chemistry database."
---

# PubChem

PubChem (NCBI) is the world's largest free chemistry database. Look up compounds by name, SMILES, InChIKey or CID; get properties, synonyms, descriptions, cross-references and 3D conformers; search by similarity, substructure or formula; read substances, bioassays, genes, proteins, taxonomy, pathways and cell lines; and get data sheet sections and annotations. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [pubchem.ncbi.nlm.nih.gov](https://pubchem.ncbi.nlm.nih.gov) |
| **Authentication** | No authentication |
| **Actions** | 37 |
| **Events** | 0 |
| **Slug** | `pubChem` |

## Use it

Add PubChem from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pubChem.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Search Terms | `autocomplete` | Get search term suggestions from a PubChem dictionary as you type (GET autocomplete/{dictionary}/{term}/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/autocomplete |
| Get Annotations by Heading | `getAnnotationsByHeading` | Get every record's annotation for one heading across PubChem, paged, e.g. all Boiling Point values for compounds (GET pug_view/annotations/heading/JSON?heading=&heading_type=&page=). One page can be about 2 MB. Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-view |
| Get Assay Compound IDs | `getAssayCompoundIds` | Get the compounds tested in a bioassay, optionally only actives or inactives (GET assay/aid/{aid}/cids/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Assay Concise Data | `getAssayConciseData` | Get a bioassay's results as a table: SID, CID, activity outcome and value (GET assay/aid/{aid}/concise/JSON). Large screens can return many MB - use small assays. Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Assay Description | `getAssayDescription` | Get the full description of a bioassay: protocol, target, results definitions (GET assay/aid/{aid}/description/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Assay Summary | `getAssaySummary` | Get a short summary of bioassays: name, source, counts of active/tested substances and compounds, targets (GET assay/aid/{aid}/summary/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Assay Targets | `getAssayTargets` | Get the targets of a bioassay by type: ProteinGI, ProteinName, GeneID or GeneSymbol (GET assay/aid/{aid}/targets/{types}/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Cell Line Summary | `getCellLineSummary` | Get a summary of a cell line by Cellosaurus accession (GET cell/cellacc/{accession}/summary/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Compound Assay IDs | `getCompoundAids` | Get the bioassay ids (AIDs) that tested compounds (GET compound/{namespace}/{identifier}/aids/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Compound Assay Summary | `getCompoundAssaySummary` | Get a table of bioassay results for compounds: AID, activity outcome, target, activity value (GET compound/{namespace}/{identifier}/assaysummary/JSON). Very well-studied compounds can return a few MB. Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Compound CIDs | `getCompoundCids` | Convert compound names, SMILES or InChIKeys to PubChem CIDs (GET compound/{namespace}/{identifier}/cids/JSON). Unknown names return 404. Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Compound Conformer IDs | `getCompoundConformerIds` | Get the 3D conformer ids of compounds (GET compound/{namespace}/{identifier}/conformers/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Compound Cross-References | `getCompoundXrefs` | Get cross-references of compounds by type, e.g. RegistryID, RN (CAS), PubMedID, PatentID, GeneID, MMDBID, TaxonomyID (GET compound/{namespace}/{identifier}/xrefs/{types}/JSON). PatentID lists can be large. Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Compound Data Sheet Section | `getCompoundView` | Get one section of a compound's PubChem data sheet (PUG View), e.g. Boiling Point, Melting Point, Solubility, Pharmacology (GET pug_view/data/compound/{cid}/JSON?heading=). The heading keeps the response small; a full record can be several MB. Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-view |
| Get Compound Dates | `getCompoundDates` | Get creation and modification dates of compound records (GET compound/{namespace}/{identifier}/dates/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Compound Description | `getCompoundDescription` | Get the title and text descriptions of compounds with their sources (GET compound/{namespace}/{identifier}/description/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Compound Properties | `getCompoundProperties` | Get chosen computed properties for compounds, e.g. MolecularFormula, MolecularWeight, IUPACName, SMILES, InChIKey, XLogP, TPSA (GET compound/{namespace}/{identifier}/property/{properties}/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Compound Record | `getCompound` | Get the full PubChem compound record (atoms, bonds, coordinates, computed properties) (GET compound/{namespace}/{identifier}/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Compound Substance IDs | `getCompoundSids` | Get the substance ids (SIDs) deposited for compounds (GET compound/{namespace}/{identifier}/sids/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Compound Synonyms | `getCompoundSynonyms` | Get all names and synonyms of compounds (GET compound/{namespace}/{identifier}/synonyms/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Conformer | `getConformer` | Get one 3D conformer record by conformer id (GET conformers/{conformer_id}/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Data Source Table | `getSourceTable` | Get a table of PubChem data sources with record counts and URLs (GET sourcetable/{substance\|assay}/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Gene Summary | `getGeneSummary` | Get a summary of a gene: symbol, name, taxonomy, description, synonyms (GET gene/{geneid\|genesymbol}/{id}/summary/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Pathway Summary | `getPathwaySummary` | Get a summary of a biological pathway (GET pathway/pwacc/{accession}/summary/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Periodic Table | `getPeriodicTable` | Get the periodic table with element properties (GET periodictable/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Protein Summary | `getProteinSummary` | Get a summary of a protein by accession (GET protein/accession/{accession}/summary/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Substance Compound IDs | `getSubstanceCids` | Get the standardized compound ids (CIDs) for substances (GET substance/{sid\|name}/{id}/cids/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Substance Record | `getSubstance` | Get a deposited substance record by SID or name (GET substance/{sid\|name}/{id}/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Substance Synonyms | `getSubstanceSynonyms` | Get the names a depositor gave a substance (GET substance/{sid\|name}/{id}/synonyms/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Get Taxonomy Summary | `getTaxonomySummary` | Get a summary of an organism: scientific and common names, rank, lineage (GET taxonomy/taxid/{taxid}/summary/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| List Annotation Headings | `listAnnotationHeadings` | List all PUG View annotation headings and their record types (GET annotations/headings/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| List Data Sources | `listSources` | List the names of PubChem data sources for substances or assays (GET sources/{substance\|assay}/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Search Compounds by Formula | `searchCompoundsByFormula` | Find compounds with a molecular formula, synchronously (GET compound/fastformula/{formula}/cids/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Search Compounds by Substructure | `searchSubstructure` | Find compounds that contain a structure, synchronously (GET compound/fastsubstructure/{smiles\|cid}/{id}/cids/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Search Compounds by Superstructure | `searchSuperstructure` | Find compounds contained in a structure, synchronously (GET compound/fastsuperstructure/{smiles\|cid}/{id}/cids/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Search Identical Compounds | `searchIdenticalCompounds` | Find compounds identical to a structure (same connectivity by default), synchronously (GET compound/fastidentity/{smiles\|cid}/{id}/cids/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
| Search Similar Compounds | `searchSimilarCompounds` | Find compounds with 2D Tanimoto similarity to a structure, synchronously (GET compound/fastsimilarity_2d/{smiles\|cid}/{id}/cids/JSON). Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest |
