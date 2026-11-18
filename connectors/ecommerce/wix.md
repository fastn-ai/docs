---
description: "Wix REST API connector (www.wixapis.com)."
hidden: true
---

# Wix

<img src="../../.gitbook/assets/connectors/lg/wix.png" alt="Wix logo">

Wix REST API connector (www.wixapis.com). Stores (products/inventory/categories), eCommerce (orders/cart/checkout), CRM contacts, members, bookings, Wix Data/CMS, media, site properties, locations. Account-level API key auth: Authorization header (raw key) + wix-site-id (site APIs) / wix-account-id (account APIs).

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [wix.com](https://wix.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Slug** | `wix` |

## Use it

Add Wix from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wix.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Customization Choices (V3) | `addCustomizationChoices` | Add choices to a customization (1-100). |
| Add Item To Categories | `addItemToCategories` | Add ONE product to MANY categories. item:{catalogItemId,appId}, categoryIds:[...]. |
| Add Line Items To Draft Order | `addLineItemsToDraft` | Add catalog or custom line items to a draft order. POST /ecom/v1/draft-orders/{draftOrderId}/add-line-items. |
| Add Location Type | `addLocationType` | Adds a location type to an existing business location. The location is identified by its ID in the path. |
| Add Order Activities | `addOrderActivities` | Add activities to an order. POST /ecom/v1/orders/{orderId}/activities/add. Each orderActivities[] entry needs activityType (enum, e.g. MERCHANT_COMMENT) plus the matching content object (e.g. merchantComment:{message} or customActivity:{type,additionalData,appId}). |
| Add Payment | `addPayment` | Record payment(s) on an order (does NOT charge). POST /ecom/v1/payments/orders/{orderId}/add-payment. payments[] item shape: {amount:{amount:'10.00'}, regularPaymentDetails:{offlinePayment:true,status:'APPROVED'}}. amount is a Price object, not a bare string. |
| Add Products To Category | `addProductsToCategory` | Add many products to ONE category (max 1000). Provide items: [{catalogItemId, appId}]. appId is the Wix Stores app GUID. |
| Add To Cart | `addToCart` | Add catalog line items to an existing cart. POST /ecom/v1/carts/{cartId}/add-to-cart with body {lineItems:[{catalogReference,quantity}]}. |
| Add To Checkout | `addToCheckout` | Add line items to an existing checkout. POST /ecom/v1/checkouts/{id}/add-to-checkout. |
| Add To Current Cart | `addToCurrentCart` | Add line items to the current cart. POST /ecom/v1/carts/current/add-to-cart with body {lineItems}. |

<details>

<summary>See 402 more actions</summary>

* **Aggregate Data Items** `aggregateItems`: Run grouping/aggregation (sum/avg/min/max/count) over a Wix Data collection.
* **Approve Member** `approveMember`: Approve a pending member so they can log in.
* **Archive Location** `archiveLocation`: Archive a business location. POST /locations/v1/locations/{id}/archive. The default location cannot be archived.
* **Assign Badge** `assignBadge`: Assign a badge to a member (create badge assignment, Badges v4).
* **Assign Working Hours Schedule** `assignWorkingHoursSchedule`: Assign a working-hours schedule to a staff member (Staff Members v1).
* **Block Member** `blockMember`: Block a member from logging in.
* **Bulk Add Customization Choices (V3)** `bulkAddCustomizationChoices`: Add choices to multiple customizations. customizationsChoices: [{customizationId,choices}].
* **Bulk Add Info Sections To Products (V3)** `bulkAddInfoSectionsToProducts`: Add up to 10 info sections to products (by product id+revision).
* **Bulk Add Info Sections To Products By Filter (V3)** `bulkAddInfoSectionsToProductsByFilter`: Async: add up to 10 info sections to products matching a filter. Returns jobId.
* **Bulk Add Products To Categories By Filter (V3)** `bulkAddProductsToCategoriesByFilter`: Async: add products matching a filter to up to 5 categories. Returns jobId.
* **Bulk Adjust Product Variants By Filter (V3)** `bulkAdjustProductVariantsByFilter`: Async: adjust variant prices/costs by amount or percentage for variants matching a filter. Returns jobId.
* **Bulk Approve Members By Filter** `bulkApproveMembersByFilter`: Approve members matching a filter (async, returns jobId).
* **Bulk Assign Badges** `bulkAssignBadges`: Assign multiple badge-member pairs in one call (Badges v4, up to 100).
* **Bulk Block Members By Filter** `bulkBlockMembersByFilter`: Block members matching a filter (async, returns jobId).
* **Bulk Confirm Or Decline Bookings** `bulkConfirmOrDeclineBookings`: Confirm or decline up to 300 bookings in one call (Bookings v2).
* **Bulk Create Bookings** `bulkCreateBookings`: Create up to 12 bookings in one call (Bookings v2).
* **Bulk Create Brands (V3)** `bulkCreateBrands`: Create multiple brands (1-100).
* **Bulk Create Coupons** `bulkCreateCoupons`: Create multiple coupons at once. POST /stores/v2/bulk/coupons/create with body {specifications}.
* **Bulk Create Customizations (V3)** `bulkCreateCustomizations`: Create multiple customizations (1-100).
* **Bulk Create Fulfillments** `bulkCreateFulfillments`: Create fulfillments for multiple orders. POST /ecom/v1/fulfillments/orders/bulk/create-fulfillments with body {ordersWithFulfillments:[{orderId,fulfillments:[...]}]}.
* **Bulk Create Info Sections (V3)** `bulkCreateInfoSections`: Create multiple info sections (1-100).
* **Bulk Create Inventory Items (V3)** `bulkCreateInventoryItems`: Create multiple inventory items (max 1000). Each needs variantId+productId; quantity (tracked) or inStock.
* **Bulk Create Products (V3)** `bulkCreateProducts`: Create multiple Wix Stores products in one call (max 100). Pass products array; each needs name, productType, variantsInfo with price.
* **Bulk Create Products With Inventory (V3)** `bulkCreateProductsWithInventory`: Create products plus default-location inventory in one call (max 100).
* **Bulk Create Ribbons (V3)** `bulkCreateRibbons`: Create multiple ribbons (1-100).
* **Bulk Create Services** `bulkCreateServices`: Create up to 100 services in one call (Services v2).
* **Bulk Decrement Inventory By Variant And Location (V3)** `bulkDecrementInventoryItemsByVariantAndLocation`: Decrement inventory by variantId (+optional locationId), max 300. decrementData: [{variantId,decrementBy}].
* **Bulk Decrement Inventory Items (V3)** `bulkDecrementInventoryItems`: Decrement quantities for inventory items by ID (max 300). decrementData: [{inventoryItemId,decrementBy}].
* **Bulk Delete Brands (V3)** `bulkDeleteBrands`: Delete multiple brands by IDs (1-100).
* **Bulk Delete Contacts** `bulkDeleteContacts`: Deletes multiple contacts matching filter and/or search. Starts a bulk job, returns jobId. POST /contacts/v4/bulk/contacts/delete. Must include filter or search.
* **Bulk Delete Coupons** `bulkDeleteCoupons`: Delete multiple coupons at once. POST /stores/v2/bulk/coupons/delete with body {ids}.
* **Bulk Delete Info Sections (V3)** `bulkDeleteInfoSections`: Delete multiple info sections by IDs (1-100).
* **Bulk Delete Inventory Items (V3)** `bulkDeleteInventoryItems`: Delete multiple inventory items by IDs (max 1000).
* **Bulk Delete Media Files** `bulkDeleteFiles`: Move (or permanently delete) media files. POST /site-media/v1/bulk/files/delete with { fileIds:[], permanent? }.
* **Bulk Delete Media Folders** `bulkDeleteFolders`: Move (or permanently delete) media folders. POST /site-media/v1/bulk/folders/delete with { folderIds:[], permanent? }.
* **Bulk Delete Members** `bulkDeleteMembers`: Delete up to 100 members by ID list. Synchronous per-item results.
* **Bulk Delete Members By Filter** `bulkDeleteMembersByFilter`: Delete members matching a filter (async, returns jobId).
* **Bulk Delete Products (V3)** `bulkDeleteProducts`: Delete multiple Wix Stores products by IDs (1-100).
* **Bulk Delete Products By Filter (V3)** `bulkDeleteProductsByFilter`: Async: delete products matching a filter. Returns jobId.
* **Bulk Delete Ribbons (V3)** `bulkDeleteRibbons`: Delete multiple ribbons by IDs (1-100).
* **Bulk Delete Services** `bulkDeleteServices`: Delete multiple services by ID list (Services v2).
* **Bulk Get Or Create Brands (V3)** `bulkGetOrCreateBrands`: Get or create multiple brands by name (1-100).
* **Bulk Get Or Create Info Sections (V3)** `bulkGetOrCreateInfoSections`: Get or create multiple info sections (1-100).
* **Bulk Get Or Create Ribbons (V3)** `bulkGetOrCreateRibbons`: Get or create multiple ribbons by name (1-100).
* **Bulk Import Media Files** `bulkImportFile`: Import multiple files from external URLs into Media Manager.
* **Bulk Increment Inventory By Variant And Location (V3)** `bulkIncrementInventoryItemsByVariantAndLocation`: Increment inventory by variantId (+optional locationId), max 300. incrementData: [{variantId,incrementBy}].
* **Bulk Increment Inventory Items (V3)** `bulkIncrementInventoryItems`: Increment quantities for inventory items by ID (max 300). incrementData: [{inventoryItemId,incrementBy}].
* **Bulk Insert Data Items** `bulkInsertItems`: Insert multiple items into a Wix Data collection in one call. CMS app may be uninstalled -&gt; WDE0110.
* **Bulk Label And Unlabel Contacts** `bulkLabelAndUnlabelContacts`: Adds and removes labels from multiple contacts matching filter/search. Starts a bulk job, returns jobId. POST /contacts/v4/bulk/contacts/add-remove-labels. Must include filter or search.
* **Bulk Patch Data Items** `bulkPatchItems`: Apply atomic field modifications (SET_FIELD/INCREMENT_FIELD/etc.) to multiple items.
* **Bulk Remove Data Items** `bulkRemoveItems`: Remove multiple items from a Wix Data collection by ID array (dataItemIds).
* **Bulk Remove Info Sections From Products (V3)** `bulkRemoveInfoSectionsFromProducts`: Remove info sections from products (by product id+revision).
* **Bulk Remove Info Sections From Products By Filter (V3)** `bulkRemoveInfoSectionsFromProductsByFilter`: Async: remove info sections from products matching a filter. Returns jobId.
* **Bulk Remove Products From Categories By Filter (V3)** `bulkRemoveProductsFromCategoriesByFilter`: Async: remove products matching a filter from up to 5 categories. Returns jobId.
* **Bulk Restore Media Files** `bulkRestoreFilesFromTrashBin`: Restore deleted media files from the trash bin.
* **Bulk Restore Media Folders** `bulkRestoreFoldersFromTrashBin`: Restore deleted media folders from the trash bin.
* **Bulk Save Data Items** `bulkSaveItems`: Upsert multiple items (insert or update) into a Wix Data collection.
* **Bulk Set Attendance** `bulkSetAttendance`: Set attendance for up to 8 bookings in one call (Attendance v2).
* **Bulk Show Categories** `bulkShowCategories`: Bulk set categories visible=true by IDs. Requires treeReference.
* **Bulk Unassign Badges** `bulkUnassignBadges`: Delete multiple badge assignments by assignment ID (Badges v4, up to 100).
* **Bulk Update Brands (V3)** `bulkUpdateBrands`: Update multiple brands; each item {brand:{id,revision,name}}.
* **Bulk Update Categories** `bulkUpdateCategories`: Update multiple categories; each item {category:{id,revision,...}}. Requires treeReference.
* **Bulk Update Contacts** `bulkUpdateContacts`: Updates specified properties for multiple contacts matching filter/search. Only fieldMask.paths are updated. Starts a bulk job, returns jobId. POST /contacts/v4/bulk/contacts/update.
* **Bulk Update Customizations (V3)** `bulkUpdateCustomizations`: Update multiple customizations; each item {customization:{id,revision,name,...}}.
* **Bulk Update Data Items** `bulkUpdateItems`: Update multiple existing items (each must include id) in a Wix Data collection.
* **Bulk Update Info Sections (V3)** `bulkUpdateInfoSections`: Update multiple info sections; each item {infoSection:{id,revision,...}}.
* **Bulk Update Inventory Items (V3)** `bulkUpdateInventoryItems`: Update multiple inventory items (max 1000). Each item: {inventoryItem:{id,revision,quantity|inStock}}.
* **Bulk Update Inventory Items By Filter (V3)** `bulkUpdateInventoryItemsByFilter`: Async: update inventory items matching a filter (set quantity or inStock). Returns jobId.
* **Bulk Update Order Tags** `bulkUpdateOrderTags`: Assign tags on multiple orders. POST /ecom/v1/bulk/orders/update-tags. assignTags is a Tags object: {tags:{tagIds:[...]}, privateTags:{tagIds:[...]}}. tagIds max 5 chars each.
* **Bulk Update Orders** `bulkUpdateOrders`: Update multiple orders at once. POST /ecom/v1/bulk/orders/update with body {orders:[{order:{id,revision,...}}],returnEntity}.
* **Bulk Update Payment Transaction Status** `bulkUpdatePaymentTransactionStatus`: Update transaction status for multiple payments. POST /ecom/v1/bulk/payments/update-payment-transaction-status with body {paymentAndOrderIds,status,returnFullEntity}.
* **Bulk Update Product Variants By Filter (V3)** `bulkUpdateProductVariantsByFilter`: Async: set explicit values on variants matching a filter (visible/price/cost/physicalProperties). Returns jobId.
* **Bulk Update Products (V3)** `bulkUpdateProducts`: Update multiple Wix Stores products (max 100). Each item must contain product with id and revision.
* **Bulk Update Products By Filter (V3)** `bulkUpdateProductsByFilter`: Async: update products matching a filter. Returns jobId. Cannot update slug/options/modifiers/variantsInfo.
* **Bulk Update Products With Inventory (V3)** `bulkUpdateProductsWithInventory`: Update products plus inventory in one call. Each item needs product id+revision.
* **Bulk Update Ribbons (V3)** `bulkUpdateRibbons`: Update multiple ribbons; each item {ribbon:{id,revision,name}}.
* **Calculate Booking Price** `calculateBookingPrice`: Calculate the price for an existing booking (Pricing v2).
* **Cancel Booking** `cancelBooking`: Cancel a booking. Requires current revision (Bookings Writer V2).
* **Cancel Calendar Event** `cancelEvent`: Cancel a calendar event by ID (Calendar V3).
* **Cancel Order** `cancelOrder`: Cancel an eCommerce order. POST /ecom/v1/orders/{orderId}/cancel with body {restockAllItems, sendOrderCanceledEmail}.
* **Cancel Schedule** `cancelSchedule`: Cancel a calendar schedule by ID (Calendar V3).
* **Clone Service** `cloneService`: Clone an existing service (Services v2).
* **Commit Draft Order** `commitDraftOrder`: Commit a draft order to create/update a real order. POST /ecom/v1/draft-orders/{draftOrderId}/commit.
* **Confirm Booking** `confirmBooking`: Confirm a pending booking (Bookings v2). Requires bookingId and revision.
* **Confirm Or Decline Booking** `confirmOrDeclineBooking`: Confirm or decline a booking based on paymentStatus. Requires current revision (Bookings Writer V2).
* **Count Attendances** `countAttendances`: Count attendance records matching a filter (Attendance v2).
* **Count Booking Policies** `countBookingPolicies`: Count booking policies matching a filter (Booking Policies v1).
* **Count Categories** `countCategories`: Count Wix Stores categories matching an optional filter. Requires treeReference @wix/stores.
* **Count Data Items** `countItems`: Count Wix Data items matching an optional filter. POST /items/count with { dataCollectionId, filter }.
* **Count Extended Bookings** `countExtendedBookings`: Count bookings matching a filter (Bookings Reader v2).
* **Count Products (V3)** `countProducts`: Count Wix Stores products matching an optional filter (Catalog V3).
* **Count Resources** `countResources`: Count bookable resources matching a filter (Resources v2).
* **Count Services** `countServices`: Count services matching a filter (Services v2).
* **Count Sites** `countSites`: Count sites in the Wix account (account-level).
* **Count Staff Members** `countStaffMembers`: Count staff members matching a filter (Staff Members v1).
* **Count Tasks** `countTasks`: Counts the number of CRM tasks, optionally filtered. POST /crm/tasks/v2/tasks/count.
* **Create Badge** `createBadge`: Create a member badge (Badges v4). Requires title, backgroundColor, textColor.
* **Create Booking** `createBooking`: Create a single-service booking (Bookings Writer V2).
* **Create Booking Form** `createBookingForm`: Create a booking form schema (Wix Forms). Set form.namespace to wix.bookings.v2.bookings.
* **Create Booking Policy** `createBookingPolicy`: Create a booking policy (Booking Policies v1). Requires name.
* **Create Brand (V3)** `createBrand`: Create a Wix Stores brand. Required: name (unique, 1-50 chars).
* **Create Calendar Event** `createEvent`: Create a calendar event/session (Calendar V3). Requires scheduleId, start/end localDate, location.type.
* **Create Cart** `createCart`: Create an eCommerce cart. POST /ecom/v2/carts (Cart V2). The lineItems input is sent as catalogItems: [{catalogReference:{appId,catalogItemId},quantity}].
* **Create Category** `createCategory`: Create a Wix Stores category. Required: category.name and treeReference.appNamespace='@wix/stores'.
* **Create Checkout** `createCheckout`: Create a checkout directly. POST /ecom/v1/checkouts with body {lineItems:[{catalogReference,quantity}],channelType}.
* **Create Checkout From Cart** `createCheckoutFromCart`: Create a checkout from a cart. POST /ecom/v1/carts/{cartId}/create-checkout with body {channelType}.
* **Create Checkout From Current Cart** `createCheckoutFromCurrentCart`: Create a checkout from the current cart. POST /ecom/v1/carts/current/create-checkout with body {channelType}.
* **Create Contact** `createContact`: Create a new contact (Contacts V4). info must include at least one of name, emails.items[].email, or phones.items[].phone. Set allowDuplicates to avoid duplicate-email errors. Returns contact.id and contact.revision.
* **Create Coupon** `createCoupon`: Create a discount coupon. POST /stores/v2/coupons with body {specification}.
* **Create Customization (V3)** `createCustomization`: Create a product option or modifier. Required: name, customizationType (PRODUCT_OPTION|MODIFIER), customizationRenderType. Provide choicesSettings.choices for TEXT/SWATCH or freeTextInput for FREE_TEXT.
* **Create Data Collection** `createCollection`: Create a new Wix Data (CMS) collection. Requires collection.id, at least one field (key+type), and a permissions object.
* **Create Data Index** `createIndex`: Create an index on a Wix Data collection for faster queries.
* **Create Discount Rule** `createDiscountRule`: Create an automatic discount rule. POST /ecom/v1/discount-rules with body {discountRule}.
* **Create Draft Custom Additional Fees** `createDraftAdditionalFees`: Add custom additional fees to a draft order. POST /ecom/v1/draft-orders/{draftOrderId}/create-additional-fees.
* **Create Draft Custom Discounts** `createDraftCustomDiscounts`: Add custom discounts to a draft order. POST /ecom/v1/draft-orders/{draftOrderId}/create-custom-discounts.
* **Create Draft Order** `createDraftOrder`: Create a draft order. POST /ecom/v1/draft-orders with body {draftOrder:{catalogLineItems:[{catalogReference,quantity}]}}.
* **Create Fulfillment** `createFulfillment`: Create a fulfillment for an order. POST /ecom/v1/fulfillments/orders/{orderId}/create-fulfillment with body {fulfillment:{lineItems:[{id,quantity}],trackingInfo}}.
* **Create Info Section (V3)** `createInfoSection`: Create a Wix Stores info section. Required: uniqueName, title (1-50 chars).
* **Create Inventory Item (V3)** `createInventoryItem`: Create a Wix Stores inventory item (Catalog V3). Required: inventoryItem.variantId, inventoryItem.productId, and either quantity (tracked) or inStock (status). variantId+locationId must be unique.
* **Create Location** `createLocation`: Create a business location. POST /locations/v1/locations with { location: { name, address, timeZone } }.
* **Create Media Folder** `createFolder`: Create a folder in the Media Manager. POST /site-media/v1/folders with { displayName, parentFolderId? }.
* **Create Member** `createMember`: Create a site member. Requires member.loginEmail.
* **Create Member About** `createMemberAbout`: Create the rich-text About section for a member (Members About v2). Content is Ricos rich content.
* **Create Note** `createNote`: Creates a note associated with a contact. POST /crm/notes/v2/notes. Body wrapped in {note:{...}}.
* **Create Order** `createOrder`: Create an order for your records (POS/external/manual). POST /ecom/v1/orders with body {order}.
* **Create Order From Checkout** `createOrderFromCheckout`: Create an order from a checkout. POST /ecom/v1/checkouts/{checkoutId}/create-order.
* **Create Order From Draft** `createOrderFromDraft`: Create a finalized order from a draft order. POST /ecom/v1/draft-orders/{draftOrderId}/create-order.
* **Create Product (V3)** `createProduct`: Create a Wix Stores product (Catalog V3). Required: product.name, product.productType=PHYSICAL, product.physicalProperties (sent automatically), and at least one variant with price.actualPrice.amount (decimal string).
* **Create Resource** `createResource`: Create a bookable resource (Resources v2). Requires name and typeId.
* **Create Ribbon (V3)** `createRibbon`: Create a Wix Stores ribbon (promotional badge). Required: name (1-30 chars).
* **Create Schedule** `createSchedule`: Create a calendar schedule (Calendar V3). appId for Wix Bookings.
* **Create Service** `createService`: Create a Bookings service (Services V2). Online booking is always enabled (onlineBooking.enabled=true); set hidden=true to keep the service off Bookings pages.
* **Create Service Options And Variants** `createServiceOptionsAndVariants`: Create options and price variants for a service (Service Options and Variants v1).
* **Create Staff Member** `createStaffMember`: Create a staff member (Staff Members v1). Requires name.
* **Create Task** `createTask`: Create a CRM task (Tasks V2). task.title is required (1-250 chars); optional description, dueDate (ISO date-time), status (ACTION_NEEDED/COMPLETED), contact.id. Returns task.id and task.revision (string).
* **Decline Booking** `declineBooking`: Decline a pending booking (Bookings v2). Requires bookingId and revision.
* **Delete Attendance** `deleteAttendance`: Delete an attendance record by ID (Attendance v2).
* **Delete Badge** `deleteBadge`: Delete a member badge by ID (Badges v4).
* **Delete Booking Form** `deleteBookingForm`: Delete a booking form schema by form ID (Wix Forms).
* **Delete Booking Policy** `deleteBookingPolicy`: Delete a booking policy by ID (Booking Policies v1). Cannot delete the default policy.
* **Delete Brand (V3)** `deleteBrand`: Delete a Wix Stores brand by ID.
* **Delete Cart** `deleteCart`: Delete a cart. DELETE /ecom/v1/carts/{cartId}.
* **Delete Category** `deleteCategory`: Delete a Wix Stores category by id.
* **Delete Contact** `deleteContact`: Permanently delete a contact by GUID (Contacts V4). Returns empty body on success.
* **Delete Coupon** `deleteCoupon`: Delete a coupon. DELETE /stores/v2/coupons/{id}.
* **Delete Current Cart** `deleteCurrentCart`: Delete the current cart. DELETE /ecom/v1/carts/current.
* **Delete Customization (V3)** `deleteCustomization`: Delete a product customization by ID (cannot delete while assigned to products).
* **Delete Data Collection** `deleteCollection`: Delete a Wix Data (CMS) collection by its ID.
* **Delete Discount Rule** `deleteDiscountRule`: Delete a discount rule. DELETE /ecom/v1/discount-rules/{discountRuleId}.
* **Delete Draft Custom Additional Fees** `deleteDraftAdditionalFees`: Remove custom additional fees from a draft order. POST /ecom/v1/draft-orders/{draftOrderId}/delete-custom-additional-fees.
* **Delete Draft Custom Discounts** `deleteDraftCustomDiscounts`: Remove custom discounts from a draft order. POST /ecom/v1/draft-orders/{draftOrderId}/delete-custom-discounts.
* **Delete Draft Order** `deleteDraftOrder`: Delete a draft order. DELETE /ecom/v1/draft-orders/{draftOrderId}.
* **Delete Extended Field** `deleteExtendedField`: Delete a custom extended field by key (Extended Fields V4). Returns empty body on success.
* **Delete Fulfillment** `deleteFulfillment`: Delete a fulfillment from an order. DELETE /ecom/v1/fulfillments/{fulfillmentId}/orders/{orderId}.
* **Delete Info Section (V3)** `deleteInfoSection`: Delete a Wix Stores info section by ID.
* **Delete Inventory Item (V3)** `deleteInventoryItem`: Delete a Wix Stores inventory item by id (Catalog V3).
* **Delete Label** `deleteLabel`: Delete a contact label by key (Labels V4). Removes it from all contacts. Returns empty body on success.
* **Delete Member** `deleteMember`: Delete a site member by ID.
* **Delete Member About** `deleteMemberAbout`: Delete a member's About section by About ID (Members About v2).
* **Delete Member Addresses** `deleteMemberAddresses`: Clear all addresses from a member's contact info.
* **Delete Member Emails** `deleteMemberEmails`: DEPRECATED - DO NOT USE. This endpoint cannot succeed by construction. Its only argument is a MEMBER id (DELETE /members/v1/members/{id}/emails), but Wix refuses the operation for anything that is a member: it answers 428 {"message":"Contact email can't be updated if contact is also a member.","code":"CANNOT_UPDATE_MEMBER_EMAIL"}. Verified live against a real member. There is no input for which this returns 2xx. To change a member's email use the Members API member-update flow instead. Ref: https://dev.wix.com/docs/rest/crm/members-contacts/members/members/member-v1
* **Delete Member Phones** `deleteMemberPhones`: Clear all phone numbers from a member's contact info.
* **Delete My Member** `deleteMyMember`: Delete the currently logged-in member (caller). Needs member identity context.
* **Delete Note** `deleteNote`: Deletes a note by ID. DELETE /crm/notes/v2/notes/{noteId}.
* **Delete Product (V3)** `deleteProduct`: Delete a Wix Stores product by id (Catalog V3).
* **Delete Resource** `deleteResource`: Delete a bookable resource by ID (Resources v2).
* **Delete Ribbon (V3)** `deleteRibbon`: Delete a Wix Stores ribbon by ID.
* **Delete Service** `deleteService`: Delete a Bookings service by ID (Services V2).
* **Delete Service Options And Variants** `deleteServiceOptionsAndVariants`: Delete a service options-and-variants object by ID (v1).
* **Delete Staff Member** `deleteStaffMember`: Delete a staff member (and its resource) by ID (Staff Members v1).
* **Delete Task** `deleteTask`: Delete a CRM task by GUID (Tasks V2). Returns empty body on success.
* **Disconnect Member** `disconnectMember`: Disconnect a member (set status OFFLINE) by member ID.
* **Drop Data Index** `dropIndex`: Drop (remove) an index from a Wix Data collection. dataCollectionId and indexName are query params.
* **Estimate Cart Totals** `estimateCartTotals`: Estimate totals for a cart (incl. shipping/tax). POST /ecom/v1/carts/{id}/estimate-totals.
* **Estimate Current Cart Totals** `estimateCurrentCartTotals`: Estimate totals for the current cart. POST /ecom/v1/carts/current/estimate-totals.
* **Find Or Create Extended Field** `createExtendedField`: Retrieve a custom contact field by display name, or create it (Extended Fields V4). dataType is one of TEXT, NUMBER, DATE, URL. Returns field.key and newField flag.
* **Find Or Create Label** `findOrCreateLabel`: Retrieve a contact label by display name, or create it if missing (Labels V4). Returns label.key (use in Label Contact) and newLabel flag.
* **Generate File Download URL** `generateFileDownloadUrl`: Generate a temporary download URL for a single media file (supports private).
* **Generate File Resumable Upload URL** `generateFileResumableUploadUrl`: Generate a resumable (TUS) upload URL for large media files. mimeType required.
* **Generate File Upload URL** `generateUploadUrl`: Generate a signed upload URL for uploading a file to the Media Manager. POST /site-media/v1/files/generate-upload-url with { mimeType, fileName? }.
* **Generate Files Download URL (ZIP)** `generateFilesDownloadUrl`: Generate a permanent ZIP download URL for multiple media files.
* **Generate Folder Download URL** `generateFolderDownloadUrl`: Generates a temporary URL for downloading an entire media folder as a ZIP archive.
* **Generate Video Streaming URL** `generateVideoStreamingUrl`: Generate an HLS/DASH streaming URL for a video file.
* **Get Account** `getAccount`: Retrieves a Wix account by its account ID. This is an account-level call and is not scoped to a single site.
* **Get Attendance** `getAttendance`: Get an attendance record by ID (Attendance v2).
* **Get Availability Time Slot** `getAvailabilityTimeSlot`: Get a single availability time slot for a service (Time Slots V2).
* **Get Badge** `getBadge`: Get a member badge by ID (Badges v4).
* **Get Booking Form** `getBookingForm`: Get a booking form schema by form ID (Wix Forms, namespace wix.bookings.v2.bookings).
* **Get Booking Policy** `getBookingPolicy`: Get a booking policy by ID (Booking Policies v1).
* **Get Brand (V3)** `getBrand`: Get a Wix Stores brand by ID.
* **Get Calendar Event** `getEvent`: Get a calendar event by ID (Calendar V3).
* **Get Cart** `getCart`: Retrieve a cart by ID. GET /ecom/v1/carts/{cartId}.
* **Get Category** `getCategory`: Get a single Wix Stores category by id.
* **Get Category By Slug** `getCategoryBySlug`: Get a Wix Stores category by slug. treeReference passed as query params.
* **Get Checkout** `getCheckout`: Retrieve a checkout by ID. GET /ecom/v1/checkouts/{checkoutId}.
* **Get Checkout By Cart ID** `getCheckoutByCartId`: Retrieve a checkout by its source cart id. GET /ecom/v1/checkouts/by-cart-id/{id}.
* **Get Checkout URL** `getCheckoutUrl`: Get the hosted checkout page URL. GET /ecom/v1/checkouts/{id}/checkout-url.
* **Get Contact** `getContact`: Retrieve a single contact by GUID (Contacts V4). Returns the full contact including revision (needed for updates).
* **Get Coupon** `getCoupon`: Get a coupon by id. GET /stores/v2/coupons/{id}.
* **Get Current Cart** `getCurrentCart`: Get the current visitor/member cart. GET /ecom/v1/carts/current (requires visitor/member context).
* **Get Current Member** `getCurrentMember`: Get the currently logged-in member. Requires member identity (not site/app token).
* **Get Customization (V3)** `getCustomization`: Get a product customization (option/modifier) by ID.
* **Get Data Collection** `getCollection`: Get a single Wix Data (CMS) collection by its data collection ID.
* **Get Data Item** `getItem`: Retrieve a single Wix Data item by ID. Uses POST /items/get with { dataItemId, dataCollectionId }.
* **Get Discount Rule** `getDiscountRule`: Get a discount rule by id. GET /ecom/v1/discount-rules/{discountRuleId}.
* **Get Draft Order** `getDraftOrder`: Retrieve a draft order by ID. GET /ecom/v1/draft-orders/{draftOrderId}.
* **Get Extended Field** `getExtendedField`: Retrieve a single extended field by its key (Extended Fields V4), e.g. custom.my-field.
* **Get Gift Card** `getGiftCard`: Get a gift card by its code. POST /ecom/v1/gift-cards/{code} with body {code,appId?,pin?}.
* **Get Info Section (V3)** `getInfoSection`: Get a Wix Stores info section by ID.
* **Get Inventory Item (V3)** `getInventoryItem`: Get a single Wix Stores inventory item by id (Catalog V3).
* **Get Label** `getLabel`: Retrieve a single contact label by its key (Labels V4), e.g. custom.my-label.
* **Get Location** `getLocation`: Get a business location by ID. GET /locations/v1/locations/{id}.
* **Get Media File** `getFile`: Get a media file descriptor by file ID. GET /site-media/v1/files/get-file-by-id?fileId=.
* **Get Media File Descriptors (Bulk)** `getFileDescriptors`: Get multiple media file descriptors by file IDs in one call.
* **Get Media Folder** `getFolder`: Get a media folder by ID. GET /site-media/v1/folders/get-folder-by-id?folderId=.
* **Get Member** `getMember`: Get a site member by ID.
* **Get Member About** `getMemberAbout`: Get a member's About section by About ID (Members About v2).
* **Get Multi-Service Availability Time Slot** `getMultiServiceTimeSlot`: Get a single multi-service availability time slot (Time Slots V2).
* **Get My Member About** `getMyMemberAbout`: Get the current member's About section (Members About v2). Needs member identity context.
* **Get Note** `getNote`: Retrieves a note by ID. GET /crm/notes/v2/notes/{noteId}.
* **Get Or Create Brand (V3)** `getOrCreateBrand`: Get a brand by name or create it if missing.
* **Get Or Create Info Section (V3)** `getOrCreateInfoSection`: Get an info section by uniqueName or create it (provide title to create).
* **Get Or Create Ribbon (V3)** `getOrCreateRibbon`: Get a ribbon by name or create it if missing.
* **Get Order** `getOrder`: Retrieve a single eCommerce order by ID. GET /ecom/v1/orders/{orderId}.
* **Get Order Draftability** `getOrderDraftability`: Check whether an existing order can be edited via a draft order. GET /ecom/v1/draft-orders/{orderId}/draftability.
* **Get Product (V3)** `getProduct`: Get a single Wix Stores product by id (Catalog V3). Returns full product details including revision and variants.
* **Get Product By Slug (V3)** `getProductBySlug`: Get a Wix Stores product by its slug (Catalog V3).
* **Get Resource** `getResource`: Get a bookable resource by ID (Resources v2).
* **Get Ribbon (V3)** `getRibbon`: Get a Wix Stores ribbon by ID.
* **Get Roles Info** `getRolesInfo`: Get predefined and custom roles for the account (account-level, requires account API key).
* **Get Schedule** `getSchedule`: Get a calendar schedule by ID (Calendar V3).
* **Get Service** `getService`: Get a Bookings service by ID (Services V2).
* **Get Service Options And Variants** `getServiceOptionsAndVariants`: Get a service options-and-variants object by ID (v1).
* **Get Service Options And Variants By Service** `getServiceOptionsAndVariantsByServiceId`: Get options-and-variants for a given service ID (v1).
* **Get Site Properties** `getSiteProperties`: Get the site's properties (locale, business info, etc.). Site-level.
* **Get Staff Member** `getStaffMember`: Get a staff member by ID (Staff Members v1).
* **Get Task** `getTask`: Retrieve a CRM task by GUID (Tasks V2). Returns the task including revision (needed for updates).
* **Import Media File** `importFile`: Import a file into the Media Manager from a public external URL. POST /site-media/v1/files/import with { url, displayName?, mimeType? }.
* **Insert Data Item** `insertItem`: Insert (create-only) a single item into a Wix Data collection. Body: { dataCollectionId, dataItem: { data: {...} } }.
* **Join Community** `joinCommunity`: Make the current member's profile public (join community). Needs member identity context.
* **Label Contact** `labelContact`: Add one or more existing label keys to a contact (Contacts V4). Label keys must already exist (use Find Or Create Label). Returns the updated contact.
* **Leave Community** `leaveCommunity`: Make the current member's profile private (leave community). Needs member identity context.
* **List Availability Time Slots** `listTimeSlots`: List appointment availability time slots. Required: serviceId, fromLocalDate, toLocalDate, timeZone (Time Slots V2).
* **List Booking Fees** `listBookingFees`: List cancellation/no-show fees for up to 5 bookings (Booking Fees v1).
* **List Calendar Events** `listEvents`: List calendar events by event IDs (Calendar V3).
* **List Categories For Item** `listCategoriesForItem`: Reverse lookup: which categories contain ONE product. item:{catalogItemId,appId}.
* **List Categories For Items** `listCategoriesForItems`: Reverse lookup for MANY products (max 100). items:[{catalogItemId,appId}].
* **List Child Accounts** `listChildAccounts`: List child accounts under the Wix account (account-level, requires account API key).
* **List Contact Facets** `listContactFacets`: Lists facets (labels and subscription statuses) from the site's contact list. GET /contacts/v4/contacts/facets.
* **List Contacts** `listContacts`: Retrieves a list of up to 1,000 contacts per request. GET /contacts/v4/contacts with optional paging, sort, fields, fieldsets.
* **List Data Collections** `listCollections`: List all Wix Data (CMS) collections on the site.
* **List Data Indexes** `listIndexes`: List indexes for a Wix Data collection. dataCollectionId is a query param.
* **List Deleted Media Files** `listDeletedFiles`: List files in the Media Manager trash bin.
* **List Deleted Media Folders** `listDeletedFolders`: List folders in the Media Manager trash bin.
* **List Draft Orders** `listDraftOrders`: List/query draft orders. POST /ecom/v1/draft-orders/query with body {query:{cursorPaging:{limit}}}. Returns draftOrders[].
* **List Extended Fields** `listExtendedFields`: List custom and system contact extended fields (Extended Fields V4). Returns fields[] each with key, displayName, dataType.
* **List Fulfillments By Order IDs** `listFulfillmentsByIds`: List fulfillments for multiple orders. POST /ecom/v1/fulfillments/list-by-ids with body {orderIds:[]}.
* **List Fulfillments For Order** `listFulfillments`: List fulfillments for a single order. GET /ecom/v1/fulfillments/orders/{orderId}.
* **List Invoices For Orders** `listInvoicesForOrders`: List invoices for multiple orders. POST /ecom/v1/invoices/list-by-ids with body {orderIds:[]}.
* **List Items In Category** `listItemsInCategory`: List products in a category (max 100). Optional includeItemsFromSubcategories, useCategoryArrangement, cursorPaging.
* **List Labels** `listLabels`: List contact labels (Labels V4). Returns labels[] each with key and displayName.
* **List Locations** `listLocations`: List business locations. GET /locations/v1/locations.
* **List Media Files** `listFiles`: List files in the Media Manager. Optional parentFolderId, mediaTypes, paging.
* **List Media Folders** `listFolders`: List folders in the Media Manager. GET /site-media/v1/folders. Optional parentFolderId.
* **List Members** `listMembers`: List site members. Supports fieldsets, paging, sorting query params.
* **List Multi Service Time Slots** `multiServiceTimeSlots`: List availability time slots across multiple services in a sequence (Time Slots V2).
* **List Transactions By Order IDs** `listTransactionsByIds`: List transactions for multiple orders. POST /ecom/v1/payments/list-by-ids with body {orderIds:[]}.
* **List Transactions For Order** `listTransactionsForOrder`: List payment and refund transactions for a single order. GET /ecom/v1/payments/orders/{orderId}.
* **Mark Booking As Pending** `markBookingAsPending`: Mark a booking as pending (Bookings v2). Requires bookingId and revision.
* **Mark Checkout As Completed** `markCheckoutAsCompleted`: Mark a checkout as completed. POST /ecom/v1/checkouts/{id}/mark-as-completed.
* **Merge Contacts** `mergeContacts`: Merges up to 5 source contacts into a target contact. Irreversible. POST /contacts/v4/contacts/{targetContactId}/merge. Requires targetContactRevision.
* **Move Badge** `moveBadge`: Reorder a badge in the display list (Badges v4).
* **Move Category** `moveCategory`: Reposition a category. position FIRST|LAST|AFTER (AFTER needs moveAfterCategoryId).
* **Move Task After** `moveTaskAfter`: Repositions a CRM task to be placed after another task. Omit beforeTaskId to move first. POST /crm/tasks/v2/tasks/{taskId}/move-after.
* **Mute Member** `muteMember`: Mute a member (cannot post in forum/blog).
* **Preview Merge Contacts** `previewMergeContacts`: Dry-run preview of merging source contacts into a target contact; no data changed. POST /contacts/v4/contacts/{targetContactId}/preview-merge.
* **Preview Service Price** `previewServicePrice`: Preview/estimate price for a service booking before it exists (Pricing v2).
* **Query Attendance** `queryAttendance`: Query attendance records (Attendance v2).
* **Query Availability Calendar** `queryAvailabilityCalendar`: DEPRECATED - DO NOT USE. The Wix Availability Calendar API is retired and its REST endpoint (POST /_api/availability-calendar/v1/availability/query) is gone - Wix answers 404 with an empty body for every input. Wix documents Time Slots V2 as the replacement, which this connector already exposes as List Time Slots and Get Availability Time Slot; use those instead. This action was deliberately NOT repointed at Time Slots V2 because that would duplicate List Time Slots and silently change this action's contract for existing callers. Ref: https://dev.wix.com/docs/api-reference/business-solutions/bookings/calendar-integration
* **Query Badge Assignments** `queryBadgeAssignments`: Query badge assignments. Filter by badgeId (members-per-badge) or memberId (badges-per-member).
* **Query Badges** `queryBadges`: Query member badges with filter/sort/cursorPaging (Badges v4).
* **Query Booking Forms** `queryBookingForms`: Query booking form schemas (Wix Forms). Must filter by namespace wix.bookings.v2.bookings.
* **Query Booking Policies** `queryBookingPolicies`: Query booking policies (Booking Policies v1).
* **Query Brands (V3)** `queryBrands`: Query Wix Stores brands (cursorPaging max 300).
* **Query Calendar Events** `queryEvents`: Query calendar events with filter/sort/cursorPaging (Calendar V3).
* **Query Categories** `queryCategories`: Query Wix Stores categories. POST body requires treeReference.appNamespace='@wix/stores' alongside query{cursorPaging{limit}}.
* **Query Contact Facets** `queryContactFacets`: Retrieves contact-list facets by filter (labels, subscription statuses). POST /contacts/v4/contacts/facets/query.
* **Query Contacts** `queryContacts`: Query/list contacts with optional paging, filtering, and sorting (Contacts V4). Pass an empty query object to list all. Returns contacts[] each with id and revision.
* **Query Coupons** `queryCoupons`: Query coupons with paging/filter/sort. POST /stores/v2/coupons/query with body {query}.
* **Query Customizations (V3)** `queryCustomizations`: Query product customizations (filter by customizationType/renderType/name).
* **Query Data Items** `queryItems`: Query Wix Data items with filter/sort/paging. POST /items/query with { dataCollectionId, query }.
* **Query Discount Rules** `queryDiscountRules`: Query discount rules. POST /ecom/v1/discount-rules/query with body {query}.
* **Query Distinct Values** `queryDistinctValues`: Return distinct values of a field in a Wix Data collection.
* **Query Extended Bookings** `queryExtendedBookings`: Query bookings with paging/filter/sort (Bookings Reader V2).
* **Query Info Sections (V3)** `queryInfoSections`: Query Wix Stores info sections (filter/sort/cursorPaging optional).
* **Query Inventory Items (V3)** `queryInventoryItems`: Query Wix Stores inventory items (Catalog V3). POST body: {query:{cursorPaging:{limit:10}}}. Supports filter/sort.
* **Query Locations** `queryLocations`: Query business locations with filter/sort/paging. POST /locations/v1/locations/query with { query }.
* **Query Media File Descriptors** `queryFileDescriptors`: Query media files with filter/sort/cursor paging.
* **Query Member Abouts** `queryMemberAbouts`: Query member About sections with filter/sort/cursorPaging (Members About v2).
* **Query Members** `queryMembers`: Query site members with paging/filter/sort.
* **Query Notes** `queryNotes`: Retrieves up to 1,000 notes for a contact with filtering/sorting/cursor paging. POST /crm/notes/v2/notes/query. contactId required on first request.
* **Query Products (V3)** `queryProducts`: Query Wix Stores products (Catalog V3). POST body: {query:{cursorPaging:{limit:10}}}. Supports filter/sort.
* **Query Resources** `queryResources`: Query bookable resources (Resources v2).
* **Query Ribbons (V3)** `queryRibbons`: Query Wix Stores ribbons (filter/sort/cursorPaging optional).
* **Query Schedules** `querySchedules`: Query calendar schedules (Calendar V3).
* **Query Service Options And Variants** `queryServiceOptionsAndVariants`: Query service options-and-variants objects (v1).
* **Query Services** `queryServices`: Query Bookings services (Services V2).
* **Query Sites** `querySites`: List sites in the Wix account (account-level). Returns each site's id (use as siteId for site-level actions), displayName, published, viewUrl.
* **Query Staff Members** `queryStaffMembers`: Query staff members (Staff Members v1).
* **Query Tasks** `queryTasks`: Query/list CRM tasks with optional filtering, sorting, paging (Tasks V2). Pass an empty query object to list all. Returns tasks[] each with id and revision.
* **Query Variants (V3)** `queryVariants`: Query product variants (read-only Variants V3). Filter on productData.productId/variantId/id.
* **Redeem Gift Card** `redeemGiftCard`: Redeem an amount from a gift card. POST /ecom/v1/gift-cards/redeem with body {code,amount,appId}.
* **Remove Cart Coupon** `removeCartCoupon`: Remove the coupon applied to a cart. POST /ecom/v1/carts/{id}/remove-coupon.
* **Remove Checkout Coupon** `removeCheckoutCoupon`: Remove the coupon applied to a checkout. POST /ecom/v1/checkouts/{id}/remove-coupon.
* **Remove Checkout Gift Card** `removeCheckoutGiftCard`: Remove the gift card applied to a checkout. POST /ecom/v1/checkouts/{id}/remove-gift-card.
* **Remove Checkout Line Items** `removeCheckoutLineItems`: Remove line items from a checkout. POST /ecom/v1/checkouts/{id}/remove-line-items with body {lineItemIds}.
* **Remove Current Cart Coupon** `removeCurrentCartCoupon`: Remove the coupon applied to the current cart. POST /ecom/v1/carts/current/remove-coupon.
* **Remove Current Cart Line Items** `removeCurrentCartLineItems`: Remove line items from the current cart. POST /ecom/v1/carts/current/remove-line-items with body {lineItemIds}.
* **Remove Customization Choices (V3)** `removeCustomizationChoices`: Remove choices from a customization by choiceIds (1-100).
* **Remove Data Item** `removeItem`: Remove a Wix Data item. POST /items/remove with { dataCollectionId, dataItemId }.
* **Remove Item From Categories** `removeItemFromCategories`: Remove ONE product from MANY categories. item:{catalogItemId,appId}, categoryIds:[...].
* **Remove Line Items From Cart** `removeLineItems`: Remove line items from a cart. POST /ecom/v1/carts/{cartId}/remove-line-items with body {lineItemIds:[...]}.
* **Remove Location Type** `removeLocationType`: Remove a location type from a location. id in path.
* **Remove Override Checkout URL** `removeOverrideCheckoutUrl`: Remove a custom override checkout URL. POST /ecom/v1/checkouts/{id}/remove-override-checkout-url.
* **Remove Products From Category** `removeProductsFromCategory`: Remove many products from ONE category (max 100). Provide items: [{catalogItemId, appId}].
* **Reschedule Booking** `rescheduleBooking`: Reschedule a booking to a new slot. Requires current revision (Bookings Writer V2).
* **Save Data Item (Upsert)** `saveItem`: Insert or update (upsert) a Wix Data item. POST /items/save with { dataCollectionId, dataItem }.
* **Search Categories** `searchCategories`: Search Wix Stores categories (filter/sort/cursor paging). Requires treeReference @wix/stores.
* **Search Inventory Items (V3)** `searchInventoryItems`: Search inventory items with filter/sort/cursor paging (Catalog V3).
* **Search Media Files** `searchFiles`: Search media files with filtering/sorting/cursor paging. POST /site-media/v1/files/search. All params optional.
* **Search Orders** `searchOrders`: Search eCommerce orders. POST /ecom/v1/orders/search with body {search:{cursorPaging,filter,sort}}. Returns orders[] and metadata.
* **Search Products (V3)** `searchProducts`: Search Wix Stores products by name/brand (Catalog V3). POST body supports search.cursorPaging.
* **Search Services** `searchServices`: Search Bookings services (Services V2).
* **Search Team Members** `searchTeam`: Search account team members and invites (account-level, requires account API key).
* **Search Variants (V3)** `searchVariants`: Free-text search product variants (read-only Variants V3).
* **Set Arranged Items In Category** `setArrangedItems`: Set manual product display order in a category (max 100). Provide arrangedItems array.
* **Set Attendance** `setAttendance`: Mark attendance for a booking (Attendance v2). status NOT_SET/ATTENDED/NOT_ATTENDED.
* **Set Booking Submission ID** `setBookingSubmissionId`: Attach a form submission ID to a booking (Bookings v2).
* **Set Customization Choices (V3)** `setCustomizationChoices`: Replace all choices of a customization (1-200).
* **Set Default Booking Policy** `setDefaultBookingPolicy`: Set a booking policy as the site default (Booking Policies v1).
* **Set Default Location** `setDefaultLocation`: Set a location as the site default. POST /locations/v1/locations/{id}/set-default.
* **Set Draft Additional Fees** `setDraftAdditionalFees`: Apply or unapply additional fees on a draft order. POST /ecom/v1/draft-orders/{draftOrderId}/set-additional-fees.
* **Set Draft Billing Info** `setDraftBillingInfo`: Set billing info on a draft order. PUT /ecom/v1/draft-orders/set-billing-info with body {draftOrderId,billingInfo}.
* **Set Draft Business Location** `setDraftBusinessLocation`: Set business location on a draft order. PUT /ecom/v1/draft-orders/set-business-location with body {draftOrderId,businessLocation:{id}}.
* **Set Draft Buyer Info** `setDraftBuyerInfo`: Set buyer info on a draft order. PUT /ecom/v1/draft-orders/set-buyer-info with body {draftOrderId,buyerInfo}.
* **Set Draft Discounts** `setDraftDiscounts`: Apply or unapply discounts on a draft order. POST /ecom/v1/draft-orders/{draftOrderId}/set-discounts.
* **Set Draft Recipient Info** `setDraftRecipientInfo`: Set recipient info on a draft order. PUT /ecom/v1/draft-orders/set-recipient-info with body {draftOrderId,recipientInfo}.
* **Set Draft Shipping Info** `setDraftShippingInfo`: Set shipping info on a draft order. PUT /ecom/v1/draft-orders/set-shipping-info with body {draftOrderId,shippingInfo}.
* **Set Draft Tax Exemption** `setDraftTaxExemption`: Set tax exemption on a draft order. PUT /ecom/v1/draft-orders/set-tax-exemption with body {draftOrderId,taxExempt}.
* **Truncate Data Items** `truncateItems`: Remove ALL items from a Wix Data collection.
* **Unassign Badge** `unassignBadge`: Remove a badge assignment by assignment ID (Badges v4).
* **Unlabel Contact** `unlabelContact`: Remove one or more label keys from a contact (Contacts V4, DELETE). Returns the updated contact.
* **Unmute Member** `unmuteMember`: Unmute a member.
* **Update Badge** `updateBadge`: Update a member badge (Badges v4). Requires id and revision.
* **Update Booking Form** `updateBookingForm`: Update a booking form schema (Wix Forms). Requires form.id and revision.
* **Update Booking Policy** `updateBookingPolicy`: Update a booking policy (Booking Policies v1). Requires id and revision.
* **Update Brand (V3)** `updateBrand`: Update a Wix Stores brand. Required: brandId, revision, name.
* **Update Business Contact** `updateBusinessContact`: Update site business contact (email/phone/fax/address). fields.paths controls which fields update.
* **Update Business Profile** `updateBusinessProfile`: Update site business profile (display name, business name, logo, description). fields.paths controls which update.
* **Update Business Schedule** `updateBusinessSchedule`: Overwrite the site business schedule (hours of operation + special hours). Full overwrite, no field mask.
* **Update Calendar Event** `updateEvent`: Update a calendar event (Calendar V3). Requires event.id and revision.
* **Update Cart** `updateCart`: Update a cart (line item quantities, buyer info). PATCH /ecom/v1/carts/{cartId} with body {cartInfo:{...}}.
* **Update Cart Line Items Quantity** `updateCartLineItemsQuantity`: Update line item quantities in a cart. POST /ecom/v1/carts/{id}/update-line-items-quantity with body {lineItems:[{id,quantity}]} (lineItems[].id = line item GUID).
* **Update Category** `updateCategory`: Update a Wix Stores category (PATCH). Requires category.revision (GET first).
* **Update Checkout** `updateCheckout`: Update a checkout (billing/contact info). PATCH /ecom/v1/checkouts/{checkoutId} with body {checkout:{...}}.
* **Update Checkout Line Items Quantity** `updateCheckoutLineItemsQuantity`: Update line item quantities on a checkout. POST /ecom/v1/checkouts/{id}/update-line-items-quantity with body {lineItems:[{id,quantity}]}.
* **Update Consent Policy** `updateConsentPolicy`: Update site consent/cookie policy. Sub-path is /policy. Full overwrite, no field mask.
* **Update Contact** `updateContact`: Update a contact by GUID (Contacts V4, PATCH). The current revision (from Get Contact) MUST be supplied; it increments on each update. Only the fields in info are changed.
* **Update Coupon** `updateCoupon`: Update a coupon. PATCH /stores/v2/coupons/{id} with body {specification} and required query param fieldMask (comma-separated field paths passed via input.fields).
* **Update Current Cart** `updateCurrentCart`: Update the current cart (e.g. apply couponCode, change line items). PATCH /ecom/v1/carts/current.
* **Update Current Cart Line Items Quantity** `updateCurrentCartLineItemsQuantity`: Update line item quantities in the current cart. POST /ecom/v1/carts/current/update-line-items-quantity with body {lineItems:[{id,quantity}]} (id = line item GUID).
* **Update Customization (V3)** `updateCustomization`: Update a product customization. Required: customizationId, and customization body with id+revision.
* **Update Data Collection** `updateCollection`: Update an existing Wix Data (CMS) collection. Pass full collection object including id, fields and permissions.
* **Update Data Item** `updateItem`: Replace a Wix Data item's payload. PUT /items/{id} with { dataCollectionId, dataItem: { id, data } }.
* **Update Discount Rule** `updateDiscountRule`: Update a discount rule (revision required). PATCH /ecom/v1/discount-rules/{discountRuleId} with body {discountRule:{id,revision,...}}.
* **Update Draft Order Extended Fields** `updateDraftExtendedFields`: Update extended (custom) fields on a draft order. POST /ecom/v1/draft-orders/{id}/update-extended-fields with body {namespace,namespaceData}.
* **Update Draft Order Line Items** `updateDraftLineItems`: Change quantities (qty 0 removes) of draft order line items. POST /ecom/v1/draft-orders/{draftOrderId}/line-items.
* **Update Extended Field** `updateExtendedField`: Rename a custom extended field by key (Extended Fields V4, PATCH). Body needs only the new displayName. Only USER_DEFINED fields can be renamed.
* **Update Fulfillment** `updateFulfillment`: Update a fulfillment on an order. PATCH /ecom/v1/fulfillments/{fulfillmentId}/orders/{orderId} with body {fulfillment}.
* **Update Info Section (V3)** `updateInfoSection`: Update a Wix Stores info section. Required: infoSectionId, revision, title.
* **Update Inventory Item (V3)** `updateInventoryItem`: Update a Wix Stores inventory item (Catalog V3, PATCH). Requires inventoryItem.id and current inventoryItem.revision (GET first). reason defaults to MANUAL.
* **Update Label** `updateLabel`: Rename a contact label by key (Labels V4, PATCH). Body needs only the new displayName; the key is in the path and cannot change.
* **Update Location** `updateLocation`: Overwrite a business location. PUT /locations/v1/locations/{id} with full location object including id, name, address, timeZone and current revision.
* **Update Media File Descriptor** `updateFileDescriptor`: Update a media file (rename, relabel, or move via parentFolderId). file.id required.
* **Update Media Folder** `updateFolder`: Update a media folder (rename or move via parentFolderId). folderId in path.
* **Update Member** `updateMember`: Update a site member. Body member.id must match path id. No revision needed.
* **Update Member About** `updateMemberAbout`: Update a member's About section (Members About v2). Requires id and revision.
* **Update Member Slug** `updateMemberSlug`: Update a specific member's profile slug by member ID.
* **Update My Slug** `updateMySlug`: Update the current member's profile slug. Needs member identity context.
* **Update Note** `updateNote`: Updates a note's text/type. PATCH /crm/notes/v2/notes/{noteId}. Body wrapped in {note:{...}} and requires current revision.
* **Update Number Of Participants** `updateNumberOfParticipants`: Update participant count on a booking (Bookings v2). Requires bookingId, revision, totalParticipants.
* **Update Order** `updateOrder`: Update limited order fields. PATCH /ecom/v1/orders/{orderId} with body {order:{...}}. Only buyerInfo.email and buyerLanguage are whitelisted for update by Wix.
* **Update Payment Transaction Status** `updatePaymentTransactionStatus`: Update a payment transaction status. POST /ecom/v1/payments/{paymentId}/orders/{orderId}/update-payment-transaction-status with body {status}.
* **Update Product (V3)** `updateProduct`: Updates a Wix Stores V3 product. NOTE: this action can only change the product name; it cannot set storefront visibility - see the connector's known-issues. Wix uses optimistic concurrency, so pass the revision from a preceding getProduct.
* **Update Resource** `updateResource`: Update a bookable resource (Resources v2). Requires resource.id and revision.
* **Update Ribbon (V3)** `updateRibbon`: Update a Wix Stores ribbon. Required: ribbonId, revision, name.
* **Update Schedule** `updateSchedule`: Update a calendar schedule (Calendar V3). Requires schedule.id and revision.
* **Update Service** `updateService`: Update a Bookings service. Requires current revision (Services V2).
* **Update Service Options And Variants** `updateServiceOptionsAndVariants`: Update a service options-and-variants object (v1). Requires id and revision.
* **Update Staff Member** `updateStaffMember`: Update a staff member (Staff Members v1). Requires id and revision.
* **Update Task** `updateTask`: Update a CRM task by GUID (Tasks V2, PATCH). The task body must include id and the current revision (string) from Get Task. Returns the updated task.
* **Void Gift Card Transaction** `voidGiftCardTransaction`: Void a gift card transaction. POST /ecom/v1/gift-cards/void with body {transactionId,appId}.

</details>
