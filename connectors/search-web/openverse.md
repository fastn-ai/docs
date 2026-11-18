---
description: "Openverse (by WordPress) is a free search engine for openly licensed images and audio, with hundreds of millions of works from Creative Commons and public…"
hidden: true
---

# Openverse

<img src="../../.gitbook/assets/connectors/openverse.png" alt="Openverse logo" width="64">

Openverse (by WordPress) is a free search engine for openly licensed images and audio, with hundreds of millions of works from Creative Commons and public domain sources. Search images and audio with license, source, creator and format filters, get details, related works, waveforms, thumbnails, oEmbed data and catalog statistics, and report content. Works without an API key (anonymous rate limits apply).

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [openverse.org](https://openverse.org) |
| **Authentication** | No authentication |
| **Slug** | `openverse` |

## Use it

Add Openverse from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openverse.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Access Token | `getAccessToken` | Exchange a registered application's client_id and client_secret for a bearer access token (POST /v1/auth_tokens/token/, client credentials grant, form encoded). The application must first be registered and its email verified. Docs: https://api.openverse.org/v1/ |
| Get Audio | `getAudio` | Get the details of a specified audio track. By using this endpoint, you can obtain info about audio files such as `id`, `title`, `indexed_on`, `foreign_landing_url`, `url`, `creator`, `creator_url`, `license`, `license_version`, `license_url`, `provider`, `source`, `category`, `genres`, `filesize`, `filetype`, `tags`, `alt_files`, `attribution`, `fields_matched`, `mature`, `audio_set`, `duration`, `bit_rate`, `sample_rate`, `thumbnail`, `detail_url`, `related_url`, `waveform`, `peaks` and `unstable__sensitivity` (GET /v1/audio/{identifier}/). Docs: https://api.openverse.org/v1/ |
| Get Audio Source Statistics | `getAudioStats` | Get a list of all content sources and their respective number of audio files in the Openverse catalog. By using this endpoint, you can obtain info about content sources such as `source_name`, `display_name`, `source_url`, `logo_url` and `media_count`. (GET /v1/audio/stats/). Docs: https://api.openverse.org/v1/ |
| Get Audio Thumbnail | `getAudioThumbnail` | Retrieve the scaled down and compressed thumbnail of the artwork of an audio track or its audio set. (GET /v1/audio/{identifier}/thumb/). Docs: https://api.openverse.org/v1/ |
| Get Audio Waveform | `getAudioWaveform` | Get the waveform peaks for an audio track. The peaks are provided as a list of numbers, each of these numbers being a fraction between 0 and 1. The list contains approximately 1000 numbers, although it can be slightly higher or lower, depending on the track's length. (GET /v1/audio/{identifier}/waveform/). Docs: https://api.openverse.org/v1/ |
| Get Image | `getImage` | Get the details of a specified image. By using this endpoint, you can obtain info about images such as `id`, `title`, `indexed_on`, `foreign_landing_url`, `url`, `creator`, `creator_url`, `license`, `license_version`, `license_url`, `provider`, `source`, `category`, `filesize`, `filetype`, `tags`, `attribution`, `fields_matched`, `mature`, `height`, `width`, `thumbnail`, `detail_url`, `related_url` and `unstable__sensitivity` (GET /v1/images/{identifier}/). Docs: https://api.openverse.org/v1/ |
| Get Image oEmbed | `getImageOembed` | Retrieve the structured data for a specified image URL as per the [oEmbed spec](https://oembed.com/). This info can be used to embed the image on the consumer's website. Only JSON format is supported. (GET /v1/images/oembed/). Docs: https://api.openverse.org/v1/ |
| Get Image Source Statistics | `getImageStats` | Get a list of all content sources and their respective number of images in the Openverse catalog. By using this endpoint, you can obtain info about content sources such as `source_name`, `display_name`, `source_url`, `logo_url` and `media_count`. (GET /v1/images/stats/). Docs: https://api.openverse.org/v1/ |
| Get Image Thumbnail | `getImageThumbnail` | Retrieve the scaled down and compressed thumbnail of the image. (GET /v1/images/{identifier}/thumb/). Docs: https://api.openverse.org/v1/ |
| List Related Audio | `listRelatedAudio` | Get related audio files for a specified audio track. By using this endpoint, you can get the details of related audio such as `id`, `title`, `indexed_on`, `foreign_landing_url`, `url`, `creator`, `creator_url`, `license`, `license_version`, `license_url`, `provider`, `source`, `category`, `genres`, `filesize`, `filetype`, `tags`, `alt_files`, `attribution`, `fields_matched`, `mature`, `audio_set`, `duration`, `bit_rate`, `sample_rate`, `thumbnail`, `detail_url`, `related_url`, `waveform`, `peaks` and `unstable__sensitivity`. (GET /v1/audio/{identifier}/related/). Docs: https://api.openverse.org/v1/ |

<details>

<summary>See 6 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Related Images | `listRelatedImages` | Get related images for a specified image. By using this endpoint, you can get the details of related images such as `id`, `title`, `indexed_on`, `foreign_landing_url`, `url`, `creator`, `creator_url`, `license`, `license_version`, `license_url`, `provider`, `source`, `category`, `filesize`, `filetype`, `tags`, `attribution`, `fields_matched`, `mature`, `height`, `width`, `thumbnail`, `detail_url`, `related_url` and `unstable__sensitivity`. (GET /v1/images/{identifier}/related/). Docs: https://api.openverse.org/v1/ |
| Register Application | `registerApplication` | Register an application for access to the Openverse API via OAuth2. Provide a unique application `name`, a brief `description`, and an `email` address where Openverse can contact you. The application `name` must be unique across all registered Openverse API applications. Upon registering, you will receive a `client_id` and `client_secret`, which you can then use to authenticate using the standard OAuth2 flow. &gt; ⚠️ **WARNINGS:** &gt; - Store your `client_id` and `client_secret` because you will not be &gt; able to retrieve them later. &gt; - You must keep `client_secret` confidential, as anybody with your &gt; `client_secret` can impersonate your application. You must verify your email address by clicking the link sent to you in an email. Until you do that, the application will be subject to the same rate limits as an anonymous user. (POST /v1/auth_tokens/register/). Docs: https://api.openverse.org/v1/ |
| Report Audio | `reportAudio` | Report an issue with a audio to the Openverse moderators: mature or sensitive content, a DMCA copyright claim, or another reason (POST /v1/audio/{identifier}/report/). A description is required when reason is dmca or other. This files a real report. Docs: https://api.openverse.org/v1/ |
| Report Image | `reportImage` | Report an issue with a image to the Openverse moderators: mature or sensitive content, a DMCA copyright claim, or another reason (POST /v1/images/{identifier}/report/). A description is required when reason is dmca or other. This files a real report. Docs: https://api.openverse.org/v1/ |
| Search Audio | `searchAudio` | Return audio files that match the query. This endpoint allows you to search within specific fields, or to retrieve a collection of all audio files from a specific source, creator or tag. Results are paginated on the basis of the `page` parameter. The `page_size` parameter controls the total number of pages. Although there may be millions of relevant records, only the most relevant or the most recent several thousand records can be viewed. This is by design: the search endpoint should be used to find the top 10,000 most relevant results, not for exhaustive search or bulk download of every barely relevant result. As such, the caller should not try to access pages beyond `page_count`, or else the server will reject the query. ### Default search The **default search** allows users to find media based on a query string. It supports a wide range of optional filters to narrow down search results according to specific needs. By default, this endpoint performs a full-text search for the va..... |
| Search Images | `searchImages` | Return images that match the query. This endpoint allows you to search within specific fields, or to retrieve a collection of all images from a specific source, creator or tag. Results are paginated on the basis of the `page` parameter. The `page_size` parameter controls the total number of pages. Although there may be millions of relevant records, only the most relevant or the most recent several thousand records can be viewed. This is by design: the search endpoint should be used to find the top 10,000 most relevant results, not for exhaustive search or bulk download of every barely relevant result. As such, the caller should not try to access pages beyond `page_count`, or else the server will reject the query. ### Default search The **default search** allows users to find media based on a query string. It supports a wide range of optional filters to narrow down search results according to specific needs. By default, this endpoint performs a full-text search for the value of `q`..... |

</details>
