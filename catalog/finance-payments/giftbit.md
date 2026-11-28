---
description: "Giftbit is a digital rewards platform. Send gift card rewards by email or link, cancel rewards and manage funds."
hidden: true
---

# Giftbit

<img src="../../.gitbook/assets/connectors/lg/giftbit.png" alt="Giftbit logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [giftbit.com](https://giftbit.com) |
| **Authentication** | API key |
| **Slug** | `giftbit` |

## Setup

Your customers enter their API key for Giftbit when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Giftbit from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Giftbit**.
2. Select **Connect** on the Giftbit card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Giftbit's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Funds</td><td><code>addFunds</code></td><td>Tops up the Giftbit account balance by charging the credit card already on file for that currency. CHARGES A REAL CREDIT CARD IMMEDIATELY - there is no confirmation step and the charge cannot be reversed through the API. Giftbit enforces a minimum of 25000 cents and a maximum of 1000000 cents per top-up, and the card must first be placed on file through the Giftbit web interface.</td></tr><tr><td>Cancel Reward</td><td><code>cancelReward</code></td><td>Cancels an unclaimed reward and returns its value to the account balance, setting the reward status to GIVER_CANCELLED. Only works while the reward is still unredeemed - a reward the recipient has already claimed cannot be cancelled, and embedded rewards are auto-claimed so they can never be cancelled.</td></tr><tr><td>Create Direct Link Order</td><td><code>createDirectLinkOrder</code></td><td>Places an order for direct link rewards - URLs that go straight to a reward with minimal Giftbit branding and no email. SPENDS REAL MONEY: each link generated is a funded reward drawn from the account balance, even though nothing is emailed. Supply either brand_codes (all from the same region) or a region for the full catalogue. link_count controls how many funded links are created, so a large link_count multiplies the spend.</td></tr><tr><td>Create Email Order</td><td><code>createEmailOrder</code></td><td>Places an order for one or more gift card rewards. SENDS REAL GIFT CARDS WITH REAL MONETARY VALUE and, with the default delivery type, emails every address in contacts immediately - there is no draft or preview state and the spend is deducted from the account balance. DANGEROUS DEFAULT: omitting delivery_type means GIFTBIT_EMAIL, so leaving it blank sends the emails; set delivery_type to SHORTLINK with a link_count to generate claim links you distribute yourself instead, in which case contacts is not used. Check Retrieve Fund Balance first. The id you supply is idempotent on retry, so re-sending the same id will not double-send.</td></tr><tr><td>Create Embedded Reward</td><td><code>createEmbeddedReward</code></td><td>Creates a single reward for immediate in-app delivery and returns a gift_link URL where the recipient reveals their code. SPENDS REAL MONEY: the reward is funded from the account balance as soon as this returns. Embedded rewards are automatically claimed and CANNOT BE CANCELLED, so unlike an email order there is no way to void one afterwards.</td></tr><tr><td>List Brands</td><td><code>listBrands</code></td><td>Lists the gift card brands available to the connected Giftbit account. Use the brand_code returned here when creating any order; call Retrieve Brand for a brand's denominations and region ids. On the testbed the catalogue is a test catalogue and every brand carries a 'For testing purposes only' disclaimer. Note that search and the price filters do narrow the results, but an unrecognised region id or currency code is silently ignored and the full catalogue comes back, so validate those values before relying on the filter.</td></tr><tr><td>List Marketplace Gifts</td><td><code>listMarketplaceGifts</code></td><td>Lists the marketplace gift products available to the connected Giftbit account. This endpoint is not in Giftbit's published API reference but is live on both the testbed and production hosts.</td></tr><tr><td>List Regions</td><td><code>listRegions</code></td><td>Lists the geographic regions Giftbit gift cards can be redeemed in, with the region id used by the region filter on List Brands.</td></tr><tr><td>List Rewards</td><td><code>listRewards</code></td><td>Lists the individual rewards already ordered through Create Email Order, Create Direct Link Order or Create Embedded Reward, with their delivery and redemption status. Supports filtering by order, recipient, price range, delivery status, redemption status and date ranges. All date and time fields Giftbit returns are Pacific Standard Time.</td></tr><tr><td>Resend Reward</td><td><code>resendReward</code></td><td>Re-sends an already-issued reward email to its recipient. SENDS A REAL EMAIL to the recipient of a real gift card and increments the reward's redelivery_count; it issues no new reward and spends no additional funds, but the recipient receives another copy. Note on Giftbit's contract: the resend flag must travel in the JSON body together with the uuid - passing resend=true as a query parameter is rejected with the self-contradicting message "A uuid must be provided. If resending, use resend=true.", which is why this action sends both in the body.</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Retrieve Brand</td><td><code>getBrand</code></td><td>Retrieves a single gift card brand by its brand_code, including the denominations it allows, its currency, the regions it can be redeemed in and its full redemption terms.</td></tr><tr><td>Retrieve Fund Balance</td><td><code>getFunds</code></td><td>Retrieves the connected Giftbit account's balance broken down by currency: funds available to spend, funds pending and funds already reserved against unclaimed rewards. Call this before creating any order, because an order that exceeds the available balance is rejected.</td></tr><tr><td>Retrieve Marketplace Gift</td><td><code>getMarketplaceGift</code></td><td>Retrieves a single marketplace gift product by its numeric id. This endpoint is not in Giftbit's published API reference but is live on both the testbed and production hosts.</td></tr><tr><td>Retrieve Order</td><td><code>getOrder</code></td><td>Retrieves the status and details of a previously placed order, by either the id you assigned when creating it or the uuid Giftbit assigned.</td></tr><tr><td>Retrieve Order Links</td><td><code>getOrderLinks</code></td><td>Retrieves the claim URLs generated by a link-based order - shortlinks from a SHORTLINK email order, or direct links from a direct link order. The URLs are not ready instantly: Giftbit recommends polling every five minutes after the order call succeeds until they appear.</td></tr><tr><td>Retrieve Reward</td><td><code>getReward</code></td><td>Retrieves a single reward by its uuid, including its delivery status, redemption status and how many times it has been resent. Note this is the reward's own uuid, not the uuid or id of the order it came from.</td></tr><tr><td>Verify Credentials</td><td><code>ping</code></td><td>Checks that the connected Giftbit access token is valid and returns the account it belongs to. Use it as a cheap connection health check; it consumes nothing and changes nothing.</td></tr></tbody></table>

</details>

