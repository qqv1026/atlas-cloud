# engine/concept_graph_engine.py

class ConceptGraphEngine:
    """
    概念網路引擎：
    建立節點（概念）、連結（概念之間的關係）、強度（學習次數）。
    """

    def __init__(self):
        # graph = { 概念: { 相關概念: 強度 } }
        self.graph = {}

    def add_concept(self, concept: str):
        """
        如果節點不存在，建立新節點。
        """
        if concept not in self.graph:
            self.graph[concept] = {}

    def link(self, a: str, b: str):
        """
        建立概念 a ↔ b 的雙向連結，並提升關係強度。
        """
        self.add_concept(a)
        self.add_concept(b)

        # a → b
        self.graph[a][b] = self.graph[a].get(b, 0) + 1

        # b → a
        self.graph[b][a] = self.graph[b].get(a, 0) + 1

    def process_keywords(self, keywords: list):
        """
        讓一組關鍵詞互相連結，形成網路。
        """
        if not keywords:
            return

        for i in range(len(keywords)):
            for j in range(i + 1, len(keywords)):
                self.link(keywords[i], keywords[j])

    def get_related(self, concept: str):
        """
        取得某概念的相關概念。
        """
        return self.graph.get(concept, {})

    def generate(self, text: str):
        """
        生成概念網路輸出：對輸入文字抽關鍵詞並建立連結，回傳子圖。
        """
        try:
            from engine.self_learning_engine import SelfLearningEngine
            sle = SelfLearningEngine()
            keywords = sle.extract_keywords(text)
        except Exception:
            keywords = []

        self.process_keywords(keywords)

        subgraph = {k: self.graph.get(k, {}) for k in keywords}
        return {"keywords": keywords, "graph": subgraph or self.graph}
