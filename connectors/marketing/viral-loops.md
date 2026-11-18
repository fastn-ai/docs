---
description: "Viral Loops referral-marketing platform."
hidden: true
---

# Viral Loops

Viral Loops referral-marketing platform. Covers the full Backend API v3: campaign stats and campaign configuration, participant registration/edit/search/query/flag/convert, participant data, rank, order, referrals and referrer, pending and given rewards and reward redemption, plus the undocumented participant count, participant delete and campaign list routes. Participant records are personal data.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [viral-loops.com](https://viral-loops.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 19 |
| **Events** | 3 |
| **Slug** | `viralLoops` |

## Use it

Add Viral Loops from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.viralLoops.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Participant | `convertParticipant` | Mark a participant as converted from your backend, optionally attaching a monetary value to the conversion event. Identify by email or referralCode. Conversion may release referral rewards to the referrer. |
| Delete Participant | `deleteParticipant` | Permanently delete a participant (lead) from the campaign by email address. Undocumented but live route. Requires the lead-deletion entitlement on the Viral Loops plan; accounts without it get 403 'You're not allowed to delete leads'. Deletion cannot be undone. |
| Edit Participant | `editParticipant` | Update an existing participant's first name, last name, referral count, conversion count or custom fields. Identify by email or referralCode. Leave sendEmails false to avoid mailing the participant and triggerIntegrations false to avoid firing campaign integrations. |
| Flag Participant | `flagParticipant` | Flag one or more participants as fraudulent so they stop counting toward referral totals and rewards. Pass an array of participant identifiers, each with an email or a referralCode. |
| Get Campaign Info | `getCampaignInfo` | Get the full campaign configuration: name, company, template, live flag, rewarding and milestone setup, widget styling, DOI, captcha, integrations and text codes. Takes no input; the API token scopes the campaign. |
| Get Campaign Stats | `getCampaignStats` | Get the lead count and total referral count of the campaign the API token belongs to. Takes no input. |
| Get Given Rewards | `getGivenRewards` | List the rewards that have already been redeemed/given to a participant. Identify by email or referralCode; omit both to list given rewards across the campaign. |
| Get Participant Count | `getParticipantCount` | Get the total number of participants in the campaign. Undocumented but live route. Takes no input. |
| Get Participant Data | `getParticipantData` | Get a participant's full profile: name, email, referral code, rank, referral counts, points, referrer, redeemed and pending rewards. Identify the participant by either email or referralCode (supply exactly one). PERSONAL DATA: the response contains the participant's email address. |
| Get Participant Order | `getParticipantOrder` | Get the join order of a participant (1 = joined first) together with the campaign lead count. Identify by email or referralCode. |
| Get Participant Rank | `getParticipantRank` | Get a participant's leaderboard rank, total referral count and points total. Identify by email or referralCode. Returns an empty object if the participant does not exist. |
| Get Participant Referrals | `getParticipantReferrals` | List the people a participant has referred, with join date, conversion status and reward earned. Identify the referrer by email or referralCode; page with limit and offset and filter with conversionStatus. PERSONAL DATA: returns referred people's email addresses. |
| Get Participant Referrer | `getParticipantReferrer` | Get the referrer record of a participant, including the referrer's referral code and the full campaign settings snapshot. Identify by email or referralCode. Returns 406 'Invalid Participant identifier' when the participant has no referrer or does not exist. PERSONAL DATA and SENSITIVE: the response embeds campaignSettingsJson, which includes the campaign captcha secret when one is configured. |
| Get Pending Rewards | `getPendingRewards` | List the rewards a participant has earned but not yet redeemed. Identify by email or referralCode; omit both to list pending rewards for every participant. Returns an empty array when the campaign has no rewarding configured. |
| List Campaigns | `listCampaigns` | List every campaign on a Viral Loops account. Undocumented but live route. It is the only route that is NOT scoped by the campaign apiToken: it takes an account-level apiKey as a query parameter, which is a different credential from the connection's campaign API token. Without a valid account apiKey the vendor answers 406 'Invalid user identifier'. |
| Query Participants | `queryParticipants` | Look up specific participants and/or everyone referred by specific referrers, in one call. Pass participants and/or referrers as arrays of identifiers (email or referralCode) and page with filter.limit and filter.skip. PERSONAL DATA: returns email addresses and unique referral links. |
| Redeem Reward | `redeemReward` | Mark one of a participant's pending rewards as redeemed. Get the rewardId from Get Pending Rewards. Identify the participant by email or referralCode. CAUTION: redemption is irreversible and, on a campaign with rewarding emails enabled, notifies the participant. |
| Register Participant | `registerParticipant` | Register a new participant in the campaign and get their referral code back. Pass referrerReferralCode to record who referred them. CAUTION: this enrols a real person and, on a campaign with an email service configured, triggers the campaign's welcome/referral emails. Disposable-email domains are rejected with 451. |
| Search Participants | `searchParticipants` | Search and page the campaign's participants, filtering by free-text search term, conversion status or acquisition source. PERSONAL DATA: returns email addresses, fraud/risk scores and custom fields. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Milestone Reached | `milestoneReached` | Fires when a participant reaches a referral milestone, carrying the milestone and the rewards it unlocked. MANUAL REGISTRATION (Viral Loops has no webhook registration API): log in to Viral Loops &gt; click the Edit button on your campaign &gt; Integrations in the bottom navigation &gt; Webhook &gt; turn on the milestone event &gt; paste this trigger's URL into the milestone endpoint field &gt; Save. PAYLOAD SCHEMA SOURCE: modelled from the vendor's documented example at developers.viral-loops.com/docs/milestone-reached, not from a captured live delivery. |
| Participation | `participation` | Fires when someone joins the campaign, carrying the new participant and, for a referred signup, their referrer. MANUAL REGISTRATION (Viral Loops has no webhook registration API): log in to Viral Loops &gt; click the Edit button on your campaign &gt; Integrations in the bottom navigation &gt; Webhook &gt; turn on 'When someone joins your campaign, you can send their submitted data to a webhook' &gt; paste this trigger's URL into 'Endpoint for participation event' &gt; optionally click 'Send a test request' &gt; Save. PAYLOAD SCHEMA SOURCE: modelled from the vendor's documented example at developers.viral-loops.com/docs/participation, not from a captured live delivery. |
| Reward Redeemed | `rewardRedeemed` | Fires when a participant's reward is redeemed, carrying the reward id, name and redemption timestamp. MANUAL REGISTRATION (Viral Loops has no webhook registration API): log in to Viral Loops &gt; click the Edit button on your campaign &gt; Integrations in the bottom navigation &gt; Webhook &gt; turn on the reward-redeemed event &gt; paste this trigger's URL into the reward endpoint field &gt; Save. PAYLOAD SCHEMA SOURCE: modelled from the vendor's documented example at developers.viral-loops.com/docs/reward-redeemed, not from a captured live delivery. |
