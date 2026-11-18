---
description: "Wachete is a website-change monitoring service."
---

# Wachete

Wachete is a website-change monitoring service. This connector covers the full Wachete third-party REST API: monitoring jobs (wachets), folders, collected page data, change notifications, sub-pages of crawl jobs and API token management.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [wachete.com](https://wachete.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 15 |
| **Events** | 10 |
| **Slug** | `wachete` |

## Use it

Add Wachete from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wachete.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Folder | `createFolder` | Creates a folder for organising Wachete monitoring jobs, optionally nested inside an existing folder. Supplying an existing Folder ID renames that folder instead of creating a new one. |
| Create Or Update Wachet | `saveWachet` | Creates a new Wachete monitoring job (wachet) or updates an existing one. Omit Wachet ID to create; supply it to update. The job type cannot be changed on an existing wachet. |
| Delete Folder | `deleteFolder` | Permanently deletes a Wachete folder together with everything inside it, including nested folders and their monitoring jobs. This cannot be undone. |
| Delete Wachet | `deleteWachet` | Permanently deletes a Wachete monitoring job and its collected history. This cannot be undone. |
| Get API Token | `getApiToken` | Exchanges a Wachete user id and API key for a bearer token that authenticates every other Wachete API call. Both values are shown in the Wachete web app under your profile. The returned token is what you paste into this connector's API Token credential field. |
| Get Notification Content | `getNotification` | Retrieves the full captured page content behind a single Wachete notification, including the stored HTML snapshot. Use the notification id returned by List Notifications. |
| Get Wachet | `getWachet` | Retrieves a single Wachete monitoring job by id, including its settings, alert rules and the most recent check result. |
| Invalidate All API Tokens | `invalidateTokens` | Revokes every bearer token previously issued for the Wachete account, including the token this connection uses. After calling this you must mint a new token with Get API Token and update the connection. |
| List Folders | `listFolders` | Lists the contents of a Wachete folder: its subfolders, the monitoring jobs (wachets) it contains and the breadcrumb path to it. Omit Parent Folder ID to list the root folder. |
| List Notifications | `listNotifications` | Lists the change and error notifications raised by Wachete, newest first. Filter to one monitoring job with Wachet ID, or to a time window with From and To. |
| List Wachet Data History | `listWachetData` | Returns the history of values captured by a monitoring job, newest first, optionally limited to a time window. Set Return Diff to true to receive a Google-diff breakdown of each change instead of the plain captured value. |
| List Wachet Pages | `listWachetPages` | Lists the individual pages discovered by a Portal (crawling) monitoring job, each with its own latest captured content. A SinglePage wachet has no sub-pages and returns an empty list. |
| Log In With Email And Password | `loginWithPassword` | Exchanges a Wachete account email and password for a bearer token. Prefer Get API Token, which uses a revocable API key instead of account credentials. |
| Move Wachets And Folders | `moveToFolder` | Moves the given monitoring jobs (wachets) and folders into a target folder. Supply at least one wachet id or folder id; leave Target Folder ID empty to move the items to the root. |
| Search Wachets | `searchWachets` | Searches every monitoring job on the account and returns those whose name, URL or captured content matches the query. Matching is on word prefixes, so a partial term such as 'price' matches while a full hyphenated name may not. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Check Failed | `Error` | Wachete could not fetch or evaluate the monitored page. To receive this event, add the fastn trigger URL as a Webhook notification endpoint on the wachet: open wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; choose Webhook &gt; paste the trigger URL &gt; Save. The same thing can be done through this connector's Create Or Update Wachet action by setting notificationEndpoints to [{"type":"Webhook","value":"&lt;trigger URL&gt;"}]. The wachet must also have an alert of type Error configured. Payload schema captured from a real Wachete delivery. |
| Check Recovered | `ErrorRecovered` | A wachet that had been failing fetched successfully again. Register the fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet an ErrorRecovered alert. Payload modelled on a captured Wachete delivery. |
| Content Changed | `NotEq` | The monitored content changed since the previous check. Register the fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet a NotEq alert. Payload modelled on a captured Wachete delivery. |
| Content Contains Value | `Contains` | The monitored content started containing the alert's comparison value. Register the fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet a Contains alert. Payload modelled on a captured Wachete delivery. |
| Content Matches Value | `Eq` | The monitored content became equal to the alert's comparison value. Register the fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet an Eq alert with the value to match. Payload modelled on a captured Wachete delivery. |
| Content No Longer Contains Value | `NotContains` | The monitored content stopped containing the alert's comparison value. Register the fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet a NotContains alert. Payload modelled on a captured Wachete delivery. |
| Value Greater Than | `Gt` | Numeric monitored content rose above the alert's comparison value. Register the fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet a Gt alert. Payload modelled on a captured Wachete delivery. |
| Value Greater Than Or Equal | `GtEq` | Numeric monitored content reached or rose above the alert's comparison value. Register the fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet a GtEq alert. Payload modelled on a captured Wachete delivery. |
| Value Less Than | `Lt` | Numeric monitored content fell below the alert's comparison value. Register the fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet an Lt alert. Payload modelled on a captured Wachete delivery. |
| Value Less Than Or Equal | `LtEq` | Numeric monitored content reached or fell below the alert's comparison value. Register the fastn trigger URL as a Webhook notification endpoint on the wachet (wachete.com &gt; sign in &gt; select the wachet &gt; Notifications &gt; Add endpoint &gt; Webhook &gt; paste the trigger URL &gt; Save), and give the wachet an LtEq alert. Payload modelled on a captured Wachete delivery. |
