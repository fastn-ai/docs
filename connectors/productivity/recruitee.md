---
description: "Recruitee (Tellent) is a collaborative recruitment and applicant tracking platform."
hidden: true
---

# Recruitee

Recruitee (Tellent) is a collaborative recruitment and applicant tracking platform. This connector provides access to candidates, job offers, departments, talent pools, pipeline templates, notes, tags, admins, roles, disqualify reasons, and other Recruitee ATS resources.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [recruitee.com](https://recruitee.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 42 |
| **Events** | 0 |
| **Slug** | `recruitee` |

## Use it

Add Recruitee from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.recruitee.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Attachment | `createAttachment` | Attaches a file, referenced by an external URL, to a candidate profile or an offer's file tab. |
| Create Candidate | `createCandidate` | Creates a new candidate in the company's talent database, with optional contact details, social links, tags, and source information. |
| Create Candidate Note | `createCandidateNote` | Adds a note to a candidate's profile. |
| Create Department | `createDepartment` | Creates a new department for grouping job offers and talent pools. |
| Create Offer | `createOffer` | Creates a new job offer (posting), starting in draft status until published. |
| Create Offer Note | `createOfferNote` | Adds a note to a job offer. |
| Create Talent Pool | `createTalentPool` | Creates a new talent pool for grouping candidates outside of a specific job offer. |
| Delete Candidate | `deleteCandidate` | Permanently deletes a candidate from the company's talent database. |
| Delete Department | `deleteDepartment` | Deletes a department. |
| Delete Note | `deleteNote` | Deletes a note from a candidate, offer, talent pool, or requisition. |
| Delete Offer | `deleteOffer` | Permanently deletes a job offer (posting). |
| Delete Talent Pool | `deleteTalentPool` | Deletes a talent pool. |
| Get Candidate | `getCandidate` | Retrieves a single candidate by ID, including contact details, tags, custom fields, and job placements. |
| Get Offer | `getOffer` | Retrieves a single job offer by ID or slug, including its pipeline, department, and status. |
| Get Talent Pool | `getTalentPool` | Retrieves a single talent pool by ID or slug. |
| List Admins | `listAdmins` | Lists the admin users (recruiting team members) who have access to this company's Recruitee account. |
| List Candidate Notes | `listCandidateNotes` | Lists the notes recorded on a candidate's profile. |
| List Candidate Sources | `listCandidateSources` | Lists the sourcing channels recorded on candidates in this company (e.g. job boards, referrals, manual entry). |
| List Candidate Tags | `listCandidateTags` | Lists the tags currently in use on candidates in this company. Tags are assigned by including a tags array on Create Candidate or Update Candidate. |
| List Candidate Tasks | `listCandidateTasks` | Lists the tasks assigned against a candidate's profile. |
| List Candidates | `listCandidates` | Returns a collection of the company's candidates, hitting the database directly. Supports pagination and filtering by qualification, disqualification, offer, and creation date. For search-oriented lookups, prefer Search Candidates for better performance. |
| List Company Memberships | `listMemberships` | Lists the memberships that map admins (users) to this company, including their role and active status. |
| List Departments | `listDepartments` | Returns a collection of the company's departments, used for grouping job offers and talent pools. |
| List Disqualify Reasons | `listDisqualifyReasons` | Lists the company's disqualification reasons (dispositions), used when rejecting a candidate. |
| List Email Templates | `listEmailTemplates` | Lists the company's saved email templates used for candidate communication. |
| List Locations | `listLocations` | Returns a collection of the company's office locations, used for placing job offers. |
| List Offer Notes | `listOfferNotes` | Lists the notes recorded on a job offer. |
| List Offer Tags | `listOfferTags` | Lists the tags currently in use on job offers in this company. Tags are assigned by including a tags array on Create Offer or Update Offer. |
| List Offers | `listOffers` | Returns a collection of the company's job offers (postings), with optional filters by status, department, and view scope. |
| List Pipeline Templates | `listPipelineTemplates` | Lists the hiring pipeline templates available in this company. Each offer references a pipeline template, whose stages are returned embedded in Get Offer and Create Offer responses. |
| List Requisitions | `listRequisitions` | Lists the company's headcount requisitions, used for approval workflows before opening a job offer. Requires the requisitions feature to be enabled on the company's plan. |
| List Roles | `listRoles` | Lists the permission roles available in this company, including their abilities. |
| List Talent Pools | `listTalentPools` | Lists the company's talent pools, used to group candidates outside of a specific job offer. |
| List Tasks | `listTasks` | Lists the company-wide tasks assigned to admins across candidates. |
| Search Candidates | `searchCandidates` | Performs an optimized search across candidates using the account's search index, recommended over List Candidates for large datasets. Filtering is driven by filters_json, an array of filter objects serialized to a JSON string; Recruitee's own API reference does not publish the exact filter-object shape, so treat it as an opaque, vendor-defined payload (malformed JSON is rejected with a 500, confirming the parameter is real and parsed server-side). |
| Set Candidate Custom Field | `setCandidateCustomField` | Sets or updates the value of a custom profile field (e.g. a single-line text, boolean, address, or skill field) on a candidate. |
| Update Candidate | `updateCandidate` | Updates an existing candidate's contact details, tags, or other profile fields. |
| Update Candidate CV | `updateCandidateCv` | Replaces a candidate's CV using a link to a file hosted on an external website. |
| Update Department | `updateDepartment` | Renames an existing department. |
| Update Note | `updateNote` | Updates the text of an existing note on a candidate, offer, talent pool, or requisition. |
| Update Offer | `updateOffer` | Updates an existing job offer's title, description, department, requirements, or employment fields. Note: offer tags are not settable via this endpoint with this credential type (the API silently ignores a tags/offer_tags field on this resource); use List Offer Tags to read tags already applied through the Recruitee UI. |
| Update Talent Pool | `updateTalentPool` | Updates an existing talent pool's title, description, or department. |
