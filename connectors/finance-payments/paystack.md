---
description: "Paystack payments platform for Africa."
hidden: true
---

# Paystack

<img src="../../.gitbook/assets/connectors/paystack.png" alt="Paystack logo" width="64">

Paystack payments platform for Africa. Accept payments and manage transactions, charges and bulk charges, customers and direct debit mandates, dedicated virtual accounts, virtual terminals and POS terminals, plans and subscriptions, transfer recipients and transfers, payment requests and invoices, products, storefronts and orders, payment pages, subaccounts and transaction splits, settlements, refunds, disputes, balance and ledger, bank resolution and account verification via the Paystack REST API (https://api.paystack.co). Authenticates with your Paystack secret key as a Bearer token; the key itself selects test or live mode.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [paystack.com](https://paystack.com) |
| **Authentication** | Bearer token |
| **Slug** | `paystack` |

## Use it

Add Paystack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.paystack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Evidence | `disputeEvidence` | Provide evidence for a dispute |
| Add Products | `pageAddProducts` | Add products to a previously created payment page. You can only add products to pages that was created with a `product` type. |
| Add Products to Storefront | `storefrontAddProducts` | Add previously created products to a Storefront |
| Add Split Code to Virtual Terminal | `virtualTerminalAddSplitCode` | Add Split Code to Virtual Terminal |
| Add Subaccount to Split | `splitAddSubaccount` | Add a subaccount to a split configuration, or update the share of an existing subaccount |
| Archive Payment Request | `paymentRequestArchive` | Archive a payment request to clean up your records. An archived payment request cannot be verified and will not be returned when listing all previously created payment requests. |
| Assign Dedicated Account | `dedicatedAccountAssign` | With this endpoint, you can create a customer, validate the customer, and assign a DVA to the customer. |
| Assign Destination to Virtual Terminal | `virtualTerminalDestinationAssign` | Add a destination (WhatsApp number) to a Virtual Terminal on your integration |
| Balance Ledger | `balanceLedger` | Fetch all pay-ins and pay-outs that occured on your integration |
| Bulk Create Transfer Recipient | `transferrecipientBulk` | Create multiple transfer recipients in batches. A duplicate account number will lead to the retrieval of the existing record. |

<details>

<summary>See 153 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Charge Authorization | `transactionChargeAuthorization` | Charge all authorizations marked as reusable with this endpoint whenever you need to receive payments |
| Check pending charge | `chargeCheck` | When you get `pending` as a charge status or if there was an exception when calling any of the `/charge` endpoints, wait 10 seconds or more, then make a check to see if its status has changed. Don't call too early as you may get a lot more pending than you should. |
| Check Slug Availability | `pageCheckSlugAvailability` | Check if a custom slug is available for use when creating a payment page |
| Commission Terminal | `terminalCommission` | Activate your debug device by linking it to your integration |
| Create Charge | `chargeCreate` | Initiate a payment by integrating the payment channel of your choice. |
| Create Customer | `customerCreate` | Create a customer on your integration |
| Create Dedicated Account | `dedicatedAccountCreate` | Create a dedicated virtual account for an existing customer |
| Create Order | `orderCreate` | Create an order for selected items |
| Create Page | `pageCreate` | Create a webpage to receive payments |
| Create Payment Request | `paymentRequestCreate` | Create a new payment request by issuing an invoice to a customer |
| Create Plan | `planCreate` | Create a plan for recurring payments |
| Create Product | `productCreate` | Create a new product on your integration |
| Create Refund | `refundCreate` | Initiate a refund for a previously completed transaction |
| Create Split | `splitCreate` | Create a split configuration for transactions |
| Create Storefront | `storefrontCreate` | Create a digital shop to manage and display your products |
| Create Subaccount | `subaccountCreate` | Create a subacount for a partner |
| Create Subscription | `subscriptionCreate` | Create a subscription a customer |
| Create Transfer Recipient | `transferrecipientCreate` | Creates a new recipient. A duplicate account number will lead to the retrieval of the existing record. |
| Create Virtual Terminal | `virtualTerminalCreate` | Create a Virtual Terminal on your integration |
| Deactivate Authorization | `customerDeactivateAuthorization` | Deactivate an authorization for any payment channel. |
| Deactivate Dedicated Account | `dedicatedAccountDeactivate` | Deactivate a dedicated virtual account on your integration. |
| Deactivate Virtual Terminal | `virtualTerminalDeactivate` | Deactivate a Virtual Terminal on your integration |
| Decommission Terminal | `terminalDecommission` | Unlink your debug device from your integration |
| Delete Product | `productDelete` | Delete a previously created product |
| Delete Storefront | `storefrontDelete` | Delete a previously created Storefront |
| Delete Transfer Recipient | `transferrecipientDelete` | Delete a transfer recipient (sets the transfer recipient to inactive) |
| Direct Debit Activation Charge | `customerDirectDebitActivationCharge` | Trigger an activation charge on an inactive mandate on behalf of your customer |
| Disable OTP for Transfers | `transferDisableOtp` | This is used in the event that you want to be able to complete transfers programmatically without use of OTPs. No arguments required. You will get an OTP to complete the request. |
| Disable Subscription | `subscriptionDisable` | Disable a subscription on your integration |
| Duplicate Storefront | `storefrontDuplicate` | Duplicate a previously created Storefront |
| Enable OTP requirement for Transfers | `transferEnableOtp` | In the event that a customer wants to stop being able to complete transfers programmatically, this endpoint helps turn OTP requirement back on. No arguments required. |
| Enable Subscription | `subscriptionEnable` | Enable a subscription on your integration |
| Export Disputes | `disputeDownload` | Export the disputes available on your integration |
| Export Transactions | `transactionExport` | Download transactions that occurred on your integration for a specific timeframe |
| Export Transfers | `transferExportTransfer` | Export a list of transfers carried out on your integration |
| Fetch Balance | `balanceFetch` | Fetch the available balance on your integration |
| Fetch Bank Providers | `dedicatedAccountAvailableProviders` | Get available bank providers for a dedicated virtual account |
| Fetch Bulk Charge Batch | `bulkChargeFetch` | This endpoint retrieves a specific batch code. It also returns useful information on its progress by way of the `total_charges` and `pending_charges` attributes. |
| Fetch Customer | `customerFetch` | Get details of a customer on your integration. |
| Fetch Dedicated Account | `dedicatedAccountFetch` | Get details of a dedicated virtual account on your integration. |
| Fetch Dispute | `disputeFetch` | Fetch a transaction dispute |
| Fetch Event Status | `terminalFetchEventStatus` | Check the status of an event sent to the Terminal |
| Fetch Mandate Authorizations | `customerFetchMandateAuthorizations` | Get the list of direct debit mandates associated with a customer |
| Fetch Order | `orderFetch` | Fetch the details of a previously created order |
| Fetch Page | `pageFetch` | Get a previously created payment page |
| Fetch Payment Request | `paymentRequestFetch` | Fetch a previously created payment request |
| Fetch Payment Session Timeout | `integrationFetchPaymentSessionTimeout` | Fetch the session timeout of a transaction |
| Fetch Plan | `planFetch` | Get the details of a payment plan |
| Fetch Product | `productFetch` | Fetch a previously created product |
| Fetch Product Orders | `orderProduct` | Fetch all orders for a particular product |
| Fetch Refund | `refundFetch` | Get a previously created refund |
| Fetch Settlement Transactions | `settlementsTransaction` | Get the transactions that make up a particular settlement |
| Fetch Split | `splitFetch` | Get details of a split configuration for a transaction |
| Fetch Storefront | `storefrontFetch` | Get the details of a previously created Storefront |
| Fetch Storefront Orders | `storefrontFetchOrders` | Fetch all orders in your Storefront |
| Fetch Subaccount | `subaccountFetch` | Get details of a subaccount on your integration |
| Fetch Subscription | `subscriptionFetch` | Get details of a customer's subscription |
| Fetch Terminal | `terminalFetch` | Get the details of a Terminal |
| Fetch Terminal Status | `terminalFetchTerminalStatus` | Check the availiability of a Terminal before sending an event to it |
| Fetch Transaction | `transactionFetch` | Fetch a transaction to get its details |
| Fetch Transaction Timeline | `transactionTimeline` | Fetch the steps taken from the initiation to the completion of a transaction |
| Fetch Transfer | `transferFetch` | Get details of a transfer on your integration |
| Fetch Transfer recipient | `transferrecipientFetch` | Fetch the details of a transfer recipient |
| Fetch Upload URL | `disputeUploadUrl` | Get the URL to upload a dispute evidence |
| Fetch Virtual Terminal | `virtualTerminalFetch` | Fetch a Virtual Terminal on your integration |
| Finalize Disabling OTP for Transfers | `transferDisableOtpFinalize` | Finalize the request to disable OTP on your transfers |
| Finalize Payment Request | `paymentRequestFinalize` | Finalise the creation of a draft payment request for a customer |
| Finalize Transfer | `transferFinalize` | Finalize an initiated transfer |
| Generate Update Subscription Link | `subscriptionManageLink` | Generate a link for updating the card on a subscription |
| Initialize Authorization | `customerInitializeAuthorization` | Initiate a request to create a reusable authorization code for recurring transactions |
| Initialize Direct Debit | `customerInitializeDirectDebit` | Initialize the process of linking an account to a customer for Direct Debit transactions |
| Initialize Transaction | `transactionInitialize` | Initialize Transaction on the Paystack Transaction resource. |
| Initiate Bulk Charge | `bulkChargeInitiate` | Charge multiple customers in batches |
| Initiate Bulk Transfer | `transferBulk` | Batch multiple transfers in a single request. You need to disable the Transfers OTP requirement to use this endpoint. |
| Initiate Transfer | `transferInitiate` | Send money to your customers |
| List Banks | `bankList` | List banks supported on Paystack |
| List Bulk Charge Batches | `bulkChargeList` | List all bulk charge batches. |
| List Charges in a Batch | `bulkChargeCharges` | This endpoint retrieves the charges associated with a specified batch code |
| List Countries | `miscellaneousListCountries` | List all supported countries on Paystack |
| List Customers | `customerList` | List customers on your integration |
| List Dedicated Accounts | `dedicatedAccountList` | List dedicated virtual accounts available on your integration. |
| List Disputes | `disputeList` | List transaction disputes filed by customers |
| List Domains | `applePayListDomain` | Lists all registered domains on your integration. Returns an empty array if no domains have been added. |
| List Mandate Authorizations | `directdebitListMandateAuthorizations` | Get a list of all the direct debit mandates on your integration |
| List Orders | `orderList` | List the previously created orders |
| List Pages | `pageList` | List all previously created payment pages |
| List Payment Request | `paymentRequestList` | List all previously created payment requests to your customers |
| List Plans | `planList` | List all recurring payment plans |
| List Products | `productList` | List all previously created products |
| List Refunds | `refundList` | List previously created refunds |
| List Settlements | `settlementsFetch` | List settlements made to your settlement accounts |
| List Splits | `splitList` | List the transaction splits available on your integration |
| List States (AVS) | `miscellaneousAvs` | Get a list of states for a country for address verification |
| List Storefront Products | `storefrontListProducts` | List the products in a Storefront |
| List Storefronts | `storefrontList` | List the storefronts you previously created |
| List Subaccounts | `subaccountList` | List subaccounts available on your integration |
| List Subscriptions | `subscriptionList` | List all subscriptions available on your integration |
| List Terminals | `terminalList` | List the Terminals available on your integration |
| List Transaction Disputes | `disputeTransaction` | List all disputes filed for a transaction |
| List Transactions | `transactionList` | List transactions that has occurred on your integration |
| List Transfer Recipients | `transferrecipientList` | List transfer recipients available on your integration |
| List Transfers | `transferList` | List the transfers made on your integration |
| List Virtual Terminals | `virtualTerminalList` | List Virtual Terminals on your integration |
| Partial Debit | `transactionPartialDebit` | Retrieve part of a payment from a customer |
| Pause Bulk Charge Batch | `bulkChargePause` | Pause the processing of a charge batch |
| Payment Request Total | `paymentRequestTotals` | Get the metric of all pending and successful payment requests |
| Publish Storefront | `storefrontPublish` | Make your Storefront publicly available |
| Register Domain | `applePayRegisterDomain` | Register a top-level domain or subdomain for your Apple Pay integration. &gt; This endpoint can only be called with one domain or subdomain at a time. |
| Remove Split Code from Virtual Terminal | `virtualTerminalDeleteSplitCode` | Remove Split Code from Virtual Terminal |
| Remove Split from Dedicated Account | `dedicatedAccountRemoveSplit` | If you've previously set up split payment for transactions on a dedicated virtual account, you can remove it with this endpoint |
| Remove Subaccount from split | `splitRemoveSubaccount` | Remove a subaccount from a split configuration |
| Requery Dedicated Account | `dedicatedAccountRequery` | Requery Dedicated Virtual Account for new transactions |
| Resend OTP for Transfer | `transferResendOtp` | Generates and send a new OTP to customer in the event they are having trouble receiving one. |
| Resolve Account Number | `bankResolveAccountNumber` | Resolve an account number to confirm the name associated with it |
| Resolve Card BIN | `miscellaneousResolveCardBin` | Get the details of a card BIN |
| Resolve Dispute | `disputeResolve` | Resolve a transaction dispute |
| Resume Bulk Charge Batch | `bulkChargeResume` | Resume the processing of a previously paused charge batch |
| Retry Refund | `refundRetry` | Retry a refund with a `needs-attention` status by providing the bank account details of a customer. |
| Send Event | `terminalSendEvent` | Send an event from your application to the Paystack Terminal |
| Send Notification | `paymentRequestNotify` | Trigger an email reminder to a customer for a previously created payment request |
| Send Update Subscription Link | `subscriptionManageEmail` | Email a customer a link for updating the card on their subscription |
| Set Risk Action | `customerRiskAction` | Set customer's risk action by whitelisting or blacklisting the customer |
| Split Dedicated Account Transaction | `dedicatedAccountAddSplit` | Split a dedicated virtual account transaction with one or more accounts |
| Submit Address | `chargeSubmitAddress` | Send the details of the customer's address for address verification |
| Submit Birthday | `chargeSubmitBirthday` | Submit the customer's birthday when requested |
| Submit OTP | `chargeSubmitOtp` | Submit OTP to complete a charge |
| Submit Phone | `chargeSubmitPhone` | Submit phone number when requested |
| Submit PIN | `chargeSubmitPin` | Submit PIN to continue a charge |
| Transaction Totals | `transactionTotals` | Get the total amount of all transactions |
| Trigger Activation Charge | `directdebitTriggerActivationCharge` | Trigger activation charge for specified customers |
| Unassign Destination from Virtual Terminal | `virtualTerminalDestinationUnassign` | Unassign a destination (WhatsApp Number) from a Virtual Terminal on your integration |
| Unregister Domain | `applePayUnregisterDomain` | Unregister a top-level domain or subdomain previously used for your Apple Pay integration. |
| Update Customer | `customerUpdate` | Update a customer's details on your integration |
| Update Dispute | `disputeUpdate` | Update a transaction dispute |
| Update Page | `pageUpdate` | Update a previously created payment page |
| Update Payment Request | `paymentRequestUpdate` | Update a previously created payment request |
| Update Payment Session Timeout | `integrationUpdatePaymentSessionTimeout` | Update the session timeout of a transaction |
| Update Plan | `planUpdate` | Update a plan details on your integration |
| Update product | `productUpdate` | Update a previously created product |
| Update Split | `splitUpdate` | Update a split configuration for transactions |
| Update Storefront | `storefrontUpdate` | Update the details of a previously created Storefront |
| Update Subaccount | `subaccountUpdate` | Update a subaccount details on your integration |
| Update Terminal | `terminalUpdate` | Update the details of a Terminal |
| Update Transfer Recipient | `transferrecipientUpdate` | Update the details of a transfer recipient |
| Update Virtual Terminal | `virtualTerminalUpdate` | Update a Virtual Terminal on your integration |
| Validate Bank Account | `bankValidateAccountNumber` | Confirm the authenticity of a customer's account number before sending money |
| Validate Customer | `customerValidate` | Validate a customer's identity |
| Validate Order | `orderValidate` | Validate a pay for me order |
| Verify Authorization | `customerVerifyAuthorization` | Check the status of an authorization request |
| Verify Payment Request | `paymentRequestVerify` | Verify the status of a previously created payment request |
| Verify Storefront Slug | `storefrontVerifySlug` | Verify the availability of a slug before using it for your Storefront |
| Verify Transaction | `transactionVerify` | Verify a previously initiated transaction using it's reference |
| Verify Transfer | `transferVerify` | Verify the status of a transfer on your integration |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Charge Successful | `charge.success` | A successful charge was made. |
| Customer Identification Failed | `customeridentification.failed` | A customer ID validation has failed. |
| Customer Identification Successful | `customeridentification.success` | A customer ID validation was successful. |
| Dedicated Account Assigned | `dedicatedaccount.assign.success` | A dedicated virtual account was successfully created and assigned to a customer. |
| Dedicated Account Assigned (Legacy) | `assigndedicatedaccount.success` | Legacy event name sent on successful assignment of a dedicated virtual account. |
| Dedicated Account Assignment Failed | `dedicatedaccount.assign.failed` | A dedicated virtual account could not be created for the customer. |
| Dedicated Account Assignment Failed (Legacy) | `assigndedicatedaccount.failed` | Legacy event name sent when a dedicated virtual account could not be assigned. |
| Dispute Created | `charge.dispute.create` | A dispute was logged against your business. |
| Dispute Reminder | `charge.dispute.remind` | A logged dispute has not been resolved. |
| Dispute Resolved | `charge.dispute.resolve` | A dispute has been resolved. |

<details>

<summary>See 15 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Invoice Created | `invoice.create` | An invoice has been created for a subscription, usually 3 days before the charge date. |
| Invoice Payment Failed | `invoice.payment_failed` | A payment for a subscription invoice failed. |
| Invoice Updated | `invoice.update` | An invoice has been updated, usually meaning the customer was charged successfully. |
| Payment Request Paid | `paymentrequest.success` | A payment request has been paid for. |
| Payment Request Pending | `paymentrequest.pending` | A payment request has been sent to a customer. |
| Refund Failed | `refund.failed` | A refund could not be completed. |
| Refund Pending | `refund.pending` | A refund has been logged and is pending. |
| Refund Processed | `refund.processed` | A refund has been completed. |
| Refund Processing | `refund.processing` | A refund is being processed. |
| Subscription Created | `subscription.create` | A subscription has been created. |
| Subscription Disabled | `subscription.disable` | A subscription on your account has been disabled. |
| Subscription Enabled | `subscription.enable` | A subscription on your account has been enabled. |
| Transfer Failed | `transfer.failed` | A transfer you attempted has failed. |
| Transfer Reversed | `transfer.reversed` | A transfer you attempted has been reversed. |
| Transfer Successful | `transfer.success` | A transfer has been completed successfully. |

</details>
