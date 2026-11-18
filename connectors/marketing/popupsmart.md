---
description: "Popupsmart popup builder."
hidden: true
---

# Popupsmart

<img src="../../.gitbook/assets/connectors/lg/popupsmart.png" alt="Popupsmart logo">

Popupsmart popup builder. Public Leads API (GET /api/leads, x-token + x-campaign-id headers) plus the app.popupsmart.com GraphQL dashboard API (campaigns, websites, folders, segments, leads, analytics, templates, webhook integrations) authenticated with a dashboard access token.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [popupsmart.com](https://popupsmart.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `popupsmart` |

## Use it

Add Popupsmart from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.popupsmart.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Campaign | `createCampaign` | Create a new Popupsmart campaign (popup) as a DRAFT on one or more registered website ids. Verified: the new campaign comes back with status=false and publishVersion=0 - it is NOT live on the website until Publish Campaign is called. Dashboard Access Token connection. |
| Create Folder | `createFolder` | Create a campaign folder. Requires a Popupsmart plan that includes the folder feature (accountPlan.hasFolderFeature); on plans without it the API answers "Folder feature is not available on your current plan." Dashboard Access Token connection. |
| Create Webhook Integration | `createWebhookIntegration` | Register a webhook on a Popupsmart campaign. Popupsmart POSTs the submitted form data to the given URL every time a visitor submits that campaign's popup. campaignId is required by the backend. Returns the new integration id. Dashboard Access Token connection. |
| Create Website | `createWebsite` | Register a website (domain) on the Popupsmart account so campaigns can target it. Bounded by the plan's domain limit; over the limit the API answers WEBSITE_LIMIT_EXCEEDED. Dashboard Access Token connection. |
| Delete Campaign | `deleteCampaign` | Permanently delete a Popupsmart campaign by id. Returns true on success. Dashboard Access Token connection. |
| Delete Folder | `deleteFolder` | Delete a campaign folder by id. Paid-plan feature (see Create Folder). Dashboard Access Token connection. |
| Delete Webhook Integration | `deleteWebhookIntegration` | Remove a Popupsmart webhook integration by id so form submissions stop being forwarded. Dashboard Access Token connection. |
| Delete Website | `deleteWebsite` | DESTRUCTIVE. Remove a website (domain) from the Popupsmart account. Campaigns targeting only that domain are orphaned. Dashboard Access Token connection. |
| Get Account Stats | `getAccountStats` | Return the connected Popupsmart account's usage against plan limits: page views, emails, extension totals and the blocked flag. Dashboard Access Token connection. |
| Get Campaign | `getCampaign` | Fetch one Popupsmart campaign (popup) by numeric id, including its status, publish version, domains, targeting rules, layout and settings. Dashboard Access Token connection. |
| Get Campaign Counts | `getCampaignCounts` | Return how many Popupsmart campaigns the account has in total, active and passive. Dashboard Access Token connection. |
| Get Current User | `getMe` | Return the signed-in Popupsmart dashboard user and their account plan. Uses the Dashboard Access Token connection. NOTE: the vendor's own `me` query also exposes the account's raw API key (`apiToken`); this action deliberately does NOT request that field. |
| Get Leads | `getLeads` | Download the leads (popup form submissions) collected by the connected Popupsmart campaign. Uses the public Leads API. Default window is 1 day; maximum window is 90 days. Returns { leads: [...] } where each lead carries submission data plus session, location, page, device and user-agent metadata. |
| Get Page Analytics | `getPageAnalytics` | Per-page Popupsmart analytics for a date range: which pages the popups were displayed on and how they performed. Dashboard Access Token connection. |
| Get Short Analytics | `getShortAnalytics` | Headline Popupsmart analytics for a date range: displays, interactions, leads, page views, visitors and driven revenue, each with the previous-period comparison. Dashboard Access Token connection. |
| List Accounts | `listAccounts` | List the Popupsmart accounts (organizations) the signed-in dashboard user belongs to, with ownership and agency flags. Dashboard Access Token connection. |
| List Campaigns | `listCampaigns` | List every Popupsmart campaign (popup) in the connected account with its id, name, active flag, publish version, conversion rate, folder and domains. Dashboard Access Token connection. |
| List Folders | `listFolders` | List the campaign folders on the connected Popupsmart account and the campaigns inside each. Folders are a paid-plan feature. Dashboard Access Token connection. |
| List Invitations | `listInvitations` | List pending teammate invitations on the connected Popupsmart account with their role and campaign scope. Dashboard Access Token connection. |
| List Leads (Dashboard) | `listLeadsDashboard` | Page through the leads captured by one Popupsmart campaign over a date range, using the dashboard GraphQL API. Returns items, total and the column list. Lead rows contain personal data (email, IP, city). Dashboard Access Token connection. |
| List Segments | `listSegments` | List the audience segments defined for one Popupsmart campaign, with their targeting rules and category. Dashboard Access Token connection. |
| List Template Tags | `listTemplateTags` | List the popup-template tag taxonomy (goals, industries, seasons) with template counts. Use the returned tag ids as input to Search Templates. Dashboard Access Token connection. |
| List Webhook Integrations | `listWebhookIntegrations` | List every webhook integration on the connected Popupsmart account. Each entry is a URL that Popupsmart POSTs to when a popup form is submitted on the given campaign. Dashboard Access Token connection. |
| List Websites | `listWebsites` | List the websites (domains) registered on the connected Popupsmart account, with verification state, detected CMS and campaign count. Dashboard Access Token connection. |
| Login (Mint Dashboard Access Token) | `login` | Exchange Popupsmart dashboard email + password for an accessToken (valid 24h) and a refreshToken. Use the accessToken as the credential for the "Dashboard Access Token (GraphQL)" auth method. Needs no existing credential. |
| Publish Campaign | `publishCampaign` | DESTRUCTIVE / GOES LIVE. Publish a Popupsmart campaign so the popup starts showing to real visitors on the registered website. Only call this when you intend the popup to be live. Returns { success, message, code }. Dashboard Access Token connection. |
| Rename Campaign | `renameCampaign` | Rename an existing Popupsmart campaign. Does not change its published state. Dashboard Access Token connection. |
| Search Templates | `searchTemplates` | Search the Popupsmart popup-template gallery by tag ids (get the ids from List Template Tags). Returns template id, name, thumbnail and device type. Dashboard Access Token connection. |
| Update Folder | `updateFolder` | Rename a campaign folder. Paid-plan feature (see Create Folder). Dashboard Access Token connection. |
| Update Webhook Integration | `updateWebhookIntegration` | Change the name, target URL or campaign of an existing Popupsmart webhook integration. Dashboard Access Token connection. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Popup form submitted | `form.submission` | Fires when a visitor submits the form of the selected Popupsmart campaign. Popupsmart delivers the submission by POSTing to the registered webhook-integration URL. NOTE: this payloadSchema is MODELLED from the fields Popupsmart stores on a lead (the `leads` GraphQL query and the public /api/leads response) - it was NOT captured from a real delivery, because capturing one requires a published popup on a site that actually embeds the Popupsmart snippet. |
