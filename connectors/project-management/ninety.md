---
description: "Ninety is a business operating system for teams running EOS."
hidden: true
---

# Ninety

<img src="../../.gitbook/assets/connectors/lg/ninety.png" alt="Ninety logo">

Ninety is a business operating system for teams running EOS. This connector covers the full Ninety public API: Issues, To-Dos, Rocks and Milestones, Headlines and Cascading Messages, the Scorecard with its Measurables, scores and notes, Teams, Users, Meetings, the Vision/Traction Organizer and the Accountability Chart.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [ninety.io](https://ninety.io) |
| **Authentication** | Bearer token |
| **Slug** | `ninety` |

## Use it

Add Ninety from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ninety.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Issue Comment | `addIssueComment` | Appends one comment to an Issue, attributed to the authenticated user, and returns the full comment list including the new one. Send only the new comment; the existing ones are preserved for you. Callers who cannot edit the Issue in Ninety receive a 403. |
| Add To-Do Comment | `addTodoComment` | Appends one comment to a To-Do, attributed to the authenticated user, and returns the full comment list including the new one. Send only the new comment; the existing ones are read and preserved for you. |
| Create Headline | `createHeadline` | Creates a Headline on one Team, where it appears on that Team's list exactly as one created in the app does, and notifies its followers. The Headline is owned by the authenticated user unless another user in the same company is named; either way the authenticated user is recorded as the creator. Set the Cascading Message flag to create a Cascading Message instead. Note that Ninety's public API offers no way to update or delete a Headline once created, so treat every call as permanent. |
| Create Issue | `createIssue` | Creates a new Issue on the given Team. The Issue is assigned to the authenticated user unless userId names someone else in the same company. |
| Create Milestone | `createMilestone` | Creates a Milestone against a Rock. Milestones are the dated checkpoints that mark progress towards completing the Rock. The Milestone is always created outstanding: Ninety documents isDone and completedDate on this endpoint but accepts and silently discards them, so they are not offered here. Create the Milestone first, then mark it complete with Update Milestone. |
| Create Rock | `createRock` | Creates a Rock, the quarterly priority Ninety tracks against a Team. The Rock is always owned by the authenticated user: the owner and company are derived from the token and any userId in the body is ignored. The Team must be one returned by List Available Teams. Ninety returns an array because the underlying create accepts a list of owners. |
| Create To-Do | `createTodo` | Creates a new To-Do. Omit teamId, or pass an empty string, to create a personal To-Do. Note on linking: Ninety accepts linkedItemId and linkedItemType here and answers 201, but the resulting link is not visible anywhere in the public API, and Ninety's dedicated Link To-Do endpoint currently fails on every valid target - so treat linking as unverified. |
| Delete Issue | `deleteIssue` | Permanently deletes an Issue. This cannot be undone; mark an Issue completed instead if you only want it off the active list. |
| Delete Measurable Note | `deleteMeasurableNote` | Removes the note recorded against a Measurable for one period. The score for that period is left untouched. |
| Delete Measurable Score | `deleteMeasurableScore` | Removes a Measurable's recorded score for one period, leaving the period blank on the Scorecard. |
| Delete Rock | `deleteRock` | Soft-deletes a Rock the same way the Ninety app does: the Rock is flagged deleted and stamped with who deleted it and when, its linked items are cleared, and it stops appearing in reads. Returns the deleted Rock. |
| Delete To-Do | `deleteTodo` | Deletes a To-Do. Unlike Delete Issue this is a soft delete: Ninety answers 204, flags the To-Do deleted and stamps who deleted it and when, and it stops appearing in queries and lists - but Get To-Do still returns the record with deleted set to true. Archive the To-Do instead if you only want it off the active list. |
| Get Accountability Chart | `getAccountabilityChart` | Returns the company's Accountability Chart: every Seat, what that Seat is accountable for, and the people sitting in it. The seats array is flat and ordered top-down, so rebuild the hierarchy from parentSeatId, which is absent on the top Seat. A Seat with no holders is a real state, not an error. |
| Get Issue | `getIssue` | Returns a single Issue by its Id, including its comments. |
| Get Measurable Score | `getMeasurableScore` | Returns one Measurable's score for the period containing the given date, together with the period it resolved to. Prefer this over reading the whole Team Scorecard when only one number is needed. A null value means no score has been recorded for that period, which is not an error. |
| Get Meeting | `getMeeting` | Returns one concluded Meeting with the notes taken during it and the Headlines, cascading messages, Issues, To-Dos and Rocks it worked. Notes are the only free-text record of what was decided, as Ninety has no separate decisions field. |
| Get Milestone | `getMilestone` | Returns a single Milestone by its Id. |
| Get Next Meeting | `getNextMeeting` | Returns the soonest upcoming Meeting for a Team, with its agenda sections and the Team roster, so a caller has everything needed to prepare. Only the near term is considered - roughly the next month for most companies - so a 404 means nothing is scheduled soon, not that the Team never meets. |
| Get Rock | `getRock` | Returns a single Rock by its Id, including its Milestones. |
| Get Team Scorecard | `getTeamScorecard` | Returns a Team's Scorecard - its Measurables and their scores - for a window of periods. Every score is labelled with the period as Ninety displays it, such as 'Q4' or 'Jan 06 - Jan 12'; select a period by matching that label rather than computing date boundaries, which depend on the company's fiscal calendar and weekly start day. Supply a date to read just the single period containing it. |
| Get Team Vision Traction Organizer | `getTeamVto` | Returns a Team's Vision/Traction Organizer alongside the leadership Team's, each trimmed to the Core Values, the Core Focus, and the 1-Year Plan and 3-Year Picture goals. Only what the caller can see in the app is returned, so leadership sections that have not been shared come back empty. A Team that has never filled its V/TO in returns empty sections rather than an error. |
| Get To-Do | `getTodo` | Returns a single To-Do by its Id, including its comments and any linked Rock, Issue or Milestone. |
| Get User | `getUser` | Returns a single User by their Ninety user Id, including their role and the Teams they belong to. |
| Link To-Do | `linkTodo` | Links an existing To-Do to a Rock, Issue or Milestone, so the two appear connected in Ninety. The linked item must belong to the same company as the authenticated caller. |
| List Available Teams | `listAvailableTeams` | Returns the Teams the authenticated user may pick when creating or querying work, mirroring the Team picker in the Ninety app. It always includes the Teams they belong to, and for an Owner, Admin or Implementer it also includes every non-private Team in the company. Prefer this over List Teams when choosing a teamId for a create call. |
| List Company Issues | `listCompanyIssues` | Returns every non-archived, non-deleted Issue across the whole company, paginated by cursor. Restricted to company Owners and Admins; other roles receive a 403. Pass the nextToken from the previous response to fetch the next page. |
| List Company To-Dos | `listCompanyTodos` | Returns every non-personal To-Do across the whole company, regardless of assignee or Team, paginated by cursor. Restricted to company Owners and Admins; other roles receive a 403. |
| List Headlines | `listHeadlines` | Returns a page of one Team's Headlines - the short good-news and bad-news notes a Team raises in its Meetings. Headlines belong to exactly one Team, so a Team Id is required and there is no cross-Team read. Discussed Headlines are left out unless you ask for them, archived ones are a separate list, and Cascading Messages live in the same collection but are never mixed into the same response. |
| List Meetings | `listMeetings` | Returns a page of a Team's concluded Meetings, most recent first, each with the ratings its attendees gave, how long it ran and how many Issues it worked. This covers past Meetings only - the upcoming one is returned by Get Next Meeting. Exactly one kind of Meeting is returned per call, so reading Weeklies and Quarterlies takes two calls. A Team that has never met returns an empty page rather than a 404. |
| List Rock Milestones | `listRockMilestones` | Returns every Milestone belonging to one Rock. Milestones are the checkpoints that mark progress towards completing the Rock. |
| List Team Users | `listTeamUsers` | Returns the Users assigned to one Team, ordered by name, with their role and every Team they are on. The authenticated user must belong to that Team or be an admin of the company that owns it. |
| List Teams | `listTeams` | Returns every Team the authenticated user belongs to. Use List Available Teams instead when you need the Teams the user may create or query work for, which for an Owner or Admin is wider than their own membership. |
| List Users | `listUsers` | Returns every active User in the authenticated user's company, with their role and the Teams they are on. Use it to resolve a person's name or email to the userId that the To-Do, Issue, Rock and Headline create actions accept. An email nobody in the company uses returns an empty array rather than an error. |
| Query Issues | `queryIssues` | Returns a paginated list of Issues, filtered by Team, classification and free-text search. Filters are sent in the request body rather than the query string. |
| Query Measurables | `queryMeasurables` | Returns a paginated list of Measurables - their names, targets, owners and cadence - without score values. Pass a Team Id to limit results to one Team's Scorecards. Results are always limited to Measurables the caller can see. |
| Query Rocks | `queryRocks` | Returns every Rock matching the filters, grouped by Team Id rather than as a flat list, and with no total. A Rock belonging to several Teams is repeated under each of their keys. Ninety recommends Query Rocks Paged instead, which pages properly and de-duplicates. |
| Query Rocks Paged | `queryRocksPaged` | Returns one page of Rocks as a flat, de-duplicated list, plus the total number of distinct matches. Prefer this over Query Rocks: the ordering carries a tiebreaker so a Rock will not repeat across pages or be skipped. Filter by Team wherever possible to keep the result set small. |
| Query To-Dos | `queryTodos` | Returns every To-Do matching the supplied filters as a flat list, with no total. Personal and team To-Dos cannot be returned by the same call: omit Is Personal (or pass false) for team To-Dos, and pass true for personal ones. Use Query To-Dos Paged when you need a total or stable paging. |
| Query To-Dos Paged | `queryTodosPaged` | Returns one page of To-Dos matching the supplied filters, plus the total number of matches. Pass a sort field whenever you intend to read more than one page, so the ordering stays stable between calls. |
| Set Measurable Note | `setMeasurableNote` | Records a note against a Measurable for one period, explaining the number. If a note already exists for that period it is overwritten. |
| Set Measurable Score | `setMeasurableScore` | Records a Measurable's score for one period. If a score already exists for that period it is overwritten. Take the period start date from Get Team Scorecard rather than computing it, because period boundaries depend on the company's fiscal calendar. |
| Unlink To-Do | `unlinkTodo` | Removes the link between a To-Do and a Rock, Issue or Milestone. The To-Do and the linked item both remain; only the connection between them is removed. |
| Update Issue | `updateIssue` | Partially updates an Issue. Only the fields you supply are changed; everything you leave out keeps its current value. |
| Update Milestone | `updateMilestone` | Partially updates a Milestone. Only the fields you supply are changed. Provide a completion date alongside Is Done when marking a Milestone complete. |
| Update Rock | `updateRock` | Partially updates a Rock and returns the complete Rock as it now stands. Only the fields you supply are changed. Completion is tracked from the status: setting it to DONE marks the Rock completed and stamps the completion date, and moving off DONE clears both - completed and completedDate are not writable directly. |
| Update To-Do | `updateTodo` | Partially updates a To-Do. Only the fields you supply are changed; everything you leave out keeps its current value. Two fields Ninety documents for this endpoint are deliberately not offered, because both misbehave: linkedItemId and linkedItemType make Ninety reject the whole request with a 400, losing the rest of the update, and repeat is accepted but silently discarded. Set the recurrence when you create the To-Do instead. |
