# GEO Taxonomy

GEO 不是单点技巧，而是一条从内容生产到生成答案呈现的管线。下面的分类用于给论文、工具和产品路线分层。

## 1. 名称归并

这些词经常描述同一个问题空间，但侧重点不同：

| Term | 重点 | 备注 |
| --- | --- | --- |
| GEO, Generative Engine Optimization | 在生成式答案中提升内容可见度、覆盖率、引用和归因 | 学术原点来自 KDD 2024 GEO 论文 |
| GSEO, Generative Search Engine Optimization | 偏搜索系统语境，强调 GSE / SAGE 管线 | 常用于基准和 RAG 搜索论文 |
| C-SEO, Conversational SEO | 面向 conversational search engine 的 citation ranking | NeurIPS 2025 C-SEO Bench 是关键负结果 |
| AEO, Answer Engine Optimization | 更偏营销/SEO行业话术，强调“成为答案” | 常与 GEO 混用，学术边界较弱 |
| LLMO / AI Search Optimization | 更宽泛，包含品牌、知识图谱、AI可读内容 | 适合产业地图，不适合直接当学术新概念 |

## 2. 生成式搜索管线

GEO 的可优化点可以分成七层：

1. **Content Layer**: 内容本身是否有独特信息、原始数据、清晰结构、引用和可抽取片段。
2. **Technical Access Layer**: 爬虫可访问性、HTTP 状态、robots/preview 控制、结构化数据、页面渲染。
3. **Retrieval Layer**: BM25、dense retrieval、hybrid retrieval、query fan-out、候选集召回。
4. **Reranking Layer**: 上下文位置、域名/来源权重、相关性、可信度和多样性。
5. **Generation Layer**: LLM 如何选择、融合、压缩、重写来源。
6. **Citation / Attribution Layer**: 是否引用、引用谁、引用位置、是否忠实归因。
7. **Outcome Layer**: 点击、转化、品牌记忆、用户信任、广告或 agentic commerce 行为。

## 3. 研究主题簇

| Cluster | 核心问题 | 代表资料 |
| --- | --- | --- |
| O1 Foundation / Visibility | 如何定义和提升生成答案可见度 | GEO, AutoGEO, AgenticGEO |
| O2 Benchmark / Evaluation | 如何衡量 GEO 是否真的有效 | GEO-Bench, C-SEO Bench, CC-GSEO-Bench, SAGEO Arena |
| O3 Citation / Attribution | “被引用”和“真正影响答案”是否一致 | Diagnosing Citation Failures, CC-GSEO-Bench |
| O4 Strategy / Empirical Sourcing | AI Search 与 Google/SEO 在来源偏好上有何差异 | How to Dominate AI Search |
| O5 Agentic Platforms | 从答案引用走向意图路由、专用 agent 和交易 | Beyond Retrieval, platform commerce docs |
| O6 Monetization / GEM | 广告如何嵌入生成答案 | GEM-Bench |
| O7 Security / Adversarial | GEO 如何变成操纵或投毒 | Adversarial SEO, Ranking Manipulation, GASLITE |
| O8 RAG Evidence Quality | LLM 选择哪些证据，如何处理冲突 | ConflictingQA, ConflictBank |
| O9 Search-LLM Architecture | LLM 与搜索系统怎样融合 | When Search Engine Services meet LLMs |

## 4. 判断一篇 GEO 论文是否真有价值

优先级最高的论文通常满足以下条件：

- 有清晰系统模型，而不是只给 prompt 技巧。
- 覆盖检索、重排、生成、引用中的多个阶段，或明确说明只研究某一阶段。
- 有可复现代码、数据、评价脚本。
- 同时报告可见度和用户/搜索效用，避免只优化内容曝光。
- 讨论多参与者竞争或对抗风险。
- 给出负结果、失败模式或边界条件。

低优先级信号：

- 只把 SEO 常识换成 GEO 名词。
- 只用少量 anecdotal prompt 测试。
- 不区分 citation、mention、word overlap、traffic、conversion。
- 没有对照传统 SEO / retrieval rank / context position。
- 只做营销式“90天计划”，但无实验或平台官方依据。

