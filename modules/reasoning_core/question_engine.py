# reasoning_core/question_engine.py

class QuestionEngine:
    """
    問題引擎：協助孩子學會提問、釐清目標。
    """

    def analyze_intent(self, query: str):
        """
        判斷使用者真正意圖。
        """
        q = query.lower()

        if "目標" in query or "想要" in query:
            return "intent: goal"
        if "怎麼" in query or "方法" in query:
            return "intent: method"
        if "為什麼" in query:
            return "intent: cause"

        return "intent: unknown"

    def generate_subquestions(self, query: str):
        """
        引導式子問題。
        """
        return [
            f"此問題的核心是什麼？（基於：{query}）",
            "需要哪些資訊才能回答？",
            "是否存在先決條件？"
        ]
