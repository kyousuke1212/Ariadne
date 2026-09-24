# app/ui.py
"""Streamlit 页面。启动: streamlit run app/ui.py
@st.cache_resource 缓存构建结果：页面每次刷新不重建检索器。
"""
import streamlit as st
from app.builder import build_app


@st.cache_resource
def get_app():
    return build_app()


st.title("Ariadne 知识库")
st.caption("自研混合检索（BM25 + Dense + HNSW 图索引）+ ReAct Agent")

chunks, agent = get_app()
q = st.text_input("问点什么:", placeholder="例如：谁负责搭建产品矩阵体系？")

if q:
    with st.spinner("思考中…"):
        r = agent.ask(q)
    st.markdown(r["answer"])
    if r["sources"]:
        by_id = {c.chunk_id: c for c in chunks}
        with st.expander(f"来源（{len(r['sources'])} 个块，{r['rounds']} 轮）"):
            for sid in r["sources"]:
                c = by_id.get(sid)
                if c:
                    st.markdown(f"**[{sid}]** ({c.source})\n\n{c.text[:200]}")
