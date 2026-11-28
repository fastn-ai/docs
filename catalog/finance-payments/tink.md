---
description: "Tink is an open banking platform for Europe. Read bank accounts and transactions, and manage credentials and budgets."
hidden: true
---

# Tink

<img src="../../.gitbook/assets/connectors/lg/tink.png" alt="Tink logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [tink.com](https://tink.com) |
| **Authentication** | Client ID and secret, OAuth 2.0 |
| **Slug** | `tink` |

## Setup

Your customers sign in to Tink through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Tink from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Tink**.
2. Select **Connect** on the Tink card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Tink offers more than one sign-in method. Choose one in **Auth Method**, then:

   * For a key or credential method, fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

     <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

   * For OAuth 2.0, keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Tink and approve access in the window that opens.

     <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Tink's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Archive Budget</td><td><code>archiveBudget</code></td><td>Archives a budget so it no longer tracks spending, while retaining its history. Tink archives budgets rather than deleting them.</td></tr><tr><td>Create Credential</td><td><code>createCredential</code></td><td>Connects a bank for the current user by creating credentials against a provider, starting Tink's aggregation of that bank's accounts and transactions. The credentials are returned with status CREATED; poll the Get Credential action until the status becomes UPDATED.</td></tr><tr><td>Create One-Off Budget</td><td><code>createOneOffBudget</code></td><td>Creates a one-off budget for the connected user that tracks spending against a target amount over a fixed start and end date, filtered by accounts, categories, or tags.</td></tr><tr><td>Create Recurring Budget</td><td><code>createRecurringBudget</code></td><td>Creates a recurring budget for the connected user that tracks spending against a target amount every week, month, or year, filtered by accounts, categories, or tags.</td></tr><tr><td>Delete Credential</td><td><code>deleteCredential</code></td><td>Disconnects a bank by deleting a set of credentials and all financial data aggregated through them. This is irreversible and revokes the underlying bank consent.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Retrieves a single bank account of the connected user by its account identifier, including its balances and account identifiers.</td></tr><tr><td>Get Budget Details</td><td><code>getBudgetDetails</code></td><td>Retrieves spending progress for a budget over a given time window, including the amount spent per budget period and the average spent amount across those periods.</td></tr><tr><td>Get Credential</td><td><code>getCredential</code></td><td>Retrieves a single set of bank credentials of the connected user by its credentials identifier, including its current aggregation status.</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Retrieves the Tink user associated with the current access token, including the user's ID, external user ID, app ID, feature flags, and profile settings.</td></tr><tr><td>Get User Profile</td><td><code>getUserProfile</code></td><td>Retrieves the profile settings of the current Tink user, including market, locale, currency, time zone, period configuration, and notification preferences.</td></tr></tbody></table>

<details>

<summary>View 13 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Accounts</td><td><code>listAccounts</code></td><td>Lists the connected user's bank accounts with their identifiers, type, name, and balances. Returns an empty list until the user has connected a bank via Tink Link.</td></tr><tr><td>List Accounts (Legacy)</td><td><code>listAccountsLegacy</code></td><td>Lists the connected user's accounts using Tink's legacy v1 accounts endpoint. Prefer the List Accounts action, which uses the current Data API v2.</td></tr><tr><td>List Budgets</td><td><code>listBudgets</code></td><td>Lists the budgets defined for the connected user, including each budget's target amount, periodicity, and the filter that selects the transactions it tracks.</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>Lists Tink's transaction category tree for the connected user's locale, including each category's code, identifier, and display name.</td></tr><tr><td>List Credentials</td><td><code>listCredentials</code></td><td>Lists the bank credentials of the connected user, showing each connected provider, its aggregation status, and when it was last refreshed.</td></tr><tr><td>List Loans</td><td><code>listLoans</code></td><td>Lists the connected user's loan accounts with balances, interest rates, and the weighted average interest rate across all loans.</td></tr><tr><td>List Provider Consents</td><td><code>listProviderConsents</code></td><td>Lists the connected user's bank consents, showing each consent's status, the accounts it covers, and when it expires. Use this to detect consents that need renewal.</td></tr><tr><td>List Providers</td><td><code>listProviders</code></td><td>Lists the financial institution providers available to the connected user's market, including each provider's authentication type, access type, capabilities, and the credential fields it requires.</td></tr><tr><td>List Providers by Market</td><td><code>listProvidersByMarket</code></td><td>Lists the financial institution providers available in a specific market, identified by its ISO 3166-1 alpha-2 country code.</td></tr><tr><td>List Transactions</td><td><code>listTransactions</code></td><td>Lists the connected user's bank transactions with amounts, dates, descriptions, and categorization. Returns an empty list until the user has connected a bank via Tink Link.</td></tr><tr><td>Query Statistics</td><td><code>queryStatistics</code></td><td>Queries aggregated financial statistics for the connected user, such as expenses by category, income by category, balances by account, or left-to-spend, over one or more periods.</td></tr><tr><td>Refresh Credential</td><td><code>refreshCredential</code></td><td>Triggers a new aggregation run for a set of bank credentials, fetching the latest accounts and transactions from the bank. Returns an empty body; poll the Get Credential action until the status becomes UPDATED.</td></tr><tr><td>Search Transactions</td><td><code>searchTransactions</code></td><td>Searches the connected user's transactions using free-text, account, category, amount, and date filters, and returns matching transactions together with aggregate metrics such as count, sum, and average.</td></tr></tbody></table>

</details>

