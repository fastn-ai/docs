---
description: "Productboard is a product management platform for capturing customer feedback, prioritizing features, and building product roadmaps."
---

# Productboard

Productboard is a product management platform for capturing customer feedback, prioritizing features, and building product roadmaps. This connector covers the Productboard REST API v2: notes (customer feedback) with search and relationships; the unified Entities API for products, components, features, subfeatures, initiatives, objectives, key results, releases, release groups, companies, and users (including configuration discovery, relationships, and select-field values); members and member activity; teams and team membership; Jira integrations; plugin (push) integrations and their connections; and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Authentication** | Bearer token |
| **Actions** | 57 |
| **Events** | 0 |
| **Slug** | `productboard` |

## Use it

Add Productboard from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.productboard.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Entity | `createEntity` | Creates a new product-management entity (product, component, feature, subfeature, initiative, objective, key result, release, release group, company, or user). Provide the type and field values; child types (feature, subfeature, component) require a parent supplied via relationships. |
| Create Entity Relationship | `createEntityRelationship` | Creates a relationship from an entity to a target entity. Types: parent, child, link, isBlockedBy, isBlocking. |
| Create Field Value | `createEntityFieldValue` | Creates a new option value for a select-type field (SINGLE_SELECT, MULTI_SELECT, TAG). STATUS fields are not supported. If color is omitted a color is auto-assigned. |
| Create Note | `createNote` | Creates a new note (customer or internal feedback). Provide the note type and field values; the title (name) is required and textNotes also require content. Optionally attach a customer or product-link relationship. |
| Create Note Relationship | `createNoteRelationship` | Links a note to another entity: either a customer (a user or company) or a product link (e.g. a feature). A note can have one customer and multiple links. |
| Create Plugin Integration | `createPluginIntegration` | Creates a plugin (push) integration that adds a push button to entities. Provide the integration name, initial button label, and an action URL. When enabled, Productboard probes the action URL; set integrationStatus to disabled to skip the probe. |
| Create Team | `createTeam` | Creates a new team. Provide a unique name and a unique handle (lowercase alphanumeric, used for @mentions); a description is optional. |
| Create Webhook Subscription | `createWebhook` | Creates a webhook subscription that notifies a URL on each change to the subscribed event types. The notification URL must be HTTPS and publicly resolvable. |
| Delete Entity | `deleteEntity` | Permanently deletes an entity by ID. Any child entities (e.g. a product's components, a feature's subfeatures) are deleted as part of a cascading delete. This is irreversible. |
| Delete Entity Relationship | `deleteEntityRelationship` | Removes a relationship of the given type between an entity and a target entity. |
| Delete Field Value | `deleteEntityFieldValue` | Deletes an option value from a select-type field. By default deletion is rejected if the value is in use; use force to unset it everywhere, or replaceWith to reassign to another value. |
| Delete Note | `deleteNote` | Permanently deletes a note and all of its content, metadata, and relationships. This is irreversible; use Update Note with archived=true for a soft delete. |
| Delete Note Relationship | `deleteNoteRelationship` | Removes a relationship between a note and a target entity (a customer or a product link). |
| Delete Plugin Integration | `deletePluginIntegration` | Permanently deletes a plugin integration and all of its connections. Entities lose their push buttons. This cannot be undone. |
| Delete Plugin Integration Connection | `deletePluginIntegrationConnection` | Permanently deletes the connection between an entity and the third-party system, resetting the push button to its initial state. |
| Delete Team | `deleteTeam` | Permanently deletes a team and all of its membership associations. This is irreversible. |
| Delete Webhook Subscription | `deleteWebhook` | Permanently deletes a webhook subscription; no further notifications are sent after deletion. |
| Get Entity | `getEntity` | Retrieves all configured fields and values for a single entity by its ID. |
| Get Entity Configuration | `getEntityConfiguration` | Returns configuration metadata for a single entity type, including its fields, patch operations, and supported filters. |
| Get Jira Integration | `getJiraIntegration` | Returns details of a specific Jira integration by its UUID. |
| Get Jira Integration Connection | `getJiraIntegrationConnection` | Returns a specific Productboard feature to Jira issue connection, identified by integration UUID and entity UUID. |
| Get Member | `getMember` | Retrieves the full details of a workspace member by their UUID, including name, username, email, and role. |
| Get Note | `getNote` | Retrieves the full details of a specific note by its ID. |
| Get Note Configuration | `getNoteConfiguration` | Returns configuration metadata for a specific note type, including supported fields and patch operations. |
| Get Plugin Integration | `getPluginIntegration` | Returns a single plugin integration by ID. The write-only action configuration is never returned. |
| Get Plugin Integration Connection | `getPluginIntegrationConnection` | Returns the connection for a specific entity within a plugin integration. If none exists, a connection with state=initial is returned rather than a 404. |
| Get Team | `getTeam` | Retrieves the full details of a team by its UUID, including name, handle, description, and metadata. |
| Get Webhook Subscription | `getWebhook` | Returns a single webhook subscription by ID. |
| List Entities | `listEntities` | Retrieves a paginated list of product-management entities of a given type (e.g. features, initiatives), with optional filters for owner, status, teams, parent, archived state, and source metadata. |
| List Entity Configurations | `listEntityConfigurations` | Returns configuration metadata for all entity types (products, features, initiatives, etc.), including which fields are available, required, and filterable in your workspace. |
| List Entity Relationships | `listEntityRelationships` | Retrieves all relationships (parent, child, and linked entities) associated with an entity. |
| List Field Values | `listEntityFieldValues` | Returns a paginated list of the allowed options for a select-type or status field (SINGLE_SELECT, MULTI_SELECT, TAG, STATUS), identified by its field id. |
| List Jira Integration Connections | `listJiraIntegrationConnections` | Returns all Productboard feature to Jira issue connections for a given integration; can look up a connection by Jira issue key or id. |
| List Jira Integrations | `listJiraIntegrations` | Returns details of all Jira integrations configured in the workspace, with cursor-based pagination. |
| List Member Activities | `listMemberActivities` | Lists member activity records with optional date filtering and pagination. |
| List Members | `listMembers` | Retrieves a paginated list of workspace members. Supports searching by name or email and filtering by role. |
| List Note Configurations | `listNoteConfigurations` | Returns configuration metadata for note types, including supported fields, patch operations, and validation rules. |
| List Note Relationships | `listNoteRelationships` | Retrieves all relationships connected to a note, including its customer (a user or company) and product links (e.g. linked features). |
| List Notes | `listNotes` | Retrieves a paginated list of notes (customer feedback), newest first, with optional filters for archived/processed state, owner, creator, source metadata, and date ranges. |
| List Plugin Integration Connections | `listPluginIntegrationConnections` | Returns all connections for a plugin integration (excluding those in the initial state), with cursor-based pagination and optional state filtering. |
| List Plugin Integrations | `listPluginIntegrations` | Returns all plugin (push) integrations for the workspace, with cursor-based pagination. |
| List Team Members | `listTeamMembers` | Returns a paginated list of the members belonging to a specific team, newest membership first. |
| List Teams | `listTeams` | Retrieves a paginated list of teams, newest first, with optional name/handle/query filters. |
| List Webhook Subscriptions | `listWebhooks` | Returns all webhook subscriptions for the workspace, with cursor-based pagination. |
| Search Entities | `searchEntities` | Performs a filtered search over entities of a single type using a POST body, supporting long ID lists and complex field/relationship filters that exceed URL length limits. |
| Search Members | `searchMembers` | Performs a filtered search over workspace members using a POST body: batch lookups by IDs or emails, role filters, and full-text search. |
| Search Notes | `searchNotes` | Performs a filtered search over notes using a POST body, supporting full-text search plus relationship, metadata, and date filters. |
| Search Plugin Integration Connections | `searchPluginIntegrationConnections` | Performs a filtered search over a plugin integration's connections using a POST body, useful for long entity-id lists. |
| Search Teams | `searchTeams` | Performs a filtered search over teams using a POST body: batch lookups by IDs, names, or handles plus full-text search. |
| Set Entity Parent | `setEntityParent` | Replaces the parent of an entity. Some types (features, subfeatures) require a parent; this updates it. Provide the parent's entity type and id. |
| Set Note Customer | `setNoteCustomer` | Sets or replaces the single customer (user or company) associated with a note. Provide the customer id and type, or a user email. |
| Set Plugin Integration Connection State | `setPluginIntegrationConnectionState` | Creates or replaces the connection state for an entity within a plugin integration (an upsert). States: connected, error, progress, or initial (resets the button). |
| Update Entity | `updateEntity` | Updates one or more field values of an entity. Provide the fields object to replace values (set a value to null to clear it). |
| Update Field Value | `updateEntityFieldValue` | Updates an existing option value (name and/or color) for a select-type field. Only provided fields are changed. STATUS fields are not supported. |
| Update Note | `updateNote` | Updates one or more field values of an existing note. Provide the fields object to replace values (set a value to null to clear it). |
| Update Plugin Integration | `updatePluginIntegration` | Partially updates a plugin integration. Omitted fields keep their current value. Updating the action URL while enabled triggers a new probe. |
| Update Team | `updateTeam` | Updates a team's fields and/or its members. Use fields to change name/handle/description, and patch to add, remove, set, or clear members. |
