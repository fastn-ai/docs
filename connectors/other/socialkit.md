---
description: "SocialKit is a unified REST API for extracting public data from social video and social network URLs: transcripts, AI summaries, comments, engagement stats,…"
hidden: true
---

# SocialKit

SocialKit is a unified REST API for extracting public data from social video and social network URLs: transcripts, AI summaries, comments, engagement stats, channel/profile data, keyword search, and direct or asynchronous media download URLs across YouTube, TikTok, Instagram, Facebook, Twitter/X, LinkedIn and Reddit.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [socialkit.dev](https://socialkit.dev) |
| **Authentication** | Credentials you enter |
| **Actions** | 63 |
| **Events** | 0 |
| **Slug** | `socialkit` |

## Use it

Add SocialKit from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.socialkit.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Get Instagram Post Stats | `bulkInstagramStats` | Get engagement metrics for up to five Instagram posts or reels in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Bulk Get Instagram Profile Stats | `bulkInstagramChannelStats` | Get profile statistics for up to five Instagram profiles in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Bulk Get Instagram Transcripts | `bulkInstagramTranscripts` | Extract transcripts for up to five Instagram videos or reels in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Bulk Get TikTok Comments | `bulkTiktokComments` | Fetch comments for up to five TikTok videos in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Bulk Get TikTok Creator Stats | `bulkTiktokChannelStats` | Get creator statistics for up to five TikTok profiles in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Bulk Get TikTok Transcripts | `bulkTiktokTranscripts` | Extract transcripts for up to five TikTok videos in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Bulk Get TikTok Video Stats | `bulkTiktokStats` | Get engagement metrics for up to five TikTok videos in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Bulk Get YouTube Comments | `bulkYoutubeComments` | Fetch comments for up to five YouTube videos in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Bulk Get YouTube Transcripts | `bulkYoutubeTranscripts` | Extract transcripts for up to five YouTube videos in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Bulk Get YouTube Video Stats | `bulkYoutubeStats` | Get metadata and engagement statistics for up to five YouTube videos in one call. Returns a per-URL result array and a summary of successes and failures. Each successful item costs one SocialKit credit. |
| Bulk Summarize Instagram Videos | `bulkInstagramSummaries` | Produce AI summaries for up to five Instagram videos or reels in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Bulk Summarize TikTok Videos | `bulkTiktokSummaries` | Produce AI summaries for up to five TikTok videos in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Bulk Summarize YouTube Videos | `bulkYoutubeSummaries` | Produce AI summaries for up to five YouTube videos in one call. Returns a per-URL result array plus a summary with the credits actually used; failed items are not billed. |
| Get API Service Status | `getApiStatus` | Get the current public health status of every SocialKit API capability, with an overall indicator and a per-tool status and message. Consumes no credits. |
| Get Async Download Job | `getAsyncDownloadJob` | Poll a download job created by Start Async Video Download Job. Polling is free. Failed jobs are unbilled and include errorCode and retryable. A completed job with insufficient credits returns 403 insufficient_credits without its URL; add credits and poll the same job to pay once and unlock it. The returned downloadUrl is an unauthenticated link that expires - treat it as sensitive. |
| Get Facebook Page Stats | `getFacebookChannelStats` | Get statistics and metadata for a Facebook page, including follower count, category, bio, avatar and cover photo. Costs one SocialKit credit per successful request. |
| Get Facebook Post Comments | `getFacebookComments` | Fetch the top comments on a Facebook video or post, with author, text, like count and reply count, plus a cursor for the next page. Costs one SocialKit credit per successful request. |
| Get Facebook Post Stats | `getFacebookStats` | Get engagement metrics and metadata for a Facebook video or post, including views, likes, comments, shares and a reaction breakdown. Costs one SocialKit credit per successful request. |
| Get Facebook Video Transcript | `getFacebookTranscript` | Extract the full spoken transcript, with timestamped segments, from a Facebook video. Costs one SocialKit credit per successful request. |
| Get Instagram Post Comments | `getInstagramComments` | Fetch the top comments on an Instagram post or reel, with author, text, like count and reply count, plus a cursor for the next page. Costs one SocialKit credit per successful request. |
| Get Instagram Post Stats | `getInstagramStats` | Get metadata and engagement metrics for an Instagram post or reel. Views are optional by default and return null when unavailable; set requireViews to true to demand a verified count, in which case unavailable strict requests return 503 without a charge. |
| Get Instagram Profile Stats | `getInstagramChannelStats` | Get statistics and metadata for an Instagram profile, including followers, following, total posts, bio and avatar. Costs one SocialKit credit per successful request. |
| Get Instagram Video Download URL | `getInstagramDownloadUrl` | Get a temporary direct download URL for an Instagram video or reel. The returned downloadUrl is an unauthenticated link that expires - treat it as sensitive. Costs SocialKit credits per successful request. |
| Get Instagram Video Transcript | `getInstagramTranscript` | Extract the full spoken transcript, with timestamped segments, from an Instagram video or reel. Costs one SocialKit credit per successful request. |
| Get LinkedIn Company | `getLinkedinCompany` | Get public data from a LinkedIn company page, including name, description, follower count, employee count and logo. Costs one SocialKit credit per successful request. |
| Get LinkedIn Post | `getLinkedinPost` | Get a single LinkedIn post by URL, with its text, engagement metrics, media links and author. Costs one SocialKit credit per successful request. |
| Get LinkedIn Profile | `getLinkedinProfile` | Get public data from a LinkedIn person profile, including name, headline, follower and connection counts, profile image and recent articles. Costs one SocialKit credit per successful request. |
| Get LinkedIn Video Transcript | `getLinkedinTranscript` | Extract the spoken transcript, with timestamped segments, from a LinkedIn post that carries native video. Costs one SocialKit credit per successful request. |
| Get Reddit Post | `getRedditPost` | Get public details for a Reddit post without a Reddit login, including title, body text, author, score, upvote ratio, comment count, flair, media and moderation flags. Supply exactly one of url or postId. Costs one SocialKit credit per successful request. |
| Get Reddit Subreddit Details | `getRedditSubredditDetails` | Get public details for a subreddit without a Reddit login, including title, description, subscriber and active-user counts, creation date, icon, banner and access flags. Supply exactly one of url or subreddit. Costs one SocialKit credit per successful request. |
| Get Remaining Credits | `getCredits` | Get the authenticated project's remaining monthly and purchased SocialKit credits, with the current billing cycle start and reset date. This request itself does not consume credits. |
| Get TikTok Creator Stats | `getTiktokChannelStats` | Get statistics for a TikTok creator profile, including followers, following, total likes, total videos and bio link. Paid requests allow up to 120 seconds for recovery and failures use zero credits; cache hits also use zero credits. |
| Get TikTok Video Comments | `getTiktokComments` | Fetch the top comments on a TikTok video, with author, username, text, like count and reply count. Costs one SocialKit credit per successful request. |
| Get TikTok Video Download URL | `getTiktokDownloadUrl` | Get a temporary watermark-free direct download URL for a TikTok video. The returned downloadUrl is an unauthenticated link that expires - treat it as sensitive. Costs SocialKit credits per successful request. |
| Get TikTok Video Stats | `getTiktokStats` | Get metadata and engagement metrics for a single TikTok video, including title, creator, views, likes, comments, shares, collects, duration and thumbnail. Costs one SocialKit credit per successful request. |
| Get TikTok Video Transcript | `getTiktokTranscript` | Extract the full spoken transcript, with timestamped segments, from a TikTok video. Costs one SocialKit credit per successful request. |
| Get Transcript From Video File URL | `getVideoFileTranscript` | Extract the spoken transcript from any publicly accessible video file URL (MP4, WebM, MOV), with timestamped segments. Costs SocialKit credits per successful request. |
| Get X Article | `getTwitterArticle` | Extract a native X Article as plain text and Markdown with author metadata and media references. Accepts article or share URLs (/author/article/POST_ID, /i/article/POST_ID) and the associated post URLs. Requires public content. Costs one SocialKit credit per successful request. |
| Get X Post | `getTwitterTweet` | Get a single Twitter/X post by URL, with its text, author and like, retweet, reply and view counts. Costs one SocialKit credit per successful request. |
| Get X Profile | `getTwitterProfile` | Get public profile data for a Twitter/X user, including bio, follower and following counts, tweet count, verification status, location and join date. Costs one SocialKit credit per successful request. |
| Get X Thread | `getTwitterThread` | Reconstruct a full Twitter/X thread (a self-reply chain) from any post URL in it, returning every post in order plus one combined text with untruncated long-form note content. Costs one SocialKit credit per successful request. |
| Get X Video Transcript | `getTwitterTranscript` | Extract the spoken transcript, with timestamped segments, from a Twitter/X post that carries native video. Costs one SocialKit credit per successful request. |
| Get YouTube Channel Stats | `getYoutubeChannelStats` | Get statistics and metadata for a YouTube channel, including subscriber count, total videos, bio, avatar and banner. Costs one SocialKit credit per successful request. |
| Get YouTube Video Comments | `getYoutubeComments` | Fetch the top comments on a YouTube video, with author, text, like count, reply count and posting date. Costs one SocialKit credit per successful request. |
| Get YouTube Video Download URL | `getYoutubeDownloadUrl` | Get a temporary direct download URL for a YouTube video in the requested format and quality. Live and upcoming streams return 422 media_not_ready; completed recordings are supported. The returned downloadUrl is an unauthenticated link that expires - treat it as sensitive. Costs SocialKit credits per successful request. |
| Get YouTube Video Stats | `getYoutubeStats` | Get metadata and engagement statistics for a single YouTube video or Short, including title, description, channel, views, likes, comment count, duration, publish date and thumbnail. Costs one SocialKit credit per successful request. |
| Get YouTube Video Transcript | `getYoutubeTranscript` | Extract the full spoken transcript, with timestamped segments, from a YouTube video or Short. Costs one SocialKit credit per successful request. |
| List Instagram Profile Posts | `listInstagramChannelPosts` | List recent posts from an Instagram profile feed, with caption, type, like, comment and view counts and a cursor for the next page. Costs one SocialKit credit per successful request. |
| List Instagram Profile Reels | `listInstagramChannelReels` | List recent reels from an Instagram profile reels tab, with caption, duration, like, comment and view counts and a cursor for the next page. Costs one SocialKit credit per successful request. |
| List LinkedIn Company Posts | `listLinkedinCompanyPosts` | List recent posts from a LinkedIn company page, with text, like, comment and share counts, media links and publish date. Costs one SocialKit credit per successful request. |
| List TikTok Creator Videos | `listTiktokChannelVideos` | List recent videos posted by a TikTok creator, with description, duration, view, like, comment and share counts, and a cursor for the next page. Paid requests allow up to 120 seconds for recovery and failures use zero credits. |
| List X User Posts | `listTwitterTweets` | List recent posts from a Twitter/X user timeline, with text, engagement counts, hashtags and links, plus a cursor for the next page. Costs one SocialKit credit per successful request. |
| List YouTube Channel Or Playlist Videos | `listYoutubeVideos` | List the videos published on a YouTube channel or contained in a YouTube playlist, with title, duration, view count and publish time. Costs one SocialKit credit per request - note that an unresolvable channel URL still returns 200 with an empty results array and is still billed. |
| Search Instagram Reels | `searchInstagramReels` | Search Instagram reels by keyword and return matching reels with caption, author and engagement counts. Anonymous Instagram search exposes a single batch, so page must be 1. Costs one SocialKit credit per successful request. |
| Search TikTok Videos | `searchTiktokVideos` | Search TikTok videos by keyword and return matching videos with description, author and engagement stats. Costs one SocialKit credit per successful request. |
| Search TikTok Videos By Hashtag | `searchTiktokHashtag` | Search TikTok videos carrying a given hashtag and return matching videos with description, author and engagement stats. Costs one SocialKit credit per successful request. |
| Search YouTube Videos | `searchYoutubeVideos` | Search YouTube videos by keyword and return matching videos with title, channel, duration, view count and thumbnail. Costs one SocialKit credit per successful request. |
| Start Async Video Download Job | `startAsyncDownloadJob` | Start an asynchronous download job for a video of up to 1080p and 2 GB. Responds 202 with a jobId; poll Get Async Download Job until status is ready to obtain the download URL. An identical request from the same project reuses a queued or processing job. Successful downloads cost 1 credit per started minute through 480p, or 4 credits per started minute at 720p and 1080p, charged once on completion; failed jobs are unbilled. |
| Summarize Facebook Video | `summarizeFacebookVideo` | Produce an AI summary of a Facebook video, returning a narrative summary plus main topics, key points, tone, target audience and notable quotes. Costs SocialKit credits per successful request. |
| Summarize Instagram Video | `summarizeInstagramVideo` | Produce an AI summary of an Instagram video or reel, returning a narrative summary plus main topics, key points, tone, target audience and notable quotes. Costs SocialKit credits per successful request. |
| Summarize TikTok Video | `summarizeTiktokVideo` | Produce an AI summary of a TikTok video, returning a narrative summary plus main topics, key points, tone, target audience and notable quotes. Costs SocialKit credits per successful request. |
| Summarize Video File URL | `summarizeVideoFile` | Produce an AI summary of any publicly accessible video file URL, returning a narrative summary plus main topics, key points, tone, target audience and notable quotes. Costs SocialKit credits per successful request. |
| Summarize YouTube Video | `summarizeYoutubeVideo` | Produce an AI summary of a YouTube video, returning a narrative summary plus main topics, key points, tone, target audience and notable quotes. Costs SocialKit credits per successful request. |
