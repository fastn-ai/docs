---
description: "Nimble CRM connector."
hidden: true
---

# Nimble

<img src="../../.gitbook/assets/connectors/lg/nimble.png" alt="Nimble logo">

Nimble CRM connector. Relationship-focused CRM: contacts (person and company records with a rich fields structure), contact custom fields/tabs/groups/choices, contact pipelines and lead transitions, notes, proceedings/activities, deals (v2) with pipelines/stages/fields/groups/tags/files/notes, message drafts, and current-user info. REST API over https://app.nimble.com, Bearer API-key auth.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [nimble.com](https://nimble.com) |
| **Authentication** | Bearer token |
| **Slug** | `nimble` |

## Use it

Add Nimble from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nimble.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add custom field to deals pipeline | `postDealsPipelineField` | Create a custom field in a deals pipeline. field_type is an object describing the field kind; presentation must match field_type. |
| Add lost reason to deals pipeline | `postDealsPipelineLostReason` | Add a new lost reason to a deals pipeline. |
| Add tags to deals | `postDealsTags` | Assign tags to deals matched by an advanced search query. query is a deals advanced-search object. |
| Archive deals pipeline | `markDealsPipelineArchived` | Archive a deals pipeline. |
| Archive deals pipeline stage | `markDealsPipelineStageArchived` | Archive a stage in a deals pipeline (DELETE archives the stage). |
| Assign tags to contact | `putContactTags` | Sets the tags for a specified contact to the given set (replaces existing tags). |
| Clear leads transitions | `deleteLeadTransitions` | Clear all lead transitions in the current pipeline run for a contact. |
| Contact ids list | `listContactsIds` | Contact ids list. Has same parameters as a regular contacts list, but returns only contact ids. Works faster than regular contact list. |
| Contact List | `listContacts` | Contact List. Returns list of contacts filtered by specified parameters. Allows filters by advanced search query, tags, keyword. |
| Create a draft message | `postMessageDraft` | Create a draft message (email). recipients/cc/bcc are arrays of participant objects; sender is a participant object. |

<details>

<summary>See 76 more actions</summary>

