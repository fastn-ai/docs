---
description: "Popupsmart is a website popup builder. Manage campaigns, websites and folders, read leads and stats, and set up webhooks."
hidden: true
---

# Popupsmart

<img src="../../.gitbook/assets/connectors/lg/popupsmart.png" alt="Popupsmart logo">

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [popupsmart.com](https://popupsmart.com) |
| **Authentication** | API token |
| **Slug** | `popupsmart` |

## Setup

Your customers enter their API token for Popupsmart when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Popupsmart from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Popupsmart**.
2. Select **Connect** on the Popupsmart card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Popupsmart's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Campaign</td><td><code>createCampaign</code></td><td>Create a new Popupsmart campaign (popup) as a DRAFT on one or more registered website ids. Verified: the new campaign comes back with status=false and publishVersion=0 - it is NOT live on the website until Publish Campaign is called. Dashboard Access Token connection.</td></tr><tr><td>Create Folder</td><td><code>createFolder</code></td><td>Create a campaign folder. Requires a Popupsmart plan that includes the folder feature (accountPlan.hasFolderFeature); on plans without it the API answers "Folder feature is not available on your current plan." Dashboard Access Token connection.</td></tr><tr><td>Create Webhook Integration</td><td><code>createWebhookIntegration</code></td><td>Register a webhook on a Popupsmart campaign. Popupsmart POSTs the submitted form data to the given URL every time a visitor submits that campaign's popup. campaignId is required by the backend. Returns the new integration id. Dashboard Access Token connection.</td></tr><tr><td>Create Website</td><td><code>createWebsite</code></td><td>Register a website (domain) on the Popupsmart account so campaigns can target it. Bounded by the plan's domain limit; over the limit the API answers WEBSITE_LIMIT_EXCEEDED. Dashboard Access Token connection.</td></tr><tr><td>Delete Campaign</td><td><code>deleteCampaign</code></td><td>Permanently delete a Popupsmart campaign by id. Returns true on success. Dashboard Access Token connection.</td></tr><tr><td>Delete Folder</td><td><code>deleteFolder</code></td><td>Delete a campaign folder by id. Paid-plan feature (see Create Folder). Dashboard Access Token connection.</td></tr><tr><td>Delete Webhook Integration</td><td><code>deleteWebhookIntegration</code></td><td>Remove a Popupsmart webhook integration by id so form submissions stop being forwarded. Dashboard Access Token connection.</td></tr><tr><td>Delete Website</td><td><code>deleteWebsite</code></td><td>DESTRUCTIVE. Remove a website (domain) from the Popupsmart account. Campaigns targeting only that domain are orphaned. Dashboard Access Token connection.</td></tr><tr><td>Get Account Stats</td><td><code>getAccountStats</code></td><td>Return the connected Popupsmart account's usage against plan limits: page views, emails, extension totals and the blocked flag. Dashboard Access Token connection.</td></tr><tr><td>Get Campaign</td><td><code>getCampaign</code></td><td>Fetch one Popupsmart campaign (popup) by numeric id, including its status, publish version, domains, targeting rules, layout and settings. Dashboard Access Token connection.</td></tr></tbody></table>

<details>

<summary>View 20 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Campaign Counts</td><td><code>getCampaignCounts</code></td><td>Return how many Popupsmart campaigns the account has in total, active and passive. Dashboard Access Token connection.</td></tr><tr><td>Get Current User</td><td><code>getMe</code></td><td>Return the signed-in Popupsmart dashboard user and their account plan. Uses the Dashboard Access Token connection. NOTE: the vendor's own `me` query also exposes the account's raw API key (`apiToken`); this action deliberately does NOT request that field.</td></tr><tr><td>Get Leads</td><td><code>getLeads</code></td><td>Download the leads (popup form submissions) collected by the connected Popupsmart campaign. Uses the public Leads API. Default window is 1 day; maximum window is 90 days. Returns { leads: [...] } where each lead carries submission data plus session, location, page, device and user-agent metadata.</td></tr><tr><td>Get Page Analytics</td><td><code>getPageAnalytics</code></td><td>Per-page Popupsmart analytics for a date range: which pages the popups were displayed on and how they performed. Dashboard Access Token connection.</td></tr><tr><td>Get Short Analytics</td><td><code>getShortAnalytics</code></td><td>Headline Popupsmart analytics for a date range: displays, interactions, leads, page views, visitors and driven revenue, each with the previous-period comparison. Dashboard Access Token connection.</td></tr><tr><td>List Accounts</td><td><code>listAccounts</code></td><td>List the Popupsmart accounts (organizations) the signed-in dashboard user belongs to, with ownership and agency flags. Dashboard Access Token connection.</td></tr><tr><td>List Campaigns</td><td><code>listCampaigns</code></td><td>List every Popupsmart campaign (popup) in the connected account with its id, name, active flag, publish version, conversion rate, folder and domains. Dashboard Access Token connection.</td></tr><tr><td>List Folders</td><td><code>listFolders</code></td><td>List the campaign folders on the connected Popupsmart account and the campaigns inside each. Folders are a paid-plan feature. Dashboard Access Token connection.</td></tr><tr><td>List Invitations</td><td><code>listInvitations</code></td><td>List pending teammate invitations on the connected Popupsmart account with their role and campaign scope. Dashboard Access Token connection.</td></tr><tr><td>List Leads (Dashboard)</td><td><code>listLeadsDashboard</code></td><td>Page through the leads captured by one Popupsmart campaign over a date range, using the dashboard GraphQL API. Returns items, total and the column list. Lead rows contain personal data (email, IP, city). Dashboard Access Token connection.</td></tr><tr><td>List Segments</td><td><code>listSegments</code></td><td>List the audience segments defined for one Popupsmart campaign, with their targeting rules and category. Dashboard Access Token connection.</td></tr><tr><td>List Template Tags</td><td><code>listTemplateTags</code></td><td>List the popup-template tag taxonomy (goals, industries, seasons) with template counts. Use the returned tag ids as input to Search Templates. Dashboard Access Token connection.</td></tr><tr><td>List Webhook Integrations</td><td><code>listWebhookIntegrations</code></td><td>List every webhook integration on the connected Popupsmart account. Each entry is a URL that Popupsmart POSTs to when a popup form is submitted on the given campaign. Dashboard Access Token connection.</td></tr><tr><td>List Websites</td><td><code>listWebsites</code></td><td>List the websites (domains) registered on the connected Popupsmart account, with verification state, detected CMS and campaign count. Dashboard Access Token connection.</td></tr><tr><td>Login (Mint Dashboard Access Token)</td><td><code>login</code></td><td>Exchange Popupsmart dashboard email + password for an accessToken (valid 24h) and a refreshToken. Use the accessToken as the credential for the "Dashboard Access Token (GraphQL)" auth method. Needs no existing credential.</td></tr><tr><td>Publish Campaign</td><td><code>publishCampaign</code></td><td>DESTRUCTIVE / GOES LIVE. Publish a Popupsmart campaign so the popup starts showing to real visitors on the registered website. Only call this when you intend the popup to be live. Returns { success, message, code }. Dashboard Access Token connection.</td></tr><tr><td>Rename Campaign</td><td><code>renameCampaign</code></td><td>Rename an existing Popupsmart campaign. Does not change its published state. Dashboard Access Token connection.</td></tr><tr><td>Search Templates</td><td><code>searchTemplates</code></td><td>Search the Popupsmart popup-template gallery by tag ids (get the ids from List Template Tags). Returns template id, name, thumbnail and device type. Dashboard Access Token connection.</td></tr><tr><td>Update Folder</td><td><code>updateFolder</code></td><td>Rename a campaign folder. Paid-plan feature (see Create Folder). Dashboard Access Token connection.</td></tr><tr><td>Update Webhook Integration</td><td><code>updateWebhookIntegration</code></td><td>Change the name, target URL or campaign of an existing Popupsmart webhook integration. Dashboard Access Token connection.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Popup form submitted</td><td><code>form.submission</code></td><td>Fires when a visitor submits the form of the selected Popupsmart campaign. Popupsmart delivers the submission by POSTing to the registered webhook-integration URL.</td></tr></tbody></table>
