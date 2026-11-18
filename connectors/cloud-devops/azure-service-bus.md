---
description: "Azure Service Bus messaging."
hidden: true
---

# Azure Service Bus

<img src="../../.gitbook/assets/connectors/azure-service-bus.svg" alt="Azure Service Bus logo" width="64">

Azure Service Bus messaging. Send and receive messages on queues and topics/subscriptions, manage queue/topic/subscription entities, and handle message locking, completion, abandon, and dead-lettering. Auth via SAS token (Shared Access Signature).

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [servicebus.windows.net](https://servicebus.windows.net) |
| **Authentication** | Credentials you enter |
| **Slug** | `azureServiceBus` |

## Use it

Add Azure Service Bus from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.azureServiceBus.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Abandon Queue Message | `abandonQueueMessage` | Abandon a peek-locked queue message, making it available for re-processing. The message lock is released immediately. |
| Abandon Subscription Message | `abandonSubscriptionMessage` | Abandon a peek-locked subscription message, releasing the lock and making it available again. |
| Complete Queue Message (Delete Locked) | `completeQueueMessage` | Complete (acknowledge) a peek-locked queue message, removing it from the queue. Provide the messageId and lockToken from a previous peek-lock. |
| Complete Subscription Message | `completeSubscriptionMessage` | Complete (acknowledge) a peek-locked topic subscription message, removing it from the subscription. |
| Create Queue | `createQueue` | Create a new queue in the namespace. Provide queue properties as XML body (QueueDescription). |
| Create Subscription | `createSubscription` | Create a new subscription on a topic. |
| Create Subscription Rule | `createRule` | Create a SQL-filter rule on a topic subscription so it only receives messages matching the SQL expression (evaluated over message and user properties). Create a rule named '$Default' to replace the catch-all filter. |
| Create Topic | `createTopic` | Create a new topic in the namespace. |
| Delete Queue | `deleteQueue` | Delete a queue from the namespace. All messages in the queue are discarded. |
| Delete Subscription | `deleteSubscription` | Delete a subscription from a topic. |

<details>

<summary>See 25 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Subscription Rule | `deleteRule` | Delete a rule (filter) from a topic subscription by name. |
| Delete Topic | `deleteTopic` | Delete a topic and all its subscriptions from the namespace. |
| Get Queue | `getQueue` | Get metadata and runtime info for a specific queue, including message counts. |
| Get Subscription | `getSubscription` | Get metadata for a topic subscription, including message counts. |
| Get Subscription Rule | `getRule` | Get a single rule (filter + optional action) by name from a topic subscription. |
| Get Topic | `getTopic` | Get metadata for a specific topic. |
| List Queues | `listQueues` | List all queues in the Service Bus namespace. Returns Atom XML with queue metadata. |
| List Subscription Rules | `listRules` | List all rules (filters) configured on a topic subscription. Each subscription has at least one rule; the default is a TrueFilter that matches everything. |
| List Subscriptions | `listSubscriptions` | List all subscriptions for a topic. |
| List Topics | `listTopics` | List all topics in the Service Bus namespace. |
| Peek-Lock Queue Message | `peekLockQueueMessage` | Non-destructively peek and lock the first available message from a queue; returns the message body. NOTE: Service Bus returns the lock token and message id in the 'BrokerProperties' HTTP response header, which the connector executor does not currently surface. As a result, completing/abandoning/renewing this exact locked message through the connector is not possible (the settle actions need a lock token obtained out-of-band). For straightforward at-least-once consumption, prefer Receive and Delete. |
| Peek-Lock Subscription Message | `peekLockSubscriptionMessage` | Peek-lock the first available message from a topic subscription; returns the message body. NOTE: the lock token and message id come back in the 'BrokerProperties' HTTP response header, which the connector executor does not currently surface, so completing/abandoning/renewing this exact locked message through the connector is not possible. For straightforward at-least-once consumption, prefer Receive and Delete. |
| Receive and Delete Dead-Letter Queue Message | `receiveDeadLetterQueueMessage` | Destructively receive a message from the dead-letter sub-queue of a queue ($DeadLetterQueue). |
| Receive and Delete Dead-Letter Subscription Message | `receiveDeadLetterSubscriptionMessage` | Destructively receive the first message from the dead-letter sub-queue of a topic subscription ($DeadLetterQueue). |
| Receive and Delete Queue Message | `receiveAndDeleteQueueMessage` | Destructively receive the first message from a queue (receive-and-delete mode). The message is removed from the queue immediately. |
| Receive and Delete Subscription Message | `receiveAndDeleteSubscriptionMessage` | Destructively receive the first available message from a topic subscription. |
| Renew Queue Message Lock | `renewQueueMessageLock` | Renew the lock on a peek-locked queue message to extend the processing time. |
| Renew Subscription Message Lock | `renewSubscriptionMessageLock` | Renew the lock on a peek-locked subscription message. |
| Send Batch Messages to Queue | `sendBatchMessagesToQueue` | Send a batch of messages to a Service Bus queue in a single request (application/vnd.microsoft.servicebus.params+json body). |
| Send Batch Messages to Topic | `sendBatchMessagesToTopic` | Publish a batch of messages to a Service Bus topic in a single request. Each message is an object with a Body and optional BrokerProperties/UserProperties. All active subscriptions receive a copy. |
| Send Message to Queue | `sendMessageToQueue` | Send a message to a Service Bus queue. The message body is sent as plain text. Optional properties: BrokerProperties (JSON), custom user properties, content type. |
| Send Message to Topic | `sendMessageToTopic` | Publish a message to a Service Bus topic. All active subscriptions will receive a copy. |
| Update Queue | `updateQueue` | Update properties of an existing queue. Uses PUT with If-Match: * to modify the QueueDescription in place. Only supply the properties you want to change. |
| Update Subscription | `updateSubscription` | Update properties of an existing topic subscription. Uses PUT with If-Match: * to modify the SubscriptionDescription in place. |
| Update Topic | `updateTopic` | Update properties of an existing topic. Uses PUT with If-Match: * to modify the TopicDescription in place. |

</details>
