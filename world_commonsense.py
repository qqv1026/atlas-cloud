from modules.world_model.commonsense import CommonSenseModel

class WorldCommonsense:
    def __init__(self):
        self.cs = CommonSenseModel()

    def run(self, query: str):
        return [self.cs.check(query)]
