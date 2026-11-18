---
description: "CodeREADr is a barcode scanning platform for data collection, validation and ticket/asset tracking."
hidden: true
---

# CodeREADr

CodeREADr is a barcode scanning platform for data collection, validation and ticket/asset tracking. This connector covers the complete CodeREADr API: services (scan workflows) with user authorizations and questions, validation databases and their barcode values (add, upsert, edit, delete, search, CSV upload), scan records and scan search, scan uploads, scan properties, app users, devices, questions and answer options, API limits, and the barcode generator. Responses are returned as the raw XML documents CodeREADr produces.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [codereadr.com](https://codereadr.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 40 |
| **Events** | 0 |
| **Slug** | `codereadr` |

## Use it

Add CodeREADr from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.codereadr.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Answer Option | `addAnswerOption` | Adds an answer option to one or more choice-type questions. Responds with raw XML containing the new answer id. |
| Add Database Value | `addDatabaseValue` | Adds a new barcode value with optional response text and validity to a validation database. Responds with raw XML status. |
| Add Questions To Services | `addQuestionsToServices` | Attaches one or more questions to one or more services, with an optional display condition (shared_submit, pre_submit, post_submit, valid_scan, invalid_scan) and a list of question IDs that must be answered. Responds with raw XML status. |
| Authorize Users For Services | `authorizeUsersForServices` | Authorizes one or more app users to use one or more services. Both parameters accept a single ID, a comma-separated list or the keyword all. Responds with raw XML status. |
| Clear Database | `clearDatabase` | Removes every value from a validation database while keeping the database itself. Responds with raw XML status. |
| Create Database | `createDatabase` | Creates a validation database that services can validate scans against. Case sensitivity is fixed at creation. Responds with raw XML containing the new database id. |
| Create Question | `createQuestion` | Creates a question that can be attached to services. Choice-type questions (checkbox, dropdown, option, webcollect) need answer options added afterwards with Add Answer Option. Responds with raw XML containing the new question id. |
| Create Service | `createService` | Creates a new service (scan workflow) with the chosen validation method: record scans online or on-device, validate scans against a database online or on-device, forward scans to a postback URL, or display web content. Supports active periods, duplicate handling, upload emails, symbologies, auto-next scan, GPS, camera and manual entry restrictions, auto sync and scanner configuration. Responds with raw XML containing the new service id. |
| Create User | `createUser` | Creates an app user. If the username is an email address the password is ignored and the user receives an invitation email to set their own; otherwise a password is required. Optionally limit how many devices the user may activate per billing period. Responds with raw XML containing the new user id. |
| Delete Answer Options | `deleteAnswerOptions` | Removes one or more answer options from a question by answer ID. Responds with raw XML status. |
| Delete Database | `deleteDatabase` | Deletes a validation database and all of its values. Responds with raw XML status. |
| Delete Database Value | `deleteDatabaseValue` | Deletes a barcode value from a validation database. Responds with raw XML status. |
| Delete Questions | `deleteQuestions` | Deletes one or more questions by ID (comma-separated list supported; the keyword all deletes every question). Responds with raw XML status. |
| Delete Scan Property | `deleteScanProperty` | Deletes a named property from a scan. Responds with raw XML status. |
| Delete Scans | `deleteScans` | Deletes one or more scan records by ID (comma-separated list supported). Responds with raw XML status. |
| Delete Services | `deleteServices` | Deletes one or more services by ID (comma-separated list supported; the keyword all deletes every service). Responds with raw XML status. |
| Delete Users | `deleteUsers` | Deletes one or more app users by ID (comma-separated list supported; the keyword all deletes every user). Responds with raw XML status. |
| Edit Database Value | `editDatabaseValue` | Edits the response text and/or validity of an existing barcode value in a validation database. Responds with raw XML status. |
| Generate Barcode | `generateBarcode` | Generates a QR or PDF417 barcode image for a value using the CodeREADr Barcode Generator API. Branding options (size, value text, custom text, logo, frame, file type, error correction) are available on paid plans. Responds with the raw image (PNG, JPG or GIF), or XML on failure. |
| Get API Limits | `getApiLimits` | Returns your account's API request limits and how many requests remain for each tracked time window (per minute, per day). A value of -1 means unlimited. Responds with raw XML. |
| Get Scan Property | `getScanProperty` | Retrieves the value of a named property on a scan. Responds with raw XML. |
| List Databases | `listDatabases` | Lists the validation databases in your account with their name, value count and the services that use them. Use info_level to skip the slower count. Responds with raw XML. |
| List Devices | `listDevices` | Lists the devices registered to your account with their names and details. Optionally restrict to specific device IDs. Responds with raw XML. |
| List Questions | `listQuestions` | Lists the questions defined in your account with their text, type and answer options. Optionally restrict to specific question IDs. Responds with raw XML. |
| List Scan Uploads | `listScanUploads` | Lists the on-device scan uploads received by your account, filterable by service, device and user, with limit and offset paging. Responds with raw XML. |
| List Services | `listServices` | Lists the services (scan workflows) in your account with their validation method, linked database or postback URL, authorized users and attached questions. Optionally restrict to specific service IDs. Responds with raw XML. |
| List Users | `listUsers` | Lists the app users in your account with their username, authorized services, device limit and creation date. Optionally restrict to specific user IDs. Responds with raw XML. |
| Remove Questions From Services | `removeQuestionsFromServices` | Detaches one or more questions from one or more services. Both parameters accept a single ID, a comma-separated list or the keyword all. Responds with raw XML status. |
| Rename Database | `renameDatabase` | Renames a validation database. Responds with raw XML status. |
| Rename Device | `renameDevice` | Renames a device registered to your account. Responds with raw XML status. |
| Revoke Users From Services | `revokeUsersFromServices` | De-authorizes one or more app users from one or more services. Both parameters accept a single ID, a comma-separated list or the keyword all. Responds with raw XML status. |
| Search Database Values | `searchDatabaseValues` | Lists or searches the barcode values of a validation database by exact or partial value or response match and validity, with limit and offset paging. Responds with raw XML including the result count. |
| Search Scans | `searchScans` | Lists or searches scan records with filters for service, device, user, scan ID, validity status, date and time range, upload, value and response matching, scan properties, timezone, ordering and paging. Responds with raw XML containing the count and each scan's device, service, user, status, value, response, timestamp, answers and properties. |
| Set Scan Property | `setScanProperty` | Creates or updates a named property (case-sensitive name and value, up to 100 characters each) on one or more scans. Responds with raw XML status. |
| Update Service | `updateService` | Edits an existing service. Only the settings you pass are changed; omitted settings keep their current values (except symbologies, which reset to default when omitted). Responds with raw XML status. |
| Update User | `updateUser` | Edits an app user's username, password or device limit. Omitted fields are left unchanged. Responds with raw XML status. |
| Upload CSV To Database | `uploadCsvToDatabase` | Imports barcode values into a validation database from CSV text, sent as a multipart/form-data file upload (field csvfile). Values are trimmed and imported synchronously (CodeREADr defaults). Responds with raw XML status: &lt;status&gt;1&lt;/status&gt; on success. |
| Upsert Database Value | `upsertDatabaseValue` | Inserts a barcode value into a validation database, or updates its response text and validity if it already exists, without checking its current state first. Responds with raw XML status. |
| Upsert Multiple Database Values | `upsertMultipleDatabaseValues` | Inserts or updates up to 100 barcode values in one request. Global database_id and trim_value apply to every value that does not set its own. Responds with raw XML status. |
| Validate User | `validateUser` | Checks an app user's username and password and, when valid, returns the user's ID, authorized services, device limit and creation date. Responds with raw XML. |
