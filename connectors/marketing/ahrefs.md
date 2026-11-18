---
description: "Ahrefs is an SEO and marketing intelligence platform."
hidden: true
---

# Ahrefs

<img src="../../.gitbook/assets/connectors/ahrefs.png" alt="Ahrefs logo" width="64">

Ahrefs is an SEO and marketing intelligence platform. This connector covers the complete Ahrefs API v3 (151 endpoints across 14 tools): Site Explorer backlink, referring-domain, organic and paid traffic reports and histories; Keywords Explorer volumes and suggestions; Site Audit projects, issues and page explorer; Rank Tracker overviews and competitor reports; SERP Overview; Batch Analysis; Subscription limits and usage; Management of projects, tracked keywords, competitors, keyword lists and Brand Radar prompts and reports; Brand Radar AI-search visibility reports; Content Helper topics; Web Analytics stats and charts; GSC Insights; Social Media channels, posts and metrics; and the free Public endpoints (crawler IPs, free domain rating, top domains). Requests are authenticated with an Ahrefs API key as a Bearer token and consume API units per the plan.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [ahrefs.com](https://ahrefs.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `ahrefs` |

## Use it

Add Ahrefs from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ahrefs.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Keyword List Keywords | `putManagementKeywordListKeywords` | Add to Keywords list. **Requests to this endpoint are free and do not consume any API units.** |
| Add Project Competitors | `createManagementProjectCompetitors` | Add Competitors. &gt;Requests to this endpoint are free and do not consume any API units. |
| Add Project Keyword Tags | `putManagementProjectKeywordsTags` | Add Keywords Tags. &gt;Requests to this endpoint are free and do not consume any API units. |
| Add Project Keywords | `putManagementProjectKeywords` | Add Keywords. &gt;Requests to this endpoint are free and do not consume any API units. |
| Brand Radar AI Responses | `brandRadarAiResponses` | AI Responses. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar AI Responses (POST) | `createBrandRadarAiResponses` | AI Responses. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar Citations History | `createBrandRadarCitationsHistory` | Citations. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. Every entity provided in `brands` (and `competitors`, when applicable) must include at least one value in `url_groups`. Entities consisting only of `names` are not supported here because citations are matched against URL groups. |
| Brand Radar Citations Overview | `createBrandRadarCitationsOverview` | Citations. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. Every entity provided in `brands` (and `competitors`, when applicable) must include at least one value in `url_groups`. Entities consisting only of `names` are not supported here because citations are matched against URL groups. |
| Brand Radar Cited Domains | `brandRadarCitedDomains` | Cited Domains. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar Cited Domains (POST) | `createBrandRadarCitedDomains` | Cited Domains. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |

<details>

<summary>See 146 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Brand Radar Cited Pages | `brandRadarCitedPages` | Cited Pages. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar Cited Pages (POST) | `createBrandRadarCitedPages` | Cited Pages. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar Impressions History | `brandRadarImpressionsHistory` | Impressions. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar Impressions History (POST) | `createBrandRadarImpressionsHistory` | Impressions. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar Impressions Overview | `brandRadarImpressionsOverview` | Impressions. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar Impressions Overview (POST) | `createBrandRadarImpressionsOverview` | Impressions. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar Mentions History | `brandRadarMentionsHistory` | Mentions. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar Mentions History (POST) | `createBrandRadarMentionsHistory` | Mentions. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. Every entity provided in `brands` (and `competitors`, when applicable) must include at least one value in `names`. Entities consisting only of `url_groups` are not supported here because mentions are matched against brand names. |
| Brand Radar Mentions Overview | `brandRadarMentionsOverview` | Mentions. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar Mentions Overview (POST) | `createBrandRadarMentionsOverview` | Mentions. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. Every entity provided in `brands` (and `competitors`, when applicable) must include at least one value in `names`. Entities consisting only of `url_groups` are not supported here because mentions are matched against brand names. |
| Brand Radar SOV History | `brandRadarSovHistory` | Share of Voice. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar SOV History (POST) | `createBrandRadarSovHistory` | Share of Voice. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar SOV Overview | `brandRadarSovOverview` | Share of Voice. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Brand Radar SOV Overview (POST) | `createBrandRadarSovOverview` | Share of Voice. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Content Helper Topics | `contentHelperTopics` | Topics. &gt;This endpoint consumes a base amount of 1000 units per request, plus 500 units if you request a URL to score. &gt;The analysis runs on demand against the pages currently ranking for the keyword, so the first request for a keyword takes a few seconds. Results are cached, and repeat requests are served from the cache free of charge. &gt;Only SERPs Ahrefs has already collected are used, and no new SERP is collected. If we have collected a SERP for the keyword and country in the last 90 days, the endpoint returns a `400` error and no units are consumed. |
| Crawler IP Ranges | `publicCrawlerIpRanges` | Crawler IP ranges. &gt;Requests to this endpoint are free and do not require an API key. |
| Crawler IPs | `publicCrawlerIps` | Crawler IP addresses. &gt;Requests to this endpoint are free and do not require an API key. |
| Create Brand Radar Prompts | `createManagementBrandRadarPrompts` | Add Brand Radar prompts. &gt;Requests to this endpoint are free and do not consume any API units. |
| Create Brand Radar Report | `createManagementBrandRadarReports` | Add Brand Radar Reports. &gt;Requests to this endpoint are free and do not consume any API units. |
| Create Project | `createManagementProjects` | Add Projects. &gt;Requests to this endpoint are free and do not consume any API units. |
| Create Social Media Post | `createSocialMediaPost` | Create post. &gt;Requests to this endpoint are free and do not consume any API units. |
| Current service notices | `keywordsExplorerServiceNotices` | Current service notices. &gt;Returns the service notices that are currently displayed in Keywords Explorer. Requests to this endpoint are free and do not consume any API units. |
| Delete Projects | `deleteManagementProjects` | Delete Projects. &gt;Requests to this endpoint are free and do not consume any API units. |
| Delete Social Media Post | `deleteSocialMediaPost` | Delete post. &gt;Requests to this endpoint are free and do not consume any API units. |
| Get Free Domain Rating | `publicDomainRatingFree` | Domain rating free. &gt;Requests to this endpoint are free, yet require an APIv3 key. &gt;APIv3 keys are free to generate and use. If you don't have an Ahrefs account, here's how to get the key for free: &gt;1. [Sign up](https://ahrefs.com/) for a free Ahrefs account (if you don't have one) &gt;2. Generate an API key in [Account settings → API keys](https://app.ahrefs.com/account/api-keys) &gt;3. Add it to your requests: `Authorization: Bearer &lt;token&gt;` Use of this data is subject to the Domain Rating License at http://ahrefs.com/legal/domain-rating-license. Attribution required: "Domain Rating by Ahrefs" (https://ahrefs.com/). |
| Get Free Domain Rating (Batch) | `createPublicDomainRatingFree` | Domain rating free. &gt;Requests to this endpoint are free, yet require an APIv3 key. &gt;APIv3 keys are free to generate and use. If you don't have an Ahrefs account, here's how to get the key for free: &gt;1. [Sign up](https://ahrefs.com/) for a free Ahrefs account (if you don't have one) &gt;2. Generate an API key in [Account settings → API keys](https://app.ahrefs.com/account/api-keys) &gt;3. Add it to your requests: `Authorization: Bearer &lt;token&gt;` Use of this data is subject to the Domain Rating License at http://ahrefs.com/legal/domain-rating-license. Attribution required: "Domain Rating by Ahrefs" (https://ahrefs.com/). |
| GSC Anonymous Queries | `gscAnonymousQueries` | Anonymous queries. |
| GSC CTR By Position | `gscCtrByPosition` | CTR by position. &gt;Requests to this endpoint are free and do not consume any API units. |
| GSC Keyword History | `gscKeywordHistory` | Keyword history. &gt;Requests to this endpoint are free and do not consume any API units. |
| GSC Keywords | `gscKeywords` | Keywords. &gt;Requests to this endpoint are free and do not consume any API units. |
| GSC Metrics By Country | `gscMetricsByCountry` | Metrics by country. &gt;Requests to this endpoint are free and do not consume any API units. |
| GSC Page History | `gscPageHistory` | Page history. &gt;Requests to this endpoint are free and do not consume any API units. |
| GSC Pages | `gscPages` | Pages. &gt;Requests to this endpoint are free and do not consume any API units. |
| GSC Pages History | `gscPagesHistory` | Pages history. &gt;Requests to this endpoint are free and do not consume any API units. |
| GSC Performance By Device | `gscPerformanceByDevice` | Performance by device. &gt;Requests to this endpoint are free and do not consume any API units. |
| GSC Performance By Position | `gscPerformanceByPosition` | Performance by position. &gt;Requests to this endpoint are free and do not consume any API units. |
| GSC Performance History | `gscPerformanceHistory` | Performance history. &gt;Requests to this endpoint are free and do not consume any API units. |
| GSC Positions History | `gscPositionsHistory` | Positions history. &gt;Requests to this endpoint are free and do not consume any API units. |
| Keywords Explorer Matching Terms | `keywordsExplorerMatchingTerms` | Matching terms. |
| Keywords Explorer Overview | `keywordsExplorerOverview` | Overview. The `regex` filter has limited functionality when used in this request, and the syntax differs from other requests. It expects an asterisk (*) symbol as a wildcard. |
| Keywords Explorer Related Terms | `keywordsExplorerRelatedTerms` | Related terms. |
| Keywords Explorer Search Suggestions | `keywordsExplorerSearchSuggestions` | Search suggestions. |
| Keywords Explorer Volume By Country | `keywordsExplorerVolumeByCountry` | Volume by country. |
| Keywords Explorer Volume History | `keywordsExplorerVolumeHistory` | Volume history. |
| List Brand Radar Prompts | `managementBrandRadarPrompts` | Brand Radar prompts. &gt;Requests to this endpoint are free and do not consume any API units. |
| List Brand Radar Reports | `managementBrandRadarReports` | Brand Radar Reports. &gt;Requests to this endpoint are free and do not consume any API units. |
| List Keyword List Keywords | `managementKeywordListKeywords` | Keyword list items. **Requests to this endpoint are free and do not consume any API units.** |
| List Project Competitors | `managementProjectCompetitors` | Competitors. &gt;Requests to this endpoint are free and do not consume any API units. |
| List Project Keywords | `managementProjectKeywords` | Keywords. &gt;Requests to this endpoint are free and do not consume any API units. |
| List Projects | `managementProjects` | Projects. &gt;Requests to this endpoint are free and do not consume any API units. |
| List Social Media Authors | `socialMediaAuthors` | Authors. &gt;Requests to this endpoint are free and do not consume any API units. |
| List Social Media Channels | `socialMediaChannels` | Channels. &gt;Requests to this endpoint are free and do not consume any API units. |
| List Social Media Posts | `socialMediaPosts` | Posts. &gt;Requests to this endpoint are free and do not consume any API units. |
| Locations And Languages | `managementLocations` | Locations and languages. &gt;Requests to this endpoint are free and do not consume any API units. |
| Rank Tracker Competitors Domains | `rankTrackerCompetitorsDomains` | Competitors domains. &gt;Requests to this endpoint are free and do not consume any API units. |
| Rank Tracker Competitors Overview | `rankTrackerCompetitorsOverview` | Competitors overview. &gt;Requests to this endpoint are free and do not consume any API units. |
| Rank Tracker Competitors Pages | `rankTrackerCompetitorsPages` | Competitors pages. &gt;Requests to this endpoint are free and do not consume any API units. |
| Rank Tracker Competitors Stats | `rankTrackerCompetitorsStats` | Competitors metrics. &gt;Requests to this endpoint are free and do not consume any API units. |
| Rank Tracker Overview | `rankTrackerOverview` | Overview. &gt;Requests to this endpoint are free and do not consume any API units. |
| Rank Tracker SERP Overview | `rankTrackerSerpOverview` | SERP Overview. &gt;Requests to this endpoint are free and do not consume any API units. |
| Referring domains | `competitiveAnalysisLinkIntersectRefdomains` | Referring domains. |
| Referring pages | `competitiveAnalysisLinkIntersectRefpages` | Referring pages. |
| Remove Brand Radar Prompts | `putManagementBrandRadarPromptsDelete` | Delete Brand Radar prompts. &gt;Requests to this endpoint are free and do not consume any API units. |
| Remove Keyword List Keywords | `putManagementKeywordListKeywordsDelete` | Delete from Keywords list. **Requests to this endpoint are free and do not consume any API units.** |
| Remove Project Competitors | `createManagementProjectCompetitorsDelete` | Delete Competitors. &gt;Requests to this endpoint are free and do not consume any API units. |
| Remove Project Keyword Tags | `putManagementProjectKeywordsTagsDelete` | Delete Keywords Tags. &gt;Requests to this endpoint are free and do not consume any API units. |
| Remove Project Keywords | `putManagementProjectKeywordsDelete` | Delete Keywords. &gt;Requests to this endpoint are free and do not consume any API units. |
| Run Batch Analysis | `createBatchAnalysisBatchAnalysis` | Batch Analysis. |
| SERP Overview | `serpOverviewSerpOverview` | SERP Overview. |
| Site Audit Issues | `siteAuditIssues` | Project Issues. &gt;This endpoint consumes a fixed cost of 50 API units per request. |
| Site Audit Page Content | `siteAuditPageContent` | Page content. &gt;This endpoint consumes a fixed cost of 50 API units per request. |
| Site Audit Page Explorer | `siteAuditPageExplorer` | Page explorer. &gt;This endpoint consumes a fixed cost of 50 API units per request. |
| Site Audit Projects | `siteAuditProjects` | Project Health Scores. &gt;Requests to this endpoint are free and do not consume any API units. |
| Site Explorer AI Responses Count | `siteExplorerAiResponsesCount` | AI Responses Count. |
| Site Explorer All Backlinks | `siteExplorerAllBacklinks` | Backlinks. |
| Site Explorer Anchors | `siteExplorerAnchors` | Anchors. |
| Site Explorer Backlinks Stats | `siteExplorerBacklinksStats` | Backlinks stats. |
| Site Explorer Broken Backlinks | `siteExplorerBrokenBacklinks` | Broken Backlinks. |
| Site Explorer Crawled Pages | `siteExplorerCrawledPages` | Crawled pages. |
| Site Explorer Domain Rating | `siteExplorerDomainRating` | Domain rating. |
| Site Explorer Domain Rating History | `siteExplorerDomainRatingHistory` | Domain Rating history. |
| Site Explorer Keywords History | `siteExplorerKeywordsHistory` | Keywords history. |
| Site Explorer Linked Anchors External | `siteExplorerLinkedAnchorsExternal` | Outgoing external anchors. |
| Site Explorer Linked Anchors Internal | `siteExplorerLinkedAnchorsInternal` | Outgoing internal anchors. |
| Site Explorer Linked Domains | `siteExplorerLinkeddomains` | Linked Domains. |
| Site Explorer Metrics | `siteExplorerMetrics` | Metrics. |
| Site Explorer Metrics By Country | `siteExplorerMetricsByCountry` | Metrics by country. |
| Site Explorer Metrics History | `siteExplorerMetricsHistory` | Metrics history. |
| Site Explorer Organic Competitors | `siteExplorerOrganicCompetitors` | Organic competitors. |
| Site Explorer Organic Keywords | `siteExplorerOrganicKeywords` | Organic keywords. |
| Site Explorer Outlinks Stats | `siteExplorerOutlinksStats` | Outlinks stats. **This is a beta version of the endpoint. The data it returns may not always exactly match the corresponding values in Ahrefs UI. Data accuracy will be improved soon.** |
| Site Explorer Pages By Backlinks | `siteExplorerPagesByBacklinks` | Best pages by backlinks. Formerly `/best-by-external-links` |
| Site Explorer Pages By Internal Links | `siteExplorerPagesByInternalLinks` | Best pages by internal links. Formerly `/best-by-internal-links` |
| Site Explorer Pages By Traffic | `siteExplorerPagesByTraffic` | Pages by traffic. |
| Site Explorer Pages History | `siteExplorerPagesHistory` | Pages history. |
| Site Explorer Paid Pages | `siteExplorerPaidPages` | Paid pages. |
| Site Explorer Referring Domains | `siteExplorerRefdomains` | Refdomains. |
| Site Explorer Referring Domains History | `siteExplorerRefdomainsHistory` | Refdomains history. |
| Site Explorer Top Pages | `siteExplorerTopPages` | Top pages. |
| Site Explorer Total Search Volume History | `siteExplorerTotalSearchVolumeHistory` | Total search volume history. |
| Site Explorer URL Rating History | `siteExplorerUrlRatingHistory` | URL Rating history. |
| Social Media Activity History | `socialMediaActivityHistory` | Activity history. &gt;Requests to this endpoint are free and do not consume any API units. |
| Social Media Channel Metrics | `socialMediaChannelMetrics` | Channel metrics. &gt;Requests to this endpoint are free and do not consume any API units. |
| Social Media Post Metrics | `socialMediaPostMetrics` | Post metrics. &gt;Requests to this endpoint are free and do not consume any API units. |
| Subscription Limits And Usage | `subscriptionInfoLimitsAndUsage` | Limits and usage. &gt;Requests to this endpoint are free and do not consume any API units. |
| Top Domains By Domain Rating | `publicDomainRatingTopDomains` | Domain rating top domains. &gt;Requests to this endpoint are free, yet require an APIv3 key. &gt;APIv3 keys are free to generate and use. If you don't have an Ahrefs account, here's how to get the key for free: &gt;1. [Sign up](https://ahrefs.com/) for a free Ahrefs account (if you don't have one) &gt;2. Generate an API key in [Account settings → API keys](https://app.ahrefs.com/account/api-keys) &gt;3. Add it to your requests: `Authorization: Bearer &lt;token&gt;` Returns the top 1M domains ranked by Ahrefs Domain Rating, together with each domain's current Domain Rating. Use `from` and `to` to request a range of rank positions. Each request can return up to 250k rows (e.g. `from=1&to=250000`). |
| Topics | `brandRadarTopics` | Topics. &gt;Requests to this endpoint consume API units based on the `prompts` parameter: requests returning only custom prompt data are free, while requests including Ahrefs prompt data follow standard API unit pricing. |
| Update Brand Radar Prompts | `updateManagementBrandRadarPrompts` | Update Brand Radar prompts. &gt;Requests to this endpoint are free and do not consume any API units. |
| Update Brand Radar Report | `updateManagementBrandRadarReports` | Update Brand Radar Reports. &gt;Requests to this endpoint are free and do not consume any API units. |
| Update Project | `updateManagementUpdateProject` | Update Project. &gt;Requests to this endpoint are free and do not consume any API units. At least one of `access` or `folder` must be set. |
| Update Social Media Post | `updateSocialMediaPost` | Update post. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Browser Versions | `webAnalyticsBrowserVersions` | Browser Versions. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Browser Versions Chart | `webAnalyticsBrowserVersionsChart` | Browser Versions Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Browsers | `webAnalyticsBrowsers` | Browsers. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Browsers Chart | `webAnalyticsBrowsersChart` | Browsers Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Chart | `webAnalyticsChart` | Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Cities | `webAnalyticsCities` | Cities. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Cities Chart | `webAnalyticsCitiesChart` | Cities Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Continents | `webAnalyticsContinents` | Continents. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Continents Chart | `webAnalyticsContinentsChart` | Continents Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Countries | `webAnalyticsCountries` | Countries. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Countries Chart | `webAnalyticsCountriesChart` | Countries Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Devices | `webAnalyticsDevices` | Devices. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Devices Chart | `webAnalyticsDevicesChart` | Devices Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Entry Pages | `webAnalyticsEntryPages` | Entry Pages. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Entry Pages Chart | `webAnalyticsEntryPagesChart` | Entry Pages Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Exit Pages | `webAnalyticsExitPages` | Exit Pages. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Exit Pages Chart | `webAnalyticsExitPagesChart` | Exit Pages Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Languages | `webAnalyticsLanguages` | Languages. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Languages Chart | `webAnalyticsLanguagesChart` | Languages Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Operating System Versions | `webAnalyticsOperatingSystemsVersions` | Operating Systems Versions. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Operating System Versions Chart | `webAnalyticsOperatingSystemsVersionsChart` | Operating Systems Versions Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Operating Systems | `webAnalyticsOperatingSystems` | Operating Systems. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Operating Systems Chart | `webAnalyticsOperatingSystemsChart` | Operating Systems Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Referrers | `webAnalyticsReferrers` | Referrers. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Referrers Chart | `webAnalyticsReferrersChart` | Referrers Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Source Channels | `webAnalyticsSourceChannels` | Source Channels. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Source Channels Chart | `webAnalyticsSourceChannelsChart` | Source Channels Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Sources | `webAnalyticsSources` | Sources. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Sources Chart | `webAnalyticsSourcesChart` | Sources Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Stats | `webAnalyticsStats` | Stats. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Top Pages | `webAnalyticsTopPages` | Top Pages. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics Top Pages Chart | `webAnalyticsTopPagesChart` | Top Pages Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics UTM Params | `webAnalyticsUtmParams` | UTM Parameters. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Analytics UTM Params Chart | `webAnalyticsUtmParamsChart` | UTM Parameters Chart. &gt;Requests to this endpoint are free and do not consume any API units. |
| Web Pages | `brandRadarWebPages` | Web Pages. Returns web pages that mention the requested brands or competitors. Brand mentions are matched against page titles and content from Ahrefs' web index. |

</details>
