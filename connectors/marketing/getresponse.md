---
description: "GetResponse email marketing and automation platform."
hidden: true
---

# GetResponse

<img src="../../.gitbook/assets/connectors/lg/getresponse.png" alt="GetResponse logo">

GetResponse email marketing and automation platform. Manage contacts, campaigns (lists), custom fields, tags, from-fields, autoresponders, newsletters, RSS newsletters, forms, webforms, segments (search-contacts), statistics, ecommerce (shops, products, categories, carts, orders), account settings, and webhook callbacks via the GetResponse REST API v3.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [getresponse.com](https://getresponse.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `getresponse` |

## Use it

Add GetResponse from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.getresponse.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Account Blocklist Masks | `addAccountBlocklist` | Update account blocklist. |
| Add Campaign Blocklist Masks | `addCampaignBlocklist` | Updates campaign blocklist masks. |
| Billing information | `getAccountBilling` | Billing information. |
| Cancel A/B test | `cancelAbTest` | Cancel A/B test. This method allows you to schedule the cancellation of an A/B test. Cancelling an A/B test is an asynchronous operation. |
| Cancel sending the newsletter | `cancelMessageSend` | Cancel sending the newsletter. &gt; Using this method, you can cancel the sending of the newsletter. It will also turn the newsletter into a **draft**. |
| Choose A/B test winner | `setAbTestSubjectWinner` | Choose A/B test winner. |
| Create a file | `createFile` | Create a file. |
| Create a folder | `createFolder` | Create a folder. |
| Create a new A/B test | `createSubjectAbTest` | Create a new A/B test. |
| Create a predefined field | `createPredefinedField` | Create a predefined field. Makes it possible to create a new predefined field. |

<details>

<summary>See 209 more actions</summary>

* **Create Account Callbacks** `createAccountCallbacks`: Enable or update callbacks configuration.
* **Create address** `createAddress`: Create address.
* **Create Autoresponder** `createAutoresponder`: Create a time-based autoresponder message that sends on a given day of the subscriber cycle. Requires name, subject, from-field, content, campaign, and trigger settings.
* **Create Campaign** `createCampaign`: Create a new campaign (contact list). Requires a unique lowercase name and confirmation settings (from-field and subscription confirmation subject/body IDs).
* **Create Cart** `createCart`: Create cart. Sending a **POST** request to this URL will create a new cart resource. In order to create a new cart, you need to send the cart resource in the body of the request (remember that you need to serialize the body into a JSON string)
* **Create Category** `createCategory`: Create category. Create shop category. You can pass the `parentId` parameter to create a sub-category of a given parent. Unlike most **POST** methods, this call is idempotent, that is: sending the same request 10 times will not create 10 new categories. Only one category will be created.
* **Create Contact** `createContact`: Add a new contact to a campaign (contact list). Returns HTTP 202 Accepted (contact is queued). Requires email and campaign ID.
* **Create custom event** `createCustomEvent`: Create custom event.
* **Create Custom Field** `createCustomField`: Create a custom field.
* **Create From Field** `createFromField`: Create 'From' address.
* **Create meta field** `createMetaField`: Create meta field. Sending a **POST** request to this URL will create a new meta field resource. In order to create a new meta field, you need to send a meta field resource in the body of the request (remember that you need to serialize the body into a JSON string)
* **Create multiple contacts at once** `createBatchContacts`: Create multiple contacts at once. This endpoint lets you create multiple contacts in one request. **Note** This endpoint is subject to special limits and throttling. You can make 80 calls per time frame (10 minutes) and only 1 call per second. The allowed batch size is 1000 contacts. For more information, check our [API Docs](https://apidocs.getresponse.com/v3/case-study/adding-batch-contacts).
* **Create Newsletter** `createNewsletter`: Create and send a broadcast newsletter to selected campaigns. Requires subject, from-field, HTML content, and target campaigns.
* **Create Order** `createOrder`: Create order. Sending a **POST** request to this URL will create a new order resource. In order to create a new order, you need to send the order resource in the body of the request (remember that you need to serialize the body into a JSON string).
* **Create Product** `createProduct`: Create product. Sending a **POST** request to this URL will create a new product resource. In order to create a new product, you need to send the product resource in the body of the request (remember that you need to serialize the body into a JSON string) You don't need a separate endpoint for each element (e.g. variant, category, meta-field). You can create them all with this method. Please note that categories aren't required, but if a product has at least one category, then one of those categories must be marked as default. This can be set by field `isDefault`. If none of the elements contains isDefault=true, then the system picks the first one from the collection by default.
* **Create product variant** `createProductVariant`: Create product variant. Sending a **POST** request to this URL will create a new product variant resource. In order to create a new product variant, you need to send a product variant resource in the body of the request (remember that you need to serialize the body into a JSON string) There is no need to create every element (like: image, meta field, tax) one by one by their own endpoints. All these elements can be created during this method.
* **Create RSS Newsletter** `createRssNewsletter`: Create RSS newsletter.
* **Create Segment** `createSearchContacts`: Create search contacts. Makes it possible to create a new search-contact. Please refer to [Segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual)
* **Create Shop** `createShop`: Create shop. This method makes it possible to create a new shop.
* **Create Tag** `createTag`: Add a new tag.
* **Create tax** `createTax`: Create tax. Sending a **POST** request to this URL will create a new tax resource. In order to create a new tax, you need to send a tax resource in the body of the request (remember that you need to serialize the body into a JSON string)
* **Create the custom report** `createCustomReport`: Create the custom report. The endpoint allows scheduling a custom report of a specific type for a given time period. Depending on the report type, you can also narrow down the data using appropriate filters. &lt;strong&gt;Important:&lt;/strong&gt; The reports you can generate depend on your pricing plan. More information about using the endpoint, along with examples, can be found in the Case Study section of the [API documentation](http://apidocs.getresponse.com/v3/case-study/custom-reports-scheduling).
* **Create transactional email template** `createTransactionalEmailTemplate`: Create transactional email template. This method creates a new transactional email template
* **Creates a new suppression list** `createSuppression`: Creates a new suppression list.
* **Current status of your GetResponse badge** `getAccountBadge`: Current status of your GetResponse badge.
* **Delete a custom event by custom event ID** `deleteCustomEvent`: Delete a custom event by custom event ID.
* **Delete a predefined field** `deletePredefinedField`: Delete a predefined field.
* **Delete A/B test** `deleteAbTest`: Delete A/B test. This method allows you to delete an A/B test. Deletion is only permitted when the test is in one of the following states: `draft`, `cancelled`, `finished`, or `completed`.
* **Delete Account Callbacks** `deleteAccountCallbacks`: Disable callbacks.
* **Delete address** `deleteAddress`: Delete address.
* **Delete Autoresponder** `deleteAutoresponder`: Delete autoresponder..
* **Delete Cart** `deleteCart`: Delete cart.
* **Delete Category** `deleteCategory`: Delete category.
* **Delete Contact** `deleteContact`: Delete a contact by contact ID.
* **Delete Custom Field** `deleteCustomField`: Delete a single custom field definition.
* **Delete file by file ID** `deleteFile`: Delete file by file ID.
* **Delete folder by folder ID** `deleteFolder`: Delete folder by folder ID.
* **Delete From Field** `deleteFromField`: Delete 'From' address.
* **Delete meta field** `deleteMetaField`: Delete meta field.
* **Delete Newsletter** `deleteNewsletter`: Delete newsletter.
* **Delete Order** `deleteOrder`: Delete order.
* **Delete Product** `deleteProduct`: Delete product.
* **Delete product variant** `deleteProductVariant`: Delete product variant.
* **Delete RSS Newsletter** `deleteRssNewsletter`: Delete RSS newsletter.
* **Delete Segment** `deleteSearchContacts`: Delete search contacts.
* **Delete Shop** `deleteShop`: Delete shop. This method deletes a shop.
* **Delete Tag** `deleteTag`: Delete tag by ID.
* **Delete tax by ID** `deleteTax`: Delete tax by ID.
* **Delete transactional email template** `deleteTransactionalEmailsTemplate`: Delete transactional email template.
* **Deletes a given suppression list by ID** `deleteSuppression`: Deletes a given suppression list by ID.
* **Get a list of addresses** `getAddressList`: Get a list of addresses. Sending a **GET** request to this URL returns collection of address resources. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * firstName * lastName * address1 * address2 * city * zip * province * provinceCode * phone * company * createdOn The `name` field can be a pattern and we'll try to match this phrase. You can specify which page of the results you want and how many results per page to display. You can also specify the sort-order using one or more of the allowed fields (listed below in the request params section). Last but not least, you can even specify which fields from a resource you want to get. If you pass the param `fields` with the list of fields (separated by a comma [,]) we'll return the list of resources with only those fields (we'll always add a resource ID to ensure that you can use that data later on) You c...
* **Get a list of custom events** `getCustomEventsList`: Get a list of custom events. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get a list of custom reports** `getCustomReportList`: Get a list of custom reports. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get a list of imports.** `getImportList`: Get a list of imports.. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get a list of landing pages** `getLandingPageList`: Get a list of landing pages. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get a list of product variants** `getProductVariantList`: Get a list of product variants. Sending a **GET** request to this URL returns a collection of product variant resources that belong to the given shop and product. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * sku * description The `description` fields can be a pattern and we'll try to match this phrase.
* **Get a list of SMS sender names** `getSmsSenderNameList`: Get a list of SMS sender names. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get a list of taxes** `getTaxList`: Get a list of taxes. Sending **GET** request to this URL returns a collection of tax resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below, in the request params section). You can basically search by: * name * createdOn You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get a list of webinars** `getWebinarList`: Get a list of webinars. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get a predefined field by ID** `getPredefinedFieldById`: Get a predefined field by ID. Get detailed information about a specified predefined field.
* **Get a single A/B test by ID** `getAbTestSubjectById`: Get a single A/B test by ID.
* **Get a single A/B test.** `getSplittest`: Get a single A/B test.. Get a single A/B test by ID.
* **Get a single automated SMS message by its ID.** `getSmsAutomationById`: Get a single automated SMS message by its ID..
* **Get a single custom report by ID** `getCustomReportDetails`: Get a single custom report by ID. The endpoint allows retrieving detailed information about a custom report based on the provided `customReportId`. It returns report data, including: * details about the report, * generation statuses of the report files, * URLs from which the report files can be downloaded. More information on using custom reports can be found in the Case Study section of the [API documentation](http://apidocs.getresponse.com/v3/case-study/custom-reports).
* **Get a single form or popup by ID** `getPopupDetails`: Get a single form or popup by ID.
* **Get a single landing page by ID** `getLpsById`: Get a single landing page by ID.
* **Get a single product variant by ID** `getProductVariantById`: Get a single product variant by ID. This method returns product variant according to the given `variantId` in the context of a given `shopId` and `productId`
* **Get a single SMS message by its ID** `getSmsById`: Get a single SMS message by its ID.
* **Get a single tax by ID** `getTaxById`: Get a single tax by ID. This method returns tax with a given `taxId` in the context of a given `shopId`
* **Get a single template by ID** `getTransactionalEmailsTemplatesById`: Get a single template by ID.
* **Get a single Website by ID** `getWebsiteById`: Get a single Website by ID.
* **Get a suppression list by ID** `getSuppressionById`: Get a suppression list by ID.
* **Get a webinar by ID** `getWebinarById`: Get a webinar by ID.
* **Get Account** `getAccount`: Account information.
* **Get Account Blocklist** `getAccountBlocklist`: Returns account blocklist masks.
* **Get Account Callbacks** `getAccountCallbacks`: Get callbacks configuration.
* **Get an address by ID** `getAddress`: Get an address by ID.
* **Get Autoresponder** `getAutoresponder`: Get a single autoresponder by its ID.
* **Get Autoresponders Statistics** `getAutorespondersStatistics`: The statistics for all autoresponders. &gt; This returns the statistics summary for selected autoresponders. You can select them by specifying the autoresponder or campaign IDs. As in all statistics, you can change the date and time range (hourly daily monthly or total). Keep in mind that all statistics date ranges are given in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)) (https://app.getresponse.com/statistics.html?t=followup#total). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get Balance Statistics** `getBalanceStatistics`: Get balance statistics. Returns the balance of subscriptions. Dates in the YYYY-MM-DD format are used as keys in the response.
* **Get Campaign** `getCampaign`: Get a single campaign by the campaign ID. Retrieve detailed information about a single campaign (contact list) by its unique campaignId. The response includes additional campaign settings such as postal address, subscription notification and confirmation settings, opt-in type, and profile information.
* **Get Campaign Blocklist** `getCampaignBlocklist`: Returns campaign blocklist masks.
* **Get Campaign Contacts** `getCampaignContacts`: Get contacts from a single campaign. Provides all contacts from a single campaign. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get Cart** `getCart`: Get cart by ID. This method returns cart with the given `cartId` in the context of a given `shopId`
* **Get Category** `getCategory`: Get a single category by ID. This method returns a category according to the given `categoryId`.
* **Get click tracked link details by click track ID** `getClickTrackById`: Get click tracked link details by click track ID.
* **Get click tracked links list** `getClickTrackList`: Get click tracked links list. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get Confirmation Bodies** `getConfirmationBodies`: Get collection of SUBSCRIPTION CONFIRMATIONS bodies. Sending **GET** request to this url, returns collection of **SUBSCRIPTION CONFIRMATIONS** bodies. Language code used in url must be in ISO 639-1 Language Code Standard.
* **Get Confirmation Subjects** `getConfirmationSubjects`: Get collection of SUBSCRIPTION CONFIRMATIONS subjects. Sending **GET** request to this url, returns collection of **SUBSCRIPTION CONFIRMATIONS** subjects. Language code used in url must be in ISO 639-1 Language Code Standard.
* **Get Contact** `getContact`: Get contact details by contact ID. Returns all available information about an active (non-deleted) contact identified by `contactId`. The response includes basic contact data, associated tags, and values of custom fields
* **Get Contact Activities** `getContactActivities`: Get a list of contact activities. By default, only activities from the last 14 days are returned. To get earlier data, use the `query[createdOn]` parameter. Email open activities, including historical opens, follow your account's current open tracking consent settings: - If contact consent handling is disabled, open activities remain visible regardless of the contact's consent. - If contact consent handling is enabled, open activities are visible when the contact has given consent and hidden when the contact has refused consent. - If the contact has not declared consent, open activities are visible only when your account is configured to assume consent. They are hidden when your account assumes no consent or treats the contact as anonymous. Hidden open activities are excluded from the pagination totals. Other activity types are unaffected. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resourc...
* **Get contact's consent fields** `getContactConsentsById`: Get contact's consent fields. Returns a list of all consent fields assigned to the contact, including their current status and history of changes.
* **Get custom events by custom event ID** `getCustomEventById`: Get custom events by custom event ID.
* **Get Custom Field** `getCustomField`: Get a single custom field definition by the custom field ID. Returns a list of custom fields
* **Get details for landing page statistics** `getLpsGeneralPerformanceStats`: Get details for landing page statistics.
* **Get details for the SMS message statistics** `getSmsStats`: Get details for the SMS message statistics.
* **Get details for website statistics** `getWbeGeneralPerformanceStats`: Get details for website statistics.
* **Get file by ID** `getFileById`: Get file by ID.
* **Get Form** `getForm`: Get form by ID.
* **Get From Field** `getFromField`: Get a single 'From' address by ID.
* **Get GDPR Field details** `getGDPRField`: Get GDPR Field details.
* **Get images list** `getImageList`: Get images list.
* **Get import details by ID.** `getImportById`: Get import details by ID..
* **Get Industries** `getIndustries`: List of Industry Tags. List of Industry Tags in account's language context.
* **Get List Size Statistics** `getListSizeStatistics`: Get campaign size statistics. Returns the number of the total added and removed subscribers, grouped by default or by time period. Contact moves between lists are not reflected in these statistics.
* **Get Locations Statistics** `getLocationsStatistics`: Get subscriber location statistics. The results are indexed with the location name (PL, EN, etc.).
* **Get Newsletter** `getNewsletter`: Get a single newsletter by its ID..
* **Get Newsletter Activities** `getNewsletterActivities`: Get newsletter activities. **DEPRECATED**: This method is deprecated and scheduled for removal. To synchronise newsletter activities please use [custom reports](https://apireference.getresponse.com/#operation/createCustomReport) with type `message_activity_reports`. This is the preferred approach due to better performance. By default, activities from the **last 14 days** are listed only. You can get activities for last 30 days only. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get newsletter thumbnail** `getNewsletterThumbnail`: Get newsletter thumbnail.
* **Get Newsletters Statistics** `getNewslettersStatistics`: Total newsletter statistics. &gt;This makes it possible to fetch newsletter statistics based on the list of campaign or newsletter IDs (you can pass them in the query parameter - see the description below). Remember that all the statistics date ranges are returned in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get Order** `getOrder`: Get a single order by ID. This method returns the order according to the given `orderId`.
* **Get Origins Statistics** `getOriginsStatistics`: Get subscriber origin statistics. The results are indexed with the campaign ID.
* **Get Product** `getProduct`: Get a single product by ID. This method returns product according to the given `productId` in the context of a given `shopId`.
* **Get Removals Statistics** `getRemovalsStatistics`: Get removal statistics. Returns the number and reason for removed contacts. Dates in the YYYY-MM-DD format are used as keys in the response.
* **Get RSS Newsletter** `getRssNewsletter`: Get RSS newsletter by ID.
* **Get RSS newsletter statistics by ID** `getSingleRssNewsletterStatisticsCollection`: Get RSS newsletter statistics by ID. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get RSS Newsletters Statistics** `getRssNewslettersStatistics`: The statistics for all RSS newsletters. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get Segment** `getSearchContacts`: Get search contacts by contact ID.. Get the definition of a specific contact-search filter.
* **Get Segment Contacts** `getSearchContactsContacts`: Get contacts by search contacts ID. Get contacts from saved search contacts by ID.
* **Get Shop** `getShop`: Get a single shop by ID. This method returns the shop according to the given `shopId`
* **Get single landing page by ID** `getLandingPageById`: Get single landing page by ID.
* **Get statistics for a single form or popup** `getPopupGeneralPerformance`: Get statistics for a single form or popup.
* **Get storage space information** `getFileLibraryQuota`: Get storage space information.
* **Get Subscriptions Statistics** `getSubscriptionsStatistics`: Get the number and origin of subscription statistics. Returns the number and origin of subscriptions, grouped by a specified campaigns for each day on which any changes were made. Dates in the YYYY-MM-DD format are used as keys in the response.
* **Get Summary Statistics** `getSummaryStatistics`: Get the statistics summary for selected campaigns. The results are indexed with the campaign ID.
* **Get suppression lists** `getSuppressionsList`: Get suppression lists.
* **Get Tag** `getTag`: Get tag by ID. Retrieve a specific tag by its ID
* **Get the autoresponder thumbnail** `getAutoresponderThumbnail`: Get the autoresponder thumbnail.
* **Get the ecommerce general performance statistics** `getGeneralPerformanceStats`: Get the ecommerce general performance statistics.
* **Get the ecommerce revenue statistics** `getRevenueStats`: Get the ecommerce revenue statistics.
* **Get the GDPR fields list** `getGDPRFieldList`: Get the GDPR fields list.
* **Get the list of "Facebook Pixels"** `getFacebookPixelList`: Get the list of "Facebook Pixels". Returns the name and ID of "Facebook Pixels" assigned to a user's account.
* **Get the list of automated SMS messages.** `getSMSAutomationList`: Get the list of automated SMS messages.. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get the list of files** `getFileList`: Get the list of files. By default, you can only search files in the root directory. To search for files in all folders, use the parameter `query[allFolders]=true`. To search for files in a specified folder, use the parameter `query[folderId]=&lt;folderId&gt;`. **Note: these two parameters can't be used together**. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get the list of folders** `getFolderList`: Get the list of folders. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get the list of form variants (A/B tests)** `getFormVariantList`: Get the list of form variants (A/B tests).
* **Get the list of forms and popups** `getPopupsList`: Get the list of forms and popups. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get the list of landing pages** `getLpsList`: Get the list of landing pages. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get the list of SMS messages** `getSMSList`: Get the list of SMS messages. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get the list of transactional email templates** `getTransactionalEmailsTemplatesList`: Get the list of transactional email templates. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get the list of transactional emails** `getTransactionalEmailsList`: Get the list of transactional emails. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get the list of websites** `getWebsitesList`: Get the list of websites. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get the meta field by ID** `getMetaField`: Get the meta field by ID. This method returns meta field with a given `metaFieldId` in the context of a given `shopId`
* **Get the overall statistics of transactional emails** `getTransactionalEmailsStatistics`: Get the overall statistics of transactional emails.
* **Get the predefined fields list** `getPredefinedFieldList`: Get the predefined fields list. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get the shop meta fields** `getMetaFields`: Get the shop meta fields. Sending a **GET** request to this URL returns a collection of meta field resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * value * description * createdOn You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Get Tracking JavaScript code snippets** `getTracking`: Get Tracking JavaScript code snippets. With code snippets you will be able to track Purchases, Abandoned carts, and Visited URLs. Find more in our [Help Center](https://www.getresponse.com/help/marketing-automation/ecommerce-conditions/how-do-i-add-the-tracking-javascript-code-to-my-website.html).
* **Get transactional email details by transactional email ID** `getTransactionalEmailsById`: Get transactional email details by transactional email ID.
* **Get Webform** `getWebform`: Get Legacy Form by ID.. Get Legacy Form by ID.
* **Get Workflow** `getWorkflow`: Get workflow by ID. Get a single workflow by ID.
* **History of logins** `getAccountLoginHistory`: History of logins.
* **List Autoresponders** `listAutoresponders`: Get the list of autoresponders.. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Campaigns** `listCampaigns`: Get a list of campaigns. Returns a list of campaigns (contact lists). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Carts** `listCarts`: Get shop carts. Sending a **GET** request to this URL returns a collection of cart resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * externalId * createdOn You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Categories** `listCategories`: Get the shop categories list. Sending a **GET** request to this URL returns a collection of category resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: *name * createdOn * parentId The `name` fields can be a pattern and we'll try to match this phrase. The `parentId` will search for sub-categories of a given parent category. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Contacts** `listContacts`: Get contact list. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Custom Fields** `listCustomFields`: Get a list of custom fields. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Forms** `listForms`: Get the list of forms.. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List From Fields** `listFromFields`: Get the list of 'From' addresses. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Newsletters** `listNewsletters`: Get the newsletter list. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List of timezones** `getTimezones`: List of timezones. List of timezones in account's language context.
* **List Orders** `listOrders`: Get the list of orders. Sending a **GET** request to this URL returns a collection of order resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * description * status * externalId * processedAt The `description` fields can be a pattern and we'll try to match this phrase. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Products** `listProducts`: Get a product list.. Sending a **GET** request to this URL returns a collection of product resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * vendor * category * categoryId * externalId * variantName * metaFieldNames * metaFieldValues * createdOn The `metaFieldNames` and `metaFieldValues` fields can be a list of values separated by a comma [,]. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List RSS Newsletters** `listRssNewsletters`: Get the list of RSS newsletters. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Segments** `listSearchContacts`: Get a saved search contact list. Makes it possible to retrieve a collection of short representations of search-contact (known as custom filters in the panel). Every item represents a basic filter object. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Shops** `listShops`: Get a list of shops. Sending a **GET** request to this URL returns a collection of shop resources. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name The `name` fields can be a pattern and we'll try to match this phrase. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Tags** `listTags`: Get the list of tags. Provides a list of tags. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Webforms** `listWebforms`: Get Legacy Forms.. Get the list of Legacy Forms. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **List Workflows** `listWorkflows`: Get workflows. Get the list of workflows.
* **Query Contacts By Conditions** `queryContacts`: Search contacts using conditions. Makes it possible to get a collection of contacts according to a given condition. Please refer to [Segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual)
* **Schedule a new contact import** `createImport`: Schedule a new contact import. This endpoint lets you schedule a contact import. That way, you can add and update your contacts using a single API call. Since API imports are asynchronous, you should check periodically for updates while your original API request is being processed. To keep track of your import status, use [GET import](https://apireference.getresponse.com/#operation/getImportById) (provide the importId from the response), or subscribe to an [import finished](https://apidocs.getresponse.com/v3/payloads#contacts-import-finished) webhook. Please note, that this endpoint has **specific rate limits** - for details please refer to [Create Import Limits](https://apidocs.getresponse.com/v3/case-study/create-import#limits). For more information on imports, check our [API Docs](https://apidocs.getresponse.com/v3/case-study/create-import) or [Help Center](https://www.getresponse.com/help/how-do-i-prepare-a-file-for-import.html)
* **Send an SMS message** `sendSms`: Send an SMS message. Sends a new SMS (text) message to a list of recipients
* **Send Draft Newsletter** `sendDraftNewsletter`: Send the newsletter draft.
* **Send limits** `getSendingLimits`: Send limits.
* **Send transactional email** `createTransactionalEmail`: Send transactional email.
* **Set Default From Field** `setDefaultFromField`: Set a 'From' address as default.
* **The list of A/B tests** `getAbTestSubjectList`: The list of A/B tests. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **The list of A/B tests.** `getSplittestList`: The list of A/B tests.. The list of A/B tests. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **The statistics for a single autoresponder** `getSingleAutoresponderStatistics`: The statistics for a single autoresponder. &gt; This requst returns the statistics summary for a single given autoresponder. As in all statistics, you can change the date and time range (hourly daily monthly or total). Keep in mind that all statistics date ranges are given in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)) (https://app.getresponse.com/statistics.html?t=followup#total). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **The statistics of single newsletter** `getSingleNewsletterStatistics`: The statistics of single newsletter. &gt; This makes it possible to easily fetch statistics for a single newsletter. You can group the data hourly, daily, monthly and as a total sum. Remember that all statistics date ranges are given in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by.
* **Trigger a custom event** `triggerCustomEvent`: Trigger a custom event.
* **Turn on/off the GetResponse Badge** `updateAccountBadge`: Turn on/off the GetResponse Badge.
* **Update a predefined field** `updatePredefinedField`: Update a predefined field.
* **Update a suppression list by ID** `updateSuppression`: Update a suppression list by ID.
* **Update account** `updateAccount`: Update account.
* **Update address** `updateAddress`: Update address. Update an existing address. You should send only those fields that need to be changed. The rest of the properties will stay the same.
* **Update Autoresponder** `updateAutoresponder`: Update autoresponder. &gt; **The action-based autoresponder feature has been migrated over to marketing automation. Your existing autoresponders are now converted into workflows. You can no longer create and update action-based autoresponders using our API.** This method allows you to update an autoresponder. The same rules as in creating an autoresponder apply.
* **Update Campaign** `updateCampaign`: Update a campaign.
* **Update Cart** `updateCart`: Update cart. Update properties of the shop cart. You should send only those fields that need to be changed. The rest of the properties will stay the same. In case of selectedVariants, when the collection is updated, the old one is completely removed.
* **Update Category** `updateCategory`: Update category. Update the properties of the shop category. You can specify a `parentId` to assign a category as sub-category for an existing category. You should send only those fields that need to be changed. The rest of the properties will stay the same.
* **Update Contact** `updateContact`: Update contact details. Skip the fields you don't want to update. If tags and custom fields are provided, they'll be **replaced** with the values sent in this request. If the `campaignId` changes, the contact will be moved from the original campaign (list) to the new campaign (list). Their activity history and statistics will also be moved.
* **Update custom event details** `updateCustomEvent`: Update custom event details.
* **Update Custom Field** `updateCustomField`: Update the custom field definition.
* **Update meta field** `updateMetaField`: Update meta field. Update the properties of a shop's meta field. You should send only those fields that need to be changed. The rest of the properties will stay the same.
* **Update Order** `updateOrder`: Update order. Update the properties of a shop's order. You should send only those fields that need to be changed. The rest of the properties will stay the same. However, in case of `billingAddress` and `shippingAddress`, you must send the entire representation. Individual fields can't be updated. If you want to update individual fields of an address, you can do so using `POST /v3/addresses/{addressId}`. In case of `selectedVariants`, when the collection is updated, the old collection is completely removed. The same goes for meta fields. Individual fields can't be updated either. The full representations of `selectedVariants` and `metaFields` must be sent instead.
* **Update Product** `updateProduct`: Update product. Update the properties of a shop's product. You should only send those fields that need to be changed. The remaining properties will stay the same. However, when updating variants, categories, and meta fields, you need to send entire collections. Individual fields can't be updated. If you want to update particular fields, you can do so using their specific endpoints, i.e.: * categories - `POST /v3/shops/{shopId}/categories/{categoryId}` * variants - POST `/v3/shops/{shopId}/products/{productId}/variants/{variantId}` * metaFields - `POST /v3/shops/{shopId}/meta-fields/{metaFieldId}`
* **Update product variant** `updateProductVariant`: Update product variant. Update properties of a product variant. You should send only those fields that need to be changed. The remaining properties will stay the same. However, when updating metafields, images, and taxes, you need to send entire collections. Individual fields can't be updated. If you want to update particular metafields or tax resources, you can do so using their particular endpoints, i.e: * taxes - `POST /v3/shops/{shopId}/taxes/{taxId}` * metaFields - `POST /v3/shops/{shopId}/meta-fields/{metaFieldId}`
* **Update RSS newsletter** `updateRssNewsletter`: Update RSS newsletter.
* **Update Segment** `updateSearchContacts`: Update search contacts. Update specified search contacts.
* **Update Shop** `updateShop`: Update shop. This makes it possible to update shop preferences. You should send only those fields that need to be changed. The rest of the properties remain the same.
* **Update tax** `updateTax`: Update tax. Update the properties of the shop tax. You should only send the fields that need to be changed. The rest of the properties will stay the same.
* **Update transactional email template** `updateTransactionalEmailsTemplate`: Update transactional email template. This method allows you to update transactional email template
* **Update workflow** `updateWorkflow`: Update workflow. Update single workflow.
* **Upload image** `uploadImage`: Upload an image to the GetResponse multimedia gallery (POST /multimedia, multipart/form-data, part 'file'). Engine limit: only TEXT file content can be sent (e.g. an SVG); binary images (jpg/png/gif) cannot be transmitted through this action. Docs: https://apireference.getresponse.com/#operation/uploadImage
* **Upsert custom fields by search contacts** `upsertCustomFieldsBySearchContactId`: Upsert custom fields by search contacts. Makes it possible to add and update custom field values for all contacts that meet the search criteria. This method doesn't remove or overwrite custom fields with the values from the request.
* **Upsert product categories** `upsertProductCategories`: Upsert product categories. This method makes it possible to assign product categories, and to set a default product category. This method doesn't remove or unassign product categories. It returns a list of product categories. Please note that if you assign only one category to a given product, that category is marked as default. If you try to remove the default mark, your change won't be executed.
* **Upsert product meta fields** `upsertMetaFields`: Upsert product meta fields. This method makes it possible to assign meta fields. It doesn't remove or unassign meta fields. It returns a list of product meta fields.
* **Upsert the custom fields of a contact** `upsertContactCustoms`: Upsert the custom fields of a contact. Upsert (add or update) the custom fields of a contact. This method doesn't remove (unassign) custom fields.
* **Upsert the tags of a contact** `upsertTags`: Upsert the tags of a contact. Upsert (add or update) the tags of a contact. This method doesn't remove (unassign) tags.

</details>
