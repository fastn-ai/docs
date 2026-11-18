---
description: "ChatBotKit is an AI agent infrastructure platform for building, deploying and operating production AI agents."
hidden: true
---

# ChatBotKit

<img src="../../.gitbook/assets/connectors/lg/chatbotkit.png" alt="ChatBotKit logo">

ChatBotKit is an AI agent infrastructure platform for building, deploying and operating production AI agents. This connector covers the full ChatBotKit REST API v1: bots, blueprints, datasets and files, skillsets and abilities, conversations and messages, contacts, memories, secrets, spaces and storage, tasks and executions, users and user tokens, portals, policies, magic prompts, usage, platform catalog, GraphQL, the OpenAI-compatible chat completions endpoint and every integration type (widget, Slack, Discord, WhatsApp, Telegram, Messenger, Instagram, Twilio, email, Google Chat, Microsoft Teams, Notion, GitHub, sitemap, trigger, extract, support, SkillServer and more).

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [chatbotkit.com](https://chatbotkit.com) |
| **Authentication** | Bearer token |
| **Slug** | `chatbotkit` |

## Use it

Add ChatBotKit from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chatbotkit.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Attach Dataset File | `attachDatasetFile` | Attach a file to a dataset as a source. |
| Attach Widget Integration File | `attachWidgetIntegrationFile` | Attach a file to a widget integration. |
| Authenticate Contact Secret | `authenticateContactSecret` | Start authentication for a contact's personal secret (returns the URL to complete authentication). |
| Authenticate Secret | `authenticateSecret` | Start authentication for an OAuth secret and return the URL the user must open to complete it. |
| Cancel Task | `cancelTask` | Cancel a running task by id. |
| Cancel Task Execution | `cancelTaskExecution` | Cancel a specific execution of a task. |
| Clone Blueprint | `cloneBlueprint` | Clone a blueprint and its resources. |
| Clone Bot | `cloneBot` | Clone a bot. |
| Clone Platform Example | `clonePlatformExample` | Clone a platform example into your account, creating its bots, datasets, skillsets and integrations; returns the created resources grouped by type. |
| Clone Widget Integration | `cloneWidgetIntegration` | Clone a Widget integration. |
| Compact Conversation | `compactConversation` | Compact a conversation into a checkpoint message. |
| Compact Conversation Stateless | `compactConversationStateless` | Compact an array of messages into a single summary (stateless). |
| Complete Conversation | `completeConversation` | Stateless completion: generate the next bot message for a given list of messages without persisting a conversation. |
| Complete Conversation Message | `completeConversationMessage` | Send a user message to a conversation and receive the bot response in one call. |
| Copy Space Storage File | `copySpaceStoragePath` | Copy a file within a space's storage from the source path to a destination path. |
| Create Blueprint | `createBlueprint` | Create a blueprint. |
| Create Blueprint Bulletin | `createBlueprintBulletin` | Post a bulletin to a blueprint's shared board. |
| Create Bot | `createBot` | Create bot. |
| Create Bot Session | `createBotSession` | Create a bot session: a new conversation for the bot plus a client-side session token. |
| Create Chat Completion | `createChatCompletion` | Create a chat completion through ChatBotKit's OpenAI-compatible endpoint. Set model to a selector such as model/name=gpt-4o-mini or bot/id=&lt;botId&gt; and pass the messages array; supports tool calling and streaming (stream true returns a text event stream). |
| Create Contact | `createContact` | Create a new contact. |
| Create Conversation | `createConversation` | Create a new conversation with the given parameters and optional messages. |
| Create Conversation Message | `createConversationMessage` | Create a message in a conversation (no completion is generated). |
| Create Conversation Session | `createConversationSession` | Create a conversation session token that lets client-side applications authenticate for a single conversation. |
| Create Dataset | `createDataset` | Create a dataset. |
| Create Dataset Record | `createDatasetRecord` | Create a record in a dataset. |
| Create Discord Integration | `createDiscordIntegration` | Create a Discord integration. |
| Create Email Integration | `createEmailIntegration` | Create an Email integration. |
| Create Extract Integration | `createExtractIntegration` | Create an Extract integration. |
| Create File | `createFile` | Create a file record (upload content afterwards with Upload File). |
| Create GitHub Integration | `createGithubIntegration` | Create a GitHub integration. |
| Create Google Chat Integration | `createGoogleChatIntegration` | Create a Google Chat integration. |
| Create Instagram Integration | `createInstagramIntegration` | Create an Instagram integration. |
| Create MCP Server Integration | `createMcpServerIntegration` | Create an MCP Server integration. |
| Create Memory | `createMemory` | Create a new memory with the given parameters. |
| Create Messenger Integration | `createMessengerIntegration` | Create a Messenger integration. |
| Create Microsoft Teams Integration | `createMicrosoftTeamsIntegration` | Create a Microsoft Teams integration. |
| Create Notion Integration | `createNotionIntegration` | Create a Notion integration. |
| Create Policy | `createPolicy` | Create a retention or usage policy, globally or scoped to a bot, with its JSON configuration and state. |
| Create Portal | `createPortal` | Create a portal (a hosted, branded chat page) with a slug and configuration. |
| Create Secret | `createSecret` | Create a secret (plain, basic, bearer, JWT, OAuth, template or reference) with its value and configuration, for injection into abilities and proxied requests. |
| Create Sitemap Integration | `createSitemapIntegration` | Create a Sitemap integration. |
| Create SkillServer Integration | `createSkillServerIntegration` | Create a SkillServer integration. |
| Create Skillset | `createSkillset` | Create a skillset with an optional name, description, metadata, blueprint, visibility and state. |
| Create Skillset Ability | `createSkillsetAbility` | Create an ability in a skillset with a name, description and instruction, optionally linking a secret, file, bot or space. |
| Create Slack Integration | `createSlackIntegration` | Create a Slack integration. |
| Create Space | `createSpace` | Create a space (a file storage and site workspace) with an optional name, description, metadata, blueprint and contact. |
| Create Space Site | `createSpaceSite` | Create a static site served from a space's storage under a subdomain slug, with optional folder prefix, index and not-found filenames. |
| Create Support Integration | `createSupportIntegration` | Create a Support integration. |
| Create Task | `createTask` | Create a scheduled task that runs a bot autonomously: set the bot, an optional contact, a cron or date schedule with timezone, expiry and execution limits (iterations, time, tool calls). |
| Create Telegram Integration | `createTelegramIntegration` | Create a Telegram integration. |
| Create Trigger Integration | `createTriggerIntegration` | Create a Trigger integration. |
| Create Twilio Integration | `createTwilioIntegration` | Create a Twilio integration. |
| Create User | `createUser` | Create a user (an end user of your multi-tenant application) with an optional name, email, image, metadata and resource limits. |
| Create User Context | `createUserContext` | Create a context for a user, holding a free-form payload with optional name, description and metadata. |
| Create User Session | `createUserSession` | Create a temporary session token for a user, with an optional lifetime, allowed API route patterns and contact id embedded in the token. |
| Create User Token | `createUserToken` | Create an API token for a user; the token value is returned only in this response. |
| Create WhatsApp Integration | `createWhatsAppIntegration` | Create a WhatsApp integration. |
| Create Widget Integration | `createWidgetIntegration` | Create a Widget integration. |
| Delete Blueprint | `deleteBlueprint` | Delete a blueprint, optionally deleting all resources associated with it. |
| Delete Bot | `deleteBot` | Delete a bot. |
| Delete Contact | `deleteContact` | Delete a contact. |
| Delete Conversation | `deleteConversation` | Delete a conversation. |
| Delete Conversation Message | `deleteConversationMessage` | Delete a conversation message. |
| Delete Dataset | `deleteDataset` | Delete a dataset. |
| Delete Dataset Record | `deleteDatasetRecord` | Delete a record from a dataset. |
| Delete Discord Integration | `deleteDiscordIntegration` | Delete a Discord integration. |
| Delete Email Integration | `deleteEmailIntegration` | Delete an Email integration. |
| Delete Extract Integration | `deleteExtractIntegration` | Delete an Extract integration. |
| Delete File | `deleteFile` | Delete a file. |
| Delete GitHub Integration | `deleteGithubIntegration` | Delete a GitHub integration. |
| Delete Google Chat Integration | `deleteGoogleChatIntegration` | Delete a Google Chat integration. |
| Delete Instagram Integration | `deleteInstagramIntegration` | Delete an Instagram integration. |
| Delete MCP Server Integration | `deleteMcpServerIntegration` | Delete an MCP Server integration. |
| Delete Memory | `deleteMemory` | Delete memory. |
| Delete Messenger Integration | `deleteMessengerIntegration` | Delete a Messenger integration. |
| Delete Microsoft Teams Integration | `deleteMicrosoftTeamsIntegration` | Delete a Microsoft Teams integration. |
| Delete Notion Integration | `deleteNotionIntegration` | Delete a Notion integration. |
| Delete Policy | `deletePolicy` | Delete a policy by id. |
| Delete Portal | `deletePortal` | Delete a portal by id. |
| Delete Secret | `deleteSecret` | Delete a secret by id. |
| Delete Sitemap Integration | `deleteSitemapIntegration` | Delete a Sitemap integration. |
| Delete SkillServer Integration | `deleteSkillServerIntegration` | Delete a SkillServer integration. |
| Delete Skillset | `deleteSkillset` | Delete a skillset by id. |
| Delete Skillset Ability | `deleteSkillsetAbility` | Delete an ability from a skillset by id. |
| Delete Slack Integration | `deleteSlackIntegration` | Delete a Slack integration. |
| Delete Space | `deleteSpace` | Delete a space by id. |
| Delete Space Site | `deleteSpaceSite` | Delete a space site by id. |
| Delete Space Storage Path | `deleteSpaceStoragePath` | Delete a file or directory from a space's storage, optionally deleting directory contents recursively. |
| Delete Support Integration | `deleteSupportIntegration` | Delete a Support integration. |
| Delete Task | `deleteTask` | Delete a task by id. |
| Delete Telegram Integration | `deleteTelegramIntegration` | Delete a Telegram integration. |
| Delete Trigger Integration | `deleteTriggerIntegration` | Delete a Trigger integration. |
| Delete Twilio Integration | `deleteTwilioIntegration` | Delete a Twilio integration. |
| Delete User | `deleteUser` | Delete a user by id. |
| Delete User Context | `deleteUserContext` | Delete a user context by id. |
| Delete User Token | `deleteUserToken` | Delete one of a user's API tokens by id. |
| Delete WhatsApp Integration | `deleteWhatsAppIntegration` | Delete a WhatsApp integration. |
| Delete Widget Integration | `deleteWidgetIntegration` | Delete a Widget integration. |
| Detach Dataset File | `detachDatasetFile` | Detach a file from a dataset, optionally deleting the records derived from it. |
| Detach Widget Integration File | `detachWidgetIntegrationFile` | Detach a file from a widget integration. |
| Dispatch Conversation | `dispatchConversation` | Dispatch a stateless conversation completion to run asynchronously in the background; returns a channel ID to subscribe to for completion events. |
| Dispatch Stateful Conversation | `dispatchStatefulConversation` | Dispatch a stateful conversation completion to run asynchronously in the background; returns a channel ID to subscribe to for completion events. |
| Download File | `downloadFile` | Get a download URL for a file. |
| Download Space Storage File | `downloadSpaceStoragePath` | Get a presigned download URL for a file in a space's storage. |
| Downvote Bot | `downvoteBot` | Downvote a bot. |
| Downvote Conversation | `downvoteConversation` | Downvote a conversation. |
| Downvote Conversation Message | `downvoteConversationMessage` | Downvote a conversation message. |
| Ensure Contact | `ensureContact` | Ensure a contact with the given fingerprint exists, creating it if necessary. |
| Execute Skillset Ability | `executeSkillsetAbility` | Execute a specific ability from a skillset with the provided input, which can be structured (JSON or YAML) or natural-language text; returns the result, generated messages and token usage. |
| Export Blueprint Resources | `exportBlueprintResources` | Export a blueprint and all its resources. |
| Export Contacts | `exportContacts` | Export contacts. |
| Export Conversations | `exportConversations` | Export conversations. |
| Export Dataset Records | `exportDatasetRecords` | Export dataset records. |
| Export Event Logs | `exportEventLogs` | Export event logs. |
| Export Extract Integration Items | `exportExtractIntegrationItems` | Export the extracted data items of an Extract integration. |
| Export Memories | `exportMemories` | Export memories. |
| Export Skillset Abilities | `exportSkillsetAbilities` | Export the abilities of a skillset as a paginated list of full ability records. |
| Export Spaces | `exportSpaces` | Export spaces as a paginated list of full space records, optionally filtered by metadata. |
| Export Tasks | `exportTasks` | Export tasks as a paginated list of full task records, optionally filtered by metadata. |
| Fetch Blueprint | `fetchBlueprint` | Fetch a blueprint. |
| Fetch Bot | `fetchBot` | Fetch a bot. |
| Fetch Bot Usage | `fetchBotUsage` | Retrieve usage statistics for a specific bot, including total tokens (BASE type only), total conversations, and total messages. |
| Fetch Contact | `fetchContact` | Fetch a contact. |
| Fetch Conversation | `fetchConversation` | Fetch a conversation. |
| Fetch Conversation Message | `fetchConversationMessage` | Fetch a conversation message. |
| Fetch Conversation Usage | `fetchConversationUsage` | Retrieve usage statistics for a specific conversation, including total tokens (BASE type only) and total messages. |
| Fetch Dataset | `fetchDataset` | Fetch a dataset. |
| Fetch Dataset Record | `fetchDatasetRecord` | Fetch a record from a dataset. |
| Fetch Discord Integration | `fetchDiscordIntegration` | Fetch a Discord integration. |
| Fetch Email Integration | `fetchEmailIntegration` | Fetch an Email integration. |
| Fetch Extract Integration | `fetchExtractIntegration` | Fetch an Extract integration. |
| Fetch File | `fetchFile` | Fetch a file record. |
| Fetch GitHub Integration | `fetchGithubIntegration` | Fetch a GitHub integration. |
| Fetch Google Chat Integration | `fetchGoogleChatIntegration` | Fetch a Google Chat integration. |
| Fetch Instagram Integration | `fetchInstagramIntegration` | Fetch an Instagram integration. |
| Fetch MCP Server Integration | `fetchMcpServerIntegration` | Fetch an MCP Server integration. |
| Fetch Memory | `fetchMemory` | Fetch memory. |
| Fetch Messenger Integration | `fetchMessengerIntegration` | Fetch a Messenger integration. |
| Fetch Microsoft Teams Integration | `fetchMicrosoftTeamsIntegration` | Fetch a Microsoft Teams integration. |
| Fetch Notion Integration | `fetchNotionIntegration` | Fetch a Notion integration. |
| Fetch Platform Example | `fetchPlatformExample` | Fetch a platform example by its id (slug) with its full configuration. |
| Fetch Policy | `fetchPolicy` | Fetch a policy by id. |
| Fetch Portal | `fetchPortal` | Fetch a portal by id. |
| Fetch Secret | `fetchSecret` | Fetch a secret by id. The secret value is never returned; config.clientSecret is masked. |
| Fetch Sitemap Integration | `fetchSitemapIntegration` | Fetch a Sitemap integration. |
| Fetch SkillServer Integration | `fetchSkillServerIntegration` | Fetch a SkillServer integration. |
| Fetch SkillServer Manual | `fetchSkillServerManual` | Fetch the SkillServer manual: a text-first (markdown) manual describing the abilities exposed by this skill server and how to invoke them. |
| Fetch Skillset | `fetchSkillset` | Fetch a skillset by id. |
| Fetch Skillset Ability | `fetchSkillsetAbility` | Fetch an ability from a skillset by id. |
| Fetch Slack Integration | `fetchSlackIntegration` | Fetch a Slack integration. |
| Fetch Space | `fetchSpace` | Fetch a space by id. |
| Fetch Space Site | `fetchSpaceSite` | Fetch a space site by id. |
| Fetch Support Integration | `fetchSupportIntegration` | Fetch a Support integration. |
| Fetch Task | `fetchTask` | Fetch a task by id, including its schedule, limits, status, outcome and run timestamps. |
| Fetch Telegram Integration | `fetchTelegramIntegration` | Fetch a Telegram integration. |
| Fetch Trigger Integration | `fetchTriggerIntegration` | Fetch a Trigger integration. |
| Fetch Twilio Integration | `fetchTwilioIntegration` | Fetch a Twilio integration. |
| Fetch Usage | `fetchUsage` | Fetch the account's usage for the current billing period: tokens, conversations, messages and database object counts. |
| Fetch Usage Series | `fetchUsageSeries` | Fetch daily usage data points (tokens, conversations and messages) for the account over the last 90 days. |
| Fetch User | `fetchUser` | Fetch a user by id, including its name, email, image, metadata and resource limits. |
| Fetch User Context | `fetchUserContext` | Fetch a user context by id, including its payload and linked resource ids. |
| Fetch WhatsApp Integration | `fetchWhatsAppIntegration` | Fetch a WhatsApp integration. |
| Fetch Widget Integration | `fetchWidgetIntegration` | Fetch a Widget integration. |
| Generate Magic From Prompt | `generateMagicFromPrompt` | Generate text (description, records, abilities and more) based on input using a magic prompt. |
| Generate Platform Report | `generatePlatformReport` | Generate a specific platform report by report ID (from List Platform Reports) for a period in days; bot-scoped reports also take a botId. |
| Generate Platform Reports | `generatePlatformReports` | Generate multiple platform reports in a single request. Provide a JSON object mapping each report ID (from List Platform Reports) to its input parameters, for example {"&lt;reportId&gt;": {"periodDays": 7}}; the response maps the same keys to each report's output or error. |
| Import Blueprint Resources | `importBlueprintResources` | Import resources into an existing blueprint, reconciling resources by alias. |
| Initiate Discord Integration | `initiateDiscord` | Initiates a conversation through a Discord integration by sending a text message to a Discord channel. |
| Initiate Email Integration | `initiateEmail` | Initiates a conversation through an email integration by sending an email with the given subject and text instruction to an address. |
| Initiate Google Chat Integration | `initiateGooglechat` | Initiates a conversation through a Google Chat integration by sending a text message to a Google Chat space or user. |
| Initiate Instagram Integration | `initiateInstagram` | Initiates a conversation through an Instagram integration by sending a free-form text message from a professional account to a recipient who interacted with it before. |
| Initiate Messenger Integration | `initiateMessenger` | Initiates a conversation through a Facebook Messenger integration by sending a free-form text message from a Page to a recipient who interacted with it before. |
| Initiate Microsoft Teams Integration | `initiateTeams` | Initiates a conversation through a Microsoft Teams integration by sending a text message to a Bot Framework conversation. |
| Initiate Recall Integration | `initiateRecall` | Initiates a meeting session through a Recall integration: the bot joins the given meeting URL with the provided instruction text and optional display name. |
| Initiate Slack Integration | `initiateSlack` | Initiates a conversation through a Slack integration by sending a text instruction to a Slack channel or user. |
| Initiate Telegram Integration | `initiateTelegram` | Initiates a conversation through a Telegram integration by sending a text instruction to a Telegram chat, user, group or channel. |
| Initiate Twilio Integration | `initiateTwilio` | Initiates a conversation through a Twilio integration by SMS or voice call from a Twilio sender number to a recipient, using the given text instruction. |
| Initiate WhatsApp Integration | `initiateWhatsapp` | Initiates a proactive WhatsApp conversation through a WhatsApp integration by sending a free-form text message to a recipient within an active customer service window. |
| Invoke SkillServer Ability | `invokeSkillServerAbility` | Directly invoke a single ability from the skillset linked to a SkillServer integration, by ability name. |
| Invoke Trigger Integration | `invokeTriggerIntegration` | Invoke a Trigger integration. |
| List Blueprint Bulletins | `listBlueprintBulletins` | List the bulletins on a blueprint's shared board. |
| List Blueprint Resources | `listBlueprintResources` | List the resources of a blueprint. |
| List Blueprints | `listBlueprints` | Retrieve a list of blueprints. |
| List Bots | `listBots` | Retrieve a list of bots. |
| List Contact Conversations | `listContactConversations` | List the conversations of a contact. |
| List Contact Memories | `listContactMemories` | List the memories of a contact. |
| List Contact Ratings | `listContactRatings` | List the ratings given by a contact. |
| List Contact Secrets | `listContactSecrets` | List the personal secrets of a contact. |
| List Contact Spaces | `listContactSpaces` | List the spaces of a contact. |
| List Contact Tasks | `listContactTasks` | List the tasks of a contact. |
| List Contacts | `listContacts` | List contacts. |
| List Conversation Attachments | `listConversationAttachments` | List the attachments of a conversation. |
| List Conversation Messages | `listConversationMessages` | List the messages of a conversation. |
| List Conversations | `listConversations` | List conversations. |
| List Dataset Files | `listDatasetFiles` | Retrieve a list of files attached to a dataset. |
| List Dataset Records | `listDatasetRecords` | Retrieve a list of dataset records. |
| List Datasets | `listDatasets` | Retrieve a list of datasets. |
| List Discord Integrations | `listDiscordIntegrations` | List Discord integrations. |
| List Email Integrations | `listEmailIntegrations` | List Email integrations. |
| List Event Logs | `listEventLogs` | List event logs. |
| List Extract Integration Items | `listExtractIntegrationItems` | List the extracted data items of an Extract integration. |
| List Extract Integrations | `listExtractIntegrations` | List Extract integrations. |
| List Files | `listFiles` | Retrieve a list of files. |
| List GitHub Integrations | `listGithubIntegrations` | List GitHub integrations. |
| List Google Chat Integrations | `listGoogleChatIntegrations` | List Google Chat integrations. |
| List Instagram Integrations | `listInstagramIntegrations` | List Instagram integrations. |
| List Magic Prompts | `listMagicPrompts` | Retrieve a list of magic prompts. |
| List MCP Server Integrations | `listMcpServerIntegrations` | List MCP Server integrations. |
| List Memories | `listMemories` | List memories. |
| List Messenger Integrations | `listMessengerIntegrations` | List Messenger integrations. |
| List Microsoft Teams Integrations | `listMicrosoftTeamsIntegrations` | List Microsoft Teams integrations. |
| List Notion Integrations | `listNotionIntegrations` | List Notion integrations. |
| List Platform Abilities | `listPlatformAbilities` | Retrieve a list of platform abilities. |
| List Platform Actions | `listPlatformActions` | Retrieve a list of platform actions. |
| List Platform Examples | `listPlatformExamples` | Retrieve a paginated list of the platform catalog's examples (blueprints, projects and integration templates). |
| List Platform Models | `listPlatformModels` | Retrieve a paginated list of the AI models available on the platform (language, image, video or rerank), with provider, family and token limits. |
| List Platform Reports | `listPlatformReports` | Retrieve a list of the platform reports available to generate, with their ids, names and descriptions. |
| List Platform Secrets | `listPlatformSecrets` | Retrieve a paginated list of the platform catalog's secret templates (pre-configured OAuth apps and credential types). |
| List Policies | `listPolicies` | Retrieve a paginated list of retention and usage policies, optionally filtered by the bot they apply to or by metadata. |
| List Portals | `listPortals` | Retrieve a paginated list of portals (hosted, branded chat pages), optionally filtered by metadata. |
| List Secrets | `listSecrets` | Retrieve a paginated list of secrets (stored credentials such as API keys, bearer tokens, JWTs and OAuth apps), optionally filtered by metadata. Secret values are never returned. |
| List Sitemap Integrations | `listSitemapIntegrations` | List Sitemap integrations. |
| List SkillServer Integrations | `listSkillServerIntegrations` | List SkillServer integrations. |
| List Skillset Abilities | `listSkillsetAbilities` | Retrieve a paginated list of the abilities in a skillset, each with its instruction and linked resources. |
| List Skillsets | `listSkillsets` | Retrieve a paginated list of skillsets (collections of abilities that extend a bot), optionally filtered by metadata. |
| List Slack Integrations | `listSlackIntegrations` | List Slack integrations. |
| List Space Sites | `listSpaceSites` | Retrieve a paginated list of the static sites served from a space, optionally filtered by metadata. |
| List Space Storage Files | `listSpaceStoragePath` | List the files and directories under a path in a space's storage, optionally recursively. |
| List Spaces | `listSpaces` | Retrieve a paginated list of spaces (file storage and site workspaces), optionally filtered by metadata. |
| List Support Integrations | `listSupportIntegrations` | List Support integrations. |
| List Task Executions | `listTaskExecutions` | Retrieve a paginated list of a task's executions with their status, outcome, summary and related conversation, optionally filtered by status or metadata. |
| List Tasks | `listTasks` | Retrieve a paginated list of scheduled tasks, optionally filtered by blueprint, bot, contact, status or metadata. |
| List Teams | `listTeams` | Retrieve a paginated list of the teams the account belongs to. |
| List Telegram Integrations | `listTelegramIntegrations` | List Telegram integrations. |
| List Trigger Integrations | `listTriggerIntegrations` | List Trigger integrations. |
| List Twilio Integrations | `listTwilioIntegrations` | List Twilio integrations. |
| List Usage Records | `listUsageRecords` | Retrieve a paginated list of usage records (type and count with the related conversation, message, task, contact, bot, dataset, skillset or ability ids). |
| List User Contexts | `listUserContexts` | Retrieve a paginated list of a user's contexts, optionally filtered by blueprint, bot, dataset or skillset. |
| List User Tokens | `listUserTokens` | Retrieve a paginated list of the API tokens issued to a user. |
| List Users | `listUsers` | Retrieve a paginated list of users (end users of your multi-tenant application), optionally filtered by a metadata key and value. |
| List WhatsApp Integrations | `listWhatsAppIntegrations` | List WhatsApp integrations. |
| List Widget Integrations | `listWidgetIntegrations` | List Widget integrations. |
| Mint Contact Secret | `mintContactSecret` | Mint a usable token from a contact's personal secret. |
| Mint Secret Token | `mintSecret` | Mint a usable token from a secret: a refreshed OAuth access token, a freshly signed JWT or the stored bearer token, with its expiry. |
| Move Space Storage File | `moveSpaceStoragePath` | Move or rename a file in a space's storage by moving it from the source path to a destination path. |
| Proxy Contact Secret | `proxyContactSecret` | Perform an outbound HTTP request with a contact's personal secret injected into the request headers at egress. |
| Proxy Request With Secret | `proxySecret` | Perform an outbound HTTP request through ChatBotKit with a secret injected into the request headers at egress, so the credential never leaves the platform. Returns the upstream response body. |
| Publish Channel Message | `publishChannelMessage` | Publish a message to a channel. |
| Receive Conversation Message | `receiveConversationMessage` | Receive the bot response for a conversation (generates the next bot message from the current conversation state). |
| Revoke Contact Secret | `revokeContactSecret` | Revoke a contact's personal secret. |
| Revoke Secret | `revokeSecret` | Revoke a secret's stored authentication (for example an OAuth authorization) without deleting the secret. |
| Run GraphQL Query | `graphql` | Execute a GraphQL query or mutation against the ChatBotKit GraphQL endpoint, with optional variables and operation name. |
| Search Bot Memory | `searchBotMemory` | Search memories for a specific bot. |
| Search Contact Memory | `searchContactMemory` | Search memories for a specific contact. |
| Search Dataset | `searchDataset` | Search a dataset for records matching a given search query. |
| Search Memory | `searchMemory` | Search memories for records matching a given search query. |
| Search Platform Abilities | `searchPlatformAbilities` | Search platform abilities. |
| Search Platform Examples | `searchPlatformExamples` | Search the platform catalog of examples (blueprints, projects and integration templates) by text. |
| Search Platform Secrets | `searchPlatformSecrets` | Search the platform catalog of secret templates (pre-configured integrations such as OAuth apps) by text and return ranked matches with setup details. |
| Send Conversation Message | `sendConversationMessage` | Send a user message to a conversation (does not generate a reply; use Receive Conversation Message afterwards). |
| Setup Discord Integration | `setupDiscordIntegration` | Setup a Discord integration. |
| Setup Email Integration | `setupEmailIntegration` | Setup an Email integration. |
| Setup GitHub Integration | `setupGithubIntegration` | Validate a GitHub integration's App credentials. |
| Setup Google Chat Integration | `setupGoogleChatIntegration` | Setup a Google Chat integration. |
| Setup Instagram Integration | `setupInstagramIntegration` | Setup an Instagram integration. |
| Setup Messenger Integration | `setupMessengerIntegration` | Setup a Messenger integration. |
| Setup Microsoft Teams Integration | `setupMicrosoftTeamsIntegration` | Set up a Microsoft Teams integration. |
| Setup Slack Integration | `setupSlackIntegration` | Setup a Slack integration. |
| Setup Telegram Integration | `setupTelegramIntegration` | Setup a Telegram integration. |
| Setup Trigger Integration | `setupTriggerIntegration` | Setup a Trigger integration. |
| Setup Twilio Integration | `setupTwilioIntegration` | Setup a Twilio integration. |
| Setup WhatsApp Integration | `setupWhatsAppIntegration` | Setup a WhatsApp integration. |
| Setup Widget Integration | `setupWidgetIntegration` | Setup a Widget integration. |
| Subscribe Channel Messages | `subscribeChannelMessages` | Subscribe to a channel to receive real-time messages published to it. The response is a newline-delimited JSON (jsonl) event stream returned as raw text. |
| Subscribe Conversation Channel | `subscribeConversationChannel` | Subscribe to a conversation's live monitor channel (message, operation, completion and error events). The response is a newline-delimited JSON (jsonl) event stream returned as raw text. |
| Subscribe Event Logs | `subscribeEventLogs` | Subscribe to receive real-time event logs as they are generated. The response is a newline-delimited JSON (jsonl) event stream returned as raw text. |
| Subscribe Task Workflow Events | `subscribeTaskWorkflowEvents` | Subscribe to real-time task workflow events (operation begin, operation end and error events) for a task while an execution is running. The response is a newline-delimited JSON event stream that stays open while events arrive. |
| Sync Dataset File | `syncDatasetFile` | Sync a file attached to a dataset (re-ingest its records). |
| Sync File | `syncFile` | Sync a file. |
| Sync Notion Integration | `syncNotionIntegration` | Trigger a sync of a Notion integration. |
| Sync Sitemap Integration | `syncSitemapIntegration` | Trigger a sync of a Sitemap integration. |
| Synthesize Conversation Message | `synthesizeConversationMessage` | Synthesize (text-to-speech) a conversation message. |
| Trigger Extract Integration | `triggerExtractIntegration` | Trigger an extract integration on historic conversations. |
| Trigger Support Integration | `triggerSupportIntegration` | Trigger a support integration on historic conversations. |
| Trigger Task | `triggerTask` | Manually trigger a task to execute immediately, regardless of its schedule. |
| Update Blueprint | `updateBlueprint` | Update a blueprint. |
| Update Bot | `updateBot` | Update a bot. |
| Update Contact | `updateContact` | Update a contact. |
| Update Conversation | `updateConversation` | Update a conversation. |
| Update Conversation Message | `updateConversationMessage` | Update a conversation message. |
| Update Dataset | `updateDataset` | Update a dataset. |
| Update Dataset Record | `updateDatasetRecord` | Update a dataset record. |
| Update Discord Integration | `updateDiscordIntegration` | Update a Discord integration. |
| Update Email Integration | `updateEmailIntegration` | Update an Email integration. |
| Update Extract Integration | `updateExtractIntegration` | Update an Extract integration. |
| Update File | `updateFile` | Update a file record. |
| Update GitHub Integration | `updateGithubIntegration` | Update a GitHub integration. |
| Update Google Chat Integration | `updateGoogleChatIntegration` | Update a Google Chat integration. |
| Update Instagram Integration | `updateInstagramIntegration` | Update an Instagram integration. |
| Update MCP Server Integration | `updateMcpServerIntegration` | Update an MCP Server integration. |
| Update Memory | `updateMemory` | Update memory. |
| Update Messenger Integration | `updateMessengerIntegration` | Update a Messenger integration. |
| Update Microsoft Teams Integration | `updateMicrosoftTeamsIntegration` | Update a Microsoft Teams integration. |
| Update Notion Integration | `updateNotionIntegration` | Update a Notion integration. |
| Update Policy | `updatePolicy` | Update a policy's name, bot scope, type, state, configuration or metadata. Only the fields you send are changed. |
| Update Portal | `updatePortal` | Update a portal's name, description, metadata, slug or configuration. Only the fields you send are changed. |
| Update Secret | `updateSecret` | Update a secret's name, description, metadata, kind, type, value, configuration or visibility. Only the fields you send are changed. |
| Update Sitemap Integration | `updateSitemapIntegration` | Update a Sitemap integration. |
| Update SkillServer Integration | `updateSkillServerIntegration` | Update a SkillServer integration. |
| Update Skillset | `updateSkillset` | Update a skillset's name, description, metadata, blueprint, visibility or state. Only the fields you send are changed. |
| Update Skillset Ability | `updateSkillsetAbility` | Update a skillset ability's name, description, instruction, linked resources or state. Only the fields you send are changed. |
| Update Slack Integration | `updateSlackIntegration` | Update a Slack integration. |
| Update Space | `updateSpace` | Update a space's name, description, metadata, blueprint or contact. Only the fields you send are changed. |
| Update Space Site | `updateSpaceSite` | Update a space site's name, slug, prefix, index or not-found filename. Only the fields you send are changed. |
| Update Support Integration | `updateSupportIntegration` | Update a Support integration. |
| Update Task | `updateTask` | Update a task's name, bot, contact, schedule, timezone, expiry, metadata or execution limits. Only the fields you send are changed. |
| Update Telegram Integration | `updateTelegramIntegration` | Update a Telegram integration. |
| Update Trigger Integration | `updateTriggerIntegration` | Update a Trigger integration. |
| Update Twilio Integration | `updateTwilioIntegration` | Update a Twilio integration. |
| Update User | `updateUser` | Update a user's name, email, image, metadata or resource limits. Only the fields you send are changed. |
| Update User Context | `updateUserContext` | Update a user context's name, description, metadata or payload. Only the fields you send are changed. |
| Update User Token | `updateUserToken` | Update the name, description, configuration or metadata of a user's API token. Only the fields you send are changed. |
| Update WhatsApp Integration | `updateWhatsAppIntegration` | Update a WhatsApp integration. |
| Update Widget Integration | `updateWidgetIntegration` | Update a Widget integration. |
| Upload Conversation Attachment | `uploadConversationAttachment` | Upload a file as a conversation attachment. The file is sent as an http(s) or data: URL in JSON; direct multipart binary upload is not available through the connector. |
| Upload File | `uploadFile` | Upload content for a file record. The file is sent as an http(s) or data: URL in JSON; direct multipart binary upload is not available through the connector. |
| Upload Space Storage File | `uploadSpaceStoragePath` | Upload a file to a space's storage at the given path. The file is passed as an http: or data: URL in JSON; direct binary upload is not available through the connector. Returns the stored path and, for direct-to-source uploads, the upload request to complete. |
| Upsert Conversation Contact | `upsertConversationContact` | Create or update the contact associated with a conversation. |
| Upvote Bot | `upvoteBot` | Upvote a bot. |
| Upvote Conversation | `upvoteConversation` | Upvote a conversation. |
| Upvote Conversation Message | `upvoteConversationMessage` | Upvote a conversation message. |
| Verify Contact Secret | `verifyContactSecret` | Verify a contact's personal secret (returns its authentication status). |
| Verify Secret | `verifySecret` | Verify whether a secret is authenticated; unauthenticated OAuth secrets return an action with the URL to complete authentication. |
