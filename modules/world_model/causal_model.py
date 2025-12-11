# world_model/causal_model.py

class CausalModel:
    """
    因果模型：理解『原因 → 結果』。
    """

    def analyze(self, event: str):
        if "爆炸" in event:
            return "可能原因：壓力過高、引火物、碰撞。"
        if "停電" in event:
            return "可能原因：電網負載、斷線、設備故障。"
        return "需要更多資訊判斷。"
