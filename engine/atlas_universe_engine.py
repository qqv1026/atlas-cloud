from .long_memory_cloud import CloudMemoryEngine

class AtlasUniverseEngine:
    """
    世界觀引擎：檢查世界一致性並補強世界元素，並可持久化世界相關資料。
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

    def __init__(self):
        self.cloud = CloudMemoryEngine(path="universe_memory.json")

    def train(self, text: str):
        record = {
            "text": text,
            "validation": self.validate(text),
            "enriched": self.enrich(text)
        }
        self.cloud.save(record)
        return record

    def save(self, data: dict):
        return self.cloud.save(data)

    def get_all(self):
        return self.cloud.get_all()
