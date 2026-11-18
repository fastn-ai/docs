---
description: "MagicalAPI provides LinkedIn profile and company scraping plus resume parsing, review and job-match scoring for recruiting and sales prospecting."
hidden: true
---

# MagicalAPI

<img src="../../.gitbook/assets/connectors/lg/magicalapi.png" alt="MagicalAPI logo">

MagicalAPI provides LinkedIn profile and company scraping plus resume parsing, review and job-match scoring for recruiting and sales prospecting. This connector wraps the MagicalAPI gateway (https://gw.magicalapi.com): each service takes a request, returns a request_id, and returns the finished result when the same endpoint is called again with that request_id, or pushes it to a webhook URL.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [magicalapi.com](https://magicalapi.com) |
| **Authentication** | API key |
| **Slug** | `magicalapi` |

## Use it

Add MagicalAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.magicalapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get LinkedIn Company Data | `getCompanyData` | Retrieves the scraped LinkedIn company profile for a request ID returned by Request LinkedIn Company Data. |
| Get LinkedIn Profile Data | `getProfileData` | Retrieves the scraped LinkedIn profile for a request ID returned by Request LinkedIn Profile Data. While the job is still running the service answers with a pending status. |
| Get Resume Parse Result | `getResumeParser` | Retrieves the structured resume data for a request ID returned by Request Resume Parse. |
| Get Resume Review Result | `getResumeReview` | Retrieves the resume review feedback for a request ID returned by Request Resume Review. |
| Get Resume Score Result | `getResumeScore` | Retrieves the resume-to-job match score for a request ID returned by Request Resume Score. |
| Request LinkedIn Company Data | `requestCompanyData` | Submits a company for LinkedIn scraping and returns a request ID. Supply at least one of company name, LinkedIn company username or company website. |
| Request LinkedIn Profile Data | `requestProfileData` | Submits a LinkedIn profile for scraping and returns a request ID. Retrieve the finished profile with Get LinkedIn Profile Data, or pass a webhook URL to have the result pushed to your endpoint. |
| Request Resume Parse | `requestResumeParser` | Submits a resume document for parsing into structured data and returns a request ID. The file must be a publicly reachable PDF, DOC or DOCX of at most 10MB. |
| Request Resume Review | `requestResumeReview` | Submits a resume document for automated review and returns a request ID. The file must be a publicly reachable PDF, DOC or DOCX of at most 10MB. |
| Request Resume Score | `requestResumeScore` | Submits a resume document together with a job description to be scored for fit, and returns a request ID. The job description must be between 100 and 10,000 characters. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Result Completed | `result_completed` | MagicalAPI finished processing a request and pushed the result. There is no webhook registration API: the customer passes webhook_url on the request action (Request LinkedIn Profile Data, Request LinkedIn Company Data, Request Resume Parse, Request Resume Review, Request Resume Score) and whitelists the receiving domain in the MagicalAPI dashboard under Webhook settings (docs.magicalapi.com/docs/webhook). Point that webhook_url at the fastn trigger URL. The delivery is a POST with {status, data, usage}; the payload carries no service discriminator, so a separate trigger per service, or a marker the customer adds to the URL path, is needed to tell the services apart. docs.magicalapi.com/docs/webhook/get-samples-as-webhook can send a sample payload of a chosen service to the endpoint for testing. |
