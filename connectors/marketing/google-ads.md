---
description: "Google Ads API v25 connector (https://googleads.googleapis.com/v25)."
hidden: true
---

# Google Ads

<img src="../../.gitbook/assets/connectors/lg/google-ads.png" alt="Google Ads logo">

Google Ads API v25 connector (https://googleads.googleapis.com/v25). Manage Google Ads accounts through the query+mutate API: list accessible customers, run GAQL reporting queries (googleAds:search / googleAds:searchStream), and mutate resources either heterogeneously (googleAds:mutate) or via per-resource mutate services for campaigns, campaign budgets, ad groups, ad group ads, keywords and other criteria, bid modifiers, conversion actions, bidding strategies, labels, shared sets, user lists, and assets. Includes keyword planning (generateKeywordIdeas / generateKeywordHistoricalMetrics), offline conversion uploads, and GoogleAdsFieldService metadata. Auth: Google OAuth 2.0 (scope https://www.googleapis.com/auth/adwords) PLUS a mandatory developer-token header, and a login-customer-id header for manager (MCC) accounts.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [ads.google.com](https://ads.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleAds` |

## Use it

Add Google Ads from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleAds.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Operations Batch Jobs | `addOperationsBatchJobs` | Add operations to the batch job. (POST v25/{+resourceName}:addOperations) |
| Add Operations Offline User Data Jobs | `addOperationsOfflineUserDataJobs` | Adds operations to the offline user data job. (POST v25/{+resourceName}:addOperations) |
| Append Lead Conversation Local Services | `appendLeadConversationLocalServices` | RPC to append Local Services Lead Conversation resources to Local Services Lead resources. (POST v25/customers/{+customerId}/localServices:appendLeadConversation) |
| Apply Incentive Incentives | `applyIncentiveIncentives` | Applies the incentive for the ads customer. (POST v25/customers/{+customerId}/incentives/{+selectedIncentiveId}:applyIncentive) |
| Apply Recommendations | `applyRecommendations` | Applies given recommendations with corresponding apply parameters. (POST v25/customers/{+customerId}/recommendations:apply) |
| Book Campaigns Reservations | `bookCampaignsReservations` | Books the requested campaigns. This request can have a latency of 30 seconds. (POST v25/customers/{+customerId}/reservations:bookCampaigns) |
| Create Account Links | `createAccountLinks` | Creates an account link. (POST v25/customers/{+customerId}/accountLinks:create) |
| Create Customer Client | `createCustomerClient` | Creates a new client under manager. The new client customer is returned. (POST v25/customers/{+customerId}:createCustomerClient) |
| Create Data Links | `createDataLinks` | Creates a data link. The requesting Google Ads account name and account ID will be shared with the third party (such as YouTube creators for video links) to whom you are creating the link with. (POST v25/customers/{+customerId}/dataLinks:create) |
| Create Offline User Data Jobs | `createOfflineUserDataJobs` | Creates an offline user data job. (POST v25/customers/{+customerId}/offlineUserDataJobs:create) |

<details>

<summary>See 161 more actions</summary>

* **Create Product Link Invitations** `createProductLinkInvitations`: Creates a product link invitation. (POST v25/customers/{+customerId}/productLinkInvitations:create)
* **Create Product Links** `createProductLinks`: Creates a product link. (POST v25/customers/{+customerId}/productLinks:create)
* **Dismiss Recommendations** `dismissRecommendations`: Dismisses given recommendations. (POST v25/customers/{+customerId}/recommendations:dismiss)
* **Enable P Max Brand Guidelines Campaigns** `enablePMaxBrandGuidelinesCampaigns`: Enables Brand Guidelines for Performance Max campaigns. (POST v25/customers/{+customerId}/campaigns:enablePMaxBrandGuidelines)
* **End Experiment Experiments** `endExperimentExperiments`: Immediately ends an experiment, changing the experiment's scheduled end date and without waiting for end of day. End date is updated to be the time of the request. (POST v25/{+experiment}:endExperiment)
* **Fetch Incentive Incentives** `fetchIncentiveIncentives`: Returns incentives for a given user. (GET v25/incentives:fetchIncentive)
* **Generate Ad Group Themes** `generateAdGroupThemes`: Returns a list of suggested AdGroups and suggested modifications (text, match type) for the given keywords. (POST v25/customers/{+customerId}:generateAdGroupThemes)
* **Generate Audience Composition Insights** `generateAudienceCompositionInsights`: Returns a collection of attributes that are represented in an audience of interest, with metrics that compare each attribute's share of the audience with its share of a baseline audience. (POST v25/customers/{+customerId}:generateAudienceCompositionInsights)
* **Generate Audience Definition** `generateAudienceDefinition`: Returns a collection of audience attributes using generative AI based on the provided audience description. (POST v25/customers/{+customerId}:generateAudienceDefinition)
* **Generate Audience Overlap Insights** `generateAudienceOverlapInsights`: Returns a collection of audience attributes along with estimates of the overlap between their potential YouTube reach and that of a given input attribute. (POST v25/customers/{+customerId}:generateAudienceOverlapInsights)
* **Generate Benchmarks Metrics** `generateBenchmarksMetrics`: Returns YouTube advertisement metrics for the given client against industry benchmarks. (POST v25/customers/{+customerId}:generateBenchmarksMetrics)
* **Generate Conversion Rates** `generateConversionRates`: Returns a collection of conversion rate suggestions for supported plannable products. (POST v25:generateConversionRates)
* **Generate Creator Insights** `generateCreatorInsights`: Returns insights for a collection of YouTube Creators and Channels. (POST v25/customers/{+customerId}:generateCreatorInsights)
* **Generate Images Asset Generations** `generateImagesAssetGenerations`: Uses generative AI to generate images that can be used as assets in a campaign. (POST v25/customers/{+customerId}/assetGenerations:generateImages)
* **Generate Insights Finder Report** `generateInsightsFinderReport`: Creates a saved report that can be viewed in the Insights Finder tool. (POST v25/customers/{+customerId}:generateInsightsFinderReport)
* **Generate Keyword Forecast Metrics** `generateKeywordForecastMetrics`: Returns metrics (such as impressions, clicks, total cost) of a keyword forecast for the given campaign. (POST v25/customers/{+customerId}:generateKeywordForecastMetrics)
* **Generate Keyword Historical Metrics** `generateKeywordHistoricalMetrics`: Returns a list of keyword historical metrics. (POST v25/customers/{+customerId}:generateKeywordHistoricalMetrics)
* **Generate Keyword Ideas** `generateKeywordIdeas`: Returns a list of keyword ideas. (POST v25/customers/{+customerId}:generateKeywordIdeas)
* **Generate P Max Draft Campaign Smart Campaign Settings** `generatePMaxDraftCampaignSmartCampaignSettings`: Generates a Performance Max (PMax) draft campaign from an existing Smart campaign, initialized with a status of [CampaignStatus.PAUSED] and a creation status of [CampaignCreationStatus.INCOMPLETE]. Returns the draft PMax campaign ID and related entity IDs. Note: * Images are required for the draft PMax campaign to pass validation, so system default placeholder images are added automatically. Review and update the target images after the draft PMax campaign is generated. * Verify that the EU political advertising status ([Campaign.contains_eu_political_advertising]) is accurate. By default, this field is set to [EuPoliticalAdvertisingStatus.DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING] to satisfy Performance Max campaign validation requirements. (POST v25/{+resourceName}:generatePMaxDraftCampaign)
* **Generate Reach Forecast** `generateReachForecast`: Generates a reach forecast for a given targeting / product mix. (POST v25/customers/{+customerId}:generateReachForecast)
* **Generate Recommendations** `generateRecommendations`: Generates Recommendations based off the requested recommendation_types. (POST v25/customers/{+customerId}/recommendations:generate)
* **Generate Shareable Previews** `generateShareablePreviews`: Returns the requested Shareable Preview. (POST v25/customers/{+customerId}:generateShareablePreviews)
* **Generate Suggested Targeting Insights** `generateSuggestedTargetingInsights`: Returns a collection of targeting insights (e.g. targetable audiences) that are relevant to the requested audience. (POST v25/customers/{+customerId}:generateSuggestedTargetingInsights)
* **Generate Targeting Suggestion Metrics** `generateTargetingSuggestionMetrics`: Returns potential reach metrics for targetable audiences. This method helps answer questions like "How many Men aged 18+ interested in Camping can be reached on YouTube?" (POST v25/customers/{+customerId}:generateTargetingSuggestionMetrics)
* **Generate Text Asset Generations** `generateTextAssetGenerations`: Uses generative AI to generate text that can be used as assets in a campaign. (POST v25/customers/{+customerId}/assetGenerations:generateText)
* **Generate Trending Insights** `generateTrendingInsights`: Returns insights for trending content on YouTube. (POST v25/customers/{+customerId}:generateTrendingInsights)
* **Get Google Ads Field** `getGoogleAdsField`: Returns just the requested field. (GET v25/{+resourceName})
* **Get Identity Verification** `getIdentityVerification`: Returns Identity Verification information. (GET v25/customers/{+customerId}/getIdentityVerification)
* **Get Operations** `getOperations`: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. (GET v25/{+name})
* **Get Smart Campaign Status Smart Campaign Settings** `getSmartCampaignStatusSmartCampaignSettings`: Returns the status of the requested Smart campaign. (GET v25/{+resourceName}:getSmartCampaignStatus)
* **Graduate Experiment Experiments** `graduateExperimentExperiments`: Graduates an experiment to a full campaign. (POST v25/{+experiment}:graduateExperiment)
* **List Accessible Customers** `listAccessibleCustomers`: Returns resource names of customers directly accessible by the user authenticating the call. (GET v25/customers:listAccessibleCustomers)
* **List Async Errors Campaign Drafts** `listAsyncErrorsCampaignDrafts`: Returns all errors that occurred during CampaignDraft promote. Throws an error if called before campaign draft is promoted. Supports standard list paging. (GET v25/{+resourceName}:listAsyncErrors)
* **List Benchmarks Available Dates** `listBenchmarksAvailableDates`: Returns a date range that supports benchmarks. (POST v25:listBenchmarksAvailableDates)
* **List Benchmarks Locations** `listBenchmarksLocations`: Returns the list of locations that support benchmarks (for example, countries). (POST v25:listBenchmarksLocations)
* **List Benchmarks Products** `listBenchmarksProducts`: Returns the list of products that supports benchmarks. (POST v25:listBenchmarksProducts)
* **List Benchmarks Sources** `listBenchmarksSources`: Returns the list of benchmarks sources (for example, Industry Verticals). (POST v25:listBenchmarksSources)
* **List Experiment Async Errors Experiments** `listExperimentAsyncErrorsExperiments`: Returns all errors that occurred during the last Experiment update (either scheduling or promotion). Supports standard list paging. (GET v25/{+resourceName}:listExperimentAsyncErrors)
* **List Insights Eligible Dates Audience Insights** `listInsightsEligibleDatesAudienceInsights`: Lists date ranges for which audience insights data can be requested. (POST v25/audienceInsights:listInsightsEligibleDates)
* **List Invoices** `listInvoices`: Returns all invoices associated with a billing setup, for a given month. (GET v25/customers/{+customerId}/invoices)
* **List Payments Accounts** `listPaymentsAccounts`: Returns all payments accounts associated with all managers between the login customer ID and specified serving customer in the hierarchy, inclusive. (GET v25/customers/{+customerId}/paymentsAccounts)
* **List Plannable Locations** `listPlannableLocations`: Returns the list of plannable locations (for example, countries). (POST v25:listPlannableLocations)
* **List Plannable Products** `listPlannableProducts`: Returns the list of per-location plannable YouTube ad formats with allowed targeting. (POST v25:listPlannableProducts)
* **List Plannable User Interests** `listPlannableUserInterests`: Returns the list of plannable user interests. A plannable user interest is one that can be targeted in a reach forecast using ReachPlanService.GenerateReachForecast. (POST v25:listPlannableUserInterests)
* **List Plannable User Lists** `listPlannableUserLists`: Returns the list of plannable user lists with their plannable status. User lists may not be plannable for a number of reasons, including: - They are less than 10 days old. - They have a membership lifespan that is less than 30 days - They have less than 10,000 or more than 700,000 users. (POST v25:listPlannableUserLists)
* **List Results Batch Jobs** `listResultsBatchJobs`: Returns the results of the batch job. The job must be done. Supports standard list paging. (GET v25/{+resourceName}:listResults)
* **Move Manager Link Customer Manager Links** `moveManagerLinkCustomerManagerLinks`: Moves a client customer to a new manager customer. This simplifies the complex request that requires two operations to move a client customer to a new manager, for example: 1. Update operation with Status INACTIVE (previous manager) and, 2. Update operation with Status ACTIVE (new manager). (POST v25/customers/{+customerId}/customerManagerLinks:moveManagerLink)
* **Mutate** `mutate`: Executes mutate and actions operations. Mutate operations create, update, or remove resources. Actions perform custom operations. This method supports atomic transactions with multiple types of resources and actions. For example, you can atomically create a campaign and a campaign budget, or perform up to thousands of mutates atomically. This method is essentially a wrapper around a series of mutate methods. The only features it offers over calling those methods directly are: - Atomic transactions - Temp resource names (described below) - Somewhat reduced latency over making a series of mutate calls Note: Only resources that support atomic transactions are included, so this method can't replace all calls to individual services. ## Atomic Transaction Benefits Atomicity makes error handling much easier. If you're making a series of changes and one fails, it can leave your account in an inconsistent state. With atomicity, you either reach the chosen state directly, or the request fails an
* **Mutate Account Budget Proposals** `mutateAccountBudgetProposals`: Creates, updates, or removes account budget proposals. Operation statuses are returned. (POST v25/customers/{+customerId}/accountBudgetProposals:mutate)
* **Mutate Account Links** `mutateAccountLinks`: Creates or removes an account link. From V5, create is not supported through AccountLinkService.MutateAccountLink. Use AccountLinkService.CreateAccountLink instead. (POST v25/customers/{+customerId}/accountLinks:mutate)
* **Mutate Ad Group Ad Labels** `mutateAdGroupAdLabels`: Creates and removes ad group ad labels. Operation statuses are returned. (POST v25/customers/{+customerId}/adGroupAdLabels:mutate)
* **Mutate Ad Group Ads** `mutateAdGroupAds`: Creates, updates, or removes ads. Operation statuses are returned. (POST v25/customers/{+customerId}/adGroupAds:mutate)
* **Mutate Ad Group Asset Sets** `mutateAdGroupAssetSets`: Creates, or removes ad group asset sets. Operation statuses are returned. (POST v25/customers/{+customerId}/adGroupAssetSets:mutate)
* **Mutate Ad Group Assets** `mutateAdGroupAssets`: Creates, updates, or removes ad group assets. Operation statuses are returned. (POST v25/customers/{+customerId}/adGroupAssets:mutate)
* **Mutate Ad Group Bid Modifiers** `mutateAdGroupBidModifiers`: Creates, updates, or removes ad group bid modifiers. Operation statuses are returned. (POST v25/customers/{+customerId}/adGroupBidModifiers:mutate)
* **Mutate Ad Group Criteria** `mutateAdGroupCriteria`: Creates, updates, or removes criteria. Operation statuses are returned. (POST v25/customers/{+customerId}/adGroupCriteria:mutate)
* **Mutate Ad Group Criterion Customizers** `mutateAdGroupCriterionCustomizers`: Creates, updates or removes ad group criterion customizers. Operation statuses are returned. (POST v25/customers/{+customerId}/AdGroupCriterionCustomizers:mutate)
* **Mutate Ad Group Criterion Labels** `mutateAdGroupCriterionLabels`: Creates and removes ad group criterion labels. Operation statuses are returned. (POST v25/customers/{+customerId}/adGroupCriterionLabels:mutate)
* **Mutate Ad Group Customizers** `mutateAdGroupCustomizers`: Creates, updates or removes ad group customizers. Operation statuses are returned. (POST v25/customers/{+customerId}/adGroupCustomizers:mutate)
* **Mutate Ad Group Labels** `mutateAdGroupLabels`: Creates and removes ad group labels. Operation statuses are returned. (POST v25/customers/{+customerId}/adGroupLabels:mutate)
* **Mutate Ad Groups** `mutateAdGroups`: Creates, updates, or removes ad groups. Operation statuses are returned. (POST v25/customers/{+customerId}/adGroups:mutate)
* **Mutate Ad Parameters** `mutateAdParameters`: Creates, updates, or removes ad parameters. Operation statuses are returned. (POST v25/customers/{+customerId}/adParameters:mutate)
* **Mutate Ads** `mutateAds`: Updates ads. Operation statuses are returned. Updating ads is not supported for TextAd, ExpandedDynamicSearchAd, GmailAd and ImageAd. (POST v25/customers/{+customerId}/ads:mutate)
* **Mutate Asset Group Assets** `mutateAssetGroupAssets`: Creates, updates or removes asset group assets. Operation statuses are returned. (POST v25/customers/{+customerId}/assetGroupAssets:mutate)
* **Mutate Asset Group Listing Group Filters** `mutateAssetGroupListingGroupFilters`: Creates, updates or removes asset group listing group filters. Operation statuses are returned. (POST v25/customers/{+customerId}/assetGroupListingGroupFilters:mutate)
* **Mutate Asset Group Signals** `mutateAssetGroupSignals`: Creates or removes asset group signals. Operation statuses are returned. (POST v25/customers/{+customerId}/assetGroupSignals:mutate)
* **Mutate Asset Groups** `mutateAssetGroups`: Creates, updates or removes asset groups. Operation statuses are returned. (POST v25/customers/{+customerId}/assetGroups:mutate)
* **Mutate Asset Set Assets** `mutateAssetSetAssets`: Creates, updates or removes asset set assets. Operation statuses are returned. (POST v25/customers/{+customerId}/assetSetAssets:mutate)
* **Mutate Asset Sets** `mutateAssetSets`: Creates, updates or removes asset sets. Operation statuses are returned. (POST v25/customers/{+customerId}/assetSets:mutate)
* **Mutate Assets** `mutateAssets`: Creates assets. Operation statuses are returned. (POST v25/customers/{+customerId}/assets:mutate)
* **Mutate Audiences** `mutateAudiences`: Creates audiences. Operation statuses are returned. (POST v25/customers/{+customerId}/audiences:mutate)
* **Mutate Batch Jobs** `mutateBatchJobs`: Mutates a batch job. (POST v25/customers/{+customerId}/batchJobs:mutate)
* **Mutate Bidding Data Exclusions** `mutateBiddingDataExclusions`: Creates, updates, or removes data exclusions. Operation statuses are returned. (POST v25/customers/{+customerId}/biddingDataExclusions:mutate)
* **Mutate Bidding Seasonality Adjustments** `mutateBiddingSeasonalityAdjustments`: Creates, updates, or removes seasonality adjustments. Operation statuses are returned. (POST v25/customers/{+customerId}/biddingSeasonalityAdjustments:mutate)
* **Mutate Bidding Strategies** `mutateBiddingStrategies`: Creates, updates, or removes bidding strategies. Operation statuses are returned. (POST v25/customers/{+customerId}/biddingStrategies:mutate)
* **Mutate Billing Setups** `mutateBillingSetups`: Creates a billing setup, or cancels an existing billing setup. (POST v25/customers/{+customerId}/billingSetups:mutate)
* **Mutate Campaign Asset Sets** `mutateCampaignAssetSets`: Creates, updates or removes campaign asset sets. Operation statuses are returned. (POST v25/customers/{+customerId}/campaignAssetSets:mutate)
* **Mutate Campaign Assets** `mutateCampaignAssets`: Creates, updates, or removes campaign assets. Operation statuses are returned. (POST v25/customers/{+customerId}/campaignAssets:mutate)
* **Mutate Campaign Bid Modifiers** `mutateCampaignBidModifiers`: Creates, updates, or removes campaign bid modifiers. Operation statuses are returned. (POST v25/customers/{+customerId}/campaignBidModifiers:mutate)
* **Mutate Campaign Budgets** `mutateCampaignBudgets`: Creates, updates, or removes campaign budgets. Operation statuses are returned. (POST v25/customers/{+customerId}/campaignBudgets:mutate)
* **Mutate Campaign Conversion Goals** `mutateCampaignConversionGoals`: Creates, updates or removes campaign conversion goals. Operation statuses are returned. (POST v25/customers/{+customerId}/campaignConversionGoals:mutate)
* **Mutate Campaign Criteria** `mutateCampaignCriteria`: Creates, updates, or removes criteria. Operation statuses are returned. (POST v25/customers/{+customerId}/campaignCriteria:mutate)
* **Mutate Campaign Customizers** `mutateCampaignCustomizers`: Creates, updates or removes campaign customizers. Operation statuses are returned. (POST v25/customers/{+customerId}/campaignCustomizers:mutate)
* **Mutate Campaign Drafts** `mutateCampaignDrafts`: Creates, updates, or removes campaign drafts. Operation statuses are returned. (POST v25/customers/{+customerId}/campaignDrafts:mutate)
* **Mutate Campaign Goal Configs** `mutateCampaignGoalConfigs`: Create or update campaign goal configs. (POST v25/customers/{+customerId}/CampaignGoalConfigs:mutate)
* **Mutate Campaign Groups** `mutateCampaignGroups`: Creates, updates, or removes campaign groups. Operation statuses are returned. (POST v25/customers/{+customerId}/campaignGroups:mutate)
* **Mutate Campaign Labels** `mutateCampaignLabels`: Creates and removes campaign-label relationships. Operation statuses are returned. (POST v25/customers/{+customerId}/campaignLabels:mutate)
* **Mutate Campaign Shared Sets** `mutateCampaignSharedSets`: Creates or removes campaign shared sets. Operation statuses are returned. (POST v25/customers/{+customerId}/campaignSharedSets:mutate)
* **Mutate Campaigns** `mutateCampaigns`: Creates, updates, or removes campaigns. Operation statuses are returned. (POST v25/customers/{+customerId}/campaigns:mutate)
* **Mutate Conversion Actions** `mutateConversionActions`: Creates, updates or removes conversion actions. Operation statuses are returned. (POST v25/customers/{+customerId}/conversionActions:mutate)
* **Mutate Conversion Custom Variables** `mutateConversionCustomVariables`: Creates or updates conversion custom variables. Operation statuses are returned. (POST v25/customers/{+customerId}/conversionCustomVariables:mutate)
* **Mutate Conversion Goal Campaign Configs** `mutateConversionGoalCampaignConfigs`: Creates, updates or removes conversion goal campaign config. Operation statuses are returned. (POST v25/customers/{+customerId}/conversionGoalCampaignConfigs:mutate)
* **Mutate Conversion Value Rule Sets** `mutateConversionValueRuleSets`: Creates, updates or removes conversion value rule sets. Operation statuses are returned. (POST v25/customers/{+customerId}/conversionValueRuleSets:mutate)
* **Mutate Conversion Value Rules** `mutateConversionValueRules`: Creates, updates, or removes conversion value rules. Operation statuses are returned. (POST v25/customers/{+customerId}/conversionValueRules:mutate)
* **Mutate Custom Audiences** `mutateCustomAudiences`: Creates or updates custom audiences. Operation statuses are returned. (POST v25/customers/{+customerId}/customAudiences:mutate)
* **Mutate Custom Conversion Goals** `mutateCustomConversionGoals`: Creates, updates or removes custom conversion goals. Operation statuses are returned. (POST v25/customers/{+customerId}/customConversionGoals:mutate)
* **Mutate Custom Interests** `mutateCustomInterests`: Creates or updates custom interests. Operation statuses are returned. (POST v25/customers/{+customerId}/customInterests:mutate)
* **Mutate Customer** `mutateCustomer`: Updates a customer. Operation statuses are returned. (POST v25/customers/{+customerId}:mutate)
* **Mutate Customer Asset Sets** `mutateCustomerAssetSets`: Creates, or removes customer asset sets. Operation statuses are returned. (POST v25/customers/{+customerId}/customerAssetSets:mutate)
* **Mutate Customer Assets** `mutateCustomerAssets`: Creates, updates, or removes customer assets. Operation statuses are returned. (POST v25/customers/{+customerId}/customerAssets:mutate)
* **Mutate Customer Client Links** `mutateCustomerClientLinks`: Creates or updates a customer client link. Operation statuses are returned. (POST v25/customers/{+customerId}/customerClientLinks:mutate)
* **Mutate Customer Conversion Goals** `mutateCustomerConversionGoals`: Creates, updates or removes customer conversion goals. Operation statuses are returned. (POST v25/customers/{+customerId}/customerConversionGoals:mutate)
* **Mutate Customer Customizers** `mutateCustomerCustomizers`: Creates, updates or removes customer customizers. Operation statuses are returned. (POST v25/customers/{+customerId}/CustomerCustomizers:mutate)
* **Mutate Customer Labels** `mutateCustomerLabels`: Creates and removes customer-label relationships. Operation statuses are returned. (POST v25/customers/{+customerId}/customerLabels:mutate)
* **Mutate Customer Manager Links** `mutateCustomerManagerLinks`: Updates customer manager links. Operation statuses are returned. (POST v25/customers/{+customerId}/customerManagerLinks:mutate)
* **Mutate Customer Negative Criteria** `mutateCustomerNegativeCriteria`: Creates or removes criteria. Operation statuses are returned. (POST v25/customers/{+customerId}/customerNegativeCriteria:mutate)
* **Mutate Customer Sk Ad Network Conversion Value Schemas** `mutateCustomerSkAdNetworkConversionValueSchemas`: Creates or updates the CustomerSkAdNetworkConversionValueSchema. (POST v25/customers/{+customerId}/customerSkAdNetworkConversionValueSchemas:mutate)
* **Mutate Customer User Access Invitations** `mutateCustomerUserAccessInvitations`: Creates or removes an access invitation. (POST v25/customers/{+customerId}/customerUserAccessInvitations:mutate)
* **Mutate Customer User Accesses** `mutateCustomerUserAccesses`: Updates, removes permission of a user on a given customer. Operation statuses are returned. (POST v25/customers/{+customerId}/customerUserAccesses:mutate)
* **Mutate Customizer Attributes** `mutateCustomizerAttributes`: Creates, updates or removes customizer attributes. Operation statuses are returned. (POST v25/customers/{+customerId}/customizerAttributes:mutate)
* **Mutate Experiment Arms** `mutateExperimentArms`: Creates, updates, or removes experiment arms. Operation statuses are returned. (POST v25/customers/{+customerId}/experimentArms:mutate)
* **Mutate Experiments** `mutateExperiments`: Creates, updates, or removes experiments. Operation statuses are returned. (POST v25/customers/{+customerId}/experiments:mutate)
* **Mutate Goals** `mutateGoals`: Create or update goals. (POST v25/customers/{+customerId}/Goals:mutate)
* **Mutate Keyword Plan Ad Group Keywords** `mutateKeywordPlanAdGroupKeywords`: Creates, updates, or removes Keyword Plan ad group keywords. Operation statuses are returned. (POST v25/customers/{+customerId}/keywordPlanAdGroupKeywords:mutate)
* **Mutate Keyword Plan Ad Groups** `mutateKeywordPlanAdGroups`: Creates, updates, or removes Keyword Plan ad groups. Operation statuses are returned. (POST v25/customers/{+customerId}/keywordPlanAdGroups:mutate)
* **Mutate Keyword Plan Campaign Keywords** `mutateKeywordPlanCampaignKeywords`: Creates, updates, or removes Keyword Plan campaign keywords. Operation statuses are returned. (POST v25/customers/{+customerId}/keywordPlanCampaignKeywords:mutate)
* **Mutate Keyword Plan Campaigns** `mutateKeywordPlanCampaigns`: Creates, updates, or removes Keyword Plan campaigns. Operation statuses are returned. (POST v25/customers/{+customerId}/keywordPlanCampaigns:mutate)
* **Mutate Keyword Plans** `mutateKeywordPlans`: Creates, updates, or removes keyword plans. Operation statuses are returned. (POST v25/customers/{+customerId}/keywordPlans:mutate)
* **Mutate Labels** `mutateLabels`: Creates, updates, or removes labels. Operation statuses are returned. (POST v25/customers/{+customerId}/labels:mutate)
* **Mutate Recommendation Subscription Recommendation Subscriptions** `mutateRecommendationSubscriptionRecommendationSubscriptions`: Mutates given subscription with corresponding apply parameters. (POST v25/customers/{+customerId}/recommendationSubscriptions:mutateRecommendationSubscription)
* **Mutate Remarketing Actions** `mutateRemarketingActions`: Creates or updates remarketing actions. Operation statuses are returned. (POST v25/customers/{+customerId}/remarketingActions:mutate)
* **Mutate Shared Criteria** `mutateSharedCriteria`: Creates or removes shared criteria. Operation statuses are returned. (POST v25/customers/{+customerId}/sharedCriteria:mutate)
* **Mutate Shared Sets** `mutateSharedSets`: Creates, updates, or removes shared sets. Operation statuses are returned. (POST v25/customers/{+customerId}/sharedSets:mutate)
* **Mutate Smart Campaign Settings** `mutateSmartCampaignSettings`: Updates Smart campaign settings for campaigns. (POST v25/customers/{+customerId}/smartCampaignSettings:mutate)
* **Mutate User List Customer Types** `mutateUserListCustomerTypes`: Attach or remove user list customer types. Operation statuses are returned. (POST v25/customers/{+customerId}/userListCustomerTypes:mutate)
* **Mutate User Lists** `mutateUserLists`: Creates or updates user lists. Operation statuses are returned. (POST v25/customers/{+customerId}/userLists:mutate)
* **Promote Campaign Drafts** `promoteCampaignDrafts`: Promotes the changes in a draft back to the base campaign. This method returns a Long Running Operation (LRO) indicating if the Promote is done. Use google.longrunning.Operations.GetOperation to poll the LRO until it is done. Only a done status is returned in the response. See the status in the Campaign Draft resource to determine if the promotion was successful. If the LRO failed, use CampaignDraftService.ListCampaignDraftAsyncErrors to view the list of error reasons. (POST v25/{+campaignDraft}:promote)
* **Promote Experiment Experiments** `promoteExperimentExperiments`: Promotes the trial campaign thus applying changes in the trial campaign to the base campaign. This method returns a long running operation that tracks the promotion of the experiment campaign. If it fails, a list of errors can be retrieved using the ListExperimentAsyncErrors method. The operation's metadata will be a string containing the resource name of the created experiment. (POST v25/{+resourceName}:promoteExperiment)
* **Provide Lead Feedback Local Services Leads** `provideLeadFeedbackLocalServicesLeads`: RPC to provide feedback on Local Services Lead resources. (POST v25/{+resourceName}:provideLeadFeedback)
* **Quote Campaigns Reservations** `quoteCampaignsReservations`: Proposes quotes for booking campaigns. This request can have a latency of 30 seconds. (POST v25/customers/{+customerId}/reservations:quoteCampaigns)
* **Regenerate Shareable Link Id Third Party App Analytics Links** `regenerateShareableLinkIdThirdPartyAppAnalyticsLinks`: Regenerate ThirdPartyAppAnalyticsLink.shareable_link_id that should be provided to the third party when setting up app analytics. (POST v25/{+resourceName}:regenerateShareableLinkId)
* **Remove Automatically Created Assets Ad Group Ads** `removeAutomaticallyCreatedAssetsAdGroupAds`: Remove text customization (formerly automatically created assets) from an ad. (POST v25/{+adGroupAd}:removeAutomaticallyCreatedAssets)
* **Remove Campaign Automatically Created Asset** `removeCampaignAutomaticallyCreatedAsset`: Removes text customization (formerly automatically created assets) from a campaign. (POST v25/customers/{+customerId}:removeCampaignAutomaticallyCreatedAsset)
* **Remove Data Links** `removeDataLinks`: Remove a data link. (POST v25/customers/{+customerId}/dataLinks:remove)
* **Remove Product Link Invitations** `removeProductLinkInvitations`: Remove a product link invitation. (POST v25/customers/{+customerId}/productLinkInvitations:remove)
* **Remove Product Links** `removeProductLinks`: Removes a product link. (POST v25/customers/{+customerId}/productLinks:remove)
* **Remove You Tube Video Uploads** `removeYouTubeVideoUploads`: Removes YouTube videos uploaded using this API. (POST v25/customers/{+customerId}/youTubeVideoUploads:remove)
* **Resolve Multi Party Auth Review** `resolveMultiPartyAuthReview`: Resolves the status of a Multi-Party Authorization review. (POST v25/customers/{+customerId}/multiPartyAuthReview:resolve)
* **Run Batch Jobs** `runBatchJobs`: Runs the batch job. The Operation.metadata field type is BatchJobMetadata. When finished, the long running operation will not contain errors or a response. Instead, use ListBatchJobResults to get the results of the job. (POST v25/{+resourceName}:run)
* **Run Offline User Data Jobs** `runOfflineUserDataJobs`: Runs the offline user data job. When finished, the long running operation will contain the processing result or failure information, if any. (POST v25/{+resourceName}:run)
* **Schedule Experiment Experiments** `scheduleExperimentExperiments`: Schedule an experiment. The in design campaign will be converted into a real campaign (called the experiment campaign) that will begin serving ads if successfully created. The experiment is scheduled immediately with status INITIALIZING. This method returns a long running operation that tracks the forking of the in design campaign. If the forking fails, a list of errors can be retrieved using the ListExperimentAsyncErrors method. The operation's metadata will be a string containing the resource name of the created experiment. (POST v25/{+resourceName}:scheduleExperiment)
* **Search** `search`: Returns all rows that match the search query. (POST v25/customers/{+customerId}/googleAds:search)
* **Search Audience Insights Attributes** `searchAudienceInsightsAttributes`: Searches for audience attributes that can be used to generate insights. (POST v25/customers/{+customerId}:searchAudienceInsightsAttributes)
* **Search Google Ads Fields** `searchGoogleAdsFields`: Returns all fields that match the search query. (POST v25/googleAdsFields:search)
* **Search Stream** `searchStream`: Returns all rows that match the search stream query. (POST v25/customers/{+customerId}/googleAds:searchStream)
* **Start Identity Verification** `startIdentityVerification`: Starts Identity Verification for a given verification program type. Statuses are returned. (POST v25/customers/{+customerId}:startIdentityVerification)
* **Suggest Brands** `suggestBrands`: Rpc to return a list of matching brands based on a prefix for this customer. (POST v25/customers/{+customerId}:suggestBrands)
* **Suggest Geo Target Constants** `suggestGeoTargetConstants`: Returns GeoTargetConstant suggestions by location name or by resource name. (POST v25/geoTargetConstants:suggest)
* **Suggest Keyword Theme Constants** `suggestKeywordThemeConstants`: Returns KeywordThemeConstant suggestions by keyword themes. (POST v25/keywordThemeConstants:suggest)
* **Suggest Keyword Themes** `suggestKeywordThemes`: Suggests keyword themes to advertise on. (POST v25/customers/{+customerId}:suggestKeywordThemes)
* **Suggest Smart Campaign Ad** `suggestSmartCampaignAd`: Suggests a Smart campaign ad compatible with the Ad family of resources, based on data points such as targeting and the business to advertise. (POST v25/customers/{+customerId}:suggestSmartCampaignAd)
* **Suggest Smart Campaign Budget Options** `suggestSmartCampaignBudgetOptions`: Returns BudgetOption suggestions. (POST v25/customers/{+customerId}:suggestSmartCampaignBudgetOptions)
* **Suggest Travel Assets** `suggestTravelAssets`: Returns Travel Asset suggestions. Asset suggestions are returned on a best-effort basis. There are no guarantees that all possible asset types will be returned for any given hotel property. (POST v25/customers/{+customerId}:suggestTravelAssets)
* **Update Data Links** `updateDataLinks`: Update a data link. (POST v25/customers/{+customerId}/dataLinks:update)
* **Update Product Link Invitations** `updateProductLinkInvitations`: Update a product link invitation. (POST v25/customers/{+customerId}/productLinkInvitations:update)
* **Update You Tube Video Uploads** `updateYouTubeVideoUploads`: Updates YouTube video's metadata, but only for videos uploaded using this API. (POST v25/customers/{+customerId}/youTubeVideoUploads:update)
* **Upload Call Conversions** `uploadCallConversions`: Processes the given call conversions. (POST v25/customers/{+customerId}:uploadCallConversions)
* **Upload Click Conversions** `uploadClickConversions`: Processes the given click conversions. (POST v25/customers/{+customerId}:uploadClickConversions)
* **Upload Conversion Adjustments** `uploadConversionAdjustments`: Processes the given conversion adjustments. (POST v25/customers/{+customerId}:uploadConversionAdjustments)
* **Upload Media** `uploadMedia`: Uploads a video to Google-managed or advertiser owned (brand) YouTube channel. (POST v25/customers/{+customerId}/youTubeVideoUploads:create)
* **Upload User Data** `uploadUserData`: Uploads the given user data. (POST v25/customers/{+customerId}:uploadUserData)

</details>
