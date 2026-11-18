---
description: "Checkout.com Unified Payments API."
---

# Checkout.com

Checkout.com Unified Payments API. Request, capture, void, refund and reverse card payments; manage customers, saved instruments, payment links, hosted payment pages, payment sessions (Flow), payment contexts and setups; look up payment methods and card metadata; handle disputes and evidence files; and build risk and notification workflows with events and reflows. The API base URL is per-merchant and per-environment, so it is supplied on the connection.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [checkout.com](https://checkout.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 64 |
| **Events** | 0 |
| **Slug** | `checkoutCom` |

## Use it

Add Checkout.com from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.checkoutCom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Dispute | `acceptDispute` | Accept a dispute, conceding the chargeback and returning the funds to the cardholder. This action cannot be undone. |
| Add Workflow Action | `addWorkflowAction` | Add an action, such as a webhook, to a workflow. |
| Add Workflow Condition | `addWorkflowCondition` | Add a condition, such as an event or entity filter, to a workflow. |
| Cancel a Payment | `cancelPayment` | Cancel a payment that has not yet been captured. Voids the authorization and releases the held funds. |
| Capture a Payment | `capturePayment` | Capture a previously authorized payment, in full or in part, to settle the funds. |
| Confirm Payment Setup | `confirmPaymentSetup` | Confirm a payment setup for a specific payment method to finalize storing the customer's payment details. |
| Create and Submit Payment Session | `createAndSubmitPaymentSession` | Create a payment session and immediately submit it, processing the payment in a single request. Requires session_data captured by the Flow front-end component. |
| Create Customer | `createCustomer` | Create a customer that payment instruments and future payments can be associated with. |
| Create Hosted Payments Page Session | `createHostedPaymentsPage` | Create a Hosted Payments Page session and receive the redirect URL to send the customer to in the _links.redirect field. |
| Create Instrument | `createInstrument` | Save a payment instrument to the vault so it can be reused for future payments. Set type to token to store a Checkout.com token, or to card, bank_account, sepa or ach to store the underlying details. Provide either processing_channel_id or entity_id. |
| Create Payment Context | `createPaymentContext` | Create a payment context for an alternative payment method, returning the details needed to complete the customer's journey. |
| Create Payment Link | `createPaymentLink` | Create a shareable payment link that a customer can open to complete a payment on a Checkout.com hosted page. Returns the redirect URL in the _links.redirect field. |
| Create Payment Session | `createPaymentSession` | Create a Checkout.com Flow payment session, returning the session ID, token and secret used to render the Flow front-end component. |
| Create Payment Setup | `createPaymentSetup` | Create a payment setup to determine the available payment methods and store a customer's payment details for future merchant-initiated transactions. |
| Create Workflow | `createWorkflow` | Create a workflow that triggers actions such as webhooks when events matching its conditions occur. On NAS accounts the API requires an entity condition listing your ent_ identifiers alongside the event condition. |
| Delete Customer | `deleteCustomer` | Permanently delete a customer and detach their saved payment instruments. |
| Delete Instrument | `deleteInstrument` | Permanently remove a saved payment instrument from the vault. |
| Delete Workflow | `deleteWorkflow` | Permanently delete a workflow and stop it from triggering. |
| Get Card Metadata | `getCardMetadata` | Look up metadata for a card BIN, full card number or token, including scheme, card type, issuer and country. |
| Get Customer Details | `getCustomer` | Retrieve a customer's details and their saved payment instruments, by customer ID or email address. |
| Get Dispute Details | `getDispute` | Retrieve the full details of a dispute, including its reason code, amount, deadline and related payment. |
| Get Dispute Scheme Files | `getDisputeSchemeFiles` | Retrieve the card scheme files associated with a dispute. |
| Get File Details | `getFile` | Retrieve the details of an uploaded file, including its name, size, purpose and a temporary download link. |
| Get Hosted Payments Page Details | `getHostedPaymentsPage` | Retrieve the details and current status of a Hosted Payments Page session. |
| Get Instrument Details | `getInstrument` | Retrieve the details of a saved payment instrument, including its type, card metadata and linked customer. |
| Get Payment Context | `getPaymentContext` | Retrieve the details of a previously created payment context. |
| Get Payment Details | `getPayment` | Retrieve the full details of a payment, including its status, source, amount, currency and processing information. |
| Get Payment Link Details | `getPaymentLink` | Retrieve the details and current status of a payment link. |
| Get Payment Setup | `getPaymentSetup` | Retrieve the details and status of a payment setup. |
| Get Submitted Dispute Arbitration Evidence | `getDisputeSubmittedArbitrationEvidence` | Retrieve the arbitration evidence that has already been submitted for a dispute. |
| Get Submitted Dispute Evidence | `getDisputeSubmittedEvidence` | Retrieve the evidence that has already been submitted for a dispute. |
| Get Token Metadata | `getTokenMetadata` | Retrieve metadata associated with a card token, such as the scheme, expiry and issuer details. |
| Get Workflow | `getWorkflow` | Retrieve a workflow's full configuration, including its conditions and actions. |
| Get Workflow Action Invocations | `getWorkflowActionInvocations` | Retrieve the invocation attempts for a workflow action against a specific event, including request and response details. |
| Get Workflow Event | `getWorkflowEvent` | Retrieve the details of a workflow event, including its payload and the workflows it triggered. |
| Increment Payment Authorization | `incrementPaymentAuthorization` | Increase the authorized amount of an existing card authorization before it is captured. |
| List Disputes | `listDisputes` | Retrieve a paginated list of disputes, optionally filtered by status, payment, date range or entity. |
| List Event Types | `listEventTypes` | Retrieve all event types available for workflow conditions, grouped by source, with their display names and descriptions. |
| List Payment Actions | `listPaymentActions` | Retrieve the history of actions performed against a payment, such as authorization, capture, refund and void. |
| List Payment Methods | `listPaymentMethods` | Retrieve the payment methods enabled and available for a given processing channel. |
| List Payments | `listPayments` | Retrieve the payments matching a given reference. A reference is required; use Search Payments for richer filtering. |
| List Subject Events | `listSubjectEvents` | Retrieve all workflow events associated with a subject, such as a payment or dispute ID. |
| List Workflows | `listWorkflows` | Retrieve all workflows configured on the account, with their conditions and actions. |
| Provide Dispute Evidence | `provideDisputeEvidence` | Attach evidence to a dispute. Evidence is only sent to the scheme once you submit it with Submit Dispute Evidence. File fields take a file ID returned by Upload File. |
| Reflow Event | `reflowByEvent` | Reprocess a single event through all workflows whose conditions it matches. |
| Reflow Event by Workflow | `reflowByEventAndWorkflow` | Reprocess a single event through one specific workflow. |
| Reflow Events | `reflowEvents` | Reprocess a set of events through their matching workflows, or through specific workflows. |
| Reflow Subject Events | `reflowBySubject` | Reprocess all events for a subject, such as a payment, through their matching workflows. |
| Reflow Subject Events by Workflow | `reflowBySubjectAndWorkflow` | Reprocess all events for a subject through one specific workflow. |
| Refund a Payment | `refundPayment` | Refund a captured payment, in full or in part, returning the funds to the cardholder. |
| Remove Workflow Action | `removeWorkflowAction` | Remove an action from a workflow. |
| Remove Workflow Condition | `removeWorkflowCondition` | Remove a condition from a workflow. |
| Request a Payment | `requestPayment` | Request a card payment. Provide a source (card, token, saved instrument id, customer or network token) with the currency and amount. Set capture to false to authorize only, then settle later with Capture a Payment. A processing_channel_id is required. |
| Reverse a Payment | `reversePayment` | Reverse a payment, voiding the authorization or refunding the capture depending on its settlement state. |
| Search Payments | `searchPayments` | Search for payments using a query expression, optional date range and pagination cursor. Returns matching payments with their status and amounts. |
| Submit Payment Session | `submitPaymentSession` | Submit an existing payment session for processing once the customer has selected their payment method in Flow. |
| Update Customer | `updateCustomer` | Update a customer's email, name, phone or default payment instrument. Only the fields you provide are changed. |
| Update Instrument | `updateInstrument` | Update a saved payment instrument's expiry date, name, account holder or customer association. Only the fields you provide are changed. |
| Update Payment Setup | `updatePaymentSetup` | Update an existing payment setup with revised amount, currency, customer or order details. |
| Update Workflow | `updateWorkflow` | Update a workflow's name or enabled state. |
| Update Workflow Action | `updateWorkflowAction` | Update an existing action on a workflow. |
| Update Workflow Condition | `updateWorkflowCondition` | Update an existing condition on a workflow. |
| Upload File | `uploadFile` | Upload a file to use as dispute evidence. Returns the file ID to reference when providing evidence. |
| Void a Payment | `voidPayment` | Void an authorized but uncaptured payment, releasing the funds held on the cardholder's card. |
