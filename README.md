# GEO Research Hub

面向 Generative Engine Optimization (GEO) / Generative Search Optimization / Conversational SEO / Answer Engine Optimization 的长期维护型研究仓库。

本仓库不是普通 awesome-list。目标是把 2024-2026 年以来的论文、基准、开源实现、平台规则和产业信号整理成一个可迭代的知识底座，服务三个问题：

1. GEO 领域真正可靠的学术与工程进展是什么？
2. 哪些工作只是改名、包装或局部重复？
3. 如果要在 GEO 领域先行，下一步应该做什么研究、产品和实验？

## 当前结论

GEO 的核心问题已经从“怎么让生成答案多引用我”升级为“在检索、重排、生成、引用、归因、商业转化和安全对抗之间做全链路优化”。只优化生成阶段的内容改写，会遇到检索排名下降、引用不忠实、竞争者同时采用后收益收敛等问题。

最值得跟踪的论文线索：

- **GEO: Generative Engine Optimization**: KDD 2024 原始定义与 GEO-Bench。
- **C-SEO Bench**: NeurIPS Datasets & Benchmarks 2025，强提醒：很多 C-SEO/GEO 改写方法在多域、多参与者场景下并不稳。
- **AutoGEO**: ICLR 2026，自动学习生成引擎偏好并改写内容，同时引入可见度与搜索效用权衡。
- **CC-GSEO-Bench**: 2025 arXiv，开始把“是否露出”推进到 Exposure、Faithful Credit、Causal Impact。
- **SAGEO Arena**: 2026 arXiv，强调真实搜索增强管线中的检索、重排、生成三阶段评估。
- **AgentGEO / AgenticGEO**: 2026 arXiv，进入诊断式、智能体式和自进化 GEO。
- **Adversarial SEO for LLMs / Ranking Manipulation / GASLITE**: 说明 GEO 不能只看增长，也必须看操纵风险和防御。

## 仓库结构

```text
geo-research-hub/
├── data/
│   ├── papers.csv              # 论文和技术报告主表
│   ├── github_repos.csv        # GitHub 项目和工具生态
│   ├── industry_sources.csv    # 官方文档、平台规则、产业资料
│   └── search_queries.md       # 后续更新建议检索式
├── docs/
│   ├── taxonomy.md             # GEO 领域分类图谱
│   ├── literature-review.md    # 论文逐篇价值判断与重合分析
│   ├── benchmarks.md           # 基准和指标对比
│   ├── platform-notes.md       # Google / OpenAI 等平台可验证规则
│   ├── source-index.md         # 主要来源索引
│   ├── source-quality-rubric.md# 资料可信度评分规则
│   ├── research-agenda.md      # 研究与产品路线图
│   └── maintenance-playbook.md # 长期维护流程
├── research/
│   └── synthesis-2026.md       # 2026 版高级综述
├── references.bib              # 核心文献 BibTeX
└── tools/
    └── check_metadata.py       # 本地 CSV 元数据检查
```

## 快速使用

阅读顺序建议：

1. [research/synthesis-2026.md](research/synthesis-2026.md)
2. [docs/taxonomy.md](docs/taxonomy.md)
3. [docs/literature-review.md](docs/literature-review.md)
4. [docs/benchmarks.md](docs/benchmarks.md)
5. [docs/source-index.md](docs/source-index.md)
6. [docs/research-agenda.md](docs/research-agenda.md)

检查数据表：

```bash
python tools/check_metadata.py
```

## 维护原则

- 只把 **论文、官方文档、代码仓库、可复现实验、可验证产业报告** 放入主表。
- 营销文章可以进入 `industry_sources.csv`，但默认不作为核心结论依据。
- 每条资料都要标注 `relevance_tier`、`overlap_group`、`novelty_score`、`value_score` 和 `risk_notes`。
- 同名概念先归并再比较，例如 GEO / GSEO / C-SEO / AEO / LLMO 不直接视为新领域。
- 优先记录负结果和边界条件，因为它们最能避免后续做伪创新。
