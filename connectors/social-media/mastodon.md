---
description: "Mastodon is an open-source, self-hostable social network built on ActivityPub."
---

# Mastodon

Mastodon is an open-source, self-hostable social network built on ActivityPub. This connector covers statuses, timelines, accounts, notifications, media, polls, lists, filters, search, trends, moderation and instance metadata on any Mastodon instance.

| | |
| --- | --- |
| **Category** | [Social media](README.md) |
| **Website** | [joinmastodon.org](https://joinmastodon.org) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 242 |
| **Events** | 7 |
| **Slug** | `mastodon` |

## Use it

Add Mastodon from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mastodon.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Follow Request | `acceptFollowRequest` | Approves a pending follow request so the account becomes a follower. |
| Accept Notification Request | `acceptNotificationRequest` | Accepts a filtered-notification request, moving that account's held notifications into the main notification list. |
| Accept Notification Requests | `acceptNotificationRequests` | Accepts several filtered-notification requests at once. |
| Add Account To Collection | `addAccountToCollection` | Features an account in a collection. |
| Add Accounts To List | `addAccountsToList` | Adds accounts to a list. The connected account must already follow every account being added. |
| Add Announcement Reaction | `addAnnouncementReaction` | Adds an emoji reaction to an announcement on behalf of the connected account. |
| Add Filter Keyword | `addFilterKeyword` | Adds a keyword to an existing filter group. |
| Add Status To Filter | `addStatusToFilter` | Adds a specific status to a filter group so that one status is filtered regardless of keywords. |
| Allow Domain | `adminCreateDomainAllow` | Adds a domain to the federation allowlist so this instance will exchange content with it. Requires a moderator or administrator role on the instance. |
| Approve Account | `adminApproveAccount` | Approves a pending sign-up so the account can be used. Requires a moderator or administrator role on the instance. |
| Assign Report To Self | `adminAssignReportToSelf` | Assigns a moderation report to the connected moderator. Requires a moderator or administrator role on the instance. |
| Block Account | `blockAccount` | Blocks an account. Blocking removes any follow relationship in both directions and hides the account's content. |
| Block Canonical Email | `adminCreateCanonicalEmailBlock` | Blocks an email address and every alias that canonicalizes to it from creating new accounts. Supply either the plain address or a precomputed hash. Requires a moderator or administrator role on the instance. |
| Block Domain | `blockDomain` | Blocks an entire domain for the connected account: existing followers on that domain are removed and its content is hidden. |
| Block Domain (Moderation) | `adminCreateDomainBlock` | Blocks a domain instance-wide. Silence hides its content behind a follow, suspend removes it entirely, and noop records the entry without applying a sanction. Requires a moderator or administrator role on the instance. |
| Block Email Domain | `adminCreateEmailDomainBlock` | Bars an email domain from being used to create new accounts, typically to stop a wave of throwaway sign-ups. Requires a moderator or administrator role on the instance. |
| Bookmark Status | `bookmarkStatus` | Saves a status to the connected account's private bookmarks. Unlike favouriting, the author is not notified. |
| Boost Status | `boostStatus` | Boosts (reblogs) a status so it appears to the connected account's followers. |
| Browse Profile Directory | `browseDirectory` | Lists accounts that have opted into the instance's public profile directory, ordered by recent activity or by newest profile. |
| Cancel Scheduled Status | `deleteScheduledStatus` | Cancels a queued status so it is never published. |
| Create Application | `createApplication` | Registers a new OAuth application on the instance and returns its client id and secret. Requires no authentication. |
| Create Collection | `createCollection` | Creates a collection of accounts the connected account wants to recommend to others. Requires a Mastodon 4.6 or newer instance. |
| Create Featured Tag | `createFeaturedTag` | Features a hashtag on the connected account's profile so visitors can browse its posts using that tag. |
| Create Filter | `createFilter` | Creates a filter group. Keywords supplied here are created with it; more can be added later with Add Filter Keyword. |
| Create Filter V1 | `createFilterV1` | Creates a legacy single-phrase filter. Deprecated by Mastodon in favour of Create Filter, which supports several keywords per group. |
| Create IP Block | `adminCreateIpBlock` | Restricts an IP range: require approval for sign-ups from it, block sign-ups entirely, or deny all access. Requires a moderator or administrator role on the instance. |
| Create List | `createList` | Creates a new list. Accounts are added to it separately with Add Accounts To List. |
| Create Push Subscription | `createPushSubscription` | Registers a Web Push endpoint so the instance delivers encrypted push notifications to it. Replaces any existing subscription for the connected access token. |
| Delete Account | `adminDeleteAccount` | Permanently deletes a remote account's local cached data. This is irreversible. Requires a moderator or administrator role on the instance. |
| Delete Allowed Domain | `adminDeleteDomainAllow` | Removes a domain from the federation allowlist. Requires a moderator or administrator role on the instance. |
| Delete Blocked Domain | `adminDeleteDomainBlock` | Lifts an instance-wide federation block so the domain can federate again. Requires a moderator or administrator role on the instance. |
| Delete Blocked Email Domain | `adminDeleteEmailDomainBlock` | Removes an email domain block so that domain can be used for sign-ups again. Requires a moderator or administrator role on the instance. |
| Delete Canonical Email Block | `adminDeleteCanonicalEmailBlock` | Removes a canonical email block so that address may register again. Requires a moderator or administrator role on the instance. |
| Delete Collection | `deleteCollection` | Permanently deletes a collection. The featured accounts themselves are unaffected. |
| Delete Conversation | `deleteConversation` | Removes a conversation from the connected account's conversation list. The underlying statuses are not deleted. |
| Delete Featured Tag | `deleteFeaturedTag` | Removes a featured hashtag from the connected account's profile. |
| Delete Filter | `deleteFilter` | Permanently deletes a filter group along with all of its keywords and status filters. |
| Delete Filter Keyword | `deleteFilterKeyword` | Removes a keyword from its filter group. |
| Delete Filter V1 | `deleteFilterV1` | Deletes a legacy filter. Deprecated by Mastodon in favour of Delete Filter. |
| Delete IP Block | `adminDeleteIpBlock` | Lifts an IP restriction so that range can sign up and browse again. Requires a moderator or administrator role on the instance. |
| Delete List | `deleteList` | Permanently deletes a list. The accounts in it are not affected. |
| Delete Profile Avatar | `deleteProfileAvatar` | Removes the connected account's avatar image, reverting it to the default placeholder. |
| Delete Profile Header | `deleteProfileHeader` | Removes the connected account's header banner image, reverting it to the default placeholder. |
| Delete Push Subscription | `deletePushSubscription` | Removes the Web Push subscription for the connected access token so no further push notifications are delivered. |
| Delete Status | `deleteStatus` | Permanently deletes one of the connected account's own statuses and returns its source text so it can be re-drafted. |
| Discover OAuth Server Metadata | `getOauthServerMetadata` | Returns the instance's OAuth 2.0 authorization server metadata: endpoints, supported grant types, response modes and the full list of scopes it accepts. |
| Dismiss All Notifications | `clearNotifications` | Permanently clears every notification for the connected account. |
| Dismiss Announcement | `dismissAnnouncement` | Marks an announcement as read for the connected account. |
| Dismiss Notification | `dismissNotification` | Permanently dismisses a single notification. |
| Dismiss Notification Group | `dismissNotificationGroup` | Permanently dismisses every notification in a group. |
| Dismiss Notification Request | `dismissNotificationRequest` | Dismisses a filtered-notification request and discards its held notifications. |
| Dismiss Notification Requests | `dismissNotificationRequests` | Dismisses several filtered-notification requests at once. |
| Edit Status | `updateStatus` | Edits one of the connected account's own statuses. The previous version is preserved in the status's edit history. Only the fields supplied are changed. |
| Enable Account | `adminEnableAccount` | Re-enables login for a disabled local account. Requires a moderator or administrator role on the instance. |
| Endorse Account | `endorseAccount` | Features an account on the connected account's profile so visitors see it as a recommendation. |
| Favourite Status | `favouriteStatus` | Adds a status to the connected account's favourites and notifies its author. |
| Feature Tag | `featureTag` | Features a hashtag on the connected account's profile. Accepts the hashtag name in place of an id. |
| File Report | `createReport` | Reports an account to the instance's moderators, optionally attaching offending statuses and citing the exact server rules that were broken. |
| Find Familiar Followers | `findFamiliarFollowers` | Returns, for up to three accounts, which of the connected account's own follows also follow them. Mastodon requires one repeated id[] key per account, so each is supplied in its own numbered input. |
| Follow Account | `followAccount` | Follows an account. On a locked account this creates a pending follow request instead, indicated by `requested` in the returned relationship. |
| Follow Tag | `followTag` | Follows a hashtag so its public statuses appear in the connected account's home timeline. |
| Generate Annual Report | `generateAnnualReport` | Requests generation of a year-in-review report for a year the account is eligible for. |
| Get Account | `getAccount` | Retrieves a single account's public profile by its numeric account id. |
| Get Account (Moderation) | `adminGetAccount` | Retrieves one account with its moderation fields: email address, confirmation state, known IP addresses, role and current sanctions. Requires a moderator or administrator role on the instance. |
| Get Account Relationships | `getAccountRelationships` | Returns how the connected account relates to up to five other accounts: following, blocked, muted, requested and so on. Mastodon requires one repeated id[] key per account, so each is supplied in its own numbered input. |
| Get Allowed Domain | `adminGetDomainAllow` | Retrieves a single allowed-domain entry. Requires a moderator or administrator role on the instance. |
| Get Annual Report | `getAnnualReport` | Retrieves the year-in-review report for a specific year. |
| Get Annual Report State | `getAnnualReportState` | Returns whether a year-in-review report is available, still generating, eligible to be generated, or not offered for that year. |
| Get Async Refresh Status | `getAsyncRefreshStatus` | Polls the progress of a long-running background refresh that another endpoint started and reported through a Mastodon-Async-Refresh header. |
| Get Blocked Domain | `adminGetDomainBlock` | Retrieves a single instance-wide federation block. Requires a moderator or administrator role on the instance. |
| Get Blocked Email Domain | `adminGetEmailDomainBlock` | Retrieves a single blocked email domain with its recent sign-up attempt statistics. Requires a moderator or administrator role on the instance. |
| Get Canonical Email Block | `adminGetCanonicalEmailBlock` | Retrieves a single canonical email block by id. Requires a moderator or administrator role on the instance. |
| Get Collection | `getCollection` | Retrieves a single collection with its featured accounts. |
| Get Dimensions | `adminGetDimensions` | Returns ranked breakdowns over a date range: most-used languages and client apps, busiest remote servers, disk usage and running software versions. Requires a moderator or administrator role on the instance. |
| Get Filter | `getFilter` | Retrieves a single filter group by id. |
| Get Filter Keyword | `getFilterKeyword` | Retrieves a single filter keyword by id. |
| Get Filter Status | `getFilterStatus` | Retrieves a single status-filter entry by id. |
| Get Filter V1 | `getFilterV1` | Retrieves a single legacy filter by id. Deprecated by Mastodon in favour of Get Filter. |
| Get Grouped Unread Notification Count | `getGroupedUnreadNotificationCount` | Returns how many unread notification groups the connected account has, up to the supplied limit. |
| Get Hashtag Timeline | `getHashtagTimeline` | Returns public statuses using a given hashtag. Additional hashtags can be required or excluded through the Any, All and None inputs, one extra tag each. |
| Get Home Timeline | `getHomeTimeline` | Returns statuses from the accounts and hashtags the connected account follows, newest first. |
| Get Instance | `getInstance` | Returns the instance's configuration: name, description, software version, posting limits, media limits, registration policy and contact account. |
| Get Instance Activity | `getInstanceActivity` | Returns weekly totals of statuses, logins and registrations for the last twelve weeks. |
| Get Instance Domain Blocks | `getInstanceDomainBlocks` | Lists the domains this instance moderates against, with the severity and public rationale of each block. Instances may choose not to publish this list. |
| Get Instance Extended Description | `getInstanceExtendedDescription` | Returns the instance's long-form About text as HTML. |
| Get Instance Languages | `getInstanceLanguages` | Lists every language the instance offers for posting and interface use. |
| Get Instance Privacy Policy | `getInstancePrivacyPolicy` | Returns the instance's privacy policy as HTML. |
| Get Instance Rules | `getInstanceRules` | Lists the instance's server rules, whose ids are used when filing a violation report. |
| Get Instance Terms Of Service | `getInstanceTermsOfService` | Returns the instance's current terms of service as HTML. |
| Get Instance Terms Of Service Version | `getInstanceTermsOfServiceVersion` | Returns a specific historical version of the instance's terms of service. |
| Get Instance Translation Languages | `getInstanceTranslationLanguages` | Returns which target languages each source language can be translated into by the instance's translation provider. |
| Get Instance V1 | `getInstanceV1` | Returns instance metadata in the legacy flat format. Deprecated by Mastodon in favour of Get Instance. |
| Get IP Block | `adminGetIpBlock` | Retrieves a single IP block by id. Requires a moderator or administrator role on the instance. |
| Get Link Timeline | `getLinkTimeline` | Returns public statuses that link to a specific trending article. The URL must be one the instance currently treats as a trending link. |
| Get List | `getList` | Retrieves a single list by id. |
| Get List Timeline | `getListTimeline` | Returns statuses from the accounts in one of the connected account's lists. |
| Get Measures | `adminGetMeasures` | Returns time-series totals over a date range for instance metrics such as active users, new sign-ups, interactions and reports. Tag and instance measures need the matching id or domain parameter. Requires a moderator or administrator role on the instance. |
| Get Media Attachment | `getMediaAttachment` | Retrieves a media attachment the connected account has uploaded. Returns 206 Partial Content while the attachment is still processing. |
| Get Multiple Accounts | `getMultipleAccounts` | Retrieves up to five accounts in a single call. Mastodon requires one repeated id[] query key per account, so each account is supplied in its own numbered input; leave the unused slots empty. |
| Get Multiple Statuses | `getMultipleStatuses` | Retrieves up to five statuses in a single call. Mastodon requires one repeated id[] query key per status, so each is supplied in its own numbered input. |
| Get Notification | `getNotification` | Retrieves a single notification by id. |
| Get Notification Group | `getNotificationGroup` | Retrieves a single notification group by its group key. |
| Get Notification Policy | `getNotificationPolicy` | Returns the connected account's notification filtering policy and how many notifications it is currently holding back. |
| Get Notification Request | `getNotificationRequest` | Retrieves a single filtered-notification request. |
| Get OAuth User Info | `getOauthUserInfo` | Returns OpenID Connect claims about the connected account: issuer, subject, name, preferred username, profile URL and picture. Requires the profile scope. |
| Get oEmbed For Status | `getOembed` | Returns oEmbed metadata and an embeddable iframe for a public status URL, for rendering it on another site. |
| Get Poll | `getPoll` | Retrieves a poll, including its options, current vote counts and whether the connected account has already voted. |
| Get Preferences | `getPreferences` | Returns the connected account's user preferences: default post visibility and language, whether media is expanded, and whether sensitive content is shown. |
| Get Profile | `getProfile` | Returns the connected account's editable profile: display name, bio and metadata fields, in both raw and formatted form. |
| Get Public Timeline | `getPublicTimeline` | Returns public statuses known to the instance. Use Local Only for this server's own posts or Remote Only for federated posts. |
| Get Push Subscription | `getPushSubscription` | Returns the Web Push subscription currently registered for the connected access token. |
| Get Report (Moderation) | `adminGetReport` | Retrieves one moderation report with its reporter, target account, attached statuses and cited rules. Requires a moderator or administrator role on the instance. |
| Get Retention | `adminGetRetention` | Returns a cohort retention table showing how many users who signed up in each period were still active in the periods that followed. Requires a moderator or administrator role on the instance. |
| Get Scheduled Status | `getScheduledStatus` | Retrieves a single queued status and the parameters it will be published with. |
| Get Server Health | `getServerHealth` | Checks that the instance's web server is up and serving requests. Returns the plain text body OK rather than JSON. |
| Get Status | `getStatus` | Retrieves a single status by id, including its author, attachments, poll and interaction counts. |
| Get Status Context | `getStatusContext` | Returns the conversation thread around a status: its ancestors up the reply chain and its descendants down the reply chain. |
| Get Status Edit History | `getStatusHistory` | Returns every past version of a status that has been edited. |
| Get Status Source | `getStatusSource` | Returns the original plain-text source of a status, suitable for pre-filling an edit form. |
| Get Streaming Health | `getStreamingHealth` | Checks that the instance's streaming server is alive. The real-time streaming channels themselves are long-lived Server-Sent Event connections and are not available as actions. |
| Get Tag | `getTag` | Retrieves a hashtag with its recent usage statistics and whether the connected account follows or features it. |
| Get Timeline Markers | `getMarkers` | Returns the connected account's saved reading position for a timeline, so a client can resume where the user left off. |
| Get Trending Links | `getTrendingLinks` | Lists the news articles and links trending on the instance right now. |
| Get Trending Statuses | `getTrendingStatuses` | Lists the statuses trending on the instance right now. |
| Get Trending Tags | `getTrendingTags` | Lists the hashtags trending on the instance right now, each with a week of usage history. |
| Get Unread Notification Count | `getUnreadNotificationCount` | Returns how many notifications the connected account has not yet read, up to the supplied limit. |
| List Account Collections | `listAccountCollections` | Lists the collections created by a given account. |
| List Account Endorsements | `listAccountEndorsements` | Lists the accounts that a given account features on its profile. |
| List Account Featured Tags | `listAccountFeaturedTags` | Lists the hashtags an account has chosen to feature on its profile. |
| List Account Followers | `listAccountFollowers` | Lists the accounts that follow the given account. |
| List Account Following | `listAccountFollowing` | Lists the accounts that the given account follows. |
| List Account Statuses | `listAccountStatuses` | Lists statuses posted by a given account, with filters for media-only, replies, boosts, pinned posts and a specific hashtag. |
| List Accounts (Moderation) | `adminListAccounts` | Lists accounts known to the instance with moderation filters for origin, status, role and identifying details such as email or IP address. Requires a moderator or administrator role on the instance. |
| List Accounts In List | `listAccountsInList` | Lists the accounts that belong to a list. Set Limit to 0 to return every member without paging. |
| List Accounts V1 (Moderation) | `adminListAccountsV1` | Lists accounts using the legacy boolean moderation filters. Deprecated by Mastodon in favour of List Accounts (Moderation). Requires a moderator or administrator role on the instance. |
| List Allowed Domains | `adminListDomainAllows` | Lists the domains explicitly permitted to federate. Only meaningful on instances running in allowlist federation mode. Requires a moderator or administrator role on the instance. |
| List Announcements | `listAnnouncements` | Lists the instance's currently published announcements and whether the connected account has dismissed each one. |
| List Annual Reports | `listAnnualReports` | Lists the year-in-review reports generated for the connected account. |
| List Blocked Accounts | `listBlockedAccounts` | Lists the accounts the connected account has blocked. |
| List Blocked Domains | `adminListDomainBlocks` | Lists the instance-wide federation blocks with their severity and moderator notes. Requires a moderator or administrator role on the instance. |
| List Blocked Email Domains | `adminListEmailDomainBlocks` | Lists the email domains barred from creating accounts on the instance. Requires a moderator or administrator role on the instance. |
| List Bookmarks | `listBookmarks` | Lists the statuses the connected account has bookmarked, most recently bookmarked first. |
| List Canonical Email Blocks | `adminListCanonicalEmailBlocks` | Lists the hashed email addresses barred from creating new accounts. Canonicalization strips dots and plus-address suffixes so aliases of one address are covered by a single block. Requires a moderator or administrator role on the instance. |
| List Collections Featuring Account | `listCollectionsFeaturingAccount` | Lists the collections that feature a given account. |
| List Conversations | `listConversations` | Lists the connected account's direct-message conversations, each with its participants and most recent status. |
| List Custom Emojis | `listCustomEmojis` | Lists every custom emoji available on the instance, for rendering shortcodes or building an emoji picker. |
| List Domain Blocks | `listDomainBlocks` | Lists the domains the connected account has blocked for itself. This is a personal block, distinct from the instance-wide moderation blocks. |
| List Endorsed Accounts | `listEndorsedAccounts` | Lists the accounts the connected account features on its own profile. |
| List Favourites | `listFavourites` | Lists the statuses the connected account has favourited, most recently favourited first. |
| List Featured Tags | `listFeaturedTags` | Lists the hashtags the connected account features on its own profile. |
| List Filter Keywords | `listFilterKeywords` | Lists the keywords belonging to a filter group. |
| List Filter Statuses | `listFilterStatuses` | Lists the individual statuses that have been filtered by a filter group, independently of its keywords. |
| List Filters | `listFilters` | Lists the connected account's filter groups, each with its keywords and individually filtered statuses. |
| List Filters V1 | `listFiltersV1` | Lists the connected account's filters in the legacy single-phrase format. Deprecated by Mastodon in favour of List Filters; a v2 filter group with several keywords appears here as several entries. |
| List Follow Requests | `listFollowRequests` | Lists the accounts waiting for the connected account to approve their follow request. |
| List Follow Suggestions | `listFollowSuggestions` | Lists accounts the instance recommends the connected account follow, each with the reason it was suggested. |
| List Follow Suggestions V1 | `listFollowSuggestionsV1` | Lists recommended accounts without the reason they were suggested. Deprecated by Mastodon in favour of List Follow Suggestions. |
| List Followed Tags | `listFollowedTags` | Lists the hashtags the connected account follows. |
| List Grouped Notifications | `listGroupedNotifications` | Lists notifications collapsed into groups, so ten favourites of one status arrive as a single entry. Accounts and statuses are returned once each and referenced by id. |
| List Instance Peers | `listInstancePeers` | Lists every other domain this instance has federated with. |
| List IP Blocks | `adminListIpBlocks` | Lists the IP ranges restricted from signing up or accessing the instance. Requires a moderator or administrator role on the instance. |
| List Lists | `listLists` | Lists all of the connected account's user-defined lists. |
| List Lists Containing Account | `listListsContainingAccount` | Lists the connected user's own lists that contain the given account. |
| List Muted Accounts | `listMutedAccounts` | Lists the accounts the connected account has muted, each carrying the time its mute expires. |
| List Notification Group Accounts | `listNotificationGroupAccounts` | Lists every account whose action contributed to a notification group. |
| List Notification Requests | `listNotificationRequests` | Lists accounts whose notifications the policy has filtered, so they can be accepted or dismissed in bulk. |
| List Notifications | `listNotifications` | Lists notifications for the connected account: mentions, favourites, boosts, follows, poll results and moderation events. |
| List Reports (Moderation) | `adminListReports` | Lists moderation reports filed on the instance, filterable by resolution state, reporter and reported account. Requires a moderator or administrator role on the instance. |
| List Scheduled Statuses | `listScheduledStatuses` | Lists statuses the connected account has queued for future publication. |
| List Status Boosters | `listStatusBoosters` | Lists the accounts that have boosted a status. |
| List Status Favouriters | `listStatusFavouriters` | Lists the accounts that have favourited a status. |
| List Status Quotes | `listStatusQuotes` | Lists the statuses that quote a given status. |
| List Suggested Featured Tags | `listFeaturedTagSuggestions` | Lists hashtags the connected account uses most often, as candidates to feature on its profile. |
| List Trending Links (Moderation) | `adminListTrendingLinks` | Lists links the instance considers trending, including those still awaiting moderator review. Requires a moderator or administrator role on the instance. |
| List Trending Statuses (Moderation) | `adminListTrendingStatuses` | Lists statuses the instance considers trending, including those still awaiting moderator review. Requires a moderator or administrator role on the instance. |
| List Trending Tags (Moderation) | `adminListTrendingTags` | Lists hashtags the instance considers trending, including those still awaiting moderator review, with their approval flags. Requires a moderator or administrator role on the instance. |
| Lookup Account | `lookupAccount` | Resolves a username or WebFinger address such as user@example.social to its account record, giving you the numeric account id that other endpoints need. |
| Mark Annual Report Read | `markAnnualReportRead` | Marks a year-in-review report as read so it is no longer surfaced to the user. |
| Mark Conversation As Read | `markConversationRead` | Clears the unread flag on a conversation. |
| Mute Account | `muteAccount` | Mutes an account so its statuses are hidden from timelines, optionally for a limited time. Unlike blocking, the muted account is not notified and the follow relationship is kept. |
| Mute Conversation | `muteStatusConversation` | Stops notifications for a conversation thread without leaving it. |
| Perform Account Action | `adminPerformAccountAction` | Applies a moderation sanction to an account: mark its media sensitive, disable login, silence it, or suspend it, optionally citing a report and emailing the user. Requires a moderator or administrator role on the instance. |
| Pin Account To Profile | `pinAccount` | Features an account on the connected account's profile. Deprecated by Mastodon in favour of Endorse Account, which uses the same behaviour. |
| Pin Status To Profile | `pinStatus` | Pins one of the connected account's own public statuses to the top of its profile. |
| Post Status | `createStatus` | Publishes a new status. Supply text, or attach uploaded media, or attach a poll. When Scheduled At is supplied the status is queued instead and a scheduled status is returned. |
| Register Account | `registerAccount` | Creates a user and account record on the instance and returns an access token for it. Requires an application (client credentials) token rather than a user token, and the instance must have open registrations. |
| Reject Account | `adminRejectAccount` | Rejects a pending sign-up and deletes the account record. Requires a moderator or administrator role on the instance. |
| Reject Follow Request | `rejectFollowRequest` | Rejects a pending follow request. |
| Remove Account From Collection | `removeAccountFromCollection` | Removes a featured account from a collection. |
| Remove Account From Followers | `removeAccountFromFollowers` | Forces an account to stop following the connected account, without blocking it. |
| Remove Accounts From List | `removeAccountsFromList` | Removes accounts from a list without unfollowing them. |
| Remove Announcement Reaction | `removeAnnouncementReaction` | Removes the connected account's emoji reaction from an announcement. |
| Remove Follow Suggestion | `removeFollowSuggestion` | Removes an account from the connected account's follow suggestions so it is not recommended again. |
| Remove Status From Filter | `removeStatusFromFilter` | Removes a status-filter entry so that status is no longer filtered by the group. |
| Reopen Report | `adminReopenReport` | Reopens a previously resolved moderation report. Requires a moderator or administrator role on the instance. |
| Reschedule Status | `updateScheduledStatus` | Changes the publication time of a queued status. The new time must be at least 5 minutes in the future. |
| Resend Confirmation Email | `resendConfirmationEmail` | Resends the sign-up confirmation email for an account that has not yet confirmed its address. Requires the token issued by Register Account and fails once the address is confirmed. |
| Resolve Report | `adminResolveReport` | Marks a moderation report as resolved and closes it. Requires a moderator or administrator role on the instance. |
| Revoke Collection Inclusion | `revokeCollectionInclusion` | Withdraws the connected account's consent to being featured in someone else's collection. |
| Revoke OAuth Token | `revokeOauthToken` | Revokes an OAuth access token so it can no longer be used. Per RFC 7009 the instance answers with 200 whether or not the token existed. |
| Revoke Quote | `revokeQuote` | Withdraws approval for another status that quotes one of the connected account's own statuses. The connected account must own the quoted status. |
| Save Timeline Marker | `saveMarkers` | Saves the connected account's reading position in the home timeline, the notifications list, or both. |
| Search | `search` | Searches accounts, hashtags and statuses in one call. Status search only covers the connected account's own posts and interactions unless the instance has full-text search enabled. |
| Search Accounts | `searchAccounts` | Searches for accounts by display name, username or WebFinger address. Use Lookup Account instead when the exact handle is known. |
| Set Account Note | `setAccountNote` | Sets a private note about an account, visible only to the connected account. Send an empty comment to clear the note. |
| Test Canonical Email Block | `adminTestCanonicalEmailBlock` | Canonicalizes and hashes an email address and returns any existing blocks that would match it, without creating one. Requires a moderator or administrator role on the instance. |
| Translate Status | `translateStatus` | Translates a status's content into another language using the instance's configured translation provider. The instance must have translation enabled. |
| Unassign Report | `adminUnassignReport` | Removes the current assignee from a moderation report so another moderator can pick it up. Requires a moderator or administrator role on the instance. |
| Unblock Account | `unblockAccount` | Removes a block on an account. The previous follow relationships are not restored. |
| Unblock Domain | `unblockDomain` | Removes a personal domain block so content from that domain is visible again. |
| Unbookmark Status | `unbookmarkStatus` | Removes a status from the connected account's bookmarks. |
| Unboost Status | `unboostStatus` | Removes the connected account's boost of a status. |
| Unendorse Account | `unendorseAccount` | Removes an account from the featured accounts on the connected account's profile. |
| Unfavourite Status | `unfavouriteStatus` | Removes a status from the connected account's favourites. |
| Unfeature Tag | `unfeatureTag` | Removes a hashtag from the connected account's profile. Accepts the hashtag name in place of an id. |
| Unfollow Account | `unfollowAccount` | Stops following an account, or withdraws a pending follow request. |
| Unfollow Tag | `unfollowTag` | Stops following a hashtag so its statuses no longer appear in the home timeline. |
| Unmute Account | `unmuteAccount` | Removes a mute on an account so its statuses appear in timelines again. |
| Unmute Conversation | `unmuteStatusConversation` | Resumes notifications for a previously muted conversation thread. |
| Unpin Account From Profile | `unpinAccount` | Removes an account from the featured accounts on the connected account's profile. Deprecated by Mastodon in favour of Unendorse Account. |
| Unpin Status From Profile | `unpinStatus` | Removes a pinned status from the top of the connected account's profile. |
| Unsensitive Account | `adminUnsensitiveAccount` | Stops force-marking an account's media as sensitive. Requires a moderator or administrator role on the instance. |
| Unsilence Account | `adminUnsilenceAccount` | Lifts a silence so the account's posts are visible in public timelines again. Requires a moderator or administrator role on the instance. |
| Unsuspend Account | `adminUnsuspendAccount` | Lifts a suspension and restores the account. Requires a moderator or administrator role on the instance. |
| Update Account Credentials | `updateCredentials` | Updates the connected account's profile: display name, bio, metadata fields, discovery flags and default posting preferences. Only the fields supplied are changed. |
| Update Blocked Domain | `adminUpdateDomainBlock` | Changes the severity, media and report handling, notes or obfuscation of an existing instance-wide domain block. Requires a moderator or administrator role on the instance. |
| Update Collection | `updateCollection` | Updates a collection's name, description, language, hashtag or visibility flags. Only the fields supplied are changed. |
| Update Filter | `updateFilter` | Updates a filter group's name, contexts, action or expiry. Only the fields supplied are changed. |
| Update Filter Keyword | `updateFilterKeyword` | Changes the phrase or word-boundary setting of a filter keyword. |
| Update Filter V1 | `updateFilterV1` | Updates a legacy single-phrase filter. Deprecated by Mastodon in favour of Update Filter. |
| Update IP Block | `adminUpdateIpBlock` | Changes the range, severity, note or expiry of an existing IP block. Requires a moderator or administrator role on the instance. |
| Update List | `updateList` | Updates a list's title, replies policy or exclusivity. |
| Update Media Attachment | `updateMediaAttachment` | Updates the alternate text or focal point of a media attachment. An attachment that is already part of a published status can only have these fields changed. |
| Update Notification Policy | `updateNotificationPolicy` | Changes how notifications from unfollowed, non-follower, new, limited or privately mentioning accounts are handled. Accept lets them through, filter holds them for review, drop discards them silently. |
| Update Push Subscription | `updatePushSubscription` | Changes which notification types the existing Web Push subscription receives, without re-registering the endpoint. |
| Update Report | `adminUpdateReport` | Reclassifies a moderation report and, for violation reports, changes which server rules it cites. Requires a moderator or administrator role on the instance. |
| Update Status Interaction Policy | `updateStatusInteractionPolicy` | Changes who may quote one of the connected account's own statuses, without creating an edit in the status history. |
| Upload Media | `uploadMedia` | Uploads a media file and returns an attachment that can be attached to a status. Processing is asynchronous, so the returned attachment has no URL until it completes. |
| Upload Media V1 | `uploadMediaV1` | Uploads a media file synchronously and returns a fully processed attachment. Deprecated by Mastodon in favour of Upload Media, which processes asynchronously. |
| Verify Account Credentials | `verifyCredentials` | Returns the account that owns the connected access token, including private fields such as the default posting settings and the account's role on the instance. |
| Verify Application Credentials | `verifyApplicationCredentials` | Confirms that the connected token belongs to a valid application and returns that application's public details. |
| Vote On Poll | `voteOnPoll` | Casts the connected account's vote on a poll. Choices are zero-based option indexes; single-choice polls accept exactly one. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Account Approved | `account.approved` | Fires when a moderator approves a pending sign-up on an instance that requires approval. An instance administrator must create this webhook once, under Preferences &gt; Administration &gt; Webhooks &gt; Add new webhook: paste the fastn trigger URL into Endpoint URL, tick 'account.approved' under Enabled events, save, then copy the generated Secret into this connector's webhook verification secret. Mastodon has no API for this, so the step is repeated per instance. |
| Account Created | `account.created` | Fires when a new account signs up on the instance. An instance administrator must create this webhook once, under Preferences &gt; Administration &gt; Webhooks &gt; Add new webhook: paste the fastn trigger URL into Endpoint URL, tick 'account.created' under Enabled events, save, then copy the generated Secret into this connector's webhook verification secret. Mastodon has no API for this, so the step is repeated per instance. |
| Account Updated | `account.updated` | Fires when a local account's profile or moderation state changes. An instance administrator must create this webhook once, under Preferences &gt; Administration &gt; Webhooks &gt; Add new webhook: paste the fastn trigger URL into Endpoint URL, tick 'account.updated' under Enabled events, save, then copy the generated Secret into this connector's webhook verification secret. Mastodon has no API for this, so the step is repeated per instance. |
| Report Created | `report.created` | Fires when a moderation report is filed on the instance. An instance administrator must create this webhook once, under Preferences &gt; Administration &gt; Webhooks &gt; Add new webhook: paste the fastn trigger URL into Endpoint URL, tick 'report.created' under Enabled events, save, then copy the generated Secret into this connector's webhook verification secret. Mastodon has no API for this, so the step is repeated per instance. |
| Report Updated | `report.updated` | Fires when a moderation report is reclassified, assigned or resolved. An instance administrator must create this webhook once, under Preferences &gt; Administration &gt; Webhooks &gt; Add new webhook: paste the fastn trigger URL into Endpoint URL, tick 'report.updated' under Enabled events, save, then copy the generated Secret into this connector's webhook verification secret. Mastodon has no API for this, so the step is repeated per instance. |
| Status Created | `status.created` | Fires when a local account posts a new status. An instance administrator must create this webhook once, under Preferences &gt; Administration &gt; Webhooks &gt; Add new webhook: paste the fastn trigger URL into Endpoint URL, tick 'status.created' under Enabled events, save, then copy the generated Secret into this connector's webhook verification secret. Mastodon has no API for this, so the step is repeated per instance. |
| Status Updated | `status.updated` | Fires when a local account edits an existing status. An instance administrator must create this webhook once, under Preferences &gt; Administration &gt; Webhooks &gt; Add new webhook: paste the fastn trigger URL into Endpoint URL, tick 'status.updated' under Enabled events, save, then copy the generated Secret into this connector's webhook verification secret. Mastodon has no API for this, so the step is repeated per instance. |
