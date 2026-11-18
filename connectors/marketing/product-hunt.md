---
description: "Product Hunt GraphQL API v2 for posts, comments, topics, collections, and users."
hidden: true
---

# Product Hunt

<img src="../../.gitbook/assets/connectors/lg/product-hunt.png" alt="Product Hunt logo">

Product Hunt GraphQL API v2 for posts, comments, topics, collections, and users. Used to ingest pain-signal mentions from launches and product comments.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [api.producthunt.com](https://api.producthunt.com) |
| **Authentication** | Bearer token |
| **Slug** | `productHunt` |

## Use it

Add Product Hunt from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.productHunt.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Follow User | `followUser` | Follow a user. Requires private OAuth scope. |
| Get Collection | `getCollection` | Preset GraphQL: get a collection by id. |
| Get Comment | `getComment` | Preset GraphQL: get a single comment by id with reply thread. Pass null for any optional. |
| Get Post By Id | `getPostById` | Preset GraphQL: get a post by id. |
| Get Post By Slug | `getPostBySlug` | Preset GraphQL: get a post by slug. |
| Get Post By URL | `getPostByUrl` | Preset GraphQL: resolve a post by Product Hunt URL or external product URL. Pass null for the one you don't use. |
| Get Post Media By Id | `getPostMediaById` | Preset GraphQL: fetch post media gallery + product links by id. |
| Get Post Media By Slug | `getPostMediaBySlug` | Preset GraphQL: fetch post media gallery + product links by slug. |
| Get Post With Comments | `getPostWithComments` | Preset GraphQL: fetch a post with its top-level comment thread by slug. |
| Get Topic | `getTopic` | Preset GraphQL: get a single topic by slug. |
| Get User By Id | `getUserById` | Preset GraphQL: get a user by id. |
| Get User By Username | `getUserByUsername` | Preset GraphQL: get a user by username. |
| Get Viewer | `getViewer` | Preset GraphQL: get the authenticated viewer. |
| GraphQL Query | `graphqlQuery` | Run an arbitrary GraphQL query against Product Hunt v2. Use this for posts, comments, topics, collections, and users. |
| List Collections | `listCollections` | Preset GraphQL: list collections with pagination. FIXED schema (dropped non-existent slug/postsCount fields). |
| List Collections By User | `listCollectionsByUser` | Preset GraphQL: collections created by a user. |
| List Collections Containing Post | `listCollectionsContainingPost` | Preset GraphQL: collections that include a given post. |
| List Comment Voters | `listCommentVoters` | Preset GraphQL: voters on a specific comment. |
| List Featured Posts | `listFeaturedPosts` | Preset GraphQL: featured posts filtered by date range. |
| List Post Comments By Post Id | `listPostCommentsByPostId` | Preset GraphQL: top-level comments on a post by post id. |
| List Post Comments By Post Slug | `listPostCommentsByPostSlug` | Preset GraphQL: top-level comments on a post by post slug. |
| List Post Makers By Post Id | `listPostMakersByPostId` | Preset GraphQL: makers of a post by post id. |
| List Post Makers By Post Slug | `listPostMakersByPostSlug` | Preset GraphQL: makers of a post by post slug. |
| List Post Topics By Post Id | `listPostTopicsByPostId` | Preset GraphQL: topics tagged on a post by post id. |
| List Post Topics By Post Slug | `listPostTopicsByPostSlug` | Preset GraphQL: topics tagged on a post by post slug. |
| List Post Voters By Post Id | `listPostVotersByPostId` | Preset GraphQL: voters on a post by post id. |
| List Post Voters By Post Slug | `listPostVotersByPostSlug` | Preset GraphQL: voters on a post by post slug. |
| List Posts By Topic | `listPostsByTopic` | Preset GraphQL: posts in a topic. |
| List Recent Posts | `listRecentPosts` | Preset GraphQL: recent posts with order control. |
| List Topics | `listTopics` | Preset GraphQL: list topics with pagination. |
| List Topics Followed By User | `listTopicsFollowedByUser` | Preset GraphQL: topics a user follows. FIXED typo (followedByUserid, lowercase d). |
| List User Followed Collections By User Id | `listUserFollowedCollectionsByUserId` | Preset GraphQL: collections a user follows, by user id. |
| List User Followed Collections By Username | `listUserFollowedCollectionsByUsername` | Preset GraphQL: collections a user follows, by username. |
| List User Followers By User Id | `listUserFollowersByUserId` | Preset GraphQL: followers of a user, by user id. |
| List User Followers By Username | `listUserFollowersByUsername` | Preset GraphQL: followers of a user, by username. |
| List User Following By User Id | `listUserFollowingByUserId` | Preset GraphQL: users a user is following, by user id. |
| List User Following By Username | `listUserFollowingByUsername` | Preset GraphQL: users a user is following, by username. |
| List User Made Posts By User Id | `listUserMadePostsByUserId` | Preset GraphQL: posts where user is a maker, by user id. |
| List User Made Posts By Username | `listUserMadePostsByUsername` | Preset GraphQL: posts where user is a maker, by username. |
| List User Submitted Posts By User Id | `listUserSubmittedPostsByUserId` | Preset GraphQL: posts a user hunted (submitted), by user id. |
| List User Submitted Posts By Username | `listUserSubmittedPostsByUsername` | Preset GraphQL: posts a user hunted (submitted), by username. |
| List User Voted Posts By User Id | `listUserVotedPostsByUserId` | Preset GraphQL: posts a user upvoted, by user id. |
| List User Voted Posts By Username | `listUserVotedPostsByUsername` | Preset GraphQL: posts a user upvoted, by username. |
| Search Topics | `searchTopics` | Preset GraphQL: search topics by query. |
| Unfollow User | `unfollowUser` | Unfollow a user. |
