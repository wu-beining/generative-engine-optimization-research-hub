# Source Quality Rubric

每条资料进入仓库前，用下面规则打分，避免把噪声当信号。

## Evidence Level

| Level | Definition | Examples |
| --- | --- | --- |
| High | 官方文档、顶会/顶刊/正式 peer-reviewed 论文、可复现代码+数据 | OpenReview accepted paper, Google Search Central, arXiv with code and benchmark |
| Medium | arXiv preprint、技术报告、新闻采访、社区维护的高质量索引 | CC-GSEO-Bench, Guardian analysis, awesome list |
| Low | 厂商营销页、无实验博客、单次 prompt 截图、未注明方法的数据 | Agency case study, vendor ranking-factor claims |

## Novelty Score

| Score | Meaning |
| --- | --- |
| 5 | 新问题定义、新基准、新系统方法或关键负结果 |
| 4 | 在重要维度上扩展已有框架 |
| 3 | 有用改进，但与已有工作重合明显 |
| 2 | 主要是术语包装或行业执行建议 |
| 1 | 无明显新信息 |

## Value Score

| Score | Meaning |
| --- | --- |
| 5 | 必须读，能改变研究或产品路线 |
| 4 | 值得纳入核心方法或评估 |
| 3 | 对理解市场、平台或相邻问题有帮助 |
| 2 | 仅供发现工具或观察趋势 |
| 1 | 暂不建议投入时间 |

## Relevance Tier

- `core`: GEO 直接定义、方法、基准、指标、安全边界。
- `adjacent`: 对 GEO 有重要解释力，但不是直接研究 GEO。
- `background`: 架构、平台、产业背景。
- `low`: 只做链接留存，不进入结论。

## Dedup Rules

同一资料如果有 arXiv、OpenReview、GitHub、Hugging Face，应这样处理：

1. `papers.csv` 用论文页作为 `primary_url`。
2. `code_url` 放官方代码仓库。
3. `dataset_url` 放官方数据或模型集合。
4. `industry_sources.csv` 可额外记录 OpenReview / official venue 页面，用于确认接收状态。
5. 不为 Hugging Face paper mirror、ResearchGate mirror、AI 摘要站重复建论文条目。

