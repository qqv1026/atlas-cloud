class AtlasUniverseEngine:
    """
    世界觀引擎：檢查世界一致性並補強世界元素。
    """

    def validate(self, text: str):
        if any(k in text for k in ["水往上流", "太陽掉下來"]):
            return "世界觀不一致"
        return "世界觀合理"

    def enrich(self, text: str):
        return {
            "setting": "地球 / 現代",
            "physics": "牛頓力學近似",
            "theme": "探索因果",
        }
