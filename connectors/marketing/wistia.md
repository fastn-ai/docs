---
description: "Wistia video hosting platform."
hidden: true
---

# Wistia

<img src="../../.gitbook/assets/connectors/lg/wistia.png" alt="Wistia logo">

Wistia video hosting platform. Manage projects, medias, customizations, captions, project sharings, and access account and viewing statistics via the Wistia Data API and Stats API, plus media upload/import via the Upload API.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [wistia.com](https://wistia.com) |
| **Authentication** | Bearer token |
| **Slug** | `wistia` |

## Use it

Add Wistia from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wistia.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Copy Media | `copyMedia` | Copy a media. Optionally place the copy in a different project and assign a different owner. |
| Copy Project | `copyProject` | Copy a project, including all media and sections. Returns the new project. Sharing information is not copied. |
| Create Caption | `createCaption` | Add captions to a video from SRT file contents. Returns 400 if captions already exist for the video. |
| Create Media Customizations | `createCustomizations` | Replace the embed customizations for a video with the provided set of options. |
| Create Project | `createProject` | Create a new project in the Wistia account. |
| Create Project Sharing | `createProjectSharing` | Share a project with a person by email, creating a new sharing object with the given permissions. |
| Delete Caption | `deleteCaption` | Remove the captions for a specific language from a video. |
| Delete Media | `deleteMedia` | Delete a media from the account. Returns an object representing the deleted media. |
| Delete Media Customizations | `deleteCustomizations` | Delete all explicit embed customizations for a video, resetting it to defaults. |
| Delete Project | `deleteProject` | Delete a project. Returns an object representing the deleted project. |

<details>

<summary>See 30 more actions</summary>

* **Delete Project Sharing** `deleteProjectSharing`: Delete a sharing on a project. Returns the deleted sharing object.
* **Get Account** `getAccount`: Retrieve information about the authenticated Wistia account, including its name, URL, and total media count.
* **Get Account Stats** `getAccountStats`: Retrieve account-wide aggregate statistics: total load count, play count, and hours watched.
* **Get Account Stats By Date** `getAccountStatsByDate`: Retrieve account-wide statistics broken down by day for a date range.
* **Get Caption** `getCaption`: Retrieve the captions for a specific language on a video in SRT format.
* **Get Event** `getEvent`: Retrieve the information about a single viewing session event by event key.
* **Get Media** `getMedia`: Retrieve information about a specific media, including its assets and thumbnail.
* **Get Media Customizations** `getCustomizations`: Retrieve the explicitly-defined embed customizations saved for a video.
* **Get Media Detailed Stats** `getMediaDetailedStats`: Retrieve detailed statistics for a video, including load count, play rate, engagement, visitors, and action stats.
* **Get Media Engagement** `getMediaEngagement`: Retrieve the engagement and rewatch data used to build a video's engagement graph.
* **Get Media Stats** `getMediaStats`: Retrieve aggregated embed tracking statistics for a video (page loads, plays, visitors, engagement). Works for videos only.
* **Get Media Stats By Date** `getMediaStatsByDate`: Retrieve a video's statistics broken down by day for a date range.
* **Get Project** `getProject`: Retrieve details about a specific project, including the array of medias it contains.
* **Get Project Sharing** `getProjectSharing`: Retrieve the details of a specific sharing on a project.
* **Get Project Stats** `getProjectStats`: Retrieve aggregate statistics for all videos in a project.
* **Get Project Stats By Date** `getProjectStatsByDate`: Retrieve project statistics broken down by day for a date range.
* **Get Visitor** `getVisitor`: Retrieve the information for a single visitor by visitor key.
* **List Captions** `listCaptions`: List all captions for a video. Returns an array of caption objects with language codes and SRT text.
* **List Events** `listEvents`: List viewing session events from the account. Optionally filter by media, visitor, or date range.
* **List Medias** `listMedias`: List all medias in the account. Supports paging, sorting, and filtering by project, name, type, or hashed id.
* **List Project Sharings** `listProjectSharings`: List all sharings (contacts and contact groups with access) on a project.
* **List Projects** `listProjects`: List all projects in the Wistia account. Supports paging and sorting.
* **List Visitors** `listVisitors`: List visitors who have watched videos in the account. Supports paging, filtering, and search.
* **Purchase Captions** `purchaseCaptions`: Purchase professionally-transcribed English captions for a video. Note: this charges the credit card on the account. Returns 400 if English captions already exist.
* **Update Caption** `updateCaption`: Replace the captions for a specific language on a video with new SRT file contents.
* **Update Media** `updateMedia`: Update attributes on a media such as its name, description, or replacement still image.
* **Update Media Customizations** `updateCustomizations`: Partially update a video's embed customizations. Setting a value to null deletes that key from the saved customizations.
* **Update Project** `updateProject`: Update the attributes of an existing project.
* **Update Project Sharing** `updateProjectSharing`: Update the permissions of an existing sharing on a project.
* **Upload Media** `uploadMedia`: Import a media into Wistia from a public web or FTP URL via the Upload API. To upload a local file, a multipart file part is required (not supported through this action; use URL import).

</details>
