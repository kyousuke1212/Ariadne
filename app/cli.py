# app/cli.py
"""命令行问答。两种用法：
  python -m app.cli "谁负责搭建产品矩阵体系？"   # 单问
  python -m app.cli                                # 交互式（多轮对话，exit 退出）
"""
import sys
from app.builder import build_app, print_answer


def main():
    chunks, agent = build_app()
    if len(sys.argv) > 1:
        q = " ".join(sys.argv[1:])
        print_answer(chunks, q, agent.ask(q))
        return
    print("Ariadne 知识库助手（输入 exit 退出）")
    while True:
        q = input("\n问: ")
        if q.strip().lower() in ("exit", "quit", "q"):
            break
        print_answer(chunks, q, agent.ask(q))
        print()


if __name__ == "__main__":
    main()
