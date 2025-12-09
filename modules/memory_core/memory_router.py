# memory_core/memory_router.py

from .style_memory import StyleMemory
from .long_term_memory import LongTermMemory

class MemoryRouter:
    """
    記憶路由器，統整所有記憶模組。
    """

    def __init__(self):
        self.style = StyleMemory()
        self.long_term = LongTermMemory()

    def save_event(self, text: str):
        self.long_term.store(text)
