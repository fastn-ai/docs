#!/usr/bin/env python3
"""Generate reference/rest/ from the platform's OpenAPI spec.

The spec is written for the platform team: it carries operator-only routes and
names internal systems. Only the resources in PAGES are published, EXCLUDE_OPS
drops the service-only and operator-only routes among them, and scrub() removes
internal names from the text. The run fails if a banned term survives, so a new
internal name in the spec stops the publish instead of reaching the public site.

Usage: python3 scripts/rest-reference/generate.py <spec.json> --release <tag>
See scripts/rest-reference/README.txt for how to export the spec.
"""
import argparse, copy, json, os, re, sys

METHODS = ("get", "post", "put", "patch", "delete")
OUT = "reference/rest"
RAW_SPEC = "https://raw.githubusercontent.com/fastn-ai/docs/main/reference/rest/openapi.json"

PAGES = [
    ("workflows", "Workflows", "Create, publish, run and inspect workflows.",
     ["workflows", "execute", "executions", "workflow-categories", "workflow-labels", "integrations"], ""),
    ("installations", "Installations and configs", "Each customer's setup of a widget, its triggers and its configuration values.",
     ["installations", "configs", "config-drafts"],
     "An installation is one customer's setup of a widget. Creating, changing or deleting one can run the widget's [callbacks](../widget-callbacks.md)."),
    ("widgets", "Widgets and embedding", "Widgets, embed tokens, share links and setup links.",
     ["widgets", "embed", "setup-links"],
     "`lifecycle_hooks` on a widget names the workflows that run as [callbacks](../widget-callbacks.md)."),
    ("triggers", "Triggers and events", "Webhook, schedule and app event triggers, received events and the dead-letter queue.",
     ["triggers", "schedulers", "app-triggers", "webhooks", "dlq", "events"], ""),
    ("event-subscriptions", "Event subscriptions", "Endpoints of yours that fastn delivers events to.",
     ["event-subscriptions"], ""),
    ("connectors", "Connectors", "Connectors, actions, auth methods, webhook configs and mock stubs.",
     ["connectors", "actions", "action-folders", "auth-methods", "auth-providers", "entities", "webhook-configs", "connector-version-pins", "mock", "probes"], ""),
    ("connections", "Connections", "Connected accounts and how they are created.",
     ["connections", "connect-links", "oauth", "saas-connectors"], ""),
    ("unified", "Unified API", "Unified records, the catalog, and your own unified entities.",
     ["unified", "unified-custom", "unified-catalog"], ""),
    ("observability", "Alerts and observability", "Alert rules, traces and the audit log.",
     ["alerts", "traces", "audit-log"],
     "The format of `deliveries` on an alert rule is in [Set deliveries through the API](../../operate/alerts.md#set-deliveries-through-the-api)."),
    ("environments", "Environments and secrets", "Environments, their config values, and secrets.",
     ["environments", "env-configs", "secrets"], ""),
    ("organization", "Organization and access", "Customers, people, roles, teams and API keys.",
     ["orgs", "api-keys", "me", "users", "roles", "grants", "teams"],
     "The `/v1/orgs` routes are how you create and manage your customers."),
]

# Routes under a published resource that a customer has no use for: called only
# by fastn's own services, only by a fastn operator, or returning decrypted
# secrets to the dashboard.
EXCLUDE_OPS = {
    "createUnifiedCatalogCategory", "updateUnifiedCatalogCategory", "deleteUnifiedCatalogCategory",
    "createUnifiedCatalogEntity", "updateUnifiedCatalogEntity", "deleteUnifiedCatalogEntity",
    "createUnifiedConnectorMapping", "updateUnifiedConnectorMapping", "deleteUnifiedConnectorMapping",
    "testUnifiedEntityOperation",
    "eventServiceHealth", "getWorkflowDocBrief", "recordConnectorExecution",
    "redeemEmbedShareLink", "redeemMcpConnectCode", "reportEmbedEvents",
    "getEmbedIframe", "getEmbedAsset", "embedOauthDone",
    "getConnectorActivity", "getAuthProviderCredentials",
    "importUclWebhookConfigs", "getUclWebhookConfigs", "deleteUclWebhookConfigs",
    "decryptConnection", "getConnectionCredentials",
    "importConnectorHubActions", "githubInstallCallback", "githubWebhook",
    "reconcileInstallationMirror", "getMyContext",
    "listPendingReviewOrgs", "approveOrg", "rejectOrg",
    "updateOrgV1Bridge", "switchAccount", "completeWorkflowPromotion",
}
EXCLUDE_TAGS = {"Admin"}

