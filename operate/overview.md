---
description: >-
  Keep every customer's integrations working: what needs attention, who is
  connected, and every run, in one place.
---

# Operate

<figure><img src="../.gitbook/assets/lifecycle/fastn-lifecycle-5-monitor.svg" alt="Stage 5, Run and monitor: support and ops check Health while fastn retries and maintains"><figcaption>Where Operate fits in the integration lifecycle</figcaption></figure>

## What does it do?

Operate shows how every customer's integrations are doing once they are live. **Health** lists what needs a person today, with the action that fixes it. **Customers** and **Connections** show who is connected to what. **Activity** holds every event and run, down to the individual call. fastn retries, renews tokens and handles rate limits on its own, and its maintainer agent proposes fixes when a vendor changes an API.

## Who is it for?

| Role | What they use Operate for |
| --- | --- |
| **Support and customer success** | See which customers need attention before they open a ticket |
| **On-call engineer** | Find the failed run, read why it failed, and replay it |
| **Integration engineer** | Accept the fix when a vendor changes an API |
| **Account owner** | Keep an eye on totals and trends across every customer |

## How do I use it?

{% tabs %}
{% tab title="Dashboard" %}
Start each day on **Operate → Health**. If **Needs attention** is empty, everything is working. Otherwise each row carries its fix: review a proposed update, ask a customer to reconnect, or open the failed runs.

[Health](health.md) · [Alerts](alerts.md) · [Activity](README.md)
{% endtab %}

{% tab title="Your AI tool" %}
With fastn connected to your AI tool, ask about runs and failures in plain words.

[Connect your AI tool](../build/mcp-gateway/README.md)
{% endtab %}
{% endtabs %}

## Example prompts

| Job | Prompt |
| --- | --- |
| Morning check | *Which workflows failed today, and why?* |
| One customer | *Show Acme's connections and their last sync.* |
| Debug a run | *Find the failed runs of the order sync this week and summarise the errors.* |
| Stay ahead | *Which customer connections have expired?* |

## Where things are

| Screen | Use it to |
| --- | --- |
| [Health](health.md) | See what needs attention, totals and trends, pending vendor fixes and alerts |
| [Customers](customers.md) | Find a customer and everything they have connected |
| [Connections](../build/connections/README.md) | Check each signed-in account and its status |
| [Activity](README.md) | Read every event, execution, trace and sync report |
| [Troubleshooting](troubleshooting.md) | Match a symptom to its cause and fix |

## Questions?

* Your customers see their own health in the widget: [View sync status and history](../tutorials/end-user/viewing-sync-status-and-history.md).
* Error meanings: [Errors and failure states](../reference/errors.md).

## Works with

* [Build](../build/README.md): change a workflow when a failure needs a fix.
* [Embed](../embed/README.md): what your customers see and can fix themselves.
