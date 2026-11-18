---
description: "Re:amaze is a helpdesk and customer messaging platform for support teams, combining a shared inbox, live chat, FAQ knowledge base, and status page."
hidden: true
---

# Re:amaze

<img src="../../.gitbook/assets/connectors/lg/reamaze.png" alt="Re:amaze logo">

Re:amaze is a helpdesk and customer messaging platform for support teams, combining a shared inbox, live chat, FAQ knowledge base, and status page. This connector covers the Re:amaze JSON API v1: conversations, messages, contacts, contact identities and notes, help articles, channels, staff, response templates, satisfaction ratings, reports, and status page incidents and systems.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [reamaze.com](https://reamaze.com) |
| **Authentication** | Basic auth |
| **Slug** | `reamaze` |

## Use it

Add Re:amaze from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.reamaze.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Article | `createArticle` | Creates a help article in the Re:amaze FAQ without assigning it to a topic. |
| Create Article In Topic | `createArticleInTopic` | Creates a help article inside a specific FAQ topic, identified by the topic slug. |
| Create Contact | `createContact` | Creates a contact on the Re:amaze account. Either an email address or a mobile number in E.164 format must be supplied. |
| Create Contact Identity | `createContactIdentity` | Attaches an email address, mobile number, Twitter handle or Instagram identity to an existing contact. An identity already linked to another contact is moved, along with its messages and data. |
| Create Contact Note | `createContactNote` | Attaches a note to a contact, identified by the contact's email address or phone number. Returns the note that was created. |
| Create Conversation | `createConversation` | Creates a conversation in a Re:amaze channel on behalf of a customer, together with its first message. This is the endpoint behind custom contact forms and inbound integrations. |
| Create Incident | `createIncident` | Creates a status page incident for the brand with its first update, and optionally reports the status of the systems it affects. |
| Create Message | `createMessage` | Adds a message or internal note to an existing conversation. Set Visibility to 1 to write an internal note, and use the suppression flags to avoid notifying customers. |
| Create Response Template | `createResponseTemplate` | Creates a response template (saved reply) for the brand, or a personal template when the authenticated user has access to personal templates. |
| Create Staff User | `createStaff` | Creates a staff user on the Re:amaze account with a temporary password, which the user is asked to change at first login. No invitation email is sent. Adding a staff user can change the account's subscription cost. |
| Delete Contact Note | `deleteContactNote` | Deletes a note from a contact, identified by the contact's email address or phone number and the note ID. Returns the note that was deleted. |
| Get Article | `getArticle` | Retrieves a single help article by its slug, including its body, visibility, author and topic. |
| Get Channel | `getChannel` | Retrieves a single channel by its slug, including its type, visibility and reply settings. |
| Get Channel Summary Report | `getChannelSummaryReport` | Retrieves per-channel support metrics for the reporting window, including staff and customer responses, average response time, satisfaction rating and conversation counts. |
| Get Conversation | `getConversation` | Retrieves a single conversation by its slug, or by reference ID or origin ID when an ID type is supplied. |
| Get Incident | `getIncident` | Retrieves a single status page incident by its identifier, with its updates and affected systems. |
| Get Response Template | `getResponseTemplate` | Retrieves a single response template by its numeric ID, including its body and group. |
| Get Response Time Report | `getResponseTimeReport` | Retrieves daily response times in seconds for the reporting window, together with averages, trends and the ratio of conversations answered within an hour, a day and a week. |
| Get Staff Report | `getStaffReport` | Retrieves per-staff support metrics for the reporting window, including response counts, average response time, appreciations and a daily response trend. |
| Get Tags Report | `getTagsReport` | Retrieves tag usage counts for the reporting window, as a count of conversations per tag. |
| Get Volume Report | `getVolumeReport` | Retrieves the daily conversation volume for the reporting window, as a count of conversations per day. |
| List Active Incidents | `listActiveIncidents` | Retrieves only the currently active status page incidents for the brand. The response body is a JSON array of incidents. |
| List Articles | `listArticles` | Retrieves the help articles published in the Re:amaze FAQ for the brand, with optional keyword search and visibility filtering. |
| List Articles In Topic | `listArticlesInTopic` | Retrieves the help articles that belong to a single FAQ topic, identified by the topic slug. |
| List Channels | `listChannels` | Retrieves all channels configured for the Re:amaze brand, including email, chat, social and messaging channels, with their slug, type and settings. |
| List Contact Identities | `listContactIdentities` | Retrieves every identity (email, mobile, Twitter, Facebook or Instagram) linked to a contact. |
| List Contact Notes | `listContactNotes` | Retrieves every note attached to a contact, identified by the contact's email address or phone number. The response body is a JSON array of notes. |
| List Contacts | `listContacts` | Retrieves the contacts on the Re:amaze account, with optional keyword search, identity-type filtering and sorting. Contacts belong to the account rather than to an individual brand. |
| List Conversation Messages | `listConversationMessages` | Retrieves the messages belonging to a single conversation, newest first. |
| List Conversations | `listConversations` | Retrieves conversations for the Re:amaze brand, with filtering by state, channel, tag, origin, participant and date range. Only unarchived conversations are returned unless a filter is supplied. |
| List Incidents | `listIncidents` | Retrieves every status page incident for the brand, with its updates and the systems it affects. The response body is a JSON array of incidents. |
| List Messages | `listMessages` | Retrieves individual messages across every conversation in the brand, newest first, with filtering by author, channel, origin, tag and date range. |
| List Response Templates | `listResponseTemplates` | Retrieves the response templates available to the authenticated staff user for the brand, including personal templates where the user's role allows them. |
| List Satisfaction Ratings | `listSatisfactionRatings` | Retrieves customer satisfaction survey ratings, newest first, with filtering by score, assignee, brand and creation or update date. The authenticated user's role must carry the access_reports permission. |
| List Staff | `listStaff` | Retrieves the staff users on the Re:amaze account, sorted by creation time, with the permission hash for each user's role. |
| List Systems | `listSystems` | Retrieves the status page systems configured for the brand, with each system's current status and any active incidents affecting it. The response body is a JSON array of systems. Systems are created in the Re:amaze admin interface and cannot be created through the API. |
| Update Article | `updateArticle` | Updates the title, body, visibility or topic of an existing help article, identified by its slug. Returns HTTP 204 with an empty response body on success. |
| Update Contact | `updateContact` | Updates the name, friendly name, avatar or custom data of an existing contact, and can add new notes. Email addresses, mobile numbers and other identifiers cannot be changed here. |
| Update Contact Note | `updateContactNote` | Updates the text, creator or creation time of an existing note on a contact. Returns the updated note. |
| Update Conversation | `updateConversation` | Updates an existing conversation: its status, tags, assignee, custom data, or the channel and brand it belongs to. |
| Update Incident | `updateIncident` | Updates a status page incident, which is also how a new update is appended to the incident's timeline and how affected systems are moved back to operational. |
| Update Response Template | `updateResponseTemplate` | Updates the name, body or personal flag of an existing response template, identified by its numeric ID. |
