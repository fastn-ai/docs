---
description: "Supadata turns videos and websites into structured data."
hidden: true
---

# Supadata

Supadata turns videos and websites into structured data. This connector covers the Supadata v1 API: transcripts and unified metadata for YouTube, TikTok, Instagram, X and Facebook media, AI extraction of structured data from videos, YouTube video, channel, playlist, search, transcript, translation and batch jobs, web page scraping to Markdown, site maps and website crawls, and account credit usage.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [supadata.ai](https://supadata.ai) |
| **Authentication** | Credentials you enter |
| **Actions** | 21 |
| **Events** | 0 |
| **Slug** | `supadata` |

## Use it

Add Supadata from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.supadata.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Video Extraction | `createExtract` | Starts an AI job that analyzes a video on YouTube, TikTok, Instagram, X or Facebook, or a media file URL, and extracts structured data described by a prompt, a JSON Schema or both. Poll Get Video Extraction Result with the returned job ID. Costs 5 credits per started minute of video, minimum 5. |
| Create Website Crawl | `createCrawl` | Starts a crawl job that extracts Markdown content from pages across a website, up to a page limit. Poll Get Crawl Result with the returned job ID. Costs 1 credit per crawled page. |
| Create YouTube Transcript Batch | `createYoutubeTranscriptBatch` | Creates a batch job that fetches transcripts for multiple YouTube videos given as a list of video IDs or URLs, a playlist or a channel. Provide exactly one of Video IDs, Playlist or Channel. Playlist and channel batches include regular videos only. Poll Get YouTube Batch Result with the returned job ID. Costs 1 credit per video. |
| Create YouTube Video Metadata Batch | `createYoutubeVideoBatch` | Creates a batch job that fetches metadata for multiple YouTube videos given as a list of video IDs or URLs, a playlist or a channel. Provide exactly one of Video IDs, Playlist or Channel. Playlist and channel batches include regular videos only. Poll Get YouTube Batch Result with the returned job ID. Costs 1 credit per video. |
| Get Account Information | `getAccount` | Retrieves the Supadata organization for the API key with its subscription plan, credit allowance for the billing period and credits used so far. This request does not consume credits. |
| Get Crawl Result | `getCrawl` | Retrieves the status of a website crawl job and, once completed, the Markdown content of the crawled pages. Use skip to page through large results. Polling does not consume credits. |
| Get Media Metadata | `getMetadata` | Retrieves unified metadata for a post or video on YouTube, TikTok, Instagram, X or Facebook, including author, engagement statistics, media details, tags and publish time. Costs 1 credit. |
| Get Transcript | `getTranscript` | Retrieves the transcript of a video on YouTube, TikTok, Instagram, X or Facebook, or of a public media file URL, fetching an existing transcript or generating one with AI. Large videos return a job ID instead; poll Get Transcript Result. Costs 1 credit for a native transcript or 2 credits per generated minute. |
| Get Transcript Result | `getTranscriptJob` | Retrieves the status and, when completed, the transcript of an asynchronous transcript job. Polling does not consume credits. |
| Get Video Extraction Result | `getExtractJob` | Retrieves the status and, when completed, the structured data of an AI video extraction job, plus the AI-generated schema when none was supplied. Polling does not consume credits. |
| Get YouTube Batch Result | `getYoutubeBatch` | Retrieves the status, progress statistics and per-video results of a YouTube transcript or video metadata batch job. Use limit and offset to page through a completed batch. Polling does not consume credits. |
| Get YouTube Channel | `getYoutubeChannel` | Retrieves metadata for a YouTube channel, including name, handle, description, subscriber, video and view counts, thumbnail and banner. |
| Get YouTube Playlist | `getYoutubePlaylist` | Retrieves metadata for a YouTube playlist, including title, description, video count, view count, last update time and owning channel. |
| Get YouTube Transcript | `getYoutubeTranscript` | Retrieves the transcript of a YouTube video as timed segments or plain text. If the requested language is unavailable, the first available language is returned. Provide either a video URL or a video ID. Costs 1 credit. |
| Get YouTube Video | `getYoutubeVideo` | Retrieves metadata for a YouTube video, including title, description, duration, channel, tags, thumbnail, upload date, view and like counts, and the languages its transcript is available in. |
| List YouTube Channel Videos | `listYoutubeChannelVideos` | Lists video IDs from a YouTube channel, split into regular videos, Shorts and live streams, optionally limited to one type. |
| List YouTube Playlist Videos | `listYoutubePlaylistVideos` | Lists the video IDs in a YouTube playlist, split into regular videos, Shorts and live streams. |
| Map Website | `mapWebsite` | Scans a website and returns the URLs found across it, useful for building a sitemap or choosing pages to scrape. Costs 1 credit. |
| Scrape Web Page | `scrapeWebPage` | Scrapes a web page and returns its content as Markdown with the page name, description, character count and the links found on it. Costs 1 credit. |
| Search YouTube | `searchYoutube` | Searches YouTube for videos, channels, playlists and movies with filters for upload date, type, duration, special feature and sort order. Without a limit a single page of about 20 results is returned with a next page token (1 credit); with a limit results are paginated automatically at 1 credit per 20 results. |
| Translate YouTube Transcript | `translateYoutubeTranscript` | Translates the transcript of a YouTube video into the requested language and returns it as timed segments or plain text. Provide either a video URL or a video ID. Costs 30 credits per minute of transcript. |
