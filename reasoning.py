from modules.reasoning_core.reasoning_engine import ReasoningEngine

class Reasoning:
    def __init__(self):
        self.engine = ReasoningEngine()

    def run(self, query: str):
        return self.engine.run(query)
