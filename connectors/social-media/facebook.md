---
description: "Facebook (Meta Graph API v25.0) connector for Page publishing and engagement: list/read Pages, create posts, publish photos/videos, comments, insights, and…"
---

# Facebook

Facebook (Meta Graph API v25.0) connector for Page publishing and engagement: list/read Pages, create posts, publish photos/videos, comments, insights, and Page webhook subscriptions. OAuth 2.0 (Facebook Login) primary.

| | |
| --- | --- |
| **Category** | [Social media](README.md) |
| **Website** | [facebook.com](https://facebook.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 37 |
| **Events** | 3 |
| **Slug** | `facebook` |

## Use it

Add Facebook from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.facebook.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create App Subscription | `createAppSubscription` | App-level webhook subscription for the 'page' object. Requires an app access token (appId\|appSecret) passed as access_token. |
| Create Comment | `createComment` | Create a comment on an object, or reply to a comment by passing its id as objectId. Requires a Page access token. |
| Create Page Post | `createPagePost` | Publish a text (and optional link) post to a Page feed. Requires a Page access token (pass via pageAccessToken from listPages). |
| Delete Comment | `deleteComment` | Delete a comment on the Page's content (DELETE /{commentId}). Returns {success}. |
| Delete Photo or Video | `deleteMediaObject` | Delete a Page photo or video by id (DELETE /{objectId}). Returns {success}. |
| Delete Post | `deletePost` | Delete a Page post (or photo/video object) by id. Requires a Page access token. |
| Get Comment | `getComment` | Read one comment (GET /{commentId}). |
| Get Comments | `getComments` | Get comments on a post, photo, or other object. |
| Get Lead | `getLead` | Retrieve a single submitted lead by its leadgen id, including the answers the person entered. This is the follow-up call for a leadgen webhook notification, whose payload carries only the leadgen_id and no field data. Requires the leads_retrieval permission and a Page access token for the Page that owns the form. |
| Get Me | `getMe` | Get the authenticated user's basic profile. |
| Get Page | `getPage` | Get details for a Facebook Page by id. |
| Get Page Feed | `getPageFeed` | Get posts from a Page feed. |
| Get Page Insights | `getPageInsights` | Get insights/analytics metrics for a Page. |
| Get Post | `getPost` | Read one Page post (GET /{postId}). |
| Get Post Insights | `getPostInsights` | Metrics for one Page post (GET /{postId}/insights), e.g. post_impressions, post_clicks, post_reactions_by_type_total. |
| Get Video | `getVideo` | Read one Page video including processing status (GET /{videoId}). |
| Hide Comment | `hideComment` | Hide or unhide a comment on the Page's content (POST /{commentId}?is_hidden=true\|false). Returns {success}. |
| Like Object | `likeObject` | Like a post or comment as the Page (POST /{objectId}/likes). Returns {success}. |
| List Albums | `listAlbums` | List the Page's photo albums (GET /{pageId}/albums). |
| List App Subscriptions | `listAppSubscriptions` | List the app's current webhook subscriptions. Requires an app access token. |
| List Form Leads | `listFormLeads` | List all leads submitted through a specific Lead Ads form, newest first, with the answers each person entered. Use this to backfill leads or to recover any the webhook missed. Requires the leads_retrieval permission and a Page access token for the Page that owns the form. |
| List Granted Permissions | `listPermissions` | List the permissions the connected user has granted or declined for this app. Each entry has a permission name and a status of granted or declined. Use it to verify a connection carries the scopes an action needs before calling it. |
| List Lead Forms | `listLeadForms` | List the Lead Ads instant forms attached to a Facebook Page. Returns each form's id, name, status and questions. Use the returned form id with List Form Leads. Requires a Page access token plus the pages_manage_ads or leads_retrieval permission. |
| List Managed Pages | `listPages` | List the Facebook Pages the authenticated user manages. Each entry includes the Page access_token needed for publishing/engagement actions. |
| List Page Photos | `listPagePhotos` | List photos uploaded by the Page (GET /{pageId}/photos?type=uploaded). |
| List Page Ratings | `listPageRatings` | List recommendations/reviews left on the Page (GET /{pageId}/ratings). |
| List Page Videos | `listPageVideos` | List videos uploaded by the Page (GET /{pageId}/videos). |
| List Pages For Trigger | `listPagesForTrigger` | Lists the Facebook Pages the connected user manages, returning only each Page's id and name (no Page access tokens). Used by app triggers to let the user pick which Page's events to receive. |
| List Published Posts | `listPublishedPosts` | List posts published by the Page (GET /{pageId}/published_posts). |
| List Scheduled Posts | `listScheduledPosts` | List the Page's scheduled (not yet published) posts (GET /{pageId}/scheduled_posts). |
| Publish Photo | `publishPhoto` | Publish a photo to a Page from a hosted image URL. Requires a Page access token. |
| Publish Video | `publishVideo` | Publish a video to a Page from a hosted file URL. Requires a Page access token. |
| Subscribe Page App | `subscribePageApp` | Install/subscribe the app on a Page so it receives webhook notifications. Requires a Page access token. |
| Unlike Object | `unlikeObject` | Remove the Page's like from a post or comment (DELETE /{objectId}/likes). Returns {success}. |
| Unsubscribe Page App | `unsubscribePageApp` | Uninstall/unsubscribe the app from a Page. Requires a Page access token. |
| Update Comment | `updateComment` | Edit a comment the Page wrote (POST /{commentId} message). Returns {success}. |
| Update Post | `updatePost` | Edit the text of a Page post (POST /{postId} message). Returns {success}. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Lead Submitted | `leadgen` | Fires when someone submits one of the Page's Lead Ads instant forms. The payload carries only leadgen_id - call Get Lead with it to retrieve the submitted answers. Setup: Meta app console &gt; Products &gt; Webhooks &gt; Page &gt; Subscribe to this object, tick the leadgen field, paste this connector's webhook URL, and use the connector's verification secret as the verify token. Then run Subscribe Page App on each customer Page with subscribed_fields including leadgen. Payload modelled from Meta's documented Lead Ads sample, not captured. |
| Page Feed Activity | `feed` | Fires on activity in the Page feed - a new post, comment, reaction, share or edit. Setup: Meta app console &gt; Products &gt; Webhooks &gt; Page &gt; Subscribe to this object, tick the feed field, paste this connector's webhook URL, and use the connector's verification secret as the verify token. Then run Subscribe Page App on each customer Page with subscribed_fields including feed. Payload modelled from Meta's documented Page feed sample, not captured. |
| Page Mentioned | `mention` | Fires when the Page is mentioned in another person's or Page's post or comment. Setup: Meta app console &gt; Products &gt; Webhooks &gt; Page &gt; Subscribe to this object, tick the mention field, paste this connector's webhook URL, and use the connector's verification secret as the verify token. Then run Subscribe Page App on each customer Page with subscribed_fields including mention. Payload modelled from Meta's documented Page mention sample, not captured. |
