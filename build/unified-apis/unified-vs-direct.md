---
description: When to use a unified API and when to call an app's connector directly.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Choose between unified and direct

There are two ways to reach a customer's app:

* **Unified API:** one call that works the same for every app in a category, such as every CRM. It covers what those apps have in common. [Learn more](README.md)
* **Direct:** a call to one app's own API through its [connector](../connectors/README.md). It reaches everything that app offers, but the code is for that app only.

For example, creating a contact works the same in every CRM, so use the unified API. A field that only one CRM has needs a direct call to that CRM's connector.

| Use a unified API when                                      | Use the connector directly when                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Several providers do the same job for different customers   | You need a field or action only one provider has            |
| You want one code path regardless of the customer's stack   | The operation has no meaningful equivalent elsewhere        |
| The fields you need are common across providers             | You already rely heavily on one vendor's data model         |

You can use both. A workflow can use a unified endpoint for the common path and a direct connector action for the vendor-specific part.

To check how one provider handles an entity before you decide, use the **All providers** filter on the category's page. See [Filter by provider](inside-a-category.md#filter-by-provider).
