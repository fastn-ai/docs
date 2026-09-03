---
description: When to reach for a unified API and when to call the connector directly.
---

# Choosing between unified and direct

| Use a unified API when                                      | Use the connector directly when                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Several providers do the same job for different customers   | You need a field or action only one provider has            |
| You want one code path regardless of the customer's stack   | The operation has no meaningful equivalent elsewhere        |
| The fields you need are common across providers             | You are already deep in one vendor's model                  |

The two are not exclusive — a workflow can use a unified endpoint for the common path and a direct connector action for the vendor-specific part.

### The All providers filter

Above the endpoint list, **All providers** shows the canonical surface; picking a single provider shows how that one behaves. Useful when a provider has a quirk you need to design around.
