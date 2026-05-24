# GEO Research Hub Daily Brief — 2026-05-24

## Executive summary

今天补跑发现，GEO 相关研究正在从早期的可见度优化，快速扩展到 citation absorption、AI Overview source fidelity、source selection bias、traffic substitution、AI search information market impact 和平台反操纵政策。最值得后续合并到主表的是 citation absorption 框架、Pinterest 生产级视觉 GEO 框架、Google Search/Gemini/AI Overview 11,500 查询对比研究，以及 Google AIO 55,393 查询纵向测量研究。

## Items recommended for main integration

### P-candidate-1: From Citation Selection to Citation Absorption

- URL: https://arxiv.org/abs/2604.25707
- Why it matters: It separates citation selection from citation absorption, making GEO evaluation more faithful to whether a cited page actually shapes the generated answer.
- Suggested destination: data/papers.csv, docs/literature-review.md, docs/benchmarks.md
- Suggested tier: core

### P-candidate-2: Pinterest VLM and Agent GEO Framework

- URL: https://arxiv.org/abs/2602.02961
- Why it matters: It is a production-scale multimodal GEO system for visual content platforms, with VLM search-intent prediction, trend-mining agents, collection-page generation, multimodal embeddings and authority-aware interlinking.
- Suggested destination: data/papers.csv, research/synthesis-2026.md
- Suggested tier: core or strong adjacent

### P-candidate-3: How Generative AI Disrupts Search

- URL: https://arxiv.org/abs/2604.27790
- Why it matters: It compares Google Search, Google AI Overviews and Gemini on 11,500 user queries and shows that generative search source selection differs sharply from traditional search.
- Suggested destination: data/papers.csv, data/benchmarks.csv, docs/benchmarks.md
- Suggested tier: core-background

### P-candidate-4: Answer Bubbles

- URL: https://arxiv.org/abs/2603.16138
- Why it matters: It examines 11,000 real queries across vanilla GPT, Search GPT, Google AI Overviews and traditional Google Search, focusing on source diversity, linguistic characterization and source-summary fidelity.
- Suggested destination: data/papers.csv, docs/literature-review.md
- Suggested tier: core-background

### P-candidate-5: Measuring Google AI Overviews

- URL: https://arxiv.org/abs/2605.14021
- Why it matters: It measures 55,393 trending queries across 19 topics and decomposes AI Overview responses into 98,020 atomic claims, making it useful for claim fidelity and source quality discussions.
- Suggested destination: data/papers.csv, docs/benchmarks.md, data/industry_sources.csv
- Suggested tier: core-background

### P-candidate-6: AI Search and Reddit Ecosystem Impact

- URL: https://arxiv.org/abs/2605.16428
- Why it matters: It studies Google AI Overviews and Reddit using a difference-in-differences design, showing that AI search effects depend heavily on content type and interface design.
- Suggested destination: data/papers.csv
- Suggested tier: adjacent

### P-candidate-7: AI Search Summaries and Wikipedia Traffic

- URL: https://arxiv.org/abs/2602.18455
- Why it matters: It estimates a roughly 15 percent traffic reduction for English Wikipedia articles exposed to Google AI Overviews, useful for GEO value modeling.
- Suggested destination: data/papers.csv
- Suggested tier: adjacent

### P-candidate-8: The Rise of AI Search

- URL: https://arxiv.org/abs/2602.13415
- Why it matters: It runs 24,000 search queries in 243 countries and frames AI search as a global information market and exposure problem.
- Suggested destination: data/papers.csv
- Suggested tier: adjacent

## Rejected or deferred GitHub repos

### getauracite/geo-benchmarks

- URL: https://github.com/getauracite/geo-benchmarks
- Decision: defer
- Reason: The repo currently describes a future Q3 2026 benchmark. It does not yet release raw data, reports, scripts or reproducible methodology files.

### Vaishnavii-01/geo-optimizer

- URL: https://github.com/Vaishnavii-01/geo-optimizer
- Decision: reject for now
- Reason: It is a frontend GEO audit and strategy app with common feature claims. No distinctive benchmark or rigorous evaluation was identified.

### aritheboss18785/Prompty

- URL: https://github.com/aritheboss18785/Prompty
- Decision: reject for now
- Reason: It is a small Streamlit visibility dashboard and overlaps with stronger monitoring tools already tracked in the hub.

## Repository files created today

- logs/2026-05-24.md
- data/daily_updates/2026-05-24_curated_candidates.csv
- reports/2026-05-24-daily-brief.md

## Next integration recommendation

The next daily run should merge the strongest stable entries into the canonical CSV tables after verifying dataset URLs and avoiding duplicate overlap groups. Recommended first batch: citation absorption, Pinterest GEO, Google Search/Gemini/AIO benchmark, and Google AIO measurement.
