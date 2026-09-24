# agent/react.py
"""ReAct Agent——第 9 步成品：Thought/Action/Observation 循环。
把检索器包装成工具，让 LLM 自己决定搜什么、搜几次、什么时候停。
零 LangChain：循环、解析、消息管理全部手写。"""
import os
import re
from openai import OpenAI

SYSTEM_PROMPT = """你是 Ariadne 知识库助手。回答必须依据检索到的资料，禁止凭记忆编造。严格按以下格式循环，直到能回答：

Thought: <对当前情况的分析：证据够不够、下一步搜什么>
Action: search[<搜索关键词>]

之后你会收到 Observation（搜索结果）。反复搜索直到证据足够，然后输出：

Final Answer: <最终答案>
[sources: <用到的块ID，逗号分隔>]

规则：
1. 每轮只输出一个 Action，禁止同时给多个
2. 证据不足就换角度搜索，重复同一关键词没有意义
3. Final Answer 必须附 [sources: ...]，块 ID 形如 vue3-1.md-3
"""


class SearchTool:
    """把检索器包成工具：query → top-k 块的文本 + 块 ID（Observation 的原料）。"""
    def __init__(self, retriever, chunks, k=5):
        self.retriever = retriever
        self.chunks = chunks
        self.k = k

    def __call__(self, query: str) -> str:
        ids = self.retriever.search(query, self.k)
        parts = [f"[{self.chunks[i].chunk_id}]\n{self.chunks[i].text[:300]}" for i in ids]
        return "\n\n".join(parts)


class ReactAgent:
    def __init__(self, tool, max_rounds=4, model="deepseek-v4-pro"):
        self.tool = tool
        self.max_rounds = max_rounds
        api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY")
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.model = model
        # messages 是会话历史：连续 ask 多个问题会累积上下文（多轮对话能力）
        self.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    def _call_llm(self) -> str:
        resp = self.client.chat.completions.create(
            model=self.model, messages=self.messages, temperature=0.2)
        return resp.choices[0].message.content or ""

    def _parse(self, text: str):
        """解析模型输出。返回 ("search", 关键词) / ("final", 答案) / ("unparsed", 原文)。"""
        m = re.search(r"Final Answer:\s*(.+)", text, re.S)
        if m:
            return ("final", m.group(1).strip())
        m = re.search(r"Action:\s*search\[(.*?)\]", text, re.S)
        if m:
            return ("search", m.group(1).strip())
        return ("unparsed", text)

    def ask(self, question: str) -> dict:
        """跑一轮完整 ReAct。返回 {answer, sources, rounds, trace}。"""
        self.messages.append({"role": "user", "content": question})
        trace = []
        for r in range(self.max_rounds):
            text = self._call_llm()
            kind, payload = self._parse(text)
            trace.append(text)
            if kind == "final":
                self.messages.append({"role": "assistant", "content": text})
                return self._finish(payload, r + 1, trace)
            if kind == "search":
                obs = self.tool(payload)
                self.messages.append({"role": "assistant", "content": text})
                self.messages.append({"role": "user", "content": f"Observation:\n{obs}"})
            else:
                # 不按格式出牌：把原文当观察追问，让它按格式继续
                self.messages.append({"role": "assistant", "content": text})
                self.messages.append({"role": "user",
                                      "content": "Observation: 未找到 Action 或 Final Answer，请按格式输出。"})
        # 轮数耗尽：强制收卷
        self.messages.append({"role": "user", "content": "轮数已用尽，请直接输出 Final Answer。"})
        text = self._call_llm()
        kind, payload = self._parse(text)
        trace.append(text)
        self.messages.append({"role": "assistant", "content": text})
        return self._finish(payload if kind == "final" else text, self.max_rounds + 1, trace)

    @staticmethod
    def _finish(payload: str, rounds: int, trace: list) -> dict:
        m = re.search(r"\[sources:\s*([^\]]+)\]", payload, re.S)
        sources = [s.strip() for s in m.group(1).split(",")] if m else []
        return {"answer": payload, "sources": sources, "rounds": rounds, "trace": trace}
