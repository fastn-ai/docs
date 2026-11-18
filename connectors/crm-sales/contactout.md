---
description: "ContactOut is a contact-data and recruitment-outreach platform that finds verified email addresses and phone numbers for professionals."
hidden: true
---

# ContactOut

<img src="../../.gitbook/assets/connectors/contactout.png" alt="ContactOut logo" width="64">

ContactOut is a contact-data and recruitment-outreach platform that finds verified email addresses and phone numbers for professionals. This connector covers the full ContactOut public API: LinkedIn and email profile enrichment, people and company search, decision-maker discovery, bulk contact-info jobs, contact availability checks, hashed-email identifiers, single and bulk email verification, outreach campaign management and API usage statistics.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [contactout.com](https://contactout.com) |
| **Authentication** | API key |
| **Slug** | `contactout` |

## Use it

Add ContactOut from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.contactout.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Campaign Recipients | `addCampaignRecipients` | Adds between 1 and 100 recipients to an outreach campaign. Each recipient must carry at least one contact identifier, an email address or a phone number, and may also carry a first name, last name and company. Recipients become eligible to receive campaign messages once the campaign is started. |
| Check Personal Email Availability | `checkPersonalEmailAvailability` | Reports whether ContactOut holds a personal email address for a LinkedIn member profile, without revealing it or consuming email credits. |
| Check Phone Availability | `checkPhoneAvailability` | Reports whether ContactOut holds a phone number for a LinkedIn member profile, without revealing it or consuming phone credits. |
| Check Work Email Availability | `checkWorkEmailAvailability` | Reports whether ContactOut holds a work email address for a LinkedIn member profile and how well it is verified, without revealing it or consuming email credits. |
| Count People | `countPeople` | Returns how many profiles match a set of people-search criteria, together with estimates of how many have a personal email, work email or phone number. Consumes no credits and is available to paid plans only. |
| Create Bulk Contact Info Job | `createBulkContactInfoJob` | Queues an asynchronous contact-info lookup for up to 1000 LinkedIn member profiles and returns a job identifier. Results are retrieved with Get Bulk Contact Info Job or delivered to the supplied callback URL. |
| Create Bulk Email Verification Job | `createBulkEmailVerificationJob` | Queues deliverability verification for up to 100 email addresses and returns a job identifier. Results are retrieved with Get Bulk Email Verification Job or delivered to the supplied callback URL. |
| Enrich Companies By Domain | `enrichCompaniesByDomain` | Returns company firmographics for up to 30 website domains, including size, industry, revenue, headquarters, technologies and LinkedIn page. |
| Enrich Person | `enrichPerson` | Finds and enriches a person from any combination of identifying details such as name, email address, phone number, LinkedIn URL, employer, education or location. Supply as many identifiers as you have to improve the match rate. |
| Enrich Profile By Email | `enrichProfileByEmail` | Returns the ContactOut profile that matches a single email address. Match rates are highest for personal email addresses; for work addresses belonging to a former employer ContactOut also checks previous employment history. |

<details>

<summary>See 17 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Enrich Profile By LinkedIn URL | `enrichProfileByLinkedInUrl` | Returns the full ContactOut profile for a LinkedIn member URL, including work and personal email addresses, phone numbers, employment history, education, skills and company details. Set Profile Only to true to retrieve profile data without contact information at a lower credit cost. |
| Find LinkedIn Profile By Email | `findLinkedInProfileByEmail` | Returns the LinkedIn member profile URL associated with an email address. |
| Get API Usage Stats | `getApiUsageStats` | Returns ContactOut API usage and remaining quota for a billing month, covering email, phone and search credits. |
| Get Bulk Contact Info | `getBulkContactInfo` | Returns contact details for up to 100 LinkedIn member profiles in a single synchronous request. Use Create Bulk Contact Info Job for larger batches. |
| Get Bulk Contact Info Job | `getBulkContactInfoJob` | Returns the status and, once complete, the results of an asynchronous bulk contact-info job created with Create Bulk Contact Info Job. |
| Get Bulk Email Verification Job | `getBulkEmailVerificationJob` | Returns the status and, once complete, the per-address verdicts of a bulk email verification job created with Create Bulk Email Verification Job. |
| Get Campaign | `getCampaign` | Returns a single outreach campaign by its identifier, optionally including performance statistics such as sends, opens, clicks and replies. |
| Get Contact Info By LinkedIn URL | `getContactInfoByLinkedInUrl` | Returns only the contact details held for a LinkedIn member profile: email addresses, work and personal email verification status and, optionally, phone numbers. Use Enrich Profile By LinkedIn URL when you also need biographical data. |
| Get Hashed Email Identifiers | `getHashedEmailIdentifiers` | Returns privacy-preserving hashed email identifiers for a batch of LinkedIn member profiles, for use in advertising audience matching. At least five unique profiles are required. |
| List Campaigns | `listCampaigns` | Returns a paginated list of the outreach campaigns in the connected ContactOut account, with each campaign's identifier, name and status. |
| List Decision Makers | `listDecisionMakers` | Returns the key decision makers at a company, identified by its LinkedIn company URL, website domain or name. Set Reveal Info to true to include email addresses and phone numbers, which consumes credits. |
| Remove Campaign Recipients | `removeCampaignRecipients` | Removes up to 100 recipients from an outreach campaign. Each recipient object must contain the email address identifying the recipient to remove. |
| Search Companies | `searchCompanies` | Searches the ContactOut company database by LinkedIn page, name, domain, employee count, location, industry, technology stack, revenue and founding year. |
| Search People | `searchPeople` | Searches the ContactOut people database by job title, seniority, function, company, industry, location, skills, education, experience and more, returning up to 25 matching profiles per page. Set Reveal Contact Info to true to include email addresses and phone numbers, which consumes credits. |
| Start Campaign | `startCampaign` | Starts an outreach campaign so that its scheduled messages begin sending to its recipients. |
| Stop Campaign | `stopCampaign` | Stops a running outreach campaign so that no further messages are sent to its recipients. |
| Verify Email | `verifyEmail` | Verifies the deliverability of a single email address and returns its status, such as valid, invalid or accept_all. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Bulk Contact Info Job Completed | `bulk_contact_info_job_completed` | Fires when an asynchronous bulk contact-info job finishes and ContactOut posts its results. ContactOut has no webhook registration API: you register this trigger per job. Setup: copy this trigger's URL, then run the Create Bulk Contact Info Job action (POST /v2/people/linkedin/batch) with that URL in its Callback URL input. ContactOut posts the finished results to it once the job completes. Because the callback URL is supplied per job, each trigger receives only the jobs it was passed to. ContactOut sends no event-type field and no signature on this delivery. Payload schema modelled from ContactOut's documented webhook payload, not from a captured delivery. |
| Bulk Email Verification Job Completed | `bulk_email_verification_job_completed` | Fires when an asynchronous bulk email verification job finishes and ContactOut posts its results. ContactOut has no webhook registration API: you register this trigger per job. Setup: copy this trigger's URL, then run the Create Bulk Email Verification Job action (POST /v1/email/verify/batch) with that URL in its Callback URL input. Because the callback URL is supplied per job, each trigger receives only the jobs it was passed to. ContactOut sends no event-type field and no signature on this delivery. ContactOut does not publish the callback body for this job type; the schema below is modelled from the body its Get Bulk Email Verification Job endpoint returns and should be treated as indicative rather than a vendor contract. |
