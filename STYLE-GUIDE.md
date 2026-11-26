# Fastn docs style guide

How every page in these docs is written. It is for anyone editing this repo, human or AI agent. It is not published to the site.

## Voice

- Write to the reader as **you**. Fastn is **Fastn** or **we** only when the product itself acts or decides ("Fastn retries the call"), never **us** in the sense of the docs team ("what should page us").
- Plain and direct. Say what a thing does, then how to use it. No marketing adjectives (powerful, seamless, effortless, robust), no slogans, no opening with what something is *not*.
- Be honest about limits, once. State a warning in one place, in full, and link to it from everywhere else (see [Warnings](#warnings)).
- No jokes or wordplay in headings or warnings. A heading names the task: "Turn on failure alerts", not "Make failure loud".
- Keep Fastn's internal words out of reader-facing pages. On pages for end users, the partner is "the product you use", never "the SaaS company".

## Spelling and naming

- **US English**: catalog, organization, authorize, behavior, canceled, color. Quote product copy exactly as the app shows it, even where it differs, and only inside quotes or bold UI labels.
- **Fastn** is capitalized in prose, including in titles, descriptions and mid-sentence. Code, identifiers, headers, URLs and file paths stay as written (`X-fastn-Test-Mode`, `fastn.connector.<slug>`, `mcp.fastn.dev`), and so do UI labels the app shows in lowercase.
- One name per thing:

| Use | Not | Note |
| --- | --- | --- |
| customer | tenant, end org, user (for the business) | Where a UI label or id says *user* or *tenant*, add "(the customer)" on first mention. |
| end user | customer user | A person at a customer who uses the widget. |
| organization | org, workspace (in prose) | `x-org-id` and `orgId` stay as written: they are identifiers. |
| connector | integration (for the API definition) | An **integration** is what you offer in the widget. |
| connection | credential, account link | One customer's authorized link to one system. |
| Schedule | Scheduler, Scheduled trigger | Until the product uses one label everywhere, keep the hint on Triggers. |

- Spell out an abbreviation on first use on each page: "dead-letter queue (DLQ)".

## Formatting

- **Sentence case** for every title, heading, link text and table header: "Customize an integration", not "Customizing Your Integrations".
- **UI labels in bold**, exactly as the app shows them, including case: **Run Live**, **Create link**.
- **Menu paths** are full sidebar paths with arrows, the same on every page: **Operate → Health → Alerts**, **Build → Integrations → Triggers**, **Embed → Widget**.
- **Code, fields, headers and ids** in backticks: `x-org-id`, `peakSandboxMB`.
- Use a list when a sentence would carry three or more items or ideas.
- Dashes: use a comma, colon or parentheses. Do not use a spaced hyphen ( - ) as a dash.
- Every page has a one-line `description:` in its frontmatter. It shows in search, link previews and `llms.txt`.
- Give pages distinct titles. "Build overview", not a third page called "Overview".
- Information in a screenshot is also in the text. A caption describes the screen ("The Add a trigger dialog"); it never says "read them here".
- Use the public API prefix `/v1` and the host `https://api.fastn.dev` in examples. Do not mix `YOUR_FASTN_HOST` and a real host on one page.

## Warnings

- Use `{% hint style="warning" %}` for something that can lose data, expose credentials, or affect every customer at once. Use `info` for everything else.
- A warning says what happens and what to do, in plain words: "Reset replaces your widget with the defaults for every customer, immediately."
- Each warning lives in full on one page. Elsewhere, one sentence and a link. The test-mode warning lives on [API keys](manage/api-keys.md): elsewhere write "Test keys act on real data. See [API keys](manage/api-keys.md)."
- Do not describe product bugs in the docs as permanent facts. Put them in the [Changelog](reference/changelog.md) with a date, a workaround and a status, and remove them when fixed.

## Page templates

Pick one per page. Do not mix task steps and reference tables on one page; link between them instead.

**How-to** (a task the reader does)

1. One line: what you will have at the end.
2. **Before you start**: who this is for (role) and what you need (plan, keys, connected app).
3. Numbered steps. Each ends with a **You should see:** line.
4. **What's next**: one to three links.

**Reference** (something the reader looks up)

1. What it is, in one or two sentences.
2. Fields, options or endpoints, as a table.
3. Limits and defaults.

**Concept** (something the reader needs to understand)

1. What it is.
2. Why it exists.
3. How it relates to the things next to it, with links.

## Checking your change

- Every product fact (a label, a limit, a default, a header) is checked against the app or the platform code before it goes in. Docs that disagree with the product are worse than no docs.
- Every link is a relative path to a file in this repo, as in `SUMMARY.md`. GitBook turns file paths into the site URLs; never write a site URL path into the source.
- A page you move or rename gets a line in `.gitbook.yaml` under `redirects`.