# Whole phrases rewritten before the banned-term check; the rest of a sentence
# stays. Order matters: longer phrases first.
REWRITES = [
    (r"\bRoles: platform_admin, ", "Roles: "),
    (r"\b, platform_admin\b", ""),
    (r"\bplatform_admin, ", ""),
    (r"\ba ucl: id for a UCL-held connection\b", "an id starting ucl: for a managed connection"),
    (r"\bUCL-held\b", "managed"),
    (r"\bUCL-managed\b", "managed"),
    (r"\bGrafana Loki\b", "the log store"),
    (r"\bfrom Loki\b", "from the log store"),
    (r"\bKeycloak user id\b", "user id"),
    (r"\bKeycloak profiles\b", "user profiles"),
    (r"\bKeycloak profile\b", "user profile"),
    (r"\s+\(UCL for a migrated org\)", ""),
    (r"\bReads Postgres only\b\.?", ""),
    (r"\bRequired by the legacy connector service unless\b", "Required unless"),
    (r"\bwithout Redis\b", "while the store is unavailable"),
    (r"\bOperational rollup\b", "Summary"),
    (r"\boperational rollup\b", "summary"),
    (r"\bpre-aggregated rollups\b", "pre-aggregated counts"),
    (r"\boutcome rollup\b", "outcome counts"),
    (r"\brollup\b", "summary"),
    (r"\bLoki\b", "the log store"),
    (r"\bbring-your-own Postgres\b", "your own Postgres database"),
    (r"\bLists tenants\b", "Lists customers"),
    (r"\btenants\b", "customers"),
    (r"\bTenants\b", "Customers"),
    (r"\btenant\b", "customer"),
    (r"\bTenant\b", "Customer"),
    (r"\s+—\s+", ", "),
    (r"—", ", "),
    (r"\s+--\s+", ", "),
]
# A sentence holding one of these after REWRITES is dropped; one surviving
# anywhere in the output fails the run. "Postgres" alone is allowed only where a
# customer connects their own database, which REWRITES states explicitly.
BANNED = re.compile(r"\b(?:UCL|Keycloak|Redis|Temporal|BullMQ|Grafana|sync_jobs|LOKI_QUERY_URL|x-gateway-[a-z-]+|platform_admin|KAT-\d+|KAN-\d+|ADR-\d+|Platform admin|pg_[a-z_]+)\b|\bReads and writes Postgres\b")
ALLOWED_POSTGRES = re.compile(r"your own Postgres")


def scrub(text):
    if not isinstance(text, str):
        return text
    out = text
    for pat, rep in REWRITES:
        out = re.sub(pat, rep, out)
    if not BANNED.search(out) and not bare_postgres(out):
        return out.strip()
    kept = [s for s in re.split(r"(?<=[.;:])\s+", out) if not BANNED.search(s) and not bare_postgres(s)]
    return " ".join(kept).strip()


def bare_postgres(s):
    return "Postgres" in ALLOWED_POSTGRES.sub("", s)


def scrub_tree(node):
    if isinstance(node, dict):
        for k, v in list(node.items()):
            if k in ("description", "summary") and isinstance(v, str):
                node[k] = scrub(v)
                if not node[k] and k == "description":
                    del node[k]
            elif k == "enum" and isinstance(v, list):
                node[k] = [e for e in v if e != "platform_admin"]
            else:
                scrub_tree(v)
    elif isinstance(node, list):
        for v in node:
            scrub_tree(v)


def patch_spec(spec):
    """Facts the spec does not state yet. The validator is routes/observe.ts validateDeliveries."""
    schemas = spec["components"]["schemas"]
    props = schemas["AlertDelivery"]["properties"]
    props["subject"] = {"type": "string", "description": "email, or a connection through Gmail: optional subject, one line, at most 200 characters"}
    props["targetName"] = {"type": "string", "description": "connection: optional display name of the target, at most 200 characters"}
    props.pop("connectorSlug", None)
    for path, item in spec["paths"].items():
        op = item.get("post", {})
        if op.get("operationId") == "createAlert":
            body = op["requestBody"]["content"]["application/json"]["schema"]
            body["properties"]["deliveries"]["items"] = {"$ref": "#/components/schemas/AlertDelivery"}


