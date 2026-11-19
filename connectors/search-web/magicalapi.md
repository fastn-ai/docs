---
description: "MagicalAPI pulls LinkedIn profile and company data and parses resumes. Request profile and company data and parse, review or score resumes."
hidden: true
---

# MagicalAPI

<img src="../../.gitbook/assets/connectors/lg/magicalapi.png" alt="MagicalAPI logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [magicalapi.com](https://magicalapi.com) |
| **Authentication** | API key |
| **Slug** | `magicalapi` |

## Setup

Your customers enter their API key for MagicalAPI when they connect. Nothing else needs setting up.

## Use it

Add MagicalAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.magicalapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get LinkedIn Company Data</td><td><code>getCompanyData</code></td><td>Retrieves the scraped LinkedIn company profile for a request ID returned by Request LinkedIn Company Data.</td></tr><tr><td>Get LinkedIn Profile Data</td><td><code>getProfileData</code></td><td>Retrieves the scraped LinkedIn profile for a request ID returned by Request LinkedIn Profile Data. While the job is still running the service answers with a pending status.</td></tr><tr><td>Get Resume Parse Result</td><td><code>getResumeParser</code></td><td>Retrieves the structured resume data for a request ID returned by Request Resume Parse.</td></tr><tr><td>Get Resume Review Result</td><td><code>getResumeReview</code></td><td>Retrieves the resume review feedback for a request ID returned by Request Resume Review.</td></tr><tr><td>Get Resume Score Result</td><td><code>getResumeScore</code></td><td>Retrieves the resume-to-job match score for a request ID returned by Request Resume Score.</td></tr><tr><td>Request LinkedIn Company Data</td><td><code>requestCompanyData</code></td><td>Submits a company for LinkedIn scraping and returns a request ID. Supply at least one of company name, LinkedIn company username or company website.</td></tr><tr><td>Request LinkedIn Profile Data</td><td><code>requestProfileData</code></td><td>Submits a LinkedIn profile for scraping and returns a request ID. Retrieve the finished profile with Get LinkedIn Profile Data, or pass a webhook URL to have the result pushed to your endpoint.</td></tr><tr><td>Request Resume Parse</td><td><code>requestResumeParser</code></td><td>Submits a resume document for parsing into structured data and returns a request ID. The file must be a publicly reachable PDF, DOC or DOCX of at most 10MB.</td></tr><tr><td>Request Resume Review</td><td><code>requestResumeReview</code></td><td>Submits a resume document for automated review and returns a request ID. The file must be a publicly reachable PDF, DOC or DOCX of at most 10MB.</td></tr><tr><td>Request Resume Score</td><td><code>requestResumeScore</code></td><td>Submits a resume document together with a job description to be scored for fit, and returns a request ID. The job description must be between 100 and 10,000 characters.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Result Completed</td><td><code>result_completed</code></td><td>MagicalAPI finished processing a request and pushed the result. There is no webhook registration API: the customer passes webhook_url on the request action (Request LinkedIn Profile Data, Request LinkedIn Company Data, Request Resume Parse, Request Resume Review, Request Resume Score) and whitelists the receiving domain in the MagicalAPI dashboard under Webhook settings (docs.magicalapi.com/docs/webhook). Point that webhook_url at the fastn trigger URL. The delivery is a POST with {status, data, usage}; the payload carries no service discriminator, so a separate trigger per service, or a marker the customer adds to the URL path, is needed to tell the services apart.</td></tr></tbody></table>
