---
description: "Baremetrics is a subscription analytics and revenue insights platform."
hidden: true
---

# Baremetrics

Baremetrics is a subscription analytics and revenue insights platform. This connector covers the full Baremetrics REST API: account, users, sources, plans, customers, subscriptions, one-off charges and refunds, subscription events, customer attributes and attribute fields, segments, annotations, goals, metrics (summary, per-metric, plan breakout, customer breakdown, cohorts) and Cancellation Insights reasons and events.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [baremetrics.com](https://baremetrics.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 65 |
| **Events** | 0 |
| **Slug** | `baremetrics` |

## Use it

Add Baremetrics from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.baremetrics.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Subscription | `cancelSubscription` | Cancels a Baremetrics subscription at the given time. Returns the resulting subscription.canceled event. |
| Create Annotation | `createAnnotation` | Adds an annotation to a Baremetrics metric chart on a given date, optionally shown on all charts. |
| Create Attribute Field | `createAttributeField` | Creates a custom customer attribute field in Baremetrics. Values for the field are then set on customers with Set Customer Attributes. |
| Create Cancellation Event | `createCancellationEvent` | Records a cancellation event in Baremetrics Cancellation Insights with a reason, optional comment and the affected customer and subscriptions. Requires a Cancellation Insights subscription. |
| Create Cancellation Reason | `createCancellationReason` | Creates a cancellation reason in Baremetrics Cancellation Insights. Requires a Cancellation Insights subscription. |
| Create Charge | `createCharge` | Records a one-off charge against a customer in a Baremetrics source. Note that Subscription OID may only be supplied on accounts where Auto Charging is disabled; accounts with Auto Charging enabled reject it with "Subscription oid cannot be provided". |
| Create Customer | `createCustomer` | Creates a customer record in a Baremetrics API source. After creating the customer you can create subscriptions, charges and refunds for it. |
| Create Goal | `createGoal` | Creates a goal in Baremetrics that tracks a metric from a start amount to a target amount over a date range. Amounts are in cents. |
| Create Plan | `createPlan` | Creates a plan in a Baremetrics API source, for use when creating or updating subscriptions. Amounts are in cents. |
| Create Refund | `createRefund` | Records a refund against a one-off API charge in a Baremetrics API source. This only records revenue data in Baremetrics; no money is moved. Amounts are in cents. |
| Create Segment | `createSegment` | Saves a new customer segment in Baremetrics defined by a list of query conditions. |
| Create Subscription | `createSubscription` | Creates a subscription for an existing customer and plan in a Baremetrics API source. Returns the resulting subscription.created event; metrics are processed asynchronously. |
| Delete Annotation | `deleteAnnotation` | Deletes a Baremetrics chart annotation by annotation ID. The deletion is accepted asynchronously (HTTP 202). |
| Delete Attribute Field | `deleteAttributeField` | Deletes a custom customer attribute field from Baremetrics by field ID. The deletion is accepted asynchronously (HTTP 202). This endpoint is live on the API but not listed in the public reference. |
| Delete Cancellation Reason | `deleteCancellationReason` | Deletes a Baremetrics Cancellation Insights reason by reason ID. Requires a Cancellation Insights subscription. |
| Delete Charge | `deleteCharge` | Deletes a one-off charge from a Baremetrics API source by charge OID. The deletion is accepted asynchronously (HTTP 202). |
| Delete Customer | `deleteCustomer` | Deletes a customer from a Baremetrics API source by customer OID. The deletion is accepted asynchronously (HTTP 202). |
| Delete Goal | `deleteGoal` | Deletes a Baremetrics goal by goal ID. The deletion is accepted asynchronously (HTTP 202). |
| Delete Plan | `deletePlan` | Deletes a plan from a Baremetrics API source by its plan OID. The deletion is accepted asynchronously (HTTP 202). |
| Delete Refund | `deleteRefund` | Deletes a one-off refund from a Baremetrics API source by refund OID. The deletion is accepted asynchronously (HTTP 202). |
| Delete Segment | `deleteSegment` | Deletes a saved Baremetrics customer segment by segment ID. The deletion is accepted asynchronously (HTTP 202). |
| Delete Subscription | `deleteSubscription` | Deletes a subscription from a Baremetrics API source by subscription OID. The deletion is accepted asynchronously (HTTP 202). |
| Get Account | `getAccount` | Retrieves the Baremetrics account linked to the API key, including the company name, default currency and account creation date. |
| Get Annotation | `getAnnotation` | Retrieves a single Baremetrics chart annotation by annotation ID. |
| Get Cancellation Event | `getCancellationEvent` | Retrieves a single Baremetrics Cancellation Insights event by event ID. Requires a Cancellation Insights subscription. |
| Get Cancellation Reason | `getCancellationReason` | Retrieves a single Baremetrics Cancellation Insights reason by reason ID. Requires a Cancellation Insights subscription. |
| Get Charge | `getCharge` | Retrieves a single charge from a Baremetrics source by charge OID, including amount, fee, status and customer. |
| Get Cohorts | `getCohorts` | Returns the Baremetrics customer retention cohort table. The response is an array of cohorts, wrapped under items. |
| Get Customer | `getCustomer` | Retrieves a single customer from a Baremetrics source by customer OID, including LTV, current MRR, status flags and attribute values. |
| Get Event | `getEvent` | Retrieves a single processed subscription event from a Baremetrics source by event ID. |
| Get Goal | `getGoal` | Retrieves a single Baremetrics goal by goal ID. |
| Get Metric | `getMetric` | Returns daily values for a single Baremetrics metric over a date range, each compared with the value a set number of days earlier, including any chart annotations. |
| Get Metric Customers | `getMetricCustomers` | Returns the customers that make up a given metric over a date range, with each customer's contribution. Only count-based customer metrics are supported (for example new_customers, churned_customers, upgrades, downgrades, cancellations, reactivations); value-based metrics such as mrr and arr are rejected by Baremetrics with an HTTP 200 body of {"error":"Cannot be performed on this metric"}. |
| Get Metric Plan Breakout | `getMetricPlanBreakout` | Breaks a Baremetrics metric down by plan across a date range, showing each plan's contribution. |
| Get Metrics Summary | `getMetricsSummary` | Returns a daily summary of every Baremetrics metric (MRR, ARR, ARPU, LTV, churn, customers, trials and more) for each day in the given date range. |
| Get Plan | `getPlan` | Retrieves a single plan from a Baremetrics source by its plan OID, including pricing amounts, billing interval and trial settings. |
| Get Refund | `getRefund` | Retrieves a single refund from a Baremetrics source by refund OID, including the refunded charge and customer. |
| Get Segment | `getSegment` | Retrieves a single saved Baremetrics customer segment by segment ID. |
| Get Subscription | `getSubscription` | Retrieves a single subscription from a Baremetrics source by subscription OID, including its customer, plan, MRR and start and cancellation dates. |
| Get User | `getUser` | Retrieves a single Baremetrics account user by user ID. |
| List Annotations | `listAnnotations` | Lists the annotations added to Baremetrics metric charts, including the metric, date, text and the user who added each one. |
| List Attribute Fields | `listAttributeFields` | Lists the custom customer attribute fields defined in Baremetrics, with their type and title. |
| List Cancellation Events | `listCancellationEvents` | Lists recorded cancellation events in Baremetrics Cancellation Insights, including the chosen reason and customer comment. Requires a Cancellation Insights subscription. |
| List Cancellation Reasons | `listCancellationReasons` | Lists the cancellation reasons configured in Baremetrics Cancellation Insights. Requires a Cancellation Insights subscription. |
| List Charges | `listCharges` | Lists charges in a Baremetrics source, optionally filtered by date range, customer OID or subscription OID. |
| List Customer Events | `listCustomerEvents` | Lists the subscription events (new, upgrade, downgrade, cancellation, reactivation and similar) recorded for a single Baremetrics customer. |
| List Customers | `listCustomers` | Lists customers in a Baremetrics source, with optional search across OID, email, notes and name, and sorting by LTV or creation date. |
| List Events | `listEvents` | Lists processed subscription events (such as new subscriptions, upgrades, downgrades and cancellations) in a Baremetrics source, optionally limited to live-stream events or a date range. |
| List Goals | `listGoals` | Lists the revenue and growth goals configured in Baremetrics, with their metric, target amounts and date range. |
| List Plans | `listPlans` | Lists the plans in a Baremetrics source, optionally filtered by a search term that matches the plan name or OID. |
| List Refunds | `listRefunds` | Lists refunds in a Baremetrics source, optionally filtered by date range. |
| List Segment Fields | `listSegmentFields` | Returns the fields that can be used to build or search Baremetrics customer segments, grouped by category, with each field's type, allowed comparison methods and options. |
| List Segments | `listSegments` | Lists the saved customer segments in Baremetrics, including each segment's name and query conditions. |
| List Sources | `listSources` | Lists the data sources connected to the Baremetrics account (for example Stripe, Recurly or the Baremetrics API source). The source ID is required by plan, customer, subscription, charge, refund and event actions. |
| List Subscriptions | `listSubscriptions` | Lists subscriptions in a Baremetrics source, optionally restricted to one customer and ordered newest or oldest first. Returns 404 when the customer OID filter matches no customer. |
| List Users | `listUsers` | Lists the users who have access to the Baremetrics account, with their name, email and admin flag. Supports page-based pagination. |
| Search Segment | `searchSegment` | Runs an ad-hoc customer segment query in Baremetrics without saving it, returning the matching customers, pagination and segment metrics. |
| Set Customer Attributes | `setCustomerAttributes` | Creates or updates custom attribute values on one or more Baremetrics customers, identified by customer OID or email. Works across all sources. |
| Update Attribute Field | `updateAttributeField` | Renames a custom customer attribute field in Baremetrics. Only the title can be changed. |
| Update Cancellation Event | `updateCancellationEvent` | Updates the reason or comment of a Baremetrics Cancellation Insights event. Requires a Cancellation Insights subscription. |
| Update Cancellation Reason | `updateCancellationReason` | Updates the text or sort position of a Baremetrics Cancellation Insights reason. Requires a Cancellation Insights subscription. |
| Update Customer | `updateCustomer` | Updates the basic information stored on a Baremetrics customer, such as name, email, notes and creation date. Only the fields you supply are changed. |
| Update Plan | `updatePlan` | Renames a plan in a Baremetrics API source. Only the plan name can be changed. |
| Update Segment | `updateSegment` | Updates the name and/or query conditions of a saved Baremetrics customer segment. Only the fields you supply are changed. |
| Update Subscription | `updateSubscription` | Updates a Baremetrics subscription, for example to change its plan, quantity, discount or add-ons. Returns the resulting subscription.updated event. |
