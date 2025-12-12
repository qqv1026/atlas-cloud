# engine/emotion_character_engine.py

class EmotionCharacterEngine:
    """
    角色心理大腦：
    分析情緒、動機、行為模式、角色弧線與角色定位。
    """

    def detect_emotion(self, text: str):
        if any(k in text for k in ["怕", "恐懼", "緊張", "心跳"]):
            return "恐懼 / 緊張"
        if any(k in text for k in ["怒", "憤", "大喊", "咬牙"]):
            return "憤怒"
        if any(k in text for k in ["傷心", "落淚", "沉默"]):
            return "悲傷"
        if any(k in text for k in ["開心", "笑", "鬆一口氣"]):
            return "開心 / 放鬆"
        return "中性情緒"

    def detect_motivation(self, text: str):
        if any(k in text for k in ["救", "保護", "擋住", "守護"]):
            return "保護他人"
        if any(k in text for k in ["逃", "跑", "閃開"]):
            return "逃離危險"
        if any(k in text for k in ["調查", "找到原因", "追查"]):
            return "尋找真相"
        if any(k in text for k in ["攻擊", "反擊", "報仇"]):
            return "攻擊 / 報復"
        return "一般行為動機"

    def detect_behavior_style(self, text: str):
        if any(k in text for k in ["突然", "衝", "不顧一切"]):
            return "衝動型"
        if any(k in text for k in ["觀察", "注意", "判斷"]):
            return "理性型"
        if any(k in text for k in ["小心", "緩緩", "試探"]):
            return "謹慎型"
        return "中性風格"

    def detect_arc(self, text: str):
        if any(k in text for k in ["覺醒", "領悟", "突破"]):
            return "角色覺醒（成長弧）"
        if any(k in text for k in ["動搖", "崩潰", "痛苦"]):
            return "角色崩潰（低谷）"
        if any(k in text for k in ["冷靜", "堅定", "決心"]):
            return "心境穩定（成熟期）"
        return "一般敘事"

    def analyze(self, text: str):
        emotion = self.detect_emotion(text)
        motivation = self.detect_motivation(text)
        style = self.detect_behavior_style(text)
        arc = self.detect_arc(text)

        return {
            "emotion": emotion,
            "motivation": motivation,
            "behavior_style": style,
            "character_arc": arc
        }

    def character_profile(self, text: str):
        analysis = self.analyze(text)
        traits = [analysis.get("behavior_style"), analysis.get("emotion"), analysis.get("character_arc")]
        traits = [t for t in traits if t]
        return {
            "name": "未知角色",
            "traits": traits,
            "motivation": analysis.get("motivation")
        }
