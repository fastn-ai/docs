---
description: "Memberstack adds authentication, gated content, member profiles and Stripe-backed memberships to any website."
hidden: true
---

# Memberstack

Memberstack adds authentication, gated content, member profiles and Stripe-backed memberships to any website. This connector covers the Memberstack Admin REST API: member listing, retrieval, creation, update and deletion; custom fields, metadata and JSON storage; free-plan assignment and removal; member JWT verification; and the Data Tables API for listing tables and creating, querying, updating and deleting records.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [memberstack.com](https://memberstack.com) |
| **Authentication** | API key |
| **Actions** | 14 |
| **Events** | 11 |
| **Slug** | `memberstack` |

## Use it

Add Memberstack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.memberstack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Free Plan To Member | `addFreePlanToMember` | Grants a free plan to an existing member, immediately giving them that plan's permissions and gated content. Only free plans work here; paid plans must go through the Stripe checkout flow in the DOM package or the Stripe Customer Portal. A member can hold several plans at once. A plan ID that does not resolve returns the plan-not-found error. |
| Create Data Record | `createDataRecord` | Creates a record in one of your Memberstack data tables. Data holds the field values keyed by field key, and an optional Member ID assigns a member as the record's owner - the member must belong to the same app and the same live or sandbox environment. A record created without an owner is shown as 'System'. |
| Create Member | `createMember` | Creates a member in your Memberstack app with an email address and, optionally, a password, free plans, custom fields, metadata, JSON storage and a login redirect. Email addresses must be unique within the app. Only free plans (IDs starting with pln_) can be granted here; paid plans require the Stripe checkout flow in the DOM package. |
| Delete Data Record | `deleteDataRecord` | Permanently deletes a record from a Memberstack data table. A table or record that does not exist returns 404 with the message 'Data table not found' or 'Data record not found'. |
| Delete Member | `deleteMember` | Permanently removes a member from your Memberstack app, optionally deleting their Stripe customer and cancelling their Stripe subscriptions at the same time. This cannot be undone. An unknown member ID returns 400 with the message 'There is no member with this identifier.' |
| Get Data Table | `getDataTable` | Retrieves one data table by its key or its ID, including its access rules and the full definition of every field. A table that does not exist returns 404 with the message 'Data table not found'. |
| Get Member | `getMember` | Retrieves a single member by Memberstack ID or by email address. A member that does not exist is not an error: Memberstack answers 200 with data set to null, so assert the data field rather than the status code. |
| List Data Tables | `listDataTables` | Lists every data table in your Memberstack app together with its access rules and field definitions. Tables themselves are created in the Memberstack dashboard; the API manages their records. |
| List Members | `listMembers` | Retrieves a cursor-paginated page of the members in your Memberstack app, each with their authentication email, verification status, custom fields, metadata, permissions and plan connections. |
| Query Data Records | `queryDataRecords` | Queries the records of a Memberstack data table using a Prisma-style query object. Use Find Many with where, orderBy, select or include, take, skip or after and _count to search and page through records, or Find Unique with where.id to fetch exactly one. Find Many and Find Unique are mutually exclusive and one of them is required. |
| Remove Free Plan From Member | `removeFreePlanFromMember` | Removes a free plan from a member, immediately revoking the access that plan granted. Only free plans work here; a paid subscription must be cancelled through Stripe. A plan ID that does not resolve returns the plan-not-found error. |
| Update Data Record | `updateDataRecord` | Updates an existing record in a Memberstack data table. The update is partial, so include only the fields you want to change; the Data object may not be empty. Unique constraints are re-validated excluding this record, and reference constraints are validated for relationship fields. |
| Update Member | `updateMember` | Updates a member's email, verification status, profile image, login redirect, custom fields, metadata or JSON storage. Updates are partial. Custom Fields and Metadata are shallow-merged, so keys you omit are preserved and you can send a single key; Metadata additionally drops any key whose value is falsy. JSON is the exception and is replaced wholesale with the object you send. |
| Verify Member Token | `verifyMemberToken` | Verifies a member JWT issued by Memberstack and returns its decoded payload, so a server can trust the member ID behind a request. Any token problem - invalid signature, expiry, audience mismatch, malformed token or a missing token field - returns 400 with the code INVALID_TOKEN, never 401, so treat every non-200 response as an authentication failure. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Member Created | `member.created` | Fires immediately after a member finishes signing up, whether by password, social login, the Admin API or a CSV import. Setup: in the Memberstack dashboard open Dev Tools &gt; Webhooks, add an endpoint, paste the fastn trigger URL, then subscribe it to member.created. Payload schema modelled from Memberstack's documented sample, not captured from a live delivery. |
| Member Deleted | `member.deleted` | Fires when a member is deleted from the dashboard or through the Admin API, including bulk deletions. Setup: Memberstack dashboard &gt; Dev Tools &gt; Webhooks &gt; add endpoint, paste the fastn trigger URL, subscribe to member.deleted. Payload schema modelled from Memberstack's documented member sample. |
| Member Payment Failed | `member.payment.failed` | Fires when a member's payment fails. Listed on Memberstack's Webhooks feature page but not in the current Webhook Events Reference table, so confirm it appears in the event-type picker in Dev Tools &gt; Webhooks before relying on it. Setup: Memberstack dashboard &gt; Dev Tools &gt; Webhooks &gt; add endpoint, paste the fastn trigger URL, subscribe to member.payment.failed. Payload schema modelled from Memberstack's documented member sample. |
| Member Payment Succeeded | `member.payment.succeeded` | Fires when a member's payment is collected successfully. Listed on Memberstack's Webhooks feature page but not in the current Webhook Events Reference table, so confirm it appears in the event-type picker in Dev Tools &gt; Webhooks before relying on it. Setup: Memberstack dashboard &gt; Dev Tools &gt; Webhooks &gt; add endpoint, paste the fastn trigger URL, subscribe to member.payment.succeeded. Payload schema modelled from Memberstack's documented member sample. |
| Member Plan Added | `member.plan.added` | Fires when a member subscribes to a free or paid plan, or an admin grants one. Setup: Memberstack dashboard &gt; Dev Tools &gt; Webhooks &gt; add endpoint, paste the fastn trigger URL, subscribe to member.plan.added. Payload schema modelled from Memberstack's documented member sample. |
| Member Plan Canceled | `member.plan.canceled` | Fires when a member cancels a plan or a subscription is terminated for non-payment. Setup: Memberstack dashboard &gt; Dev Tools &gt; Webhooks &gt; add endpoint, paste the fastn trigger URL, subscribe to member.plan.canceled. Payload schema modelled from Memberstack's documented member sample. |
| Member Plan Replaced | `member.plan.replaced` | Fires when one of a member's plans is swapped for another. Listed on Memberstack's Webhooks feature page but not in the current Webhook Events Reference table, so confirm it appears in the event-type picker in Dev Tools &gt; Webhooks before relying on it. Setup: Memberstack dashboard &gt; Dev Tools &gt; Webhooks &gt; add endpoint, paste the fastn trigger URL, subscribe to member.plan.replaced. Payload schema modelled from Memberstack's documented member sample. |
| Member Plan Updated | `member.plan.updated` | Fires when a plan's status changes, for example trialing to active, active to past due, or a change of billing interval. Setup: Memberstack dashboard &gt; Dev Tools &gt; Webhooks &gt; add endpoint, paste the fastn trigger URL, subscribe to member.plan.updated. Payload schema modelled from Memberstack's documented member sample. |
| Member Updated | `member.updated` | Fires when any member data changes - custom fields, email, metadata or verification status. Setup: Memberstack dashboard &gt; Dev Tools &gt; Webhooks &gt; add endpoint, paste the fastn trigger URL, subscribe to member.updated. Payload schema modelled from Memberstack's documented member sample. |
| Team Member Added | `team.member.added` | Fires when a member joins a team through an invitation link. Setup: Memberstack dashboard &gt; Dev Tools &gt; Webhooks &gt; add endpoint, paste the fastn trigger URL, subscribe to team.member.added. Payload schema modelled from Memberstack's documented member sample. |
| Team Member Removed | `team.member.removed` | Fires when a member leaves or is removed from a team. Setup: Memberstack dashboard &gt; Dev Tools &gt; Webhooks &gt; add endpoint, paste the fastn trigger URL, subscribe to team.member.removed. Payload schema modelled from Memberstack's documented member sample. |
