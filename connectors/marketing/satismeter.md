---
description: "SatisMeter is a customer-feedback platform for NPS, CSAT, CES, PMF and custom in-app, email and mobile surveys."
hidden: true
---

# SatisMeter

<img src="../../.gitbook/assets/connectors/lg/satismeter.png" alt="SatisMeter logo">

This connector covers the whole SatisMeter REST API: project details, surveys, survey statistics, project-level and survey-level responses, the legacy response export with dashboard summary counts, response insertion, user creation and updates, user event tracking, user listing, lookup and deletion, and the project email unsubscribe list. Survey completion and dismissal are available as events.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [satismeter.com](https://satismeter.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `satismeter` |

## Use it

Add SatisMeter from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.satismeter.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Or Update User</td><td><code>createOrUpdateUser</code></td><td>Adds a user to the connected project or updates an existing one, matched on your own user id. The traits you supply are used for survey targeting and are shown alongside the user's feedback. Returns 204 No Content on success.</td></tr><tr><td>Delete User</td><td><code>deleteUser</code></td><td>Permanently deletes a tracked user and their personal data from the connected project. Their survey responses are kept but anonymised. Identify the user by SatisMeter's internal id from List Users, not by your own userId. Returns 204 No Content on success.</td></tr><tr><td>Export Responses And Summary</td><td><code>exportResponsesAndSummary</code></td><td>Returns the connected project's responses together with SatisMeter's dashboard summary counts: total responses, how many carried a comment, and the promoter, passive and detractor split. Set Format to csv to receive a flat CSV export instead of JSON. This is SatisMeter's original export endpoint; for per-survey detail and cursor pagination use List Project Responses.</td></tr><tr><td>Get Project</td><td><code>getProject</code></td><td>Returns the SatisMeter project this connection is bound to, with its identifier and name. Takes no inputs: the project is taken from the connection's Project ID.</td></tr><tr><td>Get Survey</td><td><code>getSurvey</code></td><td>Returns a single survey in the connected project by its identifier, including its name, template type and state.</td></tr><tr><td>Get Survey Statistics</td><td><code>getSurveyStatistics</code></td><td>Returns aggregated statistics for one survey: display and response counts, response rate, and per-question answer distributions with the calculated NPS, CES, CSAT or PMF metric. Without a date range it covers the last 30 days.</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Returns a single tracked user by SatisMeter's internal user id, with their traits and recorded events. The internal id comes from the id field of List Users, not from your own userId.</td></tr><tr><td>Insert Response</td><td><code>insertResponse</code></td><td>Records a survey response collected outside SatisMeter against one of the project's surveys. Authenticates with the connection's Write Key rather than the API key. Identify the respondent with User ID, or with Anonymous ID when the survey allows anonymous responses. Question and survey identifiers are listed in SatisMeter under Settings, then Integrations, then API keys.</td></tr><tr><td>List Project Responses</td><td><code>listProjectResponses</code></td><td>Returns survey responses recorded across every survey in the connected project, newest first, using cursor pagination. Without a date range it returns the last 30 days.</td></tr><tr><td>List Survey Responses</td><td><code>listSurveyResponses</code></td><td>Returns the survey responses recorded in one specific survey, using cursor pagination. Without a date range it returns the last 30 days.</td></tr></tbody></table>

<details>

<summary>View 5 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Surveys</td><td><code>listSurveys</code></td><td>Returns every survey in the connected SatisMeter project, with each survey's identifier, name, template type and state. Use the returned identifier with Get Survey, List Survey Responses and Get Survey Statistics.</td></tr><tr><td>List Unsubscribed Emails</td><td><code>listUnsubscribedEmails</code></td><td>Returns the email addresses that are unsubscribed from survey emails in the connected project. Takes no inputs: the project is taken from the connection's Project ID.</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>Returns the users tracked in the connected SatisMeter project, with their traits, recorded events and survey subscription state. Supply External User ID to return only the single user that matches it.</td></tr><tr><td>Track User Event</td><td><code>trackUserEvent</code></td><td>Records a named event against a user in the connected project, so surveys can be targeted at people who have performed it. Returns 204 No Content on success.</td></tr><tr><td>Update Unsubscribed Emails</td><td><code>updateUnsubscribedEmails</code></td><td>Replaces the project's list of email addresses that are excluded from survey emails. The list you supply becomes the whole list, so read the current list with List Unsubscribed Emails first and send it back with your additions. There is no limit on the number of addresses.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Survey Completed</td><td><code>completed</code></td><td>Fires when a user answers every question in a survey. SatisMeter has no webhook registration API, so the customer registers this URL by hand: in SatisMeter open Settings, then Integrations, then Webhooks, paste this trigger's URL into the webhook URL field, select the completed scenario and save. SatisMeter posts to that one URL for the whole project, so fastn routes deliveries on the payload's event field and matches the account on response.project. Payload schema modelled from SatisMeter's documented sample delivery, not captured from a live delivery.</td></tr><tr><td>Survey Dismissed</td><td><code>dismissed</code></td><td>Fires when a user closes a survey without answering it. SatisMeter has no webhook registration API, so the customer registers this URL by hand: in SatisMeter open Settings, then Integrations, then Webhooks, paste this trigger's URL into the webhook URL field, select the dismissed scenario and save. Payload schema modelled from SatisMeter's documented sample delivery, not captured from a live delivery; a dismissed delivery carries the same response object with completed false and no rating or feedback.</td></tr></tbody></table>
