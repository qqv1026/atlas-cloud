# engine/narrative_brain_engine.py

class NarrativeBrainEngine:
    """
    敘事大腦：
    分析故事節奏、張力、伏筆、轉折、結構。
    """

    def detect_pacing(self, text: str):
        """
        根據文字判定節奏。
        """
        if any(k in text for k in ["爆", "衝", "跑", "急", "突然"]):
            return "快節奏"
        if any(k in text for k in ["沉默", "靜", "慢", "停頓"]):
            return "慢節奏"
        return "中性節奏"

    def detect_tension(self, text: str):
        """
        判定張力（緊張程度）。
        """
        if any(k in text for k in ["心跳", "緊張", "汗", "呼吸急促"]):
            return "高張力"
        if any(k in text for k in ["平靜", "冷靜", "放鬆"]):
            return "低張力"
        return "中張力"

    def detect_foreshadow(self, text: str):
        """
        偵測伏筆。
        """
        if any(k in text for k in ["奇怪", "不對勁", "像是預兆", "彷彿"]):
            return "可能的伏筆"
        return "無明顯伏筆"

    def detect_structure(self, text: str):
        """
        判斷文字屬於哪種故事段落。
        """
        if any(k in text for k in ["開始", "剛", "第一次"]):
            return "開場段落"
        if any(k in text for k in ["但", "然而", "突然"]):
            return "轉折段落"
        if any(k in text for k in ["爆發", "衝突", "高潮"]):
            return "高潮段落"
        if any(k in text for k in ["結束", "收尾", "安靜下來"]):
            return "收束段落"
        return "一般敘事段落"

    def analyze(self, text: str):
        """
        綜合敘事分析。
        """
        pacing = self.detect_pacing(text)
        tension = self.detect_tension(text)
        foreshadow = self.detect_foreshadow(text)
        structure = self.detect_structure(text)

        return {
            "pacing": pacing,
            "tension": tension,
            "foreshadow": foreshadow,
            "structure": structure
        }
