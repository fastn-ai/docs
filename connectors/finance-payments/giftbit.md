---
description: "Giftbit is a digital rewards platform for sending, managing and tracking gift cards and prepaid cards in bulk for incentives, disbursements and employee…"
---

# Giftbit

Giftbit is a digital rewards platform for sending, managing and tracking gift cards and prepaid cards in bulk for incentives, disbursements and employee rewards. This connector wraps the Giftbit Partner API v1 (/papi/v1): credential verification, the brand and region catalogues, the marketplace gift list, account funding and balances, email gift orders (campaigns), direct-link and embedded reward orders, campaign link retrieval, and reward management including listing, retrieving, resending and cancelling individual rewards. The testbed and production hosts are selected by an environment setting on the connection.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [giftbit.com](https://giftbit.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 17 |
| **Events** | 0 |
| **Slug** | `giftbit` |

## Use it

Add Giftbit from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.giftbit.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Funds | `addFunds` | Tops up the Giftbit account balance by charging the credit card already on file for that currency. CHARGES A REAL CREDIT CARD IMMEDIATELY - there is no confirmation step and the charge cannot be reversed through the API. Giftbit enforces a minimum of 25000 cents and a maximum of 1000000 cents per top-up, and the card must first be placed on file through the Giftbit web interface. |
| Cancel Reward | `cancelReward` | Cancels an unclaimed reward and returns its value to the account balance, setting the reward status to GIVER_CANCELLED. Only works while the reward is still unredeemed - a reward the recipient has already claimed cannot be cancelled, and embedded rewards are auto-claimed so they can never be cancelled. |
| Create Direct Link Order | `createDirectLinkOrder` | Places an order for direct link rewards - URLs that go straight to a reward with minimal Giftbit branding and no email. SPENDS REAL MONEY: each link generated is a funded reward drawn from the account balance, even though nothing is emailed. Supply either brand_codes (all from the same region) or a region for the full catalogue. link_count controls how many funded links are created, so a large link_count multiplies the spend. |
| Create Email Order | `createEmailOrder` | Places an order for one or more gift card rewards. SENDS REAL GIFT CARDS WITH REAL MONETARY VALUE and, with the default delivery type, emails every address in contacts immediately - there is no draft or preview state and the spend is deducted from the account balance. DANGEROUS DEFAULT: omitting delivery_type means GIFTBIT_EMAIL, so leaving it blank sends the emails; set delivery_type to SHORTLINK with a link_count to generate claim links you distribute yourself instead, in which case contacts is not used. Check Retrieve Fund Balance first. The id you supply is idempotent on retry, so re-sending the same id will not double-send. |
| Create Embedded Reward | `createEmbeddedReward` | Creates a single reward for immediate in-app delivery and returns a gift_link URL where the recipient reveals their code. SPENDS REAL MONEY: the reward is funded from the account balance as soon as this returns. Embedded rewards are automatically claimed and CANNOT BE CANCELLED, so unlike an email order there is no way to void one afterwards. |
| List Brands | `listBrands` | Lists the gift card brands available to the connected Giftbit account. Use the brand_code returned here when creating any order; call Retrieve Brand for a brand's denominations and region ids. On the testbed the catalogue is a test catalogue and every brand carries a 'For testing purposes only' disclaimer. Note that search and the price filters do narrow the results, but an unrecognised region id or currency code is silently ignored and the full catalogue comes back, so validate those values before relying on the filter. |
| List Marketplace Gifts | `listMarketplaceGifts` | Lists the marketplace gift products available to the connected Giftbit account. This endpoint is not in Giftbit's published API reference but is live on both the testbed and production hosts. |
| List Regions | `listRegions` | Lists the geographic regions Giftbit gift cards can be redeemed in, with the region id used by the region filter on List Brands. |
| List Rewards | `listRewards` | Lists the individual rewards already ordered through Create Email Order, Create Direct Link Order or Create Embedded Reward, with their delivery and redemption status. Supports filtering by order, recipient, price range, delivery status, redemption status and date ranges. All date and time fields Giftbit returns are Pacific Standard Time. |
| Resend Reward | `resendReward` | Re-sends an already-issued reward email to its recipient. SENDS A REAL EMAIL to the recipient of a real gift card and increments the reward's redelivery_count; it issues no new reward and spends no additional funds, but the recipient receives another copy. Note on Giftbit's contract: the resend flag must travel in the JSON body together with the uuid - passing resend=true as a query parameter is rejected with the self-contradicting message "A uuid must be provided. If resending, use resend=true.", which is why this action sends both in the body. |
| Retrieve Brand | `getBrand` | Retrieves a single gift card brand by its brand_code, including the denominations it allows, its currency, the regions it can be redeemed in and its full redemption terms. |
| Retrieve Fund Balance | `getFunds` | Retrieves the connected Giftbit account's balance broken down by currency: funds available to spend, funds pending and funds already reserved against unclaimed rewards. Call this before creating any order, because an order that exceeds the available balance is rejected. |
| Retrieve Marketplace Gift | `getMarketplaceGift` | Retrieves a single marketplace gift product by its numeric id. This endpoint is not in Giftbit's published API reference but is live on both the testbed and production hosts. |
| Retrieve Order | `getOrder` | Retrieves the status and details of a previously placed order, by either the id you assigned when creating it or the uuid Giftbit assigned. |
| Retrieve Order Links | `getOrderLinks` | Retrieves the claim URLs generated by a link-based order - shortlinks from a SHORTLINK email order, or direct links from a direct link order. The URLs are not ready instantly: Giftbit recommends polling every five minutes after the order call succeeds until they appear. |
| Retrieve Reward | `getReward` | Retrieves a single reward by its uuid, including its delivery status, redemption status and how many times it has been resent. Note this is the reward's own uuid, not the uuid or id of the order it came from. |
| Verify Credentials | `ping` | Checks that the connected Giftbit access token is valid and returns the account it belongs to. Use it as a cheap connection health check; it consumes nothing and changes nothing. |
