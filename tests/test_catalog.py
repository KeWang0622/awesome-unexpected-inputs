"""Regression tests for the catalog builder; uses only Python's standard library."""
import copy
from datetime import date, timedelta
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

SCRIPT = Path(__file__).with_name("catalog.py")
if not SCRIPT.exists():
    SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "catalog.py"
SPEC = importlib.util.spec_from_file_location("catalog", SCRIPT)
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)


def fixture():
    categories = [
        {"id": "controls", "name": "Controls", "name_zh": "控制",
         "description": "Control tools.", "description_zh": "控制工具。"},
        {"id": "displays", "name": "Displays", "name_zh": "显示",
         "description": "Display tools.", "description_zh": "显示工具。"},
    ]
    projects = []
    for i in range(6):
        projects.append({
            "id": f"app-{i}", "name": f"App {i}",
            "category": "Controls" if i < 3 else "Displays",
            "url": f"https://example.com/app-{i}",
            "summary": "A useful tool.", "summary_zh": "实用工具。",
            "outcome": "Control a computer.", "outcome_zh": f"专属结果{i}",
            "devices": ["Camera"], "requirements": ["Windows"],
            "status": "released" if i < 3 else "source-build",
            "evidence_url": f"https://example.com/docs/{i}",
            "evidence_note": "Upstream documents camera control.",
            "checked_at": "2026-10-26", "limitations": ["Calibration required."],
            "steps": ["Read upstream setup instructions."],
        })
    config = {
        "slug": "awesome-demo", "title": "Awesome Demo", "title_zh": "示例",
        "tagline": "Useful transformations.", "tagline_zh": "有用的转变。",
        "description": "Source-reviewed projects.", "description_zh": "资料核查项目。",
        "theme": "afterlife", "categories": categories,
        "spotlights": [
            {"id": p["id"], "from": "A & B", "to": "Useful action",
             "icon": "camera", "output": "cursor"} for p in projects
        ],
        "sibling": "[Related project](https://example.com/related)",
    }
    return projects, config


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.projects, self.config = fixture()
        self.today = date(2026, 10, 26)

    def validate(self, projects=None, config=None):
        catalog.validate(self.projects if projects is None else projects,
                         self.config if config is None else config, today=self.today)

    def test_identity_distinguishes_packages_and_normalizes_aliases(self):
        one = "https://play.google.com/store/apps/details?id=org.one"
        two = "https://play.google.com/store/apps/details?id=org.two"
        self.assertNotEqual(catalog.identity(one), catalog.identity(two))
        self.assertEqual(catalog.identity(one), catalog.identity(one + "&hl=fr"))
        self.assertEqual(catalog.identity("https://apps.apple.com/us/app/name/id123"),
                         catalog.identity("https://apps.apple.com/gb/app/other/id123"))
        self.assertEqual(catalog.identity("https://github.com/Owner/Repo.git"),
                         catalog.identity("https://www.github.com./owner/repo/"))
        self.assertNotEqual(catalog.identity("https://example.com/view?project=one"),
                            catalog.identity("https://example.com/view?project=two"))
        self.assertEqual(catalog.identity("https://example.com/x?b=2&a=1"),
                         catalog.identity("https://example.com/x?a=1&b=2&utm_source=demo"))

    def test_invalid_url_ports_and_private_hosts_raise_catalog_errors(self):
        for value in ["https://example.com:bad/", "https://example.com:70000/",
                      "https://127.0.0.1/", "https://device.local/", "https://user@example.com/",
                      "http://example.com/", "https://example.com/(raw)"]:
            with self.subTest(value=value), self.assertRaises(catalog.CatalogError):
                catalog.public_url(value)
        catalog.public_url("https://example.com:443/a%20b")

    def test_config_rejects_bad_ids_duplicate_ids_and_unknown_diagrams(self):
        mutations = [
            lambda c: c["categories"][0].update(id='bad" onclick="x'),
            lambda c: c["categories"][1].update(id="controls"),
            lambda c: c["spotlights"][0].update(icon="unknown"),
            lambda c: c["spotlights"][0].update(output="unknown"),
            lambda c: c.update(theme=[]),
            lambda c: c["spotlights"][0].update(id="missing"),
        ]
        for mutate in mutations:
            c = copy.deepcopy(self.config)
            mutate(c)
            with self.subTest(config=c), self.assertRaises(catalog.CatalogError):
                self.validate(config=c)
        self.validate()

    def test_evidence_status_duplicates_and_unknown_fields_are_rejected(self):
        mutations = [
            lambda ps: ps[0].pop("evidence_url"),
            lambda ps: ps[0].update(evidence_note=" "),
            lambda ps: ps[0].update(status="tested"),
            lambda ps: ps[1].update(id=ps[0]["id"]),
            lambda ps: ps[1].update(name=ps[0]["name"].upper()),
            lambda ps: ps[1].update(url=ps[0]["url"] + "/"),
            lambda ps: ps[0].update(unreviewed=True),
            lambda ps: ps[0].update(media_url="https://example.com/demo"),
        ]
        for mutate in mutations:
            ps = copy.deepcopy(self.projects)
            mutate(ps)
            with self.subTest(projects=ps), self.assertRaises(catalog.CatalogError):
                self.validate(projects=ps)

    def test_review_dates_use_explicit_today_and_calendar_validity(self):
        self.projects[0]["checked_at"] = self.today.isoformat()
        self.validate()
        for value in [(self.today + timedelta(days=1)).isoformat(), "2026-02-30", "2026-2-01"]:
            self.projects[0]["checked_at"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.validate()

    def test_rendering_preserves_plain_text_evidence_and_attribution(self):
        self.projects[0].update(
            name="App 0 *special*",
            evidence_note="Use a *specific* camera.",
            media_url="https://example.com/demo",
            media_note="Photo credit: Ada & Lin."
        )
        self.validate()
        details = catalog.render_details(self.projects, self.config)
        self.assertIn(r"**Evidence:** Use a \*specific\* camera\.", details)
        self.assertIn(r"**Visual credit / context:** Photo credit: Ada &amp; Lin\.", details)
        self.assertIn(r"### App 0 \*special\*", details)
        readme = catalog.render_readme(self.projects, self.config)
        self.assertIn(self.config["sibling"], readme)
        self.assertIn("not screenshots or test evidence", readme)

    def test_markdown_local_links_titles_references_fragments_and_fences(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "target file.md").write_text("# Hello *world*\n", encoding="utf-8")
            readme = root / "README.md"
            readme.write_text(
                '# Start\n[one](<target file.md#hello-world> "title")\n'
                "[two](target%20file.md?view=1#hello-world)\n"
                "[three][Some Label]\n[Some Label]: <target file.md#hello-world>\n"
                "`[example](missing.md)`\n"
                "```md\n[example](missing.md)\n```\n", encoding="utf-8")
            catalog.local_links(root)
            for body in ['[missing](missing.md "title")', "[bad](target%20file.md#absent)",
                         "[bad][undefined]", "[escape](../outside.md)"]:
                readme.write_text(body, encoding="utf-8")
                with self.subTest(body=body), self.assertRaises(catalog.CatalogError):
                    catalog.local_links(root)

    def test_bilingual_search_combines_filters(self):
        matches = catalog.find(self.projects, "专属结果4", status="source-build", category="Displays")
        self.assertEqual([p["id"] for p in matches], ["app-4"])
        self.assertEqual(catalog.find(self.projects, "专属结果4", status="released"), [])
        self.assertEqual(len(catalog.find(self.projects, "camera WINDOWS")), 6)

    def test_schema_matches_structural_contract_and_documents_runtime_checks(self):
        schema = catalog.project_schema(self.config)
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        item = schema["items"]
        self.assertEqual(set(item["required"]), catalog.REQUIRED)
        self.assertEqual(set(item["properties"]), catalog.REQUIRED | catalog.OPTIONAL)
        self.assertFalse(item["additionalProperties"])
        self.assertEqual(item["properties"]["category"]["enum"], ["Controls", "Displays"])
        self.assertEqual(item["properties"]["status"]["enum"], list(catalog.STATUS))
        self.assertEqual(item["dependentRequired"], {"media_url": ["media_note"]})
        self.assertEqual(item["properties"]["spotlight"]["type"], "boolean")
        self.assertIn("future dates", schema["$comment"])
        self.assertIn("order", schema["$comment"])

    def test_outputs_are_deterministic_and_schema_svg_summary_are_consistent(self):
        self.validate()
        first = catalog.outputs(self.projects, self.config)
        self.assertEqual(first, catalog.outputs(copy.deepcopy(self.projects), copy.deepcopy(self.config)))
        self.assertEqual(json.loads(first["data/schema.json"]), catalog.project_schema(self.config))
        summary = json.loads(first["data/summary.json"])
        self.assertEqual(summary["projects"], 6)
        self.assertEqual(summary["independently_tested_setups"], 0)
        svg_names = [name for name in first if name.endswith(".svg")]
        self.assertEqual(len(svg_names), 6)
        for name in svg_names:
            tree = ET.fromstring(first[name])
            self.assertIn("not a screenshot or test result", "".join(tree.itertext()))

    def test_duplicate_json_keys_and_unsorted_records_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "duplicate.json"
            path.write_text('{"id":"one","id":"two"}', encoding="utf-8")
            with self.assertRaises(catalog.CatalogError):
                catalog.read(path)
        self.projects[0], self.projects[1] = self.projects[1], self.projects[0]
        with self.assertRaises(catalog.CatalogError):
            self.validate()


if __name__ == "__main__":
    unittest.main()
