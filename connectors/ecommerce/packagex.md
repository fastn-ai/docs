---
description: "PackageX is a logistics operations platform providing package and mail tracking, mailroom management, shipping label generation, carrier rate shopping,…"
hidden: true
---

# PackageX

<img src="../../.gitbook/assets/connectors/packagex.png" alt="PackageX logo" width="64">

PackageX is a logistics operations platform providing package and mail tracking, mailroom management, shipping label generation, carrier rate shopping, deliveries, inventory, and warehouse operations via a unified REST API.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [packagex.io](https://packagex.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `packagex` |

## Use it

Add PackageX from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.packagex.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Address | `autocompleteAddress` | Returns up to five address completions for a partial address string, powered by Google Maps Places. Optionally restrict results to a specific country using a two-letter region code. |
| Create API Key | `createApiKey` | Creates a new PackageX API key scoped to the given resources, optionally with an expiration date. The full key value is returned only once, at creation time. |
| Create Contact | `createContact` | Creates a new contact with name, contact details, and address information for use as a sender or recipient on deliveries and shipments. |
| Create Group | `createGroup` | Creates a group used to organize contacts or locations, optionally scoped to a location and pre-populated with member contact ids. |
| Create Location | `createLocation` | Creates a new physical location for your organization from a name and address. Operating hours, notification settings, and a default layout are generated automatically. |
| Create Shipment | `createShipment` | Creates an outbound shipment with sender and recipient details and one or more parcels. Generates shipping rates and, depending on options, a shipping label. |
| Create User | `createUser` | Creates a new user in your organization with a name, email, and role. A role_id is required by the API. |
| Delete API Key | `deleteApiKey` | Permanently deletes a single API key by its id, immediately revoking its access. |
| Delete Contact | `deleteContact` | Permanently deletes a contact by its id. |
| Delete Group | `deleteGroup` | Permanently deletes a group by its id. |

<details>

<summary>See 25 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Location | `deleteLocation` | Permanently deletes a physical location by its id. |
| Delete User | `deleteUser` | Permanently removes a user from your organization by their id. |
| Geocode Address | `geocodeAddress` | Converts an address, or the id of an existing address or location, into geographical coordinates (latitude and longitude). |
| Get API Key | `getApiKey` | Retrieves a single API key by its id. |
| Get Contact | `getContact` | Retrieves a single contact by its id. |
| Get Delivery | `getDelivery` | Retrieves detailed information about a single delivery by its id, including tracking updates and addresses. |
| Get Group | `getGroup` | Retrieves a single group by its id. |
| Get Location | `getLocation` | Retrieves a single physical location by its id. |
| Get Organization | `getOrganization` | Retrieves comprehensive information about an organization, including configuration settings, carrier credentials, and tenant relationships. |
| Get Shipment | `getShipment` | Retrieves detailed information about a single outbound shipment by its id. |
| Get Tracker | `getTracker` | Retrieves detailed information about a specific tracker by its id, including its shipments, destination details, and tracking updates. |
| Get User | `getUser` | Retrieves a single user by its id. |
| List API Keys | `listApiKeys` | Retrieves the API keys associated with your organization, with an optional filter by key type. |
| List Contacts | `listContacts` | Retrieves the contacts belonging to your organization, with pagination. |
| List Deliveries | `listDeliveries` | Retrieves multiple deliveries with comprehensive filtering, sorting, and search capabilities. Returns an array of delivery records with a pagination object, even when no deliveries match. |
| List Groups | `listGroups` | Retrieves the groups belonging to your organization, with pagination. Groups are used to organize contacts, locations, and other resources. |
| List Locations | `listLocations` | Retrieves the physical locations belonging to your organization, with pagination. |
| List Shipments | `listShipments` | Retrieves outbound shipments belonging to your organization, with filtering, sorting, and pagination. |
| List Trackers | `listTrackers` | Retrieves the trackers belonging to your organization, with pagination. A tracker represents the end-to-end journey of a shipment, potentially spanning multiple hops. |
| List Users | `listUsers` | Retrieves the users belonging to your organization, with pagination. |
| Parse Address | `parseAddress` | Validates, normalizes, and standardizes a free-text or structured address into the PackageX address model, with optional USPS CASS validation for US addresses. |
| Update API Key | `updateApiKey` | Updates the name or scopes of an existing API key. |
| Update Contact | `updateContact` | Updates an existing contact's name, contact details, or address. |
| Update Group | `updateGroup` | Updates a group's name, or adds, removes, or replaces its member contact ids. |
| Update Location | `updateLocation` | Updates an existing location's attributes such as name, code, contact info, address, or provider instructions. |

</details>
