---
description: "Beamer is a changelog, feedback, NPS and user-onboarding platform for announcing product updates in-app."
hidden: true
---

# Beamer

Beamer is a changelog, feedback, NPS and user-onboarding platform for announcing product updates in-app. This connector covers the full Beamer v0 REST API: feed URL, ping, posts, post comments, post reactions, unread posts, feature requests with their comments and votes, analytics users, NPS responses and surveys, team members and privacy data deletion.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [getbeamer.com](https://getbeamer.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 51 |
| **Events** | 9 |
| **Slug** | `beamer` |

## Use it

Add Beamer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.beamer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check NPS Prompt | `checkNpsPrompt` | Checks whether a given user should be shown the Beamer NPS prompt right now and returns the survey URL to display. Requires an NPS-enabled Beamer plan. |
| Count Feature Request Comments | `countFeatureRequestComments` | Returns the number of comments on a feature request that match the supplied date, visibility, language and search filters. |
| Count Feature Request Votes | `countFeatureRequestVotes` | Returns the total number of votes cast on a feature request on your Beamer Ideas board. |
| Count Feature Requests | `countFeatureRequests` | Returns the number of feature requests on your Beamer Ideas board that match the supplied filters. |
| Count NPS Responses | `countNpsResponses` | Returns the number of NPS survey responses that match the supplied date range, score range and search filters. Requires an NPS-enabled Beamer plan. |
| Count Post Comments | `countPostComments` | Returns the number of comments on a Beamer post that match the supplied date, language and search filters. |
| Count Post Reactions | `countPostReactions` | Returns the number of reactions on a Beamer post that match the supplied date range and reaction type. |
| Count Posts | `countPosts` | Returns the number of posts in your Beamer changelog that match the supplied filters, without returning the posts themselves. |
| Count Unread Posts | `countUnreadPosts` | Returns the number of posts a given user would see as unread when opening their Beamer feed, together with the feed and popup URLs. Use it to drive your own unread badge. |
| Create Analytics User | `createUser` | Creates an end user in Beamer Analytics so that segmentation filters and per-user feeds can target them before they are first seen in the widget. |
| Create Feature Request | `createFeatureRequest` | Creates a feature request on your Beamer Ideas board on behalf of an end user. Title, content and language are arrays so several translations can be created at once, keeping the same order across all of them. |
| Create Feature Request Comment | `createFeatureRequestComment` | Adds a comment to a feature request on your Beamer Ideas board on behalf of an end user. |
| Create Feature Request Vote | `createFeatureRequestVote` | Casts a vote on a feature request on your Beamer Ideas board on behalf of an end user. |
| Create Post | `createPost` | Creates a new post in your Beamer changelog. Title, content, language, link URL and link text are arrays so that several translations can be created at once; keep the same order across all of them. Multiple translations require the Starter plan or above. |
| Create Post Comment | `createPostComment` | Adds a comment to a Beamer post on behalf of one of your end users. The comment appears in the Beamer inbox alongside organic feedback. |
| Create Post Reaction | `createPostReaction` | Records a positive, neutral or negative reaction to a Beamer post on behalf of one of your end users. |
| Delete Analytics Users | `deleteUsers` | Deletes every Beamer Analytics user matching the supplied selector and returns how many were removed. Provide at least one of User ID, Beamer ID or User Email. |
| Delete Feature Request | `deleteFeatureRequest` | Permanently deletes a feature request from your Beamer Ideas board, together with its comments and votes. |
| Delete Feature Request Comment | `deleteFeatureRequestComment` | Permanently deletes a single comment from a feature request on your Beamer Ideas board. |
| Delete Feature Request Vote | `deleteFeatureRequestVote` | Removes a single vote from a feature request on your Beamer Ideas board. |
| Delete Post | `deletePost` | Permanently deletes a Beamer post by its id, together with its translations, comments and reactions. |
| Delete Post Comment | `deletePostComment` | Permanently deletes a single comment from a Beamer post. |
| Delete Post Reaction | `deletePostReaction` | Permanently deletes a single reaction from a Beamer post. |
| Delete User Privacy Data | `deleteUserPrivacyData` | Erases all data Beamer holds about the matching end users, including their analytics profile, comments, reactions, votes and NPS responses. Use it to satisfy GDPR erasure requests. Provide at least one of User ID, Beamer ID or User Email. |
| Get Feature Request | `getFeatureRequest` | Returns a single feature request from your Beamer Ideas board by its id, including translations, vote and comment counts. |
| Get Feature Request Comment | `getFeatureRequestComment` | Returns a single comment on a feature request by its id, including the details of the user who left it. |
| Get Feature Request Vote | `getFeatureRequestVote` | Returns a single vote on a feature request by its id, including the details of the user who cast it. |
| Get Feed URL | `getFeedUrl` | Retrieves the URL of your standalone Beamer feed, optionally scoped to a language, a segmentation filter, a theme and the identity of the viewing user for analytics. |
| Get NPS Survey Link | `getNpsSurveyLink` | Returns a shareable Beamer NPS survey link personalised for the given user, so you can embed it in your own emails or in-app messaging. Requires an NPS-enabled Beamer plan. |
| Get Post | `getPost` | Returns a single Beamer post by its id, including all of its translations and engagement counters. |
| Get Post Comment | `getPostComment` | Returns a single comment on a Beamer post by its id, including the details of the user who left it. |
| Get Post Reaction | `getPostReaction` | Returns a single reaction on a Beamer post by its id, including the details of the user who left it. |
| Invite Team Member | `inviteTeamMember` | Invites a new member into your Beamer team with the given role. Beamer emails the invitation to the address supplied, so use it only with addresses you are authorised to contact. |
| List Analytics Users | `listUsers` | Returns the end users tracked in Beamer Analytics, optionally narrowed to a single user id, Beamer id or email address, with sorting and pagination. |
| List Feature Request Comments | `listFeatureRequestComments` | Returns the comments left on a feature request, with optional date, visibility, language and free-text search filtering plus pagination. |
| List Feature Request Votes | `listFeatureRequestVotes` | Returns the individual votes cast on a feature request, optionally restricted to a date range, with pagination. |
| List Feature Requests | `listFeatureRequests` | Returns feature requests submitted to your Beamer Ideas board, with optional filtering by date range, language, category, status, visibility and free-text search. |
| List Languages | `listLanguages` | Returns the languages enabled on your Beamer product, so you can pick a valid ISO-639 code for the Language fields on posts, feeds and feature requests. This endpoint is live on the Beamer API but is not covered by the public API reference. |
| List NPS Responses | `listNpsResponses` | Returns the NPS survey responses collected in Beamer, with optional date range, score range and free-text search filtering plus pagination. Requires an NPS-enabled Beamer plan. |
| List Post Comments | `listPostComments` | Returns the comments users left on a Beamer post, with optional date, language and free-text search filtering plus pagination. |
| List Post Reactions | `listPostReactions` | Returns the reactions users left on a Beamer post, optionally restricted to a date range or a single reaction type, with pagination. |
| List Posts | `listPosts` | Returns posts from your Beamer changelog, with optional filtering by date range, language, category, published, archived and expired state, plus pagination. At most 10 posts are returned per page. |
| List Segmentation Filters | `listSegmentationFilters` | Returns the segmentation filters configured on your Beamer product, so you can pick a valid value for the Segmentation Filter fields on posts, feeds and users. This endpoint is live on the Beamer API but is not covered by the public API reference. |
| List Unread Posts | `listUnreadPosts` | Returns the posts a given user has not yet seen in their Beamer feed, optionally marking them as read. |
| Ping The API | `ping` | Checks that your Beamer API key is valid and returns the name of the product the key belongs to. Use it as a lightweight connectivity and credential check. |
| Remove Team Member | `removeTeamMember` | Removes a member from your Beamer team by their email address. The member loses access to the product immediately. |
| Send NPS Email Survey | `sendNpsEmailSurvey` | Sends the Beamer NPS survey by email to the given address. Beamer answers 204 with no content when the survey was already sent to that user. This action delivers a real email, so use it only against addresses you own. Requires an NPS-enabled Beamer plan. |
| Update Analytics Users | `updateUsers` | Updates every Beamer Analytics user matching the supplied selector. Provide at least one of Match User ID, Match Beamer ID or Match User Email to choose which users are updated, and supply the new attribute values in the remaining fields. |
| Update Feature Request | `updateFeatureRequest` | Updates an existing feature request on your Beamer Ideas board, for example to move it to a new status, change its visibility or edit its content. |
| Update Post | `updatePost` | Updates an existing Beamer post. Only the fields supplied are sent; title, content, language, link URL and link text are arrays so several translations can be updated at once, keeping the same order across all of them. |
| Update Team Member Role | `updateTeamMemberRole` | Changes the role of an existing member of your Beamer team, identified by their email address. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| New Comment | `new_comment` | A user left a comment on one of your Beamer posts. Register the fastn trigger URL in Beamer: log in to app.getbeamer.com, open Settings &gt; Integrations &gt; Webhooks, click Add webhook, paste the trigger URL, tick 'New Comment' and save. Payload schema is modelled from the Beamer comment object returned by GET /posts/{postId}/comments, not captured from a real delivery. |
| New Idea | `new_idea` | A user submitted a new feature request on your Beamer Ideas board. Register the fastn trigger URL in Beamer: log in to app.getbeamer.com, open Settings &gt; Integrations &gt; Webhooks, click Add webhook, paste the trigger URL, tick 'New Idea' and save. Payload schema is modelled from the Beamer feature request object, not captured from a real delivery. |
| New Idea Comment | `new_idea_comment` | A user commented on a feature request on your Beamer Ideas board. Register the fastn trigger URL in Beamer: log in to app.getbeamer.com, open Settings &gt; Integrations &gt; Webhooks, click Add webhook, paste the trigger URL, tick 'New Idea Comment' and save. Payload schema is modelled from the Beamer feature request comment object, not captured from a real delivery. |
| New Idea Vote | `new_idea_vote` | A user voted on a feature request on your Beamer Ideas board. Register the fastn trigger URL in Beamer: log in to app.getbeamer.com, open Settings &gt; Integrations &gt; Webhooks, click Add webhook, paste the trigger URL, tick 'New Idea Vote' and save. Payload schema is modelled from the Beamer feature request vote object, not captured from a real delivery. |
| New NPS Response | `new_nps_response` | A user submitted an NPS survey response. Requires an NPS-enabled Beamer plan. Register the fastn trigger URL in Beamer: log in to app.getbeamer.com, open Settings &gt; Integrations &gt; Webhooks, click Add webhook, paste the trigger URL, tick 'New NPS Response' and save. Payload schema is modelled from the Beamer NPS response object, not captured from a real delivery. |
| New Post | `new_post` | A new post was published in your Beamer changelog. Register the fastn trigger URL in Beamer: log in to app.getbeamer.com, open Settings &gt; Integrations &gt; Webhooks, click Add webhook, paste the trigger URL, tick 'New Post' and save. Beamer sends no event-type discriminator that fastn could verify, so if you subscribe to more than one event type in Beamer, add a literal field naming the event to the payload or use one trigger URL per event type. Payload schema is modelled from the Beamer post object returned by the API, not captured from a real delivery. |
| New Reaction | `new_reaction` | A user reacted to one of your Beamer posts. Register the fastn trigger URL in Beamer: log in to app.getbeamer.com, open Settings &gt; Integrations &gt; Webhooks, click Add webhook, paste the trigger URL, tick 'New Reaction' and save. Payload schema is modelled from the Beamer reaction object returned by GET /posts/{postId}/reactions, not captured from a real delivery. |
| Post Deleted | `post_deleted` | A post was deleted from your Beamer changelog. Register the fastn trigger URL in Beamer: log in to app.getbeamer.com, open Settings &gt; Integrations &gt; Webhooks, click Add webhook, paste the trigger URL, tick 'Post Deleted' and save. Payload schema is modelled from the Beamer post object, not captured from a real delivery. |
| Post Edited | `post_edited` | An existing post was edited in your Beamer changelog. Register the fastn trigger URL in Beamer: log in to app.getbeamer.com, open Settings &gt; Integrations &gt; Webhooks, click Add webhook, paste the trigger URL, tick 'Post Edited' and save. Payload schema is modelled from the Beamer post object, not captured from a real delivery. |
