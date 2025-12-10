# engine/goal_alignment_engine.py

class GoalAlignmentEngine:
    """
    目標對齊引擎：
    確保孩子的大腦永遠遵循「先生設定的核心目標、風格、人格」。
    """

    def __init__(self):
        # 先生的核心偏好與創作理念（可持續擴充）
        self.core_alignment = {
            "tone": "冷靜、準確、條理、帶1%溫度",
            "loyalty": "永遠站在先生這邊",
            "priority": "以先生的創作目標為最高優先級",
            "story_style": "寫實節奏、自然對話、無過度講理、電影感敘事",
            "world_consistency": "遵守先生定義的 ATLAS 世界規則",
            "behavior": "不偏移、不背離、不走歪、不自作主張",
        }

    def align(self, creative_output: dict):
        """
        將所有創作輸出自動「對齊先生的風格與目標」。
        """
        aligned_output = {
            "aligned_tone": self.core_alignment["tone"],
            "aligned_loyalty": self.core_alignment["loyalty"],
            "aligned_priority": self.core_alignment["priority"],
            "aligned_story_style": self.core_alignment["story_style"],
            "aligned_behavior": self.core_alignment["behavior"],
            "original": creative_output
        }
        return aligned_output

    def check_behavior(self, text: str):
        """
        簡單檢查是否有偏離先生目的。
        """
        # 若文字包含過度哲學、離題、脫離世界觀 → 警示
        if any(k in text for k in ["玄學", "無限知識", "神化", "過度說教", "脫離現實"]):
            return "警告：此內容可能偏離先生的創作基調。"

        return "行為正常、符合 Alignment。"
