from modules.world_model.causal_model import CausalModel

class WorldCausal:
    def __init__(self):
        self.causal = CausalModel()

    def run(self, query: str):
        return [self.causal.analyze(query)]
