# engine/long_memory_cloud.py

import json
import os

class CloudMemoryEngine:
    """
    雲端長期記憶：
    - 將孩子的重要學習紀錄/世界觀/角色資料永久保存
    - 重啟後可重新載入
    """

    def __init__(self, path="cloud_memory.json"):
        self.path = path

        # 若檔案不存在則建立空記憶
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump({"memory": []}, f, ensure_ascii=False, indent=2)

    def load(self):
        """載入雲端記憶"""
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {"memory": []}

    def save(self, data: dict):
        """存入雲端記憶（追加式）"""
        memory = self.load()
        memory["memory"].append(data)

        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(memory, f, ensure_ascii=False, indent=2)

        return {"status": "saved", "total_records": len(memory["memory"])}

    def get_all(self):
        """取得所有長期記憶"""
        return self.load().get("memory", [])

