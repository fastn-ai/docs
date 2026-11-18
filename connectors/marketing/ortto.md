---
description: "Ortto is an AI-native customer data platform (CDP) and marketing automation tool."
hidden: true
---

# Ortto

<img src="../../.gitbook/assets/connectors/lg/ortto.png" alt="Ortto logo">

Ortto is an AI-native customer data platform (CDP) and marketing automation tool. This connector covers people/contacts, accounts (organizations), audiences, custom fields, custom activities and definitions, tags, campaigns, transactional email and push, reports, Talk conversations, knowledge base, and business fields via the Ortto public API (ap3api).

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [ortto.com](https://ortto.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `ortto` |

## Use it

Add Ortto from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ortto.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contacts to Account | `addAccountContacts` | Associates one or more people with an account (organization). Identify people with inclusion_ids or a filter and target the account via account_id. Returns an empty object on success. |
| Add Emails to Suppression List | `addEmailSuppression` | Adds one or more email addresses to the email suppression list so they will not receive email. |
| Archive Accounts | `archiveAccounts` | Archives one or more accounts (organizations). Identify with inclusion_ids, all_rows_selected/exclusion_ids, or a filter. |
| Archive People | `archivePeople` | Archives one or more people. Identify contacts with inclusion_ids, or use all_rows_selected with optional exclusion_ids, or a filter. |
| Compose Talk Conversation | `composeTalkConversation` | Creates a new Ortto Talk conversation for a person, merging the person into the CDP and adding one or more initial messages (text or HTML). |
| Create Account Custom Activity Event | `createAccountActivityEvent` | Creates one or more custom activity events against accounts (organizations) in Ortto's CDP. Each activity references an account activity_id (act:oc:...), attributes, and account fields for matching. |
| Create Account Custom Field | `createAccountCustomField` | Creates a custom field on the account (organization) object in Ortto's CDP. single_select and multi_select types require the values array. |
| Create Business Field | `createBusinessField` | Creates a custom business field (company-level profile field) in Ortto's CDP. |
| Create Custom Activity Definition | `createActivityDefinition` | Creates a custom activity definition (schema) in Ortto's CDP, including its attributes and display style. |
| Create Custom Activity Event | `createActivityEvent` | Creates one or more custom activity events against people in Ortto's CDP. Each activity references an activity_id (act:cm:...), attributes keyed by field IDs, and person fields for matching. |

<details>

<summary>See 44 more actions</summary>

* **Create or Update Accounts** `mergeAccounts`: Creates or updates one or more account (organization) records in Ortto's CDP. Account fields use org field IDs (e.g. str:o:name, int:o:employees, geo:o:country). Also used to tag/untag accounts via tags and unset_tags.
* **Create or Update People** `mergePerson`: Creates or updates one or more person (contact) records in Ortto's CDP using a merge strategy. Person fields use Ortto field IDs (e.g. str::first, str::last, str::email, phn::phone, geo::city, bol::p).
* **Create Person Custom Field** `createPersonCustomField`: Creates a custom field on the person (contact) object in Ortto's CDP. single_select and multi_select types require the values array.
* **Delete Accounts** `deleteAccounts`: Permanently deletes one or more accounts (organizations). Accounts must be archived first.
* **Delete Business Field** `deleteBusinessField`: Permanently deletes a custom business field in Ortto's CDP by its field ID.
* **Delete Custom Activity Definition** `deleteActivityDefinition`: Archives (deletes) a custom activity definition in Ortto's CDP by its activity_field_id.
* **Delete Custom Field** `deleteCustomField`: Deletes a custom field (person or account) from the Ortto instance by its field ID. This is permanent.
* **Delete People** `deletePeople`: Permanently deletes one or more people. Contacts must be archived first. Identify contacts with inclusion_ids, all_rows_selected/exclusion_ids, or a filter.
* **Get Accounts By IDs** `getAccountsByIds`: Retrieve specific accounts (organizations) by their account IDs (POST /v1/accounts/get-by-ids). Docs: https://help.ortto.com/a-277-retrieve-one-or-more-organizations-get
* **Get Asset HTML** `getAssetHtml`: Retrieves the HTML and metadata (subject, from, reply-to) of an email asset created in the Ortto asset manager.
* **Get Business Field** `getBusinessField`: Retrieves a single business field in Ortto's CDP by its field ID.
* **Get Campaign Report** `getCampaignReport`: Retrieves a performance report for a sent campaign or asset in Ortto, optionally for a specific timeframe. Only works for campaigns that have been sent.
* **Get Contact Activity Feed** `getContactActivities`: Retrieves the activity feed for a given contact, optionally filtered by activity field IDs, with pagination.
* **Get Instance Schema** `getInstanceSchema`: Retrieves the account/instance schema from Ortto's CDP, including system and custom field and activity definitions per namespace.
* **Get Knowledge Base Article** `getKnowledgeBaseArticle`: Retrieves a single knowledge base article in Ortto by its ID, including its full HTML content.
* **Get People By IDs** `getPeopleByIds`: Retrieve specific people (contacts) by their contact IDs (POST /v1/person/get-by-ids). Docs: https://help.ortto.com/a-258-retrieve-one-or-more-people-get
* **Get People Subscription Statuses** `getPersonSubscriptions`: Retrieves the audience subscription statuses and email/SMS permissions for one or more people identified by person_id, email or external_id.
* **Get Report** `getReport`: Retrieves a single report in Ortto by its report ID, including its snapshot data and metadata.
* **Get SMS Asset** `getSmsAsset`: Retrieves the details of an SMS asset (body, encoding, character count, segments, mapped links) created in the Ortto asset manager.
* **List Account Custom Fields** `getAccountCustomFields`: Retrieves the list of custom fields defined on the account (organization) object in Ortto's CDP.
* **List Accounts** `getAccounts`: Retrieves one or more account (organization) records from Ortto's CDP with optional filtering, sorting, field selection and pagination.
* **List Audiences** `getAudiences`: Retrieves a list of audiences (segments) in Ortto, optionally filtered by a search term, with pagination.
* **List Business Fields** `getAllBusinessFields`: Retrieves all system and custom business fields (company-level profile fields) in Ortto's CDP.
* **List Campaigns** `listCampaigns`: Retrieves and filters campaigns (email, SMS, push, journey, playbook) in Ortto by type, state, folder and search term, with sorting and pagination. Used to export campaign data.
* **List Email Suppressions** `getEmailSuppressionList`: Retrieves the email suppression list, with pagination and sorting. Each entry includes the suppressed email, when it was added, and the reason.
* **List Knowledge Base Articles** `getKnowledgeBaseArticles`: Retrieves knowledge base articles in Ortto, optionally filtered by status and search term, with pagination.
* **List People** `getPeople`: Retrieves one or more people (contacts) from Ortto's CDP with optional filtering, sorting, field selection and pagination.
* **List Person Custom Fields** `getPersonCustomFields`: Retrieves the list of custom fields defined on the person (contact) object in Ortto's CDP.
* **List Reports** `listReports`: Retrieves a list of reports configured in Ortto, optionally filtered by a search term.
* **List Sent Campaigns (Calendar)** `getSentCampaignsCalendar`: Retrieves a list of sent email, SMS and push notification campaigns within a calendar period defined by start and end year/month.
* **List Tags** `getTags`: Retrieves a list of tags in Ortto. Provide q to search (tokenised with AND logic); pass an empty object to return all tags.
* **Modify Custom Activity Definition** `modifyActivityDefinition`: Modifies an existing custom activity definition in Ortto's CDP, identified by activity_field_id, including state, attributes and display style.
* **Remove Contacts from Account** `removeAccountContacts`: Removes the association between one or more people and an account (organization). Identify people with inclusion_ids or a filter and target the account via account_id. Returns an empty object on success.
* **Remove Emails from Suppression List** `removeEmailSuppression`: Removes one or more email addresses from the email suppression list.
* **Restore Accounts** `restoreAccounts`: Restores one or more previously archived accounts (organizations).
* **Restore People** `restorePeople`: Restores one or more previously archived people. Identify contacts with inclusion_ids, all_rows_selected/exclusion_ids, or a filter.
* **Send Transactional Email** `sendTransactionalEmail`: Sends a transactional email to one or more recipients via the Ortto API, defining the email asset (from, subject, HTML body) inline and merging the recipients into the CDP.
* **Send Transactional Push Notification** `sendTransactionalPush`: Sends one or more transactional push notifications via the Ortto API to targeted contacts across web, iOS and/or Android platforms.
* **Send Transactional SMS** `sendTransactionalSms`: Send a transactional (or marketing) SMS to up to 100 people (POST /v1/transactional/send-sms). Needs an active SMS number and Ortto approval for transactional sends; recipients must be SMS-subscribed. Returns 202 when accepted. Docs: https://help.ortto.com/a-243-using-the-api-to-send-sms-messages
* **Subscribe or Unsubscribe People to Audience** `subscribeAudience`: Subscribes or unsubscribes people to/from an audience by setting subscribed and/or sms_opted_in per person. People must already be members of the audience. Set subscribed:false to unsubscribe.
* **Update Account Custom Field** `updateAccountCustomField`: Updates a single_select or multi_select custom field on the account (organization) object by replacing, appending or removing option values.
* **Update Business Field** `updateBusinessField`: Updates the value of a business field in Ortto's CDP by its field ID.
* **Update Contact Email Address** `updateContactEmail`: Updates a contact's email address by merging on the person ID with overwrite strategy. Provide the person's str::person_id and the new str::email in each people item.
* **Update Person Custom Field** `updatePersonCustomField`: Updates a single_select or multi_select custom field on the person object by replacing, appending or removing option values.

</details>
