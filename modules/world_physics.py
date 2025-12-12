from modules.world_model.physics_model import PhysicsModel

class WorldPhysics:
    def __init__(self):
        self.physics = PhysicsModel()

    def run(self, query: str):
        g = self.physics.gravity()
        return [f"重力加速度約 {g} m/s^2，與『{query}』相關的物理直觀已載入。"]
