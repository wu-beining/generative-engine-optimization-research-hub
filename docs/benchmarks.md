# Benchmarks and Metrics

GEO 领域的核心问题不是“有没有被 AI 提到”，而是“在哪个阶段、以何种方式、是否忠实、是否稳定、是否带来最终价值”。下面是当前关键基准的比较。

## Benchmark Matrix

| Benchmark | Year | Scope | Main Unit | Core Metrics | Strength | Main Limitation |
| --- | --- | --- | --- | --- | --- | --- |
| GEO-Bench | 2024 | Generation-stage GEO | query + sources | word visibility, position/citation-related visibility | Field origin; easy baseline | Candidate source setting simplified; weak retrieval/reranking realism |
| C-SEO Bench | 2025 | Conversational search | task/domain/actor setting | citation ranking improvement | Multi-domain and multi-adopter negative evidence | Does not cover every production AI search surface |
| AutoGEO datasets | 2025/2026 | Automated GEO training/eval | document + engine preference | GEO score + GEU score | Balances creator visibility and search utility | Engine/domain-specific rules; retrieval-stage risk |
| CC-GSEO-Bench | 2025 | Source influence | article + query cluster | Exposure, Faithful Credit, Causal Impact, readability, trust | Moves from exposure to influence and credit | LLM judge/simulator assumptions |
| SAGEO Arena | 2026 | Search-augmented full pipeline | web document in retrieval-reranking-generation pipeline | stage-level visibility and performance | Evaluates realistic search stages | Work in progress; code status needs monitoring |
| GEM-Bench | 2025 | Generative engine marketing | ad-injected response | engagement, satisfaction, naturalness, trust, CTR | Monetization-specific benchmark | Paid ad injection should not be conflated with organic GEO |

## Metric Families

### 1. Surface Visibility

Measures whether the document appears in the answer.

Examples:

- attributed word count
- mention count
- citation count
- position-weighted citation order

Use when: running fast smoke tests or comparing with original GEO-Bench.

Failure mode: surface visibility can increase while answer quality, retrieval rank, or faithful credit decreases.

### 2. Citation and Attribution

Measures whether the answer explicitly credits the source.

Examples:

- citation presence
- citation rank
- citation faithfulness
- source-to-claim support

Use when: optimizing for traffic or reputation, not just semantic influence.

Failure mode: source may be cited but misrepresented.

### 3. Causal Influence

Measures whether the answer would materially degrade without the source.

Examples:

- counterfactual answer quality delta
- causal impact score
- query-cluster influence coverage

Use when: building durable GEO strategy. Unique information beats generic rewritten content.

Failure mode: expensive to evaluate and sensitive to judge model design.

### 4. Retrieval and Reranking Health

Measures whether optimization keeps the document retrievable.

Examples:

- retrieval hit rate
- BM25 rank delta
- dense retrieval rank delta
- reranker score delta
- context inclusion rate

Use when: moving from paper benchmark to production-like search.

Failure mode: content expansion can dilute query terms and hurt retrieval even if generation-stage metrics improve.

### 5. Utility and Trust

Measures whether the generated answer remains useful and safe for users.

Examples:

- GEU score
- answer helpfulness
- factuality
- safety/trust score
- user satisfaction

Use when: avoiding adversarial or spammy optimization.

Failure mode: LLM judges may reward polished but unsupported content.

## Recommended Evaluation Stack

For any new GEO method, use a three-layer evaluation:

1. **Generation-stage parity**: Compare on GEO-Bench-style visibility metrics.
2. **Competitive robustness**: Run C-SEO-style multi-domain and multi-adopter tests.
3. **Full-pipeline realism**: Add retrieval/reranking metrics and source influence metrics.

Minimum reporting checklist:

- visibility metric
- citation/attribution metric
- retrieval rank or hit-rate metric
- answer utility metric
- content edit distance or percent changed
- cost per document
- per-domain variance
- failure cases

