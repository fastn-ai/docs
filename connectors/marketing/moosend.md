---
description: "Moosend email marketing and automation platform."
hidden: true
---

# Moosend

<img src="../../.gitbook/assets/connectors/lg/moosend.png" alt="Moosend logo">

Moosend email marketing and automation platform. Manage mailing lists, subscribers, custom fields, segments, campaigns, and sender addresses through the Moosend v3 REST API.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [moosend.com](https://moosend.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `moosend` |

## Use it

Add Moosend from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.moosend.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Multiple Subscribers | `addSubscribersBatch` | Adds up to 1000 subscribers to a mailing list in a single request. Existing subscribers are updated; invalid emails are ignored. |
| Add Segment Criteria | `addSegmentCriteria` | Adds a filtering criterion to a specific segment. |
| Add Subscriber | `addSubscriber` | Adds a new subscriber to a specific mailing list. If the subscriber already exists it is updated. |
| Clone Campaign | `cloneCampaign` | Creates a copy of an existing campaign as a new draft. |
| Create Custom Field | `createCustomField` | Creates a custom data field for a specific mailing list and returns its ID. |
| Create Draft Campaign | `createDraftCampaign` | Creates a new draft campaign (regular or AB split) ready for sending or testing. Content is retrieved from a web location. |
| Create Mailing List | `createMailingList` | Creates a new mailing list in your Moosend account and returns its ID. |
| Create Segment | `createSegment` | Creates a new empty segment (without criteria) for a specific mailing list and returns its ID. |
| Delete Campaign | `deleteCampaign` | Deletes a campaign (draft or sent) from your account. |
| Delete Mailing List | `deleteMailingList` | Deletes a mailing list from your Moosend account. |
| Delete Multiple Subscribers From Mailing List | `deleteSubscribersBatch` | Delete several subscribers from a mailing list by email (POST /subscribers/{MailingListID}/delete_many.json). Docs: https://doc.sitecore.com/send/en/developers/api-documentation/api-reference/subscribers/delete-multiple-subscribers-from-a-specific-mailing-list.html |
| Delete Segment | `deleteSegment` | Deletes a segment and its criteria from a mailing list. Subscribers are not affected. |
| Delete Subscriber From Account | `deleteSubscriberFromAccount` | Delete a subscriber (by email) from every mailing list in the account (POST /subscribers/delete.json). Docs: https://doc.sitecore.com/send/en/developers/api-documentation/api-reference/subscribers/delete-a-subscriber-from-an-account.html |
| Delete Subscriber From Mailing List | `deleteSubscriber` | Delete a subscriber from a mailing list by email (POST /subscribers/{MailingListID}/delete.json). Docs: https://doc.sitecore.com/send/en/developers/api-documentation/api-reference/subscribers/delete-a-subscriber.html |
| Get AB Test Campaign Summary | `getAbTestCampaignSummary` | Retrieves the A/B test summary statistics for a specific A/B split campaign. |
| Get All Campaigns | `getCampaigns` | Retrieves all campaigns in your account with detailed information. |
| Get All Mailing Lists | `getMailingLists` | Retrieves all active mailing lists in your Moosend account, optionally including subscriber statistics. |
| Get All Senders | `getSenders` | Retrieves all sender email addresses configured in your Moosend account. |
| Get Campaign Activity By Location | `getCampaignActivityByLocation` | Retrieves campaign activity broken down by recipient country. |
| Get Campaign Details | `getCampaignDetails` | Retrieves detailed information about a specific campaign. |
| Get Campaign Link Activity | `getCampaignLinkActivity` | Retrieves click activity per link for a specific campaign. |
| Get Campaign Statistics | `getCampaignStatistics` | Retrieves detailed activity statistics for a campaign filtered by activity type, with paging and optional date range. |
| Get Campaign Summary | `getCampaignSummary` | Retrieves summary statistics for a specific campaign (opens, clicks, bounces, etc.). |
| Get Campaigns By Page | `getCampaignsByPage` | Retrieves campaigns in your account for a specific page. |
| Get Campaigns By Page And Page Size | `getCampaignsByPageAndPageSize` | Retrieves campaigns in your account using page and page size for pagination. |
| Get Mailing List Details | `getMailingListDetails` | Retrieves details for a specific mailing list, optionally including subscriber statistics. Segments are not included. |
| Get Mailing Lists With Paging | `getMailingListsWithPaging` | Retrieves active mailing lists in your Moosend account using page and page size for pagination. |
| Get Segment Details | `getSegmentDetails` | Retrieves details and criteria of a specific segment. Does not include the subscribers the segment returns. |
| Get Segment Subscribers | `getSegmentSubscribers` | Retrieves the subscribers returned by a specific segment according to its criteria, with paging. |
| Get Segments | `getSegments` | Retrieves all segments and their criteria for a specific mailing list. |
| Get Sender Details | `getSenderDetails` | Retrieves the details of a specific sender by email address. |
| Get Subscriber By Email | `getSubscriberByEmail` | Retrieves a subscriber from a specific mailing list by email address. |
| Get Subscriber By ID | `getSubscriberById` | Retrieves a subscriber from a specific mailing list by subscriber ID. |
| Get Subscriber By ID (Any List) | `getSubscriberByIdAllLists` | Get a subscriber's details by subscriber ID without giving a mailing list ID (GET /subscribers/{SubscriberID}.json). Docs: https://doc.sitecore.com/send/en/developers/api-documentation/api-reference/subscribers/get-subscriber-by-id-without-mailing-list-id.html |
| Get Subscribers By Status | `getSubscribers` | Retrieves subscribers of a mailing list filtered by status (Subscribed, Unsubscribed, Bounced or Removed), with paging. |
| Remove Custom Field | `removeCustomField` | Removes a custom data field from a specific mailing list. |
| Remove Multiple Subscribers | `removeSubscribersBatch` | Permanently removes multiple subscribers from a mailing list. Provide a comma-separated list of email addresses. |
| Remove Subscriber | `removeSubscriber` | Permanently removes a single subscriber from a mailing list by email address. |
| Schedule Campaign | `scheduleCampaign` | Schedules a draft campaign for delivery at a specific date and time. |
| Send Campaign | `sendCampaign` | Sends an existing draft campaign immediately to all recipients in its mailing list. |
| Send Transactional Campaign | `sendTransactionalCampaign` | Send a transactional email through a transactional campaign/template (POST /campaigns/transactional/send.json). Payload must be under 20MB. Docs: https://doc.sitecore.com/send/en/developers/api-documentation/api-reference/campaigns/manage-a-transactional-campaign.html |
| Test Campaign | `testCampaign` | Sends a test email of a draft campaign to up to 5 email addresses for previewing. |
| Unschedule Campaign | `unscheduleCampaign` | Cancels the scheduled delivery of a campaign. |
| Unsubscribe From Account | `unsubscribeFromAccount` | Unsubscribes a subscriber from all mailing lists in the account, adding them to the account suppression list. |
| Unsubscribe From Mailing List | `unsubscribeFromMailingList` | Unsubscribes a subscriber from a specific mailing list, moving them to the suppression list. |
| Unsubscribe From Mailing List And Campaign | `unsubscribeFromMailingListAndCampaign` | Unsubscribes a subscriber from a specific mailing list in the context of a specific campaign. |
| Update Custom Field | `updateCustomField` | Updates an existing custom data field on a specific mailing list. |
| Update Draft Campaign | `updateDraftCampaign` | Updates an existing draft campaign. Only draft campaigns can be updated. Send every field you want to keep: omitted fields (sender, content, lists) are cleared by Moosend. |
| Update Mailing List | `updateMailingList` | Updates the name and settings of an existing mailing list. |
| Update Segment | `updateSegment` | Updates the name and match type of an existing segment. |
| Update Segment Criteria | `updateSegmentCriteria` | Updates an existing filtering criterion on a specific segment. |
| Update Subscriber | `updateSubscriber` | Updates an existing subscriber in a specific mailing list. |
