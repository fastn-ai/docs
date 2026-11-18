---
description: "Enrich Layer is a B2B data enrichment API with structured data on people, companies, jobs and schools."
hidden: true
---

# Enrich Layer

<img src="../../.gitbook/assets/connectors/lg/enrich-layer.png" alt="Enrich Layer logo">

Enrich Layer is a B2B data enrichment API with structured data on people, companies, jobs and schools. This connector covers the full v2 REST surface (person, company, school and job profiles; person, company and role lookups; employee, student, follower and customer listings and counts; person and company search; work, personal and reverse email and phone lookups; disposable email checks; profile pictures and credit balance), plus the v3 person enrichment, company logo and company autocomplete endpoints.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [enrichlayer.com](https://enrichlayer.com) |
| **Authentication** | Bearer token |
| **Slug** | `enrichLayer` |

## Use it

Add Enrich Layer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.enrichLayer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Company Search (v3) | `autocompleteCompanySearch` | Searches companies by name or partial name (v3 Autocomplete API, beta) and returns up to 10 matches sorted by employee count, each with domain, industry, employee count, logo URL, location and LinkedIn URL. |
| Check Disposable Email | `checkDisposableEmail` | Checks whether an email address belongs to a disposable or free email provider. Costs 0 credits. |
| Count Company Customers | `countCompanyCustomers` | Returns the number of probable corporate customers of a target company. Requires an annual subscription or Enterprise plan; costs 1 credit per successful request. |
| Count Company Employees | `countCompanyEmployees` | Returns the number of employees of a company as counted from LinkedIn profiles, optionally at a historical date and alongside the company's self-reported headcount. Costs 1 credit per successful request. |
| Count Company Followers | `countCompanyFollowers` | Returns the number of individual LinkedIn members following a target company. Requires an annual subscription or Enterprise plan; costs 1 credit per successful request. |
| Count Jobs | `countJobs` | Returns the number of LinkedIn job postings matching the same filters as Search Jobs, without returning the postings themselves. Costs 2 credits per successful request. |
| Get Company Logo (v3) | `getCompanyLogoV3` | Searches companies by name or domain on the v3 Logo API and returns matches with their logo URLs. |
| Get Company Profile | `getCompanyProfile` | Returns the structured profile of a company from its LinkedIn company URL: name, description, website, industry, company size, HQ location, specialities, locations, similar companies, affiliated companies and updates. Costs 1 credit per successful request; each optional enrichment flag adds credits. |
| Get Company Profile Picture | `getCompanyProfilePicture` | Returns a temporary link to a company's profile picture (logo), taken from the cached company profile. Costs 0 credits. |
| Get Credit Balance | `getCreditBalance` | Returns the current credit balance of the Enrich Layer account. Costs 0 credits. |

<details>

<summary>See 22 more actions</summary>

* **Get Job Profile** `getJobProfile`: Returns the structured details of a single LinkedIn job posting: title, location, company, seniority, employment type, industry and full description. Costs 2 credits per successful request.
* **Get Person Profile** `getPersonProfile`: Returns the structured profile of a person from a LinkedIn, Twitter/X or Facebook profile URL: name, headline, summary, location, experiences, education, certifications, languages and more. Costs 1 credit per successful request; each optional enrichment flag adds credits.
* **Get Person Profile (v3)** `getPersonProfileV3`: Enrich Layer v3 person enrichment on api.enrichlayer.com. Resolves a person from any one of email, LinkedIn, Facebook, Twitter/X or GitHub identifiers and returns a unified profile, with opt-in sections for contact information, career insight and developer profile.
* **Get Person Profile Picture** `getPersonProfilePicture`: Returns a temporary link to the profile picture of a person, taken from the cached profile. Costs 0 credits.
* **Get School Profile** `getSchoolProfile`: Returns the structured profile of a school or university from its LinkedIn school URL: name, description, website, industry, size, HQ location, specialities and similar schools. Costs 1 credit per successful request.
* **List Company Customers** `listCompanyCustomers`: Lists the companies that are probable corporate customers of a target company. Requires an annual subscription or Enterprise plan; costs 10 credits per company profile URL.
* **List Company Employees** `listCompanyEmployees`: Lists the employees of a company, optionally filtered by country, role and employment status, with cursor pagination. Costs 3 credits per employee returned; several parameters add further credits.
* **List Company Followers** `listCompanyFollowers`: Lists the individual LinkedIn members who follow a target company. Requires an annual subscription or Enterprise plan; costs 10 credits per company profile URL.
* **List School Students** `listSchoolStudents`: Lists students and alumni of a school, optionally filtered by country, major and student status, with cursor pagination. Costs 3 credits per student returned; several parameters add further credits.
* **Look Up Company** `lookUpCompany`: Resolves a company's LinkedIn profile URL from its name, domain and location. Costs 2 credits on any 200 response, including when no matching company is found and url is null.
* **Look Up Company By ID** `lookUpCompanyById`: Resolves a company's public LinkedIn vanity URL from its immutable numeric LinkedIn ID. Free - costs 0 credits.
* **Look Up Person** `lookUpPerson`: Resolves a person's LinkedIn profile URL from their name plus company information. Costs 2 credits per successful request; credits are charged even when no match is found unless similarity_checks is set to skip.
* **Look Up Person By Role** `lookUpPersonByRole`: Returns the single person who most closely matches a role at a company, e.g. the CTO of Apple. Costs 3 credits on any 200 response, including when no matching profile is found.
* **Look Up Personal Contact Number** `lookUpPersonalContactNumber`: Finds personal phone numbers associated with a LinkedIn, Twitter/X or Facebook profile. Costs 1 credit per number returned.
* **Look Up Personal Email** `lookUpPersonalEmail`: Finds personal email addresses associated with a LinkedIn, Twitter/X or Facebook profile, optionally validating deliverability. Costs 1 credit per email returned.
* **Look Up Work Email** `lookUpWorkEmail`: Queues a verified work-email lookup for a LinkedIn profile. The API answers HTTP 202 with a queue acknowledgement - the resolved address is delivered asynchronously, either to the callback_url webhook supplied on the request or to the Work Email Lookup Logs page in the Enrich Layer dashboard. This callback is the only push/event surface Enrich Layer exposes. Costs 3 credits per successful request.
* **Reverse Email Lookup** `reverseEmailLookup`: Resolves a person's social profiles from an email address, personal or work. Costs 3 credits per successful request; a deep lookup is charged even when no match is found, a superficial lookup is not.
* **Reverse Phone Lookup** `reversePhoneLookup`: Finds the social media profiles associated with a phone number. Costs 3 credits per successful request.
* **Search Companies** `searchCompanies`: Searches the LinkedIn company index by location, name, type, industry, specialities, headcount, founding year, funding and domain, with token pagination. Costs 3 credits per company profile URL returned.
* **Search Company Employees** `searchCompanyEmployees`: Searches the employees of a target company by job title using boolean or regular-expression syntax. Syntactic sugar for the role_search parameter of List Company Employees. Costs 10 credits per successful request.
* **Search Jobs** `searchJobs`: Lists LinkedIn job postings filtered by company, keyword, location, job type, experience level, flexibility and recency, with token pagination. Costs 2 credits per successful request.
* **Search People** `searchPeople`: Searches the LinkedIn person index with 50+ filters covering location, name, education, current and past roles and companies, skills, languages, interests and company attributes such as size, industry and funding. Costs 3 credits per profile URL returned.

</details>
