# memory_core/long_term_memory.py

class LongTermMemory:
    """
    知識性長期記憶（可擴展為 JSON 保存與載入）
    """

    def __init__(self):
        self.knowledge = []

    def store(self, text: str):
        self.knowledge.append(text)

    def retrieve(self):
        return self.knowledge[-5:]  # 取最近 5 筆
