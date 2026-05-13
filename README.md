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
- **AgentGEO / AgenticGEO / MAGEO**: 2026 arXiv/ACL Findings，进入诊断式、智能体式、自进化和可复用策略学习 GEO。
- **Adversarial SEO for LLMs / Ranking Manipulation / GASLITE**: 说明 GEO 不能只看增长，也必须看操纵风险和防御。

## 公开论文

| Paper | Year / Venue | Main contribution | Code / Data | Tier |
| --- | --- | --- | --- | --- |
| [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) | 2024 / KDD | GEO 原始定义、GEO-Bench、黑箱可见度优化 | [GEO-optim/GEO](https://github.com/GEO-optim/GEO), [GEO-Bench](https://huggingface.co/datasets/GEO-optim/geo-bench) | core |
| [C-SEO Bench: Does Conversational SEO Work?](https://arxiv.org/abs/2506.11097) | 2025 / NeurIPS D&B | 多任务、多领域、多采用者下的 C-SEO 评估，给出重要负结果 | [parameterlab/c-seo-bench](https://github.com/parameterlab/c-seo-bench) | core |
| [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://openreview.net/forum?id=K8EinVWtUB) | 2026 / ICLR | AutoGEO，自动抽取生成引擎偏好并训练/调用改写模型 | [cxcscmu/AutoGEO](https://github.com/cxcscmu/AutoGEO) | core |
| [CC-GSEO-Bench](https://arxiv.org/abs/2509.05607) | 2025 / arXiv | 从曝光推进到 Exposure、Faithful Credit、Causal Impact 的源影响评估 | [qychen2001/CC-GSEO-Bench](https://github.com/qychen2001/CC-GSEO-Bench) | core |
| [SAGEO Arena](https://arxiv.org/abs/2602.12187) | 2026 / arXiv | 检索、重排、生成全链路 SAGEO 评估环境 | not verified | core |
| [Diagnosing and Repairing Citation Failures in GEO](https://arxiv.org/abs/2603.09296) | 2026 / arXiv | 引用失败分类与 AgentGEO 诊断式修复 | not verified | core |
| [AgenticGEO](https://arxiv.org/abs/2603.20213) | 2026 / arXiv | MAP-Elites 策略库与 co-evolving critic 的自进化 GEO | [AIcling/agentic_geo](https://github.com/AIcling/agentic_geo) | core |
| [From Experience to Skill: Multi-Agent GEO via Reusable Strategy Learning](https://arxiv.org/abs/2604.19516) | 2026 / ACL Findings | MAGEO，可复用策略学习、Twin Branch Evaluation、DSV-CF、MSME-GEO-Bench | [Wu-beining/MAGEO](https://github.com/Wu-beining/MAGEO) | core |
| [E-GEO: A Testbed for GEO in E-Commerce](https://arxiv.org/abs/2511.20867) | 2025 / arXiv | 电商垂直 GEO benchmark，覆盖产品查询和改写启发式 | [psbagga17/E-GEO](https://github.com/psbagga17/E-GEO) | core |
| [Adversarial SEO for LLMs](https://arxiv.org/abs/2406.18382) | 2024 / arXiv | LLM 搜索偏好操纵攻击与博弈风险 | not verified | core-safety |
| [Ranking Manipulation for Conversational Search Engines](https://arxiv.org/abs/2406.03589) | 2024 / EMNLP | 对话搜索排名操纵与 prompt-injection 风险 | not verified | core-safety |
| [GASLITEing the Retrieval](https://arxiv.org/abs/2412.20953) | 2025 / ACM CCS | dense retrieval SEO 攻击面与低比例投毒风险 | not verified | core-safety |
| [GEM-Bench](https://arxiv.org/abs/2509.14221) | 2025 / arXiv | 生成式引擎广告注入和营销评估基准 | [Generative-Engine-Marketing/GEM-Bench](https://github.com/Generative-Engine-Marketing/GEM-Bench) | adjacent |

## 公开 GitHub 项目

| Repository | Category | Related paper / context | What it contains | Priority |
| --- | --- | --- | --- | --- |
| [GEO-optim/GEO](https://github.com/GEO-optim/GEO) | research code + benchmark | GEO / KDD 2024 | GEO-Bench、原始优化函数、leaderboard 链接 | track |
| [cxcscmu/AutoGEO](https://github.com/cxcscmu/AutoGEO) | research code + models | AutoGEO / ICLR 2026 | 偏好规则抽取、AutoGEO_API、AutoGEO_Mini、数据和 checkpoint | track |
| [parameterlab/c-seo-bench](https://github.com/parameterlab/c-seo-bench) | benchmark code + data | C-SEO Bench / NeurIPS 2025 | C-SEO 方法、benchmark runner、citation ranking evaluation | track |
| [qychen2001/CC-GSEO-Bench](https://github.com/qychen2001/CC-GSEO-Bench) | benchmark code | CC-GSEO-Bench | 文档优化、答案生成、LLM judge、MIL/ICov/IStab 指标 | track |
| [AIcling/agentic_geo](https://github.com/AIcling/agentic_geo) | research code | AgenticGEO | MAP-Elites 策略库、critic、multi-turn rewriting evaluation | track |
| [Wu-beining/MAGEO](https://github.com/Wu-beining/MAGEO) | research code | MAGEO / ACL 2026 Findings | 多智能体规划/编辑/评估、层级记忆、DSV-CF、fidelity gate | track |
| [psbagga17/E-GEO](https://github.com/psbagga17/E-GEO) | research code + dataset | E-GEO / e-commerce GEO | 电商数据、15 个初始 prompt、meta-optimization、实验和分析脚本 | track |
| [AI2HU/gego](https://github.com/AI2HU/gego) | monitoring / analytics | multi-LLM visibility tracking | 定时跑 prompts，跨 OpenAI/Anthropic/Gemini/Perplexity/Ollama 抽取品牌和关键词 mentions | track |
| [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | CLI + MCP audit tool | technical GEO readiness | robots/llms/schema/meta/AI crawler/负面信号/prompt injection/citability 审计和修复生成 | track |
| [onvoyage-ai/gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) | agent skills | GTM + GEO workflow | 品牌、关键词、Reddit、GEO prompt、内容规划、SEO/GEO 写作、审计和页面落地技能链 | watch |
| [mverab/eGEOagents](https://github.com/mverab/eGEOagents) | agent skills | E-GEO workflow | Claude Code GEO agents/commands，审计、改写、schema、竞争分析和报告输出 | watch |
| [geo-team-red/geo-optimizer](https://github.com/geo-team-red/geo-optimizer) | Go framework | pluggable GEO optimization | structure/schema/answer-first/authority/FAQ 策略、LLM 抽象、内容评分 | watch |
| [Generative-Engine-Marketing/GEM-Bench](https://github.com/Generative-Engine-Marketing/GEM-Bench) | benchmark code | GEM-Bench | ad-injected response benchmark、多智能体广告注入 baseline | watch |
| [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) | awesome list | community resource | 论文、工具、平台文档、行业资源索引 | watch |
| [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) | awesome list | community resource | 中英双语 GEO 资源索引，补出了 E-GEO 和若干检索/RAG 背景资料 | watch |
| [izak-fisher/generative-engine-optimization-tools](https://github.com/izak-fisher/generative-engine-optimization-tools) | tool list | community resource | GEO/AEO/AI visibility 工具和厂商目录 | watch |

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
│   ├── github-project-review.md# GitHub 项目调研记录
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
6. [docs/github-project-review.md](docs/github-project-review.md)
7. [docs/research-agenda.md](docs/research-agenda.md)

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
