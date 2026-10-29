// The npm CLI prints every member and the website, from the same family.json.
import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const family = JSON.parse(readFileSync(new URL("../family.json", import.meta.url), "utf8"));

test("prints the members and the website", () => {
  const out = execFileSync(process.execPath, [fileURLToPath(new URL("../bin/figpress.js", import.meta.url))], { encoding: "utf8" });
  for (const m of family.members) assert.ok(out.includes(m.name), m.name);
  assert.ok(out.includes(family.website));
});
