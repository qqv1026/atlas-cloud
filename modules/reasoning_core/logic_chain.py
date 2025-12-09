# reasoning_core/logic_chain.py

class LogicChain:
    """
    簡易 chain-of-thought 模組，用於推理過程。
    """

    def run_chain(self, query: str):
        steps = [
            f"接收問題：{query}",
            "分析語意…",
            "建立推理鏈…",
            "產生初步判斷…",
        ]
        return steps
