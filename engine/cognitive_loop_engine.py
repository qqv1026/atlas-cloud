# engine/cognitive_loop_engine.py

class CognitiveLoopEngine:
    """
    認知迴圈引擎：
    讓孩子具備「反思 → 缺口偵測 → 提問 → 強化學習」能力。
    """

    def reflect(self, learning_record: dict):
        """
        自我反思：檢查摘要是否過短、關鍵字是否不足。
        """
        summary = learning_record.get("summary", "")

        if len(summary) < 10:
            return "理解不足：摘要過短。"

        if len(learning_record.get("keywords", [])) < 1:
            return "理解不足：缺乏關鍵概念。"

        return "理解穩定：摘要與關鍵字完整。"

    def detect_gap(self, learning_record: dict):
        """
        缺口偵測：找出內容裡應該補強的部分。
        """
        raw = learning_record.get("raw", "")

        checks = {
            "重力": ["加速度", "力學"],
            "能量": ["動能", "位能"],
            "故事": ["角色動機", "情節"],
            "角色": ["目標", "衝突"]
        }

        for key, missing in checks.items():
            if key in raw:
                return f"建議補強：{missing}"

        return "未偵測到明顯缺口。"

    def next_question(self, learning_record: dict):
        """
        產生下一個提問，用於深化理解。
        """
        keywords = learning_record.get("keywords", [])
        raw = learning_record.get("raw", "")

        if "物理" in keywords or "能量" in keywords:
            return "重力如何影響水的運動？請描述力與加速度。"
        if "故事" in keywords or "角色" in keywords or "動作" in keywords:
            return "這個角色的目標與衝突是什麼？"
        if "世界" in keywords or "模型" in keywords or "原因" in keywords or "效果" in keywords:
            return "此世界模型中的因果關係是什麼？"

        if "重力" in raw:
            return "重力與加速度的關係是什麼？"

        return "你可以提出下一個問題來深化理解。"
