Regenerates reference/rest/ from the platform's OpenAPI spec. Not published: this
folder is not in SUMMARY.md.

The served spec answers only on localhost, so export it from a platform checkout
of the release running on prod, with the workspace packages built or path-mapped:

  git -C <fastn-platform> checkout <release-tag>
  // export-spec.mts, at the repo root
  import { writeFileSync } from "node:fs";
  const { publicSpec } = await import("./services/api/src/openapi.ts");
  writeFileSync(process.argv[2], JSON.stringify(publicSpec));
  npx tsx export-spec.mts /tmp/spec.json

Then, from the root of this repo:

  python3 scripts/rest-reference/generate.py /tmp/spec.json --release <release-tag>

Only the resources in PAGES are published, EXCLUDE_OPS removes routes customers
cannot use, and the run fails if an internal name survives in the output. Do not
edit reference/rest/ by hand: the next run overwrites it.
