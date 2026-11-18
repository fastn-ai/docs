---
description: "TextIt is a messaging and chatbot automation platform (RapidPro-based) for SMS, WhatsApp and social messaging campaigns."
hidden: true
---

# TextIt

<img src="../../.gitbook/assets/connectors/textit.png" alt="TextIt logo" width="64">

TextIt is a messaging and chatbot automation platform (RapidPro-based) for SMS, WhatsApp and social messaging campaigns. This connector wraps the TextIt API v2 at https://textit.com/api/v2 and covers contacts, groups, fields, globals, labels, messages, broadcasts, flows, flow starts, runs, campaigns, campaign events, channels, tickets, topics, users, archives, media, admin boundaries, flow definitions and resthook webhook subscriptions.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [textit.com](https://textit.com) |
| **Authentication** | API key |
| **Slug** | `textit` |

## Use it

Add TextIt from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.textit.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Campaign | `createCampaign` | Create a new campaign in the TextIt workspace that runs against a contact group. Returns the created campaign including its new UUID. Campaigns cannot be deleted through the API and must be removed from the TextIt web app. |
| Create Campaign Event | `createCampaignEvent` | Add a new event to a campaign. The event fires a message or starts a flow at an offset relative to a date contact field. Supply either a message or a flow, not both. Returns the created campaign event including its new UUID. |
| Create Contact | `createContact` | Create a new contact in the TextIt workspace with an optional name, preferred language, URNs (such as tel:+250788123123 or twitter:ben), group memberships and custom field values. Returns the created contact including its new UUID. |
| Create Contact Field | `createField` | Create a new custom contact field in the TextIt workspace. The field key is generated from the display name. Returns the created field with its generated key. Contact fields cannot be deleted through the API. |
| Create Contact Group | `createGroup` | Create a new manual contact group in the TextIt workspace. Returns the created group including its new UUID and a member count of zero. |
| Create Global | `createGlobal` | Create a new global in the TextIt workspace. A global is a named workspace-wide value that flows can reference. The key is generated from the name. Globals cannot be deleted through the API. |
| Create Message Label | `createLabel` | Create a new message label in the TextIt workspace. Returns the created label including its new UUID and a message count of zero. |
| Create Ticket Topic | `createTopic` | Create a new ticket topic in the TextIt workspace with a unique name. Returns the created topic including its new UUID. Topics cannot be deleted through the API. |
| Delete Campaign Event | `deleteCampaignEvent` | Delete the campaign event with the given UUID. Returns an empty 204 response on success, or 404 if no event matches. |
| Delete Contact By URN | `deleteContactByUrn` | Permanently delete the contact that owns the given URN, e.g. tel:+250783835665. Returns an empty 204 response on success, or 404 if no contact matches. This cannot be undone. |

<details>

