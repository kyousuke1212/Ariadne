# Ariadne

自研混合检索（BM25 + Dense + 图索引）的 Agentic RAG 知识库系统

## 技术栈
- Python 3.11
- LLM: DeepSeek（openai SDK）
- Embedding: BGE-small-zh-v1.5（本地）
- 分词: jieba
- 零LangChain，核心算法自研

## Roadmap
- [x] ingest — Markdown加载 + 切块 + jieba分词
- [ ] embed — 向量化（批处理+缓存）
- [ ] BM25 关键词检索
- [ ] 评测集（先行）
- [ ] BaseRetriever + brute向量检索
- [ ] RRF 混合融合
- [ ] 评测指标（Recall@K / MRR / 延迟）
- [ ] 自研 HNSW 图索引 ★
- [ ] ReAct Agent
- [ ] FastAPI + Streamlit + Docker

## TODO
- [ ] 长章节跨块时 heading 只有文档标题，需要按标题预切分

## 项目结构
agentic-rag/
├── core/              配置、日志、异常
├── ingestion/         文档加载 + 切块 + 分词
│   ├── loader.py      Markdown 目录加载器
│   ├── chunker.py     滑窗切块（重叠 + 尾块过滤）
│   └── pipeline.py    组装流水线（Chunk 构建）
├── embed/             embedding 服务（批处理 + 缓存）
├── index/             检索器抽象层（base / brute / hnsw）
├── retrieve/          BM25 / 向量 / RRF 融合
├── agent/             ReAct 循环
├── generate/          答案合成 + 引用溯源
├── eval/              评测集 + 指标
├── app/               FastAPI + Streamlit
├── data/              测试语料
│   ├── 团队介绍.md
│   └── 检索技术笔记.md
├── .gitignore
└── README.md