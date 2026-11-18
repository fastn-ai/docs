---
description: "Short.io is a branded link-management platform for creating and tracking short links on your own domains."
hidden: true
---

# Short.io

<img src="../../.gitbook/assets/connectors/lg/shortio.png" alt="Short.io logo">

Short.io is a branded link-management platform for creating and tracking short links on your own domains. This connector covers the complete Short.io public API: domains and domain settings, DNS records, allowed hostnames, IP exclusions, themes, favicons, universal links, password pages and S3 exports; links (create, bulk create, update, duplicate, expand, archive, delete), link folders, tags, link permissions, OpenGraph properties, country and region targeting, link bundles and posts; QR code generation and hosted QR codes; organization plan and usage; the audit log; and the full click-statistics API on statistics.short.io (domain and link statistics, top values, interval breakdowns, raw click lists and popular paths).

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [short.io](https://short.io) |
| **Authentication** | API key, Credentials you enter |
| **Slug** | `shortio` |

## Use it

Add Short.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.shortio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept a pending domain transfer | `acceptDomainTransfer` | Accept a pending domain transfer. |
| Add Allowed Hostname | `addAllowedHostname` | Adds a referrer hostname to the allowlist of a domain, restricting which sites may link through this domain's short links. |
| Add Domain IP Exclusion | `addDomainIpExclusion` | Excludes an IPv4 address from click tracking on a domain, so visits from that address are not counted in statistics. |
| Add Link Country Target | `addLinkCountryTarget` | Routes visitors from one country to a different destination URL for a short link. |
| Add Link Country Targets In Bulk | `addLinkCountryTargetsBulk` | Sets several country-specific destinations on a short link in one call. |
| Add Link Permission | `addLinkPermission` | Grants a team member access to a single short link. Access changes affect real users, so run this only against a user you intend to grant access to. |
| Add Link Region Target | `addLinkRegionTarget` | Routes visitors from one region or state to a different destination URL for a short link. |
| Add Link Region Targets In Bulk | `addLinkRegionTargetsBulk` | Sets several region-specific destinations on a short link in one call. |
| Add Link To Bundle | `addLinkToBundle` | Adds a link to a bundle page, either an existing short path on the bundle's domain or a full external URL. |
| Add Tag To Links In Bulk | `addTagToLinksBulk` | Appends a single tag to many links at once, leaving any tags the links already carry in place. |
| Archive Link | `archiveLink` | Archives a single short link so it stops redirecting but is not deleted. |
| Archive Links In Bulk | `archiveLinksBulk` | Archives many short links in one call. |
| Cancel a pending domain transfer | `cancelDomainTransfer` | Cancel a pending domain transfer. |
| Clear Domain Link Signature Key | `clearDomainLinkSignatureKey` | Removes the link-signature key from a domain, so short links on it no longer require a signature. |
| Create DNS Records | `createDnsRecords` | Creates MX or TXT DNS records on a Short.io managed hostname. |
| Create Domain | `createDomain` | Adds a new domain to the Short.io account. Short.io's own suffixes such as short.gy and short.io are reserved and cannot be registered through the API. |
| Create Link | `createLink` | Creates a short link on one of the account's domains, with optional custom path, title, tags, UTM parameters, expiry, click limit, password, device-specific destinations and A/B split testing. |
| Create Link Bundle | `createLinkBundle` | Creates a link bundle, the link-in-bio style landing page that groups several short links under one branded page with social profile links. |
| Create Link Folder | `createLinkFolder` | Creates a link folder on a domain. A folder groups links and can carry default UTM parameters, redirect type, slug prefix, tracking pixels and QR code styling that new links in the folder inherit. |
| Create Link Simple | `createLinkSimple` | Creates a short link through Short.io's simplified single-request endpoint, which takes everything as query parameters. Useful for bots and integrations that can only issue a plain GET. The connection's API key is supplied automatically. |
| Create Link With Public Key | `createLinkWithPublicKey` | Creates a short link through the endpoint intended for Short.io public API keys, which may be exposed in client-side code. It accepts the same options as Create Link. |
| Create Links In Bulk | `createLinksBulk` | Creates up to 1000 short links on a single domain in one call. Each entry accepts the same options as a single link create. |
| Create or update link QR code settings | `setLinkQrCodeSettings` | Create or update link QR code settings. Saves the QR code settings for the link. Omitted fields are left untouched; send an empty string to clear a text field. |
| Create Post | `createPost` | Creates a Short.io post, a Markdown article hosted on your branded domain and reachable through a short link. |
| Decline a pending domain transfer | `declineDomainTransfer` | Decline a pending domain transfer. |
| Delete DNS Records | `deleteDnsRecords` | Deletes MX or TXT DNS records from a Short.io managed hostname. When no value is given, every matching record of that name and type is removed. |
| Delete Domain | `deleteDomain` | Permanently removes a domain and all of its links from the Short.io account. This route is not listed in the published OpenAPI document but is the live endpoint the Short.io dashboard uses; it was verified against the API during this build. |
| Delete Domain Favicon | `deleteDomainFavicon` | Removes the custom favicon from a domain so Short.io's default icon is served again. |
| Delete Domain QR Code Settings | `deleteDomainQrCodeSettings` | Removes the saved default QR code styling from a domain, so generated QR codes fall back to Short.io's defaults. |
| Delete Domain Theme | `deleteDomainTheme` | Removes a domain's custom theme so its Short.io-hosted pages fall back to the default styling. |
| Delete Link | `deleteLink` | Permanently deletes a single short link by its link ID string. |
| Delete Link Bundle | `deleteLinkBundle` | Permanently deletes a link bundle and takes its landing page offline. |
| Delete Link Country Target | `deleteLinkCountryTarget` | Removes the country-specific destination for one country from a short link, so visitors from that country fall back to the link's main destination. |
| Delete link QR code settings | `deleteLinkQrCodeSettings` | Delete link QR code settings. Deletes the QR code settings saved for the link, reverting to the domain or folder settings. |
| Delete Link Region Target | `deleteLinkRegionTarget` | Removes the region-specific destination for one region from a short link, so visitors from that region fall back to the link's main destination. |
| Delete Links By Date Interval | `deleteLinksByDateInterval` | Bulk-prunes links on a domain by creation date, optionally restricted to links whose chosen column contains a given substring. This permanently deletes every matching link. |
| Delete Links In Bulk | `deleteLinksBulk` | Permanently deletes many short links in one call. |
| Delete Post | `deletePost` | Permanently deletes a Short.io post and takes its hosted page offline. |
| Disable Domain S3 Export | `disableDomainS3Export` | Turns off scheduled export of a domain's click data to Amazon S3. |
| Duplicate Link | `duplicateLink` | Creates a copy of an existing short link on the same domain. Only the short path of the copy can be set; every other property is inherited from the source link. |
| Enable Domain S3 Export | `enableDomainS3Export` | Turns on scheduled export of a domain's raw click data to Amazon S3. |
| Expand Link | `expandLink` | Resolves a short link to its full record using the domain hostname and the short path. |
| Generate AI Link QR Code | `generateAiLinkQrCode` | Generates an artistic QR code for a short link, rendering the code into AI-generated artwork described by a prompt. |
| Generate Example Links | `generateExampleLinks` | Creates a set of sample short links on a domain, used to populate a newly added domain with demonstration data. |
| Generate Hosted Link QR Code | `generateHostedLinkQrCode` | Generates a QR code for a short link and hosts it at a permanent Short.io URL, so the image can be embedded without storing the file yourself. |
| Generate Link QR Code | `generateLinkQrCode` | Generates a QR code image for a short link, with full control over colours, size, image format, finder-pattern shapes and an optional text label. Set Use Domain Settings to inherit the domain's saved QR styling instead. |
| Generate QR Codes In Bulk | `generateQrCodesBulk` | Generates QR codes for many short links in one call, applying the same styling to every code. |
| Get Bundle Templates | `getBundleTemplates` | Lists the page templates available for link bundles, each controlling the layout and styling of the bundle page. |
| Get Domain | `getDomain` | Retrieves the full configuration of a single Short.io domain by its numeric domain ID. |
| Get Domain Clicks By Interval | `getDomainClicksByInterval` | Returns a domain's click totals bucketed into a time series, for charting clicks over hours, days, weeks or months. |
| Get Domain Password Page CSS | `getDomainPasswordPageCss` | Returns the custom stylesheet applied to the password prompt shown for password-protected links on a domain. |
| Get Domain Popular Paths | `getDomainPopularPaths` | Returns the most popular short links on a domain during a time interval, ranked by clicks. |
| Get Domain QR Code Settings | `getDomainQrCodeSettings` | Returns the default QR code styling saved on a domain, which QR generation actions can inherit by setting Use Domain Settings. |
| Get Domain Raw Clicks | `getDomainRawClicks` | Returns the raw click log for a domain over a time period, one entry per click with referrer, country, device and timestamp. |
| Get Domain S3 Export | `getDomainS3Export` | Returns whether scheduled click export to Amazon S3 is enabled for a domain and how it is configured. |
| Get Domain Statistics | `getDomainStatistics` | Returns aggregated click statistics for a domain over a time period, including totals, the clicks chart and top breakdowns by country, referrer, browser and device. |
| Get Domain Theme | `getDomainTheme` | Returns the colour and typography theme applied to a domain's Short.io-hosted pages, such as password and link-bundle pages. |
| Get Domain Top Values | `getDomainTopValues` | Returns the most-clicked values of a chosen dimension across a domain, such as top countries, cities, browsers, operating systems, short paths or UTM values, ordered by click count. The dimension list is validated by Short.io; unsupported names are rejected. |
| Get Domain Universal Links | `getDomainUniversalLinks` | Returns the iOS and Android app association configuration a domain serves, which lets short links open directly in a mobile app. |
| Get Link | `getLink` | Retrieves a single short link by its link ID string. |
| Get Link Bundle | `getLinkBundle` | Retrieves a link bundle by its ID, including its branding and social profile settings. |
| Get Link By Original URL | `getLinkByOriginalUrl` | Finds the short link on a domain that points at a given destination URL. |
| Get Link Clicks By Interval | `getLinkClicksByInterval` | Returns a single link's click totals bucketed into a time series, for charting clicks over hours, days, weeks or months. |
| Get Link Clicks For Domain | `getLinkClicksForDomain` | Returns click counts for specific links on a domain, keyed by link ID, for a date range. Pass a comma-separated list of link ID strings to limit the result. |
| Get Link Folder | `getLinkFolder` | Retrieves a single link folder on a domain by its folder ID. |
| Get Link OpenGraph Properties | `getLinkOpengraph` | Returns the OpenGraph tags configured on a short link, which control how it previews when shared on social platforms. |
| Get link QR code settings | `getLinkQrCodeSettings` | Get link QR code settings. Returns the QR code settings saved for the link, applied on every generation instead of the domain or folder settings. |
| Get Link Statistics | `getLinkStatistics` | Returns aggregated click statistics for a single short link over a time period, including totals, the clicks chart and top breakdowns. |
| Get Link Top Values | `getLinkTopValues` | Returns the most-clicked values of a chosen dimension for a single short link, ordered by click count. Short.io's statistics service currently fails to resolve the link for this endpoint and answers 500 for every link identifier form; use Get Domain Top Values with the path dimension until Short.io fixes it. |
| Get Links By Original URL | `getLinksByOriginalUrl` | Returns every short link on a domain that points at a given destination URL, for destinations that have been shortened more than once. |
| Get Organization Plan Info | `getOrganizationPlanInfo` | Returns the plan an organization is on together with its current usage, including domain and link counts, storage used and AI spend. |
| Get Post | `getPost` | Retrieves a Short.io post by its ID, including its Markdown body. |
| Inspect URL Deep Link Configuration | `inspectUrlDeepLinkConfiguration` | Fetches a domain's Apple App Site Association and Android asset links files and reports the deep link configuration they declare. Short.io protects this endpoint with hCaptcha, so a valid hCaptcha token obtained from a browser widget must be supplied. |
| Inspect URL OpenGraph Tags | `inspectUrlOpengraphTags` | Fetches a public web page and reports the OpenGraph tags it serves, for previewing how the page will look when shared. Short.io protects this endpoint with hCaptcha, so a valid hCaptcha token obtained from a browser widget must be supplied. |
| List Allowed Hostnames | `listAllowedHostnames` | Lists the referrer hostnames that are allowed to use the short links of a domain. |
| List Audit Log | `listAuditLog` | Lists audit log entries for a domain, recording who created, updated or deleted links and when. Requires a Short.io plan that includes the audit log. |
| List Bundle Links | `listBundleLinks` | Lists the links shown on a link bundle page, in their display order. |
| List Country Regions | `listCountryRegions` | Lists the ISO 3166-2 regions of a country, used to pick a region code when configuring region targeting on a link. |
| List DNS Records | `listDnsRecords` | Lists the DNS records Short.io manages for a hostname, including the records required to point the domain at Short.io. |
| List Domain Tags | `listDomainTags` | Lists every tag used across the links of a domain. |
| List Domains | `listDomains` | Lists the domains available to the connected Short.io account, with optional pagination, a hostname substring filter, and filters for personal or team domains. |
| List Hosted QR Codes | `listHostedQrCodes` | Lists the hosted QR codes created on a domain, optionally narrowed to a single link. |
| List Link Country Targets | `listLinkCountryTargets` | Lists the country-specific destinations configured on a short link, which send visitors from a given country to a different URL. |
| List Link Folders | `listLinkFolders` | Lists the link folders defined on a domain. |
| List Link Permissions | `listLinkPermissions` | Lists the team members who have been granted explicit access to a single short link. |
| List Link Region Targets | `listLinkRegionTargets` | Lists the region-specific destinations configured on a short link, which send visitors from a given state or region to a different URL. |
| List Links | `listLinks` | Lists the short links on a domain, with cursor pagination, date-range filters, sort order and an optional folder filter. |
| List pending domain transfers | `listDomainTransfers` | List pending domain transfers. |
| List Popular Domain Tags | `listPopularDomainTags` | Lists the most frequently used tags on a domain, ordered by how many links carry them. |
| Mark Domain As Favorite | `markDomainAsFavorite` | Marks a domain as a favourite so it is pinned at the top of the domain list in the Short.io dashboard. |
| Query Domain Statistics | `queryDomainStatistics` | Returns the same aggregated domain click statistics as Get Domain Statistics, taking the reporting window in the request body so that long filter sets can be submitted. |
| Query Link Clicks For Domain | `queryLinkClicksForDomain` | Returns click counts for the links of a domain within a date range, keyed by link ID. This is the POST form of the endpoint and accepts only the date range; to report on a specific subset of links use Get Link Clicks For Domain, whose ids filter Short.io honours. |
| Query Link Statistics | `queryLinkStatistics` | Returns the same aggregated link click statistics as Get Link Statistics, taking the reporting window in the request body. |
| Remove Allowed Hostname | `removeAllowedHostname` | Removes a referrer hostname from the allowlist of a domain. |
| Remove Domain IP Exclusion | `removeDomainIpExclusion` | Removes an IPv4 address from a domain's click-tracking exclusion list, so its visits are counted again. |
| Remove Link From Bundle | `removeLinkFromBundle` | Removes one link from a bundle page. The underlying short link itself is not deleted. |
| Remove Link Permission | `removeLinkPermission` | Revokes a team member's explicit access to a single short link. |
| Reorder Bundle Links | `reorderBundleLinks` | Changes the display order of the links on a bundle page by assigning each entry a new sort position. |
| Revoke Hosted QR Code | `revokeHostedQrCode` | Revokes a hosted QR code so its permanent Short.io image URL stops serving. |
| Rotate Domain Link Signature Key | `rotateDomainLinkSignatureKey` | Generates a new link-signature key for a domain and returns it. The key is used to sign short links so that only links your systems produced are honoured. Rotating invalidates every signature made with the previous key. |
| Set Domain Password Page CSS | `setDomainPasswordPageCss` | Sets the custom stylesheet used for the password prompt shown on password-protected links of a domain. |
| Set Domain QR Code Settings | `setDomainQrCodeSettings` | Creates or updates the default QR code styling for a domain, so QR codes generated with Use Domain Settings share one brand look. |
| Set Domain Theme | `setDomainTheme` | Creates or updates the colour and typography theme used on a domain's Short.io-hosted pages. |
| Set Domain Universal Links | `setDomainUniversalLinks` | Creates or updates the iOS and Android app association files a domain serves, so short links open directly in your mobile app instead of the browser. |
| Set Link OpenGraph Properties | `setLinkOpengraph` | Replaces the OpenGraph tags on a short link, controlling the title, description, image and other preview metadata shown when the link is shared. The body is a list of property and value pairs. |
| Transfer a domain to another organization | `transferDomain` | Transfer a domain to another organization. |
| Unarchive Link | `unarchiveLink` | Restores an archived short link so it redirects again. |
| Unarchive Links In Bulk | `unarchiveLinksBulk` | Restores many archived short links in one call. |
| Unmark Domain As Favorite | `unmarkDomainAsFavorite` | Removes a domain from the favourites so it is no longer pinned in the Short.io dashboard. |
| Update Domain Settings | `updateDomainSettings` | Updates the settings of a Short.io domain, including redirect behaviour, HTTPS level, link defaults, robots policy, tracking integrations and the click webhook URL. Only the fields supplied are changed. |
| Update Link | `updateLink` | Updates an existing short link. Only the fields supplied are changed; the destination, path, title, tags, UTM parameters, expiry, click limit and device destinations can all be edited. |
| Update Link Bundle | `updateLinkBundle` | Updates a link bundle's branding, description and social profile links. Only the fields supplied are changed. |
| Update Post | `updatePost` | Updates a Short.io post. The title and body must both be supplied; Short.io replaces the stored post with the values sent. |
| Upload Bundle Background Image | `uploadBundleBackgroundImage` | Uploads the background image used behind a link bundle page. The image is sent as the raw request body. |
| Upload Bundle Logo | `uploadBundleLogo` | Uploads the profile logo image shown at the top of a link bundle page. The image is sent as the raw request body. |
| Upload Domain Favicon | `uploadDomainFavicon` | Uploads the favicon served for a domain's short links and Short.io-hosted pages. The image is sent as the raw request body; pass the file contents as a base64 data URI or raw text. |
| Upload Domain QR Code Logo | `uploadDomainQrCodeLogo` | Uploads the logo image placed at the centre of QR codes generated for a domain. The image is sent as the raw request body. |
| Upload link QR code logo | `uploadLinkQrCodeLogo` | Upload the logo embedded in this link's QR code (PUT /links/qr/settings/logo/{linkIdString}). The image is sent as the raw request body. |
| Upload Post Cover Image | `uploadPostCoverImage` | Uploads the cover image shown at the top of a Short.io post. The image is sent as the raw request body. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Link Clicked | `click` | Fired for every click on any short link of the subscribed domain. Short.io delivers clicks to a single webhook URL configured per domain, so subscribing registers the fastn trigger URL as that domain's Webhook URL. Setting a domain Webhook URL requires a Short.io Pro plan. The payload below is modelled from Short.io's documented click-webhook fields, not captured from a live delivery, because the connected account is on the free tier and the vendor refuses to store a webhook URL. |
