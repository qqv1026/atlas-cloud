# memory_core/long_term_memory.py

from typing import List, Dict, Any


class LongTermMemory:
    """
    長期記憶：帶有 importance 與 usage_count 的結構化記憶。
    """

    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        self.memories: List[Dict[str, Any]] = []

    def _normalize_item(self, item: Any, importance: float | None = None) -> Dict[str, Any]:
        if isinstance(item, dict):
            text = item.get("text") or item.get("raw") or str(item)
            imp = item.get("importance", importance if importance is not None else 0.5)
        else:
            text = str(item)
            imp = importance if importance is not None else 0.5
        return {
            "text": text,
            "importance": max(0.0, min(1.0, float(imp))),
            "usage_count": int(item.get("usage_count", 0)) if isinstance(item, dict) else 0,
        }

    def store(self, item: Any, importance: float | None = None) -> Dict[str, Any]:
        entry = self._normalize_item(item, importance)
        self.memories.append(entry)
        return entry

    def retrieve(self, limit: int = 10) -> List[Dict[str, Any]]:
        return self.memories[-limit:] if self.memories else []

    def recall(self, query: str) -> List[Dict[str, Any]]:
        results = []
        q = (query or "").strip()
        for m in self.memories:
            if not q or (q in m.get("text", "")):
                m["usage_count"] = m.get("usage_count", 0) + 1
                results.append(m)
        return results

    def get_all(self) -> List[Dict[str, Any]]:
        return list(self.memories)