def select(spec):
    res_page = {r: p[0] for p in PAGES for r in p[3]}
    chosen = {p[0]: [] for p in PAGES}
    out_paths = {}
    for path, item in spec["paths"].items():
        parts = path.split("/")
        res = parts[2] if len(parts) > 2 else None
        page = res_page.get(res)
        if not page:
            continue
        for m in METHODS:
            op = item.get(m)
            if not op or op.get("operationId") in EXCLUDE_OPS or EXCLUDE_TAGS & set(op.get("tags", [])):
                continue
            op = copy.deepcopy(op)
            # Item-level parameters are not used by this spec; ops carry their own.
            for k in [k for k in op if k.startswith("x-")]:
                del op[k]
            scrub_tree(op)
            out_paths.setdefault(path, {})[m] = op
            chosen[page].append((res, path, m, op))
    return chosen, out_paths


def reachable_components(paths, components):
    """Only what the published operations refer to, so nothing else leaves with the spec."""
    keep, todo = {}, [paths]
    while todo:
        for ref in re.findall(r'"#/components/([A-Za-z]+)/([^"]+)"', json.dumps(todo.pop())):
            if ref[1] not in keep.setdefault(ref[0], {}):
                node = components[ref[0]][ref[1]]
                keep[ref[0]][ref[1]] = node
                todo.append(node)
    if "securitySchemes" in components:
        keep["securitySchemes"] = components["securitySchemes"]
    return keep


def resolve(schema, spec, seen=()):
    ref = schema.get("$ref") if isinstance(schema, dict) else None
    if not ref:
        return schema, seen
    if ref in seen:
        return {"type": "object"}, seen
    node = spec
    for part in ref.lstrip("#/").split("/"):
        node = node[part]
    return node, seen + (ref,)


def type_of(s, spec):
    s, _ = resolve(s, spec)
    if not isinstance(s, dict):
        return "any"
    for key in ("anyOf", "oneOf", "allOf"):
        if key in s:
            parts = []
            for v in s[key]:
                t = type_of(v, spec)
                if t != "null" and t not in parts:
                    parts.append(t)
            return (" or " if key != "allOf" else " and ").join(parts) or "any"
    t = s.get("type", "any")
    if isinstance(t, list):
        t = " or ".join(x for x in t if x != "null")
    if t == "array":
        return type_of(s.get("items", {}), spec) + "[]"
    if "enum" in s:
        return t
    if "const" in s:
        return t
    return t


def flatten(schema, spec, prefix="", depth=0, seen=(), rows=None, limit=60):
    rows = [] if rows is None else rows
    schema, seen = resolve(schema, spec, seen)
    if not isinstance(schema, dict):
        return rows
    for key in ("allOf", "anyOf", "oneOf"):
        for v in schema.get(key, []):
            v2, _ = resolve(v, spec, seen)
            if isinstance(v2, dict) and v2.get("properties"):
                flatten(v2, spec, prefix, depth, seen, rows, limit)
    required = set(schema.get("required") or [])
    for name, prop in (schema.get("properties") or {}).items():
        if len(rows) >= limit:
            return rows
        full = f"{prefix}{name}"
        rp, s2 = resolve(prop, spec, seen)
        rp = rp if isinstance(rp, dict) else {}
        desc = scrub(rp.get("description", "") or "")
        extra = []
        enum = rp.get("enum") or (rp.get("items", {}) if isinstance(rp.get("items"), dict) else {}).get("enum")
        if enum:
            extra.append("One of: " + ", ".join(f"`{e}`" for e in enum if e is not None) + ".")
        if "const" in rp:
            extra.append(f"Always `{rp['const']}`.")
        if "default" in rp and rp["default"] not in (None, "", [], {}):
            extra.append(f"Default: `{json.dumps(rp['default'])}`.")
        rows.append((full, type_of(rp, spec), name in required, " ".join(x for x in [desc, *extra] if x)))
        if depth < 3:
            items, s3 = resolve(rp.get("items", {}), spec, s2) if rp.get("type") == "array" else ({}, s2)
            if isinstance(items, dict) and items.get("properties"):
                flatten(items, spec, f"{full}[].", depth + 1, s3, rows, limit)
            elif rp.get("properties") or any(k in rp for k in ("allOf", "anyOf", "oneOf")):
                flatten(rp, spec, f"{full}.", depth + 1, s2, rows, limit)
    return rows


