---
description: What your own AI agent does after you ask it for an integration, where the result lands in fastn, and how to test it.
---

# Building from your AI agent

Once fastn is connected to your agent through the [MCP gateway](mcp-gateway/README.md), you can ask for an integration in the chat. Whichever agent you use, it follows fastn's integration builder through the same six steps, and each one ends with something you approve.

| Step | What the agent does | What you do |
| --- | --- | --- |
| 1. Understand | Checks who you are and what's already in your workspace | Approve the read-only fastn calls |
| 2. Plan | Picks the connectors and recommends a plan | Answer its business questions; the recommendation is pre-selected |
| 3. Map (only when data moves between systems) | Proposes field mappings and filters | Approve them on the review page it links to |
| 4. Test cases | Writes acceptance tests for the whole integration | Approve them on the review page; this is the go-ahead to build |
| 5. Build | Builds, tests and publishes each workflow, sets its trigger, and creates one widget | Confirm how often it runs, and any test that writes more than a couple of live records |
| 6. Verify | Runs the approved tests and checks real runs | Read its report: what's running, what passed, what's left |

If an account isn't connected yet, the agent stops and sends a connect link. Enter credentials there, never in the chat.

This is the same idea as fastn's in-app [Agent](agent/README.md), run from the agent you already use.

### Where the result lands in fastn

| What | Where |
| --- | --- |
| The workflows | **Workflows** |
| Tests and their results | Open the workflow → **Test cases** |
| Every run | Open the workflow → **Executions** |
| What your customers see | **Widgets** → the new widget (style, embed, publish) |

### Test it

Test from your agent or from your widget, not from the workflow editor.

* **From the agent:** ask in the same chat, for example *"Run all the test cases for the invoice integration and tell me what passed."* It runs every approved test case and reports back.
* **From the widget:** connect a test account in your widget and let the integration run, the way your customers will use it.

Each run then shows under the workflow's **Executions**.
