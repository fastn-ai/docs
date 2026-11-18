---
description: "Breezy HR is a visual pipeline recruiting/ATS platform."
---

# Breezy HR

Breezy HR is a visual pipeline recruiting/ATS platform. This connector wraps the Breezy HR REST API v3 covering companies, positions, candidates, pipelines, questionnaires, templates, and webhook management.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [breezy.hr](https://breezy.hr) |
| **Authentication** | Credentials you enter |
| **Actions** | 49 |
| **Events** | 0 |
| **Slug** | `breezyhr` |

## Use it

Add Breezy HR from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.breezyhr.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Candidate | `addCandidate` | Add a new candidate to a position's pipeline. |
| Create Position | `createPosition` | Create a new open position or candidate pool for a company. |
| Create Webhook Endpoint | `createWebhookEndpoint` | Register a new HTTPS webhook endpoint for a company to receive event notifications (candidate/position/note changes). |
| Delete Webhook Endpoint | `deleteWebhookEndpoint` | Delete a webhook endpoint by id. |
| Get Candidate | `getCandidate` | Get a single candidate by id within a position. |
| Get Candidate Assessments | `getCandidateAssessments` | List skills assessment results for a candidate. |
| Get Candidate Background Checks | `getCandidateBackgroundChecks` | List background check results for a candidate. |
| Get Candidate Conversation | `getCandidateConversation` | Get the email/message conversation thread with a candidate. |
| Get Candidate Custom Fields | `getCandidateCustomFields` | Get custom field values set on a candidate. |
| Get Candidate Documents | `getCandidateDocuments` | List documents uploaded/attached to a candidate. |
| Get Candidate Meta | `getCandidateMeta` | Get metadata (source, ratings, tags) for a candidate. |
| Get Candidate Questionnaires | `getCandidateQuestionnaires` | List questionnaires sent to / completed by a candidate. |
| Get Candidate Resume | `getCandidateResume` | Get the parsed/raw resume info for a candidate. |
| Get Candidate Stream | `getCandidateStream` | Get the activity stream (notes, stage moves, emails) for a candidate. |
| Get Company | `getCompany` | Get a single company by id. |
| Get Company Custom Attributes | `getCompanyCustomAttributes` | Get a company-level custom attribute definition by id. |
| Get Company Custom Fields | `getCompanyCustomFields` | Get a company-level custom field definition by id. |
| Get Current User | `getUser` | Get the authenticated user's basic info. |
| Get Health | `getHealth` | Health check endpoint. Does not require authentication. |
| Get Pipeline | `getPipeline` | Get a single recruiting pipeline (with its stages) by id. |
| Get Position | `getPosition` | Get a single position/candidate pool by id. |
| Get Position Custom Fields | `getPositionCustomFields` | Get custom field values set on a position. |
| Get Position Stream | `getPositionStream` | Get the activity stream (notes/events) for a position. |
| Get Position Team | `getPositionTeam` | Get the hiring team members assigned to a position. |
| Get Questionnaire | `getQuestionnaire` | Get a single candidate questionnaire by id. |
| Get Template | `getTemplate` | Get a single position/email template by id. |
| Get User Details | `getUserDetails` | Get detailed profile info for the authenticated user. |
| Get Webhook Endpoint | `getWebhookEndpoint` | Get a single webhook endpoint by id. |
| List Candidates | `listCandidates` | List candidates in a position's pipeline. |
| List Categories | `listCategories` | List position categories configured for a company. |
| List Companies | `listCompanies` | List all companies (organizations) the authenticated user has access to. |
| List Departments | `listDepartments` | List departments configured for a company. |
| List Pipelines | `listPipelines` | List recruiting pipelines (stage templates) configured for a company. |
| List Positions | `listPositions` | List open/closed positions and candidate pools for a company. |
| List Questionnaires | `listQuestionnaires` | List candidate questionnaires configured for a company. |
| List Templates | `listTemplates` | List position/email templates configured for a company. |
| List Webhook Endpoints | `listWebhookEndpoints` | List webhook endpoints configured for a company. |
| Move Candidate | `moveCandidate` | Move a candidate to a different position/pool and stage. |
| Pause Webhook Endpoint | `pauseWebhookEndpoint` | Pause an active webhook endpoint. |
| Post Candidate Note | `postCandidateNote` | Post a note to a candidate's activity stream. |
| Resume Webhook Endpoint | `resumeWebhookEndpoint` | Resume a paused webhook endpoint. |
| Search Candidates | `searchCandidates` | Search all candidates across a company by query string. |
| Search Company Candidates | `searchCompanyCandidates` | Search/list candidates across the whole company by free-text query or exact email, paginated. |
| Send Candidate Message | `sendCandidateMessage` | Send an email message to a candidate. |
| Set Candidate Stage | `setCandidateStage` | Move a candidate to a different stage within their current pipeline. |
| Set Position State | `setPositionState` | Change a position's lifecycle state (e.g. activate, put on hold, close/fill, cancel). |
| Update Candidate | `updateCandidate` | Partially update a candidate's basic fields. |
| Update Position | `updatePosition` | Partially update an existing position's fields. |
| Update Webhook Endpoint | `updateWebhookEndpoint` | Update an existing webhook endpoint's URL, description, or subscribed events. |
