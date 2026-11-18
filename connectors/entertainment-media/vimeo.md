---
description: "Vimeo video platform API."
hidden: true
---

# Vimeo

Vimeo video platform API. OAuth 2.0 (authorization_code). Manage videos, albums/showcases, channels, groups, portfolios, users, and interactions on api.vimeo.com.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [vimeo.com](https://vimeo.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 115 |
| **Events** | 0 |
| **Slug** | `vimeo` |

## Use it

Add Vimeo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.vimeo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add To Watch Later | `addToWatchLater` | Add a video to the authenticated user's Watch Later queue. |
| Add Video Credit | `addVideoCredit` | Credit a person as cast or crew on a video the authenticated user owns. |
| Add Video Privacy Domain | `addVideoPrivacyDomain` | Allow a video with whitelist embed privacy to be embedded on the specified domain. Needs a paid Vimeo plan (free accounts get 403, error_code 3202). |
| Add Video Privacy User | `addVideoPrivacyUser` | Grant a specific user access to a video whose view privacy is restricted to users. Needs a paid Vimeo plan (user-restricted privacy is not available on free accounts). |
| Add Video Tag | `addVideoTag` | Add a single tag to a video. Only owned videos can be tagged. |
| Add Video To Channel | `addVideoToChannel` | Add a video to a channel that the authenticated user moderates. |
| Add Video To Folder | `addVideoToFolder` | Add a video to a folder (project) owned by the authenticated Vimeo user. |
| Add Video To Group | `addVideoToGroup` | Add a video to a group on Vimeo. |
| Add Video To Portfolio | `addVideoToPortfolio` | Add a video to a portfolio owned by the authenticated Vimeo user. Needs a paid Vimeo plan (Vimeo help: portfolios need Standard/Pro or higher) and an existing portfolio made in the Vimeo web interface; the API cannot create one. |
| Add Video To Showcase | `addVideoToShowcase` | Add a video to a showcase (album) owned by the authenticated user. |
| Check If Following User | `checkUserFollowing` | Check whether the authenticated Vimeo user follows a specific user. Returns 204 if following, 404 if not. |
| Check If Video Liked | `checkVideoLiked` | Check whether the authenticated user has liked a specific video. Returns 204 if liked, 404 otherwise. |
| Check Video In My Library | `checkVideoInLibrary` | Check whether a specific video belongs to or appears in the authenticated user's library. Returns the video if present, 404 otherwise. |
| Check Video Tag | `checkVideoTag` | Check whether a specific tag is applied to a video. Returns 204 if present, 404 otherwise. |
| Check Watch Later | `checkWatchLater` | Check whether a specific video is in the authenticated user's Watch Later queue. Returns 204 if present, 404 otherwise. |
| Create Channel | `createChannel` | Create a new channel for the authenticated user. |
| Create Folder | `createFolder` | Create a new folder (project) for the authenticated Vimeo user to organize videos. |
| Create Group | `createGroup` | Create a new group owned by the authenticated Vimeo user. |
| Create Showcase | `createShowcase` | Create a new showcase (album) for the authenticated user. |
| Create User Portrait | `createUserPortrait` | Create a portrait image placeholder for the authenticated user. Vimeo returns an upload link that the image bytes are then transferred to out-of-band. |
| Create Video Comment | `createVideoComment` | Post a new comment on a video. |
| Create Video Text Track | `createTextTrack` | Create a text track (caption or subtitle) on a video. Vimeo returns a link that the WebVTT file contents are then uploaded to. |
| Create Video Thumbnail | `createVideoThumbnail` | Create a thumbnail placeholder on a video, either from a timecode in the video or as an empty slot. Vimeo returns an upload link that the image bytes are then transferred to out-of-band. |
| Create Video Upload | `createVideoUpload` | Create a new video resource and initiate an upload. For resumable uploads pass upload.approach 'tus' with the file size; Vimeo returns an upload.upload_link that the file bytes are then transferred to out-of-band (tus/PUT). Also supports 'pull' (from a URL) and 'post' approaches. |
| Delete Channel | `deleteChannel` | Delete a channel owned by the authenticated user. |
| Delete Folder | `deleteFolder` | Delete a folder (project) owned by the authenticated Vimeo user. By default the videos inside are not deleted. |
| Delete Group | `deleteGroup` | Delete a group owned by the authenticated Vimeo user. |
| Delete Showcase | `deleteShowcase` | Delete a showcase (album) owned by the authenticated user. |
| Delete User Portrait | `deleteUserPortrait` | Delete a portrait image belonging to the authenticated Vimeo user. |
| Delete Video | `deleteVideo` | Permanently delete an owned Vimeo video by its numeric ID. |
| Delete Video Comment | `deleteVideoComment` | Delete a comment that the authenticated user owns from a video. |
| Delete Video Credit | `deleteVideoCredit` | Remove a credit from a video the authenticated user owns. |
| Delete Video Text Track | `deleteTextTrack` | Delete a text track from a video. |
| Delete Video Thumbnail | `deleteVideoThumbnail` | Delete a thumbnail image from a video the authenticated user owns. |
| Edit Channel | `editChannel` | Update the metadata of a channel owned by the authenticated user. |
| Edit Current User | `editUser` | Update the authenticated Vimeo user's profile fields such as name, bio, and location. |
| Edit Folder | `editFolder` | Rename a folder (project) owned by the authenticated Vimeo user. |
| Edit Showcase | `editShowcase` | Update the metadata of a showcase (album) owned by the authenticated user. |
| Edit Video | `editVideo` | Update a video's metadata such as name, description, and privacy settings. Only owned videos can be edited. |
| Edit Video Comment | `editVideoComment` | Update the text of an existing comment that the authenticated user owns. |
| Edit Video Credit | `editVideoCredit` | Update the name or role of a credit on a video the authenticated user owns. |
| Edit Video Text Track | `editTextTrack` | Update a text track's metadata, such as its name, language, or active state. |
| Follow User | `followUser` | Make the authenticated Vimeo user follow another user by their numeric user ID. |
| Get Category | `getCategory` | Retrieve details of a specific content category by its slug. |
| Get Channel | `getChannel` | Retrieve metadata for a specific channel by its numeric ID. |
| Get Channel Video | `getChannelVideo` | Check whether a specific video is in a channel and return it if present. |
| Get Current User | `getCurrentUser` | Retrieve the profile of the authenticated Vimeo user, including account details, quotas, and metadata. |
| Get Folder | `getFolder` | Retrieve a specific folder (project) owned by the authenticated Vimeo user. |
| Get Group | `getGroup` | Retrieve metadata for a specific group by its numeric ID. |
| Get On Demand Page | `getOnDemandPage` | Retrieve a specific Vimeo On Demand page by its numeric ID. |
| Get Portfolio | `getPortfolio` | Retrieve a specific portfolio owned by the authenticated Vimeo user. Needs a paid Vimeo plan (Vimeo help: portfolios need Standard/Pro or higher) and an existing portfolio made in the Vimeo web interface; the API cannot create one. |
| Get Showcase | `getShowcase` | Retrieve a specific showcase (album) owned by the authenticated user. |
| Get Showcase Video | `getShowcaseVideo` | Check whether a specific video is in a showcase and return it if present. |
| Get Tag | `getTag` | Retrieve metadata about a specific tag word. |
| Get User | `getUser` | Retrieve the public profile of a specific Vimeo user by their numeric user ID. |
| Get User Portrait | `getUserPortrait` | Retrieve a specific portrait image of the authenticated user by its picture ID. |
| Get Video | `getVideo` | Retrieve the metadata of a single Vimeo video by its numeric ID. |
| Get Video Comment | `getVideoComment` | Retrieve a single comment on a video by its comment ID. |
| Get Video Credit | `getVideoCredit` | Retrieve a specific credit on a video by its ID. |
| Get Video Text Track | `getTextTrack` | Retrieve a specific text track on a video by its ID. |
| Get Video Thumbnail | `getVideoThumbnail` | Retrieve a specific thumbnail image on a video by its picture ID. |
| Like Video | `likeVideo` | Add a video to the authenticated user's likes. |
| List Categories | `listCategories` | List all top-level content categories on Vimeo. |
| List Category Channels | `listCategoryChannels` | List the channels associated with a specific content category. |
| List Category Groups | `listCategoryGroups` | List the groups associated with a specific content category. |
| List Category Videos | `listCategoryVideos` | List the videos featured in a specific content category. |
| List Channel Videos | `listChannelVideos` | List the videos in a specific channel. |
| List Channels | `listChannels` | List or search all public channels on Vimeo. |
| List Comment Replies | `listCommentReplies` | List the replies to a specific comment on a video. |
| List Current User Followers | `listUserFollowers` | List the users who follow the authenticated Vimeo user. |
| List Current User Following | `listUserFollowing` | List the users that the authenticated Vimeo user is following. |
| List Folder Videos | `listFolderVideos` | List the videos contained in a folder (project) owned by the authenticated Vimeo user. |
| List Folders | `listFolders` | List the folders (projects) belonging to the authenticated Vimeo user. |
| List Followed Categories | `listMyCategories` | List the content categories that the authenticated user follows. |
| List Followed Channels | `listMyChannels` | List the channels that the authenticated user follows or moderates. |
| List Group Videos | `listGroupVideos` | List the videos that have been added to a specific group. |
| List Groups | `listGroups` | List or search all public groups on Vimeo. |
| List Joined Groups | `listMyGroups` | List the groups that the authenticated Vimeo user has joined. |
| List My Liked Videos | `listMyLikes` | List the videos that the authenticated user has liked. |
| List My Videos | `listMyVideos` | List the videos belonging to the authenticated Vimeo user, with optional search, sort, and paging. |
| List On Demand Pages | `listOnDemandPages` | List the Vimeo On Demand pages belonging to the authenticated user. On Demand requires a paid Vimeo plan. |
| List On Demand Purchases | `listMyPurchases` | List the Vimeo On Demand videos that the authenticated user has purchased or rented. |
| List Portfolio Videos | `listPortfolioVideos` | List the videos contained in a portfolio owned by the authenticated Vimeo user. Needs a paid Vimeo plan (Vimeo help: portfolios need Standard/Pro or higher) and an existing portfolio made in the Vimeo web interface; the API cannot create one. |
| List Portfolios | `listPortfolios` | List the portfolios belonging to the authenticated Vimeo user. Portfolios are created in the Vimeo web interface, not via the API. |
| List Showcase Videos | `listShowcaseVideos` | List the videos contained in a showcase (album) owned by the authenticated user. |
| List Showcases | `listShowcases` | List the showcases (albums) belonging to the authenticated Vimeo user. |
| List User Appearances | `listUserAppearances` | List the videos in which the authenticated Vimeo user has been credited as cast or crew. |
| List User Portraits | `listUserPortraits` | List the portrait images (profile pictures) belonging to the authenticated Vimeo user. |
| List User Videos | `getUserVideos` | List the public videos belonging to a specific Vimeo user by their numeric ID. |
| List Video Comments | `listVideoComments` | List the comments on a specific video. |
| List Video Credits | `listVideoCredits` | List the cast and crew credited on a video. |
| List Video Likes | `listVideoLikes` | List the users who have liked a specific video. |
| List Video Privacy Domains | `listVideoPrivacyDomains` | List the domains on which a video with whitelist embed privacy is allowed to be embedded. Needs a paid Vimeo plan (free accounts get 403, error_code 3202). |
| List Video Privacy Users | `listVideoPrivacyUsers` | List the users granted access to a video whose view privacy is restricted to specific users. Needs a paid Vimeo plan (user-restricted privacy is not available on free accounts). |
| List Video Tags | `listVideoTags` | List all tags applied to a specific video. |
| List Video Text Tracks | `listTextTracks` | List the text tracks (captions and subtitles) attached to a video. |
| List Video Thumbnails | `listVideoThumbnails` | List the thumbnail images (pictures) associated with a video. |
| List Videos With Tag | `listVideosWithTag` | List public videos that have been tagged with a specific tag word. |
| List Watch Later | `listWatchLater` | List the videos in the authenticated user's Watch Later queue. |
| Remove From Watch Later | `removeFromWatchLater` | Remove a video from the authenticated user's Watch Later queue. |
| Remove Video From Channel | `removeVideoFromChannel` | Remove a video from a channel that the authenticated user moderates. |
| Remove Video From Folder | `removeVideoFromFolder` | Remove a video from a folder (project) owned by the authenticated Vimeo user. The video itself is not deleted. |
| Remove Video From Group | `removeVideoFromGroup` | Remove a video from a group on Vimeo. |
| Remove Video From Portfolio | `removeVideoFromPortfolio` | Remove a video from a portfolio owned by the authenticated Vimeo user. Needs a paid Vimeo plan (Vimeo help: portfolios need Standard/Pro or higher) and an existing portfolio made in the Vimeo web interface; the API cannot create one. |
| Remove Video From Showcase | `removeVideoFromShowcase` | Remove a video from a showcase (album) owned by the authenticated user. |
| Remove Video Privacy Domain | `removeVideoPrivacyDomain` | Disallow embedding a video on the specified whitelisted domain. Needs a paid Vimeo plan (free accounts get 403, error_code 3202). |
| Remove Video Privacy User | `removeVideoPrivacyUser` | Revoke a specific user's access to a view-restricted video. Needs a paid Vimeo plan (user-restricted privacy is not available on free accounts). |
| Remove Video Tag | `removeVideoTag` | Remove a tag from a video. |
| Reply To Comment | `replyToComment` | Post a reply to an existing comment on a video. |
| Search Users | `searchUsers` | Search the Vimeo user directory by keyword and return matching users. |
| Search Videos | `searchVideos` | Search all public videos on Vimeo by keyword. |
| Set User Portrait Active | `setUserPortrait` | Update a portrait image of the authenticated user, typically to make it the active profile picture. |
| Set Video Thumbnail Active | `setVideoThumbnail` | Update a video thumbnail, typically to make it the active thumbnail for the video. |
| Unfollow User | `unfollowUser` | Make the authenticated Vimeo user stop following another user by their numeric user ID. |
| Unlike Video | `unlikeVideo` | Remove a video from the authenticated user's likes. |
