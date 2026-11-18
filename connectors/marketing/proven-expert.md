---
description: "ProvenExpert review-collection platform."
hidden: true
---

# ProvenExpert

<img src="../../.gitbook/assets/connectors/lg/proven-expert.png" alt="ProvenExpert logo">

ProvenExpert review-collection platform. Manage ProvenExpert profiles and profile settings, create and manage surveys, generate personalised survey invitation links, send survey invitation e-mails and check their delivery status, read ratings and rating summaries, and generate rating-seal / widget HTML. All calls are POST to https://www.provenexpert.com/api/v1 and authenticate with HTTP Basic using the account's API-ID and API-Key.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [provenexpert.com](https://provenexpert.com) |
| **Authentication** | Basic auth |
| **Slug** | `provenExpert` |

## Use it

Add ProvenExpert from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.provenExpert.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Profile | `createProfile` | Creates a new ProvenExpert profile below the authenticated Enterprise account. Supply company for a company profile, or firstname and lastname for a person profile - never both. Returns the new profile together with a Single Sign-On login link. Requires an ENTERPRISE plan. |
| Create Rating Seal Widget | `createRatingSealWidget` | Generates the embeddable HTML for a ProvenExpert rating seal, quality seal, logo, browser-edge bar, landing widget or award widget, sized and positioned as requested. Which option fields apply depends on the chosen type. Available on every ProvenExpert plan. |
| Create Survey | `createSurvey` | Creates a new ProvenExpert survey and returns its code, public survey URL, QR-code image and printable business-card templates. Set pos to 1 for a Point of Sale survey; that mode must first be enabled on the account by ProvenExpert support. Requires an ENTERPRISE plan. |
| Create Survey Invitation Link | `createSurveyInvitationLink` | Creates a personalised invitation link for one reviewer to a given survey and returns its URL, plus a flag saying whether that e-mail address had already been invited. The link is only generated - nothing is sent to the reviewer. Requires a PLUS plan or higher. |
| Delete Profile | `deleteProfile` | Permanently deletes a managed sub-profile together with all of its reviews and surveys. proxyUser is mandatory in practice: ProvenExpert refuses to delete the account you authenticate as, refuses Enterprise profiles that still have children, and only deletes profiles that were created through the API. This cannot be undone. Requires an ENTERPRISE plan. |
| Get API Credentials | `getApiCredentials` | Returns the ProvenExpert API-ID and API-Key of the profile, or of a managed sub-profile when proxyUser is supplied, so an Enterprise integrator can obtain per-profile credentials. SECURITY: the response contains a live API key in plain text - do not log, cache or display the result. ENTERPRISE plan only. |
| Get Invitation Mailing Status | `getInvitationMailingStatus` | Reports the delivery status of an invitation mailing created by Send Survey Invitation Emails, giving the number of messages sent, still pending and failed, and the list of addresses per status. Requires a PLUS plan or higher. |
| Get Profile | `getProfile` | Returns the full ProvenExpert profile of the authenticated account: company or person name, description, public flag, contact details, websites, social links, opening hours, imprint and external data. |
| Get Profile Settings | `getProfileSettings` | Returns the current profile settings of the authenticated ProvenExpert account: whether the profile is public, all privacy switches, notification preferences and the newsletter and reporting e-mail settings. |
| Get Rating Summary | `getRatingSummary` | Returns the overall rating value, the number of reviews and the recommendation rate of the authenticated ProvenExpert profile. Available on every ProvenExpert plan. Pass proxyUser to read the summary of a managed sub-profile instead. |

<details>

<summary>See 14 more actions</summary>

* **Get Rating Summary Rich Snippet** `getRatingSummaryRichSnippet`: Returns the overall rating value, the review count and ready-to-embed schema.org rich-snippet HTML for the authenticated ProvenExpert profile. Paste the returned html into a web page so search engines can show the star rating.
* **Get Single Sign-On URL** `getSingleSignOnUrl`: Generates a one-time Single Sign-On URL that logs straight into the ProvenExpert profile without an e-mail address or password. The link is valid for 10 minutes by default. SECURITY: the returned url grants full account access to anyone holding it - never log it, store it or forward it. ENTERPRISE plan only.
* **List Child Profile API Credentials** `listChildProfileApiCredentials`: Returns the API-ID and API-Key of every sub-profile one level below the authenticated Enterprise account, keyed by the child profile's e-mail address. SECURITY: the response contains live API keys in plain text - do not log, cache or display the result. ENTERPRISE plan only.
* **List Child Profile Rating Summaries** `listChildProfileRatingSummaries`: Returns the overall rating value and review count for every sub-profile one level below the authenticated Enterprise account, keyed by the child profile's e-mail address. ENTERPRISE plan only.
* **List Child Profile Ratings** `listChildProfileRatings`: Retrieves the reviews of every sub-profile one level below the authenticated Enterprise account. Takes the same filters as List Ratings and additionally returns user.profileEmail so each review can be attributed to its child profile. ENTERPRISE plan only.
* **List Child Profile Surveys** `listChildProfileSurveys`: Returns the surveys of every sub-profile one level below the authenticated Enterprise account. This route is live but absent from the published ProvenExpert API reference. ENTERPRISE plan only; other plans receive the error body "Not an enterprise account.".
* **List Child Profiles** `listChildProfiles`: Returns the sub-profiles one level below the authenticated Enterprise account, with each child profile's core data. ENTERPRISE plan only; other plans receive a permission-denied error body.
* **List Ratings** `listRatings`: Retrieves the individual reviews of a single ProvenExpert profile, newest first, with per-category scores, per-question detail and the reviewer's feedback text. Filter by publication status, rating value range or creation date. Requires a PREMIUM plan or higher.
* **List Survey Invitation Links** `listSurveyInvitationLinks`: Returns every personalised invitation link already created for one survey, keyed by the reviewer's e-mail address, together with when it was created, whether it has been opened and whether a review has been submitted through it. Requires a PLUS plan or higher.
* **List Surveys** `listSurveys`: Returns every survey of the authenticated ProvenExpert profile, keyed by survey code, with its name, active flag, public survey URL, QR-code image link and printable business-card templates. Requires a PLUS plan or higher.
* **Send Survey Invitation Emails** `sendSurveyInvitationEmails`: Creates personalised survey invitations for up to 100 recipients and sends them by e-mail from the profile's address, with an optional reminder after 7 days. Subject, salutation and body may be set per recipient and must be plain text. Returns a mailing id for Get Invitation Mailing Status. CAUTION: this sends real e-mail to real people a few minutes after the call, and only recipients who consented may be contacted. Requires a PLUS plan or higher.
* **Update Profile** `updateProfile`: Edits an existing ProvenExpert profile. Only the supplied fields change; sending an empty string clears a field. Numerically indexed lists such as websites, social and externalRatings are replaced as a whole, while contact and openingHours can be edited field by field. Returns the updated profile. Requires an ENTERPRISE plan.
* **Update Profile Settings** `updateProfileSettings`: Changes the profile settings of a ProvenExpert account: whether the profile is public, the privacy switches that control what visitors see, which events trigger a notification, and the newsletter and reporting e-mail preferences. Only the supplied values change; all current settings are returned. Requires an ENTERPRISE plan.
* **Update Survey** `updateSurvey`: Activates or deactivates an existing ProvenExpert survey and updates its Point of Sale label and logo. The survey is selected by its code; only the supplied fields change. Requires an ENTERPRISE plan.

</details>
