# Integration Note: yaojingang/geo-citation-lab

Repository: https://github.com/yaojingang/geo-citation-lab  
Reviewed on: 2026-05-24  
Decision: track as core GEO measurement resource

## Why this repository should be included

`geo-citation-lab` is stronger than most public GEO tool repositories because it releases an integrated package of experimental prompts, data, analysis scripts, reports, and a curated GEO/AEO/AI Search paper collection. It directly targets a key gap in early GEO work: counting citation selection is not enough; we need to understand citation absorption, namely whether cited pages are actually used by the generated answer.

The repository README reports:

- 602 experimental prompts.
- 432 / 60 / 60 / 50 prompts across four experiment layers.
- 3 platforms: ChatGPT, Google AI Overview / Gemini, and Perplexity.
- 21,143 valid search-layer citation rows.
- 23,745 citation-level feature records.
- 72 extracted features.
- 18,151 successfully fetched cited pages.
- 76.44 percent cited-page fetch success rate.
- 41 collected PDFs across seven GEO/AEO/AI Search themes.

## What to learn from it

### 1. Treat GEO as a multi-stage measurement pipeline

The repository organizes GEO into three stages:

1. Search triggering: whether a prompt causes an AI system to search.
2. Citation source selection: which sources are surfaced and cited.
3. Citation absorption: whether the cited source contributes content, evidence, or structure to the final answer.

This is useful for our hub because many GEO works still collapse all three stages into a single visibility score.

### 2. Separate citation width from citation depth

The quick report highlights that a platform can cite more sources without using each source deeply. This motivates separating:

- number of cited sources,
- citation position,
- reference count,
- paragraph coverage,
- text overlap,
- embedding similarity,
- LLM relevance and quality scores,
- final influence score or absorption score.

This can improve our own taxonomy under citation fidelity, attribution fidelity, and source influence.

### 3. Use feature-level source analysis

The repository extracts 72 citation-level features. Important feature groups include:

- content length and structure: word count, heading count, paragraph count, list density, table count, image count;
- extractable evidence blocks: numbers, definitions, comparisons, how-to content, code;
- semantic alignment: title-question match, embedding similarity, LLM relevance score;
- answer-side outcome features: reference count, first position ratio, paragraph coverage ratio, TF-IDF and n-gram overlap, influence score.

This is a concrete template for designing future GEO source-quality and citation-absorption benchmarks.

### 4. Improve report packaging

The repository provides multiple reading layers:

- quick report for non-technical readers;
- full Markdown report for GitHub reading;
- HTML report for browsing;
- PDF report for sharing;
- raw CSV data and pipeline scripts for reproduction;
- paper collection organized by topic.

Our repository should copy this packaging idea: each major update should include a quick brief, full analysis note, structured data table, and integration recommendation.

## Differences from our repository

| Dimension | geo-citation-lab | GEO Research Hub |
| --- | --- | --- |
| Primary role | empirical data/report repository | curated research intelligence hub |
| Main asset | citation-level measurement data and reports | structured metadata, taxonomy, literature review, benchmark map, maintenance workflow |
| Scope | citation selection and absorption plus paper collection | full GEO ecosystem: papers, benchmarks, repositories, platform rules, industry signals, research agenda |
| Best use | source influence and citation absorption evidence | long-term GEO field mapping and strategy synthesis |

The two repositories are complementary. We should not duplicate its raw data unless licensing and reuse terms are clarified. Instead, we should link to it, summarize its contribution, and extract reusable methodology into our taxonomy and benchmark notes.

## Recommended integration actions

- Add `yaojingang/geo-citation-lab` to `data/github_repos.csv` as `research data + benchmark + paper collection`.
- Add `GEO Citation Lab` to `data/benchmarks.csv` as a public measurement benchmark.
- Reference it in `docs/benchmarks.md` under citation absorption and source influence.
- Reference it in `docs/literature-review.md` when discussing the shift from citation selection to citation absorption.
- Add its report packaging pattern to `docs/maintenance-playbook.md` as a recommended update template.
- Re-check license or author permission before mirroring raw CSVs, PDFs, or reports.

## Quality judgement

Quality level: high for a public GEO measurement repository.

Reasons:

- It includes non-trivial released data, not just claims.
- It includes analysis scripts and reports.
- It separates search trigger, source selection, and citation absorption.
- It offers practical features that can be reused for future metric design.
- It has a structured paper collection useful for discovery.

Main caveat:

- No LICENSE file was found during inspection. The hub should link and describe it, but should not copy raw data or PDFs into our repository unless reuse terms are clarified.
