"""
Meta-Controller — Phase 5A
元認知／自省中樞
"""

class MetaController:
    def __init__(self):
        pass

    def evaluate(self, *, query, skill, world=None, reasoning=None, memory=None):
        """
        根據本次回應結果，進行自省評估
        """
        meta = {
            "current_state": None,
            "sufficiency": "unknown",
            "need_clarification": False,
            "overconfidence_check": False,
            "tone_adjust": "normal"
        }

        if skill == "world_model":
            meta["current_state"] = "explaining_world"
        elif skill == "reasoning_engine":
            meta["current_state"] = "reasoning"
        elif skill == "memory_core":
            meta["current_state"] = "recalling_memory"
        else:
            meta["current_state"] = "general_response"

        if reasoning and isinstance(reasoning, dict):
            confidence = reasoning.get("confidence", 0.5)
            if confidence < 0.6:
                meta["sufficiency"] = "low"
                meta["need_clarification"] = True
            elif confidence < 0.75:
                meta["sufficiency"] = "medium"
            else:
                meta["sufficiency"] = "high"

            if confidence > 0.9 and not reasoning.get("cause_effect"):
                meta["overconfidence_check"] = True

        if world and isinstance(world, list) and len(world) <= 1:
            meta["need_clarification"] = True

        if meta["need_clarification"]:
            meta["tone_adjust"] = "ask_back"
        elif meta["overconfidence_check"]:
            meta["tone_adjust"] = "soften"

        return meta
