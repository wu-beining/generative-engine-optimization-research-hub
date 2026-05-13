# Platform Notes

本页只记录官方或高可信来源中能验证的规则。不要把营销博客里的“排名因素”直接当作平台事实。

## Google AI Experiences on Search

官方方向：

- 基础 SEO 原则仍然适用：满足用户需求、提供独特且有帮助的内容。
- 爬取和索引仍是前置条件：页面需要可访问、可索引、返回成功状态。
- 站点可以通过 preview controls 管理在搜索和 AI 体验中的展示方式，例如 `nosnippet`、`data-nosnippet`、`max-snippet`、`noindex`。
- 结构化数据应与页面可见内容一致。
- 多模态内容重要：高质量图片、视频、Merchant Center、Business Profile 等会影响 AI 搜索中的展示机会。

GEO 启示：

- 不要把 GEO 与 SEO 对立起来。Google 的官方口径仍然要求高质量内容、技术可访问性和结构化数据。
- 对 Google AI Overviews / AI Mode，技术 SEO、结构化数据、页面体验和内容独特性是底座，不是可选项。
- `noindex`、`nosnippet` 等控制会影响可见性，需要和内容授权策略一起设计。

## ChatGPT Search

官方方向：

- ChatGPT search 可提供带链接来源的实时答案。
- 在需要搜索时，ChatGPT 可能把用户问题改写成一个或多个面向搜索伙伴的查询。
- 回答可能包含 inline citations，也可能在 Sources 面板展示来源。
- 要进入 ChatGPT Search，需要允许 `OAI-SearchBot` 访问站点，并确保主机/CDN 允许 OpenAI published IPs。
- 商业购物场景里，OpenAI 推动 product feed，让产品信息更完整、及时、可控。

GEO 启示：

- Query fan-out / query rewriting 很关键：内容不应只覆盖一个关键词，而应覆盖 intent cluster。
- 被 crawl 是前置条件，但不是排名保证。
- 对电商和产品类内容，结构化 product feed 可能比单纯网页改写更重要。
- 来源面板和 inline citations 是不同展示形式，评价时要分别记录。

## Perplexity, Claude, Copilot, Gemini

本次整理未找到足够稳定的官方排名机制说明，因此暂不把第三方“排名因素分析”放入核心结论。后续维护时可加入：

- 官方 publisher / crawler / robots 说明。
- 官方 commerce / product feed / ads 文档。
- 可复现实验，而不是单次 prompt 截图。

## Practical Platform Checklist

对一个站点做 GEO 审计时，至少检查：

- 是否允许目标 AI/search crawler 访问。
- 页面主要内容是否服务端可见，避免 crawler 只看到空壳。
- title、heading、summary、FAQ、schema 是否和可见内容一致。
- 是否有清晰作者、日期、实体、来源、统计和原始数据。
- 是否覆盖 query cluster，而不只是单关键词。
- 是否有可引用短句、表格、定义、比较和决策标准。
- 是否有独特信息，否则即使被引用也可能缺少 causal impact。
- 是否监控 AI referral、citation、brand mention、sentiment、conversion。

