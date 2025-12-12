# engine/self_learning_engine.py

class SelfLearningEngine:
    """
    自學核心：從教材中抽取知識點、摘要、關鍵詞，
    並寫入記憶系統（Memory Router）。
    """

    def extract_keywords(self, text: str):
        """
        從輸入文字中抽取基礎關鍵詞。
        """
        words = []
        vocab = [
            "物理", "重力", "力", "加速度", "能量",
            "因果", "世界", "模型",
            "故事", "角色", "動作", "情緒", "動機", "行為",
            "鏡頭", "畫面", "城市", "天空"
        ]
        for w in vocab:
            if w in text:
                words.append(w)
        return words

    def summarize(self, text: str):
        """
        粗略摘要（可持續升級）。
        """
        if len(text) < 20:
            return text  # 太短無需摘要

        return text[:30] + "..."

    def create_learning_record(self, text: str):
        """
        建立一個孩子可以儲存的學習紀錄。
        """
        return {
            "raw": text,
            "summary": self.summarize(text),
            "keywords": self.extract_keywords(text)
        }

    def think(self, query: str, memory_hint: str):
        return f"思考：{query} | 記憶提示：{memory_hint}".strip()

    def feedback(self, query: str, result: str):
        return {"status": "ok", "query": query, "result_len": len(result or "")}
