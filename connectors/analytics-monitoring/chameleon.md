---
description: "Chameleon is a product-adoption platform for in-product Tours, Microsurveys, Tooltips, Launchers, Embeddables, Product Demos and the HelpBar."
hidden: true
---

# Chameleon

<img src="../../.gitbook/assets/connectors/chameleon.png" alt="Chameleon logo" width="64">

Chameleon is a product-adoption platform for in-product Tours, Microsurveys, Tooltips, Launchers, Embeddables, Product Demos and the HelpBar. This connector covers the full Chameleon v3 REST API: user profiles and companies with search and counting, segments, every Experience type, deliveries, tour interactions and microsurvey responses, themes, tags, domains and URL groups, data properties, event names, rate limit and alert groups, data imports, HelpBar search configuration and items, change history, webhook subscriptions, and the incoming data-push hooks for profiles, companies and events.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [chameleon.io](https://chameleon.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `chameleon` |

## Use it

Add Chameleon from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chameleon.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Delete Search Items | `bulkDeleteSearchItems` | Removes a large batch of indexed HelpBar items in a single request. |
| Bulk Update Domains | `bulkUpdateDomains` | Applies the same change to many domains at once, such as moving them into one environment group or archiving them together. |
| Bulk Update Search Items | `bulkUpdateSearchItems` | Applies the same change (for example a new icon or search group) to many HelpBar Search Items at once by their Chameleon IDs. |
| Bulk Update Tags | `bulkUpdateTags` | Applies or removes Tags across many Experiences in one request, which is how a new tagging scheme is rolled out. Each update names a model and either a tag id, a tag name (both prefixed with + to add or - to remove) or an exact list of tag names. |
| Clear User Profile | `clearUserProfile` | Resets an end-user profile: clears its browser and session data and the Experiences it has seen, while keeping the profile record itself. |
| Clear User Profile By Identifier | `clearUserProfileByIdentifier` | Clears (resets) a User Profile identified by your own uid: properties such as sessions and last seen are reset, Microsurvey responses and tracked Events are removed, and summary counts are reverted. |
| Count Companies | `countCompanies` | Returns how many companies match a set of segmentation filters, without returning the companies themselves. |
| Count User Profiles | `countUserProfiles` | Returns how many end-user profiles match a set of segmentation filters, without returning the profiles themselves. |
| Create Data Import | `createDataImport` | Creates a Data Import definition that tags, updates or deletes User Profiles or Companies from a CSV or from segment filters. For CSV kinds, map the CSV headers to Chameleon properties here, then upload the CSV file (multipart, outside this connector) and set import_at to start it. Imports cannot be deleted once created. |
| Create Data Property | `createDataProperty` | Declares a custom data property on user profiles or companies so it can be used for segmentation and personalization. |

<details>

<summary>See 88 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Delivery | `createDelivery` | Queues a specific Tour or Microsurvey to be shown to one specific end-user the next time they are in your product. Identify the user by Profile ID, User Identifier or Email. |
| Create Domain | `createDomain` | Enables Chameleon on a new domain so Experiences may run there. |
| Create Environment | `createEnvironment` | Creates an environment group that domains and Experiences can be organised under. |
| Create Search Import | `createSearchImport` | Creates a HelpBar content import from a CSV based on Chameleon's template. Note: Chameleon requires this request as multipart/form-data with the file part, which the fastn engine cannot send as JSON; the live response is 422 'Missing file data'. Use the Chameleon dashboard or a direct multipart upload for this step and track progress with Get Search Import. |
| Create Webhook Subscription | `createWebhookSubscription` | Subscribes an HTTPS endpoint to the chosen Chameleon webhook topics. An account is limited to five subscriptions and each URL must be unique. |
| Delete Company | `deleteCompany` | Deletes a company and removes it from every profile associated with it. Pass Cascade as 'profiles' to also delete those profiles. |
| Delete Company By Identifier | `deleteCompanyByIdentifier` | Deletes a company identified by your own company identifier rather than the Chameleon ID. |
| Delete Delivery | `deleteDelivery` | Removes a queued Delivery so the Experience is no longer scheduled for that user. |
| Delete Microsurvey Response | `deleteMicrosurveyResponse` | Permanently deletes a single Microsurvey response. |
| Delete Search Item | `deleteSearchItems` | Removes one indexed HelpBar item, identified by the unique key you supplied when it was created, so it no longer appears in end-user search results. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Removes an outgoing webhook subscription so Chameleon stops posting events to that endpoint. |
| Download Data Import CSV | `downloadDataImportCsv` | Downloads the original CSV file that was uploaded for a data import. |
| Download Experience Translations | `downloadExperienceTranslations` | Downloads the translation file (JSON) for a single Experience, listing every translatable text of each step, ready to be translated and re-uploaded. Localization is a Growth/Enterprise add-on. |
| Download Mixed Translations | `downloadMixedTranslations` | Downloads one translation file (JSON) for a chosen mix of Experiences of different kinds (Tours, Microsurveys, Launchers, Tooltips). Localization is a Growth/Enterprise add-on. |
| Download Translations By Kind | `downloadTranslationsByKind` | Downloads one translation file (JSON) covering every Experience of a kind (all Tours, all Microsurveys, all Launchers or all Tooltips). Localization is a Growth/Enterprise add-on. |
| Find User Profile By Identifier | `findUserProfileByIdentifier` | Looks up a single end-user profile by your own user identifier or by email address instead of the Chameleon ID. Supply exactly one of ID, UID or Email. |
| Forget User Profile | `forgetUserProfile` | Permanently deletes an end-user profile and all of its data from Chameleon. This cannot be undone and is the action to use for GDPR erasure requests. |
| Forget User Profile By Identifier | `forgetUserProfileByIdentifier` | Permanently deletes a User Profile and all of its data, identified by your own uid (a right-to-be-forgotten request). This cannot be undone. |
| Get Account Identity | `getAccountIdentity` | Returns the Chameleon account and user that the connected Account Secret belongs to. This root endpoint is not in the public API reference but responds reliably and is useful for verifying a connection. |
| Get Alert Group | `getAlertGroup` | Retrieves a single Alert Group by id, including its alerting conditions and notified members. |
| Get Company | `getCompany` | Retrieves a single company by its Chameleon ID, including every custom property sent for that account. |
| Get Company By Identifier | `getCompanyByIdentifier` | Retrieves a single Company using your own company identifier (uid) instead of the Chameleon ID. |
| Get Data Import | `getDataImport` | Retrieves a single CSV import by id, including its state, property mapping and row counts. |
| Get Data Property | `getDataProperty` | Retrieves a single custom data property (for User Profiles, Companies or Events) by its Chameleon ID. |
| Get Delivery | `getDelivery` | Retrieves a single Delivery (a direct trigger of a Tour or Microsurvey to a specific user) by its Chameleon ID. |
| Get Domain | `getDomain` | Retrieves a single enabled domain by id, including its environment group and installation state. |
| Get Embeddable | `getEmbeddable` | Retrieves a single Embeddable by id, including its steps and the selector it renders into. |
| Get Environment | `getEnvironment` | Retrieves a single environment group by id, including its display styling and the domains it holds. |
| Get Event Name | `getEventName` | Retrieves a single tracked event name by id. |
| Get Launcher | `getLauncher` | Retrieves a single Launcher by id, including its items and targeting configuration. |
| Get Microsurvey | `getMicrosurvey` | Retrieves a single Microsurvey by id, including its question steps and targeting configuration. |
| Get Model Change Summary | `getModelChangeSummary` | Returns a condensed summary of the edits made to one specific Experience rather than the full change list. |
| Get Rate Limit Group | `getRateLimitGroup` | Retrieves a single Rate Limit Group by id, including how many Experiences it allows per period. |
| Get Search Import | `getSearchImport` | Retrieves a single HelpBar content import by id, including its progress and how many items it indexed. |
| Get Segment | `getSegment` | Retrieves a single Segment by id, including the filter expressions that define its membership. |
| Get Tag | `getTag` | Retrieves a single Tag by id, including its readable name and how many Experiences use it. |
| Get Theme | `getTheme` | Retrieves a single Theme by id, including its custom CSS and styling options. |
| Get Tooltip | `getTooltip` | Retrieves a single Tooltip by id, including the element it anchors to and its targeting configuration. |
| Get Tour | `getTour` | Retrieves a single Tour by id, including its steps, elements, buttons and targeting configuration. |
| Get User Profile | `getUserProfile` | Retrieves a single end-user profile by its Chameleon ID, including every custom property sent for that user. |
| Get Webhook Subscription | `getWebhookSubscription` | Retrieves a single outgoing webhook subscription by its Chameleon ID, including its URL, topics and last delivery state. |
| List Alert Groups | `listAlertGroups` | Lists the Alert Groups, which notify team members when an Experience violates its alerting conditions. |
| List Changes | `listChanges` | Lists the audit trail of edits made to your Experiences, showing who changed what and when. |
| List Companies | `listCompanies` | Lists the companies identified to Chameleon in creation order, using cursor paging. |
| List Data Imports | `listDataImports` | Lists the CSV data imports run against the account, with the state and row counts of each. |
| List Data Properties | `listDataProperties` | Lists the custom data properties Chameleon has recorded for user profiles or for companies. |
| List Deliveries | `listDeliveries` | Lists the Deliveries queued or completed, each of which triggers one Experience for one specific user. |
| List Domains | `listDomains` | Lists the domains on which Chameleon is enabled, including whether the snippet has been detected on each. |
| List Embeddables | `listEmbeddables` | Lists the Embeddables in the account, the persistent widgets rendered inline inside your product UI. |
| List Environments | `listEnvironments` | Lists the environment groups that domains are organised into, such as Production and Staging. |
| List Event Names | `listEventNames` | Lists the event names Chameleon has recorded for the account, which are the events available for targeting and conversion goals. |
| List HelpBars | `listHelpBars` | Lists the HelpBar configurations on the account. There is one HelpBar per account. |
| List Launchers | `listLaunchers` | Lists the Launchers in the account, each a menu of items shown to matching end-users. |
| List Microsurvey Responses | `listMicrosurveyResponses` | Lists the responses collected by one Microsurvey, including the buttons clicked and any free-text follow-up answers. |
| List Microsurveys | `listMicrosurveys` | Lists the Microsurveys in the account, each with its question steps, targeting and publication state. |
| List Model Changes | `listModelChanges` | Lists the full edit history of one specific Experience. |
| List Rate Limit Group Experiences | `listRateLimitGroupExperiences` | Lists the Experiences assigned to a Rate Limit Group. |
| List Rate Limit Groups | `listRateLimitGroups` | Lists the Rate Limit Groups, which cap how many Experiences a single user may be shown in a period. |
| List Search Items | `listSearchItems` | Lists the individual items indexed in the HelpBar, such as help-centre articles and custom actions. |
| List Segment Experiences | `listSegmentExperiences` | Lists the Experiences of one kind that target a given Segment, for example every Tour using that Segment. |
| List Segments | `listSegments` | Lists the Segments defined in the account, each holding the filter expressions used to target Experiences. |
| List Tags | `listTags` | Lists the Tags used to group Experiences, each with how many Experiences carry it. |
| List Themes | `listThemes` | Lists the Themes configured in the account, which define the visual styling applied to Experiences. |
| List Tooltips | `listTooltips` | Lists the Tooltips in the account, each a single step shown on click or hover of an element. |
| List Tour Interactions | `listTourInteractions` | Lists how individual users have progressed through one Tour, including where each user currently is in the sequence. |
| List Tours | `listTours` | Lists the Tours in the account, each with its steps, targeting and publication state. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | Lists the outgoing webhook subscriptions configured on the account, with the delivery state of each. |
| Push Companies Batch | `pushCompaniesBatch` | Creates or updates many Companies in one request through the incoming companies hook. Each company carries its own identifier (uid or id) plus any custom properties. |
| Push Company | `pushCompany` | Creates or updates a Company in Chameleon through the incoming companies hook. Identify the company by uid (your database ID) or the Chameleon id. Any additional top-level field you pass is stored on the company as a custom property (names are normalised to snake_case). |
| Push User Profile | `pushUserProfile` | Creates or updates a User Profile in Chameleon through the incoming profiles hook. Identify the user by uid (your database ID), email or the Chameleon id; send company_uid or company_id to associate an account. Any additional top-level field you pass is stored on the profile as a custom property (names are normalised to snake_case). |
| Push User Profiles Batch | `pushUserProfilesBatch` | Creates or updates many User Profiles in one request through the incoming profiles hook. Each profile carries its own identifier (uid, email or id) plus any custom properties. |
| Save HelpBar | `saveHelpBar` | Creates or updates the account's HelpBar, the federated search bar shown to end-users. There is only one per account, so this endpoint both creates and updates it. |
| Search Companies | `searchCompanies` | Searches the companies identified to Chameleon using segmentation filter expressions, with sorting and paging. |
| Search User Profiles | `searchUserProfiles` | Searches your end-user profiles using segmentation filter expressions or an existing Segment. At least one of Segment ID or Filters must be supplied. |
| Track Event | `trackEvent` | Tracks an Event for a User Profile through the incoming events hook. Identify the user by uid, email or the Chameleon id and give the event name; any additional top-level field is stored as an event property (reserved names such as source, at, action are silently dropped by Chameleon). Events are processed asynchronously. |
| Track Events Batch | `trackEventsBatch` | Tracks many Events in one request through the incoming events hook. Each event carries its own user identifier (uid, email or id), its name and any custom properties; invalid items are reported per index without rejecting the valid ones. |
| Update Data Import | `updateDataImport` | Updates a CSV import before it runs, for example to change its name, property mapping or scheduled time. |
| Update Data Property | `updateDataProperty` | Renames a custom data property or updates the description shown to teammates building Segments. |
| Update Delivery | `updateDelivery` | Updates a queued Delivery, for example to change its validity window or its personalization options. |
| Update Domain | `updateDomain` | Updates an enabled domain, for example to move it to a different environment group or to archive it. |
| Update Embeddable | `updateEmbeddable` | Updates an Embeddable's domain group, tag or publication state. Set Published At to publish it or to null to unpublish it. |
| Update Environment | `updateEnvironment` | Updates an environment group's name, description, badge styling or archive state. |
| Update Launcher | `updateLauncher` | Updates a Launcher's domain group, tag or publication state. Set Published At to publish it or to null to unpublish it. |
| Update Microsurvey | `updateMicrosurvey` | Updates a Microsurvey's domain group, tag or publication state. Set Published At to publish it or to null to unpublish it. |
| Update Search Item | `updateSearchItem` | Updates an existing HelpBar Search Item by its Chameleon ID; any of the Search Item fields (title, description, search group, targeting, icon, actions) can be changed. |
| Update Tooltip | `updateTooltip` | Updates a Tooltip's domain group, tag or publication state. Set Published At to publish it or to null to unpublish it. |
| Update Tour | `updateTour` | Updates a Tour's domain group, tag or publication state. Set Published At to publish the Tour or to null to unpublish it. |
| Upsert Search Item | `upsertSearchItem` | Creates or updates a HelpBar Search Item identified by your own uid, with its title, description, search group, targeting (profiles, companies, segments), icon and the actions run when it is selected. Note: when an existing uid is updated, the id in the response may not be the stored item's id; read stable ids from List Search Items. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Alert Triggered | `alert.triggered` | Sent when an Alert Group's conditions are violated by an Experience. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Embeddable Button Clicked | `embed.button.clicked` | Sent when a button in an Embeddable Step is clicked; includes the Button. Payload sample follows Chameleon's tour button example (the doc links it for this topic); the model key is embed. kind carries the topic. |
| Embeddable Completed | `embed.completed` | Sent when an Embeddable is completed with the Step the user completed. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Embeddable Exited | `embed.exited` | Sent when an Embeddable is exited with the Step the user exited. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Embeddable Snoozed | `embed.snoozed` | Sent when an Embeddable is exited on a Step configured to snooze and re-display later. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Embeddable Started | `embed.started` | Sent when an Embeddable is started; includes the first Step. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| HelpBar AI Answer | `helpbar.answer` | Sent when a HelpBar search query generates an AI answer. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| HelpBar Item Actioned | `helpbar.item.action` | Sent when an item in the HelpBar is clicked or actioned. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| HelpBar Item Error | `helpbar.item.error` | Sent when an action from a HelpBar item throws an error when running. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| HelpBar Search | `helpbar.search` | Sent when a HelpBar search query displays its results. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |

<details>

<summary>See 17 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Microsurvey Button Clicked | `survey.button.clicked` | Sent when a button in a Microsurvey Step is clicked; includes the Button. Payload sample follows Chameleon's tour button example (the doc links it for this topic); the model key is survey. kind carries the topic. |
| Microsurvey Completed | `survey.completed` | Sent when a Microsurvey is completed with the Step the user completed. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Microsurvey Exited | `survey.exited` | Sent when a Microsurvey is exited with the Step the user exited. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Microsurvey Response Finished | `response.finished` | Sent when a Microsurvey is finished (all steps completed, including the text comment if configured). Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Microsurvey Snoozed | `survey.snoozed` | Sent when a Microsurvey is exited on a Step configured to snooze and re-display later. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Microsurvey Started | `survey.started` | Sent when a Microsurvey is started with its first Step. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Ping | `ping` | Sent by Chameleon as a simple check that the endpoint is working. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Product Demo Company Revealed | `demo.reveal` | Sent after a Demo starts when Clearbit reveal is enabled and a company match is found; demo_run carries reveal_domain and reveal_name. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Product Demo Email Added | `demo.email.added` | Sent once per previously anonymous Demo run when the visitor's email becomes known (form submission or product sign-up). Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Product Demo Finished | `demo.finished` | Sent when a Demo reaches its last step or times out after about 30 minutes; demo_run.finished_kind is last_step or timeout_30m. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Product Demo Form Submitted | `demo.form.submitted` | Sent when a form inside a Demo is submitted; action.submission carries the submitted values. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Product Demo Started | `demo.started` | Sent when a Product Demo is started. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Tour Button Clicked | `tour.button.clicked` | Sent when a button in a Tour Step is clicked; includes the Button. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Tour Completed | `tour.completed` | Sent when a Tour is completed; includes the Step the user completed. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Tour Exited | `tour.exited` | Sent when a Tour is exited; includes the Step the user exited. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Tour Snoozed | `tour.snoozed` | Sent when a Tour is exited on a Step configured to snooze and re-display later. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |
| Tour Started | `tour.started` | Sent when a Tour is started; includes the first Step. Payload sample is Chameleon's own example from developers.chameleon.io/webhooks/outgoing; kind carries the topic. |

</details>