def prose(text):
    """Escape text for Markdown, leaving code spans untouched."""
    parts = re.split(r"(`[^`]*`)", text or "")
    for i in range(0, len(parts), 2):
        parts[i] = parts[i].replace("<", "&lt;").replace("{%", "{ %")
    return "".join(parts)


def cell(text):
    return prose(text).replace("\n", " ").replace("|", "\\|").strip()


def code_cell(text):
    return "`" + str(text).replace("|", "\\|") + "`"


def table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(lines)


def heading(op, method, path):
    s = (op.get("summary") or f"{method.upper()} {path}").strip()
    s = re.split(r"(?<=[.:;])\s", s)[0].rstrip(".:;")
    return prose(s if len(s) <= 90 else s[:87].rsplit(" ", 1)[0] + "...")


def render_op(op, method, path, spec):
    out = [f"### {heading(op, method, path)}", "", "```http", f"{method.upper()} {path}", "```", ""]
    summary = (op.get("summary") or "").strip()
    desc = (op.get("description") or "").strip()
    first = re.split(r"(?<=[.:;])\s", summary)[0].rstrip(".:;") if summary else ""
    rest = summary[len(first):].lstrip(".:; ").strip() if summary else ""
    body = " ".join(x for x in [rest, desc] if x)
    if body:
        out += [prose(body), ""]
    out += [f"Operation: `{op['operationId']}`", ""]
    params = []
    for p in op.get("parameters") or []:
        p, _ = resolve(p, spec)
        if not p.get("name") or p.get("in") == "cookie":
            continue
        d = scrub(p.get("description", "") or (p.get("schema") or {}).get("description", "") or "")
        sch = p.get("schema") or {}
        rs, _ = resolve(sch, spec)
        extra = ""
        if isinstance(rs, dict) and rs.get("enum"):
            extra = " One of: " + ", ".join(f"`{e}`" for e in rs["enum"] if e is not None) + "."
        params.append([code_cell(p["name"]), p.get("in", ""), type_of(sch, spec), "Yes" if p.get("required") else "No", cell(d + extra)])
    if params:
        out += ["**Parameters**", "", table(["Name", "In", "Type", "Required", "Description"], params), ""]
    rb = op.get("requestBody")
    if rb:
        rb, _ = resolve(rb, spec)
        content = (rb.get("content") or {})
        media = content.get("application/json") or next(iter(content.values()), {})
        rows = flatten(media.get("schema") or {}, spec)
        if rows:
            out += ["**Request body**", "", table(["Field", "Type", "Required", "Description"],
                    [[code_cell(a), code_cell(b), "Yes" if c else "No", cell(d)] for a, b, c, d in rows]), ""]
    resp = op.get("responses") or {}
    if resp:
        out += ["**Responses**", ""]
        fields = None
        for status, r in resp.items():
            r, _ = resolve(r, spec)
            out.append(f"* `{status}`: {cell(scrub(r.get('description', '') or '')) or 'No description.'}")
            if fields is None and str(status).startswith("2"):
                media = (r.get("content") or {}).get("application/json")
                if media and media.get("schema"):
                    fields = flatten(media["schema"], spec, limit=40) or None
        out.append("")
        if fields:
            out += ["**Response fields**", "", table(["Field", "Type", "Description"],
                    [[code_cell(a), code_cell(b), cell(d)] for a, b, _, d in fields]), ""]
    return "\n".join(out)


def render_page(page, ops, spec):
    slug, title, blurb, resources, intro = page
    out = ["---", f'description: "{blurb}"', "---", "", f"# {title}", ""]
    if intro:
        out += [intro, ""]
    out += ["Base URL, authentication and errors are on the [REST API overview](README.md).", ""]
    order = {r: i for i, r in enumerate(resources)}
    ops = sorted(ops, key=lambda o: (order[o[0]], o[1], METHODS.index(o[2])))
    current = None
    for res, path, m, op in ops:
        if res != current:
            out += [f"## {res.replace('-', ' ').capitalize()}", ""]
            current = res
        out.append(render_op(op, m, path, spec))
    return "\n".join(out).rstrip() + "\n"


