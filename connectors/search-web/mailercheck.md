---
description: "MailerCheck verifies email addresses. Check single emails, verify lists, read results and view account credits."
hidden: true
---

# MailerCheck

<img src="../../.gitbook/assets/connectors/lg/mailercheck.png" alt="MailerCheck logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [mailercheck.com](https://mailercheck.com) |
| **Authentication** | API key |
| **Slug** | `mailercheck` |

## Setup

Your customers enter their API key for MailerCheck when they connect. Nothing else needs setting up.

## Use it

Add MailerCheck from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailercheck.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Single Email</td><td><code>checkSingleEmail</code></td><td>Verify one email address in real time and return its verification status (valid, catch_all, mailbox_full, role_based, disposable, typo, unknown, syntax_error). SPENDS ONE VERIFICATION CREDIT per call.</td></tr><tr><td>Check Single Email (Async)</td><td><code>checkSingleEmailAsync</code></td><td>Queue verification of one email address and return a verification id to poll with Get Single Email Result. SPENDS ONE VERIFICATION CREDIT per call.</td></tr><tr><td>Create List</td><td><code>createList</code></td><td>Create an email verification list from a name and an array of email addresses. Creating the list spends no credits; verifying it later does.</td></tr><tr><td>Delete List</td><td><code>deleteList</code></td><td>Permanently delete an email verification list by id.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Return the MailerCheck account the API token belongs to, including the remaining credit balance.</td></tr><tr><td>Get Credits</td><td><code>getCredits</code></td><td>Return the number of verification credits remaining on the account. Every single or list verification spends credits, so call this before running a check.</td></tr><tr><td>Get List</td><td><code>getList</code></td><td>Return a single email verification list by its id, including row counts and per-result totals. Spends no credits.</td></tr><tr><td>Get List Results</td><td><code>getListResults</code></td><td>Return the individual emails of a list with their verification result, paginated and optionally filtered by result type (valid, catch_all, unknown, etc). Spends no credits.</td></tr><tr><td>Get Platform Stats</td><td><code>getPlatformStats</code></td><td>Undocumented public MailerCheck endpoint returning platform-wide verification counters (total, totalToday, totalOrders, totalTodayOrders). No credentials are sent by this action.</td></tr><tr><td>Get Single Email Result (Async)</td><td><code>getSingleEmailResult</code></td><td>Retrieve the result of an asynchronous single-email verification by its verification id. Spends no credits.</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get User</td><td><code>getUser</code></td><td>Return the MailerCheck user that created the API token.</td></tr><tr><td>List Lists</td><td><code>listLists</code></td><td>Return all email verification lists belonging to the account, paginated. Spends no credits.</td></tr><tr><td>Upload List</td><td><code>uploadList</code></td><td>Create an email verification list from an uploaded CSV or TXT file, sent as multipart/form-data under the field name 'file'. Pass the file's text content in fileContent and its name in filename. Uploading spends no credits; verifying the resulting list does.</td></tr><tr><td>Verify List</td><td><code>verifyList</code></td><td>Start verification of every email in the given list. SPENDS ONE VERIFICATION CREDIT PER EMAIL in the list; Credits required: N"} when the balance is too low.</td></tr></tbody></table>

</details>

## Events

MailerCheck has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
