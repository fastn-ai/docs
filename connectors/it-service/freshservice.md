---
description: "Freshservice IT service management — tickets, problems, changes, releases, assets, service catalog, knowledge base, and administration via the Freshservice…"
hidden: true
---

# Freshservice

<img src="../../.gitbook/assets/connectors/lg/freshservice.png" alt="Freshservice logo">

Freshservice IT service management — tickets, problems, changes, releases, assets, service catalog, knowledge base, and administration via the Freshservice API v2.

| | |
| --- | --- |
| **Category** | [IT and service management](README.md) |
| **Website** | [freshservice.com](https://freshservice.com) |
| **Authentication** | Basic auth |
| **Slug** | `freshservice` |

## Use it

Add Freshservice from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.freshservice.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Acknowledge Alert | `acknowledgeAlert` | Acknowledges a monitoring alert. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| Add Catalog Item To Service Request | `addCatalogItemToServiceRequest` | Adds an additional service catalog item to an existing service request ticket. |
| Add Requester Group Member | `addRequesterGroupMember` | Adds a requester to a manual requester group. |
| Add Software Installations | `addSoftwareInstallations` | Records software installations on one or more devices. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Add Software Users | `addSoftwareUsers` | Associates users with a software application. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Archive Project | `archiveProject` | Archives a project so it no longer appears in active project lists. |
| Archive Service Catalog Shared Field | `archiveSharedField` | Archives a service catalog shared field so it can no longer be added to items. |
| Cancel Change Approval | `cancelChangeApproval` | Cancels a pending approval on a change. |
| Cancel Journey Request | `cancelJourneyRequest` | Cancels an in-progress employee journey request. Requires an employee journey to be configured under Admin &gt; Employee Journeys. Journey configurations cannot be created through the API. |
| Cancel Ticket Approval | `cancelTicketApproval` | Cancels a pending approval on a ticket. |
| Change Contract Status | `changeContractStatus` | Submits a contract for approval, or approves or rejects a submitted contract. Requires the Contract Management capability on the Freshservice plan, and a vendor record, which is itself part of Asset Management (CMDB). |
| Convert Agent To Requester | `convertAgentToRequester` | Converts an agent into a requester, releasing their agent licence. |
| Convert Requester To Agent | `convertRequesterToAgent` | Converts a requester into an agent, consuming an agent licence. |
| Create Agent | `createAgent` | Creates a new agent. The agent consumes an agent licence on the account. |
| Create Agent Group | `createAgentGroup` | Creates a new agent group. |
| Create Alert Note | `createAlertNote` | Adds a note to a monitoring alert. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| Create Announcement | `createAnnouncement` | Creates and schedules an announcement. |
| Create Asset | `createAsset` | Creates a new asset in the CMDB. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Create Asset Component | `createAssetComponent` | Adds a component to an asset. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Create Asset Type | `createAssetType` | Creates a new asset type in the CMDB. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Create Change | `createChange` | Creates a new change record. |
| Create Change Advisory Board | `createCab` | Creates a change advisory board. |
| Create Change Approval Group | `createChangeApprovalGroup` | Creates an approval group on a change. |
| Create Change Note | `createChangeNote` | Adds a note to a change. |
| Create Change Task | `createChangeTask` | Creates a task on a change. |
| Create Change Time Entry | `createChangeTimeEntry` | Logs a time entry against a change. |
| Create Child Ticket | `createChildTicket` | Creates a child ticket under an existing parent ticket. |
| Create Contract | `createContract` | Creates a new contract. A vendor is required, so the Asset Management feature must be enabled. Requires the Contract Management capability on the Freshservice plan, and a vendor record, which is itself part of Asset Management (CMDB). |
| Create Custom Object Record | `createCustomObjectRecord` | Creates a record in a custom object. The data object must match the object's field schema. |
| Create Department | `createDepartment` | Creates a new department. |
| Create Journey Request | `createJourneyRequest` | Starts an employee journey, such as onboarding or offboarding, for a user. Requires an employee journey to be configured under Admin &gt; Employee Journeys. Journey configurations cannot be created through the API. |
| Create Location | `createLocation` | Creates a new location. |
| Create Offboarding Request | `createOffboardingRequest` | Raises an employee offboarding request. Requires Employee Offboarding to be configured with at least one active offboarding actor under Admin &gt; Employee Offboarding; otherwise Freshservice returns HTTP 404 inaccessible_api. |
| Create On-Call Escalation Policy | `createEscalationPolicy` | Creates an escalation policy on an on-call schedule, defining which incidents it applies to, who is notified at each level and how often notification repeats. |
| Create On-Call Schedule | `createOnCallSchedule` | Creates an on-call schedule in a workspace. |
| Create On-Call Shift | `createOnCallShift` | Creates a new shift within an on-call schedule, including its primary, secondary and tertiary rosters. Only agents with the 'Manage On-call schedules' privilege can call this, and every roster member must already belong to the agent group that owns the schedule. |
| Create Onboarding Request | `createOnboardingRequest` | Raises an employee onboarding request. Requires the Employee Onboarding capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Create Post-Incident Report Template | `createPirTemplate` | Creates a post-incident report template. |
| Create Problem | `createProblem` | Creates a new problem record. |
| Create Problem Note | `createProblemNote` | Adds a note to a problem. |
| Create Problem Task | `createProblemTask` | Creates a task on a problem. |
| Create Problem Time Entry | `createProblemTimeEntry` | Logs a time entry against a problem. |
| Create Product | `createProduct` | Creates a new product in the CMDB. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Create Project | `createProject` | Creates a new project. |
| Create Project Task | `createProjectTask` | Creates a task in a project. |
| Create Project Task Note | `createProjectTaskNote` | Adds a note to a project task. |
| Create Purchase Order | `createPurchaseOrder` | Creates a new purchase order. |
| Create Relationships | `createRelationships` | Creates one or more CMDB relationships between configuration items. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Create Release | `createRelease` | Creates a new release record. |
| Create Release Note | `createReleaseNote` | Adds a note to a release. |
| Create Release Task | `createReleaseTask` | Creates a task on a release. |
| Create Release Time Entry | `createReleaseTimeEntry` | Logs a time entry against a release. |
| Create Requester | `createRequester` | Creates a new requester. |
| Create Requester Group | `createRequesterGroup` | Creates a new manual requester group. |
| Create Service Catalog Item | `createServiceItem` | Creates a service catalog item. The item body is sent as a service_item envelope. |
| Create Service Catalog Shared Field | `createSharedField` | Creates a shared field that can be reused across service catalog items. |
| Create Software | `createSoftware` | Creates a software application record. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Create Solution Article | `createSolutionArticle` | Creates a knowledge base article inside a folder. |
| Create Solution Category | `createSolutionCategory` | Creates a knowledge base category. |
| Create Solution Folder | `createSolutionFolder` | Creates a knowledge base folder inside a category. The default category cannot be used. |
| Create Status Page Subscriber | `createStatusPageSubscriber` | Subscribes an email address to status page updates. Requires a status page to exist. Status pages are created in the Freshservice admin console under Admin &gt; Status Pages; there is no API to create one. |
| Create Ticket | `createTicket` | Creates a new ticket. Supply either requester_id, email, or phone to identify the requester. |
| Create Ticket Approval Group | `createTicketApprovalGroup` | Creates an approval group on a service request ticket. |
| Create Ticket Communication | `createTicketCommunication` | Records an external communication, such as an outbound email, against a ticket. |
| Create Ticket Note | `createTicketNote` | Adds a note to a ticket. Notes can be private to agents or visible to the requester. |
| Create Ticket Reply | `createTicketReply` | Adds a public reply to a ticket, which is emailed to the requester. |
| Create Ticket Source | `createTicketSource` | Creates a custom ticket source that can then be set on tickets. |
| Create Ticket Task | `createTicketTask` | Creates a task on a ticket. |
| Create Ticket Time Entry | `createTicketTimeEntry` | Logs a time entry against a ticket. |
| Create User Delegation | `createUserDelegation` | Delegates a user's approvals to another user for a period of time. |
| Create Vendor | `createVendor` | Creates a new vendor. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Deactivate Agent | `deactivateAgent` | Deactivates an agent, releasing their agent licence. The record is retained. |
| Deactivate Requester | `deactivateRequester` | Deactivates a requester. The record is retained and can be reactivated. |
| Delete Agent Group | `deleteAgentGroup` | Deletes an agent group. |
| Delete Alert | `deleteAlert` | Deletes a monitoring alert. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| Delete Alert Note | `deleteAlertNote` | Deletes a note from a monitoring alert. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| Delete Announcement | `deleteAnnouncement` | Deletes an announcement. |
| Delete Asset | `deleteAsset` | Moves an asset to the trash. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Delete Asset Type | `deleteAssetType` | Deletes an asset type. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Delete Change | `deleteChange` | Deletes a change record. |
| Delete Change Advisory Board | `deleteCab` | Deletes a change advisory board. |
| Delete Change Note | `deleteChangeNote` | Deletes a note from a change. |
| Delete Change Task | `deleteChangeTask` | Deletes a task from a change. |
| Delete Change Time Entry | `deleteChangeTimeEntry` | Deletes a time entry logged against a change. |
| Delete Conversation | `deleteConversation` | Deletes a note or reply from a ticket. |
| Delete Conversation Attachment | `deleteConversationAttachment` | Removes an attachment from a ticket note or reply. |
| Delete Custom Object Record | `deleteCustomObjectRecord` | Deletes a record from a custom object. |
| Delete Department | `deleteDepartment` | Deletes a department. |
| Delete Journey Request | `deleteJourneyRequest` | Deletes an employee journey request. Requires an employee journey to be configured under Admin &gt; Employee Journeys. Journey configurations cannot be created through the API. |
| Delete Location | `deleteLocation` | Deletes a location. |
| Delete On-Call Escalation Policy | `deleteEscalationPolicy` | Deletes an escalation policy from an on-call schedule. |
| Delete On-Call Schedule | `deleteOnCallSchedule` | Deletes an on-call schedule. |
| Delete On-Call Shift | `deleteOnCallShift` | Deletes a shift from an on-call schedule. |
| Delete Post-Incident Report Template | `deletePirTemplate` | Deletes a post-incident report template. |
| Delete Problem | `deleteProblem` | Moves a problem to the trash. |
| Delete Problem Note | `deleteProblemNote` | Deletes a note from a problem. |
| Delete Problem Task | `deleteProblemTask` | Deletes a task from a problem. |
| Delete Problem Time Entry | `deleteProblemTimeEntry` | Deletes a time entry logged against a problem. |
| Delete Product | `deleteProduct` | Deletes a product from the CMDB. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Delete Project | `deleteProject` | Deletes a project. |
| Delete Project Task | `deleteProjectTask` | Deletes a task from a project. |
| Delete Purchase Order | `deletePurchaseOrder` | Deletes a purchase order. |
| Delete Relationships | `deleteRelationships` | Deletes one or more CMDB relationships. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Delete Release | `deleteRelease` | Moves a release to the trash. |
| Delete Release Note | `deleteReleaseNote` | Deletes a note from a release. |
| Delete Release Task | `deleteReleaseTask` | Deletes a task from a release. |
| Delete Release Time Entry | `deleteReleaseTimeEntry` | Deletes a time entry logged against a release. |
| Delete Requester Group | `deleteRequesterGroup` | Deletes a requester group. |
| Delete Service Catalog Item | `deleteServiceItem` | Deletes a service catalog item. |
| Delete Service Catalog Shared Field | `deleteSharedField` | Deletes a service catalog shared field. |
| Delete Software | `deleteSoftware` | Deletes one or more software application records. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Delete Solution Article | `deleteSolutionArticle` | Moves a knowledge base article to the trash. |
| Delete Solution Category | `deleteSolutionCategory` | Moves a knowledge base category to the trash. |
| Delete Solution Folder | `deleteSolutionFolder` | Moves a knowledge base folder to the trash. |
| Delete Status Page Subscriber | `deleteStatusPageSubscriber` | Removes a subscriber from a status page. Requires a status page to exist. Status pages are created in the Freshservice admin console under Admin &gt; Status Pages; there is no API to create one. |
| Delete Ticket | `deleteTicket` | Moves a ticket to the trash. Use Restore Ticket to recover it. |
| Delete Ticket Attachment | `deleteTicketAttachment` | Removes an attachment from a ticket. |
| Delete Ticket Task | `deleteTicketTask` | Deletes a task from a ticket. |
| Delete Ticket Time Entry | `deleteTicketTimeEntry` | Deletes a time entry logged against a ticket. |
| Delete User Delegation | `deleteUserDelegation` | Removes the approval delegation configured for a user. |
| Delete Vendor | `deleteVendor` | Deletes a vendor. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Demote Ticket From Major Incident | `demoteTicketFromMajorIncident` | Demotes a major incident back to a regular incident. |
| Export Audit Log | `exportAuditLog` | Starts an asynchronous export of the account audit log and returns a job identifier. |
| Export On-Call Shift Events | `exportShiftEvents` | Exports on-call shift occurrences as an iCal or webcal feed. |
| Export Post-Incident Report Template | `exportPirTemplate` | Exports a post-incident report template as a document. |
| Filter Project Tasks | `filterProjectTasks` | Searches the tasks in a project using a filter expression. |
| Filter Tickets | `filterTickets` | Searches tickets using a Freshservice query expression, for example "priority:3 AND status:2". |
| Forget Agent | `forgetAgent` | Permanently deletes an agent and all of their personal data. This cannot be undone. |
| Forget Requester | `forgetRequester` | Permanently deletes a requester and all of their personal data. This cannot be undone. |
| Get Agent | `getAgent` | Retrieves a single agent by numeric ID. |
| Get Agent Group | `getAgentGroup` | Retrieves a single agent group by numeric ID. |
| Get Agent Role | `getRole` | Retrieves a single agent role by numeric ID. |
| Get Alert | `getAlert` | Retrieves a single monitoring alert by numeric ID. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| Get Alert Note | `getAlertNote` | Retrieves a single note on a monitoring alert. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| Get Announcement | `getAnnouncement` | Retrieves a single announcement by numeric ID. |
| Get Asset | `getAsset` | Retrieves a single asset by its display ID. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Get Asset Assignment History | `getAssetAssignmentHistory` | Retrieves the assignment history of an asset. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Get Asset Type | `getAssetType` | Retrieves a single asset type by numeric ID. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Get Attachment | `getAttachment` | Retrieves metadata for an attachment, including a time-limited download URL. |
| Get Business Hours | `getBusinessHours` | Retrieves a single business hours calendar by numeric ID. |
| Get Canned Response | `getCannedResponse` | Retrieves a single canned response by numeric ID. |
| Get Canned Response Folder | `getCannedResponseFolder` | Retrieves a single canned response folder by numeric ID. |
| Get Change | `getChange` | Retrieves a single change by its numeric ID. |
| Get Change Advisory Board | `getCab` | Retrieves a single change advisory board. |
| Get Change Approval | `getChangeApproval` | Retrieves a single approval requested on a change. |
| Get Change Note | `getChangeNote` | Retrieves a single note on a change. |
| Get Change Task | `getChangeTask` | Retrieves a single task on a change. |
| Get Change Time Entry | `getChangeTimeEntry` | Retrieves a single time entry logged against a change. |
| Get Contract | `getContract` | Retrieves a single contract by numeric ID. Requires the Contract Management capability on the Freshservice plan, and a vendor record, which is itself part of Asset Management (CMDB). |
| Get Current Agent | `getCurrentAgent` | Retrieves the profile of the agent whose API key is used for authentication. |
| Get Current On-Call Agents | `getCurrentOnCall` | Retrieves the agents who are on call right now for a given on-call schedule, including the shift and roster tier each is covering. |
| Get Custom Object | `getCustomObject` | Retrieves a custom object definition, including its field schema. |
| Get Department | `getDepartment` | Retrieves a single department by numeric ID. |
| Get Job Status | `getJob` | Retrieves the status and result of an asynchronous job, such as an audit log export. Job IDs are returned by the bulk relationship endpoints, which are part of Asset Management (CMDB). Without that capability there is no job to query. |
| Get Journey Request | `getJourneyRequest` | Retrieves a single employee journey request by numeric ID. Requires an employee journey to be configured under Admin &gt; Employee Journeys. Journey configurations cannot be created through the API. |
| Get Location | `getLocation` | Retrieves a single location by numeric ID. |
| Get Offboarding Form | `getOffboardingForm` | Retrieves the field definitions of the employee offboarding form. Requires Employee Offboarding to be configured with at least one active offboarding actor under Admin &gt; Employee Offboarding; otherwise Freshservice returns HTTP 404 inaccessible_api. |
| Get Offboarding Request | `getOffboardingRequest` | Retrieves a single employee offboarding request. Requires Employee Offboarding to be configured with at least one active offboarding actor under Admin &gt; Employee Offboarding; otherwise Freshservice returns HTTP 404 inaccessible_api. |
| Get On-Call Escalation Policy | `getEscalationPolicy` | Retrieves a single escalation policy on an on-call schedule. |
| Get On-Call Schedule | `getOnCallSchedule` | Retrieves a single on-call schedule. |
| Get On-Call Shift | `getOnCallShift` | Retrieves a single shift in an on-call schedule. |
| Get Onboarding Form | `getOnboardingForm` | Retrieves the field definitions of the employee onboarding form. Requires the Employee Onboarding capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Get Onboarding Request | `getOnboardingRequest` | Retrieves a single employee onboarding request. Requires the Employee Onboarding capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Get Post-Incident Report Template | `getPirTemplate` | Retrieves a single post-incident report template. |
| Get Problem | `getProblem` | Retrieves a single problem by its numeric ID. |
| Get Problem Note | `getProblemNote` | Retrieves a single note on a problem. |
| Get Problem Task | `getProblemTask` | Retrieves a single task on a problem. |
| Get Problem Time Entry | `getProblemTimeEntry` | Retrieves a single time entry logged against a problem. |
| Get Product | `getProduct` | Retrieves a single product by numeric ID. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Get Project | `getProject` | Retrieves a single project by numeric ID. |
| Get Project Task | `getProjectTask` | Retrieves a single task in a project. |
| Get Purchase Order | `getPurchaseOrder` | Retrieves a single purchase order by numeric ID. |
| Get Relationship | `getRelationship` | Retrieves a single CMDB relationship by numeric ID. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Get Release | `getRelease` | Retrieves a single release by its numeric ID. |
| Get Release Note | `getReleaseNote` | Retrieves a single note on a release. |
| Get Release Task | `getReleaseTask` | Retrieves a single task on a release. |
| Get Release Time Entry | `getReleaseTimeEntry` | Retrieves a single time entry logged against a release. |
| Get Requester | `getRequester` | Retrieves a single requester by numeric ID. |
| Get Requester Group | `getRequesterGroup` | Retrieves a single requester group by numeric ID. |
| Get Service Catalog Item | `getServiceItem` | Retrieves a single service catalog item by its display ID. |
| Get Service Catalog Shared Field | `getSharedField` | Retrieves a single service catalog shared field by its identifier. |
| Get Software | `getSoftware` | Retrieves a single software application by numeric ID. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Get Software User | `getSoftwareUser` | Retrieves a single user association on a software application. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Get Solution Article | `getSolutionArticle` | Retrieves a single knowledge base article by numeric ID. |
| Get Solution Category | `getSolutionCategory` | Retrieves a single knowledge base category by numeric ID. |
| Get Solution Folder | `getSolutionFolder` | Retrieves a single knowledge base folder by numeric ID. |
| Get Status Page Service Component | `getStatusPageServiceComponent` | Retrieves a single service component on a status page. Requires a status page to exist. Status pages are created in the Freshservice admin console under Admin &gt; Status Pages; there is no API to create one. |
| Get Ticket | `getTicket` | Retrieves a single ticket by its numeric ID. |
| Get Ticket Approval | `getTicketApproval` | Retrieves a single approval requested on a ticket. |
| Get Ticket Communication | `getTicketCommunication` | Retrieves a single communication linked to a ticket. |
| Get Ticket CSAT Response | `getTicketCsatResponse` | Retrieves the customer satisfaction survey response submitted for a ticket. |
| Get Ticket Task | `getTicketTask` | Retrieves a single task belonging to a ticket. |
| Get Ticket Time Entry | `getTicketTimeEntry` | Retrieves a single time entry logged against a ticket. |
| Get User Assignment History | `getUserAssignmentHistory` | Retrieves the asset assignment history for a user. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Get User Delegation | `getUserDelegation` | Retrieves the approval delegation configured for a user. |
| Get Vendor | `getVendor` | Retrieves a single vendor by numeric ID. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Get Workspace | `getWorkspace` | Retrieves a single workspace by numeric ID. |
| Link Ticket To Project | `linkProjectTicket` | Links a ticket to a project. |
| Link Ticket To Project Task | `linkProjectTaskTicket` | Links a ticket to a project task. |
| List Agent Fields | `listAgentFields` | Retrieves the agent field definitions, including custom fields. |
| List Agent Groups | `listAgentGroups` | Retrieves the agent groups configured in the account. |
| List Agent Roles | `listRoles` | Retrieves the agent roles configured in the account. |
| List Agents | `listAgents` | Retrieves a paginated list of agents, optionally filtered by state or a query expression. |
| List Alert Logs | `listAlertLogs` | Retrieves the log entries recorded against a monitoring alert. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| List Alert Notes | `listAlertNotes` | Retrieves the notes added to a monitoring alert. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| List Alerts | `listAlerts` | Retrieves monitoring alerts ingested into Freshservice, filtered by a query expression. |
| List Announcements | `listAnnouncements` | Retrieves the announcements published in the account. |
| List Approvals | `listApprovals` | Retrieves approvals across tickets and changes. Both are required: parent (the record type, e.g. ticket or change) AND at least one of approver_id, status, parent_id, or delegatee_id. Calling with no filters returns HTTP 400 missing_filter_params. |
| List Asset Components | `listAssetComponents` | Retrieves the hardware or software components attached to an asset. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Asset Contracts | `listAssetContracts` | Retrieves the contracts associated with an asset. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Asset Relationships | `listAssetRelationships` | Retrieves the CMDB relationships an asset participates in. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Asset Requests | `listAssetRequests` | Retrieves the tickets raised against an asset. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Asset Type Fields | `listAssetTypeFields` | Retrieves the field definitions for an asset type. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Asset Types | `listAssetTypes` | Retrieves the asset types configured in the CMDB. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Assets | `listAssets` | Retrieves a paginated list of assets from the CMDB. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Business Hours | `listBusinessHours` | Retrieves the business hours calendars configured in the account. |
| List Canned Response Folders | `listCannedResponseFolders` | Retrieves the canned response folders configured in the account. |
| List Canned Responses | `listCannedResponses` | Retrieves the canned responses configured in the account. |
| List Canned Responses In Folder | `listCannedResponsesInFolder` | Retrieves the canned responses stored in a folder. |
| List Change Advisory Boards | `listCabs` | Retrieves the change advisory boards configured in the account. |
| List Change Approval Groups | `listChangeApprovalGroups` | Retrieves the approval groups configured on a change. |
| List Change Approvals | `listChangeApprovals` | Retrieves all approvals requested on a change. |
| List Change Form Fields | `listChangeFields` | Retrieves the change form field definitions, including custom fields. |
| List Change Notes | `listChangeNotes` | Retrieves all notes on a change. |
| List Change Tasks | `listChangeTasks` | Retrieves all tasks on a change. |
| List Change Time Entries | `listChangeTimeEntries` | Retrieves all time entries logged against a change. |
| List Changes | `listChanges` | Retrieves a paginated list of changes. |
| List Contract Associated Assets | `listContractAssociatedAssets` | Retrieves the assets covered by a contract. Requires the Contract Management capability on the Freshservice plan, and a vendor record, which is itself part of Asset Management (CMDB). |
| List Contract Attachments | `listContractAttachments` | Retrieves the files attached to a contract. Requires the Contract Management capability on the Freshservice plan, and a vendor record, which is itself part of Asset Management (CMDB). |
| List Contract Type Fields | `listContractTypeFields` | Retrieves the field definitions for a contract type. |
| List Contract Types | `listContractTypes` | Retrieves the contract types configured in the account. |
| List Contracts | `listContracts` | Retrieves the contracts recorded in the account. |
| List Custom Object Records | `listCustomObjectRecords` | Retrieves the records stored in a custom object, optionally filtered by a query expression. |
| List Custom Objects | `listCustomObjects` | Retrieves the custom objects defined in the account. |
| List Department Fields | `listDepartmentFields` | Retrieves the department field definitions, including custom fields. |
| List Departments | `listDepartments` | Retrieves the departments configured in the account. |
| List Journey Configuration Data Fields | `listJourneyConfigDataFields` | Retrieves the data fields defined on an employee journey configuration. Requires an employee journey to be configured under Admin &gt; Employee Journeys. Journey configurations cannot be created through the API. |
| List Journey Configurations | `listJourneyConfigs` | Retrieves the employee journey configurations defined in the account. |
| List Journey Request Activities | `listJourneyRequestActivities` | Retrieves the activities carried out as part of an employee journey request. Requires an employee journey to be configured under Admin &gt; Employee Journeys. Journey configurations cannot be created through the API. |
| List Journey Requests | `listJourneyRequests` | Retrieves employee journey requests, optionally filtered by state. |
| List Locations | `listLocations` | Retrieves the locations configured in the account. |
| List Offboarding Request Tickets | `listOffboardingRequestTickets` | Retrieves the tickets generated by an employee offboarding request. Requires Employee Offboarding to be configured with at least one active offboarding actor under Admin &gt; Employee Offboarding; otherwise Freshservice returns HTTP 404 inaccessible_api. |
| List Offboarding Requests | `listOffboardingRequests` | Retrieves employee offboarding requests. Requires the Employee Offboarding feature. Requires Employee Offboarding to be configured with at least one active offboarding actor under Admin &gt; Employee Offboarding; otherwise Freshservice returns HTTP 404 inaccessible_api. |
| List On-Call Escalation Policies | `listEscalationPolicies` | Retrieves the escalation policies attached to an on-call schedule. |
| List On-Call Schedules | `listOnCallSchedules` | Retrieves the on-call schedules configured in a workspace. |
| List On-Call Shift Events | `listShiftEvents` | Retrieves the on-call shift occurrences within a time window. |
| List On-Call Shifts | `listOnCallShifts` | Retrieves the shifts defined in an on-call schedule. |
| List Onboarding Request Tickets | `listOnboardingRequestTickets` | Retrieves the tickets generated by an employee onboarding request. Requires the Employee Onboarding capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Onboarding Requests | `listOnboardingRequests` | Retrieves employee onboarding requests. Requires the Employee Onboarding feature. Requires the Employee Onboarding capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Post-Incident Report Templates | `listPirTemplates` | Retrieves the post-incident report templates configured in a workspace. |
| List Problem Form Fields | `listProblemFields` | Retrieves the problem form field definitions, including custom fields. |
| List Problem Notes | `listProblemNotes` | Retrieves all notes on a problem. |
| List Problem Tasks | `listProblemTasks` | Retrieves all tasks on a problem. |
| List Problem Time Entries | `listProblemTimeEntries` | Retrieves all time entries logged against a problem. |
| List Problems | `listProblems` | Retrieves a paginated list of problems. |
| List Products | `listProducts` | Retrieves the products configured in the CMDB. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Project Fields | `listProjectFields` | Retrieves the project field definitions, including custom fields. |
| List Project Memberships | `listProjectMemberships` | Retrieves the members of a project. |
| List Project Sprints | `listProjectSprints` | Retrieves the sprints defined in a project. |
| List Project Task Notes | `listProjectTaskNotes` | Retrieves the notes on a project task. |
| List Project Task Priorities | `listProjectTaskPriorities` | Retrieves the task priorities available in a project. |
| List Project Task Statuses | `listProjectTaskStatuses` | Retrieves the task statuses available in a project. |
| List Project Task Tickets | `listProjectTaskTickets` | Retrieves the tickets linked to a project task. |
| List Project Task Types | `listProjectTaskTypes` | Retrieves the task types available in a project. |
| List Project Templates | `listProjectTemplates` | Retrieves the project templates available in the account. |
| List Project Tickets | `listProjectTickets` | Retrieves the tickets linked to a project. |
| List Project Versions | `listProjectVersions` | Retrieves the versions defined in a project. |
| List Projects | `listProjects` | Retrieves the projects in the account. Requires the Project Management feature. |
| List Purchase Orders | `listPurchaseOrders` | Retrieves the purchase orders recorded in the account. |
| List Relationship Types | `listRelationshipTypes` | Retrieves the CMDB relationship types configured in the account. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Relationships | `listRelationships` | Retrieves the CMDB relationships defined between configuration items. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Release Form Fields | `listReleaseFields` | Retrieves the release form field definitions, including custom fields. |
| List Release Notes | `listReleaseNotes` | Retrieves all notes on a release. |
| List Release Tasks | `listReleaseTasks` | Retrieves all tasks on a release. |
| List Release Time Entries | `listReleaseTimeEntries` | Retrieves all time entries logged against a release. |
| List Releases | `listReleases` | Retrieves a paginated list of releases. |
| List Requested Items | `listRequestedItems` | Retrieves the service catalog items requested on a service request ticket. |
| List Requester Fields | `listRequesterFields` | Retrieves the requester field definitions, including custom fields. |
| List Requester Group Members | `listRequesterGroupMembers` | Retrieves the requesters belonging to a manual requester group. |
| List Requester Groups | `listRequesterGroups` | Retrieves the requester groups configured in the account. |
| List Requesters | `listRequesters` | Retrieves a paginated list of requesters, optionally filtered by email, phone, or a query expression. |
| List Service Catalog Items | `listServiceItems` | Retrieves the items published in the service catalog. |
| List Service Catalog Shared Fields | `listSharedFields` | Retrieves the shared fields reusable across service catalog items. |
| List Service Categories | `listServiceCategories` | Retrieves the service catalog categories in the account. |
| List SLA Policies | `listSlaPolicies` | Retrieves the SLA policies configured in the account. |
| List Software | `listSoftware` | Retrieves the software applications tracked in the account. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Software Installations | `listSoftwareInstallations` | Retrieves the devices a software application is installed on. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Software Licences | `listSoftwareLicenses` | Retrieves the licence contracts attached to a software application. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Software Relationships | `listSoftwareRelationships` | Retrieves the CMDB relationships a software application participates in. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Software Users | `listSoftwareUsers` | Retrieves the users associated with a software application. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Solution Articles | `listSolutionArticles` | Retrieves the knowledge base articles in a folder. |
| List Solution Categories | `listSolutionCategories` | Retrieves the knowledge base categories in the account. |
| List Solution Folders | `listSolutionFolders` | Retrieves the knowledge base folders in a category. |
| List Solution Sub-Folders | `listSolutionSubFolders` | Retrieves the sub-folders nested inside a knowledge base folder. |
| List Status Page Incident Statuses | `listStatusPageIncidentStatuses` | Retrieves the incident statuses available on a status page. Requires a status page to exist. Status pages are created in the Freshservice admin console under Admin &gt; Status Pages; there is no API to create one. |
| List Status Page Incidents | `listStatusPageIncidents` | Retrieves the incidents published on a status page. Requires a status page to exist. Status pages are created in the Freshservice admin console under Admin &gt; Status Pages; there is no API to create one. |
| List Status Page Maintenance Statuses | `listStatusPageMaintenanceStatuses` | Retrieves the maintenance statuses available on a status page. Requires a status page to exist. Status pages are created in the Freshservice admin console under Admin &gt; Status Pages; there is no API to create one. |
| List Status Page Maintenances | `listStatusPageMaintenances` | Retrieves the maintenance windows published on a status page. Requires a status page to exist. Status pages are created in the Freshservice admin console under Admin &gt; Status Pages; there is no API to create one. |
| List Status Page Service Components | `listStatusPageServiceComponents` | Retrieves the service components shown on a status page. Requires a status page to exist. Status pages are created in the Freshservice admin console under Admin &gt; Status Pages; there is no API to create one. |
| List Status Page Subscribers | `listStatusPageSubscribers` | Retrieves the people subscribed to a status page. Requires a status page to exist. Status pages are created in the Freshservice admin console under Admin &gt; Status Pages; there is no API to create one. |
| List Status Pages | `listStatusPages` | Retrieves the status pages configured in the account. |
| List Ticket Activities | `getTicketActivities` | Retrieves the activity audit trail for a ticket. |
| List Ticket Approval Groups | `listTicketApprovalGroups` | Retrieves the approval groups configured on a ticket. |
| List Ticket Approvals | `listTicketApprovals` | Retrieves all approvals requested on a ticket. |
| List Ticket Communications | `listTicketCommunications` | Retrieves the external communications, such as emails or Zoom calls, linked to a ticket. |
| List Ticket Conversations | `listTicketConversations` | Retrieves all replies and notes on a ticket. |
| List Ticket Form Fields | `listTicketFields` | Retrieves the ticket form field definitions, including custom fields and their allowed choices. |
| List Ticket Tasks | `listTicketTasks` | Retrieves all tasks belonging to a ticket. |
| List Ticket Time Entries | `listTicketTimeEntries` | Retrieves all time entries logged against a ticket. |
| List Tickets | `listTickets` | Retrieves a paginated list of tickets, optionally filtered by requester, predefined filter, or last-updated time. |
| List Vendors | `listVendors` | Retrieves the vendors configured in the account. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| List Workspaces | `listWorkspaces` | Retrieves the workspaces configured in the account. Workspaces are an Enterprise feature. |
| Mark Post-Incident Report Template As Primary | `markPirTemplatePrimary` | Marks a post-incident report template as the default for the workspace. |
| Merge Requesters | `mergeRequesters` | Merges one or more secondary requesters into a primary requester. |
| Move Asset To Workspace | `moveAsset` | Moves an asset to a different workspace. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Move Change To Workspace | `moveChange` | Moves a change to a different workspace. Moving a record between workspaces requires the Multiple Workspaces capability and at least two workspaces on the account; single-workspace accounts receive HTTP 403 access_denied. |
| Move Contract To Workspace | `moveContract` | Moves a contract to a different workspace. Requires the Contract Management capability on the Freshservice plan, and a vendor record, which is itself part of Asset Management (CMDB). |
| Move Problem To Workspace | `moveProblem` | Moves a problem to a different workspace. Moving a record between workspaces requires the Multiple Workspaces capability and at least two workspaces on the account; single-workspace accounts receive HTTP 403 access_denied. |
| Move Purchase Order To Workspace | `movePurchaseOrder` | Moves a purchase order to a different workspace. |
| Move Release To Workspace | `moveRelease` | Moves a release to a different workspace. Moving a record between workspaces requires the Multiple Workspaces capability and at least two workspaces on the account; single-workspace accounts receive HTTP 403 access_denied. |
| Move Software To Workspace | `moveSoftware` | Moves a software application record to a different workspace. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Move Ticket To Workspace | `moveTicket` | Moves a ticket to a different workspace. Moving a record between workspaces requires the Multiple Workspaces capability and at least two workspaces on the account; single-workspace accounts receive HTTP 403 access_denied. |
| Override On-Call Shift Roster | `overrideOnCallShiftRoster` | Creates, updates or deletes an on-call coverage override on a shift roster, so a different agent covers a given window. Only agents with the 'Provide on-call coverage' privilege can call this. |
| Permanently Delete Asset | `deleteAssetForever` | Permanently deletes an asset. This cannot be undone. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Permanently Delete Solution Article | `deleteSolutionArticleForever` | Permanently deletes a knowledge base article. This cannot be undone. |
| Permanently Delete Solution Category | `deleteSolutionCategoryForever` | Permanently deletes a knowledge base category. This cannot be undone. |
| Permanently Delete Solution Folder | `deleteSolutionFolderForever` | Permanently deletes a knowledge base folder. This cannot be undone. |
| Place Service Request | `placeServiceRequest` | Places a request for a service catalog item, creating a service request ticket. |
| Promote Ticket To Major Incident | `promoteTicketToMajorIncident` | Promotes an incident ticket to a major incident. |
| Reactivate Agent | `reactivateAgent` | Reactivates a previously deactivated agent. |
| Reactivate Requester | `reactivateRequester` | Reactivates a previously deactivated requester. |
| Remove Requester Group Member | `removeRequesterGroupMember` | Removes a requester from a manual requester group. |
| Remove Software Installations | `removeSoftwareInstallations` | Removes recorded software installations from devices. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Remove Software Users | `removeSoftwareUsers` | Removes user associations from a software application. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Reorder On-Call Escalation Policies | `reorderEscalationPolicies` | Re-orders the escalation policies within an on-call schedule. When an incident matches more than one policy, the one with the higher rank sends the notifications. |
| Request Ticket Approval | `requestTicketApproval` | Requests approval on a service request ticket from one or more approvers. |
| Resolve Alert | `resolveAlert` | Marks a monitoring alert as resolved. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| Restore Asset | `restoreAsset` | Restores an asset from the trash. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Restore Problem | `restoreProblem` | Restores a previously deleted problem. |
| Restore Project | `restoreProject` | Restores an archived project to active use. |
| Restore Release | `restoreRelease` | Restores a previously deleted release. |
| Restore Solution Article | `restoreSolutionArticle` | Restores a knowledge base article from the trash. |
| Restore Solution Category | `restoreSolutionCategory` | Restores a knowledge base category from the trash. |
| Restore Solution Folder | `restoreSolutionFolder` | Restores a knowledge base folder from the trash. |
| Restore Ticket | `restoreTicket` | Restores a previously deleted ticket from the trash. |
| Search Service Catalog Items | `searchServiceItems` | Searches the service catalog for items matching a keyword. |
| Search Solution Articles | `searchSolutionArticles` | Searches published knowledge base articles by keyword. |
| Send Change Approval Reminder | `remindChangeApproval` | Sends a reminder email to the approver of a pending change approval. |
| Send Solution Article For Approval | `sendArticleForApproval` | Submits a knowledge base article into its folder's approval workflow. |
| Send Ticket Approval Reminder | `remindTicketApproval` | Sends a reminder email to the approver of a pending ticket approval. |
| Suppress Alert | `suppressAlert` | Suppresses a monitoring alert so it stops generating notifications. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| Unarchive Service Catalog Shared Field | `unarchiveSharedField` | Restores an archived service catalog shared field to active use. |
| Unlink Ticket From Project | `unlinkProjectTicket` | Removes the link between a ticket and a project. |
| Unlink Ticket From Project Task | `unlinkProjectTaskTicket` | Removes the link between a ticket and a project task. |
| Unsuppress Alert | `unsuppressAlert` | Removes suppression from a monitoring alert. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| Update Agent | `updateAgent` | Updates an existing agent. Only the fields supplied are modified. |
| Update Agent Group | `updateAgentGroup` | Updates an existing agent group. Only the fields supplied are modified. |
| Update Alert Note | `updateAlertNote` | Updates a note on a monitoring alert. Alerts are created by Freshservice Alert Management from a connected monitoring tool - there is no API to create one. Configure an inbound monitoring integration under Admin &gt; Alert Management before using this action. |
| Update Announcement | `updateAnnouncement` | Updates an existing announcement. |
| Update Asset | `updateAsset` | Updates an existing asset. Only the fields supplied are modified. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Update Asset Component | `updateAssetComponent` | Updates a component attached to an asset. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Update Asset Type | `updateAssetType` | Updates an asset type. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Update Change | `updateChange` | Updates an existing change. Only the fields supplied are modified. |
| Update Change Advisory Board | `updateCab` | Updates a change advisory board. |
| Update Change Approval Chain Rule | `updateChangeApprovalChainRule` | Sets whether the approval chain on a change is evaluated sequentially or in parallel. |
| Update Change Approval Group | `updateChangeApprovalGroup` | Updates an approval group on a change. |
| Update Change Note | `updateChangeNote` | Updates a note on a change. |
| Update Change Task | `updateChangeTask` | Updates a task on a change. |
| Update Change Time Entry | `updateChangeTimeEntry` | Updates a time entry logged against a change. |
| Update Contract | `updateContract` | Updates an existing contract. Requires the Contract Management capability on the Freshservice plan, and a vendor record, which is itself part of Asset Management (CMDB). |
| Update Conversation | `updateConversation` | Updates the body of an existing ticket note or reply. |
| Update Custom Object Record | `updateCustomObjectRecord` | Updates a record in a custom object. |
| Update Department | `updateDepartment` | Updates an existing department. |
| Update Journey Request | `updateJourneyRequest` | Updates an in-progress employee journey request. Requires an employee journey to be configured under Admin &gt; Employee Journeys. Journey configurations cannot be created through the API. |
| Update Location | `updateLocation` | Updates an existing location. |
| Update On-Call Escalation Policy | `updateEscalationPolicy` | Updates an escalation policy on an on-call schedule. Set the status field to ACTIVE or INACTIVE to enable or disable the policy. |
| Update On-Call Schedule | `updateOnCallSchedule` | Updates an existing on-call schedule. |
| Update On-Call Shift | `updateOnCallShift` | Updates an existing shift in an on-call schedule. Supply the full roster definition, since the rosters supplied replace the ones currently configured on the shift. |
| Update Post-Incident Report Template | `updatePirTemplate` | Updates a post-incident report template. |
| Update Problem | `updateProblem` | Updates an existing problem. Only the fields supplied are modified. |
| Update Problem Note | `updateProblemNote` | Updates a note on a problem. |
| Update Problem Task | `updateProblemTask` | Updates a task on a problem. |
| Update Problem Time Entry | `updateProblemTimeEntry` | Updates a time entry logged against a problem. |
| Update Project | `updateProject` | Updates an existing project. |
| Update Project Task | `updateProjectTask` | Updates a task in a project. |
| Update Project Task Note | `updateProjectTaskNote` | Updates a note on a project task. |
| Update Purchase Order | `updatePurchaseOrder` | Updates an existing purchase order. |
| Update Release | `updateRelease` | Updates an existing release. Only the fields supplied are modified. |
| Update Release Note | `updateReleaseNote` | Updates a note on a release. |
| Update Release Task | `updateReleaseTask` | Updates a task on a release. |
| Update Release Time Entry | `updateReleaseTimeEntry` | Updates a time entry logged against a release. |
| Update Requested Item | `updateRequestedItem` | Updates the quantity, stage, or custom fields of an item requested on a service request. |
| Update Requester | `updateRequester` | Updates an existing requester. Only the fields supplied are modified. |
| Update Requester Group | `updateRequesterGroup` | Updates an existing requester group. |
| Update Service Catalog Item | `updateServiceItem` | Updates a service catalog item. This is a full replacement, so name, category_id, description and visibility must always be supplied. |
| Update Service Catalog Shared Field | `updateSharedField` | Updates a service catalog shared field. |
| Update Software | `updateSoftware` | Updates a software application record. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Update Software Users | `updateSoftwareUsers` | Updates the user associations on a software application. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |
| Update Solution Article | `updateSolutionArticle` | Updates a knowledge base article. |
| Update Solution Category | `updateSolutionCategory` | Updates a knowledge base category. |
| Update Solution Folder | `updateSolutionFolder` | Updates a knowledge base folder. |
| Update Status Page Subscriber | `updateStatusPageSubscriber` | Updates a status page subscriber. Requires a status page to exist. Status pages are created in the Freshservice admin console under Admin &gt; Status Pages; there is no API to create one. |
| Update Ticket | `updateTicket` | Updates an existing ticket. Only the fields supplied are modified. |
| Update Ticket Approval Chain Rule | `updateTicketApprovalChainRule` | Updates whether the approval chain on a ticket is evaluated sequentially or in parallel. |
| Update Ticket Approval Group | `updateTicketApprovalGroup` | Updates an approval group on a service request ticket. |
| Update Ticket Task | `updateTicketTask` | Updates a task on a ticket. Only the fields supplied are modified. |
| Update Ticket Time Entry | `updateTicketTimeEntry` | Updates a time entry logged against a ticket. |
| Update User Delegation | `updateUserDelegation` | Updates the approval delegation configured for a user. |
| Update Vendor | `updateVendor` | Updates an existing vendor. Requires the Asset Management (CMDB) capability on the Freshservice plan; accounts without it receive HTTP 403 require_feature. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Asset Created | `assetCreated` | Fires when a new asset is added to the CMDB. SETUP: Admin &gt; Automation & Productivity &gt; Automation &gt; Workflow Automator &gt; New Automator &gt; choose the Asset module. Event = 'Asset is created', then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced content) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED; set "event_type": "assetCreated". Asset-type-specific attributes live under type_fields and are only delivered if you map them explicitly in the rule JSON. |
| Asset Updated | `assetUpdated` | Fires when an asset record changes, for example when it is reassigned or moved to a new location. SETUP: Workflow Automator &gt; New Automator &gt; Asset module. Event = 'Asset is updated' (optionally scoped to properties such as Used by, Location or Asset state), then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED; set "event_type": "assetUpdated". |
| Change Created | `changeCreated` | Fires when a new change record is raised. SETUP: Admin &gt; Automation & Productivity &gt; Automation &gt; Workflow Automator &gt; New Automator &gt; choose the Change module. Event = 'Change is raised', then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced content) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED; set "event_type": "changeCreated". The schema below is the recommended field set from the Freshservice v2 Change object. The Change module requires an Estate or Forest plan. |
| Change Updated | `changeUpdated` | Fires when a change record is updated, including approval and status transitions. SETUP: Workflow Automator &gt; New Automator &gt; Change module. Event = 'Change is updated' (scope it to Status, Approval status or any property you care about), then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED; |
| Problem Created | `problemCreated` | Fires when a new problem record is created. SETUP: Admin &gt; Automation & Productivity &gt; Automation &gt; Workflow Automator &gt; New Automator &gt; choose the Problem module. Event = 'Problem is raised', then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced content) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED; set "event_type": "problemCreated". The schema below is the recommended field set from the Freshservice v2 Problem object. Note the Problem module requires an Estate or Forest plan. |
| Problem Updated | `problemUpdated` | Fires when a problem record is updated, including status and known-error changes. SETUP: Workflow Automator &gt; New Automator &gt; Problem module. Event = 'Problem is updated' (optionally scoped to specific properties), then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED; |
| Release Created | `releaseCreated` | Fires when a new release record is raised. SETUP: Admin &gt; Automation & Productivity &gt; Automation &gt; Workflow Automator &gt; New Automator &gt; choose the Release module. Event = 'Release is raised', then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced content) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED; set "event_type": "releaseCreated". The Release module requires an Estate or Forest plan. |
| Release Updated | `releaseUpdated` | Fires when a release record is updated. SETUP: Workflow Automator &gt; New Automator &gt; Release module. Event = 'Release is updated' (optionally scoped to the Status property), then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED; set "event_type": "releaseUpdated". |
| Service Request Approval Updated | `ticketApprovalUpdated` | Fires when an approval on a service request is approved or rejected. SETUP: Workflow Automator &gt; New Automator &gt; Ticket module. Event = 'Request approval is approved' or 'Request approval is rejected' (add one rule per outcome, or one rule with both events), then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED - map the approver and approval-status placeholders yourself; Set "event_type": "ticketApprovalUpdated". |
| Task Updated | `taskUpdated` | Fires when a task attached to a ticket, problem, change or release is created, reassigned or completed. SETUP: Workflow Automator &gt; New Automator &gt; pick the parent module (Ticket, Problem, Change or Release). Event = the task event for that module, for example 'Task is added' or 'Task status is updated', then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED - the task fields are only present if you map the task placeholders; set "event_type": "taskUpdated" and include parent_type/parent_id so the consumer knows what the task belongs to. Task automations for Problem, Change and Release require an Estate or Forest plan. |
| Ticket Closed | `ticketClosed` | Fires when a ticket is closed. SETUP: Workflow Automator &gt; New Automator &gt; Ticket module. Event = 'Ticket is updated' on the Status property with a Condition 'Status is Closed', then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED; set "event_type": "ticketClosed". |
| Ticket Created | `ticketCreated` | Fires when a new ticket (incident or service request) is raised in Freshservice. SETUP: Admin &gt; Automation & Productivity &gt; Automation &gt; Workflow Automator &gt; New Automator &gt; choose the Ticket module. Set the Event to 'Ticket is raised', add any Conditions you want to narrow the rule, then add an Action &gt; 'Trigger Webhook'. Set Request Type = POST, Callback URL = this fastn webhook URL, Encoding = JSON, and Content = Advanced (Custom JSON). PAYLOAD IS RULE-DEFINED: Freshservice does not send a fixed payload - whatever JSON you compose in the rule (Simple mode = the ticket properties you tick; Advanced mode = your own JSON built from placeholders) is exactly what arrives. To route this event correctly you MUST include the literal field "event_type": "ticketCreated" in the Advanced JSON, because fastn reads the event type from the 'event_type' payload field. The schema below is the recommended field set built from the Freshservice v2 Ticket object - map each key from the matching placeholder (e.g. AUTH: optionally tick 'Requires Authentication' on the webhook and supply Username/Password (HTTP Basic) or an API key header. Freshservice does not HMAC-sign outbound webhooks. LIMITS: 1000 webhook calls per hour; a non-2xx/3xx response or a response slower than 15s is retried up to 4 times at 3, 5, 9 and 17 minute intervals. |
| Ticket Note Added | `ticketNoteAdded` | Fires when a public reply or private note is added to a ticket. SETUP: Workflow Automator &gt; New Automator &gt; Ticket module. Event = 'Note is added' (choose public, private or both), then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED - the note body and author are only delivered if you map the note placeholders into the Advanced JSON. Set "event_type": "ticketNoteAdded". |
| Ticket Priority Changed | `ticketPriorityChanged` | Fires when a ticket's priority is changed. SETUP: Workflow Automator &gt; New Automator &gt; Ticket module. Event = 'Ticket is updated' scoped to the 'Priority' property, then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED; include "event_type": "ticketPriorityChanged" and map previous_priority yourself if you need the old value. |
| Ticket Resolved | `ticketResolved` | Fires when a ticket is marked Resolved. SETUP: Workflow Automator &gt; New Automator &gt; Ticket module. Event = 'Ticket is updated' on the Status property, add a Condition 'Status is Resolved', then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced) with this fastn webhook URL. PAYLOAD IS RULE-DEFINED; set "event_type": "ticketResolved" and include the resolution/closure fields you need. |
| Ticket Status Changed | `ticketStatusChanged` | Fires when a ticket moves between statuses (for example Open to Pending). SETUP: Workflow Automator &gt; New Automator &gt; Ticket module. Event = 'Ticket is updated' and select the 'Status' property so the rule only runs on status transitions; then Action &gt; 'Trigger Webhook' (POST, JSON, Advanced content) pointing at this fastn webhook URL. PAYLOAD IS RULE-DEFINED. Freshservice does not automatically include the previous value, so add it explicitly in the Advanced JSON using the from/to placeholders exposed by the status event, and set "event_type": "ticketStatusChanged". |
| Ticket Updated | `ticketUpdated` | Fires when any ticket property is changed. SETUP: Admin &gt; Automation & Productivity &gt; Automation &gt; Workflow Automator &gt; New Automator &gt; Ticket module. Event = 'Ticket is updated' (optionally scope it to the specific properties you care about), then Action &gt; 'Trigger Webhook' with Request Type = POST, Callback URL = this fastn webhook URL, Encoding = JSON, Content = Advanced. PAYLOAD IS RULE-DEFINED - it contains exactly the fields you place in the rule's JSON, nothing more. Include "event_type": "ticketUpdated" so fastn can identify the event. The schema below is the recommended field set from the Freshservice v2 Ticket object. |
