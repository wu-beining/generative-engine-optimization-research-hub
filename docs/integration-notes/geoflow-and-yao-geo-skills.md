# Integration Note: yaojingang/GEOFlow and yaojingang/yao-geo-skills

Reviewed on: 2026-05-24  
Decision: track both as high-value GEO engineering and operations resources

## Repositories

- GEOFlow: https://github.com/yaojingang/GEOFlow
- Yao GEO Skills: https://github.com/yaojingang/yao-geo-skills

## Summary judgement

These two repositories should be treated as operational engineering assets rather than academic evidence or benchmark resources.

- `GEOFlow` is a deployable GEO content engineering and multi-site distribution system.
- `yao-geo-skills` is a structured skill library for repeatable GEO strategy, page audit, content production, knowledge assets, measurement and research workflows.

Together, they represent a practical GEO service stack:

1. Build and manage trusted knowledge assets.
2. Convert them into structured prompts, titles, pages and content tasks.
3. Generate, review and publish content.
4. Distribute content to local sites, WordPress REST channels or GEOFlow Agent target sites.
5. Produce sitemaps, TXT maps, `llms.txt`, Schema and AI-crawler-friendly outputs.
6. Monitor content operation, site distribution, access logs and AI crawler trends.
7. Reuse skills for diagnosis, execution roadmaps, page audits, page blueprints, content refinement, brand graphs, knowledge-base building and effect monitoring.

## GEOFlow assessment

### What it provides

GEOFlow describes itself as an open-source intelligent content engineering and multi-site distribution system for GEO. The README reports support for:

- OpenAI-compatible APIs and Gemini native APIs.
- Knowledge-base upload, structured chunking, optional LLM semantic planning, embeddings and RAG recall.
- Title libraries, keyword libraries, image libraries, author libraries, knowledge bases and prompt libraries.
- Task automation, draft pools, review switches, publishing rhythm, queue execution and failure retry.
- Draft, review, publish and recycle-bin workflows.
- GEOFlow Agent and WordPress REST channels.
- Target-site packages with homepage, detail pages, static assets, sitemap, `llms.txt`, TXT maps and Schema.
- Analytics for system overview, content operations, distribution, access logs, top content, AI crawler identification and trends.
- Docker Compose deployment with PostgreSQL plus pgvector, Redis, queue workers, scheduler, Reverb and production Nginx/PHP-FPM.
- Apache-2.0 license.

### Why it matters for our hub

Most GEO repositories are either small dashboards or prompt collections. GEOFlow is closer to a full content operations system. It can help us describe the engineering layer of GEO:

- content asset management,
- knowledge-base first workflow,
- RAG assisted content generation,
- editorial review and release governance,
- multi-site distribution,
- AI-crawler and source-map outputs,
- content analytics and monitoring.

This is useful for the business/SOP side of our research hub, especially for Zero Click Tech style service workflows.

### Caveats

- It is not a benchmark and should not be used as evidence that a GEO method works.
- Its value depends on the quality, truthfulness and maintainability of the knowledge base.
- It can be misused for low-quality content flooding, so our notes should frame it as a trusted content operations system rather than an internet pollution tool.

## Yao GEO Skills assessment

### What it provides

The README says the repository contains 17 GEO skills across seven categories:

- geo-operations,
- geo-strategy,
- geo-page-technical,
- geo-content-production,
- geo-knowledge-assets,
- geo-measurement,
- geo-research.

Each formal skill is expected to include:

- `SKILL.md`,
- `manifest.json`,
- `templates/brief-template.md`,
- `evals/trigger_cases.json`,
- `evals/expected_artifacts.json`,
- `docs/skills/<skill-id>.md`.

The repository also includes a validation script, `scripts/validate_repository.py`, which is useful as a structural quality-control idea.

### Why it matters for our hub

The repository is valuable because it treats GEO workflows as reusable, testable operational assets instead of one-off prompts. It offers templates and examples for:

- GEO panorama audit,
- 30/60/90 execution roadmap,
- page technical audit,
- GEO page blueprint,
- title optimization,
- comparison content generation,
- ranking article generation,
- explainer article generation,
- old content refinement,
- brand graph construction,
- knowledge-base building,
- GEO attribution tracking,
- AI answer monitoring,
- intent mining,
- GEOFlow operation and template editing.

This is very relevant to our own GEO service SOP, because it gives a modular way to package repeatable work.

### Caveats

- It is a workflow and delivery-template library, not empirical proof.
- Some examples are synthetic or demo-oriented; use them as structure references, not performance evidence.
- Before copying templates, check the MIT license notice and preserve attribution where needed.

## How to integrate into our repository

### Already integrated

- Added `yaojingang/GEOFlow` to `data/github_repos.csv`.
- Added `yaojingang/yao-geo-skills` to `data/github_repos.csv`.

### Recommended next updates

1. Add an engineering section to `docs/taxonomy.md`:
   - GEO research methods,
   - GEO measurement benchmarks,
   - GEO engineering systems,
   - GEO skill libraries and SOP assets,
   - GEO monitoring and attribution tools.

2. Add a service-workflow section to `docs/research-agenda.md`:
   - knowledge-base first GEO,
   - evidence-card construction,
   - page blueprinting,
   - AI-crawler-friendly publishing,
   - multi-site distribution governance,
   - longitudinal monitoring.

3. Add a practical resource note to `docs/github-project-review.md`:
   - GEOFlow as content operations and distribution system,
   - yao-geo-skills as repeatable workflow and deliverable library,
   - geo-citation-lab as measurement data and citation absorption evidence.

4. Update the maintenance playbook:
   - future repo reviews should distinguish `research evidence`, `benchmark`, `engineering system`, `workflow template`, `monitoring tool`, `community list`, and `marketing-only content`.

## Proposed hub positioning

These two repositories should not be mixed with core academic benchmark claims. They should be grouped under:

> Engineering and Operations Resources for GEO

Recommended wording:

`GEOFlow` and `yao-geo-skills` show how GEO ideas can be operationalized into a deployable content engineering system and a reusable skill library. They are especially useful for SOP design, service delivery, content-asset governance and engineering practice, while academic claims about effectiveness should still be grounded in peer-reviewed papers and reproducible benchmarks.
