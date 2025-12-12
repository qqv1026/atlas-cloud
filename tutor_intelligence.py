"""
Tutor Intelligence — Phase 5B
教學人格／導師行為層
"""

class TutorIntelligence:
    def __init__(self):
        pass

    def teach(self, *, query, result, meta):
        """
        根據 meta 決定教學行為
        """
        mode = "direct"
        follow_up = None

        if meta.get("need_clarification"):
            mode = "ask_back"
            follow_up = "你希望我從哪個角度說明，或要舉一個生活例子嗎？"
        elif meta.get("tone_adjust") == "soften":
            mode = "guided"

        if meta.get("sufficiency") == "low":
            mode = "guided"

        if isinstance(result, dict):
            core = result.get("conclusion", "")
        elif isinstance(result, list):
            core = "\n".join(str(x) for x in result)
        else:
            core = str(result)

        if mode == "guided":
            response = f"我們一步一步來看：\n{core}"
        elif mode == "ask_back":
            response = f"{core}\n\n我需要你幫我確認一下："
        else:
            response = core

        return {
            "mode": mode,
            "response": response,
            "follow_up": follow_up
        }
