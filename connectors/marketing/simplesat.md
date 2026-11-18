---
description: "Simplesat is a customer-satisfaction survey platform for CSAT, CES and NPS feedback."
---

# Simplesat

Simplesat is a customer-satisfaction survey platform for CSAT, CES and NPS feedback. This connector covers the Simplesat public API: survey responses and individual answers, customers, team members, surveys, questions, email survey sends and satisfaction metrics.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [simplesat.io](https://simplesat.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 20 |
| **Events** | 0 |
| **Slug** | `simplesat` |

## Use it

Add Simplesat from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.simplesat.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Upsert Customers | `bulkUpsertCustomers` | Creates or updates many Simplesat customers in one call. Each entry is matched on its email address, so existing customers are updated rather than duplicated. The upsert is processed asynchronously: the response acknowledges the request rather than returning the stored customers. |
| Create Or Update Customer | `createOrUpdateCustomer` | Creates a customer in Simplesat, or updates the existing one with the same email address. The email address is the key, so sending an existing email updates that customer rather than creating a duplicate. |
| Create Or Update Response | `createOrUpdateResponse` | Records a complete survey response in Simplesat, or updates the existing response matching the same ticket and customer. Use this to import feedback collected elsewhere or to sync historical responses. |
| Create Or Update Team Member | `createOrUpdateTeamMember` | Creates a Simplesat team member, or updates the existing one with the same email address or external id. Team members are the agents whose work is rated in survey responses. |
| Create Response | `createResponse` | Creates a new survey response in Simplesat without matching an existing one. Use Create Or Update Response when the response may already exist. This endpoint is live on the Simplesat API but is not listed in their published reference. |
| Get Answer | `getAnswerById` | Retrieves a single survey answer by its numeric Simplesat id, including the question, the rating, any comment and the detected sentiment and topics. |
| Get Customer | `getCustomerById` | Retrieves a single Simplesat customer by its numeric Simplesat id. |
| Get Metrics | `getMetrics` | Returns aggregated satisfaction metrics for a date range. The allowed metric names come from the surveys configured on the account, so call List Surveys first to see which metrics exist. This endpoint is live on the Simplesat API but is not listed in their published reference. |
| Get Response | `getResponseById` | Retrieves a complete survey response by its numeric Simplesat id, including every answer, the customer, the linked ticket and the team members involved. |
| Get Team Member | `getTeamMemberById` | Retrieves a single Simplesat team member by its numeric Simplesat id. |
| List Answers | `listAnswers` | Lists every survey answer in the account, newest first. This is Simplesat's simple paginated answers list; use Search Answers when you need date ranges or filters. |
| List Customers | `listCustomers` | Lists the customers stored in Simplesat, newest first, with optional filtering by creation or modification date and by survey-email subscription status. |
| List Questions | `listQuestions` | Lists the questions defined across the account's surveys, with their type, choices and follow-up rules. Filter by survey or by satisfaction metric. |
| List Surveys | `listSurveys` | Lists the surveys configured in the Simplesat account, including each survey's token, which is needed to send it by email. |
| Search Answers | `searchAnswers` | Searches survey answers by date range and by attribute filters such as sentiment, survey or team member. Returns a paginated list of matching answers. |
| Search Responses | `searchResponses` | Searches complete survey responses by submission, creation or modification date range and by attribute filters such as customer email or team member. Returns a paginated list of matching responses. |
| Send Survey By Email | `sendSurveyByEmail` | Sends a Simplesat survey to a customer by email. This delivers a real email to the address you supply, so only use it with addresses you control. |
| Update Answer | `updateAnswerById` | Updates an existing survey answer by its numeric Simplesat id, for example to correct the selected rating or the comment left by the customer. |
| Update Customer | `updateCustomerById` | Updates a Simplesat customer by its numeric Simplesat id. Only the fields you supply are changed; the email address cannot be changed here. |
| Update Response | `updateResponseById` | Replaces an existing survey response by its numeric Simplesat id, including its answers, customer, ticket and team members. |
