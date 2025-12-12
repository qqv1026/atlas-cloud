# memory_core/memory_router.py

from .style_memory import StyleMemory
from .long_term_memory import LongTermMemory
from .memory_decay import MemoryDecay
from .memory_summary import MemorySummary

class MemoryRouter:
    """
    記憶路由器，統整所有記憶模組。
    """

    def __init__(self):
        self.style = StyleMemory()
        self.long_term = LongTermMemory()
        self.decay = MemoryDecay()
        self.summarizer = MemorySummary()

    def save_event(self, text: str):
        self.long_term.store(text)

    def _compute_importance(self, text: str, source_hint: str | None = None) -> float:
        score = 0.3
        t = (text or "").lower()
        if any(k in t for k in ["教我", "解釋", "tutor"]):
            score += 0.3
        # 重複提及
        existing = [m for m in self.long_term.get_all() if t in m.get("text", "").lower()]
        if len(existing) >= 1:
            score += 0.2
        # 來源提示
        if source_hint and any(h in source_hint for h in ["reasoning", "world", "物理", "因果", "常識"]):
            score += 0.2
        return max(0.0, min(1.0, score))

    def store(self, text: str, source_hint: str | None = None):
        importance = self._compute_importance(text, source_hint)
        entry = self.long_term.store({"text": text, "importance": importance, "usage_count": 0})
        # 容量控制與摘要
        memories = self.long_term.get_all()
        summary = ""
        if len(memories) > self.long_term.capacity:
            summary = self.summarizer.summarize(memories)
        # 衰退
        self.decay.apply(memories)
        confidence = round(min(1.0, 0.5 + importance * 0.5), 2)
        return {"memories": self.long_term.retrieve(), "summary": summary, "confidence": confidence}

    def recall(self, query: str):
        matches = self.long_term.recall(query)
        self.decay.apply(self.long_term.memories)
        summary = self.summarizer.summarize(matches or self.long_term.retrieve())
        avg_imp = 0.0
        if matches:
            avg_imp = sum(m.get("importance", 0.5) for m in matches) / max(1, len(matches))
        confidence = round(min(1.0, 0.4 + 0.3 * (len(matches) / 10.0) + 0.3 * avg_imp), 2)
        return {"memories": matches, "summary": summary, "confidence": confidence}
