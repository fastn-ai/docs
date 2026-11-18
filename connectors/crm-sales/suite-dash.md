---
description: "SuiteDash is an all-in-one white-label client portal, CRM and business management platform."
hidden: true
---

# SuiteDash

<img src="../../.gitbook/assets/connectors/suite-dash.png" alt="SuiteDash logo" width="64">

SuiteDash is an all-in-one white-label client portal, CRM and business management platform. This connector wraps the SuiteDash Secure API (v1, https://app.suitedash.com/secure-api): CRM contacts (list with creation date filters, find by UID or email, create, update), CRM companies (list, find by UID or name, create with an optional primary contact, update), projects (list, find by UID, exact name, name substring or most recent, update), attribute metadata for contacts, companies and projects including custom fields, marketing audience subscriptions, and Worlds (WORLDS Power-up). Authentication uses the Public ID and Secret Key from Manage Account &gt; Secure API, sent as the X-Public-ID and X-Secret-Key headers.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [suitedash.com](https://suitedash.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `suiteDash` |

## Use it

Add SuiteDash from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.suiteDash.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Company | `createCompany` | Creates a SuiteDash CRM company with a name and role (Lead, Prospect or Client). Optionally links a primary contact by email, creating it when create_primary_contact_if_not_exists is true, and assigns the primary contact to Worlds. Call Get Company Meta Attributes for the full attribute list. |
| Create Contact | `createContact` | Creates a SuiteDash CRM contact with a role (Lead, Prospect or Client), first name, last name and email. The API rejects a blank email for every role, including Lead. send_welcome_email controls whether a portal access invitation is emailed. Call Get Contact Meta Attributes for the full attribute list. |
| Get Company | `getCompany` | Retrieves a single SuiteDash CRM company by UID or exact name, including phones, website, address, category, primary contact, tags, custom fields and Worlds. Optionally returns attribute metadata. |
| Get Company Meta Attributes | `getCompanyMetaAttributes` | Retrieves metadata for every SuiteDash CRM company attribute: type, format, required and nullable flags, allowed values, field label and which operations (read, create, update) accept it. |
| Get Contact | `getContact` | Retrieves a single SuiteDash CRM contact by UID or email, including phones, address, companies, circles, tags, custom fields and Worlds. Optionally returns attribute metadata. |
| Get Contact Meta Attributes | `getContactMetaAttributes` | Retrieves metadata for every SuiteDash CRM contact attribute: type, format, required and nullable flags, allowed values, field label and which operations (read, create, update) accept it. Use it to discover custom fields before creating or updating contacts. |
| Get Project | `getProject` | Retrieves a single SuiteDash project located by type: uid (identifier is the project UID), name (exact name), contains_the_following (identifier is a substring of the name) or most_recent (identifier must be true). Returns status, dates, economics, client, secondary clients, team, leader, teammates and custom fields. |
| Get Project Meta Attributes | `getProjectMetaAttributes` | Retrieves metadata for every SuiteDash project attribute: type, format, required and nullable flags, allowed values, field label and which operations (read, create, update) accept it. |
| List Companies | `listCompanies` | Lists SuiteDash CRM companies (idle companies are excluded), 10 per page, with optional creation date-time range filters (createdMin/createdMax, exclusive, RFC3339 with offset), ordering by created or name, and optional attribute metadata. |
| List Contacts | `listContacts` | Lists SuiteDash CRM contacts, 10 per page, with optional creation date-time range filters (createdMin/createdMax, exclusive, RFC3339 with offset), ordering by created or name, and optional attribute metadata. |

<details>

<summary>See 6 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Projects | `listProjects` | Lists SuiteDash projects, 10 per page, with optional creation date-time range filters (createdMin/createdMax, exclusive, RFC3339 with offset), ordering by name, created, start date or end date, and optional attribute metadata. |
| List Worlds | `listWorlds` | Lists SuiteDash Worlds, 10 per page, ordered by key, title or created. Only available on accounts with the WORLDS Power-up. |
| Subscribe Contacts To Marketing Audiences | `subscribeContactsToMarketingAudiences` | Subscribes one or more contacts (by email, with optional first and last name) to SuiteDash marketing audiences by audience ID. The top-level success is false if any item failed; per-item results and errors are returned in data. Subscribed contacts can receive that audience's marketing emails. |
| Update Company | `updateCompany` | Updates a SuiteDash CRM company identified by UID or exact name: name, phones, category, website, address, tags, background info, quizzes, community membership, Worlds and public, private or target custom fields. Only the fields you pass are changed. |
| Update Contact | `updateContact` | Updates a SuiteDash CRM contact identified by UID or email: name, emails, phones, title, website, address, company (optionally creating it), tags, circles, Worlds, background info, notes, quizzes, community membership and custom fields. Only the fields you pass are changed; send_welcome_email sends the portal welcome email only if it was never sent. |
| Update Project | `updateProject` | Updates a SuiteDash project located by type (uid, name, contains_the_following or most_recent) and identifier: name, status (a value from Categories &gt; Project Statuses), start date, estimated completion date, due time, staff and client information, economics (business sector, estimated value and currency, time tracking requirement) and project custom fields. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Automation Webhook | `automation_webhook` | A general-purpose delivery sent by a SuiteDash No-Code Automation whose action is 'Send Webhook'. Register it per automation: Flyout Menu &gt; Automations, open or create the automation, add the 'Send Webhook' action, paste the fastn trigger URL and choose (or build) the payload template - SuiteDash lets you save reusable webhook payload templates including CRM custom fields. Because the trigger and the payload are both chosen by the administrator, include a literal field named 'event' with the value 'automation_webhook' in the template so fastn can route the delivery, and add your own field identifying which automation fired. There is no fixed vendor payload for this event. |
| Project Created | `project_created` | Fires when a project is created. Register it once per SuiteDash account: Flyout Menu &gt; Integrations &gt; Webhooks &gt; Projects, toggle 'Project Created', use the arrow to select which project fields are sent, then 'Configure Webhook Endpoints' &gt; '+Add Webhook Endpoint', paste the fastn trigger URL, pick 'Project Created', toggle active and save. Add a literal field named 'event' with the value 'project_created' in the field selector so fastn can route the delivery. The payload is administrator-composed from the project fields you toggle; the schema below lists the project attributes SuiteDash exposes (confirmed against Get Project Meta Attributes). |
| Project Deleted | `project_deleted` | Fires when a project is deleted. Register it once per SuiteDash account: Flyout Menu &gt; Integrations &gt; Webhooks &gt; Projects, toggle 'Project Deleted', select the project fields, then 'Configure Webhook Endpoints' &gt; '+Add Webhook Endpoint', paste the fastn trigger URL, pick 'Project Deleted', toggle active and save. Add a literal field named 'event' with the value 'project_deleted' in the field selector so fastn can route the delivery. The deleted project can no longer be fetched with Find a Project, so capture everything you need from the payload itself. The payload is administrator-composed; the schema is the recommended field set. |
| Project Updated | `project_updated` | Fires when a project is updated. Register it once per SuiteDash account: Flyout Menu &gt; Integrations &gt; Webhooks &gt; Projects, toggle 'Project Updated', select the project fields, then 'Configure Webhook Endpoints' &gt; '+Add Webhook Endpoint', paste the fastn trigger URL, pick 'Project Updated', toggle active and save. Add a literal field named 'event' with the value 'project_updated' in the field selector so fastn can route the delivery. The payload is administrator-composed; the schema lists the project attributes SuiteDash exposes. |
| Subscription Canceled | `subscription_canceled` | Fires when a billing subscription is canceled. Register it once per SuiteDash account: Flyout Menu &gt; Integrations &gt; Webhooks &gt; Billing, toggle 'Subscription Canceled', select the data fields, then 'Configure Webhook Endpoints' &gt; '+Add Webhook Endpoint', paste the fastn trigger URL, pick 'Subscription Canceled', toggle active and save. Add a literal field named 'event' with the value 'subscription_canceled' in the field selector so fastn can route the delivery. The payload is administrator-composed; the schema is the recommended field set. |
| Subscription Created | `subscription_created` | Fires when a billing subscription is created. SuiteDash has no webhook registration API, so an administrator must register the endpoint once per SuiteDash account: Flyout Menu &gt; Integrations &gt; Webhooks &gt; Billing, toggle 'Subscription Created' on, use the arrow to select which data fields are sent, then 'Configure Webhook Endpoints' &gt; '+Add Webhook Endpoint', paste the fastn trigger URL, pick 'Subscription Created' from the dropdown, toggle it active and save. SuiteDash sends no event-type discriminator, so in the same field selector add a literal field named 'event' with the value 'subscription_created', otherwise fastn cannot route the delivery. The payload body is composed by the administrator from the toggled fields, so the schema below is the recommended field set, not a fixed vendor contract - use the Preview button in SuiteDash to see the exact shape your selection produces. |
| Subscription Expired | `subscription_expired` | Fires when a billing subscription expires. Register it once per SuiteDash account: Flyout Menu &gt; Integrations &gt; Webhooks &gt; Billing, toggle 'Subscription Expired', select the data fields, then 'Configure Webhook Endpoints' &gt; '+Add Webhook Endpoint', paste the fastn trigger URL, pick 'Subscription Expired', toggle active and save. Add a literal field named 'event' with the value 'subscription_expired' in the field selector so fastn can route the delivery. The payload is administrator-composed; the schema is the recommended field set. |
| Subscription Unpaid | `subscription_unpaid` | Fires when a billing subscription becomes unpaid. Register it once per SuiteDash account: Flyout Menu &gt; Integrations &gt; Webhooks &gt; Billing, toggle 'Subscription Unpaid', select the data fields, then 'Configure Webhook Endpoints' &gt; '+Add Webhook Endpoint', paste the fastn trigger URL, pick 'Subscription Unpaid', toggle active and save. Add a literal field named 'event' with the value 'subscription_unpaid' in the field selector so fastn can route the delivery. The payload is administrator-composed; the schema is the recommended field set. |
