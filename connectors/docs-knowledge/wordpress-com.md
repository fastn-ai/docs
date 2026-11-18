---
description: "WordPress.com is Automattic's hosted WordPress platform."
---

# WordPress.com

WordPress.com is Automattic's hosted WordPress platform. This connector covers the WordPress.com REST API v1.1 at public-api.wordpress.com, which also serves Jetpack-connected self-hosted WordPress sites: posts and pages, media library, comments and comment likes, categories, tags and custom taxonomy terms, navigation menus, widgets, site users and invites, site information and metadata, site and email statistics, followers and post subscribers, Publicize and Keyring social connections, sharing buttons, the Reader, notifications and the authenticated user's account.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [wordpress.com](https://wordpress.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 340 |
| **Events** | 0 |
| **Slug** | `wordpressCom` |

## Use it

Add WordPress.com from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wordpressCom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept WordAds Terms Of Service | `acceptWordAdsTos` | Records acceptance of the WordAds terms of service for a site. |
| Activate Site Widget | `activateSiteWidget` | Activate a widget on a site. |
| Attach SSH Key | `attachSshKey` | Attaches an SSH public key from the authenticated user's account to a site. `name` must be the name of a key already saved on the account. Requires a WordPress.com plan that includes SSH access. |
| Create Category | `createCategory` | Creates a new category on a site. `name` is required; the API returns `invalid_input "Unknown data passed"` if no recognised field is sent. |
| Create Category (Core) | `createCategoryCore` | Creates a category term through the WordPress core REST API. |
| Create Code Deployment | `createCodeDeployment` | Creates or updates a GitHub code deployment configuration for a site. Requires `installation_id` and `external_repository_id` from List GitHub Repositories. Requires a WordPress.com plan that includes GitHub Deployments. |
| Create Comment (Core) | `createCommentCore` | Creates a comment on a post through the WordPress core REST API. |
| Create Comment On Post | `createCommentOnPost` | Creates a comment on a post. `content` is required; the API returns `invalid_input "Invalid request input"` when it is missing. |
| Create Font Family | `createFontFamily` | Installs a font family on a site. `font_family_settings` must be a JSON-encoded string. |
| Create Menu (Core) | `createMenuCore` | Creates a navigation menu through the WordPress core REST API. |
| Create Menu Item | `createMenuItem` | Adds an item to a navigation menu. |
| Create Navigation Menu | `createNavigationMenu` | Create a new navigation menu. |
| Create Navigation Menu (Core) | `createNavigationMenuCore` | Creates a block-theme navigation menu. |
| Create Page | `createPage` | Creates a page. Use `status` `draft` to save without publishing, and `parent` to nest it under another page. |
| Create Post | `createPost` | Creates a new post or page on a site. Supply at least one of `title`, `content` or `excerpt` - the API returns `invalid_input "Invalid request input"` for an empty body. Set `status` to `draft` to save without publishing, and use `type` to create a page instead of a post. |
| Create Post (Core) | `createPostCore` | Creates a post through the WordPress core REST API. Use `status` `draft` to save without publishing. |
| Create Profile Link | `createProfileLink` | Adds a link to the authenticated user's public profile. The API expects an object with at least a `value` key holding the URL. |
| Create Reusable Block | `createReusableBlock` | Creates a reusable (synced pattern) block. |
| Create Site Publicize Connection | `createSitePublicizeConnection` | Create a new publicize connection that is associated with the specified site. |
| Create SSH User | `createSshUser` | Creates an SSH user for a site and returns the generated password. Requires a WordPress.com plan that includes SSH access. |
| Create Staging Site | `createStagingSite` | Creates a staging site for an existing production site. Requires a WordPress.com plan that includes staging sites. |
| Create Tag | `createTag` | Creates a new tag on a site. `name` is required; the API returns `invalid_input "Unknown data passed"` if no recognised field is sent. |
| Create Tag (Core) | `createTagCore` | Creates a tag term through the WordPress core REST API. |
| Create Taxonomy Term | `createTaxonomyTerm` | Creates a new term in any taxonomy, including custom taxonomies. `name` is required; the API returns `invalid_input "Unknown data passed"` if no recognised field is sent. |
| Create User (Core) | `createUserCore` | Creates a user on a site through the WordPress core REST API. `username`, `email` and `password` are all required and the email must be a valid address. On WordPress.com, user creation is normally performed through Invite Users To Site instead. |
| Create Widget (Core) | `createWidgetCore` | Places a new widget instance into a sidebar. |
| Deactivate Site Widget | `deactivateSiteWidget` | Deactivate a widget on a site by its ID. Will delete if already deactivated. |
| Delete Category | `deleteCategory` | Deletes a category from a site. |
| Delete Category (Core) | `deleteCategoryCore` | Deletes a category term. `force` must be true because terms are not trashed. |
| Delete Code Deployment | `deleteCodeDeployment` | Deletes a GitHub code deployment configuration from a site. Requires a WordPress.com plan that includes GitHub Deployments. |
| Delete Comment | `deleteComment` | Delete a comment. |
| Delete Comment (Core) | `deleteCommentCore` | Moves a comment to the trash, or deletes it permanently when `force` is true. |
| Delete Font Face | `deleteFontFace` | Removes a font face from a font family. `force` must be true. |
| Delete Font Family | `deleteFontFamily` | Removes an installed font family. `force` must be true. |
| Delete Keyring Connection | `deleteKeyringConnection` | Delete the Keyring connection (and associated token) with the provided ID. Also deletes all associated publicize connections. |
| Delete Media | `deleteMedia` | Delete a piece of media. Note: Media is deleted and not trashed. |
| Delete Media (Core) | `deleteMediaCore` | Permanently deletes a media library item. Media is never trashed, so `force` must be true. |
| Delete Menu (Core) | `deleteMenuCore` | Deletes a navigation menu. `force` must be true because menus are not trashed. |
| Delete Menu Item | `deleteMenuItem` | Deletes a navigation menu item. `force` must be true. |
| Delete Multiple Posts | `deleteMultiplePosts` | Deletes multiple posts in one call. `post_ids` is required. If the trash is enabled, non-trashed posts are moved to the trash and trashed posts are permanently deleted. |
| Delete My Publicize Connection | `deleteMyPublicizeConnection` | Delete the specified publicize connection. |
| Delete Navigation Menu | `deleteNavigationMenu` | Delete a navigation menu. |
| Delete Navigation Menu (Core) | `deleteNavigationMenuCore` | Moves a block-theme navigation menu to the trash, or deletes it permanently when `force` is true. |
| Delete Page | `deletePage` | Moves a page to the trash, or deletes it permanently when `force` is true. |
| Delete Page Revision | `deletePageRevision` | Permanently deletes a stored revision of a page. |
| Delete Plugin | `deletePlugin` | Uninstalls a plugin from a site. The plugin must be inactive. |
| Delete Post | `deletePost` | Delete a post. Note: If the trash is enabled, this request will send the post to the trash. A second request will permanently delete the post. |
| Delete Post (Core) | `deletePostCore` | Moves a post to the trash, or deletes it permanently when `force` is true. |
| Delete Post Revision | `deletePostRevision` | Permanently deletes a stored revision of a post. |
| Delete Profile Link | `deleteProfileLink` | Delete a link from current user’s profile. |
| Delete Reusable Block | `deleteReusableBlock` | Deletes a reusable block. |
| Delete Reusable Block Revision | `deleteReusableBlockRevision` | Permanently deletes a stored revision of a reusable block. |
| Delete Site Publicize Connection | `deleteSitePublicizeConnection` | Delete the specified publicize connection. |
| Delete Staging Site | `deleteStagingSite` | Deletes the staging site associated with a production site. Requires a WordPress.com plan that includes staging sites. |
| Delete Tag | `deleteTag` | Deletes a tag from a site. Posts that used the tag keep their content but lose the tag. |
| Delete Tag (Core) | `deleteTagCore` | Deletes a tag term. `force` must be true because terms are not trashed. |
| Delete Taxonomy Term | `deleteTaxonomyTerm` | Deletes a term from a taxonomy on a site. |
| Delete User (Core) | `deleteUserCore` | Removes a user from the site. Requires `force` and a `reassign` target for their content. |
| Delete Video Track | `deleteVideoTrack` | Deletes a subtitle or caption track from a VideoPress video. |
| Delete Widget (Core) | `deleteWidgetCore` | Removes a widget instance. `force` must be true to delete rather than move it to the inactive sidebar. |
| Detach SSH Key | `detachSshKey` | Detaches an SSH public key from a site. Requires a WordPress.com plan that includes SSH access. |
| Edit Media File | `editMediaFile` | Replaces the file behind an existing media item using a public URL supplied in `media_url`, and updates its metadata. |
| Edit Media Image | `editMediaImage` | Applies image edits such as rotation and cropping to a media item and stores the result as a new attachment. |
| Encode Widget Type Form | `encodeWidgetTypeForm` | Encodes a widget type form submission into the instance settings the widget endpoints accept. |
| Follow Reader Feed | `followReaderFeed` | Follow the specified blog. |
| Follow Site | `followSite` | Makes the authenticated user follow the specified site. Returns `follow_failed` if the site cannot be followed. |
| Get Account Preferences | `getAccountPreferences` | Retrieves the authenticated user's stored application preferences. |
| Get Account Settings | `getAccountSettings` | Get the current user’s settings. |
| Get Automated Transfer Status | `getAutomatedTransferStatus` | Returns the current status of Automated Transfer for a site. |
| Get Category | `getCategory` | Get information about a single category. |
| Get Category (Core) | `getCategoryCore` | Retrieves a single category term by its numeric ID. |
| Get Code Deployment Run Logs | `getCodeDeploymentRunLogs` | Retrieves the log output produced by a single code deployment run. Requires a WordPress.com plan that includes GitHub Deployments. |
| Get Comment | `getComment` | Retrieves a single comment on a site by its comment ID. |
| Get Comment (Core) | `getCommentCore` | Retrieves a single comment by its ID. |
| Get Comment Counts | `getCommentCounts` | Get comment counts for each available status. |
| Get Comment History | `getCommentHistory` | Get the audit history for given comment. |
| Get Connected Application | `getConnectedApplication` | Get one of current user’s connected applications. |
| Get Current User | `getCurrentUser` | Get metadata about the current user. |
| Get Current User (Core) | `getCurrentUserCore` | Retrieves the profile of the authenticated user on this site. |
| Get External Service | `getExternalService` | Get information about a single external service that WordPress.com or Jetpack sites can integrate with via keyring. |
| Get Font Face | `getFontFace` | Retrieves a single font face of a font family. |
| Get Font Family | `getFontFamily` | Retrieves a single installed font family. |
| Get Insight | `getInsight` | Get raw data for a particular graph. |
| Get Keyring Connection | `getKeyringConnection` | Get a single Keyring connection that the current user has setup. |
| Get Media | `getMedia` | Get a single media item (by ID). |
| Get Media (Core) | `getMediaCore` | Retrieves a single media library item through the WordPress core REST API. |
| Get Menu (Core) | `getMenuCore` | Retrieves a single navigation menu by its term ID. |
| Get Menu Item | `getMenuItem` | Retrieves a single navigation menu item. |
| Get Menu Location | `getMenuLocation` | Retrieves a single navigation menu location registered by the active theme. |
| Get My Comment Like Status | `getMyCommentLikeStatus` | Get your like status for a comment. |
| Get My Post Like Status | `getMyPostLikeStatus` | Get the current user’s like status for a post. |
| Get My Post Subscription | `getMyPostSubscription` | Get subscription status of the specified post for the current user. |
| Get My Publicize Connection | `getMyPublicizeConnection` | Get a single publicize connection that the current user has set up. |
| Get My Reader Tag Subscription | `getMyReaderTagSubscription` | Retrieves whether the authenticated user is subscribed to a Reader tag. `tagSlug` must be an existing tag slug; the API returns `invalid_tag` otherwise. |
| Get My Reblog Status | `getMyReblogStatus` | Get reblog status for a post. |
| Get My Site Follow Status | `getMySiteFollowStatus` | Get blog following status for the current user. |
| Get Navigation Menu | `getNavigationMenu` | Get a single navigation menu. |
| Get Navigation Menu (Core) | `getNavigationMenuCore` | Retrieves a single block-theme navigation menu. |
| Get Page | `getPage` | Retrieves a single page by its ID. |
| Get Page Revision | `getPageRevision` | Retrieves a single stored revision of a page. |
| Get Plugin | `getPlugin` | Retrieves a single installed plugin by its plugin file path. |
| Get Post | `getPost` | Get a single post (by ID). |
| Get Post (Core) | `getPostCore` | Retrieves a single post through the WordPress core REST API. |
| Get Post By Slug | `getPostBySlug` | Get a single post (by slug). |
| Get Post Counts By Status | `getPostCountsByStatus` | Get number of posts in the post type groups by post status. |
| Get Post Revision | `getPostRevision` | Retrieves a single stored revision of a post. |
| Get Post Status | `getPostStatus` | Retrieves the definition of a single registered post status. |
| Get Post Type (Core) | `getPostTypeCore` | Retrieves the definition of a single registered post type. |
| Get Reader Email Settings | `getReaderEmailSettings` | Returns the email settings. |
| Get Reader Feed | `getReaderFeed` | Get details about a feed. |
| Get Reader Menu | `getReaderMenu` | Get default reader menu. |
| Get Reader Post | `getReaderPost` | Get a single post (by ID). |
| Get Reader Subscriptions Count | `getReaderSubscriptionsCount` | Returns the number of blog, comment and pending subscriptions. |
| Get Reader Tag | `getReaderTag` | Get details about a specified tag. |
| Get Reusable Block | `getReusableBlock` | Retrieves a single reusable block by its ID. |
| Get Reusable Block Revision | `getReusableBlockRevision` | Retrieves a single stored revision of a reusable block. |
| Get Sidebar | `getSidebar` | Retrieves a single widget area and the widgets it contains. |
| Get Site | `getSite` | Get information about a site. |
| Get Site Header Options | `getSiteHeaderOptions` | Get the custom header options for a site. |
| Get Site Publicize Connection | `getSitePublicizeConnection` | Get a single publicize connection that is associated with the specified site. |
| Get Site Settings | `getSiteSettings` | Retrieves the general settings of a site, including title, tagline, timezone, date format and default category. |
| Get Site Stats | `getSiteStats` | Get a site’s stats. |
| Get Site User By Login | `getSiteUserByLogin` | Get details of a user of a site by login. |
| Get Site Widget | `getSiteWidget` | Retrieve a widget on a site by its ID. |
| Get SSH Access Setting | `getSshAccessSetting` | Retrieves the SSH access mode configured for a site. Requires a WordPress.com plan that includes SSH access. |
| Get Staging Site | `getStagingSite` | Retrieves the staging site associated with a production site. Requires a WordPress.com plan that includes staging sites. |
| Get Stats By UTM Parameter | `getStatsByUtmParameter` | Fetch site’s UTM param statistics. |
| Get Stats Clicks | `getStatsClicks` | View a site’s outbound clicks. |
| Get Stats Comment Followers | `getStatsCommentFollowers` | View a site’s comment followers. |
| Get Stats Comments | `getStatsComments` | View a site’s top comment authors and most-commented posts. |
| Get Stats Country Views | `getStatsCountryViews` | View a site’s views by country. |
| Get Stats Email Click Rate | `getStatsEmailClickRate` | Retrieves the email click-through rate for a post. The WordPress.com documentation notes that this endpoint returns mock data. |
| Get Stats Email Clicks By Client | `getStatsEmailClicksByClient` | View email clicks by client. |
| Get Stats Email Clicks By Country | `getStatsEmailClicksByCountry` | View email clicks by country. |
| Get Stats Email Clicks By Device | `getStatsEmailClicksByDevice` | View email clicks by device. |
| Get Stats Email Clicks By Link | `getStatsEmailClicksByLink` | View email clicks by link. |
| Get Stats Email Clicks By Post | `getStatsEmailClicksByPost` | View chart stats related to email clicks by period. |
| Get Stats Email Clicks By User Content Link | `getStatsEmailClicksByUserContentLink` | View email clicks by user content link. |
| Get Stats Email Clicks Summary | `getStatsEmailClicksSummary` | View the total number of email clicks for each post. |
| Get Stats Email Open Rate | `getStatsEmailOpenRate` | View email opens rate by post. |
| Get Stats Email Opens By Client | `getStatsEmailOpensByClient` | View email opens stats by client. |
| Get Stats Email Opens By Country | `getStatsEmailOpensByCountry` | View email opens stats by country. |
| Get Stats Email Opens By Device | `getStatsEmailOpensByDevice` | View email opens stats by device. |
| Get Stats Email Opens By Post | `getStatsEmailOpensByPost` | View multiple stats related to email opens by post. |
| Get Stats Email Opens Summary | `getStatsEmailOpensSummary` | View the total number of email opens for each post. |
| Get Stats Email Summary | `getStatsEmailSummary` | View the total number of email opens and clicks for each post. |
| Get Stats File Downloads | `getStatsFileDownloads` | View a site’s file downloads. |
| Get Stats Followers | `getStatsFollowers` | View a site’s followers. |
| Get Stats Highlights | `getStatsHighlights` | View highlight metrics from the last seven days. |
| Get Stats Post Views | `getStatsPostViews` | View a post’s views. |
| Get Stats Posting Streak | `getStatsPostingStreak` | Get stats for Calendar Heatmap. Returns data with each post timestamp. |
| Get Stats Publicize Followers | `getStatsPublicizeFollowers` | View a site’s publicize follower counts. |
| Get Stats Referrers | `getStatsReferrers` | View a site’s referrers. |
| Get Stats Search Terms | `getStatsSearchTerms` | View search terms used to find the site. |
| Get Stats Summary | `getStatsSummary` | View a site’s summarized views, visitors, likes and comments. |
| Get Stats Tags And Categories | `getStatsTagsAndCategories` | View a site’s views by tags and categories. |
| Get Stats Top Authors | `getStatsTopAuthors` | View a site’s top authors. |
| Get Stats Top Posts | `getStatsTopPosts` | View a site’s top posts and pages by views. |
| Get Stats Top Posts By UTM Parameter | `getStatsTopPostsByUtmParameter` | Fetch top posts for a given UTM parameter value. |
| Get Stats Video Details | `getStatsVideoDetails` | View the details of a single video. |
| Get Stats Video Plays | `getStatsVideoPlays` | View a site’s video plays. |
| Get Stats Views By Post | `getStatsViewsByPost` | View the total number of views for each post. |
| Get Tag | `getTag` | Get information about a single tag. |
| Get Tag (Core) | `getTagCore` | Retrieves a single tag term by its numeric ID. |
| Get Taxonomy (Core) | `getTaxonomyCore` | Retrieves the definition of a single registered taxonomy. |
| Get Taxonomy Term | `getTaxonomyTerm` | Get information about a single term. |
| Get Theme | `getTheme` | Retrieves a single installed theme by its stylesheet directory name. |
| Get Theme Header Options | `getThemeHeaderOptions` | Get the custom header options for a site with a particular theme. |
| Get Two Step Configuration | `getTwoStepConfiguration` | Get information about current user’s two factor configuration. |
| Get User (Core) | `getUserCore` | Retrieves a single user by numeric ID. |
| Get Video | `getVideo` | Retrieves the metadata for a VideoPress video. VideoPress requires an eligible WordPress.com plan. |
| Get Video Chapters | `getVideoChapters` | Retrieves the chapter markers defined for a VideoPress video. |
| Get Video Playlist | `getVideoPlaylist` | Retrieves the streaming playlist for a VideoPress video in the requested format. |
| Get Video Poster | `getVideoPoster` | Retrieves the poster image for a VideoPress video. |
| Get Widget (Core) | `getWidgetCore` | Retrieves a single widget instance by its ID. |
| Get Widget Type | `getWidgetType` | Retrieves the definition of a single widget type. |
| Get WordAds Earnings | `getWordAdsEarnings` | Retrieves WordAds earnings for a site. Requires an eligible WordPress.com plan with WordAds enabled. |
| Get WordAds Settings | `getWordAdsSettings` | Retrieves the WordAds advertising settings for a site. Requires an eligible WordPress.com plan with WordAds enabled. |
| Get WordAds Stats | `getWordAdsStats` | Retrieves WordAds impression and revenue statistics for a site. Requires an eligible WordPress.com plan with WordAds enabled. |
| Get WordAds Terms Of Service Status | `getWordAdsTosStatus` | Retrieves whether the site owner has accepted the WordAds terms of service. |
| Install Plugin | `installPlugin` | Installs a plugin from the WordPress.org directory. Requires a WordPress.com plan that allows plugin management. |
| Invite Users To Site | `inviteUsersToSite` | Invite one or more users to your site. |
| Like Comment | `likeComment` | Like a comment. |
| Like Post | `likePost` | Adds the authenticated user's like to a post. |
| List Agency Pending Sites | `listAgencyPendingSites` | Lists the agency sites that are provisioned and awaiting assignment. `agencyId` must be a real agency ID; the API rejects it with `rest_invalid_param` for accounts outside the Automattic for Agencies programme. |
| List Agency Sites | `listAgencySites` | Lists the sites managed by a WordPress.com agency. `agencyId` must be a real agency ID; the API rejects it with `rest_invalid_param` for accounts that are not part of the Automattic for Agencies programme. |
| List Available Sharing Services | `listAvailableSharingServices` | Get a list of external services for which sharing buttons are supported. |
| List Billing History | `listBillingHistory` | Get list of current user’s billing history and upcoming charges. |
| List Block Pattern Categories | `listBlockPatternCategories` | Lists the block pattern categories available to a site. |
| List Block Patterns | `listBlockPatterns` | Lists the block patterns registered for a site. |
| List Block Types | `listBlockTypes` | Lists the block types registered on a site. |
| List Block Types By Namespace | `listBlockTypesByNamespace` | Lists the block types registered under a single namespace, for example `core`. |
| List Categories | `listCategories` | Get a list of a site’s categories. |
| List Categories (Core) | `listCategoriesCore` | Lists category terms through the WordPress core REST API. |
| List Code Deployment Runs | `listCodeDeploymentRuns` | Lists the runs of a GitHub code deployment. Requires a WordPress.com plan that includes GitHub Deployments. |
| List Code Deployments | `listCodeDeployments` | Lists the GitHub code deployments configured for a site. Requires a WordPress.com plan that includes GitHub Deployments. |
| List Comment Likes | `listCommentLikes` | Get the likes for a comment. |
| List Comments | `listComments` | Get a list of recent comments. |
| List Comments (Core) | `listCommentsCore` | Lists comments through the WordPress core REST API, with core filters and pagination. |
| List Connected Applications | `listConnectedApplications` | Get current user’s connected applications. |
| List External Services | `listExternalServices` | Get a list of third-party services that WordPress.com or Jetpack sites can integrate with via keyring. |
| List Font Collections | `listFontCollections` | Lists the font collections available to a site. |
| List Font Faces | `listFontFaces` | Lists the font faces belonging to a font family. |
| List Font Families | `listFontFamilies` | Lists the font families installed on a site. |
| List Freshly Pressed Posts | `listFreshlyPressedPosts` | Retrieves the Freshly Pressed post list. WordPress.com has retired the Freshly Pressed editorial feature, so this endpoint is kept for compatibility and may return an empty list. |
| List GitHub Installations | `listGithubInstallations` | Lists the GitHub App installations the authenticated WordPress.com user can deploy from. |
| List GitHub Repositories | `listGithubRepositories` | Lists the repositories available in a GitHub App installation, with the `external_repository_id` values used when creating a code deployment. `installation_id` comes from List GitHub Installations. |
| List Insights | `listInsights` | Get a list of stats/metrics/insights that the current user has access to. |
| List Keyring Connections | `listKeyringConnections` | Get a list of all the keyring connections associated with the current user. |
| List Media | `listMedia` | Get a list of items in the media library. |
| List Media (Core) | `listMediaCore` | Lists media library items through the WordPress core REST API. |
| List Menu Items | `listMenuItems` | Lists the items belonging to the navigation menus of a site. |
| List Menu Locations | `listMenuLocations` | Lists the navigation menu locations registered by the active theme. |
| List Menus (Core) | `listMenusCore` | Lists the navigation menus of a site through the WordPress core REST API. |
| List My Liked Posts | `listMyLikedPosts` | Get a list of the current user’s likes. |
| List My Posts | `listMyPosts` | Get a list of posts across all the user’s sites. |
| List My Publicize Connections | `listMyPublicizeConnections` | Get a list of publicize connections that the current user has set up. |
| List My Sites | `listMySites` | Get a list of the current user’s sites. |
| List My Sites Features | `listMySitesFeatures` | Get a list of the current user’s sites features. |
| List My Sites Plugins | `listMySitesPlugins` | Get a list of the current user’s sites plugins. |
| List Navigation Menus | `listNavigationMenus` | Get a list of all navigation menus. |
| List Navigation Menus (Core) | `listNavigationMenusCore` | Lists the block-theme navigation menus stored on a site. |
| List Page Revisions | `listPageRevisions` | Lists the stored revisions of a page. |
| List Page Templates | `listPageTemplates` | Get a list of page templates supported by a site. |
| List Pages | `listPages` | Lists the pages on a site, with the full set of core filters, ordering and pagination. |
| List Pages For Dropdown | `listPagesForDropdown` | Get a list of pages to be displayed as options in a select-a-page-dropdown. |
| List Plugins | `listPlugins` | Lists the plugins installed on a site. On WordPress.com this requires a plan that allows plugin management. |
| List Post Comments | `listPostComments` | Get a list of recent comments on a post. |
| List Post Likes | `listPostLikes` | Get a list of the likes for a post. |
| List Post Revisions | `listPostRevisions` | Lists the stored revisions of a post. |
| List Post Statuses | `listPostStatuses` | Lists the post statuses registered on a site. |
| List Post Subscribers | `listPostSubscribers` | Get a list of the specified post’s subscribers. |
| List Post Type Taxonomies | `listPostTypeTaxonomies` | Get a list of taxonomies associated with a post type. |
| List Post Types | `listPostTypes` | Get a list of post types available for a site. |
| List Post Types (Core) | `listPostTypesCore` | Lists the post types registered on a site and the capabilities of each. |
| List Posts | `listPosts` | Get a list of matching posts. |
| List Posts (Core) | `listPostsCore` | Lists posts through the WordPress core REST API, with the full set of core filters, ordering and pagination. |
| List Profile Links | `listProfileLinks` | Get current user’s profile links. |
| List Reader Feed Subscriptions | `listReaderFeedSubscriptions` | Get a list of the feeds the user is following. |
| List Reader Following Posts | `listReaderFollowingPosts` | Get a list of posts from the blogs a user follows. |
| List Reader Liked Posts | `listReaderLikedPosts` | Get a list of posts from the blogs a user likes. |
| List Reader Recommendations | `listReaderRecommendations` | Get a list of blog recommendations for the current user. |
| List Reader Tag Posts | `listReaderTagPosts` | Lists posts published under a Reader tag. `tagSlug` must be an existing tag slug; the API returns `invalid_tag` otherwise. |
| List Reader Tag Subscriptions | `listReaderTagSubscriptions` | Get a list of tags subscribed to by the user. |
| List Reader Tags Alphabetically | `listReaderTagsAlphabetically` | Get a filtered list of top tags, grouped by letter. |
| List Reader Trending Tags | `listReaderTrendingTags` | Get a list of trending tags. |
| List Reusable Block Revisions | `listReusableBlockRevisions` | Lists the stored revisions of a reusable block. |
| List Reusable Blocks | `listReusableBlocks` | Lists the reusable (synced pattern) blocks saved on a site. |
| List Sharing Buttons | `listSharingButtons` | Get a list of a site’s sharing buttons. |
| List Sidebars | `listSidebars` | Lists the widget areas (sidebars) registered by the active theme. |
| List Site Followers | `listSiteFollowers` | List a site’s followers in reverse chronological order. |
| List Site Publicize Connections | `listSitePublicizeConnections` | Get a list of publicize connections that are associated with the specified site. |
| List Site Users | `listSiteUsers` | List the users of a site. |
| List Site Widgets | `listSiteWidgets` | Retrieve the active and inactive widgets for a site. |
| List SSH Keys | `listSshKeys` | Lists the SSH public keys attached to a site. Requires a WordPress.com plan that includes SSH access. |
| List SSH Users | `listSshUsers` | Lists the SSH users configured for a site. Requires a WordPress.com plan that includes SSH access. |
| List Supported Embeds | `listSupportedEmbeds` | Get a list of embeds available on a site. Note: The current user must have publishing access. |
| List Supported Shortcodes | `listSupportedShortcodes` | Get a list of shortcodes available on a site. Note: The current user must have publishing access. |
| List Tags | `listTags` | Get a list of a site’s tags. |
| List Tags (Core) | `listTagsCore` | Lists tag terms through the WordPress core REST API. |
| List Taxonomies (Core) | `listTaxonomiesCore` | Lists the taxonomies registered on a site and the capabilities of each. |
| List Taxonomy Terms | `listTaxonomyTerms` | Get a list of a site’s terms by taxonomy. |
| List Themes | `listThemes` | Lists the themes installed on a site. On WordPress.com this requires a plan that allows theme management. |
| List Users (Core) | `listUsersCore` | Lists the users of a site through the WordPress core REST API. |
| List Widget Types | `listWidgetTypes` | Lists the widget types available on a site. |
| List Widgets (Core) | `listWidgetsCore` | Lists the widget instances placed in a site’s sidebars. |
| Mark Notifications Read | `markNotificationsRead` | Marks a set of notifications as read. `counts` is a map of note ID to the number of unread items to clear; the API returns `bad_request "Incorrect Parameters."` when it is missing. |
| Mark Notifications Seen | `markNotificationsSeen` | Set the timestamp of the most recently seen notification. |
| Post Process Media | `postProcessMedia` | Runs a post-processing action, such as generating missing image sub-sizes, on a media item. |
| Provision Agency Site | `provisionAgencySite` | Provisions a new site for a WordPress.com agency. Both `agencyId` and `siteId` must be real agency-owned IDs; the API rejects them with `rest_invalid_param` for accounts outside the Automattic for Agencies programme. |
| Reblog Post | `reblogPost` | Reblogs a post to one of the authenticated user's own sites. |
| Remove Site User | `removeSiteUser` | Deletes or removes a user of a site. |
| Render Embed | `renderEmbed` | Get a rendered embed for a site. Note: The current user must have publishing access. |
| Render Shortcode | `renderShortcode` | Get a rendered shortcode for a site. Note: The current user must have publishing access. |
| Render Widget Type | `renderWidgetType` | Renders the front-end output of a widget type for the supplied instance settings. |
| Reply To Comment | `replyToComment` | Creates a comment as a reply to another comment. `content` is required. |
| Report Referrer As Spam | `reportReferrerAsSpam` | Report a referrer as spam. |
| Request WordAds Approval | `requestWordAdsApproval` | Requests streamlined approval to join the WordAds programme for a site. |
| Reset SSH User Password | `resetSshUserPassword` | Rotates an SSH user's password and returns the new value. Requires a WordPress.com plan that includes SSH access. |
| Restore Multiple Posts | `restoreMultiplePosts` | Restores multiple posts from the trash to their previous status. `post_ids` is required. |
| Restore Post | `restorePost` | Restore a post or page from the trash to its previous status. |
| Revoke Connected Application | `revokeConnectedApplication` | Delete one of current user’s connected application access tokens. |
| Run Batch Request | `runBatchRequest` | Runs several GET endpoints in a single request and returns their responses as an array. Supply each sub-request path in the `urls` parameter. |
| Search Block Directory | `searchBlockDirectory` | Searches the WordPress.org block directory for installable blocks. |
| Search Pattern Directory | `searchPatternDirectory` | Searches the WordPress.org pattern directory. |
| Search Reader Feeds | `searchReaderFeeds` | Get the ID and subscribe URL of one or more matching feeds by domain or URL. |
| Search Related Posts | `searchRelatedPosts` | Search within a site for related posts. |
| Search Site | `searchSite` | Search within a site using an Elasticsearch Query API. |
| Search Site Content | `searchSiteContent` | Searches across a site’s content and returns lightweight result objects. |
| Send Two Step SMS Code | `sendTwoStepSmsCode` | Sends a two-step authentication code by SMS to the authenticated user's verified phone number. |
| Subscribe To Post Comments | `subscribeToPostComments` | Subscribe current user to be notified of the specified post’s comments. |
| Subscribe To Reader Tag | `subscribeToReaderTag` | Subscribes the authenticated user to a Reader tag. `tagSlug` must be an existing tag slug; the API returns `invalid_tag` otherwise. |
| Suggest Users For Mention | `suggestUsersForMention` | Retrieves a list of users that can be suggested for @mentions. |
| Trigger Code Deployment Run | `triggerCodeDeploymentRun` | Starts a manual run of a configured GitHub code deployment. Requires a WordPress.com plan that includes GitHub Deployments. |
| Unfollow Reader Feed | `unfollowReaderFeed` | Unfollow the specified blog. |
| Unfollow Site | `unfollowSite` | Makes the authenticated user stop following the specified site. Returns `are_not_subscribed` if the user was not following it. |
| Unlike Comment | `unlikeComment` | Remove your like from a comment. |
| Unlike Post | `unlikePost` | Removes the authenticated user's like from a post. |
| Unreport Referrer As Spam | `unreportReferrerAsSpam` | Unreport a referrer as spam. |
| Unsubscribe From Post | `unsubscribeFromPost` | Unsubscribe the current user from the specified post. |
| Unsubscribe From Reader Tag | `unsubscribeFromReaderTag` | Unsubscribes the authenticated user from a Reader tag. `tagSlug` must be an existing tag slug; the API returns `invalid_tag` otherwise. |
| Update Account Preferences | `updateAccountPreferences` | Updates the authenticated user's stored application preferences. At least one preference must be supplied - the API returns `invalid_input "No preferences were provided for the endpoint to set."` for an empty body. |
| Update Account Settings | `updateAccountSettings` | Updates the authenticated user's account settings. At least one setting must be supplied - the API returns `invalid_input "No settings were provided to the endpoint to set."` for an empty body. |
| Update Category | `updateCategory` | Updates a category's name, slug, description or parent. |
| Update Category (Core) | `updateCategoryCore` | Updates a category term by its numeric ID. |
| Update Comment | `updateComment` | Updates a comment's content, author details or moderation status. |
| Update Comment (Core) | `updateCommentCore` | Updates a comment, including its content and moderation status. |
| Update Current User (Core) | `updateCurrentUserCore` | Updates the profile of the authenticated user on this site. |
| Update Media | `updateMedia` | Edit basic information about a media item. |
| Update Media (Core) | `updateMediaCore` | Updates the metadata of a media library item, such as its title, caption, alt text or description. |
| Update Menu (Core) | `updateMenuCore` | Updates a navigation menu, including its name and theme locations. |
| Update Menu Item | `updateMenuItem` | Updates a navigation menu item. |
| Update My Post Subscription | `updateMyPostSubscription` | Updates the authenticated user's comment-notification subscription for a post, for example switching between instant and daily delivery. |
| Update My Publicize Connection | `updateMyPublicizeConnection` | Update a single publicize connection belonging to the current user. |
| Update Navigation Menu | `updateNavigationMenu` | Update a navigation menu. |
| Update Navigation Menu (Core) | `updateNavigationMenuCore` | Updates a block-theme navigation menu. |
| Update Page | `updatePage` | Updates a page. Only supplied fields are changed. |
| Update Plugin Status | `updatePluginStatus` | Activates or deactivates an installed plugin by setting its `status`. |
| Update Post | `updatePost` | Updates an existing post or page. Supply at least one field to change - the API returns `invalid_input "Invalid request input"` for an empty body. Only the fields supplied are changed. |
| Update Post (Core) | `updatePostCore` | Updates a post through the WordPress core REST API. Only supplied fields are changed. |
| Update Reader Email Settings | `updateReaderEmailSettings` | Updates the authenticated user's Reader email delivery settings. Supply at least one setting; the endpoint returns HTTP 500 with an empty body when called with no parameters. |
| Update Reusable Block | `updateReusableBlock` | Updates a reusable block. |
| Update Sharing Buttons | `updateSharingButtons` | Edit all sharing buttons for a site. |
| Update Sidebar | `updateSidebar` | Updates a widget area, principally the ordered list of widgets it contains. |
| Update Site Header Options | `updateSiteHeaderOptions` | Set the custom header options for a site. |
| Update Site Publicize Connection | `updateSitePublicizeConnection` | Update a single publicize connection belonging to the specified site. |
| Update Site Settings | `updateSiteSettings` | Updates the general settings of a site. Only supplied settings are changed. |
| Update Site User | `updateSiteUser` | Update details of a user of a site. |
| Update Site Widget | `updateSiteWidget` | Update a widget on a site by its ID. |
| Update SSH Access Setting | `updateSshAccessSetting` | Sets the SSH access mode for a site. `setting` accepts `ssh` or `sftp`. Requires a WordPress.com plan that includes SSH access. |
| Update Tag | `updateTag` | Updates a tag's name, slug or description. |
| Update Tag (Core) | `updateTagCore` | Updates a tag term by its numeric ID. |
| Update Taxonomy Term | `updateTaxonomyTerm` | Updates a term in any taxonomy, including custom taxonomies. |
| Update User (Core) | `updateUserCore` | Updates a user profile by numeric ID. |
| Update Video Poster | `updateVideoPoster` | Sets the poster image for a VideoPress video from an uploaded frame or supplied timestamp. |
| Update Widget (Core) | `updateWidgetCore` | Updates a widget instance, including its settings and sidebar placement. |
| Update WordAds Settings | `updateWordAdsSettings` | Updates the WordAds advertising settings for a site. Requires an eligible WordPress.com plan with WordAds enabled. |
| Upload Media | `uploadMedia` | Adds one or more items to a site's media library by sideloading them from public URLs supplied in `media_urls`. Direct binary multipart upload is not supported through this connector. |
| Upload Video Track | `uploadVideoTrack` | Uploads a subtitle or caption track for a VideoPress video. |
| Validate Password Strength | `validatePasswordStrength` | Checks the strength of a candidate password for the authenticated user's account without changing it. |
