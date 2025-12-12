# ATLAS Cloud Brain v3
# 主腦整合：負責推理、記憶、技能管理、回答整合
import json

from engine.long_memory_cloud import CloudMemoryEngine
from engine.knowledge_tree_engine import KnowledgeTreeEngine
from engine.self_learning_engine import SelfLearningEngine
from engine.style_engine import StyleEngine
from engine.atlas_universe_engine import AtlasUniverseEngine
from engine.skill_manager_engine import SkillManagerEngine
from engine.skill_router import SkillRouter


class AtlasCloudBrain:
    def __init__(self):
        # 記憶模組
        self.memory = CloudMemoryEngine()
        self.knowledge = KnowledgeTreeEngine()

        # 推理 / 學習模組
        self.self_learning = SelfLearningEngine()

        # 技能模組
        self.style = StyleEngine()
        self.universe = AtlasUniverseEngine()
        self.skills = SkillManagerEngine()
        self.router = SkillRouter()

    # -----------------------------
    # ① 主推理路徑
    # -----------------------------
    def reason(self, query: str) -> str:
        """
        主推理流程：
        1. 讀取記憶
        2. 理解語意
        3. 選擇技能
        4. 執行技能
        5. 儲存新記憶
        """

        # Step 1 — 記憶參考
        memory_hint = self.memory.recall(query)

        # Step 2 — 語意推理
        thinking = self.self_learning.think(query, memory_hint)

        # Step 3 — 技能選擇
        skill_name = self.router.match(query)

        # Step 4 — 技能執行
        if skill_name == "style":
            result = self.style.process(query)
        elif skill_name == "universe":
            result = self.universe.train(query)
        elif skill_name == "cinematic":
            from engine.cinematic_engine import CinematicEngine
            ce = CinematicEngine()
            result = ce.generate(query)
        elif skill_name == "emotion":
            from engine.emotion_character_engine import EmotionCharacterEngine
            emo = EmotionCharacterEngine()
            result = emo.analyze(query)
        elif skill_name == "character":
            from engine.emotion_character_engine import EmotionCharacterEngine
            emo = EmotionCharacterEngine()
            result = emo.character_profile(query)
        elif skill_name == "concept":
            from engine.concept_graph_engine import ConceptGraphEngine
            cg = ConceptGraphEngine()
            result = cg.generate(query)
        else:
            result = self.style.process(query)  # fallback

        # Step 5 — 儲存學習結果
        self.memory.store({"query": query, "result": result})
        self.knowledge.update(query, result)
        self.self_learning.feedback(query, result)

        return result

    # -----------------------------
    # ② Tutor 專用回答（簡化）
    # -----------------------------
    def tutor_answer(self, question: str) -> dict:
        answer = self.reason(question)
        if isinstance(answer, dict):
            answer = json.dumps(answer, ensure_ascii=False, indent=2)
        return {
            "role": "tutor",
            "question": question,
            "answer": answer
        }
