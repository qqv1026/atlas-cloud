class MemoryDecay:
    def apply(self, memories: list) -> None:
        to_remove = []
        for m in memories:
            imp = float(m.get("importance", 0.5))
            use = int(m.get("usage_count", 0))
            if use < 2 and imp < 0.3:
                m["importance"] = max(0.0, imp - 0.05)
            if m.get("importance", 0.0) < 0.1 and use < 1:
                to_remove.append(m)
        for m in to_remove:
            try:
                memories.remove(m)
            except ValueError:
                pass
