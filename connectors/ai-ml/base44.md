---
description: "Base44 is an AI app-building platform."
hidden: true
---

# Base44

<img src="../../.gitbook/assets/connectors/base44.png" alt="Base44 logo" width="64">

Base44 is an AI app-building platform. This connector covers the Base44 App Management API: apps, entity records and entity schemas, workflows and workflow runs, analytics, app checkpoints, the AI builder chat and coding surface, deployments, GitHub sync, custom domains and custom email domains, URL redirects, SEO, security scans, secrets, social calendar and virality campaigns, Stripe and Wix payments, and the Google Ads advertising surface.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [base44.com](https://base44.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Slug** | `base44` |

## Use it

Add Base44 from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.base44.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Google Ads Asset | `acceptGoogleAdsAsset` | Puts a generated asset live on a Google Ads campaign for an app, attaching it to the campaign's asset groups. |
| Accept Google Ads Terms | `acceptGoogleAdsTerms` | Records acceptance of the Google Ads terms for an app's advertising account, which is required before campaigns can run. |
| Aggregate Analytics Events By Field | `aggregateAnalyticsEventsByField` | Breaks a Base44 app's analytics events down by the value of a field so you can rank them, for example the busiest pages or the most common countries. Every metric must set the field it groups by. |
| Aggregate Analytics Events Over Time | `aggregateAnalyticsEventsOverTime` | Aggregates a Base44 app's analytics events into time buckets so you can chart them, and also returns each metric over the whole range. Events are kept for 60 days. |
| Analyze Workflow Run | `analyzeWorkflowRun` | Asks Base44 to explain why an automation workflow run failed and returns the generated explanation. |
| Apply Google Ads Budget Recommendation | `applyGoogleAdsBudgetRecommendation` | Accepts a Google budget recommendation for a campaign on an app, moving the campaign to the recommended daily budget. This changes what the campaign spends each day. |
| Approve Scheduled Social Posts | `approveScheduledSocialPosts` | Approves proposed social media posts on a Base44 app so they move from proposal to scheduled and will be published. Posts that cannot be approved are reported back with the status that blocked them. |
| Archive Workflow | `archiveWorkflow` | Archives an automation workflow on a Base44 app. The workflow stops running and is hidden from List Workflows unless archived workflows are included. Restore it with Restore Workflow. |
| Ask The Google Ads Assistant | `askTheGoogleAdsAssistant` | Asks Base44's advertising assistant a question about an app's Google Ads setup or performance and returns its answer. The assistant only explains; it changes nothing. |
| Autocomplete Google Ads Keyword Themes | `autocompleteGoogleAdsKeywordThemes` | Suggests Google Ads keyword themes matching what has been typed so far, for a keyword picker. |

<details>

<summary>See 204 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Build Google Ads Tracking Fix Prompt | `buildGoogleAdsTrackingFixPrompt` | Produces a builder prompt that adds the missing Google Ads conversion tracking to an app. Set Wire Events to also create the conversion actions and mappings the prompt relies on. |
| Bulk Update Google Ads Campaign Budgets | `bulkUpdateGoogleAdsCampaignBudgets` | Sets new daily budgets on several Google Ads campaigns at once. Raising a budget raises what the campaign spends each day. |
| Cancel Workflow Run | `cancelWorkflowRun` | Stops an automation workflow run that is still in progress on a Base44 app. |
| Configure Live Stripe Keys | `configureLiveStripeKeys` | Puts a Base44 app into live Stripe mode using API keys from your own Stripe account, so real payments are taken. Handle these keys as secrets. |
| Connect GitHub Repository | `connectGithubRepository` | Creates or attaches a GitHub repository for a Base44 app so the app's source is kept in sync with it. |
| Count App Users | `countAppUsers` | Returns how many user accounts a Base44 app has. This reads the app's real user accounts, unlike Count Entity Records with an entity named User. |
| Count Entity Records | `countEntityRecords` | Returns how many records one of a Base44 app's entities holds, excluding deleted records. |
| Create App | `createApp` | Creates a new Base44 app. Send an initial message to build the app from a prompt, or send no fields at all to create an empty app. Building from a prompt runs in the background and consumes workspace credits. |
| Create App Checkpoint | `createAppCheckpoint` | Saves the current state of a Base44 app as a named checkpoint you can deploy or restore later. Nothing is created when the app has no changes since the last checkpoint. |
| Create Embedded Google Ads Payment Setup | `createEmbeddedGoogleAdsPaymentSetup` | Starts an embedded Stripe flow for adding a payment method to an app's Google Ads billing, returning the client secret needed to mount the card form in your own page. |
| Create Entity Record | `createEntityRecord` | Creates a record in one of a Base44 app's entities. Pass the record's fields as additional top-level inputs using the names the entity's schema defines; they are sent as the JSON request body. |
| Create Entity Schema | `createEntitySchema` | Defines a new entity on a Base44 app from a JSON Schema. Once created, the entity can hold records through the entity record actions. |
| Create Google Ads Campaign | `createGoogleAdsCampaign` | Creates a Google Ads campaign for an app with the daily budget you set. A live campaign spends real advertising money every day it runs. |
| Create Google Ads Campaign Brief | `createGoogleAdsCampaignBrief` | Saves a campaign brief on an app, holding the business details, keywords, budget, copy and schedule a Google Ads campaign would be built from. Saving a brief does not create a campaign or spend anything. |
| Create Google Ads Conversion Mapping | `createGoogleAdsConversionMapping` | Adds a rule that turns a change to one of an app's entities into a Google Ads conversion, so campaigns can be optimised against it. |
| Create Google Ads Payment Setup | `createGoogleAdsPaymentSetup` | Starts a hosted Stripe flow for adding a payment method to an app's Google Ads billing, and returns the checkout link to send the account owner to. |
| Create Sandbox Checkpoint | `createSandboxCheckpoint` | Commits the current state of a Base44 app's development sandbox as a checkpoint, so sandbox edits become a restorable version of the app. |
| Create Scheduled Social Post | `createScheduledSocialPost` | Adds a social media post to a Base44 app's content calendar for publishing at a given time. |
| Create Stripe Price | `createStripePrice` | Adds a price to a Stripe product sold by a Base44 app. Set a recurring interval to make it a subscription price, or leave it out for a one-off charge. |
| Create Stripe Product | `createStripeProduct` | Creates a product in the Stripe account connected to a Base44 app, so the app can sell it. |
| Create URL Redirect | `createUrlRedirect` | Adds a URL redirect to a Base44 app so visitors reaching the source path are sent to the target path. |
| Create Workflow | `createWorkflow` | Creates an automation workflow on a Base44 app from a step definition and a trigger. Validate the definition first with Validate Workflow Definition. |
| Delete App | `deleteApp` | Moves a Base44 app to the trash. The live app goes offline immediately and stops appearing in List Apps. Only the app owner or a workspace admin can delete an app. |
| Delete Custom Domain | `deleteCustomDomain` | Removes a custom domain from a Base44 app's account entirely. |
| Delete Entity Record | `deleteEntityRecord` | Deletes a record from one of a Base44 app's entities. The record stops appearing in List Entity Records. |
| Delete Entity Schema | `deleteEntitySchema` | Removes one entity definition from a Base44 app, together with the records stored under it. |
| Delete Google Ads Campaign | `deleteGoogleAdsCampaign` | Removes a Google Ads campaign from an app so it stops running and stops spending. |
| Delete Google Ads Campaign Brief | `deleteGoogleAdsCampaignBrief` | Removes a saved campaign brief from an app. Any campaign already built from it is unaffected. |
| Delete Google Ads Conversion Mapping | `deleteGoogleAdsConversionMapping` | Removes a rule that turns an app's entity events into Google Ads conversions, so those events stop being reported. |
| Delete Scheduled Social Post | `deleteScheduledSocialPost` | Removes a social media post from a Base44 app's content calendar so it is not published. |
| Delete URL Redirect | `deleteUrlRedirect` | Removes a URL redirect from a Base44 app so the source path stops redirecting. |
| Deploy App | `deployApp` | Publishes a Base44 app to production so the latest changes go live for its users. The app's current version is deployed unless you name a specific checkpoint. |
| Disable Email Domain | `disableEmailDomain` | Stops a Base44 app from sending email through a custom domain and removes the domain from the app. |
| Disconnect Google Ads Account | `disconnectGoogleAdsAccount` | Disconnects an app's Google Ads account, ending its budget so campaigns stop spending. |
| Disconnect Payments By Wix | `disconnectPaymentsByWix` | Disconnects Payments by Wix from a Base44 app so it stops taking payments through it. |
| Disconnect Wix Payments | `disconnectWixPayments` | Disconnects Wix Payments from a Base44 app so it stops taking payments through it. |
| Dismiss Google Ads Insight | `dismissGoogleAdsInsight` | Hides one Google Ads insight for an app so it stops being reported. |
| Edit And Resend Chat Message | `editAndResendChatMessage` | Rewrites an earlier prompt in a Base44 app's builder conversation and runs it again, discarding everything the builder did after it. This consumes workspace credits. |
| Edit Sandbox File | `editSandboxFile` | Applies find-and-replace edits to one source file in a Base44 app's development sandbox and returns the resulting diff. Set Dry Run to preview the diff without changing the file. |
| Enable Email Domain | `enableEmailDomain` | Registers a domain a Base44 app may send email from and returns the DNS records you have to publish before sending is allowed. |
| Enhance Google Ads Image Prompt | `enhanceGoogleAdsImagePrompt` | Rewrites a short description of an ad image into a fuller prompt for Base44's image generator, and returns both versions. |
| Estimate Google Ads Campaign Budget | `estimateGoogleAdsCampaignBudget` | Estimates the clicks and impressions a Google Ads campaign would get for a given daily budget and targeting. This is a forecast only and creates no campaign and no spend. |
| Export App Source Code | `exportAppSourceCode` | Downloads a Base44 app's full source code as a ZIP archive. |
| Generate Google Ads Assets | `generateGoogleAdsAssets` | Generates a full set of text and image assets for an app's Google Ads in one call. The assets are held in a generation session until accepted, and generating them consumes workspace credits. |
| Generate Google Ads Campaign Brief | `generateGoogleAdsCampaignBrief` | Asks Base44's AI to draft a campaign brief for an app from its business details, filling in audience, keywords, budget and copy. Drafting a brief creates no campaign and spends no ad money. |
| Generate Google Ads Copy | `generateGoogleAdsCopy` | Writes Google Ads headlines and descriptions for a business using Base44's AI, without creating or changing any campaign. |
| Generate Google Ads Image Assets | `generateGoogleAdsImageAssets` | Generates image assets for an app's Google Ads using Base44's AI. The images are held in a generation session until accepted, and generating them consumes workspace credits. |
| Generate Google Ads Text Assets | `generateGoogleAdsTextAssets` | Generates headline and description assets for an app's Google Ads using Base44's AI. The assets are held in a generation session until accepted, so nothing goes live yet. |
| Generate Social Content Plan | `generateSocialContentPlan` | Generates a full social media content plan for a Base44 app across the platforms you name, using the strategy agreed earlier in the flow. This consumes workspace credits. |
| Generate Social Post Image | `generateSocialPostImage` | Generates an image for one post in a Base44 app's social content plan from an image prompt. This consumes workspace credits. |
| Get Analytics User Stats | `getAnalyticsUserStats` | Returns how many of a Base44 app's users are active, live and inactive. A user counts once, in the bucket its most recent event falls into. |
| Get App | `getApp` | Returns a single Base44 app by its identifier, including its name, slug, workspace, build status and deployment details. |
| Get Custom Domain | `getCustomDomain` | Returns one custom domain attached to a Base44 app, including whether it is disabled and the last status check recorded for it. |
| Get Custom Domain Status | `getCustomDomainStatus` | Re-checks a custom domain's DNS and certificate state with the hosting provider and returns the refreshed domain record. |
| Get Entity Record | `getEntityRecord` | Returns a single record from one of a Base44 app's entities by its record identifier. |
| Get Entity Schema | `getEntitySchema` | Returns the stored JSON Schema of one entity on a Base44 app, including its properties, required fields and any row-level security rules. |
| Get GitHub Connection | `getGithubConnection` | Returns the GitHub repository a Base44 app is synced with, including whether the connection is active and whether this credential may push to it. |
| Get GitHub Organization Policy | `getGithubOrganizationPolicy` | Reports whether the Base44 workspace restricts which GitHub organizations an app may be connected to. |
| Get Google Ads Account | `getGoogleAdsAccount` | Returns the Google Ads account Base44 manages for an app, including its billing cadence, monthly spend cap and terms status, or nothing when the app has no account. |
| Get Google Ads Billing Status | `getGoogleAdsBillingStatus` | Reports whether an app's Google Ads billing has a payment method on file, and which card it is. |
| Get Google Ads Budget Boundaries | `getGoogleAdsBudgetBoundaries` | Returns the smallest and largest daily budget Google Ads will accept for a campaign type and currency, so a budget can be validated before it is set. |
| Get Google Ads Campaign | `getGoogleAdsCampaign` | Returns one Google Ads campaign belonging to an app, with its settings, budget and current status. |
| Get Google Ads Campaign Brief | `getGoogleAdsCampaignBrief` | Returns one saved campaign brief for an app, with the business details, keywords, budget and copy it holds. |
| Get Google Ads Campaign Metrics | `getGoogleAdsCampaignMetrics` | Returns per-campaign performance figures for an app's Google Ads over a date range. |
| Get Google Ads Campaign Targeting | `getGoogleAdsCampaignTargeting` | Returns who and where one Google Ads campaign on an app is targeting, including its locations and keyword themes. |
| Get Google Ads Conversion Stats | `getGoogleAdsConversionStats` | Returns the conversions and conversion value each of an app's Google Ads campaigns recorded over a date range. |
| Get Google Ads Hero Preview | `getGoogleAdsHeroPreview` | Returns a sample Google search result showing how an app's ad could look, for use as a preview. Base44 writes it in the app's own language. |
| Get Google Ads Launch Readiness | `getGoogleAdsLaunchReadiness` | Reports whether an app is ready to start advertising on Google Ads, covering its payment method, advertising account and landing page. |
| Get Google Ads Metric Trend | `getGoogleAdsMetricTrend` | Returns one Google Ads metric for an app plotted over time, so it can be charted. |
| Get Google Ads Performance Dashboard | `getGoogleAdsPerformanceDashboard` | Returns spend, impressions, clicks, conversions and return on ad spend for an app's Google Ads account over a date range, broken down per campaign. |
| Get Google Ads Tracking Script | `getGoogleAdsTrackingScript` | Returns the Google Ads conversion tracking script to embed in an app so conversions are reported back to Google. |
| Get Google Ads Workspace Debt | `getGoogleAdsWorkspaceDebt` | Reports any unpaid Google Ads balance on the workspace, why advertising is blocked and whether it can be settled now. |
| Get Last SEO Scan | `getLastSeoScan` | Returns the full result of the most recent SEO scan of a Base44 app, or null when the app has never been scanned. |
| Get Payment Analytics | `getPaymentAnalytics` | Returns revenue, refunds, disputes and customer counts for a Base44 app's payments, both as a summary and as a daily series. |
| Get Payments By Wix Dashboard Link | `getPaymentsByWixDashboardLink` | Returns a signed link into the Payments by Wix dashboard for a Base44 app, so the owner can manage that payment provider. |
| Get Published App URL | `getPublishedAppUrl` | Returns the public URL of a published Base44 app. The app must be live; an app that has never been published, or that has been unpublished, has no public URL. |
| Get Recent Payment Transactions | `getRecentPaymentTransactions` | Returns a Base44 app's most recent payment, refund and dispute events, newest first. |
| Get Sandbox Preview URL | `getSandboxPreviewUrl` | Returns a live preview URL for a Base44 app's development sandbox. The sandbox is started on demand, so the first call after it has been idle can take a while to return. |
| Get Scheduled Social Post | `getScheduledSocialPost` | Returns one scheduled social media post for a Base44 app, including its copy, image and publishing status. |
| Get Security Scan | `getSecurityScan` | Returns the result of the most recent security scan of a Base44 app, or a status of 'none' when the app has never been scanned. |
| Get SEO Score | `getSeoScore` | Returns the headline SEO score for a Base44 app, or null when the app has never been scanned. |
| Get SEO Settings | `getSeoSettings` | Returns a Base44 app's SEO settings, including which platform injections are enabled and any structured-data schemas configured for it. |
| Get Social Content State | `getSocialContentState` | Returns where a Base44 app stands in the guided social content flow, including the questions asked, the answers given, the agreed strategy and any generated plan. |
| Get Social Post Scheduling Job | `getSocialPostSchedulingJob` | Returns the progress of a social media post scheduling job started for a Base44 app. |
| Get Stripe Integration Status | `getStripeIntegrationStatus` | Returns how a Base44 app's Stripe integration is set up, including whether it is in test or live mode and whether live keys are in place. |
| Get Stripe Onboarding Link | `getStripeOnboardingLink` | Returns the link a Base44 app owner follows to claim the Stripe sandbox account into their own Stripe login, and says why no link is available when there is none. |
| Get Stripe Product | `getStripeProduct` | Returns one Stripe product sold by a Base44 app. |
| Get Stripe Sandbox | `getStripeSandbox` | Returns the Stripe test-mode sandbox account Base44 provisioned for an app, or nothing when the app has none. |
| Get Top Payment Customers | `getTopPaymentCustomers` | Returns the customers who have spent the most, or transacted the most often, in a Base44 app over the reporting period. |
| Get Wix Payments Dashboard Link | `getWixPaymentsDashboardLink` | Returns a signed link into the Wix Payments dashboard for a Base44 app, so the owner can manage payouts and payment settings. |
| Get Workflow | `getWorkflow` | Returns a single automation workflow on a Base44 app, including its current step definition, trigger and run statistics. |
| Get Workflow Run | `getWorkflowRun` | Returns a single automation workflow run on a Base44 app, including its per-step results, credits consumed and any AI analysis. |
| Get Workflow Run Now Options | `getWorkflowRunNowOptions` | Returns what a manual run of an automation workflow needs on a Base44 app, together with the recent runs available to replay from. |
| Get Workflow Stats | `getWorkflowStats` | Returns run statistics per automation workflow on a Base44 app, including totals, failures and average duration over the requested period. |
| Get Workflow Version | `getWorkflowVersion` | Returns the step definition stored in one saved version of an automation workflow on a Base44 app. |
| Import GitHub Branch | `importGithubBranch` | Brings a branch from the connected GitHub repository into a Base44 app as a separate working branch. |
| Install Stripe Integration | `installStripeIntegration` | Sets a Base44 app up to take payments with Stripe, provisioning a Stripe test-mode sandbox account and returning the link to claim it. Safe to call again; it reports when the integration is already installed. |
| Launch Google Ads Campaign | `launchGoogleAdsCampaign` | Sets up an app's Google Ads account if needed and puts a campaign live in one step. The campaign begins serving ads and spending its daily budget straight away, so this moves real money. |
| Link Custom Domain | `linkCustomDomain` | Points a verified custom domain at a Base44 app so the app is served from it. |
| Link Google Business Profile | `linkGoogleBusinessProfile` | Attaches a Google Business Profile location to an app's Google Ads account, so ads can show the business's address and reviews. |
| List Analytics Event Names | `listAnalyticsEventNames` | Returns the names of the analytics events a Base44 app has tracked, most frequent first, with how many times each was recorded. |
| List Analytics Event Properties | `listAnalyticsEventProperties` | Returns the property keys a Base44 app has sent with a given analytics event, so you know what you can filter, aggregate and group by. |
| List App Checkpoints | `listAppCheckpoints` | Returns a Base44 app's checkpoints, newest first. A checkpoint is a saved version of the app captured as you build, and its ID can be deployed or restored. |
| List App Workflow Runs | `listAppWorkflowRuns` | Returns the workflow runs recorded across every automation workflow on a Base44 app, newest first. |
| List Apps | `listApps` | Returns the Base44 apps you can access in a workspace. Workspace members receive the apps they own or collaborate on, while workspace admins receive every app in the workspace. Defaults to your personal workspace. |
| List Custom Domains | `listCustomDomains` | Returns the custom domains attached to a Base44 app, with the last status check recorded for each. Domains are added from the Base44 dashboard, not through the API. |
| List Email Domains | `listEmailDomains` | Returns the custom email domains a Base44 app can send from, with each one's configuration status and the DNS records it needs. |
| List Entity Records | `listEntityRecords` | Returns the records held in one of a Base44 app's entities, excluding deleted records. Row-level security applies, so only records the entity's read rule allows are returned. At most 5000 records come back per call. |
| List Entity Schemas | `listEntitySchemas` | Returns every entity schema defined on a Base44 app, with each entity's name and its stored JSON Schema. Use the entity names it reports when reading or writing entity records. |
| List GitHub Organizations | `listGithubOrganizations` | Returns the GitHub accounts and organizations the Base44 GitHub app is installed on, which are the ones an app can be connected to. |
| List Google Ads Asset Performance | `listGoogleAdsAssetPerformance` | Returns how each headline, description, image and video in an app's Google Ads campaigns is performing, with its ad strength and any policy issues. |
| List Google Ads Campaign Briefs | `listGoogleAdsCampaignBriefs` | Returns the saved campaign briefs for an app. A brief holds the business details, keywords, budget and copy a Google Ads campaign is built from, and creates no campaign by itself. |
| List Google Ads Campaign Changes | `listGoogleAdsCampaignChanges` | Returns the history of changes made to one Google Ads campaign on an app, newest first. |
| List Google Ads Campaign Optimization Suggestions | `listGoogleAdsCampaignOptimizationSuggestions` | Returns the changes Base44 suggests to improve one Google Ads campaign on an app, each with a severity and a suggested action. Suggestions only; nothing is changed. |
| List Google Ads Campaigns | `listGoogleAdsCampaigns` | Returns the Google Ads campaigns running for an app, optionally with their performance metrics. |
| List Google Ads Conversion Actions | `listGoogleAdsConversionActions` | Returns the conversion actions defined on an app's Google Ads account, which are the events campaigns are measured against. |
| List Google Ads Conversion Mappings | `listGoogleAdsConversionMappings` | Returns the rules that turn an app's entity events into Google Ads conversions, so campaign performance can be measured against real activity in the app. |
| List Google Ads Generated Assets | `listGoogleAdsGeneratedAssets` | Returns the ad assets Base44 has generated for an app, split into the current generation session, the reusable library and the assets already live on campaigns. |
| List Google Ads Insights | `listGoogleAdsInsights` | Returns the observations and recommendations Base44 has for an app's Google Ads account over a date range, each with a severity and a suggested action. |
| List Google Ads Invoices | `listGoogleAdsInvoices` | Returns the invoices raised for an app's Google Ads spend, each showing the ad spend, service fee and tax for its billing period. |
| List Google Ads Promotional Credits | `listGoogleAdsPromotionalCredits` | Returns the promotional advertising credits on an app's Google Ads account, with how much of each is left and when it expires. |
| List Google Ads Search Terms | `listGoogleAdsSearchTerms` | Returns the searches that triggered an app's Google Ads, with the impressions, clicks, cost and conversions each produced. |
| List Google Ads Top Asset Combinations | `listGoogleAdsTopAssetCombinations` | Returns the combinations of headlines, descriptions and images Google serves most often for an app's Performance Max asset groups. |
| List Sandbox Directory | `listSandboxDirectory` | Lists the files and folders in a Base44 app's development sandbox, so you can see the app's source tree before reading or editing it. |
| List Scheduled Social Posts | `listScheduledSocialPosts` | Returns the social media posts scheduled for a Base44 app, optionally limited to one content plan. |
| List Stripe Prices | `listStripePrices` | Returns the Stripe prices defined for a Base44 app's products, optionally limited to one product. |
| List Stripe Products | `listStripeProducts` | Returns the Stripe products a Base44 app sells, through the Stripe account connected to the app. |
| List URL Redirects | `listUrlRedirects` | Returns the URL redirects configured on a Base44 app, each mapping a source path to a target path. |
| List Workflow Runs | `listWorkflowRuns` | Returns the runs of one automation workflow on a Base44 app, newest first. |
| List Workflow Suggestions | `listWorkflowSuggestions` | Returns automation workflows Base44 suggests for an app, each with a title, a description and a ready-to-use build prompt. |
| List Workflow Versions | `listWorkflowVersions` | Returns the saved versions of an automation workflow on a Base44 app, newest first, with the change summary recorded for each. |
| List Workflows | `listWorkflows` | Returns the automation workflows defined on a Base44 app, with each workflow's status and run counters. |
| Pause All Google Ads Campaigns | `pauseAllGoogleAdsCampaigns` | Pauses every Google Ads campaign on an app at once, stopping all advertising spend for it. |
| Pause Google Ads Campaign | `pauseGoogleAdsCampaign` | Pauses one Google Ads campaign on an app so it stops showing ads and stops spending. |
| Pay Google Ads Workspace Debt | `payGoogleAdsWorkspaceDebt` | Charges the workspace's saved payment method to settle an outstanding Google Ads balance and unblock advertising. This moves real money. |
| Preview llms.txt | `previewLlmsTxt` | Returns the llms.txt content Base44 would serve for an app, which describes the app to AI crawlers. |
| Preview SEO JSON-LD | `previewSeoJsonLd` | Returns the JSON-LD structured data Base44 would generate for a Base44 app's entities, with the schema type and confidence it inferred for each. |
| Provision Live Stripe Keys | `provisionLiveStripeKeys` | Asks Base44 to move a Base44 app to live Stripe mode using the Stripe account already claimed by the app owner, so real payments are taken. |
| Pull Changes From GitHub | `pullChangesFromGithub` | Pulls new commits from the connected GitHub repository into a Base44 app and reports what was brought across. This endpoint answers HTTP 200 even when the pull does not happen, so check Synced and Error in the response rather than the status code. |
| Push Changes To GitHub | `pushChangesToGithub` | Commits a Base44 app's current source to the connected GitHub repository and reports the commit that resulted. This endpoint answers HTTP 200 even when the push does not happen, so check Success and Error in the response rather than the status code. |
| Query Analytics Events | `queryAnalyticsEvents` | Returns a Base44 app's individual analytics events for one event name, newest first, with the properties the app sent on each. The range defaults to the last 7 days. |
| Read Conversation Messages | `readConversationMessages` | Returns the messages in a Base44 app's builder conversation, which is the chat history between you and the Base44 AI builder for that app. |
| Read Sandbox Files | `readSandboxFiles` | Reads one or more source files from a Base44 app's development sandbox, optionally only a line range of each. |
| Refine Social Content Strategy | `refineSocialContentStrategy` | Feeds your notes back into a Base44 app's social content strategy and returns the revised strategy. This consumes workspace credits. |
| Refine Social Post | `refineSocialPost` | Asks Base44 to rewrite one post in a social content plan according to your instruction and returns the updated plan. This consumes workspace credits. |
| Regenerate Google Ads Asset Group Creative | `regenerateGoogleAdsAssetGroupCreative` | Generates a fresh set of text and image assets for one Performance Max asset group on an app's Google Ads campaign. The assets are held in a generation session until accepted, and generating them consumes workspace credits. |
| Remove Stripe Integration | `removeStripeIntegration` | Disconnects Stripe from a Base44 app so it stops taking payments through it. |
| Replace Email Domain | `replaceEmailDomain` | Swaps the domain a Base44 app sends email from for a different one and returns the DNS records the new domain needs. |
| Reset Social Content Flow | `resetSocialContentFlow` | Clears a Base44 app's guided social content flow, discarding its questions, answers, strategy and generated plan so it can be started again. |
| Resolve GitHub Sync Conflicts | `resolveGithubSyncConflicts` | Asks Base44 to reconcile a GitHub sync that stopped on conflicting changes, and reports whether the conflict was settled. |
| Resolve Wix Payments Onboarding Name | `resolveWixPaymentsOnboardingName` | Reports whether Wix Payments onboarding still needs the account holder's full name, and returns the first and last name Base44 already holds. |
| Restore App Checkpoint | `restoreAppCheckpoint` | Rolls a Base44 app back to a saved checkpoint and returns the app as it stands afterwards. This replaces the app's current working version. |
| Restore Workflow | `restoreWorkflow` | Restores an archived automation workflow on a Base44 app so it appears in List Workflows again. |
| Resume Google Ads Campaign | `resumeGoogleAdsCampaign` | Restarts a paused Google Ads campaign on an app. The campaign begins showing ads and spending its daily budget again. |
| Retry Email Domain Setup | `retryEmailDomainSetup` | Re-checks the DNS records of a Base44 app's email domain and reports the configuration status that resulted. |
| Retry Google Ads Billing Setup | `retryGoogleAdsBillingSetup` | Runs the Google Ads billing setup for an app's advertising account again after it failed, and returns the account as it stands afterwards. |
| Run Sandbox Command | `runSandboxCommand` | Runs a shell command inside a Base44 app's development sandbox and returns its output and exit code. |
| Run Security Scan | `runSecurityScan` | Starts a security scan of a Base44 app and returns the scan status. Read the findings afterwards with Get Security Scan. |
| Run SEO Scan | `runSeoScan` | Scans a Base44 app for SEO problems and returns an overall score plus a pass, warn or fail verdict for each check. |
| Run Workflow Now | `runWorkflowNow` | Starts an automation workflow on a Base44 app immediately, outside its normal trigger. Running a workflow consumes workspace credits. |
| Save App File | `saveAppFile` | Writes one source file into a Base44 app, replacing it if it already exists, and returns the app as it stands afterwards. |
| Save App Files | `saveAppFiles` | Writes several source files into a Base44 app in one call and returns the app as it stands afterwards. |
| Scan Google Ads Conversion Tracking | `scanGoogleAdsConversionTracking` | Checks whether an app's code actually reports the conversions its Google Ads mappings expect, and lists the gaps with the files to fix and a prompt that fixes them. |
| Search Google Ads Locations | `searchGoogleAdsLocations` | Looks up Google Ads location targets by name so they can be used as a campaign's geo targets, and reports the audience reach of each. |
| Search Sandbox Files | `searchSandboxFiles` | Searches the source files in a Base44 app's development sandbox for a pattern and returns the matching lines with their file and line number. |
| Send Chat Message | `sendChatMessage` | Sends a prompt to the Base44 AI builder for an app. The builder works in the background to change the app, and the call consumes workspace credits. |
| Set App Secrets | `setAppSecrets` | Stores one or more secrets on a Base44 app so its backend functions can read them. Pass each secret as an additional input whose name is the secret name and whose value is the secret. Existing secrets with the same name are overwritten. |
| Start Social Content Flow | `startSocialContentFlow` | Begins the guided social content flow for a Base44 app. Base44 analyses the app and returns the questions to answer before a strategy is drafted. This consumes workspace credits. |
| Start Social Post Scheduling | `startSocialPostScheduling` | Starts a background job that spreads a Base44 app's proposed social media posts across a date range at the best times, and returns the job to poll. |
| Stop Chat Generation | `stopChatGeneration` | Interrupts the Base44 AI builder while it is working on an app, leaving whatever it has already changed in place. |
| Submit Social Content Answers | `submitSocialContentAnswers` | Sends answers to the questions Base44 asked during the guided social content flow and returns the content strategy drafted from them. This consumes workspace credits. |
| Submit Tool Call Input | `submitToolCallInput` | Approves or rejects one action the Base44 AI builder has paused to ask about while working on an app. |
| Submit Tool Call Input Batch | `submitToolCallInputBatch` | Approves or rejects several paused Base44 builder actions at once and reports the outcome for each. |
| Suggest Google Ads Campaigns | `suggestGoogleAdsCampaigns` | Asks Base44's AI to propose Google Ads campaigns for an app's business. The proposals are returned for review and create no campaign and no spend. |
| Suggest Google Ads Keyword Themes For Campaign | `suggestGoogleAdsKeywordThemesForCampaign` | Returns keyword themes Base44 suggests adding to one Google Ads campaign on an app. Suggestions only; nothing is added to the campaign. |
| Suggest Google Ads Search Themes | `suggestGoogleAdsSearchThemes` | Asks Base44's AI for search themes a business should target in Google Ads. Suggestions only; nothing is created. |
| Suggest Google Ads Text Assets | `suggestGoogleAdsTextAssets` | Asks Base44's AI for headlines, long headlines, descriptions and calls to action for an app's Google Ads. Suggestions only; nothing is attached to a campaign. |
| Sync Entity Schemas | `syncEntitySchemas` | Replaces a Base44 app's entire set of entity schemas in one call. Entities missing from the map you send are deleted, so send the complete desired set. |
| Toggle Workflow Status | `toggleWorkflowStatus` | Switches an automation workflow on a Base44 app between active and paused. The response reports the status it ended up in. |
| Turn Off Google Ads Budget Auto Renewal | `turnOffGoogleAdsBudgetAutoRenewal` | Stops an app's Google Ads budget renewing automatically, so spending ends when the current billing window closes. |
| Turn On Google Ads Budget Auto Renewal | `turnOnGoogleAdsBudgetAutoRenewal` | Makes an app's Google Ads budget renew automatically at the end of each billing window, so campaigns keep spending without manual top-ups. |
| Undo Chat Message | `undoChatMessage` | Rolls a Base44 app back to the state it was in before a given builder message, discarding the changes that message produced. |
| Unlink Custom Domain | `unlinkCustomDomain` | Stops serving a Base44 app from a custom domain while keeping the domain on the account. |
| Unlink Google Business Profile | `unlinkGoogleBusinessProfile` | Detaches the Google Business Profile location from an app's Google Ads account, so ads stop showing the business's location details. |
| Update Email Sender Details | `updateEmailSenderDetails` | Changes the sender name and from address a Base44 app sends email under, without changing the domain. |
| Update Entity Record | `updateEntityRecord` | Updates a record in one of a Base44 app's entities. Pass the fields to change as additional top-level inputs using the names the entity's schema defines; fields you leave out keep their current values. |
| Update Entity Schema | `updateEntitySchema` | Replaces the JSON Schema of one entity on a Base44 app. The schema you send becomes the entity's full definition, so include every field you want to keep. |
| Update Google Ads Billing Cadence | `updateGoogleAdsBillingCadence` | Changes how often an app's Google Ads spend is billed, between weekly, fortnightly and monthly. |
| Update Google Ads Campaign | `updateGoogleAdsCampaign` | Changes one aspect of a Google Ads campaign on an app. Name the aspect in Field and pass its new setting in Value. Changing the budget changes what the campaign spends each day. |
| Update Google Ads Campaign Brief | `updateGoogleAdsCampaignBrief` | Changes a saved campaign brief on an app. Only the fields you send are changed, and no campaign is created or altered. |
| Update Google Ads Conversion Mapping | `updateGoogleAdsConversionMapping` | Changes a rule that turns an app's entity events into Google Ads conversions. Set Is Enabled to false to stop it reporting without deleting it. |
| Update Google Ads Monthly Spend Cap | `updateGoogleAdsMonthlySpendCap` | Sets the most an app's Google Ads account may spend in a month. Raising this raises the amount that can be charged. |
| Update Scheduled Social Post | `updateScheduledSocialPost` | Changes the copy, image or publishing time of a scheduled social media post on a Base44 app. Only the fields you send are changed. |
| Update SEO Settings | `updateSeoSettings` | Updates a Base44 app's SEO settings. Send only the settings you want to change inside the Settings object. |
| Update Social Post Content | `updateSocialPostContent` | Replaces the copy of one post in a Base44 app's generated social content plan and returns the updated plan. |
| Update Stripe Price | `updateStripePrice` | Changes a Stripe price on a Base44 app. Stripe prices are immutable, so only the nickname, metadata and active flag can be changed; set Active to false to retire a price. |
| Update Stripe Product | `updateStripeProduct` | Changes a Stripe product sold by a Base44 app. Set Active to false to archive it so it can no longer be bought. |
| Update URL Redirect | `updateUrlRedirect` | Replaces the source path, target path and match type of a URL redirect on a Base44 app. |
| Update Workflow | `updateWorkflow` | Updates an automation workflow on a Base44 app. Only the fields you send are changed, and a change to the definition or trigger records a new workflow version. |
| Upload Enhanced Google Ads Conversions | `uploadEnhancedGoogleAdsConversions` | Sends hashed customer details for conversions already reported to Google Ads, so Google can match more of them back to ad clicks. |
| Upload Google Ads Conversions | `uploadGoogleAdsConversions` | Sends offline conversions to Google Ads for an app, so campaigns can be optimised against sales that happened away from the website. |
| Validate Workflow Definition | `validateWorkflowDefinition` | Checks a workflow step definition against a Base44 app without saving it, and reports any errors plus the task types and activities the app supports. |
| Verify Custom Domain | `verifyCustomDomain` | Asks Base44 to check the DNS records for a custom domain and mark it verified once they resolve correctly. |
| Write Sandbox File | `writeSandboxFile` | Creates a source file in a Base44 app's development sandbox. Set Overwrite to replace a file that already exists. |

</details>
