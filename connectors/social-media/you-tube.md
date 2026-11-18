---
description: "YouTube Data API v3 — manage videos, channels, playlists, comments, subscriptions, and search YouTube content"
hidden: true
---

# YouTube

YouTube Data API v3 — manage videos, channels, playlists, comments, subscriptions, and search YouTube content

| | |
| --- | --- |
| **Category** | [Social media](README.md) |
| **Website** | [youtube.com](https://youtube.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 70 |
| **Events** | 0 |
| **Slug** | `youTube` |

## Use it

Add YouTube from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.youTube.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Playlist Image | `insertPlaylistImage` | Upload a custom image for a playlist you own (playlistImages.insert, type hero). Image is sent base64 in a multipart/related body; fastn currently caps execute bodies at 8 KB, so only small images work today. |
| Add Playlist Item | `addPlaylistItem` | Adds a resource (typically a video) to a playlist. |
| Bind Live Broadcast | `bindLiveBroadcast` | Bind a broadcast to a video stream (liveBroadcasts.bind). |
| Create Channel Section | `createChannelSection` | Adds a channel section to the authenticated user's channel. |
| Create Comment | `createComment` | Creates a reply to a comment thread. |
| Create Comment Thread | `createCommentThread` | Creates a new top-level comment on a video. |
| Create Live Broadcast | `insertLiveBroadcast` | Schedule a live broadcast (liveBroadcasts.insert). Needs live streaming enabled on the channel. Returns the broadcast with its id. |
| Create Live Stream | `insertLiveStream` | Create a video stream with RTMP ingestion (liveStreams.insert). Returns stream key and ingestion address in cdn. |
| Create Playlist | `createPlaylist` | Creates a playlist. |
| Create Third-Party Link | `insertThirdPartyLink` | Creates a link between the authenticated YouTube channel and a third-party account (YouTube Data API thirdPartyLinks.insert), e.g. a Google Merchant Center store (channelToStoreLink) for YouTube Shopping or a partner affiliate program (channelToAffiliateProgramLink). Google scope: youtube.third-party-link.creator. Intended for approved YouTube Shopping/affiliate partners; other callers get a 403. Remove it with Delete Third-Party Link. Returns the created link with its linkingToken and status. |
| Delete Caption | `deleteCaption` | Deletes one or more caption tracks. |
| Delete Channel Section | `deleteChannelSection` | Deletes a channel section. |
| Delete Comment | `deleteComment` | Deletes a comment. |
| Delete Live Broadcast | `deleteLiveBroadcast` | Delete a live broadcast (liveBroadcasts.delete). Returns 204. |
| Delete Live Chat Message | `deleteLiveChatMessage` | Delete a live chat message (liveChatMessages.delete). Returns 204. |
| Delete Live Stream | `deleteLiveStream` | Delete a video stream (liveStreams.delete). Returns 204. |
| Delete Playlist | `deletePlaylist` | Deletes a playlist. |
| Delete Playlist Image | `deletePlaylistImage` | Delete a playlist image (playlistImages.delete). Returns 204. |
| Delete Playlist Item | `deletePlaylistItem` | Deletes a playlist item. |
| Delete Subscription | `deleteSubscription` | Deletes a subscription. |
| Delete Third-Party Link | `deleteThirdPartyLink` | Deletes (unlinks) a third-party link of the authenticated YouTube channel by linking token and link type (YouTube Data API thirdPartyLinks.delete). Google scope: youtube.third-party-link.creator. Returns an empty body on success. |
| Delete Video | `deleteVideo` | Deletes a YouTube video. |
| Download Caption | `downloadCaption` | Download a caption track you own (captions.download, alt=media). Leave tfmt empty to get the file in its uploaded format; YouTube may answer 400 "Unsupported Output Format" when asked to convert an uploaded track. Returns {name, mime, size, data} where data is the file as base64. |
| Get Video Analytics Report | `getVideoAnalyticsReport` | Retrieves YouTube Analytics report data for a channel or content owner. Uses the YouTube Analytics API. |
| Get Video Rating | `getVideoRating` | Retrieves the ratings that the authorized user gave to a list of specified videos. |
| List Activities | `listActivities` | Returns a list of channel activity events that match the request criteria. |
| List Captions | `listCaptions` | Returns a list of caption tracks that are associated with a specified video. |
| List Channel Sections | `listChannelSections` | Returns a list of channelSection resources that match the API request criteria. |
| List Channels | `listChannels` | Returns a collection of zero or more channel resources matching the request criteria. |
| List Comment Threads | `listCommentThreads` | Returns a list of comment threads matching the API request parameters. |
| List Comments | `listComments` | Returns a list of comments matching the API request parameters. |
| List Content Owners | `listContentOwners` | Retrieves the YouTube content owners (CMS partners) that the authenticated user is linked to. Read-only. Requires the youtubepartner scope. |
| List I18n Languages | `listI18nLanguages` | Returns a list of application languages that the YouTube website supports. |
| List I18n Regions | `listI18nRegions` | Returns a list of content regions that the YouTube website supports. |
| List Live Broadcasts | `listLiveBroadcasts` | List the connected channel's live broadcasts (liveBroadcasts.list) filtered by broadcastStatus: all, active, completed or upcoming. Needs live streaming enabled on the channel. |
| List Live Chat Messages | `listLiveChatMessages` | List messages in a live chat (liveChatMessages.list). liveChatId comes from the broadcast snippet.liveChatId. |
| List Live Streams | `listLiveStreams` | List the channel's video streams (liveStreams.list, mine=true), including ingestion info. |
| List Managed Channels | `listManagedChannels` | Lists channels managed by the content owner the authenticated user is linked to (managedByMe). Read-only. Requires the youtubepartner scope. |
| List Members | `listMembers` | Lists members of a channel (YouTube Memberships feature). Requires youtube.channel-memberships.creator scope. |
| List Membership Levels | `listMembershipLevels` | Lists membership levels defined for a channel. Requires youtube.channel-memberships.creator scope. |
| List Playlist Images | `listPlaylistImages` | List the custom images of a playlist (playlistImages.list). |
| List Playlist Items | `listPlaylistItems` | Returns a collection of playlist items matching the API request parameters. |
| List Playlists | `listPlaylists` | Returns a collection of playlists matching the API request parameters. |
| List Subscriptions | `listSubscriptions` | Returns subscription resources matching the API request criteria. |
| List Third-Party Links | `listThirdPartyLinks` | Lists the third-party account links of the authenticated YouTube channel (YouTube Data API thirdPartyLinks.list), such as links between the channel and a merchandise store (channelToStoreLink) or a partner affiliate program (channelToAffiliateProgramLink). Read-only. Google scope: youtube.third-party-link.creator. Filter by type or by linkingToken. Returns items[] with linkingToken, snippet (type and store/affiliate details) and status.linkStatus; an empty list if the channel has no links. |
| List Video Abuse Report Reasons | `listVideoAbuseReportReasons` | Retrieves a list of reasons that can be used to report abusive videos. |
| List Video Categories | `listVideoCategories` | Returns a list of categories that can be associated with YouTube videos. |
| List Videos | `listVideos` | Returns a list of videos matching the API request parameters. Supports listing by id, chart (mostPopular), or myRating. There is no upstream 'mine' filter on this endpoint (removed — always caused HTTP 400 'No filter selected'); to list the authenticated user's own uploads, first call List Channels with mine=true to get contentDetails.relatedPlaylists.uploads, then call List Playlist Items on that playlist id. |
| Mark Comment as Spam | `markCommentAsSpam` | Expresses the caller's opinion that one or more comments should be flagged as spam. |
| Rate Video | `rateVideo` | Add a like or dislike rating to a video, or remove a rating from a video. |
| Report Video Abuse | `reportVideoAbuse` | Reports a video for containing abusive content. |
| Search | `search` | Returns a collection of search results matching the query. Can filter by resource type (video, channel, playlist). |
| Send Live Chat Message | `insertLiveChatMessage` | Post a text message to a live chat (liveChatMessages.insert). |
| Set Comment Moderation Status | `setCommentModerationStatus` | Sets the moderation status of one or more comments (published, heldForReview, rejected). |
| Set Video Thumbnail | `setThumbnail` | Upload a custom thumbnail for a video you own (thumbnails.set). Needs a channel verified for custom thumbnails. Replaces the current thumbnail and cannot restore an auto-generated one. Image is sent base64 in a multipart/related body; fastn currently caps execute bodies at 8 KB, so only small images work today. |
| Set Watermark | `setWatermark` | Set the channel watermark (branding image) shown on its videos (watermarks.set). Image square, at least 150x150. timingType offsetFromStart/offsetFromEnd, offsetMs when it appears, durationMs how long. Image is sent base64 in a multipart/related body; fastn currently caps execute bodies at 8 KB, so only small images work today. |
| Subscribe to Channel | `subscribeToChannel` | Subscribes the authenticated user to a channel. |
| Transition Live Broadcast | `transitionLiveBroadcast` | Change a broadcast status to testing, live or complete (liveBroadcasts.transition). The bound stream must be active. |
| Unset Watermark | `unsetWatermark` | Remove the channel's watermark image (watermarks.unset). Returns 204 with no body. |
| Update Caption | `updateCaption` | Replace the text of an existing caption track and set its draft flag (captions.update, multipart). Returns the updated caption resource. |
| Update Channel | `updateChannel` | Update the channel's branding (channels.update, part=brandingSettings). WARNING: YouTube replaces the whole brandingSettings.channel object, so read the current values with List Channels (part=brandingSettings) and send every field you want to keep. Returns the updated channel. |
| Update Comment | `updateComment` | Modifies a comment. |
| Update Comment Thread | `updateCommentThread` | Updates the text of a top-level comment via comments.update. |
| Update Playlist | `updatePlaylist` | Modifies a playlist's metadata. |
| Update Playlist Item | `updatePlaylistItem` | Modifies a playlist item (e.g. changes its position in a playlist). |
| Update Third-Party Link | `updateThirdPartyLink` | Updates an existing third-party link of the authenticated YouTube channel (YouTube Data API thirdPartyLinks.update), identified by its linkingToken; send the full snippet you want stored (e.g. a new store name/URL or affiliate programStatus). Google scope: youtube.third-party-link.creator. Intended for approved YouTube Shopping/affiliate partners. Returns the updated link. |
| Update Video | `updateVideo` | Updates a video's metadata. The part parameter identifies the properties that the write operation will set. |
| Upload Caption | `insertCaption` | Upload a caption track (SRT, WebVTT or SBV text) to a video you own (captions.insert, multipart). Text-only, so it works under the 8 KB execute limit for short tracks. Returns the caption resource with its id. |
| Upload Channel Banner | `insertChannelBanner` | Upload a channel banner image (channelBanners.insert, min 2048x1152, 16:9). Returns a url; apply it with Update Channel brandingSettings.image.bannerExternalUrl. Uploading alone does not change the channel. Image is sent base64 in a multipart/related body; fastn currently caps execute bodies at 8 KB, so only small images work today. |
| Upload Video | `uploadVideo` | Uploads a video file to the authenticated user's YouTube channel with a title, description, category and privacy status. The video bytes are passed as a base64 string, so this action suits short clips; very large files exceed the action payload limit. |
