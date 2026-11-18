---
description: "WhatConverts lead tracking and call tracking."
hidden: true
---

# WhatConverts

<img src="../../.gitbook/assets/connectors/what-converts.png" alt="WhatConverts logo" width="64">

WhatConverts lead tracking and call tracking. Read, create and update leads across every lead type (phone calls, web forms, chats, text messages, transactions, custom events, emails, appointments) with full marketing attribution, qualify and value them (quotable, quote_value, sales_value), and manage the agency hierarchy: accounts, profiles, users, roles, tracking phone numbers and tracked web forms. Wraps the REST API at https://app.whatconverts.com/api/v1 using HTTP Basic auth with an API token and secret.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [whatconverts.com](https://whatconverts.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `whatConverts` |

## Use it

Add WhatConverts from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.whatConverts.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Account | `createAccount` | Create a new account under the master account, optionally creating a first profile inside it. Requires an Agency (master account) API key. |
| Create Lead | `createLead` | Create a lead in a WhatConverts profile. lead_type is required; profile_id is required when using an Agency (master account) key and implicit when using a profile key. Fields that do not apply to the chosen lead type are simply omitted. Pass wc_client_current (the WhatConverts visitor cookie) to auto-populate source, medium, campaign, content, keyword, gclid, msclkid, user_id and landing_url. |
| Create Profile | `createProfile` | Create a new profile inside an account. A profile is the tracking container that owns tracking numbers, web forms and leads. Requires an Agency (master account) API key. |
| Create User | `createUser` | Invite a new dashboard user. Master account users take a role_id; account users take an accounts array granting per-account access and role. The user is created pending activation and receives an activation email. Requires an Agency (master account) API key. |
| Delete Account | `deleteAccount` | Permanently delete an account. This removes every profile, tracking number, lead and setting belonging to it and cannot be undone. Requires an Agency (master account) API key. |
| Delete Profile | `deleteProfile` | Permanently delete a profile. This removes every tracking number, lead and setting belonging to it and cannot be undone. Requires an Agency (master account) API key. |
| Delete Tracking Number | `deleteTrackingNumber` | Release a call tracking phone number. The number stops routing calls and is removed from its pool. Irreversible - the number may not be reclaimable afterwards. |
| Delete Web Form | `deleteWebForm` | Stop tracking a web form. Existing leads captured from it are kept; future submissions are no longer recorded. |
| Get Account | `getAccount` | Retrieve a single account and its profiles by account_id. Requires an Agency (master account) API key. |
| Get Account Info | `getAccountInfo` | Identify which WhatConverts account and profile this connection's API key belongs to. Takes no input: it reads the single most recent lead and returns its account_id, account, profile_id and profile. Used as the account-mapping action for webhook (app event) triggers, and as a cheap connection health check. Returns an empty leads array if the profile has never captured a lead. |

<details>

