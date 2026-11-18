---
description: "SatisMeter is a customer-feedback platform for NPS, CSAT, CES, PMF and custom in-app, email and mobile surveys."
hidden: true
---

# SatisMeter

<img src="../../.gitbook/assets/connectors/lg/satismeter.png" alt="SatisMeter logo">

SatisMeter is a customer-feedback platform for NPS, CSAT, CES, PMF and custom in-app, email and mobile surveys. This connector covers the whole SatisMeter REST API: project details, surveys, survey statistics, project-level and survey-level responses, the legacy response export with dashboard summary counts, response insertion, user creation and updates, user event tracking, user listing, lookup and deletion, and the project email unsubscribe list. Survey completion and dismissal are available as events.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [satismeter.com](https://satismeter.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `satismeter` |

## Use it

Add SatisMeter from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.satismeter.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Or Update User | `createOrUpdateUser` | Adds a user to the connected project or updates an existing one, matched on your own user id. The traits you supply are used for survey targeting and are shown alongside the user's feedback. Returns 204 No Content on success. |
| Delete User | `deleteUser` | Permanently deletes a tracked user and their personal data from the connected project. Their survey responses are kept but anonymised. Identify the user by SatisMeter's internal id from List Users, not by your own userId. Returns 204 No Content on success. |
| Export Responses And Summary | `exportResponsesAndSummary` | Returns the connected project's responses together with SatisMeter's dashboard summary counts: total responses, how many carried a comment, and the promoter, passive and detractor split. Set Format to csv to receive a flat CSV export instead of JSON. This is SatisMeter's original export endpoint; for per-survey detail and cursor pagination use List Project Responses. |
| Get Project | `getProject` | Returns the SatisMeter project this connection is bound to, with its identifier and name. Takes no inputs: the project is taken from the connection's Project ID. |
| Get Survey | `getSurvey` | Returns a single survey in the connected project by its identifier, including its name, template type and state. |
| Get Survey Statistics | `getSurveyStatistics` | Returns aggregated statistics for one survey: display and response counts, response rate, and per-question answer distributions with the calculated NPS, CES, CSAT or PMF metric. Without a date range it covers the last 30 days. |
| Get User | `getUser` | Returns a single tracked user by SatisMeter's internal user id, with their traits and recorded events. The internal id comes from the id field of List Users, not from your own userId. |
| Insert Response | `insertResponse` | Records a survey response collected outside SatisMeter against one of the project's surveys. Authenticates with the connection's Write Key rather than the API key. Identify the respondent with User ID, or with Anonymous ID when the survey allows anonymous responses. Question and survey identifiers are listed in SatisMeter under Settings, then Integrations, then API keys. |
| List Project Responses | `listProjectResponses` | Returns survey responses recorded across every survey in the connected project, newest first, using cursor pagination. Without a date range it returns the last 30 days. |
| List Survey Responses | `listSurveyResponses` | Returns the survey responses recorded in one specific survey, using cursor pagination. Without a date range it returns the last 30 days. |

<details>

<summary>See 5 more actions</summary>

* **List Surveys** `listSurveys`: Returns every survey in the connected SatisMeter project, with each survey's identifier, name, template type and state. Use the returned identifier with Get Survey, List Survey Responses and Get Survey Statistics.
* **List Unsubscribed Emails** `listUnsubscribedEmails`: Returns the email addresses that are unsubscribed from survey emails in the connected project. Takes no inputs: the project is taken from the connection's Project ID.
* **List Users** `listUsers`: Returns the users tracked in the connected SatisMeter project, with their traits, recorded events and survey subscription state. Supply External User ID to return only the single user that matches it.
* **Track User Event** `trackUserEvent`: Records a named event against a user in the connected project, so surveys can be targeted at people who have performed it. Returns 204 No Content on success.
* **Update Unsubscribed Emails** `updateUnsubscribedEmails`: Replaces the project's list of email addresses that are excluded from survey emails. The list you supply becomes the whole list, so read the current list with List Unsubscribed Emails first and send it back with your additions. There is no limit on the number of addresses.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Survey Completed | `completed` | Fires when a user answers every question in a survey. SatisMeter has no webhook registration API, so the customer registers this URL by hand: in SatisMeter open Settings, then Integrations, then Webhooks, paste this trigger's URL into the webhook URL field, select the completed scenario and save. SatisMeter posts to that one URL for the whole project, so fastn routes deliveries on the payload's event field and matches the account on response.project. Payload schema modelled from SatisMeter's documented sample delivery, not captured from a live delivery. |
| Survey Dismissed | `dismissed` | Fires when a user closes a survey without answering it. SatisMeter has no webhook registration API, so the customer registers this URL by hand: in SatisMeter open Settings, then Integrations, then Webhooks, paste this trigger's URL into the webhook URL field, select the dismissed scenario and save. Payload schema modelled from SatisMeter's documented sample delivery, not captured from a live delivery; a dismissed delivery carries the same response object with completed false and no rating or feedback. |
