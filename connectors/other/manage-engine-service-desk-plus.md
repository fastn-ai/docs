---
description: "ManageEngine ServiceDesk Plus Cloud IT service management - requests, problems, changes, releases, projects, assets, CMDB, purchase orders, contracts,…"
hidden: true
---

# ManageEngine ServiceDesk Plus

<img src="../../.gitbook/assets/connectors/lg/manage-engine-service-desk-plus.png" alt="ManageEngine ServiceDesk Plus logo">

ManageEngine ServiceDesk Plus Cloud IT service management - requests, problems, changes, releases, projects, assets, CMDB, purchase orders, contracts, solutions, users and administration via the SDP Cloud API v3.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [manageengine.com](https://manageengine.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `manageEngineServiceDeskPlus` |

## Use it

Add ManageEngine ServiceDesk Plus from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.manageEngineServiceDeskPlus.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Approve Change | `approveChange` | Approves the specified change approval on behalf of the approver. |
| Approve Problem | `approveProblem` | Approves the specified problem approval on behalf of the approver. |
| Approve Release | `approveRelease` | Approves the specified release approval on behalf of the approver. |
| Approve Request | `approveRequest` | Approves the specified request approval on behalf of the approver. |
| Approve Solution | `approveSolution` | Approves a solution so it can be published to the knowledge base. |
| Cancel Contract | `cancelContract` | Cancels an active contract. |
| Cancel Purchase Order | `cancelPurchaseOrder` | Cancels a purchase order. |
| Copy Checklist Template | `copyChecklistTemplate` | Creates a copy of an existing checklist template. |
| Create Announcement | `createAnnouncement` | Creates a new announcement in ManageEngine ServiceDesk Plus. |
| Create Announcement Comment | `createAnnouncementComment` | Creates a new announcement comment in ManageEngine ServiceDesk Plus. |

<details>

<summary>See 419 more actions</summary>

* **Create Asset** `createAsset`: Creates a new asset in ManageEngine ServiceDesk Plus.
* **Create Change** `createChange`: Creates a new change in ManageEngine ServiceDesk Plus.
* **Create Change Approval** `createChangeApproval`: Adds an approver to an approval level of a change.
* **Create Change Approval Level** `createChangeApprovalLevel`: Creates a new approval level on a change.
* **Create Change Maintenance** `createChangeMaintenance`: Creates a new change maintenance in ManageEngine ServiceDesk Plus.
* **Create Change Note** `createChangeNote`: Creates a new change note in ManageEngine ServiceDesk Plus.
* **Create Change Risk** `createChangeRisk`: Creates a new change risk in ManageEngine ServiceDesk Plus.
* **Create Change Task** `createChangeTask`: Creates a new change task in ManageEngine ServiceDesk Plus.
* **Create Change Task Worklog** `createChangeTaskWorklog`: Creates a new change task worklog in ManageEngine ServiceDesk Plus.
* **Create Change Type** `createChangeType`: Creates a new change type in ManageEngine ServiceDesk Plus.
* **Create Change Worklog** `createChangeWorklog`: Creates a new change worklog in ManageEngine ServiceDesk Plus.
* **Create Checklist Template** `createChecklistTemplate`: Creates a new checklist template in ManageEngine ServiceDesk Plus.
* **Create CI Relationship** `createCIRelationship`: Creates a relationship between a configuration item and another CI.
* **Create Closure Code** `createClosureCode`: Creates a new closure code in ManageEngine ServiceDesk Plus.
* **Create Configuration Item** `createConfigurationItem`: Creates a configuration item of the given CI type in the CMDB.
* **Create Contract** `createContract`: Creates a new contract in ManageEngine ServiceDesk Plus.
* **Create Contract Note** `createContractNote`: Creates a new contract note in ManageEngine ServiceDesk Plus.
* **Create Contract Type** `createContractType`: Creates a new contract type in ManageEngine ServiceDesk Plus.
* **Create Custom Module Record** `createCustomModuleRecord`: Creates a record in the specified custom module.
* **Create Item Detail** `createItemDetail`: Creates a new item detail in ManageEngine ServiceDesk Plus.
* **Create Milestone** `createMilestone`: Creates a new milestone in ManageEngine ServiceDesk Plus.
* **Create Milestone Comment** `createMilestoneComment`: Creates a new milestone comment in ManageEngine ServiceDesk Plus.
* **Create Milestone Task** `createMilestoneTask`: Creates a new milestone task in ManageEngine ServiceDesk Plus.
* **Create Milestone Task Comment** `createMilestoneTaskComment`: Creates a new milestone task comment in ManageEngine ServiceDesk Plus.
* **Create Milestone Task Worklog** `createMilestoneTaskWorklog`: Creates a new milestone task worklog in ManageEngine ServiceDesk Plus.
* **Create Problem** `createProblem`: Creates a new problem in ManageEngine ServiceDesk Plus.
* **Create Problem Approval** `createProblemApproval`: Adds an approver to an approval level of a problem.
* **Create Problem Approval Level** `createProblemApprovalLevel`: Creates a new approval level on a problem.
* **Create Problem Note** `createProblemNote`: Creates a new problem note in ManageEngine ServiceDesk Plus.
* **Create Problem Task** `createProblemTask`: Creates a new problem task in ManageEngine ServiceDesk Plus.
* **Create Problem Task Worklog** `createProblemTaskWorklog`: Creates a new problem task worklog in ManageEngine ServiceDesk Plus.
* **Create Problem Worklog** `createProblemWorklog`: Creates a new problem worklog in ManageEngine ServiceDesk Plus.
* **Create Product** `createProduct`: Creates a new product in ManageEngine ServiceDesk Plus.
* **Create Product Type** `createProductType`: Creates a new product type in ManageEngine ServiceDesk Plus.
* **Create Project** `createProject`: Creates a new project in ManageEngine ServiceDesk Plus.
* **Create Project Comment** `createProjectComment`: Creates a new project comment in ManageEngine ServiceDesk Plus.
* **Create Project Member** `createProjectMember`: Creates a new project member in ManageEngine ServiceDesk Plus.
* **Create Project Status** `createProjectStatus`: Creates a new project status in ManageEngine ServiceDesk Plus.
* **Create Project Task** `createProjectTask`: Creates a new project task in ManageEngine ServiceDesk Plus.
* **Create Project Task Comment** `createProjectTaskComment`: Creates a new project task comment in ManageEngine ServiceDesk Plus.
* **Create Project Task Worklog** `createProjectTaskWorklog`: Creates a new project task worklog in ManageEngine ServiceDesk Plus.
* **Create Project Type** `createProjectType`: Creates a new project type in ManageEngine ServiceDesk Plus.
* **Create Purchase Order** `createPurchaseOrder`: Creates a new purchase order in ManageEngine ServiceDesk Plus.
* **Create Purchase Order Note** `createPurchaseOrderNote`: Creates a new purchase order note in ManageEngine ServiceDesk Plus.
* **Create Reason For Change** `createReasonForChange`: Creates a new reason for change in ManageEngine ServiceDesk Plus.
* **Create Release** `createRelease`: Creates a new release in ManageEngine ServiceDesk Plus.
* **Create Release Approval** `createReleaseApproval`: Adds an approver to an approval level of a release.
* **Create Release Approval Level** `createReleaseApprovalLevel`: Creates a new approval level on a release.
* **Create Release Note** `createReleaseNote`: Creates a new release note in ManageEngine ServiceDesk Plus.
* **Create Release Task** `createReleaseTask`: Creates a new release task in ManageEngine ServiceDesk Plus.
* **Create Release Task Worklog** `createReleaseTaskWorklog`: Creates a new release task worklog in ManageEngine ServiceDesk Plus.
* **Create Release Worklog** `createReleaseWorklog`: Creates a new release worklog in ManageEngine ServiceDesk Plus.
* **Create Request** `createRequest`: Creates a new request in ManageEngine ServiceDesk Plus.
* **Create Request Approval** `createRequestApproval`: Adds an approver to an approval level of a request.
* **Create Request Approval Level** `createRequestApprovalLevel`: Creates a new approval level on a request.
* **Create Request Checklist** `createRequestChecklist`: Attaches a checklist to a request.
* **Create Request Checklist Item** `createRequestChecklistItem`: Adds an item to a checklist on a request.
* **Create Request Maintenance** `createRequestMaintenance`: Creates a new request maintenance in ManageEngine ServiceDesk Plus.
* **Create Request Note** `createRequestNote`: Creates a new request note in ManageEngine ServiceDesk Plus.
* **Create Request Task** `createRequestTask`: Creates a new request task in ManageEngine ServiceDesk Plus.
* **Create Request Worklog** `createRequestWorklog`: Creates a new request worklog in ManageEngine ServiceDesk Plus.
* **Create Solution** `createSolution`: Creates a new solution in ManageEngine ServiceDesk Plus.
* **Create Solution Comment** `createSolutionComment`: Creates a new solution comment in ManageEngine ServiceDesk Plus.
* **Create Solution Relation** `createSolutionRelation`: Relates another resource to a solution.
* **Create Task** `createTask`: Creates a new task in ManageEngine ServiceDesk Plus.
* **Create Template Checklist Association** `createTemplateChecklistAssociation`: Associates a checklist template with a request template.
* **Create Topic** `createTopic`: Creates a new topic in ManageEngine ServiceDesk Plus.
* **Create Unavailability** `createUnavailability`: Creates a new unavailability in ManageEngine ServiceDesk Plus.
* **Delete Announcement** `deleteAnnouncement`: Deletes the specified announcement from ManageEngine ServiceDesk Plus.
* **Delete Announcement Comment** `deleteAnnouncementComment`: Deletes the specified announcement comment from ManageEngine ServiceDesk Plus.
* **Delete Asset** `deleteAsset`: Deletes the specified asset from ManageEngine ServiceDesk Plus.
* **Delete Change** `deleteChange`: Deletes the specified change from ManageEngine ServiceDesk Plus.
* **Delete Change Approval** `deleteChangeApproval`: Removes an approval from an approval level of a change.
* **Delete Change Approval Level** `deleteChangeApprovalLevel`: Deletes an approval level from a change.
* **Delete Change Maintenance** `deleteChangeMaintenance`: Deletes the specified change maintenance from ManageEngine ServiceDesk Plus.
* **Delete Change Note** `deleteChangeNote`: Deletes the specified change note from ManageEngine ServiceDesk Plus.
* **Delete Change Risk** `deleteChangeRisk`: Deletes the specified change risk from ManageEngine ServiceDesk Plus.
* **Delete Change Task** `deleteChangeTask`: Deletes the specified change task from ManageEngine ServiceDesk Plus.
* **Delete Change Task Worklog** `deleteChangeTaskWorklog`: Deletes the specified change task worklog from ManageEngine ServiceDesk Plus.
* **Delete Change Type** `deleteChangeType`: Deletes the specified change type from ManageEngine ServiceDesk Plus.
* **Delete Change Worklog** `deleteChangeWorklog`: Deletes the specified change worklog from ManageEngine ServiceDesk Plus.
* **Delete Checklist Template** `deleteChecklistTemplate`: Deletes the specified checklist template from ManageEngine ServiceDesk Plus.
* **Delete Closure Code** `deleteClosureCode`: Deletes the specified closure code from ManageEngine ServiceDesk Plus.
* **Delete Configuration Item** `deleteConfigurationItem`: Deletes a configuration item from the CMDB.
* **Delete Contract** `deleteContract`: Deletes the specified contract from ManageEngine ServiceDesk Plus.
* **Delete Contract Note** `deleteContractNote`: Deletes the specified contract note from ManageEngine ServiceDesk Plus.
* **Delete Contract Type** `deleteContractType`: Deletes the specified contract type from ManageEngine ServiceDesk Plus.
* **Delete Custom Module Record** `deleteCustomModuleRecord`: Deletes a record from the specified custom module.
* **Delete Item Detail** `deleteItemDetail`: Deletes the specified item detail from ManageEngine ServiceDesk Plus.
* **Delete Milestone** `deleteMilestone`: Deletes the specified milestone from ManageEngine ServiceDesk Plus.
* **Delete Milestone Comment** `deleteMilestoneComment`: Deletes the specified milestone comment from ManageEngine ServiceDesk Plus.
* **Delete Milestone Task** `deleteMilestoneTask`: Deletes the specified milestone task from ManageEngine ServiceDesk Plus.
* **Delete Milestone Task Comment** `deleteMilestoneTaskComment`: Deletes the specified milestone task comment from ManageEngine ServiceDesk Plus.
* **Delete Milestone Task Worklog** `deleteMilestoneTaskWorklog`: Deletes the specified milestone task worklog from ManageEngine ServiceDesk Plus.
* **Delete Problem** `deleteProblem`: Deletes the specified problem from ManageEngine ServiceDesk Plus.
* **Delete Problem Approval** `deleteProblemApproval`: Removes an approval from an approval level of a problem.
* **Delete Problem Approval Level** `deleteProblemApprovalLevel`: Deletes an approval level from a problem.
* **Delete Problem Note** `deleteProblemNote`: Deletes the specified problem note from ManageEngine ServiceDesk Plus.
* **Delete Problem Task** `deleteProblemTask`: Deletes the specified problem task from ManageEngine ServiceDesk Plus.
* **Delete Problem Task Worklog** `deleteProblemTaskWorklog`: Deletes the specified problem task worklog from ManageEngine ServiceDesk Plus.
* **Delete Problem Worklog** `deleteProblemWorklog`: Deletes the specified problem worklog from ManageEngine ServiceDesk Plus.
* **Delete Product** `deleteProduct`: Deletes the specified product from ManageEngine ServiceDesk Plus.
* **Delete Product Type** `deleteProductType`: Deletes the specified product type from ManageEngine ServiceDesk Plus.
* **Delete Project** `deleteProject`: Deletes the specified project from ManageEngine ServiceDesk Plus.
* **Delete Project Comment** `deleteProjectComment`: Deletes the specified project comment from ManageEngine ServiceDesk Plus.
* **Delete Project Member** `deleteProjectMember`: Deletes the specified project member from ManageEngine ServiceDesk Plus.
* **Delete Project Status** `deleteProjectStatus`: Deletes the specified project status from ManageEngine ServiceDesk Plus.
* **Delete Project Task** `deleteProjectTask`: Deletes the specified project task from ManageEngine ServiceDesk Plus.
* **Delete Project Task Comment** `deleteProjectTaskComment`: Deletes the specified project task comment from ManageEngine ServiceDesk Plus.
* **Delete Project Task Worklog** `deleteProjectTaskWorklog`: Deletes the specified project task worklog from ManageEngine ServiceDesk Plus.
* **Delete Project Type** `deleteProjectType`: Deletes the specified project type from ManageEngine ServiceDesk Plus.
* **Delete Purchase Order** `deletePurchaseOrder`: Deletes the specified purchase order from ManageEngine ServiceDesk Plus.
* **Delete Purchase Order Note** `deletePurchaseOrderNote`: Deletes the specified purchase order note from ManageEngine ServiceDesk Plus.
* **Delete Reason For Change** `deleteReasonForChange`: Deletes the specified reason for change from ManageEngine ServiceDesk Plus.
* **Delete Release** `deleteRelease`: Deletes the specified release from ManageEngine ServiceDesk Plus.
* **Delete Release Approval** `deleteReleaseApproval`: Removes an approval from an approval level of a release.
* **Delete Release Approval Level** `deleteReleaseApprovalLevel`: Deletes an approval level from a release.
* **Delete Release Note** `deleteReleaseNote`: Deletes the specified release note from ManageEngine ServiceDesk Plus.
* **Delete Release Task** `deleteReleaseTask`: Deletes the specified release task from ManageEngine ServiceDesk Plus.
* **Delete Release Task Worklog** `deleteReleaseTaskWorklog`: Deletes the specified release task worklog from ManageEngine ServiceDesk Plus.
* **Delete Release Worklog** `deleteReleaseWorklog`: Deletes the specified release worklog from ManageEngine ServiceDesk Plus.
* **Delete Request** `deleteRequest`: Deletes the specified request from ManageEngine ServiceDesk Plus.
* **Delete Request Approval** `deleteRequestApproval`: Removes an approval from an approval level of a request.
* **Delete Request Approval Level** `deleteRequestApprovalLevel`: Deletes an approval level from a request.
* **Delete Request Checklist** `deleteRequestChecklist`: Removes a checklist from a request.
* **Delete Request Maintenance** `deleteRequestMaintenance`: Deletes the specified request maintenance from ManageEngine ServiceDesk Plus.
* **Delete Request Note** `deleteRequestNote`: Deletes the specified request note from ManageEngine ServiceDesk Plus.
* **Delete Request Task** `deleteRequestTask`: Deletes the specified request task from ManageEngine ServiceDesk Plus.
* **Delete Request Worklog** `deleteRequestWorklog`: Deletes the specified request worklog from ManageEngine ServiceDesk Plus.
* **Delete Solution** `deleteSolution`: Deletes the specified solution from ManageEngine ServiceDesk Plus.
* **Delete Solution Comment** `deleteSolutionComment`: Deletes the specified solution comment from ManageEngine ServiceDesk Plus.
* **Delete Solution Relation** `deleteSolutionRelation`: Removes a relation from a solution.
* **Delete Task** `deleteTask`: Deletes the specified task from ManageEngine ServiceDesk Plus.
* **Delete Template Checklist Association** `deleteTemplateChecklistAssociation`: Removes a checklist association from a request template.
* **Delete Topic** `deleteTopic`: Deletes the specified topic from ManageEngine ServiceDesk Plus.
* **Delete Unavailability** `deleteUnavailability`: Deletes the specified unavailability from ManageEngine ServiceDesk Plus.
* **Dislike Solution** `dislikeSolution`: Records a dislike against a solution on behalf of the current user.
* **Email Contract Owner** `emailContractOwner`: Sends the contract details to its owner by email.
* **Email Contract Vendor** `emailContractVendor`: Sends the contract details to the vendor by email.
* **Email Purchase Order Owner** `emailPurchaseOrderOwner`: Sends the purchase order details to its owner by email.
* **Email Purchase Order Vendor** `emailPurchaseOrderVendor`: Sends the purchase order details to the vendor by email.
* **Enable Change Maintenance** `enableChangeMaintenance`: Enables a suspended change maintenance schedule.
* **Enable Request Maintenance** `enableRequestMaintenance`: Enables a suspended request maintenance schedule.
* **Exclude Request Checklist Item** `excludeRequestChecklistItem`: Excludes a checklist item from a request checklist.
* **Execute Change Maintenance Now** `executeChangeMaintenanceNow`: Triggers the change maintenance schedule to run immediately.
* **Execute Request Maintenance Now** `executeRequestMaintenanceNow`: Triggers the request maintenance schedule to run immediately.
* **Follow Announcement** `followAnnouncement`: Subscribes the current user to updates on an announcement.
* **Get Announcement** `getAnnouncement`: Retrieves the full details of a single announcement by its identifier.
* **Get Announcement Comment** `getAnnouncementComment`: Retrieves the full details of a single announcement comment by its identifier.
* **Get Archived Request Checklist** `getArchivedRequestChecklist`: Retrieves a single checklist attached to an archived request.
* **Get Asset** `getAsset`: Retrieves the full details of a single asset by its identifier.
* **Get Change** `getChange`: Retrieves the full details of a single change by its identifier.
* **Get Change Approval** `getChangeApproval`: Retrieves a single approval of a change.
* **Get Change Approval Level** `getChangeApprovalLevel`: Retrieves a single approval level of a change.
* **Get Change Maintenance** `getChangeMaintenance`: Retrieves the full details of a single change maintenance by its identifier.
* **Get Change Note** `getChangeNote`: Retrieves the full details of a single change note by its identifier.
* **Get Change Risk** `getChangeRisk`: Retrieves the full details of a single change risk by its identifier.
* **Get Change Task** `getChangeTask`: Retrieves the full details of a single change task by its identifier.
* **Get Change Task Worklog** `getChangeTaskWorklog`: Retrieves the full details of a single change task worklog by its identifier.
* **Get Change Type** `getChangeType`: Retrieves the full details of a single change type by its identifier.
* **Get Change Worklog** `getChangeWorklog`: Retrieves the full details of a single change worklog by its identifier.
* **Get Checklist Template** `getChecklistTemplate`: Retrieves the full details of a single checklist template by its identifier.
* **Get Checklist Template Associations** `getChecklistTemplateAssociations`: Retrieves the request templates a checklist template is associated with.
* **Get Closure Code** `getClosureCode`: Retrieves the full details of a single closure code by its identifier.
* **Get Configuration Item** `getConfigurationItem`: Retrieves a single configuration item from the CMDB by its identifier.
* **Get Contract** `getContract`: Retrieves the full details of a single contract by its identifier.
* **Get Contract Note** `getContractNote`: Retrieves the full details of a single contract note by its identifier.
* **Get Contract Type** `getContractType`: Retrieves the full details of a single contract type by its identifier.
* **Get Custom Module Record** `getCustomModuleRecord`: Retrieves a single custom module record by its identifier.
* **Get Item Detail** `getItemDetail`: Retrieves the full details of a single item detail by its identifier.
* **Get Milestone** `getMilestone`: Retrieves the full details of a single milestone by its identifier.
* **Get Milestone Comment** `getMilestoneComment`: Retrieves the full details of a single milestone comment by its identifier.
* **Get Milestone Task** `getMilestoneTask`: Retrieves the full details of a single milestone task by its identifier.
* **Get Milestone Task Comment** `getMilestoneTaskComment`: Retrieves the full details of a single milestone task comment by its identifier.
* **Get Milestone Task Worklog** `getMilestoneTaskWorklog`: Retrieves the full details of a single milestone task worklog by its identifier.
* **Get Milestone Timesheet** `getMilestoneTimesheet`: Retrieves the aggregated timesheet for a milestone.
* **Get Problem** `getProblem`: Retrieves the full details of a single problem by its identifier.
* **Get Problem Approval** `getProblemApproval`: Retrieves a single approval of a problem.
* **Get Problem Approval Level** `getProblemApprovalLevel`: Retrieves a single approval level of a problem.
* **Get Problem Note** `getProblemNote`: Retrieves the full details of a single problem note by its identifier.
* **Get Problem Task** `getProblemTask`: Retrieves the full details of a single problem task by its identifier.
* **Get Problem Task Worklog** `getProblemTaskWorklog`: Retrieves the full details of a single problem task worklog by its identifier.
* **Get Problem Worklog** `getProblemWorklog`: Retrieves the full details of a single problem worklog by its identifier.
* **Get Product** `getProduct`: Retrieves the full details of a single product by its identifier.
* **Get Product Type** `getProductType`: Retrieves the full details of a single product type by its identifier.
* **Get Project** `getProject`: Retrieves the full details of a single project by its identifier.
* **Get Project Comment** `getProjectComment`: Retrieves the full details of a single project comment by its identifier.
* **Get Project Member** `getProjectMember`: Retrieves the full details of a single project member by its identifier.
* **Get Project Status** `getProjectStatus`: Retrieves the full details of a single project status by its identifier.
* **Get Project Task** `getProjectTask`: Retrieves the full details of a single project task by its identifier.
* **Get Project Task Comment** `getProjectTaskComment`: Retrieves the full details of a single project task comment by its identifier.
* **Get Project Task Worklog** `getProjectTaskWorklog`: Retrieves the full details of a single project task worklog by its identifier.
* **Get Project Timesheet** `getProjectTimesheet`: Retrieves the aggregated timesheet for a project.
* **Get Project Type** `getProjectType`: Retrieves the full details of a single project type by its identifier.
* **Get Purchase Order** `getPurchaseOrder`: Retrieves the full details of a single purchase order by its identifier.
* **Get Purchase Order Note** `getPurchaseOrderNote`: Retrieves the full details of a single purchase order note by its identifier.
* **Get Reason For Change** `getReasonForChange`: Retrieves the full details of a single reason for change by its identifier.
* **Get Release** `getRelease`: Retrieves the full details of a single release by its identifier.
* **Get Release Approval** `getReleaseApproval`: Retrieves a single approval of a release.
* **Get Release Approval Level** `getReleaseApprovalLevel`: Retrieves a single approval level of a release.
* **Get Release Note** `getReleaseNote`: Retrieves the full details of a single release note by its identifier.
* **Get Release Task** `getReleaseTask`: Retrieves the full details of a single release task by its identifier.
* **Get Release Task Worklog** `getReleaseTaskWorklog`: Retrieves the full details of a single release task worklog by its identifier.
* **Get Release Worklog** `getReleaseWorklog`: Retrieves the full details of a single release worklog by its identifier.
* **Get Request** `getRequest`: Retrieves the full details of a single request by its identifier.
* **Get Request Approval** `getRequestApproval`: Retrieves a single approval of a request.
* **Get Request Approval Level** `getRequestApprovalLevel`: Retrieves a single approval level of a request.
* **Get Request Checklist** `getRequestChecklist`: Retrieves a single checklist attached to a request.
* **Get Request Checklist Item** `getRequestChecklistItem`: Retrieves a single checklist item on a request.
* **Get Request Maintenance** `getRequestMaintenance`: Retrieves the full details of a single request maintenance by its identifier.
* **Get Request Note** `getRequestNote`: Retrieves the full details of a single request note by its identifier.
* **Get Request Task** `getRequestTask`: Retrieves the full details of a single request task by its identifier.
* **Get Request Worklog** `getRequestWorklog`: Retrieves the full details of a single request worklog by its identifier.
* **Get Solution** `getSolution`: Retrieves the full details of a single solution by its identifier.
* **Get Solution Comment** `getSolutionComment`: Retrieves the full details of a single solution comment by its identifier.
* **Get Task** `getTask`: Retrieves the full details of a single task by its identifier.
* **Get Template Checklist Association** `getTemplateChecklistAssociation`: Retrieves a single checklist association of a request template.
* **Get Topic** `getTopic`: Retrieves the full details of a single topic by its identifier.
* **Get Unavailability** `getUnavailability`: Retrieves the full details of a single unavailability by its identifier.
* **Include Request Checklist Item** `includeRequestChecklistItem`: Includes a previously excluded checklist item on a request.
* **Like Solution** `likeSolution`: Records a like against a solution on behalf of the current user.
* **List Announcement Comments** `listAnnouncementComments`: Retrieves a paginated list of announcement comment records from ManageEngine ServiceDesk Plus.
* **List Announcements** `listAnnouncements`: Retrieves a paginated list of announcement records from ManageEngine ServiceDesk Plus.
* **List Archived Request Checklists** `listArchivedRequestChecklists`: Retrieves the checklists attached to an archived request.
* **List Archived Requests** `listArchivedRequests`: Retrieves the configured archived request records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Asset States** `listAssetStates`: Retrieves the configured asset state records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Assets** `listAssets`: Retrieves a paginated list of asset records from ManageEngine ServiceDesk Plus.
* **List Categories** `listCategorys`: Retrieves the configured category records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Change Approval Levels** `listChangeApprovalLevels`: Retrieves the approval levels configured on a change.
* **List Change Approvals** `listChangeApprovals`: Retrieves the approvals within an approval level of a change.
* **List Change Maintenances** `listChangeMaintenances`: Retrieves a paginated list of change maintenance records from ManageEngine ServiceDesk Plus.
* **List Change Notes** `listChangeNotes`: Retrieves a paginated list of change note records from ManageEngine ServiceDesk Plus.
* **List Change Risks** `listChangeRisks`: Retrieves a paginated list of change risk records from ManageEngine ServiceDesk Plus.
* **List Change Stages** `listChangeStages`: Retrieves the configured change stage records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Change Statuses** `listChangeStatus`: Retrieves the configured change status records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Change Task Worklogs** `listChangeTaskWorklogs`: Retrieves a paginated list of change task worklog records from ManageEngine ServiceDesk Plus.
* **List Change Tasks** `listChangeTasks`: Retrieves a paginated list of change task records from ManageEngine ServiceDesk Plus.
* **List Change Types** `listChangeTypes`: Retrieves a paginated list of change type records from ManageEngine ServiceDesk Plus.
* **List Change Worklogs** `listChangeWorklogs`: Retrieves a paginated list of change worklog records from ManageEngine ServiceDesk Plus.
* **List Changes** `listChanges`: Retrieves a paginated list of change records from ManageEngine ServiceDesk Plus.
* **List Checklist Templates** `listChecklistTemplates`: Retrieves a paginated list of checklist template records from ManageEngine ServiceDesk Plus.
* **List CI Relationships** `listCIRelationships`: Retrieves the relationships defined between a configuration item and other CIs.
* **List CI Types** `listCITypes`: Retrieves the configured ci type records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Closure Codes** `listClosureCodes`: Retrieves a paginated list of closure code records from ManageEngine ServiceDesk Plus.
* **List Configuration Items** `listConfigurationItems`: Retrieves configuration items of a given CI type from the CMDB. The CI type is supplied as its API plural name, for example ci_computer.
* **List Contract Notes** `listContractNotes`: Retrieves a paginated list of contract note records from ManageEngine ServiceDesk Plus.
* **List Contract Types** `listContractTypes`: Retrieves a paginated list of contract type records from ManageEngine ServiceDesk Plus.
* **List Contracts** `listContracts`: Retrieves a paginated list of contract records from ManageEngine ServiceDesk Plus.
* **List Cost Centers** `listCostCenters`: Retrieves the configured cost center records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Currencies** `listCurrencys`: Retrieves the configured currency records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Custom Module Records** `listCustomModuleRecords`: Retrieves records of a custom module, identified by its API plural name.
* **List Custom Modules** `listCustomModules`: Retrieves the configured custom module records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Departments** `listDepartments`: Retrieves the configured department records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Groups** `listGroups`: Retrieves the configured group records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Holidays** `listHolidays`: Retrieves the configured holiday records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Impacts** `listImpacts`: Retrieves the configured impact records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Item Details** `listItemDetails`: Retrieves a paginated list of item detail records from ManageEngine ServiceDesk Plus.
* **List Leave Types** `listLeaveTypes`: Retrieves the configured leave type records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Levels** `listLevels`: Retrieves the configured level records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Milestone Comments** `listMilestoneComments`: Retrieves a paginated list of milestone comment records from ManageEngine ServiceDesk Plus.
* **List Milestone Task Comments** `listMilestoneTaskComments`: Retrieves a paginated list of milestone task comment records from ManageEngine ServiceDesk Plus.
* **List Milestone Task Worklogs** `listMilestoneTaskWorklogs`: Retrieves a paginated list of milestone task worklog records from ManageEngine ServiceDesk Plus.
* **List Milestone Tasks** `listMilestoneTasks`: Retrieves a paginated list of milestone task records from ManageEngine ServiceDesk Plus.
* **List Milestones** `listMilestones`: Retrieves a paginated list of milestone records from ManageEngine ServiceDesk Plus.
* **List Modes** `listModes`: Retrieves the configured mode records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Operational Hours** `listOperationalHours`: Retrieves the configured operational hour records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Priorities** `listPrioritys`: Retrieves the configured priority records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Problem Approval Levels** `listProblemApprovalLevels`: Retrieves the approval levels configured on a problem.
* **List Problem Approvals** `listProblemApprovals`: Retrieves the approvals within an approval level of a problem.
* **List Problem Notes** `listProblemNotes`: Retrieves a paginated list of problem note records from ManageEngine ServiceDesk Plus.
* **List Problem Task Worklogs** `listProblemTaskWorklogs`: Retrieves a paginated list of problem task worklog records from ManageEngine ServiceDesk Plus.
* **List Problem Tasks** `listProblemTasks`: Retrieves a paginated list of problem task records from ManageEngine ServiceDesk Plus.
* **List Problem Worklogs** `listProblemWorklogs`: Retrieves a paginated list of problem worklog records from ManageEngine ServiceDesk Plus.
* **List Problems** `listProblems`: Retrieves a paginated list of problem records from ManageEngine ServiceDesk Plus.
* **List Product Types** `listProductTypes`: Retrieves a paginated list of product type records from ManageEngine ServiceDesk Plus.
* **List Products** `listProducts`: Retrieves a paginated list of product records from ManageEngine ServiceDesk Plus.
* **List Project Comments** `listProjectComments`: Retrieves a paginated list of project comment records from ManageEngine ServiceDesk Plus.
* **List Project Members** `listProjectMembers`: Retrieves a paginated list of project member records from ManageEngine ServiceDesk Plus.
* **List Project Request Associations** `listProjectRequestAssociations`: Retrieves the requests associated with a project.
* **List Project Roles** `listProjectRoles`: Retrieves the configured project role records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Project Statuses** `listProjectStatuss`: Retrieves a paginated list of project status records from ManageEngine ServiceDesk Plus.
* **List Project Task Comments** `listProjectTaskComments`: Retrieves a paginated list of project task comment records from ManageEngine ServiceDesk Plus.
* **List Project Task Worklogs** `listProjectTaskWorklogs`: Retrieves a paginated list of project task worklog records from ManageEngine ServiceDesk Plus.
* **List Project Tasks** `listProjectTasks`: Retrieves a paginated list of project task records from ManageEngine ServiceDesk Plus.
* **List Project Types** `listProjectTypes`: Retrieves a paginated list of project type records from ManageEngine ServiceDesk Plus.
* **List Projects** `listProjects`: Retrieves a paginated list of project records from ManageEngine ServiceDesk Plus.
* **List Purchase Order Notes** `listPurchaseOrderNotes`: Retrieves a paginated list of purchase order note records from ManageEngine ServiceDesk Plus.
* **List Purchase Orders** `listPurchaseOrders`: Retrieves a paginated list of purchase order records from ManageEngine ServiceDesk Plus.
* **List Reason For Changes** `listReasonForChanges`: Retrieves a paginated list of reason for change records from ManageEngine ServiceDesk Plus.
* **List Regions** `listRegions`: Retrieves the configured region records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Release Approval Levels** `listReleaseApprovalLevels`: Retrieves the approval levels configured on a release.
* **List Release Approvals** `listReleaseApprovals`: Retrieves the approvals within an approval level of a release.
* **List Release Notes** `listReleaseNotes`: Retrieves a paginated list of release note records from ManageEngine ServiceDesk Plus.
* **List Release Stages** `listReleaseStages`: Retrieves the configured release stage records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Release Statuses** `listReleaseStatus`: Retrieves the configured release status records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Release Task Worklogs** `listReleaseTaskWorklogs`: Retrieves a paginated list of release task worklog records from ManageEngine ServiceDesk Plus.
* **List Release Tasks** `listReleaseTasks`: Retrieves a paginated list of release task records from ManageEngine ServiceDesk Plus.
* **List Release Worklogs** `listReleaseWorklogs`: Retrieves a paginated list of release worklog records from ManageEngine ServiceDesk Plus.
* **List Releases** `listReleases`: Retrieves a paginated list of release records from ManageEngine ServiceDesk Plus.
* **List Request Approval Levels** `listRequestApprovalLevels`: Retrieves the approval levels configured on a request.
* **List Request Approvals** `listRequestApprovals`: Retrieves the approvals within an approval level of a request.
* **List Request Checklist Items** `listRequestChecklistItems`: Retrieves the items of a checklist attached to a request.
* **List Request Checklists** `listRequestChecklists`: Retrieves the checklists attached to a request.
* **List Request Maintenances** `listRequestMaintenances`: Retrieves a paginated list of request maintenance records from ManageEngine ServiceDesk Plus.
* **List Request Notes** `listRequestNotes`: Retrieves a paginated list of request note records from ManageEngine ServiceDesk Plus.
* **List Request Statuses** `listStatus`: Retrieves the configured status records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Request Tasks** `listRequestTasks`: Retrieves a paginated list of request task records from ManageEngine ServiceDesk Plus.
* **List Request Templates** `listRequestTemplates`: Retrieves the configured request template records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Request Types** `listRequestTypes`: Retrieves the configured request type records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Request Worklogs** `listRequestWorklogs`: Retrieves a paginated list of request worklog records from ManageEngine ServiceDesk Plus.
* **List Requests** `listRequests`: Retrieves a paginated list of request records from ManageEngine ServiceDesk Plus.
* **List Roles** `listRoles`: Retrieves the configured role records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Service Categories** `listServiceCategorys`: Retrieves the configured service category records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Sites** `listSites`: Retrieves the configured site records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List SLAs** `listSLAs`: Retrieves the configured sla records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Software** `listSoftwares`: Retrieves the configured software records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Software Licenses** `listSoftwareLicenses`: Retrieves the configured software license records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Solution Comments** `listSolutionComments`: Retrieves a paginated list of solution comment records from ManageEngine ServiceDesk Plus.
* **List Solution Relations** `listSolutionRelations`: Retrieves the resources related to a solution.
* **List Solution Versions** `listSolutionVersions`: Retrieves the version history of a solution.
* **List Solutions** `listSolutions`: Retrieves a paginated list of solution records from ManageEngine ServiceDesk Plus.
* **List Task Types** `listTaskTypes`: Retrieves the configured task type records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Tasks** `listTasks`: Retrieves a paginated list of task records from ManageEngine ServiceDesk Plus.
* **List Template Checklist Associations** `listTemplateChecklistAssociations`: Retrieves the checklists associated with a request template.
* **List Topics** `listTopics`: Retrieves a paginated list of topic records from ManageEngine ServiceDesk Plus.
* **List Unavailability Records** `listUnavailabilitys`: Retrieves a paginated list of unavailability records from ManageEngine ServiceDesk Plus.
* **List Urgencies** `listUrgencys`: Retrieves the configured urgency records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Vendors** `listVendors`: Retrieves the configured vendor records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **List Worklog Types** `listWorklogTypes`: Retrieves the configured worklog type records from ManageEngine ServiceDesk Plus. Read-only reference data used to populate fields on requests, changes, assets and other modules.
* **Mark Purchase Order As Ordered** `markPurchaseOrderAsOrdered`: Marks a purchase order as ordered with the vendor.
* **Mark Purchase Order Payment Done** `markPurchaseOrderPaymentDone`: Marks the payment for a purchase order as completed.
* **Move Contract To Trash** `moveContractToTrash`: Moves a contract to the trash.
* **Move Custom Module Records To Trash** `moveCustomModuleRecordsToTrash`: Moves the specified custom module records to the trash.
* **Move Purchase Order To Trash** `movePurchaseOrderToTrash`: Moves a purchase order to the trash.
* **Publish Solution** `publishSolution`: Publishes an approved solution to the knowledge base.
* **Receive Purchase Order Invoice** `receivePurchaseOrderInvoice`: Records receipt of the vendor invoice for a purchase order.
* **Receive Purchase Order Items** `receivePurchaseOrderItems`: Records receipt of the items ordered on a purchase order.
* **Reject Change Approval** `rejectChangeApproval`: Rejects the specified change approval with a comment.
* **Reject Problem Approval** `rejectProblemApproval`: Rejects the specified problem approval with a comment.
* **Reject Release Approval** `rejectReleaseApproval`: Rejects the specified release approval with a comment.
* **Reject Request Approval** `rejectRequestApproval`: Rejects the specified request approval with a comment.
* **Reject Solution** `rejectSolution`: Rejects a solution that was submitted for approval.
* **Renew Contract** `renewContract`: Renews a contract for a further term.
* **Restore And Approve Solution Version** `restoreAndApproveSolutionVersion`: Restores a previous version of a solution and approves it in one operation.
* **Restore Contract From Trash** `restoreContractFromTrash`: Restores a contract from the trash.
* **Restore Custom Module Records From Trash** `restoreCustomModuleRecordsFromTrash`: Restores the specified custom module records from the trash.
* **Restore Purchase Order From Trash** `restorePurchaseOrderFromTrash`: Restores a purchase order from the trash.
* **Restore Solution Version** `restoreSolutionVersion`: Restores a previous version of a solution.
* **Send Change Approval Notification** `sendChangeApprovalNotification`: Sends the approval notification email to the approver of a change.
* **Send Problem Approval Notification** `sendProblemApprovalNotification`: Sends the approval notification email to the approver of a problem.
* **Send Release Approval Notification** `sendReleaseApprovalNotification`: Sends the approval notification email to the approver of a release.
* **Send Request Approval Notification** `sendRequestApprovalNotification`: Sends the approval notification email to the approver of a request.
* **Submit Purchase Order For Approval** `submitPurchaseOrderForApproval`: Submits a purchase order into its approval workflow.
* **Suspend Change Maintenance** `suspendChangeMaintenance`: Suspends an active change maintenance schedule.
* **Suspend Request Maintenance** `suspendRequestMaintenance`: Suspends an active request maintenance schedule.
* **Unfollow Announcement** `unfollowAnnouncement`: Unsubscribes the current user from updates on an announcement.
* **Update Announcement** `updateAnnouncement`: Updates an existing announcement with the supplied field values.
* **Update Announcement Comment** `updateAnnouncementComment`: Updates an existing announcement comment with the supplied field values.
* **Update Asset** `updateAsset`: Updates an existing asset with the supplied field values.
* **Update Change** `updateChange`: Updates an existing change with the supplied field values.
* **Update Change Approval Level** `updateChangeApprovalLevel`: Updates an approval level of a change.
* **Update Change Maintenance** `updateChangeMaintenance`: Updates an existing change maintenance with the supplied field values.
* **Update Change Note** `updateChangeNote`: Updates an existing change note with the supplied field values.
* **Update Change Risk** `updateChangeRisk`: Updates an existing change risk with the supplied field values.
* **Update Change Task** `updateChangeTask`: Updates an existing change task with the supplied field values.
* **Update Change Task Worklog** `updateChangeTaskWorklog`: Updates an existing change task worklog with the supplied field values.
* **Update Change Type** `updateChangeType`: Updates an existing change type with the supplied field values.
* **Update Change Worklog** `updateChangeWorklog`: Updates an existing change worklog with the supplied field values.
* **Update Checklist Template** `updateChecklistTemplate`: Updates an existing checklist template with the supplied field values.
* **Update Closure Code** `updateClosureCode`: Updates an existing closure code with the supplied field values.
* **Update Configuration Item** `updateConfigurationItem`: Updates a configuration item in the CMDB.
* **Update Contract** `updateContract`: Updates an existing contract with the supplied field values.
* **Update Contract Note** `updateContractNote`: Updates an existing contract note with the supplied field values.
* **Update Contract Type** `updateContractType`: Updates an existing contract type with the supplied field values.
* **Update Custom Module Record** `updateCustomModuleRecord`: Updates a record in the specified custom module.
* **Update Item Detail** `updateItemDetail`: Updates an existing item detail with the supplied field values.
* **Update Milestone** `updateMilestone`: Updates an existing milestone with the supplied field values.
* **Update Milestone Comment** `updateMilestoneComment`: Updates an existing milestone comment with the supplied field values.
* **Update Milestone Task** `updateMilestoneTask`: Updates an existing milestone task with the supplied field values.
* **Update Milestone Task Comment** `updateMilestoneTaskComment`: Updates an existing milestone task comment with the supplied field values.
* **Update Milestone Task Worklog** `updateMilestoneTaskWorklog`: Updates an existing milestone task worklog with the supplied field values.
* **Update Problem** `updateProblem`: Updates an existing problem with the supplied field values.
* **Update Problem Approval Level** `updateProblemApprovalLevel`: Updates an approval level of a problem.
* **Update Problem Note** `updateProblemNote`: Updates an existing problem note with the supplied field values.
* **Update Problem Task** `updateProblemTask`: Updates an existing problem task with the supplied field values.
* **Update Problem Task Worklog** `updateProblemTaskWorklog`: Updates an existing problem task worklog with the supplied field values.
* **Update Problem Worklog** `updateProblemWorklog`: Updates an existing problem worklog with the supplied field values.
* **Update Product** `updateProduct`: Updates an existing product with the supplied field values.
* **Update Product Type** `updateProductType`: Updates an existing product type with the supplied field values.
* **Update Project** `updateProject`: Updates an existing project with the supplied field values.
* **Update Project Comment** `updateProjectComment`: Updates an existing project comment with the supplied field values.
* **Update Project Member** `updateProjectMember`: Updates an existing project member with the supplied field values.
* **Update Project Status** `updateProjectStatus`: Updates an existing project status with the supplied field values.
* **Update Project Task** `updateProjectTask`: Updates an existing project task with the supplied field values.
* **Update Project Task Comment** `updateProjectTaskComment`: Updates an existing project task comment with the supplied field values.
* **Update Project Task Worklog** `updateProjectTaskWorklog`: Updates an existing project task worklog with the supplied field values.
* **Update Project Type** `updateProjectType`: Updates an existing project type with the supplied field values.
* **Update Purchase Order** `updatePurchaseOrder`: Updates an existing purchase order with the supplied field values.
* **Update Purchase Order Note** `updatePurchaseOrderNote`: Updates an existing purchase order note with the supplied field values.
* **Update Reason For Change** `updateReasonForChange`: Updates an existing reason for change with the supplied field values.
* **Update Release** `updateRelease`: Updates an existing release with the supplied field values.
* **Update Release Approval Level** `updateReleaseApprovalLevel`: Updates an approval level of a release.
* **Update Release Note** `updateReleaseNote`: Updates an existing release note with the supplied field values.
* **Update Release Task** `updateReleaseTask`: Updates an existing release task with the supplied field values.
* **Update Release Task Worklog** `updateReleaseTaskWorklog`: Updates an existing release task worklog with the supplied field values.
* **Update Release Worklog** `updateReleaseWorklog`: Updates an existing release worklog with the supplied field values.
* **Update Request** `updateRequest`: Updates an existing request with the supplied field values.
* **Update Request Approval Level** `updateRequestApprovalLevel`: Updates an approval level of a request.
* **Update Request Checklist** `updateRequestChecklist`: Updates a checklist attached to a request.
* **Update Request Checklist Item** `updateRequestChecklistItem`: Updates a checklist item on a request.
* **Update Request Maintenance** `updateRequestMaintenance`: Updates an existing request maintenance with the supplied field values.
* **Update Request Note** `updateRequestNote`: Updates an existing request note with the supplied field values.
* **Update Request Task** `updateRequestTask`: Updates an existing request task with the supplied field values.
* **Update Request Worklog** `updateRequestWorklog`: Updates an existing request worklog with the supplied field values.
* **Update Solution** `updateSolution`: Updates an existing solution with the supplied field values.
* **Update Solution Comment** `updateSolutionComment`: Updates an existing solution comment with the supplied field values.
* **Update Task** `updateTask`: Updates an existing task with the supplied field values.
* **Update Topic** `updateTopic`: Updates an existing topic with the supplied field values.
* **Update Unavailability** `updateUnavailability`: Updates an existing unavailability with the supplied field values.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Asset Created | `asset.created` | Fires when a new asset is added to the asset inventory. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Assets", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "asset.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Assets" in the module drop-down, click New Trigger. Set the execution event to Created. Under "Applies to" select All Assets, or a specific Product Type to scope the trigger. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save. |
| Asset Deleted | `asset.deleted` | Fires when an asset is deleted from the inventory. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Assets", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "asset.deleted". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Assets" in the module drop-down, click New Trigger. Set the execution event to Deleted. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save. |
| Asset Updated | `asset.edited` | Fires when an asset record changes - state, assigned user, department, location or any custom field. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Assets", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "asset.edited". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Assets" in the module drop-down, click New Trigger. Set the execution event to Edited. Under "Applies to" select All Assets or a specific Product Type. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save. |
| Change Approval Actioned | `change.approval.actioned` | Fires when an approver approves or rejects a change approval. Uses the Approvals sub-entity of the Changes trigger module. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Changes", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "change.approval.actioned". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Changes" in the module drop-down, click New Trigger. Set the execution event to Edited, with the sub-entity set to Approvals. Add the criteria Approval Status is Approved or Rejected. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save. |
| Change Created | `change.created` | Fires when a new change request is raised. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Changes", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "change.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Changes" in the module drop-down, click New Trigger. Set the execution event to Created. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save. |
| Change Deleted | `change.deleted` | Fires when a change request is deleted. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Changes", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "change.deleted". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Changes" in the module drop-down, click New Trigger. Set the execution event to Deleted. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save. |
| Change Task Created | `change.task.created` | Fires when a task is added to a change. Uses the Tasks sub-entity of the Changes trigger module. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Changes", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "change.task.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Changes" in the module drop-down, click New Trigger. Set the execution event to Created, with the sub-entity set to Tasks. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save. |
| Change Updated | `change.edited` | Fires when an existing change is modified, including stage and status transitions through the change workflow. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Changes", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "change.edited". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Changes" in the module drop-down, click New Trigger. Set the execution event to Edited. Add a criteria on Stage or Status to narrow it to a specific transition, or leave it empty for all edits. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save. |
| Configuration Item Created | `ci.created` | Fires when a new configuration item is added to the CMDB. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "CMDB", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "ci.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for CMDB" in the module drop-down, click New Trigger. Set the execution event to Created. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save. |
| Configuration Item Deleted | `ci.deleted` | Fires when a configuration item is deleted from the CMDB. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "CMDB", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "ci.deleted". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for CMDB" in the module drop-down, click New Trigger. Set the execution event to Deleted. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save. |

<details>

<summary>See 28 more events</summary>

* **Configuration Item Updated** `ci.edited`: Fires when a configuration item or one of its relationships is modified. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "CMDB", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "ci.edited". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for CMDB" in the module drop-down, click New Trigger. Set the execution event to Edited. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Contract Created** `contract.created`: Fires when a new contract is created. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Contracts", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "contract.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Contracts" in the module drop-down, click New Trigger. Set the execution event to Created. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Contract Deleted** `contract.deleted`: Fires when a contract is deleted. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Contracts", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "contract.deleted". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Contracts" in the module drop-down, click New Trigger. Set the execution event to Deleted. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Contract Updated** `contract.edited`: Fires when a contract is modified, including renewal and expiry status changes. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Contracts", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "contract.edited". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Contracts" in the module drop-down, click New Trigger. Set the execution event to Edited. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Custom Module Record Created** `custommodule.record.created`: Fires when a record is created in a user-defined custom module. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "the custom module", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "custommodule.record.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for &lt;your custom module&gt;" in the module drop-down, click New Trigger. Set the execution event to Created. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Custom Module Record Deleted** `custommodule.record.deleted`: Fires when a record in a user-defined custom module is deleted. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "the custom module", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "custommodule.record.deleted". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for &lt;your custom module&gt;" in the module drop-down, click New Trigger. Set the execution event to Deleted. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Custom Module Record Updated** `custommodule.record.edited`: Fires when a record in a user-defined custom module is modified. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "the custom module", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "custommodule.record.edited". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for &lt;your custom module&gt;" in the module drop-down, click New Trigger. Set the execution event to Edited. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Problem Created** `problem.created`: Fires when a new problem record is logged. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Problems", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "problem.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Problems" in the module drop-down, click New Trigger. Set the execution event to Created. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Problem Deleted** `problem.deleted`: Fires when a problem record is deleted. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Problems", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "problem.deleted". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Problems" in the module drop-down, click New Trigger. Set the execution event to Deleted. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Problem Updated** `problem.edited`: Fires when an existing problem record is modified. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Problems", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "problem.edited". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Problems" in the module drop-down, click New Trigger. Set the execution event to Edited. Set "Apply every time the criteria is met" if every edit should be delivered. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Project Created** `project.created`: Fires when a new project is created. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Projects", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "project.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Projects" in the module drop-down, click New Trigger. Set the execution event to Created. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Project Deleted** `project.deleted`: Fires when a project is deleted. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Projects", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "project.deleted". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Projects" in the module drop-down, click New Trigger. Set the execution event to Deleted. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Project Updated** `project.edited`: Fires when an existing project is modified, including status and completion changes. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Projects", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "project.edited". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Projects" in the module drop-down, click New Trigger. Set the execution event to Edited. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Purchase Order Created** `purchaseorder.created`: Fires when a new purchase order is raised. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Purchase", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "purchaseorder.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Purchase" in the module drop-down, click New Trigger. Set the execution event to Created. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Purchase Order Deleted** `purchaseorder.deleted`: Fires when a purchase order is deleted. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Purchase", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "purchaseorder.deleted". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Purchase" in the module drop-down, click New Trigger. Set the execution event to Deleted. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Purchase Order Updated** `purchaseorder.edited`: Fires when a purchase order changes, including approval and receipt status transitions. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Purchase", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "purchaseorder.edited". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Purchase" in the module drop-down, click New Trigger. Set the execution event to Edited. Add a criteria on Status to narrow it to a specific transition such as Approved or Received. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Release Created** `release.created`: Fires when a new release record is created. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Releases", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "release.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Releases" in the module drop-down, click New Trigger. Set the execution event to Created. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Release Deleted** `release.deleted`: Fires when a release record is deleted. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Releases", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "release.deleted". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Releases" in the module drop-down, click New Trigger. Set the execution event to Deleted. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Release Updated** `release.edited`: Fires when an existing release is modified, including stage transitions. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Releases", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "release.edited". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Releases" in the module drop-down, click New Trigger. Set the execution event to Edited. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Request Assigned** `request.assigned`: Fires when a request is assigned or reassigned to a technician or support group. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Requests", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "request.assigned". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Requests" in the module drop-down, click New Trigger. Set the execution event to Edited. Add the criteria Technician is changed (or Group is changed) and select "Apply every time the criteria is met". Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Request Closed** `request.closed`: Fires when a request is closed. SDP has no dedicated close trigger event - this is an Edited trigger gated on status. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Requests", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "request.closed". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Requests" in the module drop-down, click New Trigger. Set the execution event to Edited. Add the criteria Status is Closed and select "Apply only for the first time". Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Request Created** `request.created`: Fires when a new request (incident or service request) is raised in ServiceDesk Plus Cloud. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Requests", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "request.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Requests" in the module drop-down, click New Trigger. Set the execution event to Created. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Request Deleted** `request.deleted`: Fires when a request is deleted. Only identity fields are reliably populated on a delete - the record is gone by the time downstream systems read it. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Requests", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "request.deleted". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Requests" in the module drop-down, click New Trigger. Set the execution event to Deleted. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Request Resolved** `request.resolved`: Fires when a request moves into the Resolved status. SDP has no dedicated resolve trigger event - this is an Edited trigger gated on status. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Requests", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "request.resolved". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Requests" in the module drop-down, click New Trigger. Set the execution event to Edited. Add the criteria Status is Resolved and select "Apply only for the first time" so a single event is emitted per resolution. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Request Updated** `request.edited`: Fires whenever any field on an existing request changes - status, priority, category, technician, custom fields. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Requests", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "request.edited". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Requests" in the module drop-down, click New Trigger. Set the execution event to Edited. Leave the criteria empty for all edits, and set "Apply every time the criteria is met" so repeated edits keep firing. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Solution Created** `solution.created`: Fires when a new knowledge-base solution article is created. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Solutions", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "solution.created". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Solutions" in the module drop-down, click New Trigger. Set the execution event to Created. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Solution Deleted** `solution.deleted`: Fires when a solution article is deleted. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Solutions", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "solution.deleted". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Solutions" in the module drop-down, click New Trigger. Set the execution event to Deleted. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.
* **Solution Updated** `solution.edited`: Fires when a solution article is modified, including approval status changes from Draft to Approved. Setup step 1 (webhook): Setup &gt; Automation &gt; Custom Actions &gt; Webhooks, pick module "Solutions", New Webhook. Method POST, API URL = this fastn webhook URL, Endpoint Type Cloud, Content Type application/json. Compose the Message Body from this schema (type $ to pick a variable), and add a literal event_type field set to "solution.edited". SDP does not sign calls - add the shared-secret header from setupNote. Step 2 (trigger): Setup &gt; Automation &gt; Triggers, choose "Triggers for Solutions" in the module drop-down, click New Trigger. Set the execution event to Edited. Under Actions choose Custom Actions &gt; Webhooks and select the webhook from step 1, then Save.

</details>
