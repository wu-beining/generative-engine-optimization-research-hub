# Literature Review and Value Judgement

本页按“是否值得长期跟踪”组织，不按发布时间堆链接。

## Tier 1: Core Papers

### GEO: Generative Engine Optimization

价值：GEO 的正式学术原点。它把生成式搜索中的内容方可见度问题定义为黑箱优化，并引入 GEO-Bench。它的最大贡献是把“生成答案中的内容占比、位置和引用”变成可测对象。

重合：后续 AutoGEO、AgenticGEO、Role-Augmented GSEO 都是在它的内容改写和可见度指标上继续扩展。

边界：它主要评估候选内容已经进入上下文后的 generation-stage 影响，对真实搜索管线中的召回和重排关注不足。

判断：必须跟踪。任何新 GEO 方法都应至少在 GEO-Bench 或可映射指标上对照。

### C-SEO Bench

价值：这是当前最重要的“降温论文”。它把 C-SEO 放到多任务、多领域、多采用者场景下测试，发现很多当下方法并不稳定，甚至会损害排名。传统 SEO 中的检索排名和上下文位置仍然更有影响。

重合：与 GEO-Bench 都测内容优化，但它更强调竞争环境和 citation ranking。

边界：它以 conversational search benchmark 为核心，不等同于所有 Google AI Overview 或 ChatGPT Search 真实行为。

判断：必须跟踪。它是避免 GEO 变成玄学服务的关键基线。

### AutoGEO

价值：将人工设计规则推进到“自动抽取生成引擎偏好 + 自动改写 + 小模型 RL 训练”。它还引入 GEO score 与 GEU score 的权衡，强调不要为了内容方曝光损害搜索效用。

重合：与 GEO 原文的改写策略高度相关，但把规则发现和部署自动化了。

边界：不同引擎、不同领域要重新抽取规则；如果改写让文档过长或偏离检索词，可能在真实检索阶段受损。

判断：必须跟踪。适合作为自动化 GEO 研究的主干代码库。

### CC-GSEO-Bench

价值：它把 GEO 评价从“出没出现”推进到“有多大真实影响”。Exposure、Faithful Credit、Causal Impact 的拆分非常关键，因为一个来源可能被引用但被误读，也可能影响答案却没有显式归因。

重合：与 GEO-Bench 和 C-SEO Bench 都评估可见度，但更像 creator-centered influence benchmark。

边界：依赖 LLM judge 和模拟管线，后续需要和真实商业引擎对齐。

判断：必须跟踪。未来 GEO 指标应吸收其 influence / credit 视角。

### SAGEO Arena

价值：直接指出现有 GEO 基准忽略真实搜索增强管线。它把结构化网页信息、检索、重排和生成一起纳入评估，这正是 GEO 从论文到产品的最大落差。

重合：补足 GEO-Bench / AutoGEO 的简化候选集假设。

边界：目前是 work in progress，代码和社区采用度还需确认。

判断：必须跟踪。它代表 2026 以后 GEO 评估的正确方向。

### Diagnosing and Repairing Citation Failures

价值：提出“为什么某个文档没有被引用”的诊断式 GEO，而不是一刀切改写。它区分 citation failure modes，并用 AgentGEO 选择针对性修复。

重合：与 AgenticGEO 都是 agentic GEO，但本工作更聚焦 citation failure 与文档级修复。

边界：agentic 修复的调用成本、稳定性和跨引擎泛化需要更多实证。

判断：必须跟踪。它对“品牌被提到但没引用”或“长尾内容被淹没”很有价值。

### AgenticGEO

价值：用 MAP-Elites 策略记忆和 co-evolving critic 做内容条件化策略选择，试图摆脱固定 prompt 策略。

重合：与 AutoGEO 都在做自动化内容优化；AutoGEO 偏规则抽取与小模型训练，AgenticGEO 偏策略演化与推理期规划。

边界：仍需检验代理反馈是否过拟合，以及策略是否在真实检索阶段保留收益。

判断：跟踪。适合探索 adaptive GEO 系统，但不能单独作为真实商业效果证据。

### MAGEO: From Experience to Skill

价值：这篇把 GEO 明确重构为“可复用策略学习”问题，而不是每个实例孤立优化。MAGEO 用 Preference Agent、Planner Agent、Editor Agent、Evaluator Agent、层级记忆和 Fidelity Gate 组成闭环，把成功编辑模式蒸馏为可跨任务和跨引擎复用的优化技能。它还引入 Twin Branch Evaluation Protocol、DSV-CF 指标和 MSME-GEO-Bench。

重合：与 AutoGEO 和 AgenticGEO 在自动化 GEO 上重合，但差异点是 strategy reuse / skill learning。AutoGEO 更偏引擎偏好规则抽取和小模型训练；AgenticGEO 更偏策略演化和 critic 规划；MAGEO 更偏多智能体执行层、层级记忆和 attribution fidelity。

边界：新指标和新 benchmark 需要独立复现；如果只看系统复杂度，可能不如 AutoGEO 易部署。

判断：必须跟踪。它是 2026 年 GEO 从“改写策略”走向“经验累积和策略复用”的关键论文。

## Tier 2: Important Adjacent Work

### Adversarial SEO for LLMs / Ranking Manipulation / GASLITE

价值：这些工作共同说明 GEO 天然有操纵风险。只要 LLM 需要从第三方内容中选择、排序、总结，就会出现偏好操纵、排名攻击、稠密检索投毒。

重合：三者都在 adversarial search / retrieval manipulation，但攻击面不同：生成选择、对话搜索排序、dense retrieval。

判断：必须作为防御线跟踪。任何 GEO 产品都应内置操纵检测、内容审计和可解释评价。

### What Evidence Do Language Models Find Convincing?

价值：解释 LLM 在 RAG 场景下怎样看证据，尤其是模型可能过度依赖与 query 的相关性，而不充分重视人类看重的中立性、科学引用等特征。

判断：虽非 GEO 论文，但对“为什么 GEO 技巧能奏效/失效”很关键。

### ConflictBank

价值：GEO 常常涉及新鲜网页内容与模型内部知识冲突。ConflictBank 提供知识冲突评估框架，有助于研究生成引擎何时相信外部内容。

判断：背景重要，直接产品价值中等。

### GEM-Bench

价值：GEO 的商业化相邻方向。它研究广告如何嵌入生成答案，并评估用户满意度、自然度、CTR 等。

判断：值得观察，但必须与 organic GEO 分开。广告插入不是“自然引用优化”。

## Tier 3: Watch / Background

### Role-Augmented Intent-Driven GSEO

价值：强调用户意图和角色视角，有利于 query cluster 和 content brief 设计。

重合：与普通 prompt rewriting、intent expansion 很接近。

判断：观察。除非后续有更强代码/数据/对照，否则不宜作为核心方法。

### Beyond Retrieval

价值：提出从 RAG 到 deterministic agent handoff 的方向，适合思考 agentic commerce 或垂直 agent 入口。

重合：与 agentic platform 和商业路由更接近，不是传统 GEO。

判断：观察。当前证据偏概念和单产品案例。

### When Search Engine Services meet LLMs

价值：给 Search4LLM / LLM4Search 的架构背景。

判断：作为术语和系统背景使用，不直接支撑 GEO 方法论。
