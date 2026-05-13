# GitHub Project Review

Last reviewed: 2026-05-13.

This page records repository-level triage. It is intentionally separate from `data/github_repos.csv`: the CSV is the machine-readable index, while this page captures judgement, overlap, and what each repo contributed to the hub.

## Reviewed Repositories

| Repository | Verdict | Why it matters | What we harvested |
| --- | --- | --- | --- |
| [onvoyage-ai/gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) | Watch | Practical GTM/GEO skill chain from brand research to prompt targets, content planning, writing, auditing, and frontend resource pages. | Added as an operations/workflow repo; reinforces `O10 Tooling / Operations`. |
| [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | Track | Broad technical GEO audit/fix tool: robots, AI crawlers, llms.txt, schema, meta, AI discovery endpoints, prompt-injection detection, negative signals, citability, MCP and CI. | Added as a tracked tool; useful for engineering audit checklist. |
| [mverab/eGEOagents](https://github.com/mverab/eGEOagents) | Watch | Claude Code style agent workflow for GEO audit, rewrite, schema generation, competitive analysis, and report output. | Added as workflow implementation; its arXiv dependency led us to E-GEO. |
| [AI2HU/gego](https://github.com/AI2HU/gego) | Track | Multi-LLM prompt scheduler and analytics tool for brand/keyword mentions across models. | Added as monitoring-layer project; useful for share-of-voice tracking. |
| [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) | Watch | Bilingual discovery list with papers, tools, AI search engines, strategy notes, analytics, case studies, and checklists. | Surfaced E-GEO plus BRIGHT, LLM4IR survey, Search-o1, and ChatGPT reranking background. |
| [psbagga17/E-GEO](https://github.com/psbagga17/E-GEO) | Track | Research code for e-commerce GEO benchmark and prompt/meta-optimization. | Added E-GEO as a core vertical benchmark and linked code. |
| [geo-team-red/geo-optimizer](https://github.com/geo-team-red/geo-optimizer) | Watch | Go framework for pluggable GEO strategies: structure, schema, answer-first, authority, FAQ, scoring, and LLM abstraction. | Added as framework/tooling repo; not treated as benchmark evidence. |

## Added From This Pass

Core / direct GEO:

- [E-GEO: A Testbed for Generative Engine Optimization in E-Commerce](https://arxiv.org/abs/2511.20867)
- [psbagga17/E-GEO](https://github.com/psbagga17/E-GEO)

Background / retrieval architecture:

- [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://arxiv.org/abs/2407.12883)
- [Large Language Models for Information Retrieval: A Survey](https://arxiv.org/abs/2308.07107)
- [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://arxiv.org/abs/2501.05366)
- [Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents](https://arxiv.org/abs/2304.09542)

Tooling / operations:

- [AI2HU/gego](https://github.com/AI2HU/gego)
- [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill)
- [onvoyage-ai/gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills)
- [mverab/eGEOagents](https://github.com/mverab/eGEOagents)
- [geo-team-red/geo-optimizer](https://github.com/geo-team-red/geo-optimizer)
- [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo)

## Judgement Notes

- `E-GEO` is a real missing item and should be read with AutoGEO, C-SEO Bench, and platform commerce docs.
- `Gego` fills a monitoring gap, but it measures mentions/keywords rather than citation faithfulness or source influence.
- `GEO Optimizer Skill` is broad and engineering-useful, but score weights should be treated as product methodology, not peer-reviewed evidence.
- `GTM Engineer Skills` and `eGEOagents` are useful workflow implementations; they should feed an evaluation harness rather than replace it.
- `awesome-geo` is valuable for discovery, but its industry statistics and case studies need primary-source verification before entering conclusions.

