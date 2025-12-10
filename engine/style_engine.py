class StyleEngine:
    """
    風格引擎：將融合結果套用風格標籤與輸出格式。
    """

    def apply(self, fused: dict):
        style = "寫實"
        if "fused_force_level" in fused and fused["fused_force_level"] >= 4:
            style = "動作強烈"
        return {
            "style": style,
            "shot": fused.get("fused_shot", ""),
            "emotion": fused.get("fused_emotion", ""),
            "action": fused.get("fused_action", ""),
        }

    def process(self, query: str):
        tone = "寫實"
        if any(k in query for k in ["爆", "衝", "跑", "急"]):
            tone = "動作強烈"
        elif any(k in query for k in ["沉默", "靜", "慢"]):
            tone = "抒情慢節奏"
        return {
            "tone": tone,
            "guideline": "冷靜、準確、條理、帶1%溫度"
        }
