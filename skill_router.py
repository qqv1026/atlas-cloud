class SkillRouter:
    def route(self, query: str) -> dict:
        q = query.lower()
        intent = "unknown"
        if any(k in q for k in ["目標", "想要", "規劃"]):
            intent = "plan"
        elif any(k in q for k in ["為什麼", "原因", "推理"]):
            intent = "explain"
        elif any(k in q for k in ["記得", "之前", "你說過"]):
            intent = "remember"
        elif any(k in q for k in ["教我", "解釋給我聽"]):
            intent = "tutor"

        routes = []
        if any(k in q for k in ["世界", "物理", "常識", "規律", "原理", "模型"]):
            routes.append("world_model")
        if any(k in q for k in ["因果", "推理", "分析", "為什麼", "原因"]):
            routes.append("reasoning")
        if any(k in q for k in ["記得", "之前", "你說過", "記住", "記錄", "幫我記"]):
            routes.append("memory")
        if any(k in q for k in ["教我", "解釋給我聽"]):
            routes.append("tutor")

        seen = set()
        ordered_routes = []
        for r in ["world_model", "reasoning", "memory", "tutor"]:
            if r in routes and r not in seen:
                ordered_routes.append(r)
                seen.add(r)

        signals = 1 if intent != "unknown" else 0
        signals += len(ordered_routes)
        confidence = max(0.5, min(1.0, 0.5 + 0.1 * signals))

        return {"intent": intent, "route": ordered_routes, "confidence": round(confidence, 2)}
