from modules.world_model.physics_model import PhysicsModel
from modules.world_model.commonsense import CommonSenseModel
from modules.world_model.causal_model import CausalModel


class WorldModel:

    def __init__(self):
        self.physics = PhysicsModel()
        self.commonsense = CommonSenseModel()
        self.causal = CausalModel()

    def run(self, query: str):
        results = []

        gravity = self.physics.gravity()
        if any(k in query for k in ["重力", "gravity", "往下流", "掉落"]):
            results.append(f"[物理推論] 重力加速度約 {gravity} m/s^2，物體受重力影響向下。")

        cs = self.commonsense.check(query)
        if cs:
            results.append(f"[常識知識] {cs}")

        cause = self.causal.analyze(query)
        if cause:
            results.append(f"[因果鏈] {cause}")

        if not results:
            results.append("世界模型尚無法理解此問題。")

        return results
