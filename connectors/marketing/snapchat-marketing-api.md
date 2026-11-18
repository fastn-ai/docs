---
description: "Snapchat Marketing API connector covering the Ads API (organizations, ad accounts, funding sources, billing centers, members and roles, campaigns, ad squads,…"
hidden: true
---

# Snapchat Marketing API

<img src="../../.gitbook/assets/connectors/lg/snapchat-marketing-api.png" alt="Snapchat Marketing API logo">

Snapchat Marketing API connector covering the Ads API (organizations, ad accounts, funding sources, billing centers, members and roles, campaigns, ad squads, ads, creatives, creative elements, media, catalogs, product feeds and product sets, audience segments, pixels, mobile apps, lead generation forms, interaction zones, dynamic templates, targeting reference data, measurement and stats reporting, invoices and transactions, and the Ads Library), the Public Profile API (profiles, stories, saved stories, spotlights, lenses, snaps, metrics, roles, sharing policies, and messaging), and the Conversions API for server-to-server event tracking.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [snapchat.com](https://snapchat.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `snapchatMarketingApi` |

## Use it

Add Snapchat Marketing API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.snapchatMarketingApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Chunked Media Part | `addChunkedMediaPart` | Uploads one part of a chunked media upload. Supply the add path returned by Initialize Chunked Media Upload, without the https://adsapi.snapchat.com prefix. Parts may be uploaded in any order or in parallel. |
| Add Profile Media Part | `addProfileMediaPart` | Uploads one part of an encrypted Public Profile media file. Supply the add path returned when the upload was initialized, without the https://businessapi.snapchat.com prefix. |
| Add Users To Audience Segment | `addUsersToSegment` | Adds hashed user identifiers to a customer list audience segment. Send one schema type per request and at most 100000 identifiers. Normalize each identifier before hashing: lower-case and trim emails, lower-case mobile advertising IDs while keeping hyphens, and reduce phone numbers to digits with the country code and no leading zeros. Hash with SHA-256 and send lower-case hex. |
| Cancel Partnership | `deleteProfileRole` | Cancels a creator partnership, revoking the creator's ability to tag the brand and the brand's ability to read their content or run ads as their profile. Pass the creator's invitee user identifier, taken from List Profile Roles, as the role identifier. |
| Claim Media By Ad Code | `claimMediaByAdCode` | Claims a creator's organic Snap into an ad account using the ad code the creator generated in the Snapchat app, so the content can be used to build a creative. Poll Get Media until media_status is READY before referencing it. |
| Claim Media By Snap ID | `claimMediaBySnapId` | Claims a Snap into an ad account by its Snap ID, the API equivalent of Promote Snap in the Snapchat app and Profile Manager. The caller needs permission on both the ad account and the Snap's profile. |
| Combine Snaps | `combineSnaps` | Merges a multi-segment Story into a single ad-ready video asset. Supply one Snap ID per bundle and Snapchat fetches the related Snaps from the same longform content; all Snaps must share a resolution. Poll Get Media on the returned identifier, and retry if it is still not ready after 60 minutes. |
| Copy Media | `copyMedia` | Copies up to 20 READY video or image media objects into another ad account in the same organization. Lens media cannot be copied. The request is not atomic, so a partial success is possible and the response lists a status per requested copy in the order they were sent. |
| Create Ad | `createAd` | Creates an ad inside an ad squad by pairing a creative with that squad. Create it PAUSED and activate it deliberately, because an ACTIVE ad in an ACTIVE squad starts delivering as soon as review passes. Creating many ads from the same creative within a second is rate limited, so use bulk requests instead. |
| Create Ad Account | `createAdAccount` | Creates an ad account inside the specified organization. Set regulations.restricted_delivery_signals for credit, housing or employment advertising, payingAdvertiserName for political advertising, and the agency fields when an agency buys on behalf of a client based in or targeting France. |

<details>

<summary>See 245 more actions</summary>

* **Create Ad Account Role** `createAdAccountRole`: Assigns an ad account role to a member. The member must already hold the member role in the organization that owns the ad account.
* **Create Ad Engagement Audience** `createAdEngagementSegment`: Creates an audience of Snapchatters who took a specific action on ads in this ad account, campaign or ad squad. Each engagement spec is combined with OR, which is the only supported operator.
* **Create Ad Squad** `createAdSquad`: Creates an ad squad inside a campaign. The ad squad owns the targeting, budget, bid, placement and schedule for the ads beneath it. Create it PAUSED and activate it deliberately, because an ACTIVE ad squad with a budget begins spending as soon as its ads are approved.
* **Create Ad Squad Outcome Estimate** `createAdSquadOutcomeEstimate`: Estimates the daily and weekly reach, conversions, impressions and leftover budget for one or more proposed ad squads before they are created.
* **Create Billing Center** `createBillingCenter`: Creates a billing center under the specified organization. The billing center is the contact address that receives invoices for the ad accounts assigned to it.
* **Create Campaign** `createCampaign`: Creates a campaign inside an ad account. An ad account holds at most 100 campaigns. Create the campaign PAUSED and activate it deliberately, because an ACTIVE campaign with a budget begins spending as soon as its ad squads and ads are approved.
* **Create Catalog** `createCatalog`: Creates a product catalog under an organization. Requires the organization admin role. A catalog holds up to 10 million items, and an organization holds at most 200 catalogs.
* **Create Catalog Role** `createCatalogRole`: Assigns a catalog role to a member. The member must already hold the member role in the organization that owns the catalog.
* **Create Creative** `createCreative`: Creates a creative in an ad account. Supply the attachment property block that matches the creative type: webViewProperties for WEB_VIEW, appInstallProperties for APP_INSTALL, deepLinkProperties for DEEP_LINK, adToLensProperties for AD_TO_LENS, adToCallProperties for AD_TO_CALL, adToMessageProperties for AD_TO_MESSAGE, reminderProperties for REMINDER, previewProperties for PREVIEW, compositeProperties for COMPOSITE and collectionProperties for COLLECTION.
* **Create Creative Elements** `createCreativeElements`: Creates one or more creative elements in an ad account. Creative elements are the individual tiles combined into a Collection Ad through an interaction zone, which needs at least four of them.
* **Create Customer List Audience** `createCustomerListSegment`: Creates a first-party customer list audience segment in an ad account. Members are added afterwards with Add Users To Audience Segment. An ad account holds at most 1000 customer list segments.
* **Create Dynamic Template** `createDynamicTemplate`: Creates a dynamic template in an ad account. The CAROUSEL and SLIDESHOW layouts require the creative to be a Collection Ad. The available text fields depend on the catalog vertical.
* **Create Event Details** `createEventDetails`: Creates an Event Details entity describing the calendar event a Reminder creative promotes. The entity is immutable once created, so none of its attributes can be edited afterwards. The start time is interpreted as UTC, so offset it yourself for the event's own region and daylight saving.
* **Create Feed Upload** `createFeedUpload`: Triggers a one-off upload of a product feed file. Only feeds without a schedule accept on-demand uploads. REPLACE swaps the whole feed for the new file, while UPSERT adds and updates the products in the file and preserves everything else - to remove items with UPSERT, include a delete column in the file.
* **Create Interaction Zone** `createInteractionZone`: Creates an interaction zone in an ad account, grouping at least four creative elements into the tile strip of a Collection Ad. The interaction zone headline replaces the creative call to action for collection creatives.
* **Create Lead Webhook Integration** `createLeadWebhookIntegration`: Registers a webhook that Snapchat calls with the lead data every time a user submits the specified lead generation form. Only one integration is allowed per form and the caller needs the organization admin role. The response carries an HMAC secret used to verify the Signature header on delivered events.
* **Create Leads Report** `createLeadsReport`: Requests an asynchronous export of the leads collected in an ad account over a time window, and returns a report run identifier to poll with Get Leads Report.
* **Create Lookalike Audience** `createLookalikeSegment`: Creates a lookalike audience segment from a first-party customer list seed. The lookalike keeps updating as identifiers are added to the seed segment.
* **Create Media** `createMedia`: Creates a media container in an ad account. The media stays PENDING_UPLOAD until the file itself is uploaded with Upload Media, after which it becomes READY and can be referenced by creatives.
* **Create Mobile App Custom Conversion** `createMobileAppCustomConversion`: Creates a custom conversion on a Snap App ID by filtering a standard app event on parameter values.
* **Create Mobile App Events Audience** `createMobileAppEventsSegment`: Creates a mobile app custom audience from events reported against a Snap App ID connected to the ad account. The audience updates dynamically as events are reported, and prefill is always enabled so events recorded before creation are included.
* **Create Offer Disclaimer** `createOfferDisclaimer`: Creates an offer disclaimer in an ad account. Use STATIC to render the supplied disclaimer text, or DYNAMIC to render the offer_details field from a product catalog on Dynamic Product Ads. Offer disclaimers are not supported on Spotlight placements or on Collection Ads built from a catalog.
* **Create Organization Role** `createOrganizationRole`: Assigns an organization-level role to a member. Every member needs an organization role, and the member role is a prerequisite for any ad account or catalog role.
* **Create Pixel Custom Conversion** `createPixelCustomConversion`: Creates a custom conversion on a Snap Pixel by filtering a standard event on parameter values. Rule keys use Snap Pixel parameter names, so when events arrive through the Conversions API map the custom_data field you send to the matching rule key.
* **Create Product Feed** `createProductFeed`: Creates a product feed under a catalog, optionally with a schedule that tells Snapchat how often to re-fetch the file. Without a schedule you upload the file on demand with Create Feed Upload.
* **Create Product Set** `createProductSet`: Creates a product set in a catalog from a filter. A property name may appear only once in the filter, the ID property accepts up to 1000 values with IS_ANY or I_IS_ANY, and every other field accepts at most 15. Splitting values across duplicate blocks to bypass the limit is rejected.
* **Create Profile Engagement Audience** `createProfileEngagementSegment`: Creates an audience of Snapchatters who subscribe to or engage with a creator's Public Profile. Requires an accepted AD_LEVEL partnership with the creator - a BRAND_LEVEL partnership does not grant audience targeting. Segments below 1000 users report a targetable status of TOO_FEW_USERS but can still seed a lookalike.
* **Create Profile Media** `createProfileMedia`: Creates an encrypted media container on a Public Profile and returns the media identifier used for the chunked upload. Encrypt the file yourself and pass the base64-encoded 32-byte key and 16-byte initialisation vector used to encrypt it.
* **Create Profile Role** `createProfileRole`: Invites a creator into a partnership with a brand profile, or grants an internal collaborator a role. AD_LEVEL lets the creator tag the brand with the Paid Partnership label and lets the brand run ads that appear as the creator's profile; BRAND_LEVEL covers only the tagging. The caller must hold the Profile Admin role, and inviting a creator who already has an active role returns DUPLICATE_ROLE.
* **Create Reach And Frequency Forecast** `createReachAndFrequencyForecast`: Requests a reach curve for a proposed reach and frequency ad squad, showing the estimated reach for a given budget. Reach and frequency buying is a beta available on a whitelist basis; the forecast requires a minimum reach of 500000 unique users, booking between 12 hours and 365 days ahead, and does not permit radius or location-of-interest targeting. Feed the returned impression, reach and budget values straight into Create Ad Squad.
* **Create Segment Sharing Policy** `createSegmentSharingPolicy`: Shares an audience segment with another ad account or organization.
* **Create Sharing Policy** `createSharingPolicy`: Shares a pixel, Public Profile, catalog or mobile app with an ad account or organization. Use the parent policy identifier when sharing beyond the organization that owns the resource.
* **Create Website Events Audience** `createWebsiteEventsSegment`: Creates a website custom audience from Snap Pixel or Conversions API events. The audience updates dynamically as Snapchatters trigger the chosen events, and prefill is always enabled so events recorded before creation are included.
* **Delete Ad** `deleteAd`: Deletes an ad. Deleted ads cannot be restored.
* **Delete Ad Squad** `deleteAdSquad`: Deletes an ad squad and every ad beneath it. Deleted ad squads cannot be restored.
* **Delete Audience Segment** `deleteAudienceSegment`: Deletes an audience segment. Deleted segments cannot be retrieved, so use this with care.
* **Delete Campaign** `deleteCampaign`: Deletes a campaign and everything beneath it. Deleted campaigns cannot be restored.
* **Delete Catalog** `deleteCatalog`: Deletes a product catalog and everything in it. Requires the organization admin role and cannot be undone.
* **Delete Event Details** `deleteEventDetails`: Deletes an Event Details entity. There is no way to reinstate a deleted entity, so confirm it is not in use by an active Reminder creative first.
* **Delete Lead Webhook Integration** `deleteLeadWebhookIntegration`: Removes a webhook integration. Snapchat immediately stops sending lead events for the associated form.
* **Delete Member** `deleteMember`: Removes a member from the organization. Delete the member's roles first; removing the member revokes all of their access to the organization and its ad accounts.
* **Delete Offer Disclaimer** `deleteOfferDisclaimer`: Permanently deletes an offer disclaimer.
* **Delete Product Feed** `deleteProductFeed`: Deletes a product feed. This cannot be undone.
* **Delete Product Set** `deleteProductSet`: Deletes a product set. Snapchat exposes this as a PUT against the product set identifier rather than a DELETE.
* **Delete Role** `deleteRole`: Removes a role from an organization, ad account or catalog. When you remove all of a member's roles you should also remove the member from the organization.
* **Delete Sharing Policy** `deleteSharingPolicy`: Revokes a sharing policy, removing the target's access to the shared resource.
* **Discover Creators** `discoverCreators`: Searches Snapchat creators by follower count, country, category and data-sharing permissions. Results are sorted by follower count when filters are supplied without a query, and the total result set is capped at 5000 creators.
* **Extract Snap ID** `extractSnapId`: Converts a Snapchat content URL or short link into the Snap ID needed by Claim Media By Snap ID. Supply either the full URL or just the short code.
* **Finalize Chunked Media Upload** `finalizeChunkedMediaUpload`: Completes a chunked media upload once every part has been uploaded. Supply the finalize path returned by Initialize Chunked Media Upload, without the https://adsapi.snapchat.com prefix.
* **Finalize Profile Media Upload** `finalizeProfileMediaUpload`: Completes an encrypted Public Profile media upload once every part has been uploaded. Supply the finalize path returned when the upload was initialized, without the https://businessapi.snapchat.com prefix.
* **Get Ad** `getAd`: Retrieves a single ad by its identifier.
* **Get Ad Account** `getAdAccount`: Retrieves a single ad account by its identifier.
* **Get Ad Account Stats** `getAdAccountStats`: Returns delivery and conversion metrics for an ad account. Metrics are finalized 48 hours after the end of the day in the ad account timezone. Set async to true for large reports and then poll Get Ad Account Stats Report.
* **Get Ad Account Stats Report** `getAdAccountStatsReport`: Checks the status of an asynchronous ad account stats report and returns the download link once it is complete.
* **Get Ad Squad** `getAdSquad`: Retrieves a single ad squad by its identifier.
* **Get Ad Squad Stats** `getAdSquadStats`: Returns delivery and conversion metrics for an ad squad, optionally broken down to ad level. Metrics are finalized 48 hours after the end of the day in the ad account timezone.
* **Get Ad Squad Stats Report** `getAdSquadStatsReport`: Checks the status of an asynchronous ad squad stats report and returns the download link once it is complete.
* **Get Ad Squad UI Render Data** `getAdSquadUiRenderData`: Retrieves the Ad Squad UI Render Data object attached to a single ad squad.
* **Get Ad Squads By IDs** `getAdSquadsByIds`: Retrieves up to 2000 specific ad squads from the same ad account in one call by passing their identifiers in the request body.
* **Get Ad Stats** `getAdStats`: Returns delivery and conversion metrics for a single ad. Metrics are finalized 48 hours after the end of the day in the ad account timezone.
* **Get Ad Stats Report** `getAdStatsReport`: Checks the status of an asynchronous ad stats report and returns the download link once it is complete.
* **Get Ads By IDs** `getAdsByIds`: Retrieves up to 2000 specific ads from the same ad account in one call by passing their identifiers in the request body.
* **Get Ads Library Ad** `getAdsLibraryAd`: Retrieves the public Ads Library record for a single ad.
* **Get Audience Insights** `getAudienceInsights`: Compares a targeting spec against a base spec and returns the demographic, geographic, device, interest and engagement composition of the targeted audience.
* **Get Audience Segment** `getAudienceSegment`: Retrieves a single audience segment by its identifier.
* **Get Audience Size By Ad Squad** `getAudienceSizeByAdSquad`: Returns the estimated reachable audience size for an existing ad squad's targeting.
* **Get Audience Size By Ad Squad Spec** `getAudienceSizeBySpec`: Returns the estimated reachable audience size for a proposed ad squad specification before the ad squad is created.
* **Get Authenticated User** `getAuthenticatedUser`: Retrieves the Snapchat user represented by the current access token, including the member ID, email address, Snapchat username and Bitmoji identifiers.
* **Get Bid Recommendation** `getBidRecommendation`: Returns a recommended bid range for an ad account when using the TARGET_COST bid strategy. Omit conversionWindow to receive recommendations for every valid window.
* **Get Billing Center** `getBillingCenter`: Retrieves a single billing center by its identifier.
* **Get Campaign** `getCampaign`: Retrieves a single campaign by its identifier.
* **Get Campaign Stats** `getCampaignStats`: Returns delivery and conversion metrics for a campaign, optionally broken down to ad squad or ad level. Metrics are finalized 48 hours after the end of the day in the ad account timezone.
* **Get Campaign Stats Report** `getCampaignStatsReport`: Checks the status of an asynchronous campaign stats report and returns the download link once it is complete.
* **Get Campaigns By IDs** `getCampaignsByIds`: Retrieves up to 2000 specific campaigns from the same ad account in one call by passing their identifiers in the request body.
* **Get Catalog** `getCatalog`: Retrieves a single product catalog by its identifier.
* **Get Catalog Facets** `getCatalogFacets`: Groups the items in a catalog by a chosen property and returns the count in each group, optionally narrowed by a filter. This is the catalog diagnostics call - use it to see how products are distributed before building product sets.
* **Get Creative** `getCreative`: Retrieves a single creative by its identifier.
* **Get Creative Preview** `getCreativePreview`: Generates the values needed to build a Snap-hosted preview page at https://ad-preview.snapchat.com. The preview needs no login and stays available for 90 days.
* **Get Creative Snapcode** `getCreativeSnapcode`: Generates a Snapcode preview for a creative so it can be scanned inside the Snapchat app. The Snapcode stops working after seven days, as reported in expires_at.
* **Get Creative Stats** `getCreativeStats`: Returns delivery metrics for a single creative over a time window.
* **Get Creatives By IDs** `getCreativesByIds`: Retrieves up to 2000 specific creatives from the same ad account in one call by passing their identifiers in the request body.
* **Get Custom Conversion** `getCustomConversion`: Retrieves a single custom conversion by its identifier.
* **Get Dynamic Template** `getDynamicTemplate`: Retrieves a single dynamic template by its identifier.
* **Get Event Details** `getEventDetails`: Retrieves a single Event Details entity by its identifier.
* **Get Funding Source** `getFundingSource`: Retrieves a single funding source by its identifier.
* **Get Interaction Zone** `getInteractionZone`: Retrieves a single interaction zone by its identifier.
* **Get Invoice** `getInvoice`: Retrieves a single invoice for an ad account, including the invoice document as a Base64 byte stream that can be written out as a PDF.
* **Get Lead Generation Form** `getLeadGenerationForm`: Retrieves a single lead generation form by its identifier, including its questions, legal disclosures and end page.
* **Get Leads Report** `getLeadsReport`: Checks the status of an asynchronous leads export and returns the download link once it is complete.
* **Get Lens Preview Media** `getLensPreviewMedia`: Retrieves the preview resources associated with a lens. Only LENS_PACKAGE media are supported, and not every lens has preview resources - availability depends on when and how the lens was created.
* **Get Media** `getMedia`: Retrieves a single media object by its identifier.
* **Get Media By IDs** `getMediaByIds`: Retrieves up to 2000 specific media objects from the same ad account in one call by passing their identifiers in the request body.
* **Get Media Preview** `getMediaPreview`: Retrieves the preview asset for a media object. Only VIDEO and IMAGE media have previews.
* **Get Media Stats** `getMediaStats`: Returns delivery metrics for a single media object over a time window.
* **Get Media Thumbnail** `getMediaThumbnail`: Retrieves the thumbnail for a video media object. Thumbnails are not available for IMAGE, LENS_PACKAGE or PLAYABLE media.
* **Get Member** `getMember`: Retrieves a single organization member by its identifier.
* **Get Mobile App** `getMobileApp`: Retrieves a single Snap App ID by its identifier.
* **Get Mobile App Apple Campaign ID Status** `getMobileAppEcidStatus`: Returns the Apple SKAdNetwork campaign ID (eCID) allocation status for a Snap App ID, showing which campaign IDs are attached, available or withdrawn.
* **Get Mobile App Campaign Eligibilities** `getMobileAppCampaignEligibilities`: Lists the optimization goals and conversion windows a Snap App ID is eligible for. Query this before creating an app ad squad so you only offer combinations Snapchat will accept.
* **Get Mobile App Signal Readiness** `getMobileAppSignalReadiness`: Returns the Signal Readiness scores and recommendations for a Snap App ID, which indicate how well the customer parameters sent with app conversion events match to Snapchat accounts.
* **Get My Public Profile** `getMyPublicProfile`: Retrieves the Public Profile belonging to the authenticated user. The access token must carry the snapchat-profile-api scope.
* **Get Offer Disclaimer** `getOfferDisclaimer`: Retrieves a single offer disclaimer by its identifier.
* **Get Or Create Conversation** `getGroupConversation`: Gets or creates the conversation between a brand profile and a creator profile. Call this before sending a collaboration message - the returned conversation identifier and token are required by the send call. Messaging is behind a separate allowlist.
* **Get Organization** `getOrganization`: Retrieves a single Snapchat Business Manager organization by its identifier.
* **Get Pixel** `getPixel`: Retrieves a single Snap Pixel by its identifier.
* **Get Pixel Campaign Eligibilities** `getPixelCampaignEligibilities`: Lists the optimization goals and conversion windows a Snap Pixel is eligible for. Query this before creating an ad squad so you only offer combinations Snapchat will accept.
* **Get Pixel Domain Stats** `getPixelDomainStats`: Returns the domains that have fired events for a Snap Pixel over a time window, with their event volumes.
* **Get Pixel Signal Readiness** `getPixelSignalReadiness`: Returns the Signal Readiness scores and recommendations for a Snap Pixel, which indicate how well the customer parameters sent with web conversion events match to Snapchat accounts. Displaying this data in a public-facing interface requires prior Snap approval.
* **Get Pixel Stats** `getPixelStats`: Returns Snap Pixel event metrics for a domain over a time window, broken out by the requested fields.
* **Get Product Feed** `getProductFeed`: Retrieves a single product feed by its identifier.
* **Get Profile Lens** `getProfileLens`: Retrieves a single Lens published by a profile.
* **Get Profile Spotlight** `getProfileSpotlight`: Retrieves a single Spotlight post published by a profile.
* **Get Profile Stats** `getProfileStats`: Returns Public Profile metrics, optionally for every asset of a given type beneath the profile. Profile-level totals are not reduced when an underlying asset is deleted.
* **Get Public Profile** `getPublicProfile`: Retrieves a single Public Profile by its identifier. The Snapchat Public Profile APIs are read-only.
* **Get Public Profile (Public Endpoint)** `getPublicProfilePublic`: Retrieves the publicly available subset of a Public Profile's metadata. This public endpoint needs no profile owner authorization and works for any Public Profile on Snapchat.
* **Get Public Profile By Snap** `getPublicProfileBySnap`: Resolves which creator owns a Snap. This public endpoint needs no profile owner authorization.
* **Get Saved Story Stats** `getSavedStoryStats`: Returns metrics for a Saved Story, or for the Snaps inside it when assetType is SNAP.
* **Get Snap Stats** `getSnapStats`: Returns metrics for a single Snap. Supply brandProfileId only when reading a Snap that was shared with your brand through a sharing policy; for a Snap from a creator you hold an ad partnership with, the creator is resolved from the Snap itself.
* **Get Spotlight Stats** `getSpotlightStats`: Returns metrics for a Spotlight post.
* **Get Story Stats** `getStoryStats`: Returns metrics for a Public Story, or for the Snaps inside it when assetType is SNAP. Pass the story's created_at and ended_at timestamps from List Profile Stories, or the request may time out on popular profiles.
* **Get Targeting Spec** `getTargetingSpec`: Retrieves a single standalone targeting spec by its identifier.
* **Get Unread Message Count** `getUnreadMessageCount`: Returns how many group conversations with creators have unread messages, expressed as a band rather than an exact figure.
* **Initialize Chunked Media Upload** `initChunkedMediaUpload`: Starts a chunked upload for a media file larger than 32 MB. Each part may be at most 32 MB and there is a limit of 32 parts, so the largest supported file is 1 GB. The response returns the add path, finalize path and upload ID needed by the remaining chunked upload actions.
* **Invite Organization Member** `createOrganizationMember`: Invites a Snapchat user to the specified organization by email. The invitation email is sent immediately and the member status stays INVITED until the user accepts. Always follow this call with Create Organization Role so the new member holds at least the member role.
* **List Ad Account Mobile Apps** `listAdAccountMobileApps`: Retrieves the Snap App IDs available to an ad account.
* **List Ad Account Pixels** `listAdAccountPixels`: Retrieves the Snap Pixel associated with an ad account.
* **List Ad Account Roles** `listAdAccountRoles`: Retrieves every role assigned on the specified ad account.
* **List Ad Account Sharing Policies** `listAdAccountSharingPolicies`: Lists the pixels, Public Profiles, catalogs and mobile apps shared with an ad account.
* **List Ad Accounts** `listAdAccounts`: Retrieves every ad account under the specified organization.
* **List Ad Change Logs** `listAdChangeLogs`: Retrieves the audit trail of changes made to an ad. Change logs are available from 16 July 2019 onwards; always paginate when reading them.
* **List Ad Squad Ad Restrictions** `listAdSquadAdRestrictions`: Retrieves a summary of the ad types currently present in an ad squad, which determines what further ad types may be added under the multi-format delivery rules.
* **List Ad Squad Change Logs** `listAdSquadChangeLogs`: Retrieves the audit trail of changes made to an ad squad. Change logs are available from 16 July 2019 onwards; always paginate when reading them.
* **List Ad Squad Targeting Specs** `getAdSquadTargetingSpecs`: Retrieves the standalone targeting specs attached to an ad squad.
* **List Ad Squad UI Render Data** `listAdSquadUiRenderData`: Retrieves the Ad Squad UI Render Data objects in an ad account. Each object records the intended conversion location of an ad squad, which together with the campaign objective determines the optimization goals Snap Ads Manager offers. Pass ids to fetch specific objects.
* **List Ad Squads By Ad Account** `listAdSquadsByAdAccount`: Retrieves every ad squad in an ad account. The sort parameter cannot be combined with readDeletedEntities.
* **List Ad Squads By Campaign** `listAdSquadsByCampaign`: Retrieves every ad squad in a campaign, optionally sorted by creation or last-update time.
* **List Ads By Ad Account** `listAdsByAdAccount`: Retrieves every ad in an ad account. The sort parameter cannot be combined with readDeletedEntities.
* **List Ads By Ad Squad** `listAdsByAdSquad`: Retrieves every ad in an ad squad, optionally sorted by creation or last-update time.
* **List Ads By Campaign** `listAdsByCampaign`: Retrieves every ad in a campaign, optionally sorted by creation or last-update time.
* **List Ads Library Sponsored Content** `listAdsLibrarySponsoredContent`: Retrieves the public Ads Library record of organic sponsored content posted by creators.
* **List Audience Segments** `listAudienceSegments`: Retrieves every audience segment in an ad account, covering customer lists, lookalikes, website and mobile app event audiences, ad engagement and profile engagement audiences.
* **List Billing Centers** `listBillingCenters`: Retrieves every billing center under the specified organization. A billing center is the contact that receives invoices.
* **List Brand Partnership Permissions** `listBrandPartnershipPermissions`: Lists the permissions a creator granted when accepting a partnership - whether they share detailed insights, expired stories, content for ads, and their profile for use in creatives. Only creators whose role status is APPROVED return permissions.
* **List Campaign Change Logs** `listCampaignChangeLogs`: Retrieves the audit trail of changes made to a campaign. Change logs are available from 16 July 2019 onwards; always paginate when reading them.
* **List Campaigns** `listCampaigns`: Retrieves every campaign in an ad account. Results can be sorted by creation or last-update time; sort cannot be combined with readDeletedEntities.
* **List Catalog Roles** `listCatalogRoles`: Retrieves every role assigned on the specified product catalog.
* **List Catalogs** `listCatalogs`: Retrieves every product catalog under an organization. An organization holds at most 200 catalogs.
* **List Collaboration Messages** `listCollaborationMessages`: Retrieves the messages exchanged between a brand profile and a creator in a conversation.
* **List Creative Change Logs** `listCreativeChangeLogs`: Retrieves the audit trail of changes made to a creative. Change logs are available from 16 July 2019 onwards; always paginate when reading them.
* **List Creative Elements** `listCreativeElements`: Retrieves the creative elements in an ad account. Creative elements are the individual tiles combined into a Collection Ad.
* **List Creatives** `listCreatives`: Retrieves every creative in an ad account. The sort parameter cannot be combined with type or reviewStatus.
* **List Dynamic Template Change Logs** `listDynamicTemplateChangeLogs`: Retrieves the audit trail of changes made to a dynamic template. Change logs are available from 16 July 2019 onwards; always paginate when reading them.
* **List Dynamic Templates** `listDynamicTemplates`: Retrieves the dynamic templates in an ad account. A dynamic template controls how feed attributes such as title, image and price are laid out in a dynamic ad.
* **List Event Details** `listEventDetails`: Retrieves every Event Details entity in an ad account. Event Details describe the calendar event promoted by a Reminder creative.
* **List Feed Uploads** `listFeedUploads`: Retrieves the 200 most recent uploads for a product feed, newest first, with the counts and validation issues from each run.
* **List Funding Sources** `listFundingSources`: Retrieves every funding source owned by the specified organization, including lines of credit, credit cards, coupons and PayPal instruments.
* **List Interaction Zones** `listInteractionZones`: Retrieves every interaction zone in an ad account. An interaction zone groups the creative elements shown in a Collection Ad.
* **List Invoices** `listInvoices`: Retrieves every invoice issued against the specified ad account. Requires the organization admin, ad account admin or campaign manager role.
* **List Lead Generation Forms** `listLeadGenerationForms`: Retrieves the lead generation forms in an ad account. A lead generation creative references one of these forms through its lead generation form identifier.
* **List Lead Webhook Integrations** `listLeadWebhookIntegrations`: Retrieves the webhook integrations registered against a lead generation form.
* **List Media** `listMedia`: Retrieves every media object in an ad account. The type filter cannot be combined with sort.
* **List Mobile App Custom Conversions** `listMobileAppCustomConversions`: Retrieves the custom conversions defined on a Snap App ID.
* **List Offer Disclaimers** `listOfferDisclaimers`: Retrieves the offer disclaimers in an ad account. Offer disclaimers carry the terms and conditions shown behind the See Offer Details pill on regulated-vertical ads.
* **List Organization Members** `listOrganizationMembers`: Retrieves every member of the specified organization together with their display name, email address and invitation status.
* **List Organization Mobile Apps** `listOrganizationMobileApps`: Retrieves every Snap App ID registered under an organization, with its App Store and Play Store identifiers and verification state.
* **List Organization Pixels** `listOrganizationPixels`: Retrieves every Snap Pixel under an organization.
* **List Organization Roles** `listOrganizationRoles`: Retrieves every role assigned within the specified organization.
* **List Organizations** `listOrganizations`: Retrieves every Snapchat Business Manager organization the authenticated user belongs to. Set withAdAccounts to true to also return the ad accounts under each organization along with the roles the user holds on them.
* **List Phone Numbers** `listPhoneNumbers`: Retrieves the verified phone numbers in an ad account. A verified phone number is required by swipe-to-call and swipe-to-text creatives.
* **List Pixel Custom Conversions** `listPixelCustomConversions`: Retrieves the custom conversions defined on a Snap Pixel. A custom conversion filters a standard event by parameter values so it can be reported and optimized against separately.
* **List Product Feeds** `listProductFeeds`: Retrieves the product feeds under a catalog. A catalog has exactly one primary feed, which may have one supplemental feed.
* **List Product Sets** `listProductSets`: Retrieves the product sets in a catalog. A product set is a filtered group of products used to decide which items a dynamic ad may show.
* **List Profile Lenses** `listProfileLenses`: Retrieves the Lenses published by a profile.
* **List Profile Roles** `listProfileRoles`: Retrieves the roles assigned on a Public Profile, covering both internal collaborators and creator partnerships.
* **List Profile Spotlights** `listProfileSpotlights`: Retrieves the Spotlight posts published by a profile.
* **List Profile Stories** `listProfileStories`: Retrieves the Public Stories posted by a profile. Note the created_at and ended_at timestamps on each story - passing them into the Snap and stats calls avoids timeouts on popular profiles.
* **List Public Profile Change Logs** `listPublicProfileChangeLogs`: Returns signed URLs to change log files, each listing the identifiers of Public Profiles created, modified or deleted. Use this to keep a local mirror of the creator catalogue in sync.
* **List Public Profiles** `listPublicProfiles`: Retrieves every Public Profile the authenticated user can access in an organization. The call fails with AUTHORIZATION_PERMISSION_DENIED when the user has no membership in that organization.
* **List Roles For Member** `listMemberRoles`: Retrieves every role assigned to a member across organizations, ad accounts and catalogs.
* **List Saved Stories** `listSavedStories`: Retrieves the Saved Stories on a profile. Set visibility to VISIBLE_ON_PROFILE to exclude saved copies that the owner keeps off the profile, such as those created alongside a Spotlight.
* **List Saved Story Snaps** `listSavedStorySnaps`: Retrieves the Snaps inside a Saved Story.
* **List Segment Sharing Policies** `listSegmentSharingPolicies`: Lists the sharing policies applied to an audience segment.
* **List Shared Snaps** `listSharedSnaps`: Retrieves the Snaps that creators have shared with a brand profile, for example content in which the brand was tagged under a paid partnership.
* **List SKAdNetwork Ad Squads** `listSkAdNetworkAdSquads`: Lists the ad squads enrolled in SKAdNetwork for a mobile app, together with their Apple campaign ID assignment status.
* **List Story Snaps** `listStorySnaps`: Retrieves the Snaps inside a Public Story. Pass the story's own created_at and ended_at timestamps, taken from List Profile Stories, or the request may time out.
* **List Targeting Advanced Demographics** `listTargetingAdvancedDemographics`: Lists the advanced demographic targeting options available in the targeting spec.
* **List Targeting Age Groups** `listTargetingAgeGroups`: Lists the age group demographic targeting options available in the targeting spec.
* **List Targeting Carriers** `listTargetingCarriers`: Lists the mobile carrier device targeting options available in the targeting spec.
* **List Targeting Connection Types** `listTargetingConnectionTypes`: Lists the network connection type device targeting options available in the targeting spec.
* **List Targeting Countries** `listTargetingCountries`: Lists the countries available for geographic targeting.
* **List Targeting Device Makes** `listTargetingDeviceMakes`: Lists the device make and marketing name targeting options available in the targeting spec.
* **List Targeting Genders** `listTargetingGenders`: Lists the gender demographic targeting options available in the targeting spec.
* **List Targeting Interests (Nielsen)** `listTargetingInterestsNln`: Lists the Nielsen interest targeting options available in the targeting spec.
* **List Targeting Interests (Oracle Datalogix DLXC)** `listTargetingInterestsDlxc`: Lists the Oracle Datalogix DLXC interest targeting options available in the targeting spec.
* **List Targeting Interests (Oracle Datalogix DLXP)** `listTargetingInterestsDlxp`: Lists the Oracle Datalogix DLXP interest targeting options available in the targeting spec.
* **List Targeting Interests (Oracle Datalogix DLXS)** `listTargetingInterestsDlxs`: Lists the Oracle Datalogix DLXS interest targeting options available in the targeting spec.
* **List Targeting Interests (Shopper)** `listTargetingInterestsShp`: Lists the shopper interest targeting options available in the targeting spec.
* **List Targeting Interests (Snap Lifestyle Categories)** `listTargetingInterestsScls`: Lists the Snap Lifestyle Category interest targeting options. These are the only interest categories that also support exclusion.
* **List Targeting Interests (Snap Visitation)** `listTargetingInterestsVac`: Lists the Snap visitation interest targeting options available in the targeting spec.
* **List Targeting Languages** `listTargetingLanguages`: Lists the language demographic targeting options available in the targeting spec. A language entry is required when targeting more than one country.
* **List Targeting Location Categories** `listTargetingLocationCategories`: Lists the location category targeting options available in the targeting spec.
* **List Targeting Metros** `listTargetingMetros`: Lists the metro or DMA areas available for geographic targeting within a country.
* **List Targeting Operating System Versions** `listTargetingOsVersions`: Lists the operating system version device targeting options available for a given operating system.
* **List Targeting Operating Systems** `listTargetingOsTypes`: Lists the mobile operating system device targeting options available in the targeting spec.
* **List Targeting Options** `listTargetingOptions`: Lists every targeting dimension the Marketing API exposes, which is useful for discovering the available targeting taxonomies in one call.
* **List Targeting Postal Codes** `listTargetingPostalCodes`: Lists the postal codes available for geographic targeting within a country. Always paginate this call.
* **List Targeting Regions** `listTargetingRegions`: Lists the regions or states available for geographic targeting within a country.
* **List Transactions** `listTransactions`: Retrieves the financial transactions recorded for an organization within a time window, optionally narrowed to a single ad account.
* **Patch Ad** `patchAd`: Applies a single JSON Patch operation to an ad, leaving every other attribute untouched. The entity ID cannot be modified and array index paths are not supported; replace the whole array instead.
* **Patch Ad Squad** `patchAdSquad`: Applies a single JSON Patch operation to an ad squad, leaving every other attribute untouched. The entity ID cannot be modified and array index paths are not supported; replace the whole array instead.
* **Patch Campaign** `patchCampaign`: Applies a single JSON Patch operation to a campaign, leaving every other attribute untouched. The entity ID cannot be modified and array index paths are not supported; replace the whole array instead.
* **Patch Creative** `patchCreative`: Applies a single JSON Patch operation to a creative, leaving every other attribute untouched. The change affects every ad using the creative and sends those ads back into review.
* **Post Profile Saved Story** `postProfileSavedStory`: Publishes an uploaded media asset to a Public Profile as a Saved Story.
* **Post Profile Spotlight** `postProfileSpotlight`: Publishes an uploaded media asset to a Public Profile as a Spotlight post.
* **Post Profile Story** `postProfileStory`: Publishes an uploaded media asset to a Public Profile as a Story.
* **Remove All Users From Audience Segment** `removeAllUsersFromSegment`: Removes every member from a customer list audience segment while keeping the segment itself. This cannot be undone.
* **Remove Users From Audience Segment** `removeUsersFromSegment`: Removes hashed user identifiers from a customer list audience segment. Send one schema type per request and at most 100000 identifiers, normalized and SHA-256 hashed exactly as they were when added.
* **Search Ads Library Ads** `searchAdsLibraryAds`: Searches the public Snapchat Ads Library for political and advocacy ads that ran in the European Union, filtered by country, date range, status and paying advertiser.
* **Search Ads Library Sponsored Content** `searchAdsLibrarySponsoredContent`: Searches the public Ads Library for organic sponsored content by creator name.
* **Search Catalog Flights** `searchCatalogFlights`: Searches a flights catalog for routes matching a filter.
* **Search Catalog Hotels** `searchCatalogHotels`: Searches a hotels catalog for properties matching a filter.
* **Search Catalog Products** `searchCatalogProducts`: Searches a commerce catalog for products matching a filter. Useful for confirming which items a product set filter will select before creating the set.
* **Search Public Profiles** `searchPublicProfiles`: Looks up Public Profiles by Snapchat username. This public endpoint needs no profile owner authorization and is the usual way to resolve a creator's username into a profile identifier.
* **Send App Conversion Events** `sendAppConversionEvents`: Sends mobile app conversion events to Snapchat against a Snap App ID. App events require app_data including extinfo, and at least one matching identifier such as madid or a hashed email in user_data. At most 2000 events per request.
* **Send Collaboration Message** `sendCollaborationMessage`: Sends a text message from a brand profile to a creator, typically to invite them to collaborate. Call Get Or Create Conversation first to obtain the conversation identifier and token. Only TEXT messages are supported and only one message per call.
* **Send Test Lead Webhook** `sendTestLeadWebhook`: Sends a sample lead payload to the URL registered on a webhook integration so the receiving endpoint can be tested end to end. The dummy data is the same regardless of how the real form is configured.
* **Send Web Conversion Events** `sendWebConversionEvents`: Sends web or offline conversion events to Snapchat against a Snap Pixel. Every event needs at least one matching identifier in user_data, and PURCHASE events additionally need currency and value. Send event_id on every event so conversions arriving from both the Pixel and this API are deduplicated. At most 2000 events per request.
* **Update Ad** `updateAd`: Replaces an ad. The Snapchat Marketing API expects the entire object on update, so send every attribute you want to keep. Use Patch Ad for a partial update.
* **Update Ad Account** `updateAdAccount`: Updates an ad account. The Snapchat Marketing API replaces the whole object on update, so send every attribute you want to keep - omitted attributes that have defaults are reset to those defaults.
* **Update Ad Account Pixel** `updateAdAccountPixel`: Renames a Snap Pixel at ad account level. The Snapchat Marketing API expects the entire object on update, so send every attribute you want to keep.
* **Update Ad Account Role** `updateAdAccountRole`: Changes the role a member holds on an ad account. The Snapchat Marketing API replaces the whole object on update, so send every attribute you want to keep.
* **Update Ad Squad** `updateAdSquad`: Replaces an ad squad. The Snapchat Marketing API expects the entire object on update, so send every attribute you want to keep. Changing the targeting sends the ads back into review and briefly pauses delivery. campaignId, billingEvent and optimizationGoal are immutable.
* **Update Ad Squad Targeting Spec** `updateAdSquadTargetingSpec`: Replaces the standalone targeting spec attached to an ad squad. Changing targeting sends the ads back into review and briefly pauses delivery.
* **Update Audience Segment** `updateAudienceSegment`: Updates the name, description and retention of an audience segment. The Snapchat Marketing API expects the entire object on update, so send every attribute you want to keep.
* **Update Billing Center** `updateBillingCenter`: Updates a billing center. The Snapchat Marketing API replaces the whole object on update, so send every attribute you want to keep.
* **Update Campaign** `updateCampaign`: Replaces a campaign. The Snapchat Marketing API expects the entire object on update, so send every attribute you want to keep - omitted attributes with defaults are reset. Use Patch Campaign for a partial update.
* **Update Catalog** `updateCatalog`: Renames a product catalog. Requires the organization admin role. The Snapchat Marketing API expects the entire object on update, so send every attribute you want to keep.
* **Update Creative** `updateCreative`: Replaces a creative. The Snapchat Marketing API expects the entire object on update, so send every attribute you want to keep. Editing a creative sends every ad that uses it back into review. The id, adAccountId and type attributes cannot be changed.
* **Update Dynamic Template** `updateDynamicTemplate`: Updates a dynamic template. The Snapchat Marketing API expects the entire object on update, so send every attribute you want to keep.
* **Update Organization Pixel** `updateOrganizationPixel`: Renames a Snap Pixel at organization level. The Snapchat Marketing API expects the entire object on update, so send every attribute you want to keep.
* **Update Product Feed** `updateProductFeed`: Updates a product feed. The Snapchat Marketing API expects the entire object on update, so send every attribute you want to keep.
* **Update Product Set** `updateProductSet`: Updates a product set. The Snapchat Marketing API expects the entire object on update, so send every attribute you want to keep.
* **Upload Media** `uploadMedia`: Uploads the asset file into a media container created with Create Media. Videos must be 1080 by 1920 pixels, MP4 or MOV, 3 to 1800 seconds and at most 32 MB; larger videos need the chunked upload actions. Top snap images are 1080 by 1920 pixels PNG or JPG up to 5 MB, and playables are a ZIP containing index.html and config.json up to 5 MB.
* **Validate App Conversion Events** `validateAppConversionEvents`: Checks that a mobile app conversion payload is well formed without recording the events. Use this to test an integration before sending live traffic.
* **Validate Web Conversion Events** `validateWebConversionEvents`: Checks that a web or offline conversion payload is well formed without recording the events. Use this to test an integration before sending live traffic.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Lead Submitted | `lead_generation.lead_submitted` | Fires in real time each time a Snapchatter submits one of the ad account's lead generation forms. Snapchat allows a single webhook integration per form, so the subscription registers one form at a time and the form identifier must be supplied as an input. Snapchat sends no event-type discriminator in the payload - this is the only event the integration emits, so routing is by registered URL rather than by a payload field. Deliveries carry a Signature header and a t timestamp header; the signature is an HMAC-SHA256 over the timestamp, a full stop, and the UTF-8 request body, keyed with the hmacSecret returned when the integration was created. That secret is shared by every integration under the same ad account. |
