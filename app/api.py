# app/api.py
"""FastAPI 接口。启动: uvicorn app.api:app --port 8000
查询: POST /ask  {"question": "..."}  →  {"answer", "sources", "rounds"}
构建放在 lifespan 里：服务启动时建一次，不阻塞请求。
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
from app.builder import build_app


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.chunks, app.state.agent = build_app()   # 启动时构建（1~3 分钟）
    yield


app = FastAPI(title="Ariadne", lifespan=lifespan)


class Question(BaseModel):
    question: str


@app.post("/ask")
def ask(q: Question):
    r = app.state.agent.ask(q.question)
    return {"answer": r["answer"], "sources": r["sources"], "rounds": r["rounds"]}


@app.get("/health")
def health():
    return {"status": "ok"}
