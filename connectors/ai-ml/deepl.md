---
description: "DeepL language AI API: text translation, document translation, v2 and v3 multilingual glossaries, spoken terms, translation memories, style rules, DeepL Write…"
hidden: true
---

# DeepL

DeepL language AI API: text translation, document translation, v2 and v3 multilingual glossaries, spoken terms, translation memories, style rules, DeepL Write (rephrase/correct), supported languages and character usage.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [deepl.com](https://deepl.com) |
| **Authentication** | API key |
| **Actions** | 61 |
| **Events** | 0 |
| **Slug** | `deepl` |

## Use it

Add DeepL from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.deepl.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Correct Text (DeepL Write) | `correctText` | DeepL Write: corrects grammar and spelling in the supplied text. Returns improvements[] with the corrected text. |
| Create Admin Developer Key | `adminCreateDeveloperKey` | SECURITY WARNING: mints a new DeepL API key for the account and returns it. Treat the response as a live credential - never log it or forward it. Requires a DeepL API Pro account with the Admin API entitlement; Pro host (api.deepl.com) only. Without the entitlement DeepL answers 403 Forbidden. |
| Create Glossary (v2) | `createGlossaryV2` | Creates a single language-pair glossary. entries is a TSV or CSV string of source/target term pairs; entries_format must be tsv or csv. Returns the new glossary_id. |
| Create Multilingual Glossary (v3) | `createMultilingualGlossary` | Creates a multilingual glossary holding one dictionary per language pair. dictionaries is an array of {source_lang, target_lang, entries, entries_format}. Returns the new glossary_id. |
| Create Spoken Terms Collection | `createSpokenTerms` | Creates a spoken terms collection used by DeepL Voice to recognise names and jargon. term_lists is an array of {lang, entries}. Returns the new spoken_terms_id. |
| Create Style Custom Instruction | `createCustomInstruction` | Adds a free-text custom instruction to a style rule list, for example 'always address the reader informally'. Returns the new instruction id. |
| Create Style Rule List | `createStyleRuleList` | Creates a style rule list that can be passed to Translate Text as style_id to enforce house style. Returns the new style_id. |
| Create Voice Translation Job | `createVoiceTranslateJob` | DeepL Voice: creates an asynchronous job that transcribes and translates an audio file. Returns job_id, an upload_url for the audio and a short-lived signature. Requires a DeepL Voice entitlement; accounts without it get 403 Forbidden. |
| Deactivate Admin Developer Key | `adminDeactivateDeveloperKey` | DESTRUCTIVE: permanently deactivates one DeepL developer key by key_id. If key_id is the key this connection authenticates with, the connector loses access immediately and DeepL offers no API undo - list the keys first and confirm the id. Requires a DeepL API Pro account with the Admin API entitlement; Pro host (api.deepl.com) only. Without the entitlement DeepL answers 403 Forbidden. |
| Delete Glossary (v2) | `deleteGlossaryV2` | Permanently deletes a v2 glossary by id. Returns 204 No Content on success. |
| Delete Glossary Dictionary (v3) | `deleteGlossaryDictionary` | Deletes one language-pair dictionary from a multilingual (v3) glossary, leaving the glossary itself in place. Returns 204 No Content. |
| Delete Multilingual Glossary (v3) | `deleteMultilingualGlossary` | Permanently deletes a multilingual (v3) glossary and all of its dictionaries. Returns 204 No Content. |
| Delete Spoken Terms Collection | `deleteSpokenTerms` | Permanently deletes a spoken terms collection and all of its term lists. Returns 204 No Content. |
| Delete Spoken Terms List | `deleteSpokenTermsList` | Deletes the term list for one language from a spoken terms collection, leaving the collection in place. Returns 204 No Content. |
| Delete Style Custom Instruction | `deleteCustomInstruction` | Removes one custom instruction from a style rule list. Returns 204 No Content. |
| Delete Style Rule List | `deleteStyleRuleList` | Permanently deletes a style rule list and its custom instructions. Returns 204 No Content. |
| Delete Translation Memory | `deleteTranslationMemory` | Permanently deletes a translation memory and all of its segments. Returns 204 No Content. |
| Download Translated Document | `downloadDocument` | Downloads the translated document once its status is done. Returns the translated file content. The document can only be downloaded once and is then deleted by DeepL. |
| Get Admin Custom Tag Analytics | `adminGetCustomTagAnalytics` | Admin API: usage statistics grouped by the X-DeepL-Reporting-Tag values sent with translation requests. Requires a DeepL API Pro account with the Admin API entitlement; Pro host (api.deepl.com) only. Without the entitlement DeepL answers 403 Forbidden. |
| Get Admin Usage Analytics | `adminGetAnalytics` | Admin API: usage statistics per developer key for a date range. Requires a DeepL API Pro account with the Admin API entitlement and an admin key, and only exists on the Pro host (api.deepl.com) - set the connection's host accordingly. Without the entitlement DeepL answers 403 {"message":"Forbidden. ..."}. |
| Get Document Translation Status | `getDocumentStatus` | Polls the translation status of an uploaded document. Status is queued, translating, done or error. Poll this until status is done, then call Download Translated Document. |
| Get Glossary (v2) | `getGlossaryV2` | Retrieves metadata for one v2 glossary by id: name, language pair, entry count and readiness. |
| Get Glossary Entries (v2) | `getGlossaryEntriesV2` | Returns the term pairs of a v2 glossary as tab-separated values (one source/target pair per line). |
| Get Multilingual Glossary (v3) | `getMultilingualGlossary` | Retrieves one multilingual (v3) glossary by id, including the list of dictionaries it contains. |
| Get Multilingual Glossary Entries (v3) | `getMultilingualGlossaryEntries` | Returns the entries of one dictionary inside a multilingual (v3) glossary, selected by source_lang and target_lang. |
| Get Spoken Terms Collection | `getSpokenTerms` | Retrieves one spoken terms collection by id, with its per-language term lists and entry counts. |
| Get Spoken Terms Entries | `getSpokenTermsEntries` | Returns the term entries of one language inside a spoken terms collection. |
| Get Style Custom Instruction | `getCustomInstruction` | Retrieves one custom instruction of a style rule list by its id. |
| Get Style Rule List | `getStyleRuleList` | Retrieves one style rule list by style_id, including its configured rules and custom instructions. |
| Get Translation Memory | `getTranslationMemory` | Retrieves one translation memory by id: name, source language, target languages and segment count. |
| Get Translation Memory Job | `getTranslationMemoryJob` | Retrieves the status of a translation memory import or export job, including the resulting translation_memory_id once the job has finished. |
| Get Usage and Limits | `getUsage` | Returns the character count translated so far in the current billing period and the plan's character limit. Use this before running translations to check remaining quota. |
| Get Voice Realtime Streaming URL | `getVoiceStreamingUrl` | DeepL Voice realtime: opens a session and returns the WebSocket streaming_url plus a session token for live speech translation. Pro host only (this route does not exist on api-free.deepl.com); requires a DeepL Voice entitlement. |
| Get Voice Translation Job Status | `getVoiceTranslateJobStatus` | DeepL Voice: returns the status of a voice translation job, its usage and, when complete, a download_url per target. Requires a DeepL Voice entitlement; accounts without it get 403 Forbidden. |
| List Admin Developer Keys | `adminListDeveloperKeys` | SECURITY WARNING: this Admin API endpoint returns the account's own DeepL developer API keys. Treat its response as a live credential - never log it, store it, or forward it to another system. Requires a DeepL API Pro account with the Admin API entitlement; Pro host (api.deepl.com) only. Without the entitlement DeepL answers 403 Forbidden. |
| List Glossaries (v2) | `listGlossariesV2` | Lists all single language-pair (v2) glossaries owned by the account. |
| List Glossary Language Pairs | `listGlossaryLanguagePairs` | Lists the source/target language pairs that DeepL glossaries can be created for. |
| List Language Resources (v3) | `listLanguageResources` | Lists every DeepL resource (translate_text, write, glossary, voice, ...) together with the features each one supports, such as formality, glossary or tag handling. |
| List Languages For Resource (v3) | `listLanguagesV3` | Lists the languages available for one DeepL resource (translate_text, translate_document, glossary, voice, write, style_rules, translation_memory), including which are usable as source and target. |
| List Multilingual Glossaries (v3) | `listMultilingualGlossaries` | Lists all multilingual (v3) glossaries owned by the account, each with its dictionaries and entry counts. |
| List Spoken Terms Collections | `listSpokenTerms` | Lists all spoken terms collections owned by the account. |
| List Style Rule Lists | `listStyleRuleLists` | Lists the account's style rule lists. Pass detailed=true to include each list's configured rules and custom instructions. NOTE: page is ZERO-BASED - page=0 is the first page; page=1 on a single-page account returns an empty style_rules array. |
| List Supported Languages (v2) | `listLanguagesV2` | Lists the languages supported for translation. Pass type=source or type=target to choose the direction. |
| List Translation Memories | `listTranslationMemories` | Lists the account's translation memories with their segment counts and language directions. |
| List Translation Memory Segments | `getTranslationMemorySegments` | Lists the source/target segment pairs stored in a translation memory. Supports cursor paging and a text filter. |
| Reconnect Voice Realtime Session | `requestVoiceReconnection` | DeepL Voice realtime: exchanges an existing session token for a fresh streaming_url so a dropped WebSocket can be resumed. Pro host only; requires a DeepL Voice entitlement. |
| Rename Admin Developer Key | `adminRenameDeveloperKey` | Admin API: changes the label of one DeepL developer key. Requires a DeepL API Pro account with the Admin API entitlement; Pro host (api.deepl.com) only. Without the entitlement DeepL answers 403 Forbidden. |
| Rename Style Rule List | `updateStyleRuleList` | Changes the name of a style rule list. Returns the updated list. |
| Rephrase Text (DeepL Write) | `rephraseText` | DeepL Write: rewrites text to improve clarity, style or tone. Returns improvements[] with the improved text. |
| Replace Glossary Dictionary (v3) | `replaceGlossaryDictionary` | Replaces, or creates, the dictionary for one language pair inside a multilingual (v3) glossary. Returns the resulting entry_count. |
| Replace Spoken Terms List | `putSpokenTermsList` | Replaces, or creates, the term list for one language inside a spoken terms collection. Returns the resulting entry_count. |
| Replace Style Custom Instruction | `updateCustomInstruction` | Replaces the label, prompt and source language of one custom instruction in a style rule list. |
| Replace Style Rule Configured Rules | `updateStyleRuleConfiguredRules` | Replaces the whole configured_rules object of a style rule list. Groups are dates_and_times, formatting, numbers, punctuation, spelling_and_grammar, style_and_tone and vocabulary; each holds rule keys with enum option values. Rules not supplied are cleared. |
| Set Admin Developer Key Usage Limits | `adminSetDeveloperKeyUsageLimits` | Admin API: sets per-key character and speech-to-text usage limits. Requires a DeepL API Pro account with the Admin API entitlement; Pro host (api.deepl.com) only. Without the entitlement DeepL answers 403 Forbidden. |
| Start Translation Memory Export | `createTranslationMemoryExport` | Starts an export job that writes a translation memory back out as TMX. Returns a job_id to poll with Get Translation Memory Job, whose results carry the download link. |
| Start Translation Memory Import | `createTranslationMemoryImport` | Starts an import job for a TMX translation memory file. Returns job_id plus a pre-signed upload_url; the TMX file must then be PUT to that upload_url by the caller. Poll Get Translation Memory Job for progress. |
| Translate Text | `translateText` | Translates one or more text strings into a target language. Billed per source character. Returns translations[] with the translated text and the detected source language. |
| Translate Text (Legacy v1 Endpoint) | `translateTextLegacyV1` | Legacy POST /v1/translate alias of the text translation endpoint. Not present in DeepL's published OpenAPI spec but live and returning the same translations[] shape. Prefer Translate Text; kept for clients still pinned to v1. |
| Update Multilingual Glossary (v3) | `patchMultilingualGlossary` | Renames a multilingual (v3) glossary and/or merges dictionaries into it. Only the supplied fields change. |
| Update Spoken Terms Collection | `patchSpokenTerms` | Renames a spoken terms collection and/or merges term lists into it. Only the supplied fields change. |
| Upload Document For Translation | `translateDocument` | Uploads a document (txt, docx, pptx, xlsx, pdf, html, xlf) and starts its translation. Sends multipart/form-data. Returns document_id and document_key, which are both required to poll status and download the result. Billed per character of the document; the DeepL API Free plan also caps documents per month. |
