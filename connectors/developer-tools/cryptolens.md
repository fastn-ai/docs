---
description: "Cryptolens software licensing (Web API 3): license keys, products, customers, data objects, machine-code activations, messages, resellers, user auth and usage…"
---

# Cryptolens

Cryptolens software licensing (Web API 3): license keys, products, customers, data objects, machine-code activations, messages, resellers, user auth and usage analytics. Base https://app.cryptolens.io/api/. Authenticates with a Cryptolens Access Token; this connector sends it in the undocumented `token` HTTP header so it never lands in request URLs or bodies (three key routes require it in the body and are marked in their descriptions).

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [cryptolens.io](https://cryptolens.io) |
| **Authentication** | API key |
| **Actions** | 76 |
| **Events** | 0 |
| **Slug** | `cryptolens` |

## Use it

Add Cryptolens from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cryptolens.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate License Key | `activateKey` | Activate a license key for a device (machine code). Consumes a machine-code slot on the key. Requires the Activate permission. WARNING: this route rejects the token header, so the access token travels in the query string and is written into the execution record. |
| Add Customer | `addCustomer` | Create a customer record and return its CustomerId, customer secret and optional portal link. Requires the AddCustomer permission. |
| Add Data Object | `addDataObject` | Create a data object (named string/int variable) attached to the account, a product or a key via ReferencerType and ReferencerId. Requires the DataObject permission. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Add Data Object To Key | `addDataObjectToKey` | Create a data object attached to a specific license key, addressed by product id and key string. Usable with a key-locked access token. |
| Add Data Object To Machine Code | `addDataObjectToMachineCode` | Create a data object attached to one activated device (machine code) of a license key. |
| Add Feature To Key | `addFeature` | Turn on one of the eight feature flags (1-8) on a license key. Requires the AddFeature permission. |
| Add Reseller | `addReseller` | Create a reseller record. Needs the Reseller permission and the reseller module enabled on the billing page. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Associate User With Customer | `associateUser` | Link an existing end-user login to a customer record so their licenses resolve. Needs the Associate permission. |
| Block License Key | `blockKey` | Mark a license key as blocked so Get Key and Activate refuse it. DESTRUCTIVE: blocking a key in use breaks that customer's software activation. Requires the BlockKey permission. |
| Change Key Customer | `changeCustomer` | Assign a license key to a customer, or clear the assignment by omitting CustomerId. Requires the ChangeCustomer permission. |
| Change Key Notes | `changeNotes` | Replace the free-text notes field on a license key. Requires the ChangeNotes permission. |
| Change Key Reseller | `changeReseller` | Assign a license key to a reseller, or clear the assignment by omitting ResellerId. Requires the ChangeReseller permission. |
| Change User Password | `changeUserPassword` | Change an end user's password, either with their old password, with a reset token, or in admin mode. Needs the ChangePassword permission. |
| Create Key From Template | `createKeyFromTemplate` | Create a license key from a saved license template id. Requires the CreateKey permission. |
| Create Key Locked Token | `keyLock` | Exchange a product id and key for a new access token restricted to that single key, plus the key's internal id. SECURITY: the response contains a live Cryptolens access token, so every consumer of this action receives a credential and it is stored in the execution record. The calling token's Key Lock must be -1. |
| Create License Key | `createKey` | Create one or more new license keys for a product, with optional period, features F1-F8, notes, block flag, customer, trial activation and machine limit. Requires the CreateKey permission. |
| Create Message | `createMessage` | Broadcast a message on a channel so client applications can pick it up (for example a maintenance or upgrade notice). Requires the CreateMessage permission. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Create Password Reset Token | `resetPasswordToken` | Issue a one-time password reset token for an end user, to be handed to them out of band. Needs the ResetPasswordToken permission. |
| Create Payment Form Session | `createPaymentFormSession` | Open a hosted Cryptolens payment form session and return the checkout URL. MONEY-ADJACENT: a completed session charges a real customer. Requires the PaymentForm permission. |
| Create Trial Key | `createTrialKey` | Create a trial license key for a product, optionally bound to a machine code. Requires the CreateTrialKey permission. |
| Deactivate License Key | `deactivateKey` | Release a device (machine code) from a license key, freeing a seat. Requires the Deactivate permission. WARNING: this route rejects the token header, so the access token travels in the query string and is written into the execution record. |
| Decrement Data Object Int Value | `decrementIntValue` | Subtract from a data object's integer value by object id, with an optional lower bound. Requires the DecrementIntValue permission. |
| Decrement Data Object Int Value For Key | `decrementIntValueToKey` | Subtract from the integer value of a key-scoped data object, addressed by product id plus key and then either the object Id or its Name. |
| Decrement Data Object Int Value For Machine Code | `decrementIntValueToMachineCode` | Subtract from the integer value of a device-scoped data object, addressed by product id, key, machine code and then either the object Id or its Name. |
| Dissociate User From Customer | `dissociateUser` | Unlink an end-user login from its customer record, so the user stops seeing that customer's licenses. Needs the Dissociate permission. |
| Edit Customer | `editCustomer` | Update an existing customer's name, email, company, notes, device limit or portal settings. Requires the EditCustomer permission. |
| Edit Reseller | `editReseller` | Update an existing reseller's contact details or metadata. Needs the Reseller permission. |
| Extend License | `extendLicense` | Push a license key's expiry date forward by a number of days. Changes real billing state on a live key. Requires the ExtendLicense permission. |
| Get Customer Licenses | `getCustomerLicenses` | List every license key assigned to a customer id. Requires the GetCustomerLicenses permission. |
| Get Customer Licenses By Secret | `getCustomerLicensesBySecret` | List a customer's license keys using the customer secret instead of the customer id, for end-user facing flows. Requires the GetCustomerLicensesBySecret permission. |
| Get Customers | `getCustomers` | List or search customers in the account. Returns personal data (names and emails). Requires the GetCustomers permission. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Get Daily Aggregates | `getDailyAggregates` | Return per-day aggregated Web API log counts for dashboards, optionally narrowed to a product and a date range. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Get Daily Country Aggregates | `getDailyCountryAggregates` | Return per-day, per-country aggregated Web API log counts, optionally narrowed to a product, country code and date range. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Get End Users | `getUsers` | List the end-user logins registered for user authentication, optionally only those linked to one customer. Needs the GetUsers permission. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Get Events | `getEvents` | Page through the raw usage events recorded for the account, filtered by time, product or key. Requires the GetEvents permission. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Get Key Devices | `getKeyDevices` | List the devices (machine codes) seen against a license key over a date range, with last-seen information. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Get Key Usage Summaries | `getKeyUsageSummaries` | Return aggregated per-key usage summaries over a date range, for reporting on how heavily each license is used. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Get Keys For Product | `getKeys` | List the license keys of a product, paged 99 per page, with optional ordering, search query or GlobalId lookup. Requires the GetKeys permission. |
| Get License Activity Buckets | `getLicenseActivityBuckets` | Return time-bucketed licensing activity for a product, key or device, for usage charts. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Get License Key | `getKey` | Read a single license key by product id and key string, optionally signed and with metadata. Requires the GetKey permission. WARNING: key/GetKey, key/Activate and key/Deactivate are the only Cryptolens routes that reject the `token` HTTP header (401) - they read the access token from the query string or form collection only. This action therefore carries the token in its query string, so the access token IS written into this action's recorded request URL. Every other action in this connector sends it in a header instead. |
| Get License Templates | `getLicenseTemplates` | List the saved license templates that Create Key From Template can use. Needs the LicenseTemplate permission. |
| Get Messages | `getMessages` | Read broadcast messages on a channel, optionally only those created after a given time. Requires the GetMessages permission. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Get Object Log | `getObjectLog` | Page through the audit log of objects created, edited or removed in the account. Requires the GetObjectLog permission. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Get Products | `getProducts` | List every product in the Cryptolens account, including each product's Id, Name, feature definitions and the product's public key. Requires the GetProducts permission on the access token. |
| Get Reseller Customers | `getResellerCustomers` | List the customers that belong to one reseller. Needs the Reseller permission. |
| Get Resellers | `getResellers` | List or search the resellers registered in the account. Needs the Reseller permission. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Get Web API Log | `getWebApiLog` | Page through the licensing event log (activations, expiry changes, data object changes), filtered by product, key, machine code, state or anomaly classification. Requires the GetWebAPILog permission. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Increment Data Object Int Value | `incrementIntValue` | Add to a data object's integer value by object id, with an optional upper bound. Requires the IncrementIntValue permission. |
| Increment Data Object Int Value For Key | `incrementIntValueToKey` | Add to the integer value of a key-scoped data object, addressed by product id plus key and then either the object Id or its Name. |
| Increment Data Object Int Value For Machine Code | `incrementIntValueToMachineCode` | Add to the integer value of a device-scoped data object, addressed by product id, key, machine code and then either the object Id or its Name. |
| List Data Objects | `listDataObjects` | List data objects belonging to the account, a product or a key, filtered by referencer and name substring. Requires the ListDataObjects permission. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| List Data Objects For Key | `listDataObjectsToKey` | List the data objects attached to one license key, addressed by product id and key string. |
| List Data Objects For Machine Code | `listDataObjectsToMachineCode` | List the data objects attached to one activated device (machine code) of a license key. |
| Record Subscription Usage | `recordUsage` | Report metered usage against a subscription license key for recurring billing. MONEY-ADJACENT: recorded usage is invoiced. Needs the Subscription permission and the recurring billing module. |
| Register Event | `registerEvent` | Record one usage or revenue event for a product, key or device so it feeds the Cryptolens analytics engine. Requires the RegisterEvent permission. Cryptolens fails a call with an empty request body (HTTP 500 "Something went wrong" or "The input parameters were incorrect."), so send at least one field - e.g. v: 1. |
| Register Events Batch | `registerEvents` | Record a batch of usage events in one call. Events is a list of objects with FeatureName, EventName, Value, Currency, Time and Metadata. |
| Register User | `registerUser` | Create an end-user login, optionally tied to an existing customer record. Needs the Register permission. |
| Remove Customer | `removeCustomer` | Permanently delete a customer record by id. Their license keys stay but lose the customer assignment. Requires the RemoveCustomer permission. |
| Remove Data Object | `removeDataObject` | Permanently delete a data object by its object id. Requires the RemoveDataObject permission. |
| Remove Data Object For Key | `removeDataObjectToKey` | Permanently delete a key-scoped data object, addressed by product id plus key and then either the object Id or its Name. |
| Remove Data Object For Machine Code | `removeDataObjectToMachineCode` | Permanently delete a device-scoped data object, addressed by product id, key, machine code and then either the object Id or its Name. |
| Remove End User | `removeUser` | Permanently delete an end-user login by username. DESTRUCTIVE: the user loses access to their licenses through user authentication. Needs the RemoveUser permission. |
| Remove Feature From Key | `removeFeature` | Turn off one of the eight feature flags (1-8) on a license key. Requires the RemoveFeature permission. |
| Remove Message | `removeMessage` | Permanently delete a broadcast message by its id. Requires the RemoveMessage permission. |
| Remove Reseller | `removeReseller` | Permanently delete a reseller record by id. Needs the Reseller permission. |
| Set Data Object Int Value | `setIntValue` | Overwrite a data object's integer value by object id. Requires the SetIntValue permission. |
| Set Data Object Int Value For Key | `setIntValueToKey` | Overwrite the integer value of a key-scoped data object, addressed by product id plus key and then either the object Id or its Name. |
| Set Data Object Int Value For Machine Code | `setIntValueToMachineCode` | Overwrite the integer value of a device-scoped data object, addressed by product id, key, machine code and then either the object Id or its Name. |
| Set Data Object String Value | `setStringValue` | Overwrite a data object's string value by object id. Requires the SetStringValue permission. |
| Set Data Object String Value For Key | `setStringValueToKey` | Overwrite the string value of a key-scoped data object, addressed by product id plus key and then either the object Id or its Name. |
| Set Data Object String Value For Machine Code | `setStringValueToMachineCode` | Overwrite the string value of a device-scoped data object, addressed by product id, key, machine code and then either the object Id or its Name. |
| Set Machine Lock Limit | `machineLockLimit` | Set how many devices may activate a license key (0 = unlimited). Requires the MachineLockLimit permission. |
| Set Trial Activation | `trialActivation` | Enable or disable trial activation on a license key, which lets the first activation set the expiry date. Requires the TrialActivation permission. |
| Unblock License Key | `unblockKey` | Clear the blocked flag on a license key so it can be read and activated again. Requires the UnblockKey permission. |
| Upload Data Object Values For Key | `uploadValuesToKey` | Upload a base64 usage log produced by a Cryptolens SDK into a key-scoped data object, replaying up to 1000 recorded value changes. |
| User Login | `userLogin` | Authenticate an end user by username and password and return the license keys attached to their customer record. Needs the Login permission. |