* **Create choice for field** `postContactChoiceField`: Create a choice for a contact custom field.
* **Create choice in deals pipeline field** `postDealsPipelineFieldChoice`: Create a choice in a deals pipeline custom field. choice is an object {id, value}.
* **Create contact field** `postContactField`: Create a new contact custom field. field_type is an object describing the field kind; presentation must match the field_type.
* **Create contact note (with note id)** `postContactNoteWithId`: Create a contact note using a specific note id in the path.
* **Create contacts fields group** `createContactsFieldsGroup`: Create a new contacts fields group inside a tab.
* **Create contacts fields tab** `postContactsFieldsTab`: Create a new contacts fields tab.
* **Create contacts note** `postContactNote`: Creates a note on one or more contacts. At least one contact id is required (Nimble does not support notes without contacts). contact_ids count 1-10.
* **Create deals pipeline fields group** `postDealsPipelineGroup`: Create a fields group in a deals pipeline.
* **Create deals pipeline stage** `postDealsPipelineStage`: Create a new stage in a deals pipeline.
* **Create new contact** `postContact`: Create new contact. For contact-persons at least first name or last name is required. For contact-companies company name is required. The 'fields' object mirrors the contact listing structure: {"&lt;field name&gt;":[{"value":"...","is_primary":false}]}.
* **Create new deal** `createNewDeal`: Create a new deal. fields_values maps deal field ids to value arrays: {"&lt;field_id&gt;":[{"value":"...","is_primary":false}]}. At least the deal name field is required. pipeline_id and stage_id are required.
* **Create new deals pipeline** `postDealsPipelines`: Create a new deals pipeline. stages is an array of stage objects (each with name); lost_reasons an array of reason strings/objects; fields_tab_members an array of field members.
* **Create note to the deal** `createDealNote`: Create a note attached to a deal.
* **Current user info** `getMyself`: Current user info. Returns information about authenticated user. User_id from this response can be used to assign different Nimble entities to this user. Such as tasks, contacts, etc.
* **Delete choice from deals pipeline field** `deleteDealsPipelineFieldChoice`: Delete a choice from a deals pipeline custom field.
* **Delete contact by id** `deleteContact`: Delete contact by id.
* **Delete contact choice by id** `deleteContactChoiceField`: Delete a contact custom field choice by id.
* **Delete contact field** `deleteContactField`: Delete a contact custom field by id.
* **Delete contact note by id** `deleteContactNote`: Delete a contact note by id.
* **Delete contacts fields group** `deleteContactsFieldsGroup`: Delete a contacts fields group by id.
* **Delete contacts tab by id** `deleteContactsTabById`: Delete contacts tab by id. Deletes tab by id
* **Delete custom field from deals pipeline** `deleteDealsPipelineField`: Delete a custom field from a deals pipeline. If preflight_checks is true and deals use this field, returns an error.
* **Delete deal by id** `deleteDeal`: Delete a deal by its id.
* **Delete deal file** `deleteDealFile`: Delete a deal file.
* **Delete deal note by id** `deleteDealNote`: Delete a deal note by id.
* **Delete deals pipeline by id** `deleteDealsPipeline`: Delete a deals pipeline by id. All deals in this pipeline are also deleted.
* **Delete deals pipeline fields group** `deleteDealsPipelineFieldsGroup`: Delete a fields group from a deals pipeline.
* **Delete deals tag by name** `deleteDealsTag`: Delete a deals tag by its name.
* **Delete is_primary mark from field** `deletePrimaryMarkFromContactField`: Delete the is_primary mark from a contact field value at a position.
* **Delete list of contacts** `deleteContactsList2`: Delete list of contacts. Deletes a list of contacts by specified advanced search query. Requires bulk delete permission for authenticated user.
* **Exit lead from pipeline successfully** `markLeadExitedSuccessful`: Exit a lead (contact) from a pipeline successfully (won). lead_id is the contact id; pipeline_id is a contact pipeline id.
* **Exit lead from pipeline unsuccessfully** `markLeadExitedUnsuccessfully`: Exit a lead (contact) from a pipeline unsuccessfully (lost).
* **Get contact by id** `getContact`: Returns contact data by its id.
* **Get contact note by id** `getContactNote`: Returns a single contact note by id.
* **Get contacts by identifiers** `listContactsForIdentifiers`: Returns standard contact listings for the specified identifiers (up to 30 ids, comma-separated).
* **Get deal by id** `getDeal`: Get a deal by its id.
* **Get deal file download url** `getDealFileDownloadUrl`: Returns a download link for a selected deal file.
* **Get deals pipeline by id** `getDealsPipeline`: Get a deals pipeline by its id.
* **List all user's deals** `listUserDeals`: Lists all deals the user can see, sorted by last updated (newest first). Page through results with page and per_page.
* **List column catalogue** `listColumnCatalogue`: Returns a list of deal columns and column groups for the requesting user.
* **List company contacts fields** `listCompanyContactsFields`: Return all available metadata (tabs/groups/fields) for the company's contact fields.
* **List contact proceedings** `listContactProceedings`: Get all proceedings (activities: notes, deals, tasks) for a contact matching query parameters.
* **List contact's notes** `listContactNotes`: Returns a paginated list of notes for the specified contact.
* **List contacts fields metadata (deprecated)** `listContactsFieldsMetadata`: (DEPRECATED) Returns all available metadata for company's fields/groups.
* **List contacts pipelines** `listAvailableContactsPipelines`: Returns a list of contact (lead) pipelines available to the requesting user.
* **List contacts proceeding providers** `listContactsProceedingProviders`: Returns a list of user-available contact proceeding types (business activities: new deal closed, task assigned, note added, etc).
* **List deal standard and pipeline fields** `listAllUserDealsFields`: Retrieves the list of deal fields for this user (standard) and fields for each pipeline. Use to discover field ids for createNewDeal.
* **List deal's overdue activities** `listDealsOverdueActivities`: Returns a feed of overdue activities for a given deal, sorted by time since overdue (desc).
* **List deals pipelines** `listDealsPipelines`: Get the user's deal pipelines.
* **List deals tags** `listDealsTags`: Returns a list of deals tags.
* **List messages drafts** `listMessagesDrafts`: List draft messages, optionally filtered by recipients or sender.
* **List pipeline deals by owners** `listPipelineDealsByOwner`: Get deals in a pipeline listing separated by owners.
* **List pipeline deals by stages** `listPipelineDealsByStages`: Get deals in a pipeline listing separated by stages.
* **Mark field with is_primary flag** `putPrimaryMarkToContactField`: Mark a contact field value at a position with the is_primary flag.
* **Move lead to a pipeline stage** `moveLead`: Move a lead (contact) to a stage within the pipeline. Use to enter the pipeline for the first time.
* **Store deal file** `storeDealFile`: Attach a file to a deal. Two kinds: (1) a link to a file in Google Drive, Dropbox or OneDrive: send file_name, file_size and metadata {source, file_url}; (2) a file already uploaded to Nimble storage: send file_name and metadata {data_id}. Nimble replies 201 with an empty body; read the new file with Get Deal.
* **Unarchive deals pipeline** `markDealsPipelineUnarchived`: Un-archive a deals pipeline.
* **Undo lead won/lost transition** `undoLeadTransition`: Undo a recent lead transition to a won or lost stage.
* **Update choice in deals pipeline field** `putDealsPipelineFieldChoice`: Update a choice in a deals pipeline custom field.
* **Update contact by id** `putContact`: Updates a contact by its id. Fields are merged into the existing values by default. Send fields and/or avatar_url; is_important marks the contact as important.
* **Update contact field** `putContactField`: Update an existing contact custom field by id (move to group, rename, reorder, change presentation).
* **Update contact note by id** `putContactNote`: Update a contact note by id.
* **Update contacts fields group** `putContactsFieldsGroup`: Update an existing contacts fields group by id.
* **Update contacts fields tab by id** `putContactsTabById`: Update contacts fields tab by id.
* **Update custom field in deals pipeline** `putDealsPipelineField`: Update a custom field in a deals pipeline.
* **Update deal by id** `putDeal`: Edit a deal by its id. fields_values maps deal field ids to value arrays.
* **Update deal file** `putDealFile`: Rename a deal file. Only files uploaded using Azure SDK can be renamed.
* **Update deal note by id** `putDealNote`: Update a deal note by id.
* **Update deals pipeline by id** `putDealsPipeline`: Update a deals pipeline's name, description, or color by id.
* **Update deals pipeline fields group** `putDealsPipelineFieldsGroup`: Update a fields group in a deals pipeline.
* **Update deals pipeline stage** `putDealsPipelineStage`: Update a deals pipeline stage.
* **Update deals tag by name** `putDealsTag`: Rename a deals tag by its name.
* **Update field choice** `putContactsFieldChoice`: Update a contact custom field choice.
* **Update the successful exit transition** `putLeadExitSuccessful`: Updates the won 'exit' transition with new notes and/or actual_exit_date.
* **Update the unsuccessful exit transition** `putLeadExitUnsuccessful`: Updates the lost 'exit' transition with new notes, actual_exit_date and/or lost_reason.
* **Won deals sum last month** `getWonLastMonthDealsSum`: Returns the sum and count of all deal amounts won last month.

</details>
