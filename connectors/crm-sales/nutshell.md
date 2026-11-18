---
description: "Nutshell CRM connector over the JSON-RPC 2.0 API (https://app.nutshell.com/api/v1/json)."
---

# Nutshell

Nutshell CRM connector over the JSON-RPC 2.0 API (https://app.nutshell.com/api/v1/json). Full coverage of leads, contacts, accounts (companies), activities, tasks, notes, users, teams, products, sources, tags, emails, timeline, pipelines/stagesets, and CRM metadata. HTTP Basic auth (login email + API key).

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [nutshell.com](https://nutshell.com) |
| **Authentication** | Basic auth |
| **Actions** | 84 |
| **Events** | 0 |
| **Slug** | `nutshell` |

## Use it

Add Nutshell from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nutshell.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Account | `newAccount` | Create a new account (company). Minimal body is {name}. |
| Create Activity | `newActivity` | Log/create a new activity. activityTypeId is required. logNote must be an object {note}. Link leads and participants (contacts) by id. |
| Create Contact | `newContact` | Create a new contact (person). name can be a plain string (auto-split into given/family) or an object {givenName, familyName}. email accepts {"--primary":"a@b.com"}. phone accepts {"--primary":"+1..."}. Note: job title is set per contact-account relationship, not here. |
| Create Email | `newEmail` | Log a raw RFC822 email into Nutshell. emailString is the full raw message. createContacts controls auto-creating contacts from addresses. |
| Create Lead | `newLead` | Create a new lead. Provide the lead object. Link contacts/accounts by id. Minimal viable lead links at least one account or contact. |
| Create Note | `newNote` | Attach a new note to an entity (lead/contact/account). entity is a ref {id, entityType}; note is the text. |
| Create Product | `newProduct` | Create a new product or service in the Nutshell catalogue. name and type are required; set a price per market in prices. |
| Create Source | `newSource` | Create a new lead source by name. Returns the created source. |
| Create Tag | `newTag` | Create a new tag. Provide the tag object with a name and the entityType it applies to (Leads/Contacts/Accounts). |
| Create Task | `newTask` | Create a new task. title is required. Optionally link to an entity (lead/contact/account) and set dueTime/assignee. |
| Create Team | `newTeam` | Create a new team. name is required. Optionally include user refs. |
| Create User | `newUser` | Invite/create a new Nutshell user. Provide emails (required). Optionally set isAdministrator/isEnabled. The display name derives from the email and is edited via editUser. Note: may consume a seat and send an invitation email. |
| Delete Account | `deleteAccount` | Delete an account by id. Requires current rev. Returns true. |
| Delete Activity | `deleteActivity` | Delete an activity by id. Requires current rev. Returns true. |
| Delete Contact | `deleteContact` | Delete a contact by id. Requires current rev. Returns true. |
| Delete Lead | `deleteLead` | Delete a lead by id. Requires the current rev. Returns true on success. |
| Delete Note | `deleteNote` | Delete a note by id. Requires current rev. Returns true. |
| Delete Product | `deleteProduct` | Delete a product by id. Requires current rev. Returns true. |
| Delete Task | `deleteTask` | Delete a task by id. Requires current rev. Returns true. |
| Delete Team | `deleteTeam` | Delete a team by id. Requires current rev. Returns true. |
| Delete User | `deleteUser` | Delete/deactivate a user by id. Requires current rev. Returns true. |
| Edit Account | `editAccount` | Update an account. Requires current rev. account holds only fields to change. |
| Edit Activity | `editActivity` | Update an activity. Requires current rev. activity holds fields to change. |
| Edit Contact | `editContact` | Update a contact. Requires current rev. contact holds only fields to change. |
| Edit Lead | `editLead` | Update an existing lead. Requires the current rev (from getLead). The lead object contains only the fields to change. |
| Edit Note | `editNote` | Update a note's text. Requires current rev. note holds the new text. |
| Edit Product | `editProduct` | Update a product or service in the Nutshell catalogue. Requires the current rev; only the product fields you send are changed. Set prices per market in prices. |
| Edit Step | `editStep` | Update a lead process step. Requires current rev. step holds fields to change (e.g. mark complete). |
| Edit Task | `editTask` | Update a task. Requires current rev. task holds fields to change (e.g. completedTime to complete it). |
| Edit Team | `editTeam` | Update a team. Requires current rev. |
| Edit User | `editUser` | Update a user. Requires current rev. user holds fields to change. |
| Find Account Types | `findAccountTypes` | List all account types (used to set accountTypeId on accounts). |
| Find Accounts | `findAccounts` | Search/list accounts (companies) with optional filter query and pagination. |
| Find Activities | `findActivities` | Search/list activities (logged/scheduled interactions). params.query is required (pass {} for all). |
| Find Activity Types | `findActivityTypes` | List all activity types (Phone Call, Meeting, etc.) used to set activityTypeId. |
| Find Audiences | `findAudiences` | List audiences (contact segments). |
| Find Backups | `findBackups` | List available data backups/exports (Enterprise). Takes no parameters. |
| Find Competitors | `findCompetitors` | List competitors. |
| Find Contacts | `findContacts` | Search/list contacts (people) with optional filter query and pagination. Returns contact stubs. |
| Find Custom Fields | `findCustomFields` | List custom field definitions, optionally scoped to an entity type via params.entityType (Leads/Contacts/Accounts). Pass {} for all. |
| Find Delays | `findDelays` | List configured lead delays. |
| Find Industries | `findIndustries` | List industries (used to set industryId on accounts). |
| Find Lead Outcomes | `findLeadOutcomes` | List lead outcomes (win/loss reasons). Maps to JSON-RPC method findLead_Outcomes. |
| Find Leads | `findLeads` | Search/list leads with an optional filter query and pagination. Returns an array of lead stubs. params.query is required by the API (pass {} for no filter). |
| Find Markets | `findMarkets` | List markets (used to set market on leads). |
| Find Milestones | `findMilestones` | List pipeline milestones (stages). Use to get milestoneId for leads. |
| Find Notes | `findNotes` | Search/list notes with optional filter query and pagination. |
| Find Origins | `findOrigins` | List activity/interaction origins. |
| Find Processes | `findProcesses` | List lead processes matching a query. params.query is required (pass {} for all). |
| Find Products | `findProducts` | List products in the catalog with ordering/pagination. |
| Find Settings | `findSettings` | List instance settings. |
| Find Sources | `findSources` | List lead sources with ordering/pagination. |
| Find Stagesets | `findStagesets` | List pipelines (stagesets). Use to get stagesetId for leads. |
| Find Tags | `findTags` | List all tags grouped by entity type (Leads, Contacts, Accounts). Takes no parameters. |
| Find Tasks | `findTasks` | Search/list tasks. params.query is required (pass {} for all). |
| Find Teams | `findTeams` | List teams with ordering/pagination. |
| Find Territories | `findTerritories` | List sales territories. |
| Find Timeline | `findTimeline` | Retrieve the timeline (chronological activity/note/email feed) for a specific entity. params.query scopes to one record via its entityType and id, e.g. {"entityType":"Accounts","id":6}. |
| Find Users | `findUsers` | List users in the Nutshell instance with optional filter and pagination. |
| Get Account | `getAccount` | Retrieve a single account (company) by numeric id. |
| Get Activity | `getActivity` | Retrieve a single activity by numeric id. |
| Get Analytics Report | `getAnalyticsReport` | Retrieve an analytics report. reportType is one of Effort, NewLeads, Pipeline, SalesCycle, SalesProcess, Success, WinRate. period accepts 'm' (current month), 'y' (current year), '-d30' (last 30 days), 'yyyy-mm', 'yyyy-Q#', or a 'timestamp-timestamp' range. |
| Get Contact | `getContact` | Retrieve a single contact (person) by numeric id. |
| Get Current User | `getCurrentUser` | Retrieve the currently authenticated user (the API key owner). Takes no parameters. |
| Get Email | `getEmail` | Retrieve a single logged email by numeric id. |
| Get Instance Data | `instanceData` | Get metadata about the Nutshell instance (features, limits, config). Takes no parameters. |
| Get Lead | `getLead` | Retrieve a single lead by its numeric id. Optionally pass a rev. |
| Get Note | `getNote` | Retrieve a single note by numeric id. |
| Get Product | `getProduct` | Retrieve a single product by numeric id. |
| Get Task | `getTask` | Retrieve a single task by numeric id. |
| Get Team | `getTeam` | Retrieve a single team by numeric id. |
| Get Update Times | `getUpdateTimes` | Get the last-modified timestamps for entity types (for polling/sync). Takes no parameters. |
| Get User | `getUser` | Retrieve a specific user by numeric id. |
| Search Accounts | `searchAccounts` | Full-text search of accounts by name. |
| Search Activity Participants | `searchActivityParticipants` | Search entities (contacts/users/accounts) that can participate in an activity. |
| Search By Email | `searchByEmail` | Look up contacts/leads/accounts associated with an email address. |
| Search Competitors | `searchCompetitors` | Full-text search of competitors by name. |
| Search Contacts | `searchContacts` | Full-text search of contacts by name/email. |
| Search Contacts And Users | `searchContactsAndUsers` | Full-text search across contacts and users. |
| Search Leads | `searchLeads` | Full-text search of leads by name/number. Returns lightweight matches. |
| Search Products | `searchProducts` | Full-text search of products by name/sku. |
| Search Sources | `searchSources` | Full-text search of lead sources by name. |
| Search Universal | `searchUniversal` | Universal full-text search across leads, contacts, and accounts. |
| Search Users And Teams | `searchUsersAndTeams` | Full-text search across users and teams. |