<summary>See 45 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Contact By UUID | `deleteContactByUuid` | Permanently delete the contact with the given UUID from the TextIt workspace. Returns an empty 204 response on success, or 404 if no contact matches. This cannot be undone. |
| Delete Contact Group | `deleteGroup` | Delete the contact group with the given UUID. Returns an empty 204 response on success, or 404 if no group matches. Groups that still have active campaigns or triggers attached cannot be deleted through the API. |
| Delete Message Label | `deleteLabel` | Delete the message label with the given UUID. Returns an empty 204 response on success, or 404 if no label matches. Messages carrying the label are not deleted. |
| Delete Resthook Subscriber | `deleteResthookSubscriber` | Remove a resthook subscription by its numeric id, stopping further deliveries to that target URL. Returns an empty 204 response on success, or 404 if no subscriber matches. |
| Export Flow Definitions | `exportDefinitions` | Export the JSON definitions of flows and campaigns from the TextIt workspace, in the same format used by the workspace export and import screens. Pass one or more flow or campaign UUIDs, and choose whether dependencies (referenced flows, groups and fields) are included. |
| Get Organization Profile | `getOrganization` | Retrieve the workspace profile through the legacy /api/v2/org.json alias. Returns the same payload as Get Workspace and is kept for clients written against the older organization endpoint name. |
| Get Workspace | `getWorkspace` | Retrieve the details of the TextIt workspace (organization) the API token belongs to, including its UUID, name, country, configured languages, timezone, date style, anonymous-contact setting and credit balance. |
| List Admin Boundaries | `listBoundaries` | List the administrative boundaries (states, districts and wards) configured for the workspace country, used by state, district and ward contact fields. Set Include Geometry to also return each boundary's GeoJSON geometry. |
| List Archives | `listArchives` | List the daily or monthly data archives of messages and flow runs for the TextIt workspace. Each archive entry carries a temporary download URL for the gzipped archive content. |
| List Broadcasts | `listBroadcasts` | List the message broadcasts sent from the TextIt workspace, most recent first, including their recipients, translated text and delivery status. Optionally filter by broadcast UUID or creation date range. |
| List Campaign Events | `listCampaignEvents` | List the campaign events in the TextIt workspace, newest first, showing the date field each event is relative to, its offset and unit, and the message or flow it triggers. Optionally filter by event UUID or by campaign UUID. |
| List Campaigns | `listCampaigns` | List the campaigns in the TextIt workspace, newest first, with the contact group each campaign runs against and whether it is archived. Optionally filter by campaign UUID or creation date range. |
| List Channels | `listChannels` | List the messaging channels connected to the TextIt workspace (Android phones, Twilio, Vonage, Telegram, Facebook and others), newest first. Optionally filter by channel UUID or by channel address such as a phone number or handle. |
| List Contact Fields | `listFields` | List the custom contact fields defined in the TextIt workspace, newest first, with each field's key, display name and data type. Optionally filter to a single field by its key. |
| List Contact Groups | `listGroups` | List the contact groups in the TextIt workspace, newest first, with each group's member count, smart-group query and system flag. Optionally filter by group UUID or name, or restrict the result to manual (static) groups only. |
| List Contacts | `listContacts` | List the contacts in the TextIt workspace, ordered by last modified. Optionally filter by contact UUID, by URN (e.g. tel:+250788123123), by group name or UUID, or by modification date range. |
| List Flow Runs | `listRuns` | List flow runs in the TextIt workspace, most recently modified first. A run is a single contact's path through a flow and carries the values captured at each ruleset. Filter by run UUID, whether the contact responded, or modification date range. The flow and contact filters are mutually exclusive: supplying both returns 400. |
| List Flow Starts | `listFlowStarts` | List the manual flow starts in the TextIt workspace, most recently modified first, showing the flow started, the contacts and groups included, the start status and any extra parameters passed to the flow. |
| List Flows | `listFlows` | List the flows in the TextIt workspace, newest first, including their labels, expiry, run counts and the result keys each flow can produce. Optionally filter by flow UUID, flow type, archived state or modification date range. |
| List Globals | `listGlobals` | List the globals (workspace-wide named values usable inside flows) in the TextIt workspace, most recently modified first. Optionally filter to a single global by its key. |
| List Message Labels | `listLabels` | List the message labels in the TextIt workspace, newest first, with the number of messages carrying each label. Optionally filter by label UUID or name. |
| List Messages | `listMessages` | List the incoming and outgoing messages in the TextIt workspace, most recently created first. Filter by message UUID, creation date range, and exactly one of folder, label, contact or broadcast: supplying more than one of those four returns 400. |
| List Resthook Events | `listResthookEvents` | List the recent resthook events fired in the TextIt workspace, most recently created first, each carrying the full flow, contact, run, input and results payload that was delivered to subscribers. Optionally filter by resthook slug. |
| List Resthook Subscribers | `listResthookSubscribers` | List the resthook subscribers in the TextIt workspace, most recently created first, showing which resthook slug each target URL is subscribed to. Optionally filter by subscriber id or resthook slug. |
| List Resthooks | `listResthooks` | List the resthooks configured in the TextIt workspace, most recently modified first. A resthook is a named webhook event slug that flows can call, and external systems subscribe to it to receive its payloads. |
| List Ticket Topics | `listTopics` | List the ticket topics in the TextIt workspace, most recent first, with the open and closed ticket counts for each and whether it is a system topic that cannot be modified. This endpoint takes no filter parameters. |
| List Tickets | `listTickets` | List the support tickets opened in the TextIt workspace, most recent first, with each ticket's contact, status, topic, assignee and the flow that opened it. Optionally filter by ticket UUID or contact UUID. |
| List Users | `listUsers` | List the user logins that have access to the TextIt workspace, newest first, with each user's email, name, workspace role and team. Optionally filter to a single user by UUID. |
| Run Bulk Contact Action | `runContactAction` | Perform one action on up to 100 contacts at once: add them to or remove them from a group, block or unblock them, interrupt their active flow runs, or permanently delete them. Returns an empty 204 response on success. Use with care: the delete action cannot be undone. |
| Run Bulk Message Action | `runMessageAction` | Perform one action on up to 100 messages at once: apply or remove a label, archive or restore them, or permanently delete them. Returns 204 on full success, or 200 with a failures array listing message ids that no longer exist. |
| Run Bulk Ticket Action | `runTicketAction` | Perform one action on up to 100 tickets at once: assign them to a user, add a note, change their topic, close them or reopen them. Returns an empty 204 response on success. |
| Send Broadcast | `sendBroadcast` | Create and send a message broadcast to any combination of URNs, contacts and contact groups, with per-language text, attachments and quick replies. Returns the created broadcast. This sends real messages over the workspace's channels. |
| Send Message | `sendMessage` | Create and send a single outgoing message to one contact, optionally with media attachments and quick replies. Attachments are media object UUIDs returned by Upload Media File. Returns the created message. This sends a real message over the workspace's channels. |
| Start Flow | `startFlow` | Start a set of contacts, groups or URNs down a flow. Contacts are added to the flow asynchronously; use List Flow Runs to monitor the runs it creates. Returns the created flow start with a pending status. |
| Subscribe To Resthook | `createResthookSubscriber` | Subscribe a target URL to a resthook so that TextIt POSTs the resthook's payload to it whenever a flow fires that resthook. Returns the created subscription including its numeric id, which Delete Resthook Subscriber needs. |
| Update Campaign | `updateCampaign` | Update the name or target contact group of an existing campaign, identified by its UUID. Returns the updated campaign. |
| Update Campaign Event | `updateCampaignEvent` | Update an existing campaign event identified by its UUID. The live API requires the campaign UUID to be resent even though it cannot be changed. Returns the updated campaign event. |
| Update Contact By URN | `updateContactByUrn` | Update an existing contact identified by one of its URNs, e.g. tel:+250783835665. Do not send URNs in the body when using this action. If no contact has that URN a new contact is created and 201 is returned instead of 200. |
| Update Contact By UUID | `updateContactByUuid` | Update an existing contact identified by its UUID. Only the properties you supply are changed; omitted properties are left untouched. Returns the updated contact. |
| Update Contact Field | `updateField` | Update the display name or data type of an existing custom contact field, identified by its key. Returns the updated field. |
| Update Contact Group | `updateGroup` | Rename an existing contact group identified by its UUID. Returns the updated group. System groups cannot be modified. |
| Update Global | `updateGlobal` | Update the value of an existing global, identified by its key. Returns the updated global. |
| Update Message Label | `updateLabel` | Rename an existing message label identified by its UUID. Returns the updated label. |
| Update Ticket Topic | `updateTopic` | Rename an existing ticket topic identified by its UUID. Returns the updated topic. System topics cannot be modified. This update route is not covered by the published TextIt documentation but is live on the API. |
| Upload Media File | `uploadMedia` | Upload a media file to the TextIt workspace and receive a media object UUID that Send Message and Send Broadcast can attach. Pass the file content as text; text-safe formats such as PDF and SVG work directly. SECURITY: the response contains a publicly reachable S3 URL for the uploaded file. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Resthook Fired | `resthook` | Fires each time a TextIt flow reaches a Call Resthook action for the resthook slug you enter below. SETUP: TextIt has no API for creating a resthook, so the slug must first exist in the workspace. In the TextIt web app open Flows, edit the flow you want to emit the event, add or open a node, choose 'Call Resthook' as the action, type the resthook name (its slug) and save the flow. The slug then appears under Settings &gt; Resthooks and in List Resthooks. Enter that exact slug as the Resthook Slug input here; this trigger will then subscribe its fastn URL to it and TextIt will POST the run payload on every fire. PAYLOAD SCHEMA BELOW IS MODELLED FROM TEXTIT'S DOCUMENTED SAMPLE, NOT FROM A CAPTURED DELIVERY: no resthook existed in the test workspace and none could be created through the API. |
