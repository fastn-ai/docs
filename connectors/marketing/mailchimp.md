---
description: "Mailchimp is an email marketing platform. Manage audiences, members, tags, merge fields, segments, campaigns and webhooks."
hidden: true
---

# Mailchimp

<img src="../../.gitbook/assets/connectors/lg/mailchimp.png" alt="Mailchimp logo">

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [mailchimp.com](https://mailchimp.com) |
| **Authentication** | Username and password |
| **Slug** | `mailchimp` |

## Setup

Your customers enter their username and password for Mailchimp when they connect. Nothing else needs setting up.

## Use it

Add Mailchimp from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailchimp.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Member</td><td><code>addMember</code></td><td>Add a member to an audience</td></tr><tr><td>Add Member Tags</td><td><code>addMemberTags</code></td><td>Add or remove tags on a member</td></tr><tr><td>Archive Member</td><td><code>archiveMember</code></td><td>Archive a member</td></tr><tr><td>Create Audience</td><td><code>createAudience</code></td><td>Create an audience/list</td></tr><tr><td>Create Audience Webhook</td><td><code>createListWebhook</code></td><td>Create a webhook for an audience Used by the webhook config.</td></tr><tr><td>Create Campaign</td><td><code>createCampaign</code></td><td>Create a campaign</td></tr><tr><td>Create Merge Field</td><td><code>createMergeField</code></td><td>Create a merge field</td></tr><tr><td>Create Segment</td><td><code>createSegment</code></td><td>Create a segment or static tag</td></tr><tr><td>Delete Audience</td><td><code>deleteAudience</code></td><td>Delete an audience</td></tr><tr><td>Delete Audience Webhook</td><td><code>deleteListWebhook</code></td><td>Delete an audience webhook</td></tr></tbody></table>

<details>

<summary>View 24 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Campaign</td><td><code>deleteCampaign</code></td><td>Delete a campaign</td></tr><tr><td>Delete Member Permanently</td><td><code>deleteMemberPermanently</code></td><td>Permanently delete all personally identifiable information for an audience member and remove them from the audience. The member cannot be re-imported afterwards</td></tr><tr><td>Delete Merge Field</td><td><code>deleteMergeField</code></td><td>Delete a merge field from an audience</td></tr><tr><td>Delete Segment</td><td><code>deleteSegment</code></td><td>Delete a segment or static tag from an audience</td></tr><tr><td>Get Audience</td><td><code>getAudience</code></td><td>Get an audience by id</td></tr><tr><td>Get Campaign</td><td><code>getCampaign</code></td><td>Get a campaign</td></tr><tr><td>Get Member</td><td><code>getMember</code></td><td>Get a member by subscriber hash or email</td></tr><tr><td>Get Report</td><td><code>getReport</code></td><td>Get a campaign report</td></tr><tr><td>List Audience Webhooks</td><td><code>listListWebhooks</code></td><td>List webhooks for an audience</td></tr><tr><td>List Audiences</td><td><code>listAudiences</code></td><td>List audiences (lists)</td></tr><tr><td>List Campaigns</td><td><code>listCampaigns</code></td><td>List campaigns</td></tr><tr><td>List Members</td><td><code>listMembers</code></td><td>List members of an audience</td></tr><tr><td>List Merge Fields</td><td><code>listMergeFields</code></td><td>List merge fields for an audience</td></tr><tr><td>List Reports</td><td><code>listReports</code></td><td>List campaign reports</td></tr><tr><td>List Segments</td><td><code>listSegments</code></td><td>List segments/tags for an audience</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>List templates</td></tr><tr><td>Ping</td><td><code>ping</code></td><td>Health check / verify credentials</td></tr><tr><td>Schedule Campaign</td><td><code>scheduleCampaign</code></td><td>Schedule a campaign</td></tr><tr><td>Send Campaign</td><td><code>sendCampaign</code></td><td>Send a campaign immediately</td></tr><tr><td>Send Test Email</td><td><code>sendTestEmail</code></td><td>Send a test email for a campaign</td></tr><tr><td>Set Campaign Content</td><td><code>setCampaignContent</code></td><td>Set a campaign's HTML or template content</td></tr><tr><td>Update Audience</td><td><code>updateAudience</code></td><td>Update an audience</td></tr><tr><td>Update Member</td><td><code>updateMember</code></td><td>Update an existing member</td></tr><tr><td>Upsert Member</td><td><code>upsertMember</code></td><td>Add or update a member</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Campaign Sent</td><td><code>campaign</code></td><td>A campaign finished sending.</td></tr><tr><td>Email Changed</td><td><code>upemail</code></td><td>A member changed their email address.</td></tr><tr><td>Email Cleaned</td><td><code>cleaned</code></td><td>An email was cleaned (bounced/abuse).</td></tr><tr><td>Profile Update</td><td><code>profile</code></td><td>A member's profile/merge fields changed.</td></tr><tr><td>Subscribe</td><td><code>subscribe</code></td><td>A member subscribed to the audience.</td></tr><tr><td>Unsubscribe</td><td><code>unsubscribe</code></td><td>A member unsubscribed or was removed.</td></tr></tbody></table>
