---
description: "Amazing Marvin is a personal task manager and productivity system."
---

# Amazing Marvin

Amazing Marvin is a personal task manager and productivity system. This connector covers the full Amazing Marvin public REST API: tasks, projects, categories, labels, calendar events, scheduled and due items, time blocks, time tracking, reward points, Marvin Kudos, goals, habits, reminders, account profile, and raw sync-database document read/create/update/delete.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [amazingmarvin.com](https://amazingmarvin.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 35 |
| **Events** | 0 |
| **Slug** | `amazingMarvin` |

## Use it

Add Amazing Marvin from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.amazingMarvin.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Claim Reward Points | `claimRewardPoints` | Awards reward points to the connected Amazing Marvin account, either for completing a specific task or as a manual award. Returns the updated account profile with the new point balances. |
| Create Document | `createDocument` | Creates a raw document in the Amazing Marvin sync database. Requires the Full Access Token. Use this only for document types the dedicated Create Task, Create Project and Create Event actions do not cover - an invalid settings document can stop Marvin from starting. |
| Create Event | `createEvent` | Creates a calendar event in Amazing Marvin. Calendar sync runs on the Marvin client, so the event only reaches a connected external calendar while Marvin is running on one of the user's devices. |
| Create Project | `createProject` | Creates a project in Amazing Marvin. The title supports Marvin autocompletion for parent category, due date and labels. Only the fields listed here are accepted by this endpoint. |
| Create Task | `createTask` | Creates a task in Amazing Marvin. By default the title is run through Marvin's autocompletion, so '+today', '#Category' and '@label' tokens in the title are resolved and stripped. Only the fields listed here are accepted by this endpoint. |
| Delete All Reminders | `deleteAllReminders` | Removes every scheduled push reminder from Amazing Marvin's servers for the connected account. Requires the Full Access Token. Also clear the reminder details from the corresponding tasks so the Marvin interface stays accurate. |
| Delete Document | `deleteDocument` | Permanently deletes a document from the Amazing Marvin sync database. Requires the Full Access Token. Marvin's Trash is client-side only, so a document removed this way cannot be recovered. |
| Delete Reminders | `deleteReminders` | Removes one or more scheduled push reminders by their IDs. Also clear the matching reminder details from the corresponding tasks so the Marvin interface stays accurate. |
| Get Document | `getDocument` | Retrieves any single document from the Amazing Marvin sync database by its ID - a task, project, label, habit, time block or settings document. Requires the Full Access Token. The whole document is returned, including the CouchDB _id and _rev. A missing or deleted ID still answers HTTP 200, with an error envelope instead of a document, so always check the Error field before reading the rest. |
| Get Habit | `getHabit` | Retrieves the habit tracking record for one habit ID, including its full recording history and its sharing and reminder schedule. |
| Get Marvin Kudos | `getMarvinKudos` | Retrieves the connected user's Marvin Kudos standing: the current Kudos total, the Kudos level reached, and how many Kudos remain before the next level. |
| Get My Account | `getMyAccount` | Retrieves the Amazing Marvin account profile for the connected user, including email, subscription billing period and paid-through date, reward point balances, Pomodoro ("tomato") counters and current time-tracking state. |
| Get Time Tracks | `getTimeTracks` | Returns the authoritative time-tracking timestamps for up to 100 tasks at once. Use this when a task's cached times or duration fields are missing or out of date. Amazing Marvin also serves this endpoint at /api/times for environments where 'track' is blocked by an extension blacklist. |
| Get Tracked Item | `getTrackedItem` | Retrieves the task or project that is currently being time-tracked in the connected Amazing Marvin account. Returns HTTP 204 with no body when nothing is being tracked. |
| List Categories | `listCategories` | Lists every category and project in the connected Amazing Marvin account. Categories and projects share one document type; the 'type' field distinguishes them. |
| List Child Items | `listChildItems` | Lists the open tasks and projects whose parent is the given category or project. Only direct children are returned - query each child in turn to walk deeper levels. Use 'unassigned' to list items with no parent and 'root' for top-level items. |
| List Done Items | `listDoneItems` | Lists the tasks and projects completed on a given day. This endpoint is live on Amazing Marvin's API but is not covered by the published API wiki, so its response shape is modelled on the other item-list endpoints. |
| List Due Items | `listDueItems` | Lists open tasks and projects that are due on or before a given date. Pass the date explicitly because Marvin's servers run in UTC and may not share your time zone. |
| List Goals | `listGoals` | Lists every goal defined in the connected Amazing Marvin account. |
| List Habits | `listHabits` | Lists the habit tracking records for the connected Amazing Marvin account, each with its full recording history and its sharing and reminder schedule. The habit's own title and settings live in its Habits document - read that with Get Document. |
| List Labels | `listLabels` | Lists every label in the connected Amazing Marvin account, in the sort order Marvin uses when sorting by label. |
| List Reminders | `listReminders` | Lists every reminder currently scheduled on Amazing Marvin's servers for push delivery to the mobile apps. Requires the Full Access Token. |
| List Today Items | `listTodayItems` | Lists the tasks and projects scheduled for a given day, including rollover and auto-scheduled due items when those strategies are enabled. Marvin's servers run in UTC, so always pass the date explicitly to avoid time-zone drift. |
| List Today Time Blocks | `listTodayTimeBlocks` | Lists the time blocks planned for a given day in the connected Amazing Marvin account. |
| Mark Task Done | `markTaskDone` | Marks a task as complete in Amazing Marvin. Handles pinned tasks, stops time tracking, applies day-based repeats and grants reward points. Only tasks can be completed with this endpoint - projects are rejected. |
| Record Pledge Outcome | `recordPledgeOutcome` | Records whether a task that carried a Marvin pledge was completed or failed, clearing the pledge from the item. This endpoint is live on Amazing Marvin's API but is not covered by the published API wiki; its request fields were read from the Marvin web client and it returns an empty body. |
| Reset Reward Points | `resetRewardPoints` | Permanently deletes the account's reward-point earn and spend history and resets the balance to zero. This cannot be undone. Requires the Full Access Token. |
| Set Reminders | `setReminders` | Schedules one or more push reminders on Amazing Marvin's servers, replacing any existing reminder with the same reminder ID. Reminders are delivered to the Amazing Marvin mobile apps only. If a reminder corresponds to a scheduled task, also write the reminder details onto that task so the Marvin interface stays accurate. |
| Set Time Tracking | `setTimeTracking` | Starts or stops time tracking on a task in Amazing Marvin. The task's own duration and times fields are not updated by this endpoint - use Update Document afterwards if the Marvin interface must show the new totals. Amazing Marvin also serves this endpoint at /api/time for environments where 'track' is blocked by an extension blacklist. |
| Spend Reward Points | `spendRewardPoints` | Spends reward points from the connected Amazing Marvin account, for example when cashing a reward in. Returns the updated account profile with the new point balances. |
| Test Credentials | `testCredentials` | Verifies that the stored Amazing Marvin API Token is valid. Returns the literal text OK when the token is accepted; an invalid token is rejected with HTTP 400 and the message 'Invalid access token or user deleted'. |
| Unclaim Reward Points | `unclaimRewardPoints` | Reverses a previous reward-point award for a task, for example after marking that task incomplete again. Amazing Marvin works out how many points to remove from the item's own record. Returns the updated account profile. |
| Update Document | `updateDocument` | Applies a list of field setters to an existing document in the Amazing Marvin sync database. Requires the Full Access Token. Also set the matching fieldUpdates.FIELD and updatedAt timestamps so Marvin resolves sync conflicts and renders the change correctly. |
| Update Habit | `updateHabit` | Records a habit value, undoes the most recent recording, or rewrites a habit's whole history. Supply Time and Value to record, Undo to remove the last entry, or History to replace every entry. By default only the backend database changes - set Update Database to have Marvin write the change into the habit document as well. |
| Update Tracker | `updateTracker` | Records a value against a Marvin tracker, undoes the last recording, or rewrites the tracker's history. This endpoint is live on Amazing Marvin's API but is not covered by the published API wiki; its request shape was read from the Marvin web client. It answers with the literal text OK, and Amazing Marvin exposes no public endpoint for reading tracker history back. |