def render_readme(release):
    links = "\n".join(f"* [{p[1]}]({p[0]}.md): {p[2]}" for p in PAGES)
    return f"""---
description: "Every REST endpoint you can call, generated from fastn's OpenAPI spec."
---

# REST API reference

This reference lists the REST endpoints you can call with an API key. It is generated from the platform's OpenAPI spec (release `{release}`). To run workflows and mint embed tokens, start with the shorter [HTTP API](../api.md) guide.

{links}

## Base URL

```
https://api.fastn.dev
```

Paths here start with `/v1`. The same routes also answer under `/api/v1`, which is the form the [HTTP API](../api.md) guide uses.

## Authentication

Send an API key as a bearer token. Keys are created under [API keys and MCP](../../manage/api-keys.md).

```bash
curl https://api.fastn.dev/v1/installations \\
  -H "Authorization: Bearer fsk_live_<your-key>"
```

A key can only do what its permissions allow, and a call can be limited further by your role, your plan or the customer it acts for. Some routes are meant for a person signed in to the dashboard or for an embed session, so they may refuse an API key with `401` or `403`.

To act for one of your customers, send `x-org-id` with fastn's id for that customer or your own id for it. A key that requires identity verification also needs `x-user-id` and `x-identity-hmac`. See [Authentication and API keys](../../tutorials/developer/authentication-and-api-keys.md).

## Responses and errors

Most routes wrap their result as `{{ "data": ... }}` and report a failure as `{{ "error": "..." }}` with an HTTP status code, often with a `code` you can match on. See [Errors and failure states](../errors.md). Rate limits are on the [HTTP API](../api.md#rate-limits) page.

## Operation names

Each endpoint lists its operation name. Where the endpoint is also a fastn MCP tool, the tool has the same name, so `listInstallations` here is `fastnPlatform__listInstallations` from your AI tool.

## Download the spec

The spec for everything on these pages, in OpenAPI 3.1 JSON, is at [openapi.json]({RAW_SPEC}). Import it into Postman or a client generator.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--release", required=True)
    args = ap.parse_args()
    spec = json.load(open(args.spec, encoding="utf-8"))
    patch_spec(spec)
    chosen, out_paths = select(spec)
    os.makedirs(OUT, exist_ok=True)
    scrub_tree(spec["components"])
    files = {f"{OUT}/README.md": render_readme(args.release)}
    for page in PAGES:
        files[f"{OUT}/{page[0]}.md"] = render_page(page, chosen[page[0]], spec)
    used_tags = {t for i in out_paths.values() for o in i.values() for t in o.get("tags", [])}
    public = {
        "openapi": spec["openapi"],
        "info": {"title": "fastn REST API", "version": args.release},
        "servers": [{"url": "https://api.fastn.dev", "description": "Production"}],
        "security": spec.get("security"),
        "tags": [t for t in spec.get("tags", []) if t["name"] in used_tags],
        "paths": out_paths,
        "components": reachable_components(out_paths, spec["components"]),
    }
    scrub_tree(public["tags"])
    files[f"{OUT}/openapi.json"] = json.dumps(public, indent=1, ensure_ascii=False) + "\n"
    failures = []
    for name, text in files.items():
        for m in BANNED.finditer(text):
            failures.append((name, m.group(0), text[max(0, m.start() - 60):m.end() + 40].replace("\n", " ")))
        for line in text.splitlines():
            if bare_postgres(line) and name.endswith(".md"):
                failures.append((name, "Postgres", line[:120]))
    if failures:
        for f in failures[:40]:
            print("BANNED", f, file=sys.stderr)
        sys.exit(f"{len(failures)} banned term(s) survived; add a rewrite or exclude the operation")
    for name, text in files.items():
        with open(name, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(f"{sum(len(v) for v in chosen.values())} operations on {len(PAGES)} pages")
    for p in PAGES:
        print(f"  {p[0]}: {len(chosen[p[0]])}")


if __name__ == "__main__":
    main()
