# Research and Product Agenda

目标：在 GEO 领域先行，不做“把 SEO 常识换名词”的二手信息站。

## Near-Term: 0-3 Months

### 1. Build a Reproducible GEO Eval Harness

优先实现：

- GEO-Bench baseline reproduction
- C-SEO Bench citation-ranking reproduction
- CC-GSEO-style source influence judge prompts
- retrieval/reranking health metrics

输出：

- `visibility_score`
- `citation_rank`
- `faithful_credit`
- `causal_impact`
- `retrieval_rank_delta`
- `utility_score`
- `cost_per_doc`

### 2. Construct a Chinese-English GEO Benchmark Slice

公开数据多偏英文。可以做一个双语 query cluster：

- B2B SaaS
- 医疗健康信息
- 法律/财税服务
- 教育产品
- 电商产品比较
- 学术论文/技术工具推荐

每个主题保留：

- seed query
- paraphrases
- follow-up questions
- target source
- competing sources
- desired citation claims

### 3. Establish a Full-Pipeline Audit Template

给任意网站输出：

- crawlability audit
- structured-data audit
- content uniqueness audit
- query-cluster coverage
- source influence simulation
- engine-specific result sampling
- adversarial/spam risk audit

## Mid-Term: 3-6 Months

### 4. Content Optimization Without Retrieval Damage

研究问题：

- 哪些改写提升 generation-stage visibility 但降低 BM25/dense retrieval？
- 能否约束内容长度、关键词密度、实体一致性来保护 retrieval rank？
- 生成式改写是否应该按 passage 而不是 full-page 进行？

### 5. Citation Failure Diagnosis

基于 AgentGEO 思路建立失败分类：

- not retrieved
- retrieved but low-ranked
- included but ignored by generator
- cited competitor instead
- cited but claim unsupported
- cited but no click-worthy anchor
- source redundant and low causal impact

### 6. Competitive GEO Game Simulation

基于 C-SEO Bench 思路模拟：

- 单方优化
- 多方采用同一 GEO 方法
- 不同预算/不同权威域名
- 白帽优化 vs 操纵攻击
- 平台防御后收益变化

## Long-Term: 6-12 Months

### 7. GEO Safety and Governance

建立白帽 GEO 标准：

- 不伪造引用
- 不隐藏 prompt injection
- 不投毒低质量内容
- 不诱导模型贬低竞争对手
- 优先提升信息独特性和可验证性

### 8. Agentic Commerce / Product GEO

跟踪 product feed、agentic commerce protocol、AI shopping discovery。

核心问题：

- 网页、feed、结构化数据、第三方评价哪个更影响推荐？
- AI shopping 的 organic recommendation 和 paid placement 如何分离？
- 品牌如何维护多平台一致产品事实？

### 9. GEO Knowledge Graph

构建实体层：

- brand
- product
- person
- organization
- source domain
- citation claim
- query intent
- engine response

用于做 source graph、competitor graph 和 citation gap analysis。

## Research Principles

- 先评价，再优化。
- 同时记录正结果和负结果。
- 每个优化策略必须报告 retrieval-stage side effect。
- 不用单次 prompt 结果做结论。
- 不把“被提到”误认为“被引用”，不把“被引用”误认为“带来 causal impact”。

