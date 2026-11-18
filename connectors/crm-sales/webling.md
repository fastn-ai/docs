---
description: "Webling association/club management (members, finances, documents, articles, letters, users)."
---

# Webling

Webling association/club management (members, finances, documents, articles, letters, users). REST API v1 authenticated with an apikey header.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [webling.ch](https://webling.ch) |
| **Authentication** | API key |
| **Actions** | 146 |
| **Events** | 0 |
| **Slug** | `webling` |

## Use it

Add Webling from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.webling.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Account | `createAccount` | Create an accounting account inside an accountgroup (parents = [accountgroup id]). It must also be linked to exactly one accounttemplate via links.accounttemplate. |
| Create Account Group | `createAccountGroup` | Create an accountgroup inside a period (parents = [period id]). It must also be linked to exactly one accountgrouptemplate via links.accountgrouptemplate. |
| Create Account Group Template | `createAccountGroupTemplate` | Create an accountgrouptemplate. Requires exactly one parent (a periodchain or a parent accountgrouptemplate). |
| Create Account Template | `createAccountTemplate` | Create an accounttemplate inside an accountgrouptemplate (parents). |
| Create Api Key | `createApiKey` | Create a new Webling API key. |
| Create Article | `createArticle` | Create an article. parents must be one articlegroup id. |
| Create Article Group | `createArticleGroup` | Create an articlegroup. |
| Create Comment | `createComment` | Create a comment. links.member links it to member ids. |
| Create Cost Center | `createCostCenter` | Create a costcenter. Requires exactly one parent (a period id). |
| Create Debitor | `createDebitor` | Create a debitor (invoice). parents = [PERIOD id]; links.debitorcategory names the invoice run and links.member the member billed. Write title, comment, date, duedate, address and invoiceitems only - totalamount, remainingamount, paidamount, writeoffamount, state and debitorid are computed by Webling and are not writable. |
| Create Debitor Category | `createDebitorCategory` | Create a debitorcategory (invoice run). Requires exactly one parent and it must be a PERIODGROUP id, not a period. |
| Create Document | `createDocument` | Create a document. properties.file is {name, content} with base64 content; parents is one documentgroup id. |
| Create Document Group | `createDocumentGroup` | Create a documentgroup (folder). |
| Create Entry | `createEntry` | Create an accounting entry. parents holds either an existing entrygroup id or an inline entrygroup object to create with it; links.debit and links.credit name the two accounts. |
| Create Entry Group | `createEntryGroup` | Create an entrygroup (a booking) inside a period (parents = [period id]). An entrygroup must be created with at least one entry: pass children.entry as an array of inline entry objects, each {properties:{amount}, links:{debit:[accountId], credit:[accountId]}}. |
| Create Member | `createMember` | Create a member. properties holds the configured member fields; parents must contain at least one membergroup id. Returns the new member id. |
| Create Member Group | `createMemberGroup` | Create a membergroup. properties.title is required; parents may be empty for a root group. |
| Create Object | `createObject` | Create an object of any type. type is the Webling object type (e.g. calendarevent, page, bankaccount, template, memberform, payment, participant). |
| Create Object Of Type | `createObjectOfType` | Create an object at the type-specific endpoint POST /{type}, for any Webling type including undocumented ones (calendar, calendarevent, page, template, bankaccount, memberform, payment, participant, attendee, presencelist, file, domain). |
| Create Period | `createPeriod` | Create an accounting period. parents is the periodgroup id and links.periodchain is the periodchain id it belongs to. |
| Create Period Chain | `createPeriodChain` | Create a periodchain (chart of accounts) inside a periodgroup. A periodchain MUST be created together with at least one period: pass links.period as an array holding the inline period object(s), each with parents set to the same periodgroup id. |
| Create Period Group | `createPeriodGroup` | Create a periodgroup (accounting book). Subject to the plan's periodgroup quota. |
| Create User | `createUser` | Create a Webling user account. Creating a user does NOT send mail on its own; Start User Onboarding does. |
| Create User Group | `createUserGroup` | Create a usergroup (permission group). |
| Create VAT Rate | `createVatRate` | Create a VAT rate. parents = [period id]. A rate greater than 0 MUST be linked to exactly one account via links.account. |
| Delete Account | `deleteAccount` | Delete an accounting account by id. |
| Delete Account Group | `deleteAccountGroup` | Delete an accountgroup by id. |
| Delete Account Group Template | `deleteAccountGroupTemplate` | Delete an accountgrouptemplate by id. |
| Delete Account Template | `deleteAccountTemplate` | Delete an accounttemplate by id. |
| Delete Api Key | `deleteApiKey` | Delete an API key by id. Deleting the key in use revokes this connection. |
| Delete Article | `deleteArticle` | Delete an article by id. |
| Delete Article Group | `deleteArticleGroup` | Delete an articlegroup by id. |
| Delete Comment | `deleteComment` | Delete a comment by id. |
| Delete Cost Center | `deleteCostCenter` | Delete a costcenter by id. |
| Delete Debitor | `deleteDebitor` | Delete a debitor by id. |
| Delete Debitor Category | `deleteDebitorCategory` | Delete a debitorcategory by id. |
| Delete Document | `deleteDocument` | Delete a document by id. |
| Delete Document Group | `deleteDocumentGroup` | Delete a documentgroup by id. |
| Delete Entry | `deleteEntry` | Delete an accounting entry by id. |
| Delete Entry Group | `deleteEntryGroup` | Delete an entrygroup by id. |
| Delete Letter | `deleteLetter` | Delete a letter by id. |
| Delete Letter PDF | `deleteLetterPdf` | Delete a letterpdf by id. |
| Delete Member | `deleteMember` | Delete a member by id. |
| Delete Member Group | `deleteMemberGroup` | Delete a membergroup by id. |
| Delete Object | `deleteObject` | Delete any Webling object by id regardless of its type. |
| Delete Period | `deletePeriod` | Delete an accounting period by id. |
| Delete Period Chain | `deletePeriodChain` | Delete a periodchain by id. |
| Delete Period Group | `deletePeriodGroup` | Delete a periodgroup by id. |
| Delete User | `deleteUser` | Delete a Webling user account by id. |
| Delete User Group | `deleteUserGroup` | Delete a usergroup by id. |
| Delete VAT Rate | `deleteVatRate` | Delete a VAT rate by id. |
| Download Document File | `downloadDocumentFile` | Download the binary file attached to a document. |
| Download Document Group Archive | `downloadDocumentGroupArchive` | Download a documentgroup and all its documents as a zip archive. |
| Download Member File | `downloadMemberFile` | Download a file stored in a member file field. fieldname is the member property name. |
| Download Member Image | `downloadMemberImage` | Download the image stored in a member image field. fieldname is the member property name and extension its stored extension. size accepts only 'thumb'; omit it for the full image - any other value returns 404/500. |
| Get Account | `getAccount` | Get one accounting account by id. |
| Get Account Group | `getAccountGroup` | Get one accountgroup by id. |
| Get Account Group Template | `getAccountGroupTemplate` | Get one accountgrouptemplate by id. |
| Get Account Template | `getAccountTemplate` | Get one accounttemplate by id. |
| Get Api Key | `getApiKey` | Get one API key object by id. |
| Get Api Key Last Used | `getApiKeyLastUsed` | Return when the given API key was last used. |
| Get Article | `getArticle` | Get one article by id. |
| Get Article Group | `getArticleGroup` | Get one articlegroup by id. |
| Get Article Image | `getArticleImage` | Download the image of an article. filename must be the stored file name from the article's properties.image.name (e.g. image.gif). size accepts only 'thumb' for the thumbnail; omit it for the full image - any other value returns 500/404. |
| Get Changes Since | `getChangesSince` | List object ids changed since the given unix timestamp. |
| Get Comment | `getComment` | Get one comment by id. |
| Get Config | `getConfig` | Get the Webling instance configuration (name, domain, language, enabled modules). |
| Get Cost Center | `getCostCenter` | Get one costcenter by id. |
| Get Current User | `getCurrentUser` | Return the identity behind the API key in use (id, name, type). |
| Get Data Model Definition | `getDefinition` | Get the full data model: every object type with its configured properties, datatypes and allowed values. |
| Get Debitor | `getDebitor` | Get one debitor (invoice) by id. |
| Get Debitor Category | `getDebitorCategory` | Get one debitorcategory by id. |
| Get Document | `getDocument` | Get one document by id. |
| Get Document Group | `getDocumentGroup` | Get one documentgroup by id. |
| Get Entry | `getEntry` | Get one accounting entry by id. |
| Get Entry Group | `getEntryGroup` | Get one entrygroup by id. |
| Get Letter | `getLetter` | Get one letter by id. |
| Get Letter PDF | `getLetterPdf` | Get one letterpdf by id. |
| Get Member | `getMember` | Get one member by id. |
| Get Member Group | `getMemberGroup` | Get one membergroup by id. |
| Get Object | `getObject` | Get any Webling object by id regardless of its type. Works for every object type including ones without a dedicated endpoint. |
| Get Period | `getPeriod` | Get one accounting period by id. |
| Get Period Chain | `getPeriodChain` | Get one periodchain by id. |
| Get Period Group | `getPeriodGroup` | Get one periodgroup by id. |
| Get Quota | `getQuota` | Get plan quotas and current usage (members, entries, periodgroups, storage, credits). |
| Get Replication Delta | `getReplicationDelta` | Get every object created, changed or deleted since the given revision. This is Webling's change feed - use it for polling, the vendor has no webhooks. |
| Get Replication State | `getReplicationState` | Get the current replication revision and data version. Poll this to detect changes: store the revision, then call Get Replication Delta with it. |
| Get Settings | `getSettings` | Get the database settings (currency, country, logo). |
| Get Storage Quota | `getStorageQuota` | Get the storage quota broken down per area (member, finance, letter, post, file, article, document). |
| Get User | `getUser` | Get one Webling user account by id. |
| Get User Group | `getUserGroup` | Get one usergroup by id. |
| Get VAT Rate | `getVatRate` | Get one VAT rate by id. |
| List Account Group Templates | `listAccountGroupTemplates` | List accountgrouptemplate ids. |
| List Account Groups | `listAccountGroups` | List accountgroup ids. |
| List Account Templates | `listAccountTemplates` | List accounttemplate ids (chart-of-accounts template entries). |
| List Accounts | `listAccounts` | List accounting account ids. |
| List Api Keys | `listApiKeys` | List Webling API key object ids. |
| List Article Groups | `listArticleGroups` | List articlegroup ids. |
| List Articles | `listArticles` | List article (inventory item) ids. |
| List Comments | `listComments` | List comment ids. |
| List Cost Centers | `listCostCenters` | List costcenter ids. |
| List Debitor Categories | `listDebitorCategories` | List debitorcategory (invoice run) ids. |
| List Debitors | `listDebitors` | List debitor (invoice) ids. |
| List Document Groups | `listDocumentGroups` | List documentgroup (folder) ids. |
| List Documents | `listDocuments` | List document ids. |
| List Entries | `listEntries` | List accounting entry (booking) ids. |
| List Entry Groups | `listEntryGroups` | List entrygroup (transaction) ids. |
| List Letter PDFs | `listLetterPdfs` | List letterpdf ids (rendered letter PDFs). |
| List Letters | `listLetters` | List letter (mailing) ids. |
| List Member Groups | `listMemberGroups` | List membergroup ids (and root group ids). |
| List Members | `listMembers` | List member object ids. Optional filter/order/format query. |
| List Objects By Type | `listObjectsByType` | List the object ids of any Webling type, including types with no documented endpoint (calendar, calendarevent, page, post, email, emailsent, sms, file, template, settings, bankaccount, payment, participant, attendee, presencelist, memberform, domain, emotion, rnwform, rnwmerchant, saltedgeconnection, letterimage, emailimage, emailattachment, postcomment). Use Get Object to read one. |
| List Period Chains | `listPeriodChains` | List periodchain ids. |
| List Period Groups | `listPeriodGroups` | List periodgroup (accounting book) ids. |
| List Periods | `listPeriods` | List accounting period ids. |
| List User Groups | `listUserGroups` | List usergroup (permission group) ids. |
| List Users | `listUsers` | List Webling user account ids. |
| List VAT Rates | `listVatRates` | List VAT rate ids. |
| Run Transaction Batch | `createTransaction` | Run several write operations as one atomic transaction. operationsJson is a JSON STRING holding an ordered array of {name?, method, url, body} steps; Everything rolls back if any step fails. It is passed as a string because the request body must be a top-level JSON array. |
| Send New Letter | `sendNewLetter` | Render a letter template for the given members and send it (post/email). DESTRUCTIVE: this delivers real mail to real recipients and can consume credits. |
| Start User Onboarding | `startUserOnboarding` | Send the onboarding/invitation email to a Webling user account. DESTRUCTIVE: delivers a real email to a real person. |
| Update Account | `updateAccount` | Update an accounting account by id. |
| Update Account Group | `updateAccountGroup` | Update an accountgroup by id. |
| Update Account Group Template | `updateAccountGroupTemplate` | Update an accountgrouptemplate by id. |
| Update Account Template | `updateAccountTemplate` | Update an accounttemplate by id. |
| Update Api Key | `updateApiKey` | Update an API key object by id. |
| Update Article | `updateArticle` | Update an article by id. |
| Update Article Group | `updateArticleGroup` | Update an articlegroup by id. |
| Update Comment | `updateComment` | Update a comment by id. |
| Update Cost Center | `updateCostCenter` | Update a costcenter by id. |
| Update Debitor | `updateDebitor` | Update a debitor by id. |
| Update Debitor Category | `updateDebitorCategory` | Update a debitorcategory by id. |
| Update Document | `updateDocument` | Update a document by id. Writable properties are isProtected and file ({name, content} with base64 content); description, title, href, size and lastmodified are computed by Webling and are not writable. |
| Update Document Group | `updateDocumentGroup` | Update a documentgroup by id. |
| Update Entry | `updateEntry` | Update an accounting entry by id. |
| Update Entry Group | `updateEntryGroup` | Update an entrygroup by id. |
| Update Member | `updateMember` | Update a member by id (partial update of properties/parents/links). |
| Update Member Group | `updateMemberGroup` | Update a membergroup by id. |
| Update Object | `updateObject` | Update any Webling object by id regardless of its type. |
| Update Period | `updatePeriod` | Update an accounting period by id. |
| Update Period Chain | `updatePeriodChain` | Update a periodchain by id. |
| Update Period Group | `updatePeriodGroup` | Update a periodgroup by id. |
| Update Settings | `updateSettings` | Update the database settings (currency, country, logo). |
| Update User | `updateUser` | Update a Webling user account by id. |
| Update User Group | `updateUserGroup` | Update a usergroup by id. |
| Update VAT Rate | `updateVatRate` | Update a VAT rate by id. |
