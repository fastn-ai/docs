---
description: "Firebase Management API — list and inspect Firebase projects, their Android, iOS and Web apps, app configuration, admin SDK config, and available project…"
hidden: true
---

# Google Firebase

<img src="../../.gitbook/assets/connectors/lg/google-firebase.png" alt="Google Firebase logo">

Firebase Management API — list and inspect Firebase projects, their Android, iOS and Web apps, app configuration, admin SDK config, and available project locations.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [firebase.google.com](https://firebase.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleFirebase` |

## Use it

Add Google Firebase from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleFirebase.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Android App SHA Certificate | `addAndroidAppSha` | Registers a SHA-1 or SHA-256 signing certificate hash on an Android app so the app can use Firebase services that require certificate verification. |
| Add Firebase To Project | `addFirebaseToProject` | Adds Firebase resources and enables Firebase services on an existing Google Cloud project. The project must not already be a Firebase project. Returns a long-running operation. |
| Add Google Analytics | `addGoogleAnalytics` | Links a Google Analytics property to a Firebase project. Supply either an existing Analytics property ID to link it, or an Analytics account ID to provision a new property in that account. Returns a long-running operation. |
| Create Android App | `createAndroidApp` | Registers a new Android app in a Firebase project. Returns a long-running operation whose response carries the created app once it completes. |
| Create iOS App | `createIosApp` | Registers a new iOS app in a Firebase project. Returns a long-running operation whose response carries the created app once it completes. |
| Create Web App | `createWebApp` | Registers a new web app in a Firebase project. Returns a long-running operation whose response carries the created app once it completes. |
| Delete Android App SHA Certificate | `deleteAndroidAppSha` | Removes a SHA certificate from an Android app. |
| Finalize Default Location | `finalizeDefaultLocation` | Sets the permanent location for a project's default Google Cloud resources. Google has decommissioned this endpoint and it now always returns 404; set the location through each product's own API instead. The choice was irreversible once made. |
| Get Admin SDK Config | `getAdminSdkConfig` | Retrieves the configuration values a server uses to initialise the Firebase Admin SDK for a project. |
| Get Analytics Details | `getAnalyticsDetails` | Retrieves the Google Analytics property linked to a Firebase project together with the Analytics data stream mapped to each Firebase app. |

<details>

<summary>See 27 more actions</summary>

* **Get Android App** `getAndroidApp`: Retrieves a single Android app, including its display name, API key ID and lifecycle state.
* **Get Android App Config** `getAndroidAppConfig`: Retrieves the configuration artifact a Android client uses to initialise the Firebase SDK for this app.
* **Get Firebase Project** `getFirebaseProject`: Retrieves a single Firebase project, including its display name, project number, annotations and lifecycle state.
* **Get iOS App** `getIosApp`: Retrieves a single iOS app, including its display name, API key ID and lifecycle state.
* **Get iOS App Config** `getIosAppConfig`: Retrieves the configuration artifact a iOS client uses to initialise the Firebase SDK for this app.
* **Get Operation** `getOperation`: Retrieves the current state of a long-running operation returned by an app creation, Firebase enablement or Google Analytics action. Poll it until 'done' is true.
* **Get Web App** `getWebApp`: Retrieves a single web app, including its display name, API key ID and lifecycle state.
* **Get Web App Config** `getWebAppConfig`: Retrieves the configuration artifact a web client uses to initialise the Firebase SDK for this app.
* **List Android App SHA Certificates** `listAndroidAppSha`: Lists the SHA-1 and SHA-256 certificate hashes registered on an Android app. These certificates authorise the app to use Firebase services such as Dynamic Links and Google Sign-In.
* **List Android Apps** `listAndroidApps`: Lists the Android apps registered in a Firebase project, one page at a time.
* **List Available Locations** `listAvailableLocations`: DEPRECATED - DO NOT USE. Google has DECOMMISSIONED projects.availableLocations.list; the endpoint answers 404 {"error":{"code":404,"message":"Requested entity was not found.","status":"NOT_FOUND"}} for every project, so no request-shape change can make it work. The "default GCP resource location" concept it served is retired - choose a location through each product's own API (Cloud Firestore, Cloud Storage, App Engine) instead. Ref: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list
* **List Available Projects** `listAvailableProjects`: Lists the Google Cloud projects that do not yet have Firebase resources and so are available to have Firebase added to them.
* **List Firebase Projects** `listFirebaseProjects`: Lists every Firebase project the authenticated account can access, one page at a time.
* **List iOS Apps** `listIosApps`: Lists the iOS apps registered in a Firebase project, one page at a time.
* **List Web Apps** `listWebApps`: Lists the web apps registered in a Firebase project, one page at a time.
* **Remove Android App** `removeAndroidApp`: Removes a Android app from its Firebase project. By default the app is soft-deleted and can be restored with the matching undelete action until its expiry time; set 'immediate' to delete it permanently.
* **Remove Google Analytics** `removeGoogleAnalytics`: Unlinks the Google Analytics property currently associated with a Firebase project. The Analytics property itself is not deleted, only the link and the per-app data stream mappings.
* **Remove iOS App** `removeIosApp`: Removes a iOS app from its Firebase project. By default the app is soft-deleted and can be restored with the matching undelete action until its expiry time; set 'immediate' to delete it permanently.
* **Remove Web App** `removeWebApp`: Removes a web app from its Firebase project. By default the app is soft-deleted and can be restored with the matching undelete action until its expiry time; set 'immediate' to delete it permanently.
* **Search Apps** `searchApps`: Lists every Firebase app in a project across all platforms in one call, optionally filtered by app ID, namespace or platform. Useful for building app pickers.
* **Undelete Android App** `undeleteAndroidApp`: Restores a Android app that was soft-deleted, returning it to the ACTIVE state. Only works before the app's expiry time and only when it was not removed immediately.
* **Undelete iOS App** `undeleteIosApp`: Restores a iOS app that was soft-deleted, returning it to the ACTIVE state. Only works before the app's expiry time and only when it was not removed immediately.
* **Undelete Web App** `undeleteWebApp`: Restores a web app that was soft-deleted, returning it to the ACTIVE state. Only works before the app's expiry time and only when it was not removed immediately.
* **Update Android App** `updateAndroidApp`: Updates the mutable attributes of a Android app. The fields to change must be named in the update mask; the app ID, project ID and platform identifier are immutable.
* **Update Firebase Project** `updateFirebaseProject`: Updates the mutable attributes of a Firebase project. The fields to change must be named in the update mask; 'name', 'projectId' and 'projectNumber' are immutable.
* **Update iOS App** `updateIosApp`: Updates the mutable attributes of a iOS app. The fields to change must be named in the update mask; the app ID, project ID and platform identifier are immutable.
* **Update Web App** `updateWebApp`: Updates the mutable attributes of a web app. The fields to change must be named in the update mask; the app ID, project ID and platform identifier are immutable.

</details>