<summary>See 16 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Call Recording | `getRecording` | Download the call recording for a phone call lead. The response body is a raw MP3 file, not JSON, so fastn's HTTP executor may fail on it with a body-already-read error; for audio prefer the absolute recording / play_recording / voicemail / play_voicemail URLs already returned on the lead object by Get Lead. |
| Get Lead | `getLead` | Retrieve a single lead by its lead_id, including attribution, contact details, call recording links and transcriptions, form submissions and custom fields. |
| Get Profile | `getProfile` | Retrieve a single profile inside an account. Requires an Agency (master account) API key. |
| Get Role | `getRole` | Retrieve a single role with its full permission matrix (none, view or edit per area: integrations, leads, profiles, reports, settings, tracking, accounts, billing, security, users) and whether it receives lead notifications. Requires an Agency (master account) API key. The API returns the role inside a paginated envelope whose array is named users. |
| Get User | `getUser` | Retrieve a single dashboard user, including their lead-notification preferences and the accounts they can access. Requires an Agency (master account) API key. Note the API returns this single user inside the same paginated envelope as the list endpoint. |
| List Accounts | `listAccounts` | Retrieve a paginated list of accounts with their profiles. Requires an Agency (master account) API key; a profile key is rejected. |
| List Leads | `listLeads` | Retrieve a paginated list of leads with full marketing attribution. Supports filtering by lead type, status, date range, quotable state, value, contact details and every UTM dimension. account_id and profile_id filters require an Agency (master account) key. Date ranges span at most 400 days. |
| List Profiles | `listProfiles` | Retrieve a paginated list of the profiles inside one account. Requires an Agency (master account) API key. Use this to populate a profile picker before creating leads. |
| List Roles | `listRoles` | Retrieve the user roles available on the master account. Use this to resolve the role_id needed when creating or editing a user. Requires an Agency (master account) API key. |
| List Tracking Numbers | `listTrackingNumbers` | Retrieve the call tracking phone numbers on the connection, with their destination, swap number, pool trigger, source/medium assignment, recording and messaging flags and last-used date. account_id and profile_id filters require an Agency (master account) key. |
| List Users | `listUsers` | Retrieve a paginated list of dashboard users with their role and activation state. Requires an Agency (master account) API key. |
| List Web Forms | `listWebForms` | Retrieve the web forms WhatConverts is tracking (the form report), with the DOM attribute and submit-button selector each one is matched on. account_id and profile_id filters require an Agency (master account) key. |
| Update Account | `updateAccount` | Rename an existing account. Requires an Agency (master account) API key. |
| Update Lead | `updateLead` | Edit an existing lead: qualify it (quotable), attach quote and sales values, correct the lead URL, or write additional/custom fields. Only the fields you supply are changed. This is the endpoint behind "qualify" and "value" a lead in the WhatConverts Lead Manager. |
| Update Profile | `updateProfile` | Rename an existing profile. Requires an Agency (master account) API key. |
| Update User | `updateUser` | Edit an existing dashboard user: change their master-account role, their default notifications, or their per-account access. Same path as Create User - the presence of user_id in the body is what makes it an edit. Set an entry's role_id to false in the accounts array to revoke access to that account. Requires an Agency (master account) API key. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Appointment lead | `Appointment` | An appointment booking was captured or updated. Setup: profile -&gt; Tracking -&gt; Integrations -&gt; Automations -&gt; Webhooks -&gt; Add Webhook, paste the fastn URL and tick Appointments. Booking details arrive in additional_fields. |
| Chat lead | `Chat` | A web chat conversation was captured or updated. Setup: profile -&gt; Tracking -&gt; Integrations -&gt; Automations -&gt; Webhooks -&gt; Add Webhook, paste the fastn URL and tick Chats. Chat fields arrive in additional_fields. |
| Custom event lead | `Custom Event` | A custom event tracked by the WhatConverts script was captured or updated. Setup: profile -&gt; Tracking -&gt; Integrations -&gt; Automations -&gt; Webhooks -&gt; Add Webhook, paste the fastn URL and tick Custom Events. Event category, action and label arrive in additional_fields. |
| Email lead | `Email` | An email lead was captured or updated. Setup: profile -&gt; Tracking -&gt; Integrations -&gt; Automations -&gt; Webhooks -&gt; Add Webhook, paste the fastn URL and tick Emails. Sender, subject and body arrive in additional_fields. |
| Phone call lead | `Phone Call` | A phone call lead was created or updated. Setup: in the WhatConverts profile go to Tracking -&gt; Integrations -&gt; Automations -&gt; Webhooks -&gt; Connect -&gt; Add Webhook, paste the fastn webhook URL, tick Phone Calls and choose the trigger type (New or Update). Read the payload's trigger field to tell new from update. Max 5 webhooks per profile. |
| Text message lead | `Text Message` | An inbound text message to a tracking number was captured or updated. Setup: profile -&gt; Tracking -&gt; Integrations -&gt; Automations -&gt; Webhooks -&gt; Add Webhook, paste the fastn URL and tick Text Messages. |
| Transaction lead | `Transaction` | An e-commerce transaction was captured or updated. Setup: profile -&gt; Tracking -&gt; Integrations -&gt; Automations -&gt; Webhooks -&gt; Add Webhook, paste the fastn URL and tick Transactions. Transaction details arrive in additional_fields; the order value is on quote_value / sales_value. |
| Web form lead | `Web Form` | A web form submission was captured or updated. Setup: profile -&gt; Tracking -&gt; Integrations -&gt; Automations -&gt; Webhooks -&gt; Add Webhook, paste the fastn URL and tick Web Forms. form_name identifies the form; every submitted field arrives in additional_fields. |
