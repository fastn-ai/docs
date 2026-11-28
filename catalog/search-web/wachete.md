---
description: "Wachete monitors websites for changes. Manage monitoring jobs and folders, and read change notifications."
hidden: true
---

# Wachete

<img src="../../.gitbook/assets/connectors/lg/wachete.png" alt="Wachete logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [wachete.com](https://wachete.com) |
| **Authentication** | Username and password |
| **Slug** | `wachete` |

## Setup

Your customers enter their username and password for Wachete when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Wachete from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Wachete**.
2. Select **Connect** on the Wachete card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Wachete's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Folder</td><td><code>createFolder</code></td><td>Creates a folder for organising Wachete monitoring jobs, optionally nested inside an existing folder. Supplying an existing Folder ID renames that folder instead of creating a new one.</td></tr><tr><td>Create Or Update Wachet</td><td><code>saveWachet</code></td><td>Creates a new Wachete monitoring job (wachet) or updates an existing one. Omit Wachet ID to create; supply it to update. The job type cannot be changed on an existing wachet.</td></tr><tr><td>Delete Folder</td><td><code>deleteFolder</code></td><td>Permanently deletes a Wachete folder together with everything inside it, including nested folders and their monitoring jobs. This cannot be undone.</td></tr><tr><td>Delete Wachet</td><td><code>deleteWachet</code></td><td>Permanently deletes a Wachete monitoring job and its collected history. This cannot be undone.</td></tr><tr><td>Get API Token</td><td><code>getApiToken</code></td><td>Exchanges a Wachete user id and API key for a bearer token that authenticates every other Wachete API call. Both values are shown in the Wachete web app under your profile. The returned token is what you paste into this connector's API Token credential field.</td></tr><tr><td>Get Notification Content</td><td><code>getNotification</code></td><td>Retrieves the full captured page content behind a single Wachete notification, including the stored HTML snapshot. Use the notification id returned by List Notifications.</td></tr><tr><td>Get Wachet</td><td><code>getWachet</code></td><td>Retrieves a single Wachete monitoring job by id, including its settings, alert rules and the most recent check result.</td></tr><tr><td>Invalidate All API Tokens</td><td><code>invalidateTokens</code></td><td>Revokes every bearer token previously issued for the Wachete account, including the token this connection uses. After calling this you must mint a new token with Get API Token and update the connection.</td></tr><tr><td>List Folders</td><td><code>listFolders</code></td><td>Lists the contents of a Wachete folder: its subfolders, the monitoring jobs (wachets) it contains and the breadcrumb path to it. Omit Parent Folder ID to list the root folder.</td></tr><tr><td>List Notifications</td><td><code>listNotifications</code></td><td>Lists the change and error notifications raised by Wachete, newest first. Filter to one monitoring job with Wachet ID, or to a time window with From and To.</td></tr></tbody></table>

<details>

<summary>View 5 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Wachet Data History</td><td><code>listWachetData</code></td><td>Returns the history of values captured by a monitoring job, newest first, optionally limited to a time window. Set Return Diff to true to receive a Google-diff breakdown of each change instead of the plain captured value.</td></tr><tr><td>List Wachet Pages</td><td><code>listWachetPages</code></td><td>Lists the individual pages discovered by a Portal (crawling) monitoring job, each with its own latest captured content. A SinglePage wachet has no sub-pages and returns an empty list.</td></tr><tr><td>Log In With Email And Password</td><td><code>loginWithPassword</code></td><td>Exchanges a Wachete account email and password for a bearer token. Prefer Get API Token, which uses a revocable API key instead of account credentials.</td></tr><tr><td>Move Wachets And Folders</td><td><code>moveToFolder</code></td><td>Moves the given monitoring jobs (wachets) and folders into a target folder. Supply at least one wachet id or folder id; leave Target Folder ID empty to move the items to the root.</td></tr><tr><td>Search Wachets</td><td><code>searchWachets</code></td><td>Searches every monitoring job on the account and returns those whose name, URL or captured content matches the query. Matching is on word prefixes, so a partial term such as 'price' matches while a full hyphenated name may not.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Check Failed</td><td><code>Error</code></td><td>Wachete could not fetch or evaluate the monitored page. To receive this event, add the Fastn trigger URL as a Webhook notification endpoint on the wachet: open wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; choose Webhook &gt; paste the trigger URL &gt; Save. The same thing can be done through this connector's Create Or Update Wachet action by setting notificationEndpoints to [{"type":"Webhook","value":"&lt;trigger URL&gt;"}]. The wachet must also have an alert of type Error configured.</td></tr><tr><td>Check Recovered</td><td><code>ErrorRecovered</code></td><td>A wachet that had been failing fetched successfully again. Register the Fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet an ErrorRecovered alert.</td></tr><tr><td>Content Changed</td><td><code>NotEq</code></td><td>The monitored content changed since the previous check. Register the Fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet a NotEq alert.</td></tr><tr><td>Content Contains Value</td><td><code>Contains</code></td><td>The monitored content started containing the alert's comparison value. Register the Fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet a Contains alert.</td></tr><tr><td>Content Matches Value</td><td><code>Eq</code></td><td>The monitored content became equal to the alert's comparison value. Register the Fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet an Eq alert with the value to match.</td></tr><tr><td>Content No Longer Contains Value</td><td><code>NotContains</code></td><td>The monitored content stopped containing the alert's comparison value. Register the Fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet a NotContains alert.</td></tr><tr><td>Value Greater Than</td><td><code>Gt</code></td><td>Numeric monitored content rose above the alert's comparison value. Register the Fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet a Gt alert.</td></tr><tr><td>Value Greater Than Or Equal</td><td><code>GtEq</code></td><td>Numeric monitored content reached or rose above the alert's comparison value. Register the Fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet a GtEq alert.</td></tr><tr><td>Value Less Than</td><td><code>Lt</code></td><td>Numeric monitored content fell below the alert's comparison value. Register the Fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet an Lt alert.</td></tr><tr><td>Value Less Than Or Equal</td><td><code>LtEq</code></td><td>Numeric monitored content reached or fell below the alert's comparison value. Register the Fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet an LtEq alert.</td></tr></tbody></table>
