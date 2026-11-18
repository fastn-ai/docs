---
description: "PartnerStack is a partner relationship management platform for affiliate, referral and reseller programs."
hidden: true
---

# PartnerStack

<img src="../../.gitbook/assets/connectors/lg/partnerstack.png" alt="PartnerStack logo">

PartnerStack is a partner relationship management platform for affiliate, referral and reseller programs. This connector covers the complete PartnerStack Partner API v2 (https://api.partnerstack.com/api/v2), the read API available to partners: partnerships with the programs you promote, the customers you referred, transactions and actions attributed to you, the rewards you earned, your payouts, and the PartnerStack marketplace of programs you can join. Partner-side events are delivered by PartnerStack Postbacks. The separate PartnerStack Vendor API, which uses Basic authentication with a vendor public/secret key pair, is not covered here.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [partnerstack.com](https://partnerstack.com) |
| **Authentication** | Bearer token |
| **Slug** | `partnerstack` |

## Use it

Add PartnerStack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.partnerstack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Marketplace Program | `getMarketplaceProgram` | Retrieves a single PartnerStack marketplace program by its company key, including its categories, description, commission offers and promotions. Use the company key from a partnership returned by List Partnerships. Note that keys returned by List Marketplace Programs are not always resolvable here and can return a 404. |
| List Actions | `listPartnerActions` | Returns the actions you or your referred customers performed on a partner company's platform, such as a signup or a content submission, sorted by creation date with the most recent first. Each action carries its type, how many times it was performed, and the partnership and customer it belongs to. Results are cursor paginated. |
| List Customers | `listCustomers` | Returns the customers you referred to the companies you are partnered with, sorted by creation date with the most recent first. Each customer carries the referring partnership, the company, whether the customer has paid and any sub IDs used for tracking. Results are cursor paginated. |
| List Marketplace Programs | `listMarketplacePrograms` | Returns the partner programs listed on the PartnerStack marketplace that you can apply to join, sorted by creation date with the most recent first. Each program carries its categories, description, website, commission offers and available promotions. Results are cursor paginated. |
| List Partnerships | `listPartnerships` | Returns the partnerships between you and the companies whose programs you promote on PartnerStack, sorted by creation date with the most recent first. Each partnership carries the company, your status in its program, your referral link and your partner team. Results are cursor paginated. |
| List Payouts | `listPayouts` | Returns your payouts, the rewards that have been made payable to you, sorted by creation date with the most recent first. Each payout carries its amount in cents, currency, status, payment provider and withdrawal date. Results are cursor paginated. |
| List Rewards | `listRewards` | Returns the rewards you have earned from the companies you are partnered with, sorted by creation date with the most recent first. Each reward carries its amount in cents, reward and payment status, the source that generated it and the customer it relates to. Supports extensive filtering by company, group, customer, invoice, currency, status and free text keywords. Results are cursor paginated. |
| List Transactions | `listTransactions` | Returns the transactions recorded against the customers you referred, sorted by creation date with the most recent first. Each transaction carries its amount in cents, the currency, the originating customer and partnership, and the product it relates to. Results are cursor paginated. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Action Created | `action.created` | An action related to one of your partnerships with a vendor has been created. Setup: in your PartnerStack partner dashboard open https://dash.partnerstack.com/settings/postbacks (profile settings, then Postback), create a new postback, paste this fastn trigger URL as the Endpoint URL, give the postback a Name, and select the Action event types. Note the PartnerStack docs list this event as 'action_created' in prose while the documented sample payload carries 'action.created'; the dotted form is what the eventKey matches. Payload modelled from the PartnerStack Postbacks documentation. |
| Action Updated | `action.updated` | An action related to one of your partnerships with a vendor has been updated. Setup: in your PartnerStack partner dashboard open https://dash.partnerstack.com/settings/postbacks (profile settings, then Postback), create a new postback, paste this fastn trigger URL as the Endpoint URL, give the postback a Name, and select the Action event types. Note the PartnerStack docs list this event as 'action_updated' in prose while the documented sample payload uses the dotted form; the dotted form is what the eventKey matches. Payload modelled from the PartnerStack Postbacks documentation. |
| Customer Created | `customer.created` | A customer related to one of your partnerships with a vendor has been created. Setup: in your PartnerStack partner dashboard open https://dash.partnerstack.com/settings/postbacks (profile settings, then Postback), create a new postback, paste this fastn trigger URL as the Endpoint URL, give the postback a Name, and select the Customer event types. Payload modelled from the PartnerStack Postbacks documentation. |
| Customer Deleted | `customer.deleted` | A customer related to one of your partnerships with a vendor has been deleted. Setup: in your PartnerStack partner dashboard open https://dash.partnerstack.com/settings/postbacks (profile settings, then Postback), create a new postback, paste this fastn trigger URL as the Endpoint URL, give the postback a Name, and select the Customer event types. Payload modelled from the PartnerStack Postbacks documentation. |
| Customer Updated | `customer.updated` | A customer related to one of your partnerships with a vendor has been updated. Setup: in your PartnerStack partner dashboard open https://dash.partnerstack.com/settings/postbacks (profile settings, then Postback), create a new postback, paste this fastn trigger URL as the Endpoint URL, give the postback a Name, and select the Customer event types. Payload modelled from the PartnerStack Postbacks documentation. |
| Reward Created | `reward.created` | A reward has been generated for you by a vendor you are partnered with. Setup: in your PartnerStack partner dashboard open https://dash.partnerstack.com/settings/postbacks (profile settings, then Postback), create a new postback, paste this fastn trigger URL as the Endpoint URL, give the postback a Name, and select the Reward event types. Payload modelled from the PartnerStack Postbacks documentation. |
| Reward Updated | `reward.updated` | A reward of yours has been updated by a vendor you are partnered with, for example when it moves from pending to approved or paid. Setup: in your PartnerStack partner dashboard open https://dash.partnerstack.com/settings/postbacks (profile settings, then Postback), create a new postback, paste this fastn trigger URL as the Endpoint URL, give the postback a Name, and select the Reward event types. Payload modelled from the PartnerStack Postbacks documentation. |
| Test Event | `test` | The test event PartnerStack sends when you verify a postback endpoint. Setup: in your PartnerStack partner dashboard open https://dash.partnerstack.com/settings/postbacks (profile settings, then Postback), create a new postback, paste this fastn trigger URL as the Endpoint URL, give the postback a Name, select the event types you want, save it, then use the send test event control. Postback registration is done in the PartnerStack UI only; the Partner API has no postback registration endpoint. Payload modelled from the PartnerStack Postbacks documentation. |
| Transaction Created | `transaction.created` | A transaction related to one of your partnerships with a vendor has been created. Setup: in your PartnerStack partner dashboard open https://dash.partnerstack.com/settings/postbacks (profile settings, then Postback), create a new postback, paste this fastn trigger URL as the Endpoint URL, give the postback a Name, and select the Transaction event types. Payload modelled from the PartnerStack Postbacks documentation. |
| Transaction Updated | `transaction.updated` | A transaction related to one of your partnerships with a vendor has been updated. Setup: in your PartnerStack partner dashboard open https://dash.partnerstack.com/settings/postbacks (profile settings, then Postback), create a new postback, paste this fastn trigger URL as the Endpoint URL, give the postback a Name, and select the Transaction event types. Payload modelled from the PartnerStack Postbacks documentation. |
