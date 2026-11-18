---
description: "Poper is an AI popup, form, quiz, survey and widget builder for websites."
---

# Poper

Poper is an AI popup, form, quiz, survey and widget builder for websites. This connector wraps the Poper General API (https://api.poper.ai/general/v1) to list projects, domains and campaigns (popups, forms, quizzes, NPS surveys, widgets, games), read captured leads and responses, and pull domain- and campaign-level analytics. Authentication uses a Poper API key that the vendor requires in the request body.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [poper.ai](https://poper.ai) |
| **Authentication** | Credentials you enter |
| **Actions** | 29 |
| **Events** | 0 |
| **Slug** | `poper` |

## Use it

Add Poper from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.poper.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check API Availability | `checkApiAvailability` | Pings the root of the Poper API to confirm the service is reachable, without using an API key. Use Test API Key instead when you need to confirm that credentials are valid. |
| Check Email Availability | `checkEmailAvailability` | Checks whether an email address is already registered with Poper before a sign-up is attempted. Returns a message confirming that a new user can safely be created, or reporting that the address is already taken. NOTE: Poper serves this endpoint without authentication, so it is an account-enumeration surface; do not expose it to untrusted callers. |
| Confirm Password Reset | `confirmPasswordReset` | Completes Poper's forgotten-password flow by exchanging the one-time code that was emailed to the account holder for a new password. Answers with an identity-provider error when the email, code or password is rejected. |
| Create Poper Account | `createPoperAccount` | Registers a brand-new Poper user account from an email address and password, the same call Poper's own sign-up form makes. WARNING: Poper exposes no API route that deletes an account, so every successful call leaves a permanent user record; use Check Email Availability first. |
| Delete Temporary Widget State | `deleteTemporaryWidgetState` | Discards a stored draft widget configuration before its 24-hour expiry. WARNING: Poper answers with success even for a state id that does not exist, so confirm the outcome with Get Temporary Widget State rather than trusting this response. |
| Get Campaign Analytics | `getCampaignAnalytics` | Returns Poper analytics for one or more specific campaigns on a domain: total visits, opens, conversions and events, plus day-by-day series. Pass a single campaign id or a comma-separated list, and choose a preset date range or a custom start and end date. |
| Get Domain Analytics | `getDomainAnalytics` | Returns aggregate Poper analytics for one website domain: total visits, popup opens, conversions and leads, day-by-day visit, open and conversion series, and breakdown tables by campaign, traffic source, browser, operating system, page path and country. Choose a preset date range or supply a custom start and end date; 'today' returns hourly buckets instead of daily ones. |
| Get Team Invitation | `getTeamInvitation` | Looks up a pending Poper workspace invitation by its invitation id, so an invited collaborator can see who invited them before accepting. Answers 'Invitation not found.' for an unknown id. |
| Get Temporary Widget State | `getTemporaryWidgetState` | Reads back a draft widget configuration previously stored by Save Temporary Widget State. Answers 'Temporary widget state not found or expired' once the 24-hour window has passed or the state was deleted. |
| Get Username By Email | `getUsernameByEmail` | Resolves a Poper account's internal username from the email address it was registered with, for use in Poper's sign-in and password-recovery flows. Answers 'No User Found.' when no account matches. NOTE: Poper serves this endpoint without authentication, so it is an account-enumeration surface; do not expose it to untrusted callers. |
| Get Username By OAuth Access Token | `getUsernameByOauthAccessToken` | Resolves the Poper user behind an OAuth access token issued by Poper's identity provider, used when a visitor signs in with a social provider instead of an email and password. Returns the account's internal username and its identity attributes. Answers 'Invalid Token.' when the token is rejected. WARNING: the access token is passed in the request body, so every execution record of this action stores a live credential. |
| List Campaigns By Category | `listCampaignsByCategory` | Lists Poper campaigns of any kind, filtered by a broad category (popups, widgets, games, forms, quizzes, surveys or all) or by an explicit comma-separated list of campaign types. Also accepts project, domain and limit filters. Returns the matching campaigns, a count, a per-type breakdown and the list of campaign types the account supports. |
| List Domains | `listDomains` | Lists every website domain registered to the Poper account the API key belongs to, grouped by the project each domain sits under. Use a domain returned here as the Domain input of the analytics actions. |
| List Form Campaigns | `listFormCampaigns` | Lists every form campaign in the Poper account, optionally narrowed to a single project or website domain. Returns the campaign records together with a count and the breakdown of campaign types the account supports. |
| List Leads And Responses | `listLeadsAndResponses` | Returns the leads and campaign responses captured by Poper campaigns, with paging and filters for campaign id, category, project, domain, completion state and a recent-days window. WARNING: responses contain the contact details visitors submitted (email addresses, names, phone numbers), so treat the output as personal data. |
| List NPS Survey Campaigns | `listNpsSurveyCampaigns` | Lists every NPS survey campaign in the Poper account, optionally narrowed to a single project or website domain. Returns the campaign records together with a count and the breakdown of campaign types the account supports. |
| List Popup Campaigns | `listPopupCampaigns` | Lists every popup campaign in the Poper account, optionally narrowed to a single project or website domain. Returns the campaign records together with a count and the breakdown of campaign types the account supports. |
| List Popups Raw | `listPopupsRaw` | Returns the account's popup records as a flat popups array, without the campaign envelope, count or type breakdown that List Popup Campaigns adds. This is Poper's original List All Popups endpoint; prefer List Popup Campaigns when you also need counts or the per-type breakdown. |
| List Projects | `listProjects` | Lists every Poper project owned by the account the API key belongs to, each with its numeric id, name, timestamps and the website domains attached to it. Use the project id returned here to filter the campaign and lead actions. |
| List Quiz Campaigns | `listQuizCampaigns` | Lists every quiz campaign in the Poper account, optionally narrowed to a single project or website domain. Returns the campaign records together with a count and the breakdown of campaign types the account supports. |
| List Responses For Campaign | `listResponsesForCampaign` | Returns the raw responses captured by one specific Poper campaign, identified by its campaign id. WARNING: responses contain the contact details visitors submitted, so treat the output as personal data. |
| Promote Temporary Widget State | `promoteTemporaryWidgetState` | Copies a stored draft widget configuration onto a real Poper widget, so the settings held in a temporary state become the widget's live settings. Returns the per-key results and the temporary keys that were cleared. |
| Resend Account Verification Email | `resendAccountVerificationEmail` | Re-sends the sign-up confirmation email to a Poper account that has not yet been verified. WARNING: calling this with a registered, unverified address sends a real email to that person; it reports that no user exists for an unknown address without sending anything. |
| Save Temporary Widget State | `saveTemporaryWidgetState` | Stores a draft widget configuration as a temporary state that Poper keeps for 24 hours, so an in-progress widget can be handed between steps before it is promoted to a real widget. Returns the new state id and its expiry. NOTE: Poper serves this endpoint without authentication - anyone who can reach it can write a temporary state. |
| Send Password Reset Code | `sendPasswordResetCode` | Starts Poper's forgotten-password flow by emailing a one-time reset code to the address of an existing Poper account. WARNING: calling this with a registered address sends a real email to that person; it answers 'User doesn't exists.' for an unknown address without sending anything. |
| Test API Key | `testApiKey` | Verifies that the configured Poper API key is valid. Returns a Pong message together with the email address of the Poper account the key belongs to. Use this to confirm a connection before running other actions. |
| Upload Public Asset | `uploadPublicAsset` | Uploads a text asset to Poper's public landing-uploads bucket and returns the CDN URL it is served from, for use inside popup and widget content. Only text file formats are supported here because the fastn engine cannot carry binary multipart parts. SECURITY: Poper does not authenticate this endpoint - it is gated only by an allow-listed Origin header - and the resulting URL is world-readable with no expiry, and Poper exposes no route that deletes it. |
| Verify AppSumo Code | `verifyAppSumoCode` | Validates an AppSumo lifetime-deal redemption code against Poper before it is applied to an account. Returns the code's details when it is valid and 'Invalid Code.' when it is not. |
| Verify Shopify HMAC Signature | `verifyShopifyHmacSignature` | Verifies the HMAC signature Shopify attaches to an app-install or app-proxy request, so a Poper embedded Shopify app can confirm the request really came from Shopify. Pass the raw query string and the hmac value Shopify supplied. Returns 'Hmac not verified.' when the signature does not match. |
