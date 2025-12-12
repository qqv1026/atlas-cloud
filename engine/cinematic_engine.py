# engine/cinematic_engine.py

class CinematicEngine:
    """
    電影鏡頭大腦：
    分析光影、構圖、運鏡，提供電影級分鏡語法。
    """

    def detect_lighting(self, text: str):
        """
        判斷光影氛圍。
        """
        if any(k in text for k in ["夜", "黑暗", "昏暗", "影子"]):
            return "低光源 / 高反差"
        if any(k in text for k in ["陽光", "明亮", "白天", "光線"]):
            return "高光源 / 柔光"
        if any(k in text for k in ["火光", "爆炸", "閃光"]):
            return "動態光源"
        return "自然光"

    def detect_composition(self, text: str):
        """
        判斷構圖方式。
        """
        if any(k in text for k in ["凝視", "眼", "臉"]):
            return "特寫（Close-up）"
        if any(k in text for k in ["奔跑", "跳", "衝"]):
            return "中景 / 動態構圖"
        if any(k in text for k in ["城市", "天空", "遠方"]):
            return "全景（Wide shot）"
        return "標準構圖"

    def detect_camera_motion(self, text: str):
        """
        判斷運鏡方式。
        """
        if any(k in text for k in ["奔跑", "衝", "追", "移動"]):
            return "跟拍 / 追蹤"
        if any(k in text for k in ["凝視", "站", "停"]):
            return "固定 / 靜態"
        if any(k in text for k in ["查看", "環顧", "繞", "盤旋"]):
            return "環繞 / 橫移"
        return "標準運鏡"

    def create_shot(self, text: str):
        """
        生成電影鏡頭建議。
        """
        return {
            "lighting": self.detect_lighting(text),
            "composition": self.detect_composition(text),
            "motion": self.detect_camera_motion(text)
        }

    def generate(self, text: str):
        """
        封裝生成接口，與主腦統一互動。
        """
        return self.create_shot(text)
