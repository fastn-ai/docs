---
description: "Zixflow is a CRM and multichannel campaign platform."
hidden: true
---

# Zixflow

<img src="../../.gitbook/assets/connectors/zixflow.png" alt="Zixflow logo" width="64">

Zixflow is a CRM and multichannel campaign platform. This connector covers the Zixflow App REST API (api.zixflow.com/api/v1): collections, lists, custom attributes with their select and status options (create, update, delete), collection records (people, companies, deals and custom collections) with filtering and sorting, list entries, activities and tasks, and workspace members; plus campaign messaging over WhatsApp (accounts, templates, template variables, template and session messages), RCS (template variables, template, text and media messages), SMS, email with attachments, the OTPflow multichannel fallback API, and WhatsApp, SMS and email delivery reports. Incoming WhatsApp and RCS message events are delivered to a webhook URL registered in Zixflow under Settings &gt; Developer &gt; Webhook. Authentication uses a Zixflow API key sent as a Bearer token. The separate Zixflow AI product (api-ai.zixflow.com, x-api-key and workspace ID authentication) is not part of this connector.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [zixflow.com](https://zixflow.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `zixflow` |

## Use it

Add Zixflow from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zixflow.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Activity | `createActivity` | Creates an activity or task in Zixflow, such as a call, meeting or follow-up, optionally associated with a collection record. Returns the created activity. |
| Create Attribute | `createAttribute` | Creates a custom attribute (field) on a Zixflow collection or list. Zixflow stores the API key name with an 'api' prefix in camel case (for example 'tier' becomes 'apiTier'); use the returned apiKeyName in record data. Returns the created attribute. |
| Create Attribute Option | `createAttributeOption` | Adds an option to a select or multiselect attribute on a Zixflow collection or list. Returns the created option and its ID. This endpoint is served by the Zixflow API but is not described in the public reference, which documents only listing, updating and deleting options. |
| Create Attribute Status | `createAttributeStatus` | Adds a status option (for example a pipeline stage) to a status attribute on a Zixflow collection or list. Returns the created status option and its ID. This endpoint is served by the Zixflow API but is not described in the public reference, which documents only listing, updating and deleting status options. |
| Create Collection Record | `createCollectionRecord` | Creates a record (a person, company, deal or custom collection record) in a Zixflow collection. Pass attribute values as top-level fields keyed by attribute API key name; common system attributes of People, Company and Deals are listed below, and custom attributes (keys starting with 'api') can be added as extra fields. Use List Attributes to discover keys and input types. Select and status attributes take option IDs, record references take record IDs. Note: when a person is created with an email address, Zixflow may automatically create or link a Company record for the email domain. Returns the created record and its ID. |
| Create List Entry | `createListEntry` | Adds a collection record to a Zixflow list as a new entry, optionally setting the list's own attribute values. Returns the created entry. |
| Delete Activity | `deleteActivity` | Deletes a Zixflow activity or task. |
| Delete Attribute | `deleteAttribute` | Deletes a custom attribute from a Zixflow collection or list. |
| Delete Attribute Option | `deleteAttributeOption` | Deletes an option from a select or multiselect attribute on a Zixflow collection or list. |
| Delete Attribute Status | `deleteAttributeStatus` | Deletes a status option from a status attribute on a Zixflow collection or list. |

<details>

<summary>See 49 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Collection Record | `deleteCollectionRecord` | Deletes a record from a Zixflow collection. |
| Delete List Entry | `deleteListEntry` | Removes an entry from a Zixflow list. The underlying collection record is not deleted. |
| Get Activity | `getActivity` | Retrieves a single Zixflow activity or task by ID. |
| Get Attribute | `getAttribute` | Retrieves a single attribute of a Zixflow collection or list by ID. |
| Get Collection | `getCollection` | Retrieves a single Zixflow collection by ID, including its name, slug and collection type. |
| Get Collection Record | `getCollectionRecord` | Retrieves a single record from a Zixflow collection by ID. The keys of the returned record depend on the collection's attributes. |
| Get Email Message Report | `getEmailMessageReport` | Retrieves the delivery report of an email sent through Zixflow by its message ID, with status SENT, OPENED, CLICKED, BOUNCE, COMPLAINT or UNSUBSCRIBED. |
| Get List | `getList` | Retrieves a single Zixflow list by ID, including its parent collection details. |
| Get List Entry | `getListEntry` | Retrieves a single entry of a Zixflow list by ID. The keys of the returned entry depend on the list's attributes. |
| Get RCS Template Variables | `getRcsTemplateVariables` | Retrieves the variables of an RCS template for an RCS bot, with each variable's key and type. RCS is available for Indian recipients and must be activated for the workspace by Zixflow support. |
| Get SMS Message Report | `getSmsMessageReport` | Retrieves the delivery report of an SMS sent through Zixflow by its message ID, with status SENT, DELIVERED or UNDELIVERED and the failure remark when applicable. |
| Get WhatsApp Message Report | `getWhatsappMessageReport` | Retrieves the delivery report of a WhatsApp message sent through Zixflow by its message ID, with status SENT, DELIVERED, READ or FAILED and the failure remark when applicable. |
| Get WhatsApp Template Variables | `getWhatsappTemplateVariables` | Retrieves the variables a WhatsApp template requires, with each variable's label, key name and value type (TEXT, IMAGE_URL, VIDEO_URL, DOCUMENT_URL or OTP). Use the key names in the Variables field of Send WhatsApp Template Message. |
| Get Workspace Member | `getWorkspaceMember` | Retrieves a single Zixflow workspace member by user ID. |
| List Attribute Options | `listAttributeOptions` | Lists the options of a select or multiselect attribute on a Zixflow collection or list. |
| List Attribute Statuses | `listAttributeStatuses` | Lists the status options (pipeline stages) of a status attribute on a Zixflow collection or list, such as the stages of the Deals pipeline. |
| List Attributes | `listAttributes` | Lists the attributes (fields) defined on a Zixflow collection or list, including each attribute's API key name, input type, configuration and flags. Use the API key names as keys when creating or updating records and list entries. |
| List Collections | `listCollections` | Lists all system collections (People, Company, Deals) and custom collections in the Zixflow workspace. |
| List Lists | `listLists` | Lists all lists in the Zixflow workspace, including each list's emoji, parent collection and whether duplicate records are allowed. |
| List WhatsApp Accounts | `listWhatsappAccounts` | Lists the WhatsApp Business phone numbers connected to the Zixflow workspace, including each number's phone ID, WABA ID, verified name, quality rating and daily messaging limit. Use the phone ID with the WhatsApp template and messaging actions. |
| List WhatsApp Templates | `listWhatsappTemplates` | Lists the WhatsApp message templates available for a connected WhatsApp phone number, including each template's name, language, category, approval status and components. |
| List Workspace Members | `listWorkspaceMembers` | Lists all members of the Zixflow workspace with their name, email, phone, role, status and timezone. |
| Query Activities | `queryActivities` | Lists activities and tasks in the Zixflow workspace with offset pagination, optional filtering and sorting. Each activity includes its schedule, associated record, assignee, status, source and creator. Filters are objects keyed by activity field, for example {"name": {"$contains": "call"}}; note that the Zixflow reference describes filter as an array, but the API only applies an object and silently ignores an array. |
| Query Collection Records | `queryCollectionRecords` | Lists records of a Zixflow collection with optional filtering, sorting and offset pagination. Filters use attribute API key names in shorthand ({"name": "John Doe"}) or verbose form with operators $eq, $not_empty, $in, $contains, $not_contains, $starts_with, $ends_with, $lt, $lte, $gt, $gte, combined with $and, $or and $not. |
| Query List Entries | `queryListEntries` | Lists the entries of a Zixflow list with optional filtering, sorting and offset pagination. Entry keys depend on the list's attributes; filters and sorts use attribute API key names with the same operators as Query Collection Records. |
| Send Email | `sendEmail` | Sends a transactional email through Zixflow to up to 10 recipients from a verified sender address, with HTML and/or plain-text body, optional tracking, reply-to and attachments uploaded with Upload Email Attachment. The sending domain must be verified in Zixflow campaign email settings. |
| Send OTPflow Messages | `sendOtpflowMessages` | Sends a message through Zixflow OTPflow, which tries up to 5 channel messages (SMS, WhatsApp, RCS or email) in order and falls back to the next one when a message fails or is not delivered within its timeout (total 300 seconds). Each message's data uses the same payload as the matching send action. Optionally notifies a webhook when a channel switch happens. |
| Send RCS Audio Message | `sendRcsAudioMessage` | Sends an audio file by public URL with suggestion buttons from an RCS bot to a recipient with a live session. |
| Send RCS Document Message | `sendRcsDocumentMessage` | Sends a document by public URL with suggestion buttons from an RCS bot to a recipient with a live session. |
| Send RCS Image Message | `sendRcsImageMessage` | Sends an image by public URL with suggestion buttons from an RCS bot to a recipient with a live session. |
| Send RCS Template Message | `sendRcsTemplateMessage` | Sends an approved RCS template message from an RCS bot to a recipient. RCS is available for Indian recipients and must be activated for the workspace by Zixflow support. |
| Send RCS Text Message | `sendRcsTextMessage` | Sends an RCS text message with suggestion buttons (reply, open URL, dial, location or calendar event) from an RCS bot to a recipient with a live session. |
| Send RCS Video Message | `sendRcsVideoMessage` | Sends a video by public URL with suggestion buttons from an RCS bot to a recipient with a live session. |
| Send SMS | `sendSms` | Sends an SMS from a registered sender ID to a phone number through Zixflow. Indian traffic can pass DLT template and entity IDs; delivery reports can be pushed to a report URL. |
| Send SMS Via Query String | `sendSmsViaQueryString` | Sends an SMS using Zixflow's single-line HTTP GET API, where the API key and message parameters are passed in the query string. Functionally equivalent to Send SMS; the connection's API key is added automatically. |
| Send WhatsApp Audio Message | `sendWhatsappAudioMessage` | Sends an audio file by public URL to a WhatsApp recipient who has an active conversation session with the business number. |
| Send WhatsApp Document Message | `sendWhatsappDocumentMessage` | Sends a document by public URL, with an optional caption and file name, to a WhatsApp recipient who has an active conversation session with the business number. |
| Send WhatsApp Image Message | `sendWhatsappImageMessage` | Sends an image by public URL, with an optional caption, to a WhatsApp recipient who has an active conversation session with the business number. |
| Send WhatsApp Location Message | `sendWhatsappLocationMessage` | Sends a location pin, with optional name and address, to a WhatsApp recipient who has an active conversation session with the business number. |
| Send WhatsApp Template Message | `sendWhatsappTemplateMessage` | Sends an approved WhatsApp template message to a recipient from a connected WhatsApp number. Use Get WhatsApp Template Variables to find the variable keys the template requires. Template messages can start a new conversation with a user. |
| Send WhatsApp Text Message | `sendWhatsappTextMessage` | Sends a free-form WhatsApp text message to a recipient who has an active 24-hour conversation session with the business number. Outside a session the message fails; start with a template message instead. |
| Send WhatsApp Video Message | `sendWhatsappVideoMessage` | Sends a video by public URL, with an optional caption, to a WhatsApp recipient who has an active conversation session with the business number. |
| Update Activity | `updateActivity` | Updates a Zixflow activity or task. Only the properties you pass are changed. |
| Update Attribute | `updateAttribute` | Updates a custom attribute on a Zixflow collection or list. Only the properties you pass are changed. The response confirms the update without returning the attribute; use Get Attribute to read it back. |
| Update Attribute Option | `updateAttributeOption` | Updates an option of a select or multiselect attribute on a Zixflow collection or list: its name, color, archived flag or order. Note that Zixflow reports success even when the option ID does not exist. |
| Update Attribute Status | `updateAttributeStatus` | Updates a status option of a status attribute on a Zixflow collection or list: its name, color, archived flag or celebration setting. |
| Update Collection Record | `updateCollectionRecord` | Updates a record in a Zixflow collection. Pass only the attributes to change as top-level fields keyed by attribute API key name; common system attributes are listed below and custom attributes (keys starting with 'api') can be added as extra fields. |
| Update List Entry | `updateListEntry` | Updates the list attribute values of an entry in a Zixflow list. Pass each list attribute to change as a top-level field keyed by its API key name (for example apiStatus with a status option ID); use List Attributes with target 'list' to discover the keys. Note: although the Zixflow reference shows a 'data' wrapper, the API only applies top-level keys and silently ignores a 'data' object. |
| Upload Email Attachment | `uploadEmailAttachment` | Uploads a file (up to 25 MB) to Zixflow as multipart form data so it can be attached to emails. Returns the file ID to pass in the Attachment IDs field of Send Email. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Incoming RCS Message | `incoming.rcs.message` | Triggered when an RCS message (text, suggestion reply, image, video, audio, file or location) is received by an RCS bot connected to Zixflow (RCS is available for Indian numbers once activated by Zixflow support). Setup (once per Zixflow workspace): in Zixflow open Settings &gt; Developer &gt; Webhook, click Add, paste the fastn webhook URL and select the incoming.rcs.message event. Zixflow has no webhook registration API and does not sign deliveries. The event type is read from the 'event' field. Payload schema is modelled from Zixflow's documented example; the 'message' object carries only the key matching message.type. |
| Incoming WhatsApp Message | `incoming.whatsapp.message` | Triggered when a WhatsApp message (text, media, location, contacts, button reply, flow form reply or order) is received on a WhatsApp number connected to Zixflow. Setup (once per Zixflow workspace): in Zixflow open Settings &gt; Developer &gt; Webhook, click Add, paste the fastn webhook URL and select the incoming.whatsapp.message event. Zixflow has no webhook registration API and does not sign deliveries. The event type is read from the 'event' field. Payload schema is modelled from Zixflow's documented example; the 'message' object carries only the key matching message.type. |
