import json
import os

class CloudMemoryEngine:
    def __init__(self, path="cloud_memory.json"):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump({"memory": []}, f, ensure_ascii=False, indent=2)

    def load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {"memory": []}

    def save(self, data: dict):
        memory = self.load()
        memory["memory"].append(data)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(memory, f, ensure_ascii=False, indent=2)
        return {"status": "saved", "total_records": len(memory["memory"])}

    def get_all(self):
        return self.load().get("memory", [])
