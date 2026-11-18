---
description: "Google Street View Publish API (streetviewpublish.googleapis.com v1)."
hidden: true
---

# Google Street View Publish

<img src="../../.gitbook/assets/connectors/google-street-view-publish.png" alt="Google Street View Publish logo" width="64">

Google Street View Publish API (streetviewpublish.googleapis.com v1). List and read the 360 photos a user has published to Google Street View / Google Maps (with places, pose, view counts and Maps publish status) and request an upload reference for a new 360 photo. Authorizes with Google OAuth 2.0 using the scope https://www.googleapis.com/auth/streetviewpublish.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [streetviewpublish.googleapis.com](https://streetviewpublish.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleStreetViewPublish` |

## Use it

Add Google Street View Publish from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleStreetViewPublish.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Photo | `getPhoto` | Gets the metadata of one Street View 360 photo the connected user created (pose, places, connections, share/thumbnail links, view count, Maps publish status). Returns PERMISSION_DENIED for photos the user did not create. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/streetviewpublish. |
| List Photos | `listPhotos` | Lists the 360 photos the connected user has published to Google Street View, with photo IDs, capture/upload times, pose, places, share and thumbnail links, view counts and Maps publish status. Optionally filter by placeId or a latitude/longitude bounding box. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/streetviewpublish. |
| Start Photo Upload | `startUpload` | Starts an upload session for a new Street View 360 photo and returns an uploadUrl (upload reference) to which the photo bytes are sent. Nothing is published by this call alone: a photo only appears after its bytes are uploaded to the uploadUrl and a photo is created with that reference, so it is safe to demo. Requires the Google OAuth scope https://www.googleapis.com/auth/streetviewpublish. |
