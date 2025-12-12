from modules.memory_core import MemoryCore

class Memory:
    def __init__(self):
        self.core = MemoryCore()

    def run(self, query: str):
        return self.core.get_context()
