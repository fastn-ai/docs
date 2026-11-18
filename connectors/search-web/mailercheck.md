---
description: "MailerCheck email verification API."
---

# MailerCheck

MailerCheck email verification API. Verify single emails in real time or asynchronously, manage verification lists, run list verification, read results, and read account/credit/user information. Auth is a Bearer API token created in the MailerCheck UI (profile &gt; API &gt; Create token).

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [mailercheck.com](https://mailercheck.com) |
| **Authentication** | API key |
| **Actions** | 14 |
| **Events** | 0 |
| **Slug** | `mailercheck` |

## Use it

Add MailerCheck from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailercheck.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Single Email | `checkSingleEmail` | Verify one email address in real time and return its verification status (valid, catch_all, mailbox_full, role_based, disposable, typo, unknown, syntax_error). SPENDS ONE VERIFICATION CREDIT per call. |
| Check Single Email (Async) | `checkSingleEmailAsync` | Queue verification of one email address and return a verification id to poll with Get Single Email Result. SPENDS ONE VERIFICATION CREDIT per call. |
| Create List | `createList` | Create an email verification list from a name and an array of email addresses. Creating the list spends no credits; verifying it later does. |
| Delete List | `deleteList` | Permanently delete an email verification list by id. Returns HTTP 204 with an empty body. |
| Get Account | `getAccount` | Return the MailerCheck account the API token belongs to, including the remaining credit balance. |
| Get Credits | `getCredits` | Return the number of verification credits remaining on the account. Every single or list verification spends credits, so call this before running a check. |
| Get List | `getList` | Return a single email verification list by its id, including row counts and per-result totals. Spends no credits. |
| Get List Results | `getListResults` | Return the individual emails of a list with their verification result, paginated and optionally filtered by result type (valid, catch_all, unknown, etc). Spends no credits. |
| Get Platform Stats | `getPlatformStats` | Undocumented public MailerCheck endpoint returning platform-wide verification counters (total, totalToday, totalOrders, totalTodayOrders). It is NOT account-scoped and must be called WITHOUT an Authorization header: sending a valid API token switches it to an admin-only mode that answers 401 'Please provide account id in header X-Acc-Id.' for every account id. No credentials are sent by this action. |
| Get Single Email Result (Async) | `getSingleEmailResult` | Retrieve the result of an asynchronous single-email verification by its verification id. Spends no credits. |
| Get User | `getUser` | Return the MailerCheck user that created the API token. |
| List Lists | `listLists` | Return all email verification lists belonging to the account, paginated. Spends no credits. |
| Upload List | `uploadList` | Create an email verification list from an uploaded CSV or TXT file, sent as multipart/form-data under the field name 'file'. Pass the file's text content in fileContent and its name in filename. Uploading spends no credits; verifying the resulting list does. |
| Verify List | `verifyList` | Start verification of every email in the given list. Returns HTTP 202 with the list object. SPENDS ONE VERIFICATION CREDIT PER EMAIL in the list; returns HTTP 402 with {"error":"Not enough credits. Credits required: N"} when the balance is too low. |
