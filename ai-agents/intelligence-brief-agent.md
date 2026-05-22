---
description: >-
  A multi-agent graph that researches companies using public information and
  produces integration strategy briefs with recommended connectors and workflow
  patterns.
---

# Intelligence Brief Agent

The Intelligence Brief agent is a standalone agent — but internally it operates as a **multi-agent graph**, meaning multiple specialized sub-processes run in parallel to research different aspects of a company before synthesizing the results into a single brief.

### What it does

Given a company name or domain, the Intelligence Brief agent:

1. **Researches the company** — Analyzes the company's website, tech stack, industry, product offering, and competitive landscape using public information.
2. **Identifies integration opportunities** — Based on the company's product and customer base, determines which third-party apps their customers are most likely to use.
3. **Recommends connectors** — Maps the integration opportunities to Fastn's available connectors, flagging any gaps where custom connectors would be needed.
4. **Suggests workflow patterns** — Proposes common automation patterns that fit the company's use case (e.g., order-to-invoice sync for e-commerce, contact sync for CRM-heavy products).
5. **Produces a strategy brief** — A structured document summarizing all findings with prioritized recommendations.

### When it's used

The Intelligence Brief agent runs during two scenarios:

**SaaS partner signup** — When a new SaaS company signs up, the platform's signup validation pipeline includes an LLM classification step. The Intelligence Brief agent provides deeper analysis for companies that pass initial validation, helping the Fastn team and the SaaS Onboarding agent understand the partner's integration landscape.

**Manual research** — Platform Admins or SaaS Admins can trigger the agent to research a specific company — useful when evaluating potential partnerships, preparing for onboarding calls, or scoping integration work.

### What the brief contains

A completed Intelligence Brief includes:

| Section                       | Content                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Company profile**           | Industry, product type, target customer, estimated size, tech stack                                                       |
| **Integration landscape**     | What apps the company's customers likely use, organized by category (CRM, accounting, e-commerce, communication)          |
| **Connector recommendations** | Which Fastn connectors to configure first, with priority ranking                                                          |
| **Connector gaps**            | Apps that the company's customers need but Fastn doesn't have a built-in connector for — candidates for custom connectors |
| **Workflow patterns**         | Suggested automation flows based on common patterns in the company's industry                                             |
| **Competitive context**       | How the company's integration offering compares to competitors in their space                                             |

> **📷 Screenshot needed:** A completed Intelligence Brief showing the company profile, connector recommendations, and suggested workflow patterns.

### How the multi-agent graph works

Unlike the orchestrated agents (Connector Agent, Workflow Agent) which run sub-agents sequentially, the Intelligence Brief uses a **graph pattern** where multiple research tasks run in parallel:

* Web research (company website, product pages)
* Tech stack analysis (infrastructure, APIs, developer docs)
* Competitor research (similar products, their integration offerings)
* Connector matching (mapping needs to available connectors)

Results from all branches are synthesized into the final brief. This parallel execution makes the agent faster — it doesn't wait for one research step to finish before starting the next.

### Related pages

* [**SaaS Onboarding Agent**](https://claude.ai/chat/saas-onboarding.md) — Uses Intelligence Brief data during onboarding
* [**Connector Agent**](https://claude.ai/chat/connector-agent.md) — Builds the connectors recommended by the brief
