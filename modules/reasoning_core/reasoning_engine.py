# reasoning_core/reasoning_engine.py

class ReasoningEngine:
    """
    通用推理核心：負責分解問題、邏輯推論、反思修正。
    """

    def __init__(self):
        pass

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

    def reflect(self, answer: str):
        """
        最基礎版反思：檢查答案是否含糊。
        """
        if len(answer) < 10:
            return "答案過短，需補充。"
        return "答案可接受。"
