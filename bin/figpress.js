#!/usr/bin/env node
// `figpress` (npm): the family's members and its website, from the same family.json as the site.
import { readFileSync } from "node:fs";

const read = (rel) => JSON.parse(readFileSync(new URL(rel, import.meta.url), "utf8"));
const family = read("../family.json");
const { version } = read("../package.json");

const lines = [`figpress ${version}: ${family.about}`, ""];
for (const m of family.members) {
  lines.push(`  ${m.name}${m.released ? "" : " (not released yet)"}`, `    ${m.purpose}`, `    ${m.repository}`, "");
}
lines.push(`More: ${family.website}`);
console.log(lines.join("\n"));
