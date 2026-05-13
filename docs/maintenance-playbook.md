# Maintenance Playbook

## Update Cadence

建议频率：

- 每 2 周：arXiv / OpenReview / GitHub topic 快速扫一遍。
- 每月：更新 `data/*.csv` 和 `research/synthesis-2026.md`。
- 每季度：重写一次 `docs/research-agenda.md`，把已经过时的假设降级。

## Intake Workflow

1. Search using `data/search_queries.md`.
2. Prefer primary sources:
   - arXiv
   - OpenReview
   - ACM / ACL Anthology / NeurIPS / ICLR / KDD pages
   - official GitHub repos
   - official platform docs
3. Check whether it is a duplicate:
   - same arXiv id
   - same title
   - same official repo
   - mirror page only
4. Add to the right CSV:
   - paper / benchmark -> `data/papers.csv`
   - repo/tool -> `data/github_repos.csv`
   - official docs / news / market reports -> `data/industry_sources.csv`
5. Assign:
   - `relevance_tier`
   - `overlap_group`
   - `novelty_score`
   - `value_score`
   - `maintenance_priority`
6. Run:

```bash
python tools/check_metadata.py
```

7. If a core source changed conclusions, update:
   - `docs/literature-review.md`
   - `docs/benchmarks.md`
   - `research/synthesis-2026.md`

## Commit Convention

Use conventional-style commits:

```text
research: add AutoGEO and C-SEO benchmark notes
data: add new 2026 citation-failure paper
docs: update GEO benchmark comparison
tools: validate paper metadata
```

## Review Checklist

Before merging updates:

- Does the source have a primary URL?
- Is it core, adjacent, background, or low evidence?
- Is there code or data?
- Does it overlap with existing papers?
- What is the new claim?
- What would falsify the claim?
- Does it improve or harm retrieval, utility, citation, or trust?

