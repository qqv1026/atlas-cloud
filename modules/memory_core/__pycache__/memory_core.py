from .memory_router import MemoryRouter

class MemoryCore:
    def __init__(self, capacity: int = 100):
        self.router = MemoryRouter()

    def run(self, query: str):
        return self.router.recall(query)

    def get_context(self):
        return self.router.long_term.get_all()
