---
description: "Tink is an open banking platform for accessing bank account, balance, transaction, and financial insight data across European financial institutions."
hidden: true
---

# Tink

<img src="../../.gitbook/assets/connectors/tink.png" alt="Tink logo" width="64">

Tink is an open banking platform for accessing bank account, balance, transaction, and financial insight data across European financial institutions. Connect an end user's bank via Tink Link to read accounts, balances, transactions, categories, budgets, statistics, loans, and consent status.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [tink.com](https://tink.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Slug** | `tink` |

## Use it

Add Tink from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tink.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Budget | `archiveBudget` | Archives a budget so it no longer tracks spending, while retaining its history. Tink archives budgets rather than deleting them. |
| Create Credential | `createCredential` | Connects a bank for the current user by creating credentials against a provider, starting Tink's aggregation of that bank's accounts and transactions. The credentials are returned with status CREATED; poll the Get Credential action until the status becomes UPDATED. |
| Create One-Off Budget | `createOneOffBudget` | Creates a one-off budget for the connected user that tracks spending against a target amount over a fixed start and end date, filtered by accounts, categories, or tags. |
| Create Recurring Budget | `createRecurringBudget` | Creates a recurring budget for the connected user that tracks spending against a target amount every week, month, or year, filtered by accounts, categories, or tags. |
| Delete Credential | `deleteCredential` | Disconnects a bank by deleting a set of credentials and all financial data aggregated through them. This is irreversible and revokes the underlying bank consent. |
| Get Account | `getAccount` | Retrieves a single bank account of the connected user by its account identifier, including its balances and account identifiers. |
| Get Budget Details | `getBudgetDetails` | Retrieves spending progress for a budget over a given time window, including the amount spent per budget period and the average spent amount across those periods. |
| Get Credential | `getCredential` | Retrieves a single set of bank credentials of the connected user by its credentials identifier, including its current aggregation status. |
| Get User | `getUser` | Retrieves the Tink user associated with the current access token, including the user's ID, external user ID, app ID, feature flags, and profile settings. |
| Get User Profile | `getUserProfile` | Retrieves the profile settings of the current Tink user, including market, locale, currency, time zone, period configuration, and notification preferences. |

<details>

<summary>See 13 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Accounts | `listAccounts` | Lists the connected user's bank accounts with their identifiers, type, name, and balances. Returns an empty list until the user has connected a bank via Tink Link. |
| List Accounts (Legacy) | `listAccountsLegacy` | Lists the connected user's accounts using Tink's legacy v1 accounts endpoint. Prefer the List Accounts action, which uses the current Data API v2. |
| List Budgets | `listBudgets` | Lists the budgets defined for the connected user, including each budget's target amount, periodicity, and the filter that selects the transactions it tracks. |
| List Categories | `listCategories` | Lists Tink's transaction category tree for the connected user's locale, including each category's code, identifier, and display name. |
| List Credentials | `listCredentials` | Lists the bank credentials of the connected user, showing each connected provider, its aggregation status, and when it was last refreshed. |
| List Loans | `listLoans` | Lists the connected user's loan accounts with balances, interest rates, and the weighted average interest rate across all loans. |
| List Provider Consents | `listProviderConsents` | Lists the connected user's bank consents, showing each consent's status, the accounts it covers, and when it expires. Use this to detect consents that need renewal. |
| List Providers | `listProviders` | Lists the financial institution providers available to the connected user's market, including each provider's authentication type, access type, capabilities, and the credential fields it requires. |
| List Providers by Market | `listProvidersByMarket` | Lists the financial institution providers available in a specific market, identified by its ISO 3166-1 alpha-2 country code. |
| List Transactions | `listTransactions` | Lists the connected user's bank transactions with amounts, dates, descriptions, and categorization. Returns an empty list until the user has connected a bank via Tink Link. |
| Query Statistics | `queryStatistics` | Queries aggregated financial statistics for the connected user, such as expenses by category, income by category, balances by account, or left-to-spend, over one or more periods. |
| Refresh Credential | `refreshCredential` | Triggers a new aggregation run for a set of bank credentials, fetching the latest accounts and transactions from the bank. Returns an empty body; poll the Get Credential action until the status becomes UPDATED. |
| Search Transactions | `searchTransactions` | Searches the connected user's transactions using free-text, account, category, amount, and date filters, and returns matching transactions together with aggregate metrics such as count, sum, and average. |

</details>
