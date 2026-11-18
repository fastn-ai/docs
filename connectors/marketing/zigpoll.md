---
description: "Zigpoll is a survey platform for post-purchase, on-site, email and SMS surveys."
---

# Zigpoll

Zigpoll is a survey platform for post-purchase, on-site, email and SMS surveys. This connector covers the complete Zigpoll Web API v1: the current user and accounts, surveys (polls) and their slides (questions) including create, update, dry-run staging and commit, slide reordering, translations, action logic, responses, response metadata, location, device and trend breakdowns, attribution reports, participants, captured emails, AI insights, synthetic research, email and SMS campaign sends, trackable survey links and signed webhooks. API access requires a Zigpoll Premium plan or higher.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [zigpoll.com](https://zigpoll.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 36 |
| **Events** | 2 |
| **Slug** | `zigpoll` |

## Use it

Add Zigpoll from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zigpoll.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Synthetic Research | `cancelSyntheticResearch` | Cancels the synthetic research job currently running on a poll. Responses already generated are kept. |
| Commit Staged Object | `commitStagedObject` | Saves a poll or slide that was previously staged with a dry run of Create Poll or Create Slide. The object is inserted exactly as returned by the dry run, without further defaulting. |
| Create Poll | `createPoll` | Creates a new poll (survey) under an account you own. The poll starts hidden (isVisible false) with no slides. Set dryRun to true to receive the fully defaulted poll object without saving it, then persist it with Commit Staged Object. |
| Create Slide | `createSlide` | Creates a new slide (question) inside a poll you own. The handle is generated from the title and the title defaults to "Slide N" when omitted. With dryRun true the slide object is built with defaults and returned without saving (pollId is then optional); persist it later with Commit Staged Object. |
| Create Webhook | `createWebhook` | Registers a signed webhook on a survey so its responses are delivered to an https endpoint. Deliveries carry an HMAC X-Zigpoll-Signature header (t=&lt;unix ms&gt;,v1=&lt;hex&gt;, HMAC-SHA256 over "&lt;t&gt;.&lt;raw body&gt;") and are retried. The account's signing secret is returned only in this response. Requires an admin-tier API key. |
| Delete Webhook | `deleteWebhook` | Removes a signed webhook from a survey by its key and stops its deliveries, including pending retries. The key is scoped to the given survey. Requires an admin-tier API key. |
| Duplicate Poll | `duplicatePoll` | Creates a clean copy of a poll with its slides but without response data, for example to run a fresh round of synthetic research. The title defaults to the original title plus " (Copy)". |
| Generate Survey Link | `generateSurveyLink` | Generates a unique, trackable survey link for a poll. Each call creates a new activity record and returns a URL to hand to one respondent; optional metadata is attached to the activity for tracking. Counts against the plan's monthly survey link limit. |
| Get Account | `getAccount` | Returns one Zigpoll account by id, with its plan, poll ids, team and the account-level response, answer and write-in counters. Requires a plan with API access. |
| Get Attribution Report | `getAttributionReport` | Returns attributed revenue, orders, average order value and share per answer for a "How did you hear about us?" style question, bucketed by day, week or month, with the previous window of equal length for comparison and a cross-tab of answers against one traffic field. |
| Get Current User | `getCurrentUser` | Returns the Zigpoll user that owns the connected API key, including the ids of the accounts they belong to. |
| Get Device Breakdown | `getDeviceBreakdown` | Returns the distribution of respondents by device type, browser and operating system for an account, poll or slide. truncated is true when more distinct user agents existed than distinctUserAgentLimit. |
| Get Location Breakdown | `getLocationBreakdown` | Returns the country, region and city distribution of respondents for an account, poll or slide, derived from participant IP geolocation. Each list is a top 25; truncated flags any list that was cut. |
| Get Poll | `getPoll` | Returns one poll (survey) by id, including its status, visibility, page rules, slide ids and counters. |
| Get Poll Action Logic | `getPollActionLogic` | Returns a survey's current Action Logic rules together with everything needed to write new ones: the actions the account can use now, the actions available once an integration is connected, the survey-level rules and each slide's valid rule operators and answer values. |
| Get Poll Translations | `getPollTranslations` | Returns a poll's translation state: the languages it is translated into with per-language coverage, the widget CTA keys that can be translated and the translatable source content of every slide. Pass a language to also receive that language's translation layer. |
| Get Response Metadata Breakdown | `getResponseMetadataBreakdown` | Returns a server-side aggregation of response metadata (utm_source, referrer, landing page and custom keys). Call without key to discover which keys exist and how many responses carry each; call with key for that key's top values, broken down by answer when a slideId is also given. |
| Get Response Trends | `getResponseTrends` | Returns response volume bucketed by day. With a slideId the buckets are per answer option; with only a pollId or accountId the unit is distinct responding participants per day. Defaults to a trailing 90-day window. |
| Get Slide | `getSlide` | Returns one slide (question) by id with its answer options and vote counts. Matrix slides also return a rows array with per-row vote counts. |
| Get Synthetic Research Status | `getSyntheticResearchStatus` | Returns the current status and progress of synthetic research running on a poll. |
| List Accounts | `listAccounts` | Returns every Zigpoll account the connected user belongs to, with plan details, poll ids, team members and the account-level response, answer and write-in counters. |
| List Emails | `listEmails` | Returns the email addresses captured by surveys for an account, poll or slide with cursor pagination. Supply exactly one of accountId, pollId or slideId. |
| List Insights | `listInsights` | Returns the automated AI insight objects generated for an account, poll or slide with cursor pagination. Supply exactly one of accountId, pollId or slideId. |
| List Participants | `listParticipants` | Returns participant objects for an account, poll or slide with cursor pagination. Supply exactly one of accountId, pollId or slideId. Each participant carries their IP geolocation, user agent, the polls and slides they responded to and their response ids. |
| List Polls | `listPolls` | Returns all polls (surveys) belonging to an account, with status, visibility, page rules, slide ids and the per-survey render, open, engagement, response and completion counters. |
| List Responses | `listResponses` | Returns response objects for an account, poll or slide with cursor pagination. Supply exactly one of accountId, pollId or slideId. Each response carries the participant, order value, metadata (UTM, referrer, landing page), the compiled display string and the individual selected answers. |
| List Slides | `listSlides` | Returns all slides (questions) of a poll in survey order, with each answer option's vote count. Pass createdAfter and/or createdBefore to recompute vote counts from responses inside that time window. |
| List Webhooks | `listWebhooks` | Lists the signed webhooks registered on a survey. These are the account-level webhooks signed with the X-Zigpoll-Signature header and retried on failure. The signing secret is never returned here. Requires an admin-tier API key. |
| Reorder Slides | `reorderSlides` | Sets the order in which a survey's slides appear. slideIds must be the complete ordered list of every slide on the survey, with no duplicates or foreign ids; a partial list is rejected. |
| Send Email Campaign | `sendEmailCampaign` | Sends an email survey invitation for a poll to one or more recipients. Enforces the plan's email limits, spam detection and bulk-send validation. This delivers mail to real people; use with care. |
| Send SMS Campaign | `sendSmsCampaign` | Sends an SMS survey invitation for a poll to one or more phone numbers. Numbers are normalised and deduplicated; the plan's SMS limits, spam detection and bulk-send validation apply. This delivers messages to real people; use with care. |
| Set Poll Action Logic | `setPollActionLogic` | Replaces a survey's complete Action Logic. Each row pairs rules with actions: when every rule passes, every action runs. Call Get Poll Action Logic first, because this overwrites the whole array; an empty array clears all rows. |
| Start Synthetic Research | `startSyntheticResearch` | Starts AI-powered synthetic research on a poll, generating realistic survey responses from weighted demographic personas. The generation runs asynchronously; monitor it with Get Synthetic Research Status. Counts against the plan's monthly synthetic submission limit. |
| Update Poll | `updatePoll` | Updates an existing poll (survey). Only the fields you include are changed; counters, timestamps and the slides list are system-managed and ignored. A poll cannot be made visible while it has no slides or is archived. |
| Update Poll Translations | `updatePollTranslations` | Writes translations for one language of a poll without touching other languages. By default the translations are deep-merged into the language's existing layer (set a key to null to delete it); set replace to swap the whole layer or remove to delete the language. |
| Update Slide | `updateSlide` | Updates an existing slide (question). Only the fields you include are changed; counters, insights and timestamps are system-managed and ignored. The handle is regenerated from the title. Send -1 for a field to remove it from the slide. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Responses Submitted | `submitted-responses` | Delivered on every submission to the survey, including respondents who stop partway. Registered with notificationRules 'always'. Responses are briefly batched, so one delivery can contain several answers from the same respondent. Deliveries are signed with the X-Zigpoll-Signature header (t=&lt;ms&gt;,v1=&lt;hex&gt;, HMAC-SHA256 over '&lt;t&gt;.&lt;raw body&gt;') using the account signing secret returned by the subscription; verify it in your workflow. |
| Survey Completed | `completed-survey` | Delivered only once the respondent reaches the end of the survey. Registered with notificationRules 'strict'. Deliveries are signed with the X-Zigpoll-Signature header (t=&lt;ms&gt;,v1=&lt;hex&gt;, HMAC-SHA256 over '&lt;t&gt;.&lt;raw body&gt;') using the account signing secret returned by the subscription; verify it in your workflow. |
