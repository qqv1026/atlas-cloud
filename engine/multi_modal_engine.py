# engine/multi_modal_engine.py

class MultiModalEngine:
    """
    多模態整合引擎：
    讓孩子能把「語言 → 動作 → 畫面 → 故事 → 分鏡」彼此連結。
    """

    def text_to_action(self, text: str):
        """
        從文字推論動作類型（動畫/分鏡用）
        """
        if any(k in text for k in ["跑", "衝", "跳"]):
            return "動作：高速移動"
        if any(k in text for k in ["看", "望", "凝視"]):
            return "動作：視線焦點"
        if any(k in text for k in ["握", "舉", "抓"]):
            return "動作：手部動作"
        return "動作：一般行為"

    def text_to_shot(self, text: str):
        """
        從文字推論鏡頭語法（Storyboard / Sora 用）
        """
        if any(k in text for k in ["震動", "爆炸", "衝擊"]):
            return "鏡頭：低角度 + 特寫"
        if any(k in text for k in ["遠方", "城市", "天空"]):
            return "鏡頭：全景"
        if any(k in text for k in ["臉", "眼", "表情"]):
            return "鏡頭：面部特寫"
        return "鏡頭：中景"

    def text_to_emotion(self, text: str):
        """
        從對話/敘事推論感受（角色模型）
        """
        if any(k in text for k in ["怕", "緊張", "心跳"]):
            return "情緒：緊張"
        if any(k in text for k in ["怒", "憤", "咬牙"]):
            return "情緒：憤怒"
        if any(k in text for k in ["笑", "放鬆"]):
            return "情緒：放鬆"
        return "情緒：中性"

    def integrate(self, text: str):
        """
        主整合：把文字轉成行為、情緒、鏡頭建議
        """
        return {
            "action": self.text_to_action(text),
            "shot": self.text_to_shot(text),
            "emotion": self.text_to_emotion(text)
        }
