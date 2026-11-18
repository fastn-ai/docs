---
description: "Starshipit is a multi-carrier shipping and fulfilment platform for ecommerce retailers."
hidden: true
---

# Starshipit

<img src="../../.gitbook/assets/connectors/lg/starshipit.png" alt="Starshipit logo">

Starshipit is a multi-carrier shipping and fulfilment platform for ecommerce retailers. This connector wraps the Starshipit REST API: orders and order search, label printing and manifesting, shipments, tracking, live rates and delivery services, the address book, manifests and the product catalogue.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [starshipit.com](https://starshipit.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `starshipit` |

## Use it

Add Starshipit from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.starshipit.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Address Book Entry | `addressBookAdd` | Save a new contact in the account's address book. |
| Add Product | `productsAdd` | Add a product to the Starshipit catalogue so its weight, dimensions and customs details are applied automatically to orders. |
| Assign Orders | `ordersAssign` | Move unshipped orders from one Starshipit account to another, identified by the source and destination API keys. |
| Batch Update Orders | `ordersBatchUpdate` | Apply the same carrier and product code to a list of orders in one request. |
| Clone Shipment | `shipmentClone` | Copy a printed or shipped order into a new unshipped order, optionally as a return shipment. |
| Create Order | `ordersCreate` | Create a single order in Starshipit ready for a label to be printed against it. |
| Create Tracking Only Orders | `ordersCreateTrackingOnly` | Register shipments that were labelled outside Starshipit so their carrier tracking still flows through Starshipit. |
| Delete Address Book Entries | `addressBookDelete` | Remove one or more saved contacts from the account's address book. |
| Delete Orders | `ordersDelete` | Delete unshipped orders from Starshipit. The Starshipit reference documents this as DELETE with a single order_id; the live API is POST with an order_ids array, and the documented form returns the router 404. |
| Delete Products | `productsDelete` | Remove products from the Starshipit catalogue, either the listed ones or, with All Products set, the whole catalogue. |
| Get Account Settings | `settingsGet` | Return the account's Starshipit settings: plan and account identity, the default sender address, packaging presets, default shipping options, the carriers that are configured and the carriers available for pickup, plan permissions and feature flags. This route is not in the published Starshipit reference but is live, and its pickup_carriers list is the source of the numeric carrier_id that Batch Update Orders expects. |
| Get Delivery Services | `deliveryServicesGet` | Return the delivery services available for a shipment, optionally with live pricing, for a given sender, destination and parcel set. |
| Get Manifest Files | `manifestFilesGet` | List the documents attached to a manifest, such as the carrier manifest PDF. |
| Get Orders | `ordersGet` | Retrieve one order by its Starshipit order identifier or your own order number. With neither supplied, returns the orders matching the remaining criteria. |
| Get Orders Summary | `ordersSummary` | Return a summary listing of orders in a given status, with paging and optional filtering. |
| Get Rates | `ratesGet` | Quote live shipping rates across the account's carriers for a given sender, destination and set of parcels. |
| Get Rates (Deprecated) | `ratesGetLegacy` | Quote a shipping rate using the older query-string endpoint. Starshipit marks this deprecated; use Get Rates for new work. |
| Get Suggested Merges | `ordersMergeable` | List groups of unshipped orders going to the same person at the same address, which Starshipit suggests merging. |
| Import Orders | `ordersImport` | Create several orders in one request. Starshipit reports per-order results, so the response must be inspected for individual failures. |
| List Address Book Entries | `addressBookList` | List the saved contacts in the account's address book, one page at a time. |
| List Delivered Orders | `ordersListDelivered` | List delivered orders carrying a given order reference. |
| List Manifests | `manifestsList` | List the manifests raised on the account, newest first. |
| List Products | `productsList` | List the products in the Starshipit catalogue, with search, paging and sorting. |
| List Scheduled Reports | `reportsList` | List the scheduled reports configured on the account, a page at a time. This route is not in the published Starshipit reference but is live and read-only; GET on a single report returns the router 404. |
| List Shipments | `ordersListShipments` | List shipments that were recently printed or that are still waiting to be manifested. |
| List Shipped Orders | `ordersListShipped` | List orders that have had a label printed and have been dispatched. Defaults to orders updated in the last 24 hours. |
| List Shipping Rules | `rulesList` | Return the shipping rules configured on the account, together with the revision hash Starshipit uses for optimistic concurrency. Rules decide which carrier and service an order is assigned automatically. This route is not in the published Starshipit reference but is live and read-only from the API; rules are edited in the Starshipit app. |
| List Tags | `tagsList` | List the order tags defined on the account, a page at a time. Tags are what Starshipit uses to group and filter orders in the app. This route is not in the published Starshipit reference but is live and read-only: POST, PUT and DELETE on it, and GET on a single tag, all return the router 404. |
| List Unshipped Orders | `ordersListUnshipped` | List orders that have been imported into Starshipit but do not yet have a label printed. |
| List Users | `usersList` | List the users that have access to the Starshipit account. |
| Manifest By Carrier | `manifestsByCarrier` | Manifest every printed but unmanifested shipment for one carrier in a single request, and report how many records were manifested. This endpoint returns a count rather than a manifest document; use List Manifests and Get Manifest Files to retrieve the paperwork. Manifesting cannot be undone. |
| Manifest Orders | `ordersManifest` | Finalise printed orders and send their details to the carrier for billing. Manifesting cannot be undone. |
| Manifest Shipments By Number | `manifestsFindShipments` | Manifest printed shipments identified by their tracking numbers, or by their order numbers when Use Order Numbers is set, and return the carrier manifest document. Despite the Starshipit reference describing this as a lookup that returns shipment ids, the live endpoint performs the manifest and answers with the PDF. Manifesting cannot be undone. |
| Merge Orders | `ordersMerge` | Merge one or more child orders into a parent order so they ship together on a single label. |
| Print Label | `shipmentPrintLabel` | Print a shipping label for one order. The label comes back as a base64 string that decodes to a PDF, and printing consumes carrier quota. |
| Print Labels | `shipmentsPrintLabels` | Print shipping labels for several orders at once. Every order must already have a carrier set, because this endpoint takes no carrier override; without one Starshipit answers success false with "Could not find the Label Type for courier: -1". Printing consumes carrier quota. |
| Print Packing Slips | `shipmentsPrintPackingSlips` | Generate packing slips for a list of orders. The slips come back as a base64 string that decodes to a PDF. |
| Replace Shipment | `shipmentReplace` | Redo a printed or shipped order, voiding the existing shipment and producing a fresh one. |
| Search Orders | `ordersSearch` | Search printed orders by order number, tracking number or recipient name. |
| Track Shipment | `trackingGet` | Return carrier tracking events for a shipment, looked up by tracking number or by order number. |
| Update Address Book Entry | `addressBookUpdate` | Update a saved contact in the account's address book. |
| Update Order | `ordersUpdate` | Update a single unshipped order. Starshipit replaces the order with the body supplied, so send the whole order, not only the changed fields. |
| Update Orders | `ordersUpdateMany` | Update several unshipped orders in one request. Starshipit replaces each order with the body supplied, so send the whole order, not only the changed fields. |
| Update Product | `productsUpdate` | Update a product in the Starshipit catalogue. Starshipit replaces the stored record, so send the whole product. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Attempted Delivery | `AttemptedDelivery` | The carrier tried to deliver and could not. |
| Awaiting Collection | `AwaitingCollection` | The parcel is waiting to be collected from a depot or locker. |
| Cancelled | `Cancelled` | The shipment was cancelled. |
| Delivered | `Delivered` | The parcel has been delivered. |
| Dispatched | `Dispatched` | The carrier has collected or received the parcel. |
| Exception | `Exception` | The carrier reported a problem with the shipment. |
| In Transit | `InTransit` | The parcel is moving through the carrier network. |
| Label Printed | `Printed` | A shipping label has been generated for the order. |
| Out For Delivery | `OutForDelivery` | The parcel is on the vehicle for final delivery. |
| Pickup In Store | `PickupInStore` | The parcel is waiting for collection in store. |
