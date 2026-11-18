---
description: "Amazon Simple Notification Service (SNS) Query API."
hidden: true
---

# AWS Simple Notification Service

<img src="../../.gitbook/assets/connectors/lg/aws-sns.png" alt="AWS Simple Notification Service logo">

Amazon Simple Notification Service (SNS) Query API. Create and manage topics and their subscriptions, publish messages to topics, phone numbers and mobile endpoints, manage topic and subscription attributes, tags and access policies, and administer SMS settings, the SMS sandbox and mobile push platform applications and endpoints. Requests are signed with AWS Signature Version 4 using the access key pair on the connection.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [aws.amazon.com](https://aws.amazon.com) |
| **Authentication** | AWS Signature |
| **Slug** | `awsSns` |

## Use it

Add AWS Simple Notification Service from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.awsSns.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Permission | `addPermission` | Adds a statement to an Amazon SNS topic's access policy granting the named AWS accounts permission to use specific SNS actions on that topic. The label identifies the statement and is used later to remove it. Requires the sns:AddPermission permission. |
| Check If Phone Number Is Opted Out | `checkIfPhoneNumberIsOptedOut` | Reports whether a phone number has opted out of receiving SMS messages from the connection's AWS account. Requires the sns:CheckIfPhoneNumberIsOptedOut permission. |
| Confirm Subscription | `confirmSubscription` | Confirms a pending Amazon SNS subscription using the short-lived token that SNS sent to the endpoint in its SubscriptionConfirmation message, and returns the confirmed subscription ARN. Tokens are valid for three days. Requires the sns:ConfirmSubscription permission. |
| Create Platform Application | `createPlatformApplication` | Registers a mobile push platform application with Amazon SNS - APNS, FCM, ADM, Baidu or Microsoft push - using the credentials issued by that push service, and returns its ARN for creating device endpoints. Requires the sns:CreatePlatformApplication permission. |
| Create Platform Endpoint | `createPlatformEndpoint` | Registers a device with a mobile push platform application and returns the endpoint ARN used to publish notifications to that device. Calling it again with the same device token returns the existing endpoint. Requires the sns:CreatePlatformEndpoint permission. |
| Create SMS Sandbox Phone Number | `createSmsSandboxPhoneNumber` | Adds a destination phone number to the SMS sandbox for the connection's account and Region and sends it a one-time password, which must then be supplied to Verify SMS Sandbox Phone Number. Only sandbox-verified numbers can receive SMS while the account is in the sandbox. This action sends a real SMS to the number. Requires the sns:CreateSMSSandboxPhoneNumber permission. |
| Create Subscription | `createSubscription` | Subscribes an endpoint to an Amazon SNS topic using the SNS Subscribe operation. Endpoints that the account does not own - email, SMS and HTTP or HTTPS - must confirm the subscription before messages are delivered, and until then the subscription ARN is returned as pending confirmation unless Return Subscription ARN is true. Requires the sns:Subscribe permission. |
| Create Topic | `createTopic` | Creates an Amazon SNS topic, or returns the ARN of the existing topic when one with the same name already exists. Standard topic names may contain letters, numbers, hyphens and underscores; FIFO topic names must end in .fifo and set the FifoTopic attribute to true. Requires the sns:CreateTopic permission. Returns the topic ARN. |
| Delete Endpoint | `deleteEndpoint` | Deletes a mobile push device endpoint from its platform application. The call succeeds even when the endpoint does not exist. Requires the sns:DeleteEndpoint permission. |
| Delete Platform Application | `deletePlatformApplication` | Deletes a mobile push platform application and every device endpoint registered under it. Requires the sns:DeletePlatformApplication permission. |
| Delete SMS Sandbox Phone Number | `deleteSmsSandboxPhoneNumber` | Removes a destination phone number from the SMS sandbox for the connection's account and Region, so it can no longer receive sandbox SMS messages. Requires the sns:DeleteSMSSandboxPhoneNumber permission. |
| Delete Topic | `deleteTopic` | Deletes an Amazon SNS topic and every subscription attached to it. Messages published to the topic while it is being deleted may be lost, and deleting a topic that does not exist still succeeds. Requires the sns:DeleteTopic permission. |
| Get Data Protection Policy | `getDataProtectionPolicy` | Returns the data protection policy attached to an Amazon SNS topic, which defines how sensitive data in published messages is audited, masked or redacted. Requires the sns:GetDataProtectionPolicy permission. |
| Get Endpoint Attributes | `getEndpointAttributes` | Returns the attributes of a mobile push device endpoint, including whether it is enabled, its device token and any custom user data. Requires the sns:GetEndpointAttributes permission. |
| Get Platform Application Attributes | `getPlatformApplicationAttributes` | Returns the attributes of a mobile push platform application, including its event notification topics, delivery feedback roles and whether its push credentials are still valid. Requires the sns:GetPlatformApplicationAttributes permission. |
| Get SMS Attributes | `getSmsAttributes` | Returns the account-level SMS settings for the connection's AWS account and Region, such as the monthly spend limit, default sender ID, default SMS type and delivery status logging configuration. Requires the sns:GetSMSAttributes permission. |
| Get SMS Sandbox Account Status | `getSmsSandboxAccountStatus` | Reports whether the connection's AWS account is still in the SMS sandbox for this Region. While in the sandbox, SMS messages can only be sent to verified destination phone numbers. Requires the sns:GetSMSSandboxAccountStatus permission. |
| Get Subscription Attributes | `getSubscriptionAttributes` | Returns the properties of an Amazon SNS subscription as a key-value attribute map, including its topic, endpoint, protocol, owner, confirmation status, filter policy, redrive policy and raw message delivery setting. Requires the sns:GetSubscriptionAttributes permission. |
| Get Topic Attributes | `getTopicAttributes` | Returns the properties of an Amazon SNS topic as a key-value attribute map, including its display name, owner, access policy, delivery policy, subscription counts and encryption settings. Requires the sns:GetTopicAttributes permission. |
| List Endpoints By Platform Application | `listEndpointsByPlatformApplication` | Lists the device endpoints registered under a mobile push platform application, with each endpoint's ARN and attributes, 100 per page. Requires the sns:ListEndpointsByPlatformApplication permission. |
| List Origination Numbers | `listOriginationNumbers` | Lists the origination phone numbers the connection's AWS account owns in this Region, with their route type, ISO country code and supported capabilities such as SMS, MMS and voice. Requires the sns:ListOriginationNumbers permission. |
| List Phone Numbers Opted Out | `listPhoneNumbersOptedOut` | Lists the phone numbers that have opted out of receiving SMS messages from the connection's AWS account, 100 per page. Requires the sns:ListPhoneNumbersOptedOut permission. |
| List Platform Applications | `listPlatformApplications` | Lists the mobile push platform applications registered in the connection's account and Region, with their ARNs and attributes, 100 per page. Requires the sns:ListPlatformApplications permission. |
| List SMS Sandbox Phone Numbers | `listSmsSandboxPhoneNumbers` | Lists the destination phone numbers registered for the SMS sandbox in the connection's account and Region, with each number's verification status. Requires the sns:ListSMSSandboxPhoneNumbers permission. |
| List Subscriptions | `listSubscriptions` | Lists the Amazon SNS subscriptions in the connection's account and Region, up to 100 per call, with each subscription's ARN, topic, protocol, endpoint and owner. When more subscriptions exist the response carries a Next Token to pass back for the following page. Requires the sns:ListSubscriptions permission. |
| List Subscriptions By Topic | `listSubscriptionsByTopic` | Lists the subscriptions attached to one Amazon SNS topic, up to 100 per call, with each subscription's ARN, protocol, endpoint and owner. When more subscriptions exist the response carries a Next Token to pass back for the following page. Requires the sns:ListSubscriptionsByTopic permission. |
| List Tags For Resource | `listTagsForResource` | Lists the tags attached to an Amazon SNS topic. Requires the sns:ListTagsForResource permission. |
| List Topics | `listTopics` | Lists the ARNs of the Amazon SNS topics in the connection's account and Region, up to 100 per call. When more topics exist the response carries a Next Token to pass back for the following page. Requires the sns:ListTopics permission. |
| Opt In Phone Number | `optInPhoneNumber` | Opts a phone number back in to receiving SMS messages from the connection's AWS account. A number can only be opted in once every 30 days. Requires the sns:OptInPhoneNumber permission. |
| Publish Batch | `publishBatch` | Publishes up to ten messages to an Amazon SNS topic in a single request. Each entry needs an ID that is unique within the batch, and the combined size of all messages must stay under 256 KB. FIFO topics also require a Message Group ID per entry. The response reports successful and failed entries separately, so a 200 can still contain failures. Requires the sns:Publish permission. |
| Publish Message | `publishMessage` | Publishes a message to an Amazon SNS topic, to a mobile push endpoint, or directly to a phone number as an SMS. Exactly one of Topic ARN, Target ARN or Phone Number must be supplied. Messages are at most 256 KB, or 140 characters for SMS. Set Message Structure to json to send a different payload per protocol. FIFO topics require a Message Group ID. Requires the sns:Publish permission. |
| Put Data Protection Policy | `putDataProtectionPolicy` | Attaches or replaces the data protection policy on an Amazon SNS topic, defining how sensitive data in published messages is audited, masked, redacted or blocked. Passing an empty policy removes the current one. Requires the sns:PutDataProtectionPolicy permission. |
| Remove Permission | `removePermission` | Removes a statement from an Amazon SNS topic's access policy by the label it was added with. Requires the sns:RemovePermission permission. |
| Set Endpoint Attributes | `setEndpointAttributes` | Updates the attributes of a mobile push device endpoint, typically to re-enable an endpoint that push feedback disabled or to store a refreshed device token. Requires the sns:SetEndpointAttributes permission. |
| Set Platform Application Attributes | `setPlatformApplicationAttributes` | Updates the attributes of a mobile push platform application, such as rotating its push credentials or setting the SNS topics that receive endpoint lifecycle and delivery failure events. Requires the sns:SetPlatformApplicationAttributes permission. |
| Set SMS Attributes | `setSmsAttributes` | Sets account-level SMS settings for the connection's AWS account and Region, such as the monthly spend limit, default sender ID, default SMS type and delivery status logging. These settings affect every SMS message the account sends, so change them deliberately. Requires the sns:SetSMSAttributes permission. |
| Set Subscription Attributes | `setSubscriptionAttributes` | Sets one attribute of an Amazon SNS subscription, such as its filter policy, delivery policy, redrive policy or raw message delivery flag. One attribute per call. Requires the sns:SetSubscriptionAttributes permission. |
| Set Topic Attributes | `setTopicAttributes` | Sets one attribute of an Amazon SNS topic, such as its display name, access policy, delivery policy, KMS key or FIFO throughput scope. One attribute per call. Requires the sns:SetTopicAttributes permission. |
| Tag Resource | `tagResource` | Adds or updates tags on an Amazon SNS topic. A topic can carry up to 50 tags; adding a tag with an existing key overwrites its value. Requires the sns:TagResource permission. |
| Unsubscribe | `unsubscribe` | Deletes an Amazon SNS subscription so its endpoint stops receiving messages from the topic. If the subscription was confirmed with Authenticate On Unsubscribe set to true, only the topic owner or the subscription owner may call this and the request must be signed. Pending-confirmation subscriptions cannot be removed this way and expire on their own after three days. Requires the sns:Unsubscribe permission. |
| Untag Resource | `untagResource` | Removes tags from an Amazon SNS topic by tag key. Requires the sns:UntagResource permission. |
| Verify SMS Sandbox Phone Number | `verifySmsSandboxPhoneNumber` | Verifies a destination phone number in the SMS sandbox using the one-time password that Create SMS Sandbox Phone Number sent to it. Requires the sns:VerifySMSSandboxPhoneNumber permission. |
