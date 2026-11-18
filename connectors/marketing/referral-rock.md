---
description: "Referral Rock is a referral, affiliate and partner marketing platform."
hidden: true
---

# Referral Rock

<img src="../../.gitbook/assets/connectors/lg/referral-rock.png" alt="Referral Rock logo">

Referral Rock is a referral, affiliate and partner marketing platform. This connector covers the complete Referral Rock REST API (https://api.referralrock.com): referral programs, members (referrers) and their statistics, referrals, rewards and reward rules, payouts and payout transactions, referral actions for recurring rewards, the customer feed that approves matching referrals, pre-authenticated member access and share URLs, the email unsubscribe list, and webhook subscription management with delivery history. Authentication is HTTP Basic using your Referral Rock public key as the username and private key as the password.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [referralrock.com](https://referralrock.com) |
| **Authentication** | Basic auth |
| **Slug** | `referralRock` |

## Use it

Add Referral Rock from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.referralRock.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Member | `createMember` | Creates a new member (referrer) and adds them to a referral program, returning the created member with the referral code and share URLs they can start sharing. Set Should Send Email to true to send the program's confirmation email to the new member; leave it false to create the member silently. |
| Create Member Access (Deprecated) | `createMemberAccess` | Deprecated by Referral Rock: use Create Member Access URLs instead, which takes separate typed fields for each way of finding the member. This version takes a single free-form member query and returns the same set of pre-authenticated portal and share URLs. Note: Referral Rock returns the Facebook and Telegram keys with a trailing space in the key name ("facebookShareUrl " and "telegramShareUrl "); the output contract reproduces them verbatim. |
| Create Member Access URLs | `createMemberAccessUrls` | Generates a set of short-lived, pre-authenticated URLs for one member so you can embed the Referral Rock member portal or share widget in your own product, or build a custom share experience. Identify the member by internal ID, referral code, email address or external ID. The URLs expire after Expire In Minutes, which defaults to 20. Note: Referral Rock returns the Facebook and Telegram keys with a trailing space in the key name ("facebookShareUrl " and "telegramShareUrl "); the output contract reproduces them verbatim. |
| Create Referral | `createReferral` | Adds a referral to a referral program, attributing it to the member whose referral code you supply. Optionally set the referral's contact details, order amount, status, address, custom fields and assigned recruiter. Returns the created referral. |
| Create Referral Action | `createReferralAction` | Records a referral action against an existing referral, such as a renewal or repeat purchase, so that recurring percentage-based rewards can be calculated from its amount. Identify the referral by its ID, email address or external identifier, and supply an external identifier of your own to prevent duplicate actions being recorded. |
| Create Rewards | `createRewards` | Creates rewards for members and referrals of a referral program. The request body is a JSON array, so several rewards can be created in one call. Each element identifies the recipient with a member query and/or a referral query and describes the reward to create. Creating a reward does not pay it out; use Issue Reward or Issue Payout Transactions for that. Check each element's resultInfo.Status rather than relying on the 200 status alone. |
| Create Webhook Subscription | `createWebhookSubscription` | Subscribes a URL of yours to one Referral Rock event, so Referral Rock posts the event payload to that URL whenever it occurs. Returns the subscription's web_hook_id, which is what Delete Webhook Subscription needs to unsubscribe. Subscribe once per event you want to receive. |
| Delete Members | `deleteMembers` | Permanently deletes members from a referral program. The request body is a JSON array, so several members can be deleted in one call. Each element identifies one member with a query object. The response echoes each query alongside a resultInfo whose Status is 'Succeeded' or 'Failed' per member, so check every element rather than relying on the 200 status alone. |
| Delete Members (DELETE Verb) | `deleteMembersViaDelete` | Permanently deletes members from a referral program using the HTTP DELETE verb. Identical in body and response to Delete Members, which uses POST; Referral Rock exposes both verbs on the same route so clients that cannot send a POST for a delete still have a path. Check each element's resultInfo.Status rather than relying on the 200 status alone. |
| Delete Referrals | `deleteReferrals` | Permanently deletes referrals from a referral program. The request body is a JSON array, so several referrals can be deleted in one call. Each element identifies one referral with a query object. The response echoes each query with a resultInfo whose Status is 'Success' or 'Failed' per element, so check every element rather than relying on the 200 status alone. |

<details>

<summary>See 30 more actions</summary>

* **Delete Referrals (DELETE Verb)** `deleteReferralsViaDelete`: Permanently deletes referrals from a referral program using the HTTP DELETE verb. Identical in body and response to Delete Referrals, which uses POST; Referral Rock exposes both verbs on the same route. Check each element's resultInfo.Status rather than relying on the 200 status alone.
* **Delete Rewards** `deleteRewards`: Permanently deletes rewards from members or referrals of a referral program. The request body is a JSON array of reward IDs, so several rewards can be deleted in one call. The response returns one element per ID with a resultInfo whose Status must be checked, because a 200 can still carry a Failed outcome such as "Reward Id does not exist".
* **Delete Rewards (DELETE Verb)** `deleteRewardsViaDelete`: Permanently deletes rewards using the HTTP DELETE verb. Identical in body and response to Delete Rewards, which uses POST; Referral Rock exposes both verbs on the same route. Check each element's resultInfo.Status rather than relying on the 200 status alone.
* **Delete Webhook Subscription** `deleteWebhookSubscription`: Unsubscribes from a Referral Rock event by the web_hook_id returned when the subscription was created. After this, Referral Rock stops posting that event to your URL.
* **Get Member Statistics** `getMemberStats`: Retrieves sharing, referral and reward statistics for a single member over a chosen time period. Identify the member by email address, internal ID, external ID or referral code. Both the query and the time period are required; omitting the time period makes the route unresolvable. Returns 400 with "Member query found no matches" when no member matches.
* **Get Program** `getProgram`: Retrieves a single referral program by its name, returning the program's ID, active flag, type, title, member and referral offer text, and its direct and widget URLs.
* **Get Referral** `getReferral`: Retrieves a single referral by its email address, Referral Rock referral ID or your own external identifier. At least one of the three must be supplied. Returns the full referral record including status, amount, attribution to the referring member, custom fields, address, UTM data and recruiter assignment.
* **Issue Payout Transactions** `issuePayoutTransactions`: Pays out every pending reward of one payout type, optionally narrowed to one recipient, transferring real money. Returns one result per issued payout. Note: Referral Rock answers 500 with an empty body when Recipient ID is a well-formed but non-existent identifier; supply a recipient that exists, or omit it to pay all recipients for the payout type.
* **Issue Reward** `issueReward`: Issues a single pending reward to its recipient, moving real value to a real person. Optionally attach a note for the recipient, and set Override Ineligible to issue a reward whose eligibility date has not yet arrived. Returns the reward after the attempt along with a resultInfo whose Status must be checked, because a 200 can still carry a Failed outcome.
* **List Members** `listMembers`: Lists the members (referrers) of your referral programs, ordered by create date, with each member's contact details, referral code and share URLs, sharing and referral counters, reward totals and recruiter assignment. Filter by program, by a free-text query matching email, internal ID, external ID or referral code, by disabled state or by create-date range, and page with offset and count.
* **List Payout Transactions** `listPayoutTransactions`: Lists payout transactions already transferred to participants of your referral programs, with amount, currency, destination, status and any vendor error, plus the account balance remaining to fulfil pending payouts. Filter by recipient or by a single transaction ID.
* **List Payouts** `listPayouts`: Lists the payout types configured in your Referral Rock account, each with its description, payout method and the programs it applies to. Supply a payout ID to return just that one.
* **List Pending Payouts** `listPendingPayouts`: Lists payouts that are owed but not yet transferred to a participant, grouped by payout type and recipient, with the number of rewards rolled up and the total amount due. Filter by recipient, and optionally include payouts whose rewards have a future eligibility date.
* **List Programs** `listPrograms`: Lists the referral programs in your Referral Rock account, with each program's name, title, type, member and referral offer text, and its direct and widget URLs. Narrow to one program with programId, and page with offset and count.
* **List Referrals** `listReferrals`: Lists referrals (leads introduced by your members), ordered by create date, with contact details, status, amount, attribution to the referring member, custom fields, UTM data and recruiter assignment. Filter by program, by a free-text query, by referring member, by status or by create-date range, and page with offset and count.
* **List Reward Rules** `listRewardRules`: Lists the member reward rules configured on a referral program: what triggers a reward, how its amount is calculated, which payout type it uses, and how and when it is delivered. Returns a bare JSON array of rule objects.
* **List Rewards** `listRewards`: Lists rewards owed to or already issued to members and referrals, ordered by create date, with amount, currency, status, payout type, recipient details and the reward rule that generated it. Filter by program, member, recipient query, status or create-date range, and page with offset and count.
* **List Unsubscribed Emails** `listUnsubscribedEmails`: Returns the email addresses that have unsubscribed from your Referral Rock emails. Supply an email address to check whether that one address is unsubscribed. The response is a bare JSON array.
* **List Webhook History** `listWebhookHistory`: Returns the stored delivery history for one Referral Rock webhook event, newest first, with each item shaped exactly like the payload the webhook posts. Use it to replay or reconcile events you may have missed. Counts above 5000 are capped at 5000; a non-integer or value below 1 falls back to the default of 25.
* **List Webhook History (Legacy)** `listWebhookHistoryLegacy`: Deprecated by Referral Rock: use List Webhook History instead, which returns each event in the same shape the webhook posts and supports a count parameter. This legacy version returns the stored delivery history for one Referral Rock event in the older format.
* **Remove Email Unsubscribe** `removeEmailUnsubscribe`: Removes an email address from your Referral Rock unsubscribe list, so Referral Rock emails can be sent to it again. Only re-subscribe an address with the recipient's consent.
* **Remove Email Unsubscribe (DELETE Verb)** `removeEmailUnsubscribeViaDelete`: Removes an email address from your Referral Rock unsubscribe list using the HTTP DELETE verb. Identical in body and response to Remove Email Unsubscribe, which uses POST; Referral Rock exposes both verbs on the same route.
* **Submit Customer** `submitCustomerFeed`: Submits one customer to the Referral Rock customer feed. If the email matches a pending referral, that referral is approved and updated with the customer's details; otherwise the customer is pre-loaded as a member. Use it to close the loop from your billing or CRM system so referral conversions are attributed automatically. The response reports the engine's per-record outcome in status and statusCategory.
* **Submit Customers** `submitCustomerFeeds`: Submits a batch of customers to the Referral Rock customer feed in one call. Each customer whose email matches a pending referral approves and updates that referral; the rest are pre-loaded as members. The response returns one result per submitted record, in the order sent, with the engine's per-record status and statusCategory.
* **Submit Invite Contact (Deprecated)** `submitInviteFeed`: Deprecated by Referral Rock: use Submit Customer instead. Submits a contact to the invite feed with a first name, last name, email and optional contact type declaring which API event the contact originates from.
* **Unsubscribe Email** `unsubscribeEmail`: Adds an email address to your Referral Rock unsubscribe list so that no further Referral Rock emails are sent to it. Use Remove Email Unsubscribe to reverse it.
* **Update Members** `updateMembers`: Updates one or more members of a referral program. The request body is a JSON array, so several members can be updated in one call. Each element pairs a query that identifies the member with a member object holding only the fields to change; omitted fields are left untouched. The response echoes each query with the updated member and a resultInfo whose Status is 'Success' or 'Failed' per element, so check every element rather than relying on the 200 status alone.
* **Update Referral Status (Deprecated)** `updateReferralStatus`: Deprecated by Referral Rock: use Update Referrals instead, which can change status and every other referral field in one batched call. This endpoint sets the status of a single referral and can optionally set its amount and public note.
* **Update Referrals** `updateReferrals`: Updates one or more referrals in a referral program, including moving a referral between the pending, qualified, approved and denied statuses. The request body is a JSON array, so several referrals can be updated in one call. Each element pairs a query that identifies the referral with a referral object holding only the fields to change. This replaces the deprecated Update Referral Status action.
* **Update Rewards** `updateRewards`: Updates existing rewards in a referral program, changing the amount, the payout type, the eligibility date or the description. The request body is a JSON array, so several rewards can be updated in one call, each identified by its reward ID.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Email Unsubscribed | `EmailUnsubscribed` | Fires when an email address is added to your Referral Rock unsubscribe list. Schema modelled from the blocklist entry the REST API returns from Get Unsubscribed Emails; not captured from a live delivery. |
| Member Added | `MemberAdd` | Fires when a member (referrer) is added to a referral program, whether created through the API, the share page or automatically when a referral is approved. Payload schema captured from a real Referral Rock delivery (GET /api/hooks/history/MemberAdd). |
| Member Deleted | `MemberDelete` | Fires when a member is deleted from a referral program. Carries the same member payload as Member Added. Schema modelled on the captured MemberAdd delivery, not captured for this event specifically. |
| Member Updated | `MemberUpdate` | Fires when a member's details change. Carries the same member payload as Member Added. Schema modelled on the captured MemberAdd delivery, not captured for this event specifically. |
| Program Added | `ProgramAdd` | Fires when a referral program is created. Schema modelled from the Program object the REST API returns; not captured from a live delivery, because programs can only be created in the Referral Rock interface. |
| Referral Added | `ReferralAdd` | Fires when a referral is added to a referral program. Payload schema captured from a real Referral Rock delivery (GET /api/v2/hooks/history/ReferralAdd). |
| Referral Deleted | `ReferralDelete` | Fires when a referral is deleted from a referral program. Carries the same referral payload as Referral Added. Schema modelled on the captured ReferralAdd delivery, not captured for this event specifically. |
| Referral Status Changed | `ReferralStatusChange` | Fires when a referral moves between the pending, qualified, approved and denied statuses. Carries the same referral payload as Referral Added. Schema modelled on the captured ReferralAdd delivery, not captured for this event specifically. |
| Referral Updated | `ReferralUpdate` | Fires when an existing referral is changed. Carries the same referral payload as Referral Added. Schema modelled on the captured ReferralAdd delivery, not captured for this event specifically. |
| Reward Added | `RewardAdd` | Fires when a reward is created for a member or a referral. Schema modelled from the Reward object the REST API returns; not captured from a live delivery, because the sandbox account has no payout type configured and so cannot generate a reward. |

<details>

<summary>See 1 more event</summary>

* **Reward Issued** `RewardIssue`: Fires when a reward is issued to its recipient. Schema modelled from the Reward object the REST API returns; not captured from a live delivery, because the sandbox account has no payout type configured and so cannot issue a reward.

</details>
