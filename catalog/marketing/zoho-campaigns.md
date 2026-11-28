---
description: "Zoho Campaigns is an email marketing tool. Manage mailing lists and contacts, and create, clone and report on campaigns."
hidden: true
---

# Zoho Campaigns

<img src="../../.gitbook/assets/connectors/lg/zoho-campaigns.png" alt="Zoho Campaigns logo">

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [campaigns.zoho.com](https://campaigns.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoCampaigns` |

## Setup

Your customers sign in to Zoho Campaigns through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Zoho Campaigns from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Zoho Campaigns**.
2. Select **Connect** on the Zoho Campaigns card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Zoho Campaigns and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Zoho Campaigns's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Clone Campaign</td><td><code>cloneCampaign</code></td><td>Duplicate an existing Zoho Campaigns campaign under a new name and subject, reusing its content instead of building a campaign from scratch.</td></tr><tr><td>Create Campaign</td><td><code>createCampaign</code></td><td>Create an email campaign in Zoho Campaigns from content hosted at a public URL, targeting one or more mailing lists and a topic.</td></tr><tr><td>Delete Campaign</td><td><code>deleteCampaign</code></td><td>Permanently delete a campaign from your Zoho Campaigns organization, identified by its campaign key.</td></tr><tr><td>Delete Mailing List</td><td><code>deleteMailingList</code></td><td>Delete a Zoho Campaigns mailing list, optionally also removing its contacts from the whole organization.</td></tr><tr><td>Get Campaign Details</td><td><code>getCampaignDetails</code></td><td>Retrieve the full details of a single Zoho Campaigns campaign, identified by its campaign key.</td></tr><tr><td>Get Campaign Reports</td><td><code>getCampaignReports</code></td><td>Retrieve the performance report for a sent Zoho Campaigns campaign, including sent, open, click, bounce and unsubscribe counts.</td></tr><tr><td>List Contact Fields</td><td><code>listContactFields</code></td><td>Retrieve every contact field defined in your Zoho Campaigns account, including display names and field names. Use these field names when building the contact information for subscribe and unsubscribe actions.</td></tr><tr><td>List Contacts In Mailing List</td><td><code>listContactsInMailingList</code></td><td>Retrieve the contacts belonging to a Zoho Campaigns mailing list, optionally filtered by subscription status and paginated.</td></tr><tr><td>List Mailing Lists</td><td><code>listMailingLists</code></td><td>Retrieve the mailing lists in your Zoho Campaigns organization, with optional sorting and pagination. Each list returns its list key, which other actions require.</td></tr><tr><td>List Recent Campaigns</td><td><code>listRecentCampaigns</code></td><td>Retrieve recently created campaigns in your Zoho Campaigns organization, optionally filtered by status. Each campaign returns its campaign key, which the campaign detail, send, schedule, report and delete actions require.</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Topics</td><td><code>listTopics</code></td><td>Retrieve the topics configured in your Zoho Campaigns account. Topics group the kinds of email a contact can opt in to and are required when creating a campaign.</td></tr><tr><td>Schedule Campaign</td><td><code>scheduleCampaign</code></td><td>Schedule an existing Zoho Campaigns campaign to be sent at a specific date and time, optionally using timewarp delivery in each recipient's own timezone.</td></tr><tr><td>Send Campaign</td><td><code>sendCampaign</code></td><td>Send an existing Zoho Campaigns campaign immediately to its configured mailing lists.</td></tr><tr><td>Subscribe Contact To Mailing List</td><td><code>subscribeContactToMailingList</code></td><td>Add a contact to a Zoho Campaigns mailing list and send the subscription email. Contact details are supplied as a JSON object of Zoho Campaigns contact field names.</td></tr><tr><td>Unsubscribe Contact From Mailing List</td><td><code>unsubscribeContactFromMailingList</code></td><td>Unsubscribe a contact from a Zoho Campaigns mailing list, or from a specific topic within it.</td></tr><tr><td>Update Mailing List</td><td><code>updateMailingList</code></td><td>Rename a Zoho Campaigns mailing list and set whether its signup form is public or private.</td></tr></tbody></table>

</details>

