---
description: "Simplesat runs CSAT, CES and NPS surveys. Create and update responses, customers and team members, and read metrics."
hidden: true
---

# Simplesat

<img src="../../.gitbook/assets/connectors/lg/simplesat.png" alt="Simplesat logo">

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [simplesat.io](https://simplesat.io) |
| **Authentication** | API key |
| **Slug** | `simplesat` |

## Setup

Your customers enter their API key for Simplesat when they connect. Nothing else needs setting up.

## Use it

Add Simplesat from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.simplesat.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bulk Upsert Customers</td><td><code>bulkUpsertCustomers</code></td><td>Creates or updates many Simplesat customers in one call. Each entry is matched on its email address, so existing customers are updated rather than duplicated. The upsert is processed asynchronously: the response acknowledges the request rather than returning the stored customers.</td></tr><tr><td>Create Or Update Customer</td><td><code>createOrUpdateCustomer</code></td><td>Creates a customer in Simplesat, or updates the existing one with the same email address. The email address is the key, so sending an existing email updates that customer rather than creating a duplicate.</td></tr><tr><td>Create Or Update Response</td><td><code>createOrUpdateResponse</code></td><td>Records a complete survey response in Simplesat, or updates the existing response matching the same ticket and customer. Use this to import feedback collected elsewhere or to sync historical responses.</td></tr><tr><td>Create Or Update Team Member</td><td><code>createOrUpdateTeamMember</code></td><td>Creates a Simplesat team member, or updates the existing one with the same email address or external id. Team members are the agents whose work is rated in survey responses.</td></tr><tr><td>Create Response</td><td><code>createResponse</code></td><td>Creates a new survey response in Simplesat without matching an existing one. Use Create Or Update Response when the response may already exist. This endpoint is live on the Simplesat API but is not listed in their published reference.</td></tr><tr><td>Get Answer</td><td><code>getAnswerById</code></td><td>Retrieves a single survey answer by its numeric Simplesat id, including the question, the rating, any comment and the detected sentiment and topics.</td></tr><tr><td>Get Customer</td><td><code>getCustomerById</code></td><td>Retrieves a single Simplesat customer by its numeric Simplesat id.</td></tr><tr><td>Get Metrics</td><td><code>getMetrics</code></td><td>Returns aggregated satisfaction metrics for a date range. The allowed metric names come from the surveys configured on the account, so call List Surveys first to see which metrics exist. This endpoint is live on the Simplesat API but is not listed in their published reference.</td></tr><tr><td>Get Response</td><td><code>getResponseById</code></td><td>Retrieves a complete survey response by its numeric Simplesat id, including every answer, the customer, the linked ticket and the team members involved.</td></tr><tr><td>Get Team Member</td><td><code>getTeamMemberById</code></td><td>Retrieves a single Simplesat team member by its numeric Simplesat id.</td></tr></tbody></table>

<details>

<summary>View 10 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Answers</td><td><code>listAnswers</code></td><td>Lists every survey answer in the account, newest first. This is Simplesat's simple paginated answers list; use Search Answers when you need date ranges or filters.</td></tr><tr><td>List Customers</td><td><code>listCustomers</code></td><td>Lists the customers stored in Simplesat, newest first, with optional filtering by creation or modification date and by survey-email subscription status.</td></tr><tr><td>List Questions</td><td><code>listQuestions</code></td><td>Lists the questions defined across the account's surveys, with their type, choices and follow-up rules. Filter by survey or by satisfaction metric.</td></tr><tr><td>List Surveys</td><td><code>listSurveys</code></td><td>Lists the surveys configured in the Simplesat account, including each survey's token, which is needed to send it by email.</td></tr><tr><td>Search Answers</td><td><code>searchAnswers</code></td><td>Searches survey answers by date range and by attribute filters such as sentiment, survey or team member. Returns a paginated list of matching answers.</td></tr><tr><td>Search Responses</td><td><code>searchResponses</code></td><td>Searches complete survey responses by submission, creation or modification date range and by attribute filters such as customer email or team member. Returns a paginated list of matching responses.</td></tr><tr><td>Send Survey By Email</td><td><code>sendSurveyByEmail</code></td><td>Sends a Simplesat survey to a customer by email. This delivers a real email to the address you supply, so only use it with addresses you control.</td></tr><tr><td>Update Answer</td><td><code>updateAnswerById</code></td><td>Updates an existing survey answer by its numeric Simplesat id, for example to correct the selected rating or the comment left by the customer.</td></tr><tr><td>Update Customer</td><td><code>updateCustomerById</code></td><td>Updates a Simplesat customer by its numeric Simplesat id. Only the fields you supply are changed; the email address cannot be changed here.</td></tr><tr><td>Update Response</td><td><code>updateResponseById</code></td><td>Replaces an existing survey response by its numeric Simplesat id, including its answers, customer, ticket and team members.</td></tr></tbody></table>

</details>

## Events

Simplesat has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
