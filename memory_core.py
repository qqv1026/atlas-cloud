"""
Memory Core v1 — 工作記憶（短期上下文）
• 維持最近 10 則訊息
• Skill Router 與 Tutor API 必備
"""

class MemoryCore:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.memory = []

    def add(self, role: str, content: str):
        item = {"role": role, "content": content}

        self.memory.append(item)

        if len(self.memory) > self.capacity:
            self.memory.pop(0)

    def clear(self):
        self.memory = []

    def get_context(self):
        return self.memory

    def run(self):
        return {
            "type": "memory_context",
            "messages": self.memory
        }

    def recall(self, query: str):
        for item in reversed(self.memory):
            if query and (query in item.get("content", "")):
                return item
        return {}

    def get_all(self):
        return self.memory

    def run(self, query: str):
        return self.get_all()
