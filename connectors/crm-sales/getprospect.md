---
description: "GetProspect is a B2B lead generation platform."
hidden: true
---

# GetProspect

<img src="../../.gitbook/assets/connectors/lg/getprospect.png" alt="GetProspect logo">

GetProspect is a B2B lead generation platform. This connector wraps the GetProspect REST API: v2 People and Company Search, People and Company Enrich (single and bulk), Email Finder, Email Verifier, search suggestions and filter enums, plus the workspace CRM API for contacts, companies, lists and properties. Authenticates with a workspace API key sent in the x-api-key header.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [getprospect.com](https://getprospect.com) |
| **Authentication** | API key |
| **Slug** | `getprospect` |

## Use it

Add GetProspect from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.getprospect.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Companies To Contact | `addCompaniesToContact` | Attaches one or more saved companies to a contact, with optional work email, email status and position. Returns 201 with an empty body. |
| Add Contacts To List | `addContactsToList` | Adds saved contacts to a contact list by contact id. Returns 201 with an empty body. |
| Bulk Enrich Companies | `bulkEnrichCompanies` | Enriches up to 50 companies in one request and returns matched, not matched and invalid items keyed by your identifier. |
| Bulk Enrich People | `bulkEnrichPeople` | Enriches up to 50 people in one request and returns matched, not matched and invalid items keyed by your identifier. Spends email and phone credits per matched item when enabled. |
| Check API Health | `checkApiHealth` | Calls the GetProspect API health-check endpoint and returns its greeting message. Useful to confirm the API is reachable and the workspace API key is accepted. Consumes no credits. |
| Check People Exist | `checkPeopleExist` | Checks which of up to 50 LinkedIn profile URLs exist in the GetProspect people index and returns matched person summaries. Free - no credits are spent. |
| Create Company | `createCompany` | Creates a new company in the GetProspect CRM from property name/value pairs. The domain property is required and must be unique. |
| Create Contact | `createContact` | Creates a new contact in the GetProspect CRM from property name/value pairs, optionally adding it to lists. firstName and lastName are required properties. |
| Create Contact List | `createContactList` | Creates a new contact list in the GetProspect CRM with the given name. |
| Delete Company | `deleteCompany` | Deletes a saved CRM company by its id. Returns 204 No Content. |
| Delete Contact | `deleteContact` | Deletes a saved contact by its id. Returns 204 No Content. |
| Delete Contact Lists | `deleteContactLists` | Deletes one or more contact lists by id. Returns 204 No Content. Warning: an empty listIds array permanently removes all lists already marked deleted. |
| Enrich Company | `enrichCompany` | Retrieves the full profile of one company by GetProspect id, LinkedIn id or URL, domain, or name. Returns success false with a NOT_FOUND error when no company matches. |
| Enrich Person | `enrichPerson` | Retrieves the full profile of one person by GetProspect id, LinkedIn id or URL, email, or name plus company. Reveals a business email by default (1 email credit per newly revealed email); enrich_phone costs 1 phone credit. Returns success false with NOT_FOUND when no one matches. |
| Fast Search Database | `fastSearchDatabase` | Runs a quick name search across the GetProspect contacts and companies database and returns the top matches of each. |
| Find Email | `findEmail` | Finds the verified business email address of a person from their name and company domain or name. Costs 1 email credit only when a valid email is found. |
| Find Email By Name (Legacy) | `findEmailLegacy` | Finds a contact's business email from their full name and company name or domain using the v1 public API. Costs 1 email credit when found. |
| Find Lead By LinkedIn URL (Legacy) | `findLeadByLinkedinUrlLegacy` | Finds a lead's data in the GetProspect database by LinkedIn profile URL using the v1 public API. |
| Get All Properties | `getAllProperties` | Retrieves every contact and company property defined in the GetProspect workspace, including required flags, field types and select options. |
| Get Company | `getCompany` | Retrieves all properties of a saved CRM company by its id. |
| Get Contact | `getContact` | Retrieves all properties, list relations and company relations of a saved contact by its id. |
| Get Contact List Sizes | `getContactListSizes` | Retrieves the number of contacts in each of the given contact lists. |
| Get Filter Enum | `getFilterEnum` | Fetches the allowed values of a single search filter enum by name, for example industries or seniorities. |
| Get People Export Column View | `getPeopleExportColumnView` | Retrieves the saved People Export column view for the API key's user: the columns exported to CSV, in order, or the default view when none is saved. |
| Get People Search Table View | `getPeopleSearchTableView` | Retrieves the saved People Search table view for the API key's user: the visible columns in display order, their widths and frozen state, and whether the default view is in use. |
| Get Purchase Status | `getPurchaseStatus` | Returns the current Stripe purchase status of the workspace, indicating the next billing step (for example create_subscription_session when no subscription checkout is in progress). Read-only; it does not create or modify any subscription. |
| Get Search Suggestions | `getSearchSuggestions` | Returns autocomplete suggestions for search filter values: locations, job titles, industries, company keywords, people or companies. |
| List Contact Lists | `listContactLists` | Retrieves all contact lists in the GetProspect workspace, with paging and sorting. sort and order must be provided together. |
| List Contacts In List | `listContactsInList` | Retrieves the contacts that belong to a contact list, with paging and sorting. |
| List Filter Enums | `listFilterEnums` | Lists every allowed value for the enum-backed search filters: industries, countries, employee ranges, company types, business types, revenue streams, keyword sources, departments, seniorities and regions. |
| Lookup Email (Legacy) | `lookupEmailLegacy` | Looks up the lead profile associated with an email address using the v1 public API: name, company and position, LinkedIn ids, location and summary. |
| Preview Matching Job Titles | `previewMatchingJobTitles` | Previews the most common job titles matched by a boolean job title query, with the number of people holding each title. |
| Rename Contact List | `renameContactList` | Updates the name of an existing contact list. |
| Reset People Export Column View | `resetPeopleExportColumnView` | Resets the People Export column view for the API key's user back to the default columns. |
| Reset People Search Table View | `resetPeopleSearchTableView` | Resets the People Search table view for the API key's user back to the default columns. |
| Save People Export Column View | `savePeopleExportColumnView` | Saves the People Export column view for the API key's user: the columns exported to CSV, in order. The name and linkedin_url columns are always exported and must be included. |
| Save People Search Table View | `savePeopleSearchTableView` | Saves the People Search table view for the API key's user: the visible columns in display order, with optional width and frozen state. The name and email columns cannot be hidden and must be included. |
| Search Companies | `searchCompanies` | Searches the GetProspect company index with structured filters, 25 results per page. At least one include filter is required. Free - no credits are spent. |
| Search Companies (Legacy) | `searchCompaniesLegacy` | Searches the GetProspect companies database by name, domain, industry, location, keywords and size using the v1 public API, with paging and sorting. |
| Search Contacts | `searchContacts` | Retrieves saved CRM contacts matching property filters, with paging and sorting. |
| Search Leads (Legacy) | `searchLeadsLegacy` | Searches the GetProspect B2B leads database by contact name, company, job title, seniority, domain, industry, location and keywords using the v1 public API, with paging and sorting. |
| Search People | `searchPeople` | Searches the GetProspect people index with structured person and company filters, 25 results per page. At least one include filter is required. Searching is free; enrich_email and enrich_phone spend credits for revealed data. |
| Search Saved Companies By Name | `searchSavedCompaniesByName` | Finds saved CRM companies whose name matches the given text. |
| Update Company | `updateCompany` | Updates one or more properties of a saved CRM company. Properties not sent are left unchanged. |
| Update Contact | `updateContact` | Updates one or more properties of a saved contact, and optionally replaces its list relations. Properties not sent are left unchanged. |
| Verify Email | `verifyEmail` | Verifies whether an email address is deliverable and returns its status, domain health and whether the mailbox is free or disposable. Costs 1 verification credit per check. |
| Verify Email (Legacy) | `verifyEmailLegacy` | Verifies the deliverability of an email address using the v1 public API. Costs 1 verification credit. |
