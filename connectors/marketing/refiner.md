---
description: "Refiner is a customer survey platform for in-product, web and link surveys."
---

# Refiner

Refiner is a customer survey platform for in-product, web and link surveys. This connector covers the full Refiner REST API v1: authentication check, account info, identifying users, tracking events, survey responses (list, store and tag), aggregated reporting, contacts, forms (list, publish, archive, duplicate and change history), segments and manual segment membership.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [refiner.io](https://refiner.io) |
| **Authentication** | Bearer token |
| **Actions** | 19 |
| **Events** | 3 |
| **Slug** | `refiner` |

## Use it

Add Refiner from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.refiner.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add User to Segment | `addUserToSegment` | Adds a user, identified by user ID or email, to a manual list segment, creating the user if they do not exist. Data-driven segments are rejected with a 400. |
| Archive Form | `archiveForm` | Archives an existing survey. Archived surveys stop running and appear only when listing archived surveys. |
| Delete Contact | `deleteContact` | Deletes a contact and all of their survey responses, identified by your user ID or email address. Refiner's delete endpoint does not accept the contact UUID, although its docs list it. To keep responses for compliance, overwrite the user's traits with Identify User instead. |
| Duplicate Form | `duplicateForm` | Duplicates an existing survey into a new draft with the given name, and returns the new survey's UUID. |
| Get Account Info | `getAccountInfo` | Returns the Refiner account's subscription plan with monthly usage and limits for tracked users, events, page views and survey responses, plus every environment with its usage. |
| Get Contact | `getContact` | Retrieves everything Refiner has on record for one contact, identified by your user ID, email address or Refiner contact UUID, including traits, survey answers, segments and the associated account. Provide at least one identifier; user ID is preferred because several contacts can share an email. |
| Get Form Change History | `getFormHistory` | Retrieves the change log of a survey as a paginated list of versions, each with a snapshot of the survey's configuration, channels and questions at that point in time. |
| Get Reporting | `getReporting` | Returns an aggregated report like Refiner's reporting dashboards: NPS, CSAT, ratings average, answer distribution, or response and view counts. Optionally narrow it to one survey, tag, segment or question identifier, a date range (default the last seven days), and one survey answer, contact trait or account trait each. |
| Identify User | `identifyUser` | Creates or updates a Refiner contact identified by your user ID or email address, and sets user traits on it. Any additional top-level field you pass is stored as a trait: strings up to 255 characters, integers, booleans, and dates for keys ending in _at. Pass an account object to group the user under an account. Returns 201 on success, or 409 if another identify call for the same user is still running. |
| List Contacts | `listContacts` | Retrieves contacts with their traits, segments and account, with optional search by email, user ID or name, filtering by survey or segment, ordering, and page or cursor pagination. |
| List Forms | `listForms` | Retrieves surveys ordered by name, optionally limited to published, draft or archived surveys, and optionally including each survey's full configuration or metadata such as channels, publish date, response and view counts, folder and link survey URL. |
| List Responses | `listResponses` | Retrieves survey responses and, optionally, partial responses and survey views, newest first, with the answers, survey and contact. Filter by survey, segment, tag, date range, completion status, contact search, and one survey answer, contact trait or account trait each. Supports page or cursor pagination. |
| List Segments | `listSegments` | Retrieves all user segments ordered by name, showing whether each is a manual list segment (users can be added through the API) or a data-driven segment. |
| Publish Form | `publishForm` | Publishes an existing survey, or unpublishes it when Published is 0. Publishing makes the survey live to its targeted audience. |
| Remove User from Segment | `removeUserFromSegment` | Removes a user, identified by user ID or email, from a manual list segment. |
| Store Response | `storeResponse` | Stores a survey response for a user, for importing historical survey data or collecting answers in your own UI. The survey must exist but can be empty and unpublished. Identify the user by user ID, email or contact UUID. Any additional top-level field is stored as an answer keyed by its question identifier, for example nps: 9. |
| Tag Response | `tagResponse` | Adds up to 20 tags to an existing survey response. |
| Track Event | `trackEvent` | Tracks a named event for a user identified by user ID or email address, creating the user if they do not exist. Tracked events can trigger in-product surveys and build segments. Event tracking is available on Refiner's Growth and Enterprise plans. |
| Verify Authentication | `verifyAuthentication` | Confirms the API key is valid and returns the UUID and name of the Refiner environment the key belongs to. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Survey Completed | `Completed Survey` | Fires when a user completes a Refiner survey. The response object carries the answers. Refiner has no webhook registration API, so each customer sets this up once per environment in the Refiner dashboard: go to Integrations &gt; Webhooks, click Create Webhook, give it a name, paste the fastn webhook URL as the target URL, choose the trigger event 'Survey Interaction', and save. Refiner sends the interaction type in the triggered_event field, so one webhook delivers Saw Survey, Completed Survey and Dismissed Survey. The optional secret token is not verified by fastn. Payload schema is Refiner's documented sample payload, not a captured delivery. |
| Survey Dismissed | `Dismissed Survey` | Fires when a user dismisses a Refiner survey without completing it. Refiner has no webhook registration API, so each customer sets this up once per environment in the Refiner dashboard: go to Integrations &gt; Webhooks, click Create Webhook, give it a name, paste the fastn webhook URL as the target URL, choose the trigger event 'Survey Interaction', and save. Refiner sends the interaction type in the triggered_event field, so one webhook delivers Saw Survey, Completed Survey and Dismissed Survey. The optional secret token is not verified by fastn. Payload schema is Refiner's documented sample payload, not a captured delivery. |
| Survey Seen | `Saw Survey` | Fires when a Refiner survey is shown to a user. Refiner has no webhook registration API, so each customer sets this up once per environment in the Refiner dashboard: go to Integrations &gt; Webhooks, click Create Webhook, give it a name, paste the fastn webhook URL as the target URL, choose the trigger event 'Survey Interaction', and save. Refiner sends the interaction type in the triggered_event field, so one webhook delivers Saw Survey, Completed Survey and Dismissed Survey. The optional secret token is not verified by fastn. Payload schema is Refiner's documented sample payload, not a captured delivery. |
