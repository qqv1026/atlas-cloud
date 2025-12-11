# world_model/physics_model.py

class PhysicsModel:
    """
    基礎物理直觀。後續可擴充為更完整的世界模型。
    """

    def gravity(self):
        return 9.8  # m/s^2

    def can_object_fly(self, mass, lift):
        return lift > mass * self.gravity()
