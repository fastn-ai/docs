---
description: "GIPHY is a library of GIFs, stickers and short clips. Search, autocomplete and get GIFs, stickers, clips and channels."
hidden: true
---

# GIPHY

<img src="../../.gitbook/assets/connectors/lg/giphy.png" alt="GIPHY logo">

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Authentication** | API key |
| **Slug** | `giphy` |

## Setup

Your customers enter their API key for GIPHY when they connect. Nothing else needs setting up.

## Use it

Add GIPHY from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.giphy.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Autocomplete Search Term</td><td><code>autocompleteSearchTerm</code></td><td>Returns search terms that complete a partially typed query, for building a search-as-you-type experience.</td></tr><tr><td>Generate Random ID</td><td><code>generateRandomId</code></td><td>Generates an anonymous customer identifier that can be passed as the Customer ID on later calls so GIPHY can personalise results without you supplying your own user id.</td></tr><tr><td>Get Channel</td><td><code>getChannel</code></td><td>Returns a single GIPHY channel by its identifier.</td></tr><tr><td>Get Clip By ID</td><td><code>getClipById</code></td><td>Returns a single GIPHY Clip by its identifier.</td></tr><tr><td>Get Clips By IDs</td><td><code>getClipsByIds</code></td><td>Returns several GIPHY Clips in one call from a comma-separated list of identifiers.</td></tr><tr><td>Get GIF By ID</td><td><code>getGifById</code></td><td>Returns a single GIF by its GIPHY identifier.</td></tr><tr><td>Get GIFs By IDs</td><td><code>getGifsByIds</code></td><td>Returns several GIFs in one call from a comma-separated list of GIPHY identifiers, up to 100 per request.</td></tr><tr><td>Get Random GIF</td><td><code>getRandomGif</code></td><td>Returns one randomly selected GIF, optionally limited to a tag.</td></tr><tr><td>Get Random Sticker</td><td><code>getRandomSticker</code></td><td>Returns one randomly selected sticker, optionally limited to a tag.</td></tr><tr><td>Get Sticker Pack</td><td><code>getStickerPack</code></td><td>Returns a single sticker pack by its identifier.</td></tr></tbody></table>

<details>

<summary>View 21 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Channel Children</td><td><code>listChannelChildren</code></td><td>Returns the sub-channels nested directly under a channel.</td></tr><tr><td>List Channel GIFs</td><td><code>listChannelGifs</code></td><td>Returns the GIFs published by a channel.</td></tr><tr><td>List Child Sticker Packs</td><td><code>listChildStickerPacks</code></td><td>Returns the sticker packs nested directly under a parent pack.</td></tr><tr><td>List Emoji</td><td><code>listEmoji</code></td><td>Returns GIPHY's animated emoji library.</td></tr><tr><td>List Emoji Variations</td><td><code>listEmojiVariations</code></td><td>Returns the skin-tone and styling variations of a single animated emoji.</td></tr><tr><td>List GIF Categories</td><td><code>listGifCategories</code></td><td>Returns GIPHY's browse categories and their subcategories, each with a representative GIF.</td></tr><tr><td>List Related Search Terms</td><td><code>listRelatedSearchTerms</code></td><td>Returns search terms related to a given term, useful for suggesting alternative searches.</td></tr><tr><td>List Sticker Packs</td><td><code>listStickerPacks</code></td><td>Returns GIPHY's curated sticker packs.</td></tr><tr><td>List Stickers In Pack</td><td><code>listStickersInPack</code></td><td>Returns the stickers contained in a sticker pack.</td></tr><tr><td>List Trending Clips</td><td><code>listTrendingClips</code></td><td>Returns the GIPHY Clips currently trending, in the order GIPHY ranks them.</td></tr><tr><td>List Trending GIFs</td><td><code>listTrendingGifs</code></td><td>Returns the GIFs currently trending on GIPHY, in the order GIPHY ranks them.</td></tr><tr><td>List Trending Search Terms</td><td><code>listTrendingSearchTerms</code></td><td>Returns the search terms currently trending across GIPHY.</td></tr><tr><td>List Trending Stickers</td><td><code>listTrendingStickers</code></td><td>Returns the stickers currently trending on GIPHY, in the order GIPHY ranks them.</td></tr><tr><td>Register User Action</td><td><code>registerUserAction</code></td><td>Reports that an end user saw, clicked or sent an asset, so GIPHY can improve the results it returns. Pass the analytics payload GIPHY returned alongside the asset.</td></tr><tr><td>Search Channels</td><td><code>searchChannels</code></td><td>Searches GIPHY channels by name and returns the matching channels with their featured GIF.</td></tr><tr><td>Search Clips</td><td><code>searchClips</code></td><td>Searches GIPHY Clips, the library of short videos with sound, and returns a paginated list of matches.</td></tr><tr><td>Search GIFs</td><td><code>searchGifs</code></td><td>Searches the GIPHY GIF library for a word or phrase and returns a paginated list of matching GIFs.</td></tr><tr><td>Search Stickers</td><td><code>searchStickers</code></td><td>Searches the GIPHY sticker library, which contains only assets with transparent backgrounds, and returns a paginated list of matches.</td></tr><tr><td>Translate Term To GIF</td><td><code>translateGif</code></td><td>Translates a word or phrase into the single GIF that GIPHY's search engine considers the best match.</td></tr><tr><td>Translate Term To Sticker</td><td><code>translateSticker</code></td><td>Translates a word or phrase into the single sticker that GIPHY's search engine considers the best match.</td></tr><tr><td>Upload GIF</td><td><code>uploadGif</code></td><td>Uploads a GIF or video to GIPHY from a URL or file and publishes it on your channel. Uploaded assets become publicly visible on GIPHY and there is no documented delete endpoint, so treat every call as permanent.</td></tr></tbody></table>

</details>

## Events

GIPHY has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
