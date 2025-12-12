# engine/knowledge_tree_engine.py

class KnowledgeTreeEngine:
    """
    知識樹引擎：
    將孩子學到的內容分類、建立階層、形成知識網路。
    """

    def __init__(self):
        # 主類別 → 子類別 → 概念列表
        self.tree = {
            "物理學": {},
            "故事創作": {},
            "心理與行為": {},
            "世界構造": {},
            "其他": {}
        }

    def classify(self, record):
        """
        根據關鍵詞決定知識屬於哪一類。
        """
        keywords = record.get("keywords", [])

        if any(k in keywords for k in ["物理", "能量", "力"]):
            return "物理學"
        if any(k in keywords for k in ["故事", "角色", "動作", "情節"]):
            return "故事創作"
        if any(k in keywords for k in ["情緒", "動機", "行為"]):
            return "心理與行為"
        if any(k in keywords for k in ["世界", "模型", "因果"]):
            return "世界構造"

        return "其他"

    def add_to_tree(self, category, record):
        """
        將知識加入樹狀結構
        """
        summary = record.get("summary", "")
        raw = record.get("raw", "")

        if category not in self.tree:
            self.tree[category] = {}

        if "資料" not in self.tree[category]:
            self.tree[category]["資料"] = []

        self.tree[category]["資料"].append({
            "summary": summary,
            "raw": raw
        })

    def process_record(self, record):
        """
        對外接口：讓主大腦呼叫
        """
        category = self.classify(record)
        self.add_to_tree(category, record)
        return category

    def update(self, question: str, answer: str):
        record = {
            "summary": question,
            "raw": answer,
            "keywords": []
        }
        self.add_to_tree("其他", record)
