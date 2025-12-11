# reasoning_core/reasoning_engine.py

class ReasoningEngine:
    """
    通用推理核心：負責分解問題、邏輯推論、反思修正。
    """

    def __init__(self):
        try:
            from .question_engine import QuestionEngine
            from .logic_chain import LogicChain
            self._question = QuestionEngine()
            self._chain = LogicChain()
        except Exception:
            self._question = None
            self._chain = None

    def decompose(self, query: str):
        """
        將問題拆解成更小的子問題。
        """
        # 最基礎版本：分句拆解
        parts = [p.strip() for p in query.replace("？", "?").split("?") if p.strip()]
        return parts

    def infer(self, query: str):
        """
        高層推理：理解問題、找出核心需求。
        """
        lowered = query.lower()

        if "why" in lowered or "為什麼" in query:
            return "這是一個原因推論問題。"
        if "how" in lowered or "怎麼做" in query:
            return "這是一個方法與步驟問題。"
        if "what" in lowered or "是什麼" in query:
            return "這是一個定義或理解問題。"

        return "通用推理：需要綜合判斷。"

    def infer_intent(self, query: str):
        if self._question:
            intent = self._question.analyze_intent(query)  # e.g. "intent: cause"
            return intent.replace("intent: ", "")
        lowered = query.lower()
        if "為什麼" in query or "why" in lowered:
            return "cause"
        if "怎麼" in query or "方法" in query or "how" in lowered:
            return "method"
        if "目標" in query or "想要" in query or "goal" in lowered:
            return "goal"
        return "unknown"

    def run_chain(self, query: str):
        if self._chain:
            return self._chain.run_chain(query)
        return [f"接收問題：{query}", "分析語意…", "建立推理鏈…", "產生初步判斷…"]

    def run(self, query: str):
        steps = self.run_chain(query)
        return {"type": "reasoning", "steps": steps, "conclusion": self.infer(query)}

    def reflect(self, answer: str):
        """
        最基礎版反思：檢查答案是否含糊。
        """
        if len(answer) < 10:
            return "答案過短，需補充。"
        return "答案可接受。"
