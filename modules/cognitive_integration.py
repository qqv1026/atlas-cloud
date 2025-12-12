"""
Cognitive Integration Layer — Phase 4
世界 × 推理 × 記憶 的理解整合層
"""

from modules.world_model.world_model import WorldModel
from modules.reasoning_core.reasoning_engine import ReasoningEngine
from modules.memory_core.memory_router import MemoryRouter


class CognitiveIntegration:
    def __init__(self):
        self.world = WorldModel()
        self.reasoning = ReasoningEngine()
        self.memory = MemoryRouter()

    def run(self, query: str):
        world_result = self.world.run(query)

        reasoning_input = f"根據以下世界判斷結果解釋原因：{world_result}"
        reasoning_result = self.reasoning.run(reasoning_input)

        memory_record = {
            "type": "world_understanding",
            "query": query,
            "understanding": reasoning_result.get("conclusion", ""),
            "source": "cognitive_integration"
        }
        self.memory.store(memory_record)

        return {
            "world": world_result,
            "reasoning": reasoning_result,
            "memory_update": "stored"
        }
