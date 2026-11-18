---
description: "Zoho Campaigns is Zoho's email marketing automation platform."
hidden: true
---

# Zoho Campaigns

Zoho Campaigns is Zoho's email marketing automation platform. This connector wraps the Zoho Campaigns REST API v1.1 (campaigns.zoho.com/api/v1.1): mailing lists, list contacts (subscribe/unsubscribe), contact fields, topics, and campaigns (create, clone, send, schedule, delete) together with campaign details and campaign reports. OAuth 2.0 authorization code auth via the shared Zoho API Console app.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [campaigns.zoho.com](https://campaigns.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 16 |
| **Events** | 0 |
| **Slug** | `zohoCampaigns` |

## Use it

Add Zoho Campaigns from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoCampaigns.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Clone Campaign | `cloneCampaign` | Duplicate an existing Zoho Campaigns campaign under a new name and subject, reusing its content instead of building a campaign from scratch. |
| Create Campaign | `createCampaign` | Create an email campaign in Zoho Campaigns from content hosted at a public URL, targeting one or more mailing lists and a topic. |
| Delete Campaign | `deleteCampaign` | Permanently delete a campaign from your Zoho Campaigns organization, identified by its campaign key. |
| Delete Mailing List | `deleteMailingList` | Delete a Zoho Campaigns mailing list, optionally also removing its contacts from the whole organization. |
| Get Campaign Details | `getCampaignDetails` | Retrieve the full details of a single Zoho Campaigns campaign, identified by its campaign key. |
| Get Campaign Reports | `getCampaignReports` | Retrieve the performance report for a sent Zoho Campaigns campaign, including sent, open, click, bounce and unsubscribe counts. |
| List Contact Fields | `listContactFields` | Retrieve every contact field defined in your Zoho Campaigns account, including display names and field names. Use these field names when building the contact information for subscribe and unsubscribe actions. |
| List Contacts In Mailing List | `listContactsInMailingList` | Retrieve the contacts belonging to a Zoho Campaigns mailing list, optionally filtered by subscription status and paginated. |
| List Mailing Lists | `listMailingLists` | Retrieve the mailing lists in your Zoho Campaigns organization, with optional sorting and pagination. Each list returns its list key, which other actions require. |
| List Recent Campaigns | `listRecentCampaigns` | Retrieve recently created campaigns in your Zoho Campaigns organization, optionally filtered by status. Each campaign returns its campaign key, which the campaign detail, send, schedule, report and delete actions require. |
| List Topics | `listTopics` | Retrieve the topics configured in your Zoho Campaigns account. Topics group the kinds of email a contact can opt in to and are required when creating a campaign. |
| Schedule Campaign | `scheduleCampaign` | Schedule an existing Zoho Campaigns campaign to be sent at a specific date and time, optionally using timewarp delivery in each recipient's own timezone. |
| Send Campaign | `sendCampaign` | Send an existing Zoho Campaigns campaign immediately to its configured mailing lists. |
| Subscribe Contact To Mailing List | `subscribeContactToMailingList` | Add a contact to a Zoho Campaigns mailing list and send the subscription email. Contact details are supplied as a JSON object of Zoho Campaigns contact field names. |
| Unsubscribe Contact From Mailing List | `unsubscribeContactFromMailingList` | Unsubscribe a contact from a Zoho Campaigns mailing list, or from a specific topic within it. |
| Update Mailing List | `updateMailingList` | Rename a Zoho Campaigns mailing list and set whether its signup form is public or private. |
