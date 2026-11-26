#!/usr/bin/env python3
"""Generate the docs' architecture diagrams as theme-aware SVGs.

Every diagram uses the same palette as the lifecycle and Welcome page images
and switches with the reader's light or dark mode. Edit a diagram below, then
run from the repo root:  python3 scripts/diagrams.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(".gitbook/assets/diagrams")
W = 680

STYLE = """<style>
:root{--bg:#ffffff;--fg:#17171f;--mut:#5e5e72;--line:#c9c9d6;
--team:#5b4cf0;--teamc:#efedff;--cust:#0e8f7e;--custc:#e3f6f3;--fastn:#3c3c52;--fastnc:#ececf3}
@media (prefers-color-scheme:dark){:root{--bg:#121218;--fg:#ececf2;--mut:#9d9db0;--line:#3a3a48;
--team:#9a8fff;--teamc:#26224a;--cust:#45d1bd;--custc:#12312d;--fastn:#c7c7d8;--fastnc:#24242f}}
.bg{fill:var(--bg)}
.h{fill:var(--fg);font-size:14px;font-weight:600}
.s{fill:var(--mut);font-size:12px}
.l{fill:var(--fg);font-size:12px}
.team{fill:var(--teamc);stroke:var(--team);stroke-width:1}
.cust{fill:var(--custc);stroke:var(--cust);stroke-width:1}
.fastn{fill:var(--fastnc);stroke:var(--fastn);stroke-width:1}
.frame{fill:none;stroke:var(--line);stroke-width:1;stroke-dasharray:4 4}
.life{stroke:var(--line);stroke-width:1;stroke-dasharray:3 4}
.arr{stroke:var(--mut);stroke-width:1.4;fill:none}
.ah{fill:var(--mut)}
</style>"""


def svg(name, height, title, desc, body):
    doc = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {height}" width="{W}" height="{height}" '
        'font-family="Inter, -apple-system, Segoe UI, Roboto, sans-serif" role="img" aria-labelledby="t d">\n'
        f'<title id="t">{escape(title)}</title>\n<desc id="d">{escape(desc)}</desc>\n{STYLE}\n'
        '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        'orient="auto"><path class="ah" d="M0 0L10 5L0 10z"/></marker></defs>\n'
        f'<rect class="bg" width="{W}" height="{height}" rx="12"/>\n'
        f'<g text-anchor="middle" dominant-baseline="central">\n{body}</g>\n</svg>\n'
    )
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(doc)


def box(x, y, w, h, kind, title, sub=None):
    cx = x + w / 2
    out = f'<rect class="{kind}" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>\n'
    if sub:
        out += f'<text class="h" x="{cx}" y="{y + h / 2 - 9}">{escape(title)}</text>'
        out += f'<text class="s" x="{cx}" y="{y + h / 2 + 10}">{escape(sub)}</text>\n'
    else:
        out += f'<text class="h" x="{cx}" y="{y + h / 2}">{escape(title)}</text>\n'
    return out


def arrow(x1, y1, x2, y2, dashed=False):
    dash = ' stroke-dasharray="4 4"' if dashed else ""
    return f'<line class="arr" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"{dash} marker-end="url(#a)"/>\n'


def text(x, y, s, cls="s"):
    return f'<text class="{cls}" x="{x}" y="{y}">{escape(s)}</text>\n'


def sequence(name, title, desc, lanes, steps):
    """lanes: [(label, kind)], steps: [(from, to, label)] with from == to for a note."""
    n = len(lanes)
    lane_w = (W - 40) / n
    xs = [20 + lane_w * i + lane_w / 2 for i in range(n)]
    bw = min(150, lane_w - 20)
    top, gap = 108, 52
    height = top + gap * (len(steps) - 1) + 50
    body = ""
    for (label, kind), x in zip(lanes, xs):
        body += box(x - bw / 2, 20, bw, 44, kind, label)
        body += f'<line class="life" x1="{x}" y1="64" x2="{x}" y2="{height - 20}"/>\n'
    for i, (a, b, label) in enumerate(steps):
        y = top + gap * i
        if a == b:
            body += f'<rect class="fastn" x="{xs[a] - 95}" y="{y - 15}" width="190" height="30" rx="6"/>\n'
            body += text(xs[a], y, f"{i + 1}. {label}", "l")
            continue
        sign = 1 if b > a else -1
        body += text((xs[a] + xs[b]) / 2, y - 12, f"{i + 1}. {label}", "l")
        body += arrow(xs[a] + 4 * sign, y + 4, xs[b] - 6 * sign, y + 4)
    svg(name, height, title, desc, body)


# 1. Authentication: from your API key to a customer's connected app
sequence(
    "auth-flow.svg",
    "How authentication works",
    "Your backend mints a short-lived embed token for one customer with your API key. Only the token reaches "
    "your frontend, which opens the widget with it. The customer signs in to their app in the widget, and fastn "
    "stores the credential encrypted for that customer.",
    [("Your backend", "team"), ("fastn", "fastn"), ("Your frontend", "team"), ("Customer's app", "cust")],
    [
        (0, 1, "Mint token"),
        (1, 0, "Embed token, 8 h"),
        (0, 2, "Token only"),
        (2, 1, "Open widget"),
        (1, 3, "Customer signs in"),
        (3, 1, "Credential saved"),
    ],
)

# 2. Running an integration for one customer
sequence(
    "run-for-a-customer.svg",
    "Running an integration for one customer",
    "Your backend calls a workflow or a webhook trigger and names the customer with x-org-id. fastn loads that "
    "customer's setup, calls their apps with their connections, and returns the result inline or an execution "
    "id to poll.",
    [("Your backend", "team"), ("fastn", "fastn"), ("Customer's apps", "cust")],
    [
        (0, 1, "Run, with x-org-id"),
        (1, 1, "Load customer's setup"),
        (1, 2, "Call their apps"),
        (2, 1, "Data"),
        (1, 0, "Result, or execution id"),
    ],
)

# 3. The two MCP addresses
body = text(180, 40, "Build integrations", "h") + text(500, 40, "Use integrations from AI agents", "h")
body += '<rect class="frame" x="30" y="60" width="300" height="300" rx="12"/>\n'
body += '<rect class="frame" x="350" y="60" width="300" height="300" rx="12"/>\n'
body += box(45, 80, 130, 56, "team", "Your team", "Claude, Cursor")
body += box(185, 80, 130, 56, "cust", "Your customer", "If you allow it")
body += arrow(110, 136, 110, 176) + arrow(250, 136, 250, 176)
body += box(45, 180, 270, 56, "fastn", "fastn MCP server", "mcp.fastn.dev/fastn-workspace")
body += arrow(180, 236, 180, 276)
body += box(45, 280, 270, 56, "team", "Your integrations", "Connectors, workflows, widget")
body += box(365, 80, 270, 56, "team", "Your AI agent", "Acts for each customer")
body += arrow(500, 136, 500, 176)
body += box(365, 180, 270, 56, "fastn", "fastn MCP gateway", "fastn Connect")
body += arrow(500, 236, 500, 276)
body += box(365, 280, 270, 56, "cust", "Each customer's apps", "With their own sign-in")
svg(
    "mcp-server-and-gateway.svg", 384, "The fastn MCP server and the fastn MCP gateway",
    "Two MCP addresses for two jobs. Your team, and your customers if you allow it, connect an AI tool to the "
    "fastn MCP server to build and manage integrations. Your AI agent connects to the fastn MCP gateway, fastn "
    "Connect, to use each customer's apps as tools with that customer's own sign-in.", body,
)

# 4. How an API change gets fixed
body = ""
xs = [20, 185, 350, 515]
items = [("fastn", "App changes API", "Vendor update"), ("fastn", "Maintainer agent", "Proposes a patch"),
         ("team", "Your team reviews", "Pending updates"), ("cust", "Fix goes live", "Every customer")]
for x, (kind, t, s) in zip(xs, items):
    body += box(x, 30, 145, 56, kind, t, s)
for x in xs[:-1]:
    body += arrow(x + 145, 58, x + 162, 58)
svg(
    "maintainer-flow.svg", 116, "How an API change gets fixed",
    "An app changes its API. The maintainer agent detects it and proposes a patch. Your team reviews it in "
    "Health, Pending updates. Once accepted, the fix applies to every customer's setup.", body,
)

print("Wrote", ", ".join(sorted(p.name for p in OUT.glob("*.svg"))))


# ---------------------------------------------------------------- architecture
C1, C2, C3, BW = 125, 340, 555, 190
def col(c):
    return c - BW / 2
body = ""
body += box(col(C1), 20, BW, 50, "team", "Your team", "dashboard or your AI tool")
body += box(col(C2), 20, BW, 50, "team", "Your backend", "holds the API key")
body += box(col(C3), 20, BW, 50, "cust", "Your customer", "inside your product")
body += f'<rect class="frame" x="20" y="92" width="{W - 40}" height="262" rx="10"/>\n'
body += text(52, 106, "fastn", "h")
rows = [
    (118, [("fastn MCP server", "build and manage"), ("API and SDK", "embed tokens, runs"), ("Widget", "connect and configure")]),
    (200, [("Integrations", "connectors, workflows"), ("Workflow runtime", "one customer per run"), ("Connections", "each customer's sign-ins")]),
    (282, [("Maintainer agent", "watches apps, proposes fixes"), ("fastn Connect", "MCP gateway for AI agents"), ("Health and Logs", "every run and event")]),
]
for y, cells in rows:
    for c, (t, s) in zip((C1, C2, C3), cells):
        body += box(col(c), y, BW, 54, "fastn", t, s)
for c in (C1, C2, C3):
    body += arrow(c, 70, c, 116)
body += arrow(C1, 172, C1, 198)
body += arrow(C2, 172, C2, 198)
body += arrow(C3, 172, C3, 198)
body += arrow(C1 + BW / 2, 227, col(C2) - 2, 227)
body += arrow(col(C3), 227, C2 + BW / 2 + 2, 227)
body += arrow(C1, 280, C1, 256)
body += arrow(C2, 280, C2, 256)
body += box(col(C1), 392, BW, 50, "team", "Your AI agents", "act for one customer")
body += box(col(C3), 392, BW, 50, "cust", "Customers' apps", "CRM, Slack, Jira, 1,000+ more")
body += arrow(C1 + 40, 392, C2 - 30, 338)
body += arrow(C3, 356, C3, 390)
body += text(C3 - 140, 374, "calls with that customer's sign-in", "s")
svg(
    "architecture.svg", 462,
    "fastn architecture",
    "Your team builds in the fastn dashboard or from an AI tool through the fastn MCP server. Your backend holds the "
    "API key and uses the API and SDK to get embed tokens and start runs. Your customer uses the widget inside your "
    "product to connect apps, which stores a connection per customer. Integrations hold connectors, workflows and "
    "triggers; the workflow runtime runs them once per customer with that customer's connections. The maintainer "
    "agent watches apps and proposes fixes, fastn Connect gives your AI agents each customer's apps as tools, and "
    "Health and Logs record every run and event. All calls reach the customers' apps with that customer's sign-in.",
    body,
)
print("Wrote architecture.svg")


# ------------------------------------------------------------- organizations
def chip(x, y, w, label, color):
    return (f'<rect style="fill:var(--bg);stroke:var(--{color})" x="{x}" y="{y}" width="{w}" height="26" rx="6"/>\n'
            + text(x + w / 2, y + 13, label, "l"))


body = '<rect class="team" x="20" y="20" width="640" height="104" rx="10"/>\n'
body += text(340, 42, "Your organization", "h")
body += text(340, 62, "The SaaS company: builds the integrations and the widget")
body += text(136, 99, "Team members", "l")
for i, role in enumerate(["Owner", "Admin", "Developer", "Operator", "Viewer"]):
    body += chip(210 + i * 90, 86, 82, role, "team")
customers = [("Customer A", ["User", "User", "User"], ["HubSpot", "Slack"]),
             ("Customer B", ["User"], ["Salesforce"]),
             ("Customer C", ["User", "User"], ["Zoho", "Jira"])]
for i, (name, users, apps) in enumerate(customers):
    x = 20 + i * 222
    cx = x + 98
    body += arrow(340, 124, cx, 166)
    body += f'<rect class="cust" x="{x}" y="170" width="196" height="176" rx="10"/>\n'
    body += text(cx, 190, name, "h") + text(cx, 208, "Its own organization")
    body += text(cx, 234, "End users", "l")
    for j, u in enumerate(users):
        body += chip(cx - (len(users) * 58 - 6) / 2 + j * 58, 246, 52, u, "cust")
    body += text(cx, 294, "Connections", "l")
    for j, a in enumerate(apps):
        body += chip(cx - (len(apps) * 86 - 6) / 2 + j * 86, 306, 80, a, "cust")
body += text(340, 370, "Each customer is isolated: its users, connections and data never reach another customer.")
svg(
    "organization-hierarchy.svg", 392,
    "Your organization, its customers and their end users",
    "Your organization is the SaaS company that builds the integrations, with team members in roles such as Owner, "
    "Admin and Developer. Under it, each customer is its own organization with its own end users and its own "
    "connections to apps such as HubSpot, Salesforce or Jira. Customers are isolated from each other.",
    body,
)
print("Wrote organization-hierarchy.svg")
