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
