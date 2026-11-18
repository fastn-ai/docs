---
description: "OpenRegister provides programmatic access to official German company data from the Handelsregister, Bundesanzeiger, Transparenzregister and Insolvenzregister."
hidden: true
---

# OpenRegister

<img src="../../.gitbook/assets/connectors/lg/openregister.png" alt="OpenRegister logo">

OpenRegister provides programmatic access to official German company data from the Handelsregister, Bundesanzeiger, Transparenzregister and Insolvenzregister. This connector covers company search and lookup, ownership and beneficial owners, holdings, financial statements, contact and web data, official register documents, person search and holdings, insolvency proceedings, Transparenzregister extracts, and register change monitors.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [openregister.de](https://openregister.de) |
| **Authentication** | Bearer token |
| **Slug** | `openregister` |

## Use it

Add OpenRegister from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openregister.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Company | `autocompleteCompany` | Performs a fast, lightweight search for German companies by name, matching both current and historical names. Optimised for search-as-you-type experiences and returns basic register details for each match. Costs 1 credit per request. |
| Create Document Job | `createDocumentJob` | Starts an asynchronous job that fetches an official register document for a company and returns the job id. Poll Get Document Job until the status is completed to receive the download URL. |
| Create Monitor | `createMonitor` | Creates a register monitor so that changes to a company or person are delivered to the webhook endpoint configured in the OpenRegister dashboard. Preferences must match the entity type. Costs 25 credits for a weekly monitor and 50 for a daily one, plus the same amount per month while it stays active. |
| Create Transparenzregister Extract | `createTransparenzregisterExtract` | Submits a Transparenzregister extract request for a company and returns an extract resource with status 'processing'. Poll Get Transparenzregister Extract with the returned id to collect the parsed report and document downloads. Set the credential name to 'sandbox' for a test-mode extract, in which case the company identifier is omitted. |
| Delete Monitor | `deleteMonitor` | Permanently removes the monitor for an entity and stops all future webhook notifications for it. The deletion cannot be undone. Free of charge. |
| Download Document | `downloadDocument` | Downloads the binary file of a stored register document. The response is the raw file with its original filename in the content-disposition header. Where a link is sufficient, Get Stored Document returns a download URL instead. |
| Get Company | `getCompany` | Returns the full register profile for a company, including register entries, name and address history, business purpose, share capital, representation, financial indicators, filed documents, corporate events, industry codes, contact data and any insolvency proceedings. Costs 10 credits, or 20 credits when realtime is enabled. |
| Get Company Contact | `getCompanyContact` | Returns contact information extracted from the company's own website, including the email address, phone number and VAT identification number, along with the page the data was found on. |
| Get Company Details | `getCompanyDetails` | Returns company information from the original v0 endpoint, where history, financials and document metadata are each switched on with a flag. For the full current profile use Get Company. |
| Get Company Financials | `getCompanyFinancials` | Returns the annual accounts a company has published in the Bundesanzeiger: the balance sheet (Aktiva and Passiva), the profit and loss statement (GuV) and a normalised set of financial indicators per reporting period. Monetary indicator values are in cents. |
| Get Company Shareholders | `getCompanyShareholders` | Returns the shareholders recorded in a company's latest shareholder list (the original v0 endpoint), with nominal and percentage shares and the document the data was taken from. For richer owner data use List Company Owners. |
| Get Credit Usage | `getCreditUsage` | Returns the API credit usage for the current billing period, including used, included, remaining and overage credits, whether the account is on a paid plan and when the period resets. Takes no inputs, so it also works as a connection check. |
| Get Document Information | `getDocumentInformation` | Returns metadata and a 15-minute download URL for a stored register document using the original v0 endpoint. Equivalent to Get Stored Document. |
| Get Document Job | `getDocumentJob` | Returns the status of an asynchronous document job and, once it has completed, the download URL of the fetched document. |
| Get Insolvency Proceeding | `getInsolvencyProceeding` | Returns a single German insolvency proceeding with its court, case number, debtor, administrator, distribution figures and the full chronological list of official court publications. |
| Get Person | `getPerson` | Returns a person recorded in the German registers, including their name, date of birth, city and the management positions they hold or have held across companies. |
| Get Realtime Document | `getRealtimeDocument` | Orders an official register document for a company directly from the Handelsregister in real time and returns a download URL for it. Use it for printouts, structured information, shareholder lists and articles of association. |
| Get Stored Document | `getStoredDocument` | Returns a document already stored by OpenRegister, identified by the document id listed on a company profile, together with a download URL that stays valid for 15 minutes. |
| Get Transparenzregister Extract | `getTransparenzregisterExtract` | Returns a Transparenzregister extract by id, including its processing state, the parsed beneficial-ownership report and download URLs for the extract documents. While the request is still running the status stays 'processing'. |
| List Company Historical Owners | `listCompanyHistoricalOwners` | Returns every owner ever recorded for a company, with the full ownership history reconstructed from each filed shareholder list, including first and last appearance and whether the owner is still active. |
| List Company Holdings | `listCompanyHoldings` | Returns the companies in which the given company holds a stake, with the relation type, nominal and percentage share and the period the holding was recorded for. |
| List Company Owners | `listCompanyOwners` | Returns the current direct owners of a company - shareholders, stockholders, general partners and limited partners - with their nominal and percentage shares and the source documents the data was taken from. |
| List Company UBOs | `listCompanyUbos` | Returns the ultimate beneficial owners of a company, resolved through the full ownership chain, with the percentage or maximum percentage each natural person or entity ultimately controls. |
| List Monitors | `listMonitors` | Lists the register monitors configured on the account, with the entity each one watches, the data categories it covers, its check frequency and whether it has been disabled by a plan change. Free of charge. |
| List Person Holdings | `listPersonHoldings` | Returns the shareholder and limited-partner positions a person holds in German companies, with the nominal and percentage share and the period each holding was recorded for. |
| Look Up Company By Website | `lookupCompanyByWebsite` | Resolves a company website URL to the registered company behind it and returns its identifier together with the contact details published on that site. |
| Search Companies | `searchCompanies` | Runs an advanced company search combining a free-text query with structured filters, an optional geographic radius and pagination. Filters cover register data, financial figures, ownership structure and insolvency status. Costs 1 credit per request. |
| Search Companies By Register Fields | `searchCompaniesByRegisterFields` | Searches companies with simple query-string filters on name, register number, register type, register court, legal form, incorporation date and active status (the original v0 search endpoint). For richer filtering use Search Companies. |
| Search Insolvency Proceedings | `searchInsolvencyProceedings` | Searches German insolvency proceedings by debtor name, case number, administrator or court, with structured filters on status, proceeding kind, court, city and the relevant dates. |
| Search People | `searchPeople` | Searches for people recorded in the German registers by name, optionally narrowed by date of birth, city or active status, with pagination. |
| Store Transparenzregister Credentials | `storeTransparenzregisterCredentials` | Stores a Transparenzregister portal username and password under a name so that extract requests can be made with them. Credentials are validated against the Transparenzregister before being saved. The name 'sandbox' is reserved for test-mode extracts and cannot be used. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Monitored Entity Updated | `monitor.update` | Fires when OpenRegister detects a change to a company or person you monitor, in one of the data categories chosen on the monitor (for companies: basic, representation, financials, documents, ownership, holdings, insolvencies; for people: management_positions, holdings, insolvencies). Setup is manual and account-wide: 1) sign in at https://openregister.de, open the API Keys page (https://openregister.de/keys) and add a webhook endpoint, pasting the fastn webhook URL for this trigger; 2) then create a monitor for each company or person with the Create Monitor action. Until an endpoint is configured, Create Monitor is rejected with 'no webhook endpoint configured'. Deliveries are sent through Svix and signed with svix-id, svix-timestamp and svix-signature headers; that signing scheme cannot be verified by the platform today, so signature checking must be done downstream with the endpoint's whsec_ secret. OpenRegister does not publish the notification body and no live delivery has been captured, so the schema below is a recommended minimum modelled from the monitor resource, not a vendor contract. |
