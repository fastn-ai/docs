---
description: "Apollo.io REST API (base https://api.apollo.io/v1)."
hidden: true
---

# Apollo

<img src="../../.gitbook/assets/connectors/lg/apollo.png" alt="Apollo logo">

Apollo.io REST API (base https://api.apollo.io/v1). People & organization enrichment, people/contacts/accounts/organizations search and CRUD, sequences (emailer campaigns), deals (opportunities), tasks, users, email accounts, and labels. Auth: API key in the x-api-key header. Note: Apollo has no public webhook API.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [apollo.io](https://apollo.io) |
| **Authentication** | API key, OAuth 2.0 |
| **Slug** | `apollo` |

## Use it

Add Apollo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.apollo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Sequence | `activateSequence` | Activate a sequence. Starts an inactive sequence so contacts in it begin receiving steps. |
| Add Contacts To Sequence | `addContactsToSequence` | Add contacts to a sequence. Adds contacts (by ID or by list name) to a sequence, sending from one or more linked mailboxes. Requires a mailbox linked to the Apollo account; the same sequence ID must be passed as both sequence_id and emailer_campaign_id. |
| Add Records To List | `addRecordsToList` | Add records to a list. Adds existing contacts or accounts to one or more lists referenced by name, creating any list that does not yet exist for that modality. Invalid IDs are ignored. Set async to true for large batches. |
| Archive Sequence | `archiveSequence` | Archive a sequence. Marks a sequence inactive and archived, finishing all contacts in it. Apollo has no hard delete for sequences; archiving is the cleanup path. |
| Bulk Create Accounts | `bulkCreateAccounts` | Bulk create accounts. Creates up to 100 accounts in one request with optional deduplication, returning separate arrays for newly created and already existing accounts. |
| Bulk Create Contacts | `bulkCreateContacts` | Bulk create contacts. Creates up to 100 contacts in one request with optional deduplication, returning separate arrays for newly created and already existing contacts. |
| Bulk Create Tasks | `createTask` | Bulk create tasks. Creates one task per contact in contact_ids, all owned by user_id, with the same type, priority, status, due date and note. Use Create Single Task for one contact. |
| Bulk Enrich Organizations | `bulkEnrichOrganizations` | Bulk organization enrichment. Enriches up to 10 companies by domain, or by details objects combining domain, LinkedIn URL, website and name. Consumes 1 credit per organization. |
| Bulk Enrich People | `bulkEnrichPeople` | Bulk people enrichment. Enriches up to 10 people in one call; each details entry accepts the same identifiers as Enrich Person. Credits are consumed per matched person when data is found. |
| Bulk Update Accounts | `bulkUpdateAccounts` | Bulk update accounts. Updates many accounts at once, either applying the same name, owner or stage to a list of account_ids, or applying per-account changes via account_attributes. |

<details>

<summary>See 70 more actions</summary>

* **Bulk Update Contacts** `bulkUpdateContacts`: Bulk update contacts. Updates many contacts at once, either applying the same field values to a list of contact_ids, or applying per-contact changes via contact_attributes. Automatically asynchronous above 100 contacts.
* **Check Email Send Status** `checkEmailSendStatus`: Check email send status. Checks the current delivery status of an email message, typically after Send Email Now, since sending is asynchronous. Returns 404 if the message does not belong to your team.
* **Complete Task** `completeTask`: Complete a task. Marks an existing task as completed, optionally recording a note.
* **Create Account** `createAccount`: Create an account. Creates a company saved in your Apollo account with name, domain, owner, stage, phone, address and custom fields. Consumes no credits.
* **Create Call Record** `createCallRecord`: Create call records. Logs a call made in an outside dialer (Orum, Nooks, etc.) as a call record in Apollo. This cannot place calls.
* **Create Contact** `createContact`: Create a contact. Creates a person saved in your Apollo account with name, employer, title, email, phones, address, stage, lists and custom fields. Set run_dedupe to match existing contacts instead of always creating a new one. Consumes no credits.
* **Create Custom Field** `createCustomField`: Create a custom field. Adds a custom contact, account or deal field to the Apollo account so the team can capture details unique to their process and use them in sequences.
* **Create Deal** `createDeal`: Create deal. Creates a sales opportunity with name, owner, account, amount, stage, expected close date and custom fields. Consumes no credits.
* **Create Email Draft** `createEmailDraft`: Create an email draft. Creates a single unsent email (status drafted) for a contact, optionally as a reply to an existing message or from a template. Send it with Send Email Now. Requires a linked mailbox in Apollo.
* **Create List** `createList`: Create a list. Creates a new empty contact or account list (label). Name must be unique per modality within the team. Add records afterwards with Add Records To List.
* **Create Sequence** `createSequence`: Create a sequence. Creates a new outreach sequence (emailer campaign) in the team's Apollo account with its sending schedule, safety settings and labels. Sequences are created inactive unless active is true; the owner is always the user the API key acts as (reassign with Update Sequence).
* **Create Single Task** `createSingleTask`: Create a task. Creates one task for a single contact, assigned to a team user, with type, priority, status, due date, optional title and note. Apollo does not deduplicate tasks. Use Create Task (bulk_create) to create the same task for many contacts.
* **Deactivate Sequence** `deactivateSequence`: Deactivate a sequence. Stops an active sequence, pausing all contacts in it.
* **Enrich Organization** `enrichOrganization`: Organization enrichment. Enriches one company from the Apollo database by domain, LinkedIn URL or website, optionally with name to improve matching. Consumes 1 credit.
* **Enrich Person** `enrichPerson`: People enrichment. Enriches one person from the Apollo database by name, email, hashed email, employer, domain, LinkedIn URL or Apollo ID. Set reveal_personal_emails or reveal_phone_number to unlock contact data (phone reveal is asynchronous and requires webhook_url). Consumes 1 to 9 credits per person when data is found; free accounts need a work email.
* **Export Conversations** `exportConversations`: Export conversations. Starts an asynchronous export of recorded conversations within a time range and notifies a team member by email when ready. Retrieve the download URL with Get Conversations Export.
* **Get Account** `getAccount`: Retrieve a single account (company) by its Apollo ID (GET /v1/accounts/{id}).
* **Get API Usage Stats** `getApiUsageStats`: View API usage stats. Returns, for every endpoint the API key can call, the per-minute, per-hour and per-day rate limit with consumed and left_over counts. Keys are JSON-encoded [controller, action] pairs such as ["api/v1/contacts", "search"].
* **Get Contact** `getContact`: Retrieve a single contact by its Apollo ID (GET /v1/contacts/{id}).
* **Get Contact Sequence Activity** `getContactSequenceActivity`: Get contact sequence activity. Retrieves one contact's sequence timeline: enrolled, paused, resumed, failed, completed, removed and replied events, newest first. Returns 404 if the contact does not belong to your team.
* **Get Conversation** `getConversation`: Get conversations info. Retrieves the full details of a single recorded conversation (video meeting or dialer call) by its ID. Find IDs with Search Conversations.
* **Get Conversations Export** `getConversationsExport`: Get conversations export. Retrieves a signed download URL for a conversations export previously started with Export Conversations.
* **Get Credit Usage Stats** `getCreditUsageStats`: View credit usage stats. Monitors the team's credit balance across every credit type in the current billing cycle. For each credit type the response returns limit, consumed and left_over; current_credit_cycle reports the cycle's start and end dates.
* **Get Current User Profile** `getCurrentUserProfile`: Get current user profile. Retrieves the authenticated profile of the person the API key acts as. Set include_credit_usage to true to also return the user's and team's credit usage and remaining balances. Returns 401 without valid credentials, which makes it the credential verification action for this connector.
* **Get Deal** `getDeal`: Retrieve a single deal/opportunity by its Apollo ID (GET /v1/opportunities/{id}).
* **Get Email Content** `getEmailContent`: Get email content. Retrieves the subject, body and recipients of up to 10 emails the team has already sent, as plain text or original HTML. Drafted, scheduled and failed emails are not returned.
* **Get Email Stats** `getEmailStats`: Check email stats. Reviews the complete details for an email sent as part of an Apollo sequence: content, open and click stats, and the receiving contact.
* **Get Organization** `getOrganization`: Get complete organization info. Retrieves complete details about a company in the Apollo database by its Apollo organization ID. Organizations are companies not yet saved as accounts. Consumes 1 credit per company.
* **Get Person** `getPerson`: Get complete person info. Retrieves complete details about a person in the Apollo database by Apollo person ID, including employment history, location and current organization. For people not saved as contacts the email field holds the placeholder email_not_unlocked@domain.com rather than a real address. Consumes 1 credit per person.
* **Get Task** `getTask`: Get a task. Retrieves the full details for a single task in the team's Apollo account, including the associated account and contact when attached. Call tasks may include phone_call and email tasks emailer_message.
* **Get Webhook Result** `getWebhookResult`: Poll webhook result. Retrieves the payload Apollo delivered (or would have delivered) to the webhook_url of a people enrichment or bulk people enrichment request, using the request_id from that call. Available for 30 days. While processing it returns 404 with error_code result_pending and retry_after_seconds.
* **List Account Stages** `listAccountStages`: List all account stages (GET /v1/account_stages). Useful for categorizing accounts in the pipeline.
* **List Contact Deals** `listContactDeals`: View associated deals. Retrieves the deals (opportunities) associated with a contact. Returns 200 with an empty array when the contact has no deals or the ID is unknown.
* **List Contact Stages** `listContactStages`: List all contact stages (GET /v1/contact_stages). Use a returned stage ID as contact_stage_id when updating a contact.
* **List Email Accounts** `listEmailAccounts`: List connected email accounts/mailboxes (GET /v1/email_accounts).
* **List Email Schedules** `listEmailSchedules`: List email schedules. Retrieves every sequence sending schedule for the team with its id, name, time zone, weekly sending windows and whether it is the default. Use a schedule id as emailer_schedule_id when creating or updating a sequence.
* **List Fields** `listFields`: Get a list of fields. Retrieves every field that exists in the Apollo account, including system, custom and CRM-synced fields. Filter by source to return only one kind.
* **List Lists** `listLabels`: Get a list of all lists. Retrieves every contact and account list (label) in your Apollo account. The API returns a bare JSON array of list objects; it is modelled here as items.
* **List Notes** `listNotes`: Get a list of notes. Retrieves notes attached to a contact, account, opportunity, calendar event or conversation, with sorting and pagination. At least one relation parameter (contact_id, account_id, opportunity_id, calendar_event_id or conversation_id) must be provided.
* **List Opportunity Stages** `listOpportunityStages`: List all deal/opportunity stages in the team's pipeline (GET /v1/opportunity_stages). Use the returned stage IDs when creating or updating deals.
* **List Organization Job Postings** `listOrganizationJobPostings`: Organization job postings. Retrieves the current job postings for a company in the Apollo database, useful for spotting companies growing headcount in areas that matter to you. Display limit of 10,000 records. Consumes 1 credit per page.
* **List Typed Custom Fields** `listTypedCustomFields`: Get a list of all custom fields. Deprecated by Apollo in favour of List Fields with source=custom, but still served. Retrieves every custom field created in the Apollo account. Takes no parameters.
* **Query Analytics Report** `queryAnalyticsReport`: Query analytics report. Programmatically queries Apollo analytics for aggregated sales activity: pick metrics, a row dimension, an optional pivot dimension, filters and a date range preset. Rate limited to 5 requests per hour.
* **Remove Records From List** `removeRecordsFromList`: Remove records from a list. Removes contacts or accounts from one or more lists referenced by name. The records themselves are not deleted. Invalid IDs are ignored. Set async to true for large batches.
* **Search Accounts** `searchAccounts`: Search for accounts. Searches the accounts (companies) saved in your Apollo account by name, stage, list and sort order. Consumes no credits.
* **Search Calls** `searchCalls`: Search for calls. Finds calls the team has made or received with the Apollo dialer, filtered by date range, duration, direction, users, purpose, outcome and keywords. Array filters are sent comma-joined, so pass a single value per array filter.
* **Search Contacts** `searchContacts`: Search for contacts. Searches the contacts saved in your Apollo account by keywords, stage, list and sort order. Consumes no credits.
* **Search Conversations** `searchConversations`: Search conversations. Finds recorded conversations (video meetings and dialer calls) with filters for type, account, contacts, date range, labels and scorecards. Results are summaries without transcripts or recording URLs.
* **Search Deals** `searchDeals`: List all deals. Lists the deals (opportunities) in your team's Apollo account with optional sorting and pagination. Consumes no credits.
* **Search News Articles** `searchNewsArticles`: News articles search. Finds news articles related to specific companies in the Apollo database, filtered by category and publish date.
* **Search Organizations** `searchOrganizations`: Organization search. Searches the Apollo company database by name, domain, headcount, location, revenue, technologies, keywords, funding and job postings. Consumes 1 credit per page.
* **Search Outreach Emails** `searchOutreachEmails`: Search for outreach emails. Finds emails the team created and sent as part of Apollo sequences, filtered by status, reply sentiment, sender, sequence, date range and keywords. Display limit of 50,000 records (100 per page). Array filters are sent comma-joined, so pass a single value per array filter.
* **Search People** `searchPeople`: People API search. Searches the Apollo people database by title, name, location, seniority, employer, email status, headcount, revenue, technologies and job postings. Results are obfuscated on some plans (no email or phone); use Enrich Person to unlock contact data. Consumes no credits.
* **Search Sequences** `searchSequences`: Search sequences / emailer campaigns (POST /v1/emailer_campaigns/search).
* **Search Tasks** `searchTasks`: Search for tasks. Lists the tasks in your team's Apollo account with sorting, pagination and an optional count of tasks by type. Consumes no credits.
* **Search Users** `searchUsers`: List users in your team (GET /v1/users/search).
* **Send Email Now** `sendEmailNow`: Send email now. Immediately queues an existing drafted, scheduled or failed email message for sending. Sending is asynchronous; confirm delivery with Check Email Send Status.
* **Skip Task** `skipTask`: Skip a task. Marks an existing task as skipped without completing it, optionally recording a note.
* **Update Account** `updateAccount`: Update an account. Changes an existing account's name, domain, owner, stage, phone, address or custom fields. Only the fields you send are changed.
* **Update Account Owners** `updateAccountOwners`: Update account owner for multiple accounts. Assigns several accounts to a different user in the team's Apollo account.
* **Update Call Record** `updateCallRecord`: Update call records. Updates an existing call record in Apollo, such as its status, duration, purpose, outcome or note.
* **Update Contact** `updateContact`: Update a contact. Changes an existing contact's name, employer, title, email, phones, address, stage, lists or custom fields. Only the fields you send are changed; label_names replaces the contact's lists.
* **Update Contact Owners** `updateContactOwners`: Update contact owner for multiple contacts. Assigns several contacts to a different user in the team's Apollo account.
* **Update Contact Stages** `updateContactStages`: Update contact stage for multiple contacts. Moves several contacts to a given contact stage. Use List Contact Stages for valid stage IDs.
* **Update Contact Status In Sequence** `updateContactStatusInSequence`: Update contact status in a sequence. Marks contacts as finished in, removes them from, or stops their progress in one or more sequences.
* **Update Custom Field** `updateCustomField`: Update a custom field. Renames a custom field, moves it to a field group, changes text max length or picklist values. Pass exactly one field object in the fields array; only the parameters included are changed. Modality and type cannot be changed.
* **Update Deal** `updateDeal`: Update deal. Changes an existing deal's owner, name, amount, stage, close date or custom fields. Only the fields you send are changed.
* **Update List** `updateList`: Update a list. Renames an existing list or toggles its Book of Business status. A list's modality cannot be changed after creation.
* **Update Sequence** `updateSequence`: Update a sequence. Changes an existing sequence's name, active state, owner, sending schedule, labels, daily cap, CC/BCC, sharing permission or steps. Only fields you send are changed; label_names replaces the existing labels.
* **Update Task** `updateTask`: Update a task. Changes the details of an existing task. Most fields only apply to tasks with scheduled status; use Complete Task or Skip Task to close a task. Only the fields you send are changed, except priority and creator_id which Apollo resets to defaults on scheduled tasks when omitted.

</details>
