# GEO Research Hub Daily Brief — 2026-06-14

## Executive summary

本次即时补跑主要发现：GEO 领域最近的重点不在普通工具仓库，而在安全评测、ranking manipulation detectability、feature-level optimization、AI Overview source fidelity 和平台法律责任。最值得正式纳入主表的是 `GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization`，因为它把多类 ranking manipulation 方法放到统一协议下比较，并同时报告 effectiveness 与 stealth。

## Canonical update

### GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization

- URL: https://arxiv.org/abs/2605.29107
- Date: 2026-05-27
- Added as: `P025` in `data/papers.csv`; `B010` in `data/benchmarks.csv`
- Why it matters: Existing ranking-manipulation and GEO attack/optimization papers often use different datasets, rankers and metrics. This benchmark standardizes black-box prompt-based attacks, white-box gradient-based attacks and white-hat C-SEO strategies under one protocol.
- Evaluated methods: TAP, Zero-Shot, STS, RAF, StealthRank and ten white-hat C-SEO strategies.
- Metrics: NRG, Success@alpha, Promote@alpha, keyword violation rate, perplexity ratio.
- Main value for the hub: It complements the existing safety line around Adversarial SEO for LLMs, Ranking Manipulation for Conversational Search Engines, GASLITE and manipulation/detectability work.
- Risk: dual-use. Keep it as defensive benchmark and governance evidence, not an operational attack guide.

## Watchlist additions

### FeatGEO / Think Before Writing

This work proposes feature-level, multi-objective optimization over structural, content and linguistic properties. It is worth monitoring because it moves beyond token-level rewriting and aligns with GEO Citation Lab style feature analysis. It should be promoted only after assets and overlap are verified.

### Structural Feature Engineering for GEO

This work argues that citation behavior can be shaped at macro, meso and micro content-structure levels. It is useful for taxonomy and page-structure discussions, but overlaps with FeatGEO and citation-level feature work.

### GEO16 citation behavior audit

This observational framework is useful for B2B SaaS page-audit dimensions, but it is narrower than GEO Citation Lab and should remain watch-level for now.

### Caption Injection

Caption Injection is a multimodal G-SEO candidate. It is relevant to future multimodal GEO taxonomy, but should be compared against Pinterest VLM/GEO and multimodal ranker work before being treated as a core method.

### Google AI Overviews liability ruling

A German court ruling reported by Reuters/Wired is important for AI Overview accountability and source-fidelity risk. It should be tracked as an industry/legal signal after primary legal materials or stable legal summaries are checked.

## GitHub screening result

The GitHub search mostly surfaced known repositories already tracked in the hub, small overlapping tools, or duplicate/copy-like repositories. Two examples were rejected:

- `QianfengWen/SafeGEO`: README inspection showed it mirrors this hub's README content.
- `aldegad/awesome-geo`: README inspection also showed duplicated hub README content.

## Files changed

- `data/papers.csv`
- `data/benchmarks.csv`
- `logs/2026-06-14.md`
- `data/daily_updates/2026-06-14_curated_candidates.csv`
- `reports/2026-06-14-daily-brief.md`

## Next recommended action

In the next scheduled run, verify whether `GEO-Bench: Benchmarking Ranking Manipulation` releases code, datasets or a leaderboard. If it does, update `code_url`, `dataset_url`, and `status` in both canonical CSV tables. Also verify whether FeatGEO and Structural Feature Engineering have public code or reproducible assets before moving them from watch to track.
