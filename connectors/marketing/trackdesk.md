---
description: "Trackdesk affiliate and partner tracking platform."
hidden: true
---

# Trackdesk

<img src="../../.gitbook/assets/connectors/lg/trackdesk.png" alt="Trackdesk logo">

Trackdesk affiliate and partner tracking platform. Manage offers, affiliates, conversions, clicks, coupons, tracking links, tiers, tags, advertisers, billing settlements and reporting through the Trackdesk public API.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [trackdesk.com](https://trackdesk.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `trackdesk` |

## Use it

Add Trackdesk from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.trackdesk.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add offer cap source limit | `addOfferCapSourceLimit` | Add offer cap source limit. Sets a per-source limit override for an existing offer cap. Overrides the default source limit for a specific affiliate source. |
| Advertiser open balance | `listRevenueOriginOpenBalances` | Advertiser open balance. Get information about current open balance per individual advertiser. |
| Affiliate overview report | `affiliateOverviewReport` | Affiliate overview report. Deprecated: Shows data related to individual affiliates and their performance. |
| Build Tracking Link | `buildTrackingLink` | BuildTrackingLink. Build a tracking link |
| Check payment batch status | `checkPaymentBatchStatus` | Check payment batch status. Checks status of a specific Tipalti payment batch of given settlement and refreshes the payment data of the settlement. This should be used only if there is need to manually synchronize payment data with new state in Tipalti system. You can then see the refreshed data in SettlementService.GetSettlement endpoint. |
| Check the presented credential | `oauth2CheckCredential` | Check the presented credential. Checks whether an access token or API key is valid. Revoked authorizations, deleted clients and disabled accounts are rejected. |
| Click report | `clickReport` | Click report. Provides information about registered clicks. |
| Conversion report | `conversionReport` | Conversion report. Shows data related to conversions tracked by the system. |
| Country overview | `countryOverviewReport` | Country overview. Deprecated: Displays performance data grouped by specific countries. |
| Create a new payment method | `createPaymentMethod` | Create a new payment method. Creates a new payment method for the affiliate account. Once created, it can be set as a default payment method using `SetPaymentMethodAccountDefault` endpoint. |

<details>

<summary>See 99 more actions</summary>

* **Create Account Note** `createAccountNote`: Create account note. Creates a new note attached to a specific affiliate account. - Errors: may use ERROR_CODE_ACCOUNT_NOT_FOUND when account_id does not exist.
* **Create advertiser settlement** `claimBalances`: Create advertiser settlement. Generates a settlement for specific advertiser.
* **Create Affiliate** `createAffiliate`: Create new affiliate. Creates a new affiliate in your system.
* **Create affiliate bonus** `createAffiliateBonus`: Create affiliate bonus. Creates a standalone bonus in one of the currencies configured for the tenant.
* **Create Affiliate Registration Data** `createAffiliateRegistrationData`: Create affiliate registration data. Create affiliate registration data for the affiliate.
* **Create Affiliate Tier** `createTier`: Create affiliate tier. Creates a new affiliate tier in the system.
* **Create Click** `createClick`: Create click. Creates a new click in the system.
* **Create client** `createClient`: Create client. Create client associated with the click.
* **Create client metric movement** `createClientMetricMovement`: Create client metric movement. Records metric values for a client identified by external_client_id. Duplicate requests with the same request_id are silently ignored.
* **Create Conversion** `createConversion`: Create conversion. Create a new conversion in the system.
* **Create conversion** `createConversion2`: Create conversion. Create a new conversion in the system.
* **Create Coupon** `createCoupon`: Create a new coupon.. Creates a new coupon in the system.
* **Create landing pages** `createLandingPages`: Create landing pages. Creates one or more landing pages for an offer. Each landing page declares either a direct or redirect tracking link. All landing pages in a single request must use the same link type.
* **Create new advertiser** `createRevenueOrigin`: Create new advertiser. Creates a new advertiser in your system.
* **Create Offer** `createOffer`: Create offer. Creates an offer with the supplied configuration, pricing and landing pages, and publishes it. All landing pages must use the same link type (either all direct or all redirect). By default the offer is published immediately; set `publish_at` to schedule it to go live at a future time instead. Returns the created offer together with its pricing and landing pages.
* **Create offer cap** `createOfferCap`: Create offer cap. Creates a new conversion cap for an offer. The cap defines daily, weekly or monthly limits on conversions (by count or revenue), optionally split by source, with a fallback redirect when the cap is reached.
* **Create Offer Creative** `createOfferCreative`: Create offer creative. Adds a single content-based creative (HTML, text link, external video or post) to the offer and returns it with its generated id. File-based creatives (image banners, videos, ZIP archives) are added through the creative upload endpoint instead.
* **Create or refresh an access token** `oauth2CreateToken`: Create or refresh an access token. OAuth2 token endpoint for the client_credentials, authorization_code, and refresh_token grants. Confidential clients authenticate with HTTP Basic or client_id and client_secret form fields, using exactly one method. Authorization codes require the original redirect_uri and PKCE code_verifier. Refresh tokens are rotated on every use.
* **Create settlement** `settleBalances`: Create settlement. Creates a new settlement for selected affiliates covering balances up to the specified date.
* **Create Tag** `createTag`: Create new tag. Creates a new tag in the system.
* **Create Tipalti payment batch** `createPaymentBatch`: Create Tipalti payment batch. Sends new payment batch to Tipalti system for specified settlement. Account settlements of the specified settlement are included in the payment batch only if it has Tipalti payment method, is still unpaid and Tipalti payee corresponding to the account settlement's affiliate is in payable state.
* **Create Webhook** `createWebhook`: Create a new webhook. Creates new webhooks in the system.
* **Daily overview report** `dailyOverviewReport`: Daily overview report. Features overview of the daily performance, providing data such as clicks, conversions, revenue, payouts etc. per given day.
* **Delete Account Note** `deleteAccountNote`: Delete account note. Removes a note by its unique identifier.
* **Delete advertiser settlement** `deleteClaim`: Delete advertiser settlement. Deletes the selected advertiser settlement.
* **Delete Affiliate** `deleteAffiliate`: Delete affiliate. Deletes affiliate from the system.
* **Delete affiliate bonus** `deleteAffiliateBonus`: Delete affiliate bonus. Deletes an unsettled affiliate bonus.
* **Delete affiliate settlement** `deleteAccountSettlement`: Delete affiliate settlement. Deletes settlement for specific affiliate without deleting the entirety of a single settlement.
* **Delete Affiliate Tier** `deleteTier`: Delete affiliate tier. Deletes a specific affiliate tier. A tier cannot be deleted if affiliates are still assigned to it. Default tier cannot be deleted.
* **Delete Coupon** `deleteCoupon`: Delete coupon. Delete an existing coupon from the system.
* **Delete offer cap** `deleteOfferCap`: Delete offer cap. Permanently removes a conversion cap from an offer by its ID.
* **Delete offer creative** `deleteOfferCreative`: Delete offer creative. Removes a single creative identified by its id from the offer.
* **Delete settlement** `deleteSettlement`: Delete settlement. Delete the entirety of a single settlement. This might include settlements of multiple affiliates.
* **Delete Tag** `deleteTag`: Delete tag. Deletes a tag from the system.
* **Delete Webhook** `deleteWebhook`: Delete webhook. Deletes a specific webhook from the system.
* **General overview** `generalOverviewReport`: General overview. Provides a comprehensive performance overview with data aggregated at multiple levels (such as daily, country, affiliate, offer, etc.).
* **Get advertiser settlement** `getClaim`: Get advertiser settlement. Provides details of specific advertiser settlement details.
* **Get Affiliate** `getAffiliate`: Affiliate details. Get detailed information about a specific affiliate.
* **Get affiliate bonus** `getAffiliateBonus`: Get affiliate bonus. Returns an affiliate bonus by id.
* **Get Affiliate Registration Data** `getAffiliateRegistrationData`: Affiliate registration data. Get the data the affiliate filled in during registration.
* **Get Affiliate Tier** `getTier`: Affiliate tier detail. Returns the detail of specific affiliate tier with the payout rates.
* **Get balances for account** `getBalancesForAccount`: Get balances for account. Retrieves balance breakdown for a specific affiliate including open, on-hold, and settled amounts.
* **Get default timezone** `getDefaultTimezone`: Get default timezone. Returns the default timezone configured in the general settings of the tenant.
* **Get Offer** `getOffer`: Get offer. Retrieves an offer together with its pricing and landing pages, in the same shape returned by create.
* **Get settlement** `getSettlement`: Get settlement. Get information about the settlement.
* **Get Tag** `getTag`: Get tag details. Provides details of existing tag in the system.
* **List Account Notes** `listAccountNotes`: List account notes for account. Lists notes for a given affiliate account ordered by creation time.
* **List advertiser settlements** `listClaims`: List advertiser settlements. Provides a list of existing advertiser settlements.
* **List advertisers** `listRevenueOrigins`: List advertisers. List the existing advertisers in your system.
* **List affiliate bonuses** `listAffiliateBonuses`: List affiliate bonuses. Lists affiliate bonuses with optional affiliate, settlement, and creation date filters.
* **List affiliate settlements** `listAccountSettlements`: List affiliate settlements. Lists all settlements for a specific affiliate or all affiliates.
* **List Affiliate Tiers** `listTiers`: List affiliate tiers. Returns a list of active affiliate tiers and their associated payout rates.
* **List Affiliates** `listAffiliates`: List affiliates. List the existing affiliates in your system.
* **List affiliates assignments to offer** `listAffiliateAssignmentsToOffer`: List affiliates assignments to offer. Lists the affiliate assignments to the offer, each together with its access level, assignment time and any pending application details.
* **List client metric movements** `listClientMetricMovements`: List client metric movements. Returns a paginated list of metric movements matching the given filters.
* **List client metrics** `listClientMetrics`: List client metrics. Returns all integer and decimal metrics defined for the revenue origin.
* **List Conversion Types For Click** `listConversionTypesForCid`: List conversion types available for CID. Provides a list of conversion types that are available for the requesting click identifier (CID)
* **List Coupons** `listCoupons`: List coupons. Returns a list of all existing coupons in the system.
* **List landing pages by offer** `listLandingPages`: List landing pages by offer. Lists all landing pages assigned to an offer. Each item carries either direct or redirect tracking link metadata.
* **List offer caps** `listOfferCaps`: List offer caps. Returns all conversion caps configured for a specific offer, including their limits, current utilization, and source-specific overrides.
* **List Offer Creatives** `listOfferCreatives`: List offer creatives. Lists the promotional creatives configured for this offer, each identified by its unique id.
* **List Offers** `listOffers`: List offers. Lists offers matching the given filters, each returned together with its pricing and landing pages, in the same shape returned by create.
* **List open balances** `listOpenBalances`: List open balances. Lists open balances for affiliates with details about conversion and commission amounts by status.
* **List open balances** `listOpenBalances2`: List open balances. Lists open balances for affiliates with details about conversion and commission amounts by status.
* **List payable account settlements of a settlement** `listPayableAccountSettlements`: List payable account settlements of a settlement. Retrieve list of payable and unpaid account settlements via Tipalti.
* **List settlements** `listSettlements`: List settlements. List all existing settlements in the selected timeframe.
* **List supported payment method types** `listSupportedPaymentMethodTypes`: List supported payment method types. Returns all payment method types enabled in the system along with their supported currencies.
* **List Tags** `listTags`: List tags. Lists all tags in the system.
* **List Webhooks** `listWebhooks`: List active webhooks. Returns a list of currently active webhooks.
* **Offer overview** `offerOverviewReport`: Offer overview. Deprecated: Shows performance overview grouped by individual offers.
* **Prioritize landing pages** `prioritizeLandingPages`: Prioritize landing pages. Sets the priority order used to pick which redirect landing page an offer serves to a visitor. When a redirect tracking link is clicked, the offer's redirect landing pages are matched against the visitor's location, language, device and operating system. Among the pages whose targeting rules match, the one appearing earliest in `ordered_landing_page_ids` is chosen as the single redirect destination — earlier position means higher priority. Landing pages omitted from the list rank below every listed page. For this reason, order landing pages from the most specific targeting rules to the most general, so a broad catch-all page cannot win ahead of a more specific page that also matches the visitor. Only redirect landing pages use this ordering; direct landing pages are unaffected.
* **Redeem Coupon** `redeemCoupon`: Redeem coupon. Looks up the affiliate associated with any of the provided coupon codes and returns a coupon redemption identifier (CID) for conversion attribution.
* **Register an OAuth client** `oauth2RegisterClient`: Register an OAuth client. RFC 7591 dynamic client registration, so a client can obtain a client_id without anyone entering one by hand. Registration is unauthenticated and rate limited per IP. It always produces a public client holding no secret, limited to the authorization_code and refresh_token grants, and owned by nobody: the client can do nothing at all until a resource owner authorizes it on the consent screen. A registration nobody consents to is deleted within two hours. A client asking to authenticate with a secret is registered with none instead, as the response says. Other metadata that cannot be honoured is refused rather than silently narrowed; anything else the request sends is ignored.
* **Remove offer cap source limit** `removeOfferCapSourceLimit`: Remove offer cap source limit. Removes the per-source limit override for a specific source on an offer cap, reverting it to the cap's default source limit.
* **Revoke an OAuth grant** `oauth2RevokeToken`: Revoke an OAuth grant. RFC 7009-style revocation endpoint accepting either an access token or a refresh token. Whichever is presented, revocation takes the complete user authorization behind it, including rotated refresh tokens and every access token derived from the grant. Access tokens issued through client_credentials cannot be revoked individually; they return unsupported_token_type. Delete the client to invalidate its access tokens. Unknown tokens return success. Confidential clients authenticate as at the token endpoint.
* **Set affiliate access to offer** `setAffiliatesAccessToOffer`: Set affiliate access to offer. Sets the access level (allowed or forbidden) of one or more affiliate sources on the offer, creating an assignment for sources that are not yet assigned and updating the access level of those that already are. Returns the resulting assignments.
* **Set affiliate billing status** `setAffiliateBillingStatus`: Set affiliate billing status. Lets you change the billing status of an affiliate. Affiliates with an excluded billing status are left out of open balances and settlements.
* **Set Affiliate Status** `setAffiliateStatus`: Set affiliate status. Lets you change the status of an affiliate.
* **Set Affiliate Tier** `setAffiliateTier`: Set affiliate tier. Set a tier for the selected affiliates.
* **Set billing detail** `setBillingDetail`: Set billing detail. Fill in the billing details for affiliate's account.
* **Set Conversion Status** `setConversionStatus`: Set conversion status. Change the status of an already existing conversion.
* **Set Conversion Status By External ID** `setConversionStatusByExternalId`: Change conversion status by External ID. Update the status of conversions by matching with external ID (see [Conversion sources](#tag--tracking.v1.ConversionSourceService) for more details).
* **Set External Click ID** `setExternalCid`: Set external CID. Adds external click identifier to a conversion.
* **Test Webhook** `testWebhook`: Test webhook response. Triggers specific webhook to test functionality and sent data.
* **Update advertiser** `updateRevenueOrigin`: Update advertiser. Update the advertiser in your system.
* **Update affiliate bonus** `updateAffiliateBonus`: Update affiliate bonus. Replaces the editable fields of an unsettled affiliate bonus. The affiliate cannot be changed.
* **Update affiliate settlement status** `updateAccountSettlementStatus`: Update affiliate settlement status. Updates the status of a single affiliate settlement. Manual status change is forbidden for Tipalti settlements, and the ERROR status cannot be set manually.
* **Update Affiliate Tier** `updateTier`: Update affiliate tier. Updates the values of selected affiliate tier.
* **Update client** `updateClient`: Update client. Updates mutable fields of a client. Fields absent from the request are left unchanged.
* **Update client metric name** `updateClientMetricName`: Update client metric name. Updates the display name of an existing client metric.
* **Update client metric visibility** `updateClientMetricVisibility`: Update client metric visibility. Controls whether the metric is visible in the UI.
* **Update Conversion** `updateConversion`: Update conversion. Update selected properties of a conversion.
* **Update conversion** `updateConversion2`: Update conversion. Update selected properties of a conversion.
* **Update landing page** `updateLandingPage`: Update landing page. Updates an existing landing page. The link type provided must match the landing page's existing link type.
* **Update Offer** `updateOffer`: Update offer. Updates the offer's general settings (name, visibility, targeting, tags, description, ...) and its status. Provide the full new settings; the offer's pricing and landing pages are left untouched and are updated through their own endpoints. Returns the updated offer.
* **Update offer creative** `updateOfferCreative`: Update offer creative. Updates the editable fields (content, name, note, visibility) of a single creative identified by its id. The creative's type, uploaded file and metadata are left unchanged.
* **Update Offer Pricing** `updateOfferPricing`: Update offer pricing. Updates the pricing settings of the offer (conversion type settings and targeting groups). Returns the updated pricing.
* **Update payment method** `updatePaymentMethod`: Update payment method. Updates the data for selected payment method.
* **Upload offer creative** `uploadOfferCreative`: Upload offer creative. Upload a promotional creative whose content is a file and attach it to the offer in a single request. This is the file-based counterpart to the offer creatives service, which manages the content-based creatives and also lists, edits and removes the creatives created here. Send the request as `multipart/form-data`, with the binary in the `file` field and the creative's metadata in the remaining fields. The file size is measured server-side; the pixel width and height may be supplied by the caller for image and video creatives. Set `creativeId` to replace the file of an existing creative instead of creating a new one. Returns the created or replaced creative together with its metadata.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Advertiser Claim Created | `EVENT_TYPE_CLAIM_CREATED` | Fires when an advertiser settlement claim is created. Payload captured from Trackdesk's own test-event sample. |
| Affiliate Created | `EVENT_TYPE_AFFILIATE_CREATED` | Fires when a new affiliate is registered. Payload captured from Trackdesk's own POST /api/node/webhooks/v1/test sample for this event type. |
| Affiliate Registration Data Created | `EVENT_TYPE_AFFILIATE_REGISTRATION_DATA_CREATED` | Fires when an affiliate submits application/registration answers. Payload captured from Trackdesk's own test-event sample. |
| Affiliate Status Changed | `EVENT_TYPE_AFFILIATE_STATUS_CHANGED` | Fires when an affiliate is enabled, disabled or set pending. Payload captured from Trackdesk's own test-event sample. |
| Affiliate Ticket Created | `EVENT_TYPE_AFFILIATE_TICKET_CREATED` | Fires when an affiliate opens a ticket. Payload captured from Trackdesk's own test-event sample. |
| Affiliate Ticket Updated | `EVENT_TYPE_AFFILIATE_TICKET_UPDATED` | Fires when an affiliate ticket changes. Payload captured from Trackdesk's own test-event sample. |
| Affiliate Tier Changed | `EVENT_TYPE_AFFILIATE_TIER_CHANGED` | Fires when an affiliate is moved to a different commission tier. Payload captured from Trackdesk's own test-event sample. |
| Click Created | `EVENT_TYPE_CLICK_CREATED` | Fires on every tracked click. Payload captured from Trackdesk's own test-event sample. |
| Conversion Created | `EVENT_TYPE_CONVERSION_CREATED` | Fires when a conversion is recorded. Payload captured from Trackdesk's own test-event sample. |
| Conversion Status Changed | `EVENT_TYPE_CONVERSION_STATUS_CHANGED` | Fires when a conversion is approved, rejected, refunded or otherwise re-statused. Payload captured from Trackdesk's own test-event sample. |

<details>

<summary>See 2 more events</summary>

* **Coupon Created** `EVENT_TYPE_COUPON_CREATED`: Fires when a coupon code is created for an affiliate on an offer. Payload captured from Trackdesk's own test-event sample.
* **Settlement Created** `EVENT_TYPE_SETTLEMENT_CREATED`: Fires when an affiliate settlement (payout batch) is created. Payload captured from Trackdesk's own test-event sample.

</details>
