# Contribute one useful, well-supported idea

[Collection](README.md) · [Research method](docs/methodology.md) · [Testing protocol](docs/testing.md)

Start with a concrete outcome and the project's own evidence. A clear correction is as valuable as a new entry. Commercial projects can qualify; public source is not required. A license is required before calling a project open source.

1. Search the existing catalog by project name, device and outcome.
2. Confirm the project fits this repository's scope in the research method.
3. Inspect a maintainer's README, official documentation, release page or original research/demo. Search snippets and reposts are leads, not sufficient evidence alone.
4. Add one record to `data/projects.json`. Use the fields in [the schema](data/schema.json), a stable slug, concise original English and Chinese descriptions, and an honest review date.
5. Write the decisive prerequisites and limits. State the exact device/OS where known, host or bridge, additional hardware, account/service dependencies and relevant paid software. Record an unknown instead of inferring compatibility.
6. Add brief steps that lead into upstream instructions. Do not duplicate entire manuals. Use `source_url` only for actual source code and `media_note` for every linked demo's provenance.
7. Sort by category order in `data/config.json`, then project name. Run `make build` and `make verify` with Python 3.10 or later. Commit generated changes with the data.

The status describes the route available upstream, not a successful test here. Use `released` for a documented installer, runnable script, downloadable configuration or ready product; `source-build` when the route requires a source/DIY build; `research` for experimental demonstrations; `archived` for legacy or explicitly archived work. Explain paid or DIY hardware separately. Check [the testing record](docs/testing.md) before labeling anything tested.

The six illustrated spotlights are editorial selections in `data/config.json`. A new entry does not automatically become a spotlight. Keep their labels short and their image meaning consistent with the evidence.

## Images and attribution

Link an upstream demonstration when useful. Do not copy arbitrary screenshots or videos into this repository. To add an image, document its origin, license or permission, credit and any changes in [visual credits](assets/README.md). Conceptual illustrations must be labeled; they are not proof that a setup works. Keep the text useful without images.

## Corrections and test reports

Use the issue templates to report a broken URL, changed requirement, unsupported claim or firsthand result. Include the exact project, model, OS/firmware, project version, steps, expected/actual result and a public evidence link if possible. Never include account tokens or private recordings. A maintainer must reconcile a report into the data before it becomes part of the catalog.

Please do not bulk-submit generated lists, duplicate platform variants, remove limitations to make an entry sound better, or add tracking/referral links. Keep disagreements about claims and evidence, and treat contributors respectfully.

Contributed original prose and diagrams are dedicated under [CC0](LICENSE); scripts and tests use [MIT](LICENSE-CODE). Identify any third-party material separately.
