from collections import Counter

class MemorySummary:
    def summarize(self, memories: list, max_tokens: int = 50) -> str:
        texts = [m.get("text", "") for m in memories if isinstance(m.get("text", ""), str)]
        if not texts:
            return ""
        tokens = []
        for t in texts:
            for w in t.lower().replace("，", " ").replace(",", " ").split():
                if len(w) > 1 and w.isalpha() or w.isalnum():
                    tokens.append(w)
        common = Counter(tokens).most_common(5)
        top_words = ", ".join([w for w, _ in common])
        return f"摘要記憶（{len(texts)}則）：主題傾向 {top_words}"
