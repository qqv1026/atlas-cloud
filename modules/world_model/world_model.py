from modules.world_model.world_causal import WorldCausal
from modules.world_model.world_commonsense import WorldCommonsense
from modules.world_model.world_physics import WorldPhysics


class WorldModel:
    def __init__(self):
        self.causal = WorldCausal()
        self.commonsense = WorldCommonsense()
        self.physics = WorldPhysics()

    def run(self, query: str):
        q = query.lower()

        if "因果" in q or "為什麼" in q:
            return {"skill": "world-causal", "result": self.causal.run(query)}

        if "常識" in q or "合理嗎" in q:
            return {"skill": "world-commonsense", "result": self.commonsense.run(query)}

        if "物理" in q or "力" in q or "速度" in q or "加速度" in q:
            return {"skill": "world-physics", "result": self.physics.run(query)}

        return {"skill": "world", "result": ["（世界模型）目前無法分類，但已收到訊息。"]}
