---
description: "Microsoft Planner task management via the Microsoft Graph v1.0 API (https://graph.microsoft.com/v1.0/planner)."
---

# Microsoft Planner

Microsoft Planner task management via the Microsoft Graph v1.0 API (https://graph.microsoft.com/v1.0/planner). Create and manage plans, buckets and tasks, read and update task details (description, checklist, references, preview type) and plan details (category descriptions, sharedWith), and set the three task board formats - assignedTo, bucket and progress. Also lists the plans and tasks of the signed-in user, of another user, and of a Microsoft 365 group. Connect with a Microsoft work or school account using Entra ID OAuth 2.0; the delegated Tasks.ReadWrite permission is user-consentable and needs no tenant administrator approval. Every PATCH and DELETE requires the target object's current ETag in the If-Match header, which each action exposes as an input.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [graph.microsoft.com](https://graph.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 33 |
| **Events** | 0 |
| **Slug** | `microsoftPlanner` |

## Use it

Add Microsoft Planner from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.microsoftPlanner.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Bucket | `createBucket` | Creates a new bucket, which appears as a column on the task board of the specified Planner plan. |
| Create Plan | `createPlan` | Creates a new Planner plan inside a container, normally a Microsoft 365 group. The signed-in user must already be a member of that group; creating a group does not add you to it. The container cannot be changed after the plan is created. |
| Create Task | `createTask` | Creates a new task in a Planner plan, optionally placing it in a bucket and assigning it to one or more users. Long description, checklist and references are set afterwards with Update Task Details. |
| Delete Bucket | `deleteBucket` | Permanently deletes a Planner bucket and the tasks it contains. Requires the bucket's current ETag, which Get Bucket returns as @odata.etag. This cannot be undone. |
| Delete Plan | `deletePlan` | Permanently deletes a Planner plan and every bucket and task in it. Requires the plan's current ETag, which Get Plan returns as @odata.etag. This cannot be undone. |
| Delete Task | `deleteTask` | Permanently deletes a Planner task. Requires the task's current ETag, which Get Task returns as @odata.etag. This cannot be undone. |
| Get Assigned To Task Board Format | `getAssignedToTaskBoardFormat` | Retrieves the assignedToTaskBoardFormat of a task, which controls where the task sits in the Assigned To view of the plan's task board. |
| Get Bucket | `getBucket` | Retrieves a single Planner bucket by its ID. The @odata.etag in the response is the value to pass as If-Match when updating or deleting the bucket. |
| Get Bucket Task Board Format | `getBucketTaskBoardFormat` | Retrieves the bucketTaskBoardFormat of a task, which controls where the task sits in the Bucket view of the plan's task board. |
| Get Plan | `getPlan` | Retrieves a single Planner plan by its ID, including its title, container and creation metadata. The @odata.etag in the response is the value to pass as If-Match when updating or deleting the plan. |
| Get Plan Details | `getPlanDetails` | Retrieves the plannerPlanDetails of a plan: the label names for the 25 task categories and the set of user IDs the plan is shared with. |
| Get Progress Task Board Format | `getProgressTaskBoardFormat` | Retrieves the progressTaskBoardFormat of a task, which controls where the task sits in the Progress view of the plan's task board. |
| Get Task | `getTask` | Retrieves a single Planner task by its ID, including its assignments, dates, priority and completion percentage. The @odata.etag in the response is the value to pass as If-Match when updating or deleting the task. |
| Get Task Details | `getTaskDetails` | Retrieves the plannerTaskDetails of a task: its long description, checklist items, external references and preview type. |
| List Bucket Tasks | `listBucketTasks` | Lists all tasks contained in a specific Planner bucket, which is one column of the plan's task board. |
| List Buckets | `listBuckets` | Lists Planner buckets. Microsoft Graph requires a planId filter on this endpoint, so the Filter input is mandatory and must be of the form planId eq '{plan-id}'. Verified live: Graph often answers this filtered collection with an empty first page plus an @odata.nextLink that must be followed to reach the rows, so prefer List Plan Buckets, which returns a plan's buckets directly in one response. |
| List Group Plans | `listGroupPlans` | Lists the Planner plans owned by a Microsoft 365 group. The signed-in user must be able to read the group. |
| List My Plans | `listMyPlans` | Lists the Planner plans the signed-in user has recently viewed or interacted with in Planner. Verified live: this collection is not a general access list, so a plan the user can reach through a group can still be absent from it until the user opens that plan. To enumerate a group's plans reliably, use List Group Plans. |
| List My Tasks | `listMyTasks` | Lists every Planner task assigned to the signed-in user, across all plans they belong to. |
| List Plan Buckets | `listPlanBuckets` | Lists all buckets that belong to a specific Planner plan, in board order. |
| List Plan Tasks | `listPlanTasks` | Lists all tasks that belong to a specific Planner plan, across every bucket in that plan. |
| List Plans | `listPlans` | Lists Planner plans across the tenant. Microsoft Graph requires an owner filter on this endpoint, so the Filter input is mandatory and must be of the form owner eq '{group-id}'. Returns a collection of plannerPlan objects. |
| List Tasks | `listTasks` | Lists Planner tasks. Microsoft Graph requires a planId filter on this endpoint, so the Filter input is mandatory and must be of the form planId eq '{plan-id}'. Returns a collection of plannerTask objects. |
| List User Plans | `listUserPlans` | Lists the Planner plans a specified user has recently viewed or interacted with in Planner. Verified live: this collection is not a general access list, so a plan the user can reach through a group can still be absent from it until the user opens that plan. To enumerate a group's plans reliably, use List Group Plans. Use List My Plans for the signed-in user. |
| List User Tasks | `listUserTasks` | Lists every Planner task assigned to a specified user, across all plans they belong to. Use List My Tasks for the signed-in user. |
| Update Assigned To Task Board Format | `updateAssignedToTaskBoardFormat` | Repositions a task within the Assigned To view of the plan's task board, per assignee or in the unassigned column. Requires the format's current ETag, which Get Assigned To Task Board Format returns as @odata.etag. |
| Update Bucket | `updateBucket` | Renames a Planner bucket or moves it to a different position on the task board. Requires the bucket's current ETag, which Get Bucket returns as @odata.etag. |
| Update Bucket Task Board Format | `updateBucketTaskBoardFormat` | Repositions a task within the Bucket view of the plan's task board. Requires the format's current ETag, which Get Bucket Task Board Format returns as @odata.etag. |
| Update Plan | `updatePlan` | Renames a Planner plan. Title is the only updatable property; the container is fixed once the plan exists. Requires the plan's current ETag, which Get Plan returns as @odata.etag. |
| Update Plan Details | `updatePlanDetails` | Updates a plan's details: the label text for its task categories and the set of users the plan is shared with. Requires the plan details' current ETag, which Get Plan Details returns as @odata.etag. |
| Update Progress Task Board Format | `updateProgressTaskBoardFormat` | Repositions a task within the Progress view of the plan's task board. Requires the format's current ETag, which Get Progress Task Board Format returns as @odata.etag. |
| Update Task | `updateTask` | Updates a Planner task. Only the properties you supply are sent, so untouched fields keep their values. Requires the task's current ETag, which Get Task returns as @odata.etag. For tasks replicated from Project, only percentComplete can be updated. |
| Update Task Details | `updateTaskDetails` | Updates a task's details: its long description, checklist items, external references and which of them is shown as the task preview. Requires the task details' current ETag, which Get Task Details returns as @odata.etag. |
