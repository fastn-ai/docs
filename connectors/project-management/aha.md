---
description: "Aha!"
---

# Aha!

Aha! product roadmap and idea management API (v1). Manage products/workspaces, features, releases and release phases, epics, requirements, ideas with categories/organizations/votes/comments, initiatives, goals and key results, to-dos, comments, users, competitors, personas, strategic models, notes, teams, integrations, record links, custom table records and custom fields.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [aha.io](https://aha.io) |
| **Authentication** | Bearer token |
| **Actions** | 124 |
| **Events** | 0 |
| **Slug** | `aha` |

## Use it

Add Aha! from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.aha.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Feature to Epic | `convertFeatureToEpic` | Convert a feature into an epic. |
| Convert Requirement to Feature | `convertRequirementToFeature` | Convert a requirement into a standalone feature. |
| Create Competitor | `createCompetitor` | Create a competitor in a product/workspace. |
| Create Epic | `createEpic` | Create an epic within a product/workspace. |
| Create Epic Comment | `createEpicComment` | Add a comment to a epic. |
| Create Epic in Release | `createEpicInRelease` | Create an epic within a specific release. |
| Create Feature | `createFeature` | Create a feature within a release. |
| Create Feature Comment | `createFeatureComment` | Add a comment to a feature. |
| Create Feature Record Link | `createFeatureRecordLink` | Create a link from a feature to another record. Returns 204 No Content on success. |
| Create Goal | `createGoal` | Create a goal within a product/workspace. |
| Create Goal Comment | `createGoalComment` | Add a comment to a goal. |
| Create Idea | `createIdea` | Create an idea within a product/workspace. |
| Create Idea Category | `createIdeaCategory` | Create an idea category in a product/workspace. |
| Create Idea Comment | `createIdeaComment` | Add a comment to an idea. |
| Create Idea Organization | `createIdeaOrganization` | Create an idea organization. |
| Create Idea Vote | `createIdeaEndorsement` | Add a vote (endorsement) to an idea on behalf of a portal user. |
| Create Initiative | `createInitiative` | Create an initiative within a product/workspace. |
| Create Initiative Comment | `createInitiativeComment` | Add a comment to a initiative. |
| Create Key Result | `createKeyResult` | Create a key result under a goal. |
| Create Note | `createNote` | Create a note (page) in a product/workspace. |
| Create Note Comment | `createNoteComment` | Add a comment to a note. |
| Create Persona | `createPersona` | Create a persona in a product/workspace. |
| Create Release | `createRelease` | Create a release within a product/workspace. |
| Create Release Comment | `createReleaseComment` | Add a comment to a release. |
| Create Release Phase | `createReleasePhase` | Create a phase or milestone within a release. |
| Create Release Phase Comment | `createReleasePhaseComment` | Add a comment to a release phase. |
| Create Requirement | `createRequirement` | Create a requirement within a feature. |
| Create Requirement Comment | `createRequirementComment` | Add a comment to a requirement. |
| Create To-Do | `createToDo` | Create a to-do, optionally associated with a record. |
| Create To-Do Comment | `createToDoComment` | Add a comment to a to-do. |
| Create User | `createUser` | Create a user with access to a specific product/workspace. |
| Delete Competitor | `deleteCompetitor` | Delete a competitor by ID or reference number. |
| Delete Epic | `deleteEpic` | Delete an epic by ID or reference number. |
| Delete Feature | `deleteFeature` | Delete a feature by ID or reference number. |
| Delete Goal | `deleteGoal` | Delete a goal by ID or reference number. |
| Delete Idea | `deleteIdea` | Delete an idea by ID or reference number. |
| Delete Initiative | `deleteInitiative` | Delete an initiative by ID or reference number. |
| Delete Key Result | `deleteKeyResult` | Delete a key result by ID. |
| Delete Note | `deleteNote` | Delete a note (page) by ID or reference number. |
| Delete Persona | `deletePersona` | Delete a persona by ID or reference number. |
| Delete Record Link | `deleteRecordLink` | Delete a record link by ID. |
| Delete Release | `deleteRelease` | Delete a release by ID or reference number. |
| Delete Release Phase | `deleteReleasePhase` | Delete a release phase or milestone by ID. |
| Delete Requirement | `deleteRequirement` | Delete a requirement by ID or reference number. |
| Delete To-Do | `deleteToDo` | Delete a to-do by ID. |
| Duplicate Release | `duplicateRelease` | Create a copy of an existing release. |
| Get Comment | `getComment` | Retrieve a specific comment by ID. |
| Get Competitor | `getCompetitor` | Retrieve a specific competitor by ID or reference number. |
| Get Current User | `getCurrentUser` | Retrieve the profile of the user whose API key is being used. |
| Get Epic | `getEpic` | Retrieve a specific epic by ID or reference number. |
| Get Feature | `getFeature` | Retrieve a specific feature by ID or reference number. |
| Get Goal | `getGoal` | Retrieve a specific goal by ID or reference number. |
| Get Idea | `getIdea` | Retrieve a specific idea by ID or reference number. |
| Get Initiative | `getInitiative` | Retrieve a specific initiative by ID or reference number. |
| Get Key Result | `getKeyResult` | Retrieve a specific key result by ID. |
| Get Note | `getNote` | Retrieve a specific note (page) by ID or reference number. |
| Get Persona | `getPersona` | Retrieve a specific persona by ID or reference number. |
| Get Record Link | `getRecordLink` | Retrieve a specific record link by ID. |
| Get Release | `getRelease` | Retrieve a specific release by ID or reference number. |
| Get Release Phase | `getReleasePhase` | Retrieve a specific release phase or milestone by ID. |
| Get Requirement | `getRequirement` | Retrieve a specific requirement by ID or reference number. |
| Get Strategic Model | `getStrategicModel` | Retrieve a specific strategic model by ID or reference number. |
| Get To-Do | `getToDo` | Retrieve a specific to-do by ID. |
| Get User | `getUser` | Retrieve a specific user by ID. |
| Get Workspace | `getProduct` | Retrieve a specific product/workspace by ID or reference key. |
| Get Workspace Integration | `getProductIntegration` | Retrieve a specific integration for a product/workspace. |
| List Audits | `listAudits` | List audit records (historical changes) across the account, filtered by date. |
| List Competitors | `listCompetitors` | List competitors in a product/workspace. |
| List Custom Field Definitions | `listCustomFieldDefinitions` | List all custom field definitions in the account. |
| List Epic Comments | `listEpicComments` | List comments on a epic. |
| List Epic Features | `listEpicFeatures` | List features that belong to a specific epic. |
| List Epics | `listEpics` | List all epics across the account. |
| List Feature Comments | `listFeatureComments` | List comments on a feature. |
| List Feature Record Links | `listFeatureRecordLinks` | List record links for a feature. |
| List Feature Requirements | `listFeatureRequirements` | List requirements belonging to a feature. |
| List Features | `listFeatures` | List all features across the account, optionally filtered. |
| List Goal Comments | `listGoalComments` | List comments on a goal. |
| List Goals | `listGoals` | List all goals across the account. |
| List Idea Categories | `listIdeaCategories` | List idea categories for a product/workspace. |
| List Idea Comments | `listIdeaComments` | List comments on a specific idea. |
| List Idea Organizations | `listIdeaOrganizations` | List idea organizations in the account. |
| List Idea Votes | `listIdeaEndorsements` | List votes (endorsements) on a specific idea. |
| List Ideas | `listIdeas` | List all ideas across the account. |
| List Initiative Comments | `listInitiativeComments` | List comments on a initiative. |
| List Initiatives | `listInitiatives` | List all initiatives across the account. |
| List Key Results | `listKeyResults` | List key results for a specific goal. |
| List My Assigned Records | `listMyAssignedRecords` | List records (features, releases, etc.) assigned to the current user. |
| List My Pending To-Dos | `listMyPendingTasks` | List to-dos (tasks) pending for the current user. |
| List Personas | `listPersonas` | List personas in a product/workspace. |
| List Release Comments | `listReleaseComments` | List comments on a release. |
| List Release Epics | `listReleaseEpics` | List epics in a specific release. |
| List Release Features | `listReleaseFeatures` | List features in a specific release. |
| List Release Phases | `listReleasePhases` | List phases and milestones for a specific release. |
| List Releases | `listReleases` | List all releases across the account. |
| List Requirement Comments | `listRequirementComments` | List comments on a requirement. |
| List Strategic Models | `listStrategicModels` | List strategic models (business model canvases, etc.) in the account. |
| List To-Dos | `listToDos` | List all to-dos across the account. |
| List Users | `listUsers` | List all users in the account. |
| List Workspace Epics | `listProductEpics` | List epics in a specific product/workspace. |
| List Workspace Features | `listProductFeatures` | List features in a specific product/workspace. |
| List Workspace Goals | `listProductGoals` | List goals in a specific product/workspace. |
| List Workspace Ideas | `listProductIdeas` | List ideas in a specific product/workspace. |
| List Workspace Initiatives | `listProductInitiatives` | List initiatives in a specific product/workspace. |
| List Workspace Integrations | `listProductIntegrations` | List integrations configured for a product/workspace. |
| List Workspace Notes | `listProductNotes` | List notes (pages) in a product/workspace. |
| List Workspace Releases | `listProductReleases` | List releases in a specific product/workspace. |
| List Workspace To-Dos | `listProductToDos` | List to-dos in a specific product/workspace. |
| List Workspace Users | `listProductUsers` | List users with access to a specific product/workspace. |
| List Workspaces | `listProducts` | List all products/workspaces the current user can access. |
| Remove User from Workspace | `deleteUser` | Remove a user's role in a product/workspace, revoking their access to it. Returns 204 No Content. |
| Update Competitor | `updateCompetitor` | Update a competitor's attributes. |
| Update Epic | `updateEpic` | Update an epic's attributes. Only the fields you send are changed. |
| Update Feature | `updateFeature` | Update a feature's attributes. Only the fields you send are changed. |
| Update Goal | `updateGoal` | Update a goal's attributes. |
| Update Idea | `updateIdea` | Update an idea's attributes. Only the fields you send are changed. |
| Update Initiative | `updateInitiative` | Update an initiative's attributes. Only the fields you send are changed. |
| Update Key Result | `updateKeyResult` | Update a key result. |
| Update Note | `updateNote` | Update a note's attributes. |
| Update Persona | `updatePersona` | Update a persona's attributes. |
| Update Release | `updateRelease` | Update a release's attributes. Only the fields you send are changed. |
| Update Release Phase | `updateReleasePhase` | Update a release phase's attributes. |
| Update Requirement | `updateRequirement` | Update a requirement's attributes. Only the fields you send are changed. |
| Update To-Do | `updateToDo` | Update a to-do's attributes. |
| Update User | `updateUser` | Update a user's attributes. |
