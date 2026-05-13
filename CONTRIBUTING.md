# Contributing

欢迎添加新论文、代码仓库、平台文档和实验结果。请优先提交可验证资料，而不是单纯观点。

## Add a Paper

1. Add one row to `data/papers.csv`.
2. Use the primary source URL, preferably arXiv, OpenReview, ACM, ACL Anthology, NeurIPS, ICLR, KDD, or official project page.
3. Fill `overlap_group`, `novelty_score`, `value_score`, and `risk_notes`.
4. If it changes current conclusions, update `docs/literature-review.md` or `research/synthesis-2026.md`.
5. Run:

```bash
python tools/check_metadata.py
```

## Add a GitHub Repo

1. Add one row to `data/github_repos.csv`.
2. Distinguish official research code from community forks and vendor demos.
3. If possible, record license and whether code/data are actually usable.

## Add an Industry Source

1. Add one row to `data/industry_sources.csv`.
2. Mark official platform docs as `high`, strong news/reporting as `medium`, vendor marketing as `low`.
3. Do not promote vendor claims into research conclusions without independent evidence.

