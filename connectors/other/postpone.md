---
description: "Postpone is a social media scheduling and analytics platform for creators, brands and agencies, covering Reddit, Twitter/X, Instagram, Facebook, TikTok,…"
---

# Postpone

Postpone is a social media scheduling and analytics platform for creators, brands and agencies, covering Reddit, Twitter/X, Instagram, Facebook, TikTok, YouTube, LinkedIn, Pinterest, Threads, Bluesky, Tumblr and Mastodon. This connector wraps the Postpone public GraphQL API at https://api.postpone.app/gql: content library and media uploads, post tags, campaigns, post templates, scheduling and managing posts on every supported platform, and post/account analytics.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [postpone.app](https://postpone.app) |
| **Authentication** | API key |
| **Actions** | 151 |
| **Events** | 0 |
| **Slug** | `postpone` |

## Use it

Add Postpone from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.postpone.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Acknowledge Submission Errors | `acknowledgeSubmissionErrors` | Dismiss the error state on the given posts or submissions so they no longer appear in the failed list. |
| Add Moderator Alert | `addModAlert` | Add a Reddit moderator username to the alert list, so Postpone flags posts removed by that moderator. |
| Archive Post Tag | `archivePostTag` | Archive a post tag so it is hidden from the active tag list while remaining on historical posts. |
| Bulk Auto-Space Submissions | `bulkUpdateAutoSpaceSubmissions` | Re-space the given submissions evenly by the supplied amount and unit. |
| Bulk Create Reddit Posts | `bulkCreateRedditPosts` | Create many Reddit posts in one call from a list of rows or an uploaded file, returning an import group ID and any per-row validation errors. Requires a plan with bulk import. Each row uses the field "user" for the Reddit username (not "redditUsername"). |
| Bulk Delete Reddit Post Submissions | `bulkDeleteRedditPostSubmissions` | Delete several Reddit submissions at once by their IDs. |
| Bulk Delete Reddit Posts | `bulkDeleteRedditPosts` | Delete several Reddit posts at once by their numeric IDs. |
| Bulk Move Post Times | `bulkUpdateMovePostAt` | Shift the scheduled time of the given submissions forwards or backwards by an amount and unit. |
| Bulk Update Comment | `bulkUpdateComment` | Set the same first comment on every one of the given submissions. |
| Bulk Update Post Options | `bulkUpdatePostOptions` | Set the NSFW, spoiler and send-replies-to-inbox flags on the given submissions in one call. |
| Bulk Update Reddit Username | `bulkUpdateRedditUsername` | Reassign the given Reddit submissions to a different linked Reddit username. |
| Cancel Platform Auto Remove | `cancelPlatformAutoRemove` | Cancel the pending automatic removal configured on a submission, so the post stays up. |
| Cancel Platform Auto Repost | `cancelPlatformAutoRepost` | Cancel the pending automatic repost configured on a submission. |
| Cancel Submission Auto Removal | `cancelSubmissionAutoRemoval` | Cancel the scheduled automatic removal of a Reddit submission. |
| Change Reddit Post Submission Title | `changeRedditPostSubmissionTitle` | Change the title of a single Reddit submission without touching the other submissions on the post. |
| Complete Media Upload | `completeMediaUpload` | Finish a direct file upload started with Start Media Upload by exchanging the upload token for a stored media object in the content library. |
| Create Campaign | `createCampaign` | Create a Reddit campaign: a reusable set of default post settings and default per-subreddit submissions that new posts can inherit. |
| Create Hashtag Group | `createHashtagGroup` | Create a named hashtag group with a colour and a list of hashtags, for quick reuse in captions. |
| Create Post Tag | `createPostTag` | Create a post tag with a name and colour. Post tags group posts for filtering and tag-level analytics. |
| Create Reddit Post | `createRedditPost` | Create a Reddit post with one or more per-subreddit submissions. Accepts title, content, link, media or gallery, poll options, campaign, tags, NSFW and spoiler flags and the publishing status. Warning: unless the publishing status is DRAFT, the submissions are posted to the live subreddits at their post time. |
| Delete Campaign | `deleteCampaign` | Delete a Reddit campaign by ID. |
| Delete Hashtag Group | `deleteHashtagGroup` | Delete a hashtag group by ID. |
| Delete Platform Post | `deletePlatformPost` | Delete a post on any platform from Postpone. Pass hardDelete true to delete it permanently instead of moving it to the trash. |
| Delete Post Tag | `deletePostTag` | Permanently delete a post tag and remove it from every post that carries it. |
| Delete Reddit Post | `deleteRedditPost` | Move a Reddit post and all of its submissions to the Postpone trash. |
| Delete Reddit Post Submission | `deleteRedditPostSubmission` | Delete a single per-subreddit submission from a Reddit post. |
| Duplicate Campaign | `duplicateCampaign` | Create a copy of an existing Reddit campaign. |
| Duplicate Reddit Post | `duplicateRedditPost` | Create a copy of an existing Reddit post together with its submissions. |
| Duplicate Reddit Post Submission | `duplicateRedditPostSubmission` | Create a copy of a single Reddit submission on the same post. |
| Edit Campaign | `editCampaign` | Update an existing Reddit campaign's settings and its default submissions. |
| Edit Reddit Post | `editRedditPost` | Edit an existing Reddit post and replace its per-subreddit submissions, using the same fields as Create Reddit Post plus the post ID. |
| Get Aggregate Post Metrics | `aggregatePostMetrics` | Return post metrics aggregated over a date range for the chosen social accounts, campaigns, subreddits and metrics. |
| Get Aggregate Social Account Post Metrics | `aggregateSocialAccountPostMetrics` | Return the requested post metrics aggregated per social account over a date range, optionally grouped by day, week or month. |
| Get Bluesky Post | `blueskyPost` | Retrieve a single scheduled or published Bluesky post from Postpone by its post ID, including its content, media, schedule, publishing status and all of its submissions. |
| Get Campaign | `campaign` | Retrieve a Reddit campaign by its numeric ID, including its default post settings and its default per-subreddit submissions. |
| Get Current User Profile | `profile` | Retrieve the authenticated Postpone user: username, email, timezone, week start, preferences, notification settings and the account with its plan, entitlements and usage. Use it to verify the API key and to discover plan limits. |
| Get Debug Info | `djangoDebug` | Return the Django debug payload (executed SQL queries and any captured exception) for the request. Postpone exposes this GraphQL debug field; it is empty unless server-side debugging is enabled. |
| Get Facebook Post | `facebookPost` | Retrieve a single scheduled or published Facebook post from Postpone by its post ID, including its content, media, schedule, publishing status and all of its submissions. |
| Get Hourly Engagement | `hourlyEngagement` | Return the best posting hours for a social account, as engagement aggregated by hour of the week. |
| Get Import Group | `importGroup` | Retrieve a bulk-import group by ID, with its status, row counts and any validation errors. |
| Get Instagram Audio | `instagramAudio` | Retrieve a single Instagram audio track by its audio ID for a linked Instagram account. |
| Get Instagram Post | `instagramPost` | Retrieve a single scheduled or published Instagram post from Postpone by its post ID, including its content, media, schedule, publishing status and all of its submissions. |
| Get Last Submission To Subreddit | `lastSubmission` | Retrieve the most recent submission the account made to a given subreddit. Use it to respect a subreddit's posting frequency. |
| Get LinkedIn Post | `linkedinPost` | Retrieve a single scheduled or published LinkedIn post from Postpone by its post ID, including its content, media, schedule, publishing status and all of its submissions. |
| Get Mastodon Post | `mastodonPost` | Retrieve a single scheduled or published Mastodon post from Postpone by its post ID, including its content, media, schedule, publishing status and all of its submissions. |
| Get Next Submission To Subreddit | `nextSubmission` | Retrieve the next scheduled submission for a given subreddit. |
| Get Pinterest Post | `pinterestPost` | Retrieve a single scheduled or published Pinterest post from Postpone by its post ID, including its content, media, schedule, publishing status and all of its submissions. |
| Get Post Analytics | `postAnalytics` | Return Reddit post analytics over a date range, optionally grouped and filtered by account, campaign and subreddit. |
| Get Post Tag Metrics | `postTagMetrics` | Return aggregated post metrics broken down by post tag over a date range. |
| Get Post Time Series Metrics | `postTimeSeriesMetrics` | Return post metrics as a time series between two dates, grouped by day, week or month, optionally narrowed to social accounts, subreddits, campaigns and a chosen metric list. |
| Get Post Word Cloud | `analyticsPostWordCloud` | Return the most frequent words and phrases across the account's posts in a date range, for a word-cloud visualisation. |
| Get Public Secure Connect Link | `publicSecureConnectLink` | Retrieve the public details of a secure connect link by its token, as shown to the client who opens the link. |
| Get Reddit Post | `redditPost` | Retrieve a single Reddit post by its numeric ID, including its content, media, campaign, tags and every per-subreddit submission. |
| Get Reddit Post Submission | `redditPostSubmission` | Retrieve a single Reddit submission by ID. Set prepare to true to have Postpone resolve flair, requirements and the final title before submitting. |
| Get Redditor Analytics | `redditorAnalytics` | Return karma and account-level analytics for the linked Reddit accounts over a date range, optionally grouped by period. |
| Get Scheduled Post Analytics | `scheduledPostAnalytics` | Return aggregate counts of scheduled posts, optionally narrowed to given accounts, campaigns and subreddits. The schema also exposes a lastCreated sub-field; it is omitted here because selecting it makes Postpone's own gateway time out (reproduced outside fastn: 29.8s then HTTP 504 "Endpoint request timed out"). Use Get Reddit Post for the post itself. |
| Get Social Account Analytics | `socialAccountAnalytics` | Return follower and account-level analytics for one or more social accounts over a date range, optionally grouped by period. |
| Get Subreddit | `subreddit` | Retrieve Postpone's information about a subreddit by name: posting requirements, allowed post types, flair requirements, rules and moderation settings. |
| Get Threads Post | `threadsPost` | Retrieve a single scheduled or published Threads post from Postpone by its post ID, including its content, media, schedule, publishing status and all of its submissions. |
| Get TikTok Post | `tiktokPost` | Retrieve a single scheduled or published TikTok post from Postpone by its post ID, including its content, media, schedule, publishing status and all of its submissions. |
| Get TikTok User Info | `tiktokUserInfo` | Retrieve the TikTok creator info for a linked TikTok social account: nickname, avatar, privacy level options, interaction settings and the maximum video duration. |
| Get Tumblr Post | `tumblrPost` | Retrieve a single scheduled or published Tumblr post from Postpone by its post ID, including its content, media, schedule, publishing status and all of its submissions. |
| Get Twitter/X Post | `twitterPost` | Retrieve a single scheduled or published Twitter/X post from Postpone by its post ID, including its content, media, schedule, publishing status and all of its submissions. |
| Get VAPID Public Key | `vapidPublicKey` | Retrieve the VAPID public key used to register a browser for Postpone Web Push notifications. |
| Get YouTube Post | `youtubePost` | Retrieve a single scheduled or published YouTube post from Postpone by its post ID, including its content, media, schedule, publishing status and all of its submissions. |
| List Account Members | `accountMembers` | List the members of the Postpone account, with their role, permissions and invitation state. |
| List Analytics Submissions | `analyticsSubmissions` | List submissions with their analytics metrics between two dates, with paging, ordering and filters for social accounts, subreddits, campaigns and unlinked posts. |
| List Bluesky Submissions | `blueskySubmissions` | List Bluesky submissions (individual scheduled or published posts) with paging and filters for date range, social account, client, search text, media, post tags, submission type and publishing status. Returns a paginated list with the total count. |
| List Browser Push Subscriptions | `browserSubscriptions` | List the Web Push browser subscriptions registered for the account. These drive Postpone's own in-browser notifications; they are not outbound integration webhooks. |
| List Campaigns | `campaigns` | List the Reddit campaigns on the account, optionally filtered by Reddit account or subreddit. |
| List Devices | `devices` | List the mobile devices registered to the account for push notifications. |
| List Facebook Submissions | `facebookSubmissions` | List Facebook submissions (individual scheduled or published posts) with paging and filters for date range, social account, client, search text, media, post tags, submission type and publishing status. Returns a paginated list with the total count. |
| List Hashtag Groups | `hashtagGroups` | List the saved hashtag groups on the account, with each group's name, colour and hashtags. |
| List Instagram Submissions | `instagramSubmissions` | List Instagram submissions (individual scheduled or published posts) with paging and filters for date range, social account, client, search text, media, post tags, submission type and publishing status. Returns a paginated list with the total count. |
| List LinkedIn Submissions | `linkedinSubmissions` | List LinkedIn submissions (individual scheduled or published posts) with paging and filters for date range, social account, client, search text, media, post tags, submission type and publishing status. Returns a paginated list with the total count. |
| List Mastodon Submissions | `mastodonSubmissions` | List Mastodon submissions (individual scheduled or published posts) with paging and filters for date range, social account, client, search text, media, post tags, submission type and publishing status. Returns a paginated list with the total count. |
| List Media | `media` | List items in the Postpone content library with paging and filters for IDs, external IDs, Imgur URLs, search text, file type, usage, labels and watermark state. Returns the total count and the matching media objects. |
| List Media Labels | `mediaLabels` | List every label defined on the Postpone content library. Labels are used to group and filter media. |
| List Multi-Platform Analytics Submissions | `multiPlatformAnalyticsSubmissions` | List submissions with analytics across every platform between two dates, with paging, ordering, a free-text query and filters for social accounts, client and post tags. |
| List Next Schedule Dates | `nextScheduleDates` | For the given social accounts, return the next date and time each account's posting schedule would place a post. |
| List Open Account Schedule Slots | `openAccountScheduleSlots` | List the unfilled slots in a social account's posting schedule between a start and end date. The range must lie in the future: Postpone rejects a past window with "end must come after start.". |
| List Pinterest Boards | `pinterestBoards` | List the boards on a linked Pinterest account, for use as the destination of a scheduled Pin. |
| List Pinterest Submissions | `pinterestSubmissions` | List Pinterest submissions (individual scheduled or published posts) with paging and filters for date range, social account, client, search text, media, post tags, submission type and publishing status. Returns a paginated list with the total count. |
| List Post Tags | `postTags` | List the post tags defined on the account, optionally limited to active (non-archived) tags. |
| List Post Templates | `postTemplates` | List saved post templates with paging and ordering, optionally filtered by Reddit account or subreddit. |
| List Previous Titles | `previousTitles` | List titles previously used by the account that match the supplied text, so a title can be reused or avoided. |
| List Recent Import Groups | `recentImportGroups` | List the most recent bulk-import groups on the account with their status and counts. |
| List Recent Threads Topic Tags | `recentThreadsTopicTags` | List the topic tags most recently used on a linked Threads account, for reuse on a new Threads post. |
| List Reddit Posts | `redditPosts` | List Reddit posts on the account with paging and ordering. |
| List Reddit Submissions | `redditSubmissions` | List Reddit submissions with paging, sorting and filters for date range, accounts, media, clients, social accounts, search text, campaigns, subreddits, labels, links, removal categories, error codes, submission type and post tags. |
| List Role Templates | `roleTemplates` | List the role templates available when inviting a member, with each template's content, inbox, subreddit-manager and analytics permissions. |
| List Saved Watermarks | `savedWatermarks` | List the saved watermark presets on the account, including position, opacity, scale and the watermark image. |
| List Scheduled Reddit Posts | `scheduledRedditPosts` | List Reddit posts that are scheduled but not yet submitted, with paging and filters for date range, account, campaign, media, subreddit, label, link, comment text, import group and publishing status. |
| List Scheduled Submissions | `scheduledSubmissions` | List scheduled submissions across every platform, with paging and a wide set of filters (date range, accounts, clients, campaigns, media, subreddits, labels, links, post tags, publishing status and method). Returns a paginated list with the total count. |
| List Secure Connect Links | `secureConnectLinks` | List the secure connect links created on the account. Agencies use these to let a client link their own social accounts without sharing credentials. |
| List Social Accounts | `socialAccounts` | List every social account linked to the Postpone account, optionally filtered by platform. Returns the account ID, platform, username, follower count, capabilities, schedule and connection state. Most scheduling actions need a socialAccountId from here. |
| List Submissions | `submissions` | List submissions across every platform with paging and filters for date range, accounts, clients, campaigns, media, subreddits, removal categories, labels, links and title. |
| List Submissions With Errors | `submissionsWithErrors` | List submissions that failed to publish, with paging and filters for date range, accounts, clients, error codes, subreddits, media and title. Use it to find and re-queue failed posts. |
| List Subreddit Link Flair | `linkFlair` | List the link flair templates available in a subreddit, with their IDs, text and whether the text is editable. |
| List Subreddits Used By Campaigns | `uniqueCampaignsSubreddits` | List the distinct subreddits referenced by the account's campaigns. |
| List Threads Submissions | `threadsSubmissions` | List Threads submissions (individual scheduled or published posts) with paging and filters for date range, social account, client, search text, media, post tags, submission type and publishing status. Returns a paginated list with the total count. |
| List TikTok Submissions | `tiktokSubmissions` | List TikTok submissions (individual scheduled or published posts) with paging and filters for date range, social account, client, search text, media, post tags, submission type and publishing status. Returns a paginated list with the total count. |
| List Timezones | `timezones` | List every timezone Postpone supports, as value/name pairs, for use when setting a user or schedule timezone. |
| List Top Twitter Communities | `twitterTopCommunities` | List the Twitter/X communities the account's posts performed best in over a date range. |
| List Trashed Reddit Posts | `trashedRedditPosts` | List Reddit posts currently in the trash, which can still be restored or permanently deleted. |
| List Tumblr Submissions | `tumblrSubmissions` | List Tumblr submissions (individual scheduled or published posts) with paging and filters for date range, social account, client, search text, media, post tags, submission type and publishing status. Returns a paginated list with the total count. |
| List Twitter/X Submissions | `twitterSubmissions` | List Twitter/X submissions (individual scheduled or published posts) with paging and filters for date range, social account, client, search text, media, post tags, submission type and publishing status. Returns a paginated list with the total count. |
| List Unique Subreddits Posted To | `uniqueSubreddits` | List the distinct subreddits the account has posted to within a date range, with an optional limit. |
| List Watermark Images | `watermarkImages` | List the images in the content library that are available for use as watermarks, optionally filtered by a search string. |
| List YouTube Submissions | `youtubeSubmissions` | List YouTube submissions (individual scheduled or published posts) with paging and filters for date range, social account, client, search text, media, post tags, submission type and publishing status. Returns a paginated list with the total count. |
| Remove Moderator Alert | `removeModAlert` | Remove a Reddit moderator username from the alert list. |
| Remove Scheduled Posts For Subreddit | `removeScheduledPostsForSubreddit` | Delete every scheduled submission for a given Reddit account and subreddit. |
| Remove Submission From Platform | `removeSubmissionFromPlatform` | Delete an already published submission from the social platform it was posted to. Warning: this removes live content from the social network. |
| Reschedule Platform Post | `reschedulePlatformPost` | Move a scheduled post on any platform to a new postAt date and time. |
| Restore Post Tag | `restorePostTag` | Restore a previously archived post tag to the active list. |
| Save Platform Submission As Draft | `savePlatformSubmissionAsDraft` | Move a scheduled submission back to draft so it will not publish until it is scheduled again. |
| Schedule Bluesky Post | `scheduleBlueskyPost` | Create and schedule a Bluesky post through Postpone. Accepts the full ScheduleBlueskyPostInput: social account, caption or body, media, post type, scheduling time and post tags. Warning: a scheduled post is published to the linked live Bluesky account at its post time. |
| Schedule Facebook Post | `scheduleFacebookPost` | Create and schedule a Facebook post through Postpone. Accepts the full ScheduleFacebookPostInput: social account, caption or body, media, post type, scheduling time and post tags. Warning: a scheduled post is published to the linked live Facebook account at its post time. |
| Schedule Instagram Post | `scheduleInstagramPost` | Create and schedule a Instagram post through Postpone. Accepts the full ScheduleInstagramPostInput: social account, caption or body, media, post type, scheduling time and post tags. Warning: a scheduled post is published to the linked live Instagram account at its post time. |
| Schedule LinkedIn Post | `scheduleLinkedInPost` | Create and schedule a LinkedIn post through Postpone. Accepts the full ScheduleLinkedInPostInput: social account, caption or body, media, post type, scheduling time and post tags. Warning: a scheduled post is published to the linked live LinkedIn account at its post time. |
| Schedule Mastodon Post | `scheduleMastodonPost` | Create and schedule a Mastodon post through Postpone. Accepts the full ScheduleMastodonPostInput: social account, caption or body, media, post type, scheduling time and post tags. Warning: a scheduled post is published to the linked live Mastodon account at its post time. |
| Schedule Pinterest Post | `schedulePinterestPost` | Create and schedule a Pinterest post through Postpone. Accepts the full SchedulePinterestPostInput: social account, caption or body, media, post type, scheduling time and post tags. Warning: a scheduled post is published to the linked live Pinterest account at its post time. |
| Schedule Platform Submission | `schedulePlatformSubmission` | Schedule an existing draft submission on any supported platform for a given date and time. Takes the platform, the submission ID and the postAt timestamp. |
| Schedule Reddit Post | `scheduleRedditPost` | Create and schedule a Reddit post through Postpone, including its per-subreddit submissions. Warning: a scheduled post is submitted to the live subreddits at its post time. |
| Schedule Threads Post | `scheduleThreadsPost` | Create and schedule a Threads post through Postpone. Accepts the full ScheduleThreadsPostInput: social account, caption or body, media, post type, scheduling time and post tags. Warning: a scheduled post is published to the linked live Threads account at its post time. |
| Schedule TikTok Post | `scheduleTikTokPost` | Create and schedule a TikTok post through Postpone. Accepts the full ScheduleTikTokPostInput: social account, caption or body, media, post type, scheduling time and post tags. Warning: a scheduled post is published to the linked live TikTok account at its post time. |
| Schedule Tumblr Post | `scheduleTumblrPost` | Create and schedule a Tumblr post through Postpone. Accepts the full ScheduleTumblrPostInput: social account, caption or body, media, post type, scheduling time and post tags. Warning: a scheduled post is published to the linked live Tumblr account at its post time. |
| Schedule Tweet | `scheduleTweet` | Create and schedule a tweet (Twitter/X post) or thread through Postpone. Accepts the full ScheduleTweetInput: social account, text, media, reply settings, post time, tags and thread items. Warning: a scheduled tweet is published to the linked live Twitter/X account at its post time. |
| Schedule YouTube Post | `scheduleYouTubePost` | Create and schedule a YouTube post through Postpone. Accepts the full ScheduleYouTubePostInput: social account, caption or body, media, post type, scheduling time and post tags. Warning: a scheduled post is published to the linked live YouTube account at its post time. |
| Search Instagram Audio | `instagramAudioSearch` | Search the Instagram audio catalogue available to a linked Instagram account, by query and audio type (music or original sound). |
| Set Default Post Settings Fields | `setDefaultPostSettingsFields` | Set a subset of the account-wide default post settings from a DefaultPostSettingsInputType object, leaving the remaining settings unchanged. |
| Set Frequency Warnings Enabled | `setFrequencyWarningsEnabled` | Turn the subreddit posting-frequency warnings on or off for the account. |
| Start Media Upload | `startMediaUpload` | Begin a direct file upload by requesting a pre-signed S3 upload URL and upload token for a given MIME type and byte size. PUT the file to the returned uploadUrl, then call Complete Media Upload. |
| Submit Platform Post Now | `submitPlatformPost` | Publish a scheduled post immediately on the given platform instead of waiting for its scheduled time. Warning: this publishes to the linked live social account straight away. |
| Update Default Post Settings | `updateDefaultPostSettings` | Update the account-wide default post settings (post type, Reddit username, NSFW and spoiler defaults, upload locations, fresh links, auto-spacing, removal rules, repost protection and frequency warnings), optionally applying them to existing posts and templates. |
| Update Hashtag Group | `updateHashtagGroup` | Replace the name, colour and hashtags of an existing hashtag group. |
| Update Post Tag | `updatePostTag` | Rename a post tag or change its colour, by tag ID. |
| Update Reddit Submission Post Time | `updateRedditPostSubmissionPostAt` | Change the scheduled post time of a single Reddit submission. |
| Update Scheduled Bluesky Post | `updateScheduledBlueskyPost` | Update an already scheduled Bluesky post in place. Accepts the same ScheduleBlueskyPostInput as Schedule Bluesky Post, including the ID of the post being updated. |
| Update Scheduled Facebook Post | `updateScheduledFacebookPost` | Update an already scheduled Facebook post in place. Accepts the same ScheduleFacebookPostInput as Schedule Facebook Post, including the ID of the post being updated. |
| Update Scheduled Instagram Post | `updateScheduledInstagramPost` | Update an already scheduled Instagram post in place. Accepts the same ScheduleInstagramPostInput as Schedule Instagram Post, including the ID of the post being updated. |
| Update Scheduled LinkedIn Post | `updateScheduledLinkedInPost` | Update an already scheduled LinkedIn post in place. Accepts the same ScheduleLinkedInPostInput as Schedule LinkedIn Post, including the ID of the post being updated. |
| Update Scheduled Mastodon Post | `updateScheduledMastodonPost` | Update an already scheduled Mastodon post in place. Accepts the same ScheduleMastodonPostInput as Schedule Mastodon Post, including the ID of the post being updated. |
| Update Scheduled Pinterest Post | `updateScheduledPinterestPost` | Update an already scheduled Pinterest post in place. Accepts the same SchedulePinterestPostInput as Schedule Pinterest Post, including the ID of the post being updated. |
| Update Scheduled Reddit Post | `updateScheduledRedditPost` | Update an already scheduled Reddit post and its submissions in place, using the same ScheduleRedditPostInput as Schedule Reddit Post. |
| Update Scheduled Threads Post | `updateScheduledThreadsPost` | Update an already scheduled Threads post in place. Accepts the same ScheduleThreadsPostInput as Schedule Threads Post, including the ID of the post being updated. |
| Update Scheduled TikTok Post | `updateScheduledTikTokPost` | Update an already scheduled TikTok post in place. Accepts the same ScheduleTikTokPostInput as Schedule TikTok Post, including the ID of the post being updated. |
| Update Scheduled Tumblr Post | `updateScheduledTumblrPost` | Update an already scheduled Tumblr post in place. Accepts the same ScheduleTumblrPostInput as Schedule Tumblr Post, including the ID of the post being updated. |
| Update Scheduled Tweet | `updateScheduledTweet` | Update an already scheduled tweet or thread in place. Accepts the same ScheduleTweetInput as Schedule Tweet, including the ID of the post being updated. |
| Update Scheduled YouTube Post | `updateScheduledYouTubePost` | Update an already scheduled YouTube post in place. Accepts the same ScheduleYouTubePostInput as Schedule YouTube Post, including the ID of the post being updated. |
| Upload Media From URL | `uploadMediaFromUrl` | Add a file to the content library by having Postpone download it from a public URL. Returns the stored media object with its CDN URL, MIME type and size. |
