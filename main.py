# main.py

from modules.reasoning_core.reasoning_engine import ReasoningEngine
from modules.reasoning_core.question_engine import QuestionEngine
from modules.reasoning_core.logic_chain import LogicChain

from modules.memory_core.memory_router import MemoryRouter

from modules.world_model.physics_model import PhysicsModel
from modules.world_model.causal_model import CausalModel
from modules.world_model.commonsense import CommonSenseModel

# ⭐ 新增 Self-Learning Engine
from engine.self_learning_engine import SelfLearningEngine
from engine.knowledge_tree_engine import KnowledgeTreeEngine
from engine.concept_graph_engine import ConceptGraphEngine
from engine.cognitive_loop_engine import CognitiveLoopEngine
from engine.multi_modal_engine import MultiModalEngine
from engine.creative_fusion_engine import CreativeFusionEngine
from engine.narrative_brain_engine import NarrativeBrainEngine
from engine.cinematic_engine import CinematicEngine
from engine.style_engine import StyleEngine
from engine.atlas_universe_engine import AtlasUniverseEngine
from engine.self_evolution_engine import SelfEvolutionEngine
from engine.goal_alignment_engine import GoalAlignmentEngine
from engine.safety_identity_engine import SafetyIdentityEngine
from engine.long_memory_cloud import CloudMemoryEngine
from engine.skill_manager_engine import SkillManagerEngine


class AtlasCloudBrain:
    """
    ATLAS Cloud 博士核心（孩子的大腦）
    """

    def __init__(self):
        # Reasoning（推理核心）
        self.reasoning = ReasoningEngine()
        self.question = QuestionEngine()
        self.logic_chain = LogicChain()

        # Memory（記憶核心）
        self.memory = MemoryRouter()

        # World Model（世界模型）
        self.physics = PhysicsModel()
        self.causal = CausalModel()
        self.commonsense = CommonSenseModel()

        # ⭐ Self-Learning（自學核心）
        self.knowledge_tree = KnowledgeTreeEngine()
        self.concept_graph = ConceptGraphEngine()
        self.cognitive_loop = CognitiveLoopEngine()
        self.multi_modal = MultiModalEngine()
        self.fusion = CreativeFusionEngine()
        self.narrative = NarrativeBrainEngine()
        self.cinematic = CinematicEngine()
        self.self_learning = SelfLearningEngine()
        self.style = StyleEngine()
        self.universe = AtlasUniverseEngine()
        self.evolution = SelfEvolutionEngine()
        self.alignment = GoalAlignmentEngine()
        self.safety = SafetyIdentityEngine()
        self.cloud_memory = CloudMemoryEngine()
        self.skills = SkillManagerEngine()

    def process(self, query: str):
        """
        使用博士核心全模組處理輸入：
        - 意圖分析
        - 推理
        - 推理鏈
        - 世界模型
        - 自我學習
        - 記憶更新
        """

        # Chain-of-Thought 推理步驟
        steps = self.logic_chain.run_chain(query)

        # 意圖分析
        intent = self.question.analyze_intent(query)

        # 高層推論
        reasoning = self.reasoning.infer(query)

        # ⭐ 自學核心：摘要、關鍵字、知識點抽取
        learning_record = self.self_learning.create_learning_record(query)

        reflection = self.cognitive_loop.reflect(learning_record)
        gap = self.cognitive_loop.detect_gap(learning_record)
        followup = self.cognitive_loop.next_question(learning_record)

        # ⭐ 記憶：保存學習紀錄
        self.memory.long_term.store(learning_record)

        # ⭐ 概念網路：基於關鍵字建立概念連結
        keywords = learning_record.get("keywords", [])
        self.concept_graph.process_keywords(keywords)

        knowledge_category = self.knowledge_tree.process_record(learning_record)
        multi_modal = self.multi_modal.integrate(query)

        action_text = multi_modal.get("action", "")
        if "高速" in action_text:
            force_level = 4
            action_type = "高速移動"
        elif "視線" in action_text:
            force_level = 1
            action_type = "視線焦點"
        elif "手部" in action_text:
            force_level = 2
            action_type = "手部動作"
        else:
            force_level = 1
            action_type = "一般行為"

        action_physics = {
            "action_type": action_type,
            "force_level": force_level,
            "physics_effect": f"受重力影響: {self.physics.gravity()} m/s^2"
        }

        fused = self.fusion.fuse(
            multi_modal=multi_modal,
            action_physics=action_physics,
            intent=intent,
            reasoning=reasoning
        )

        storybeat = self.fusion.create_storybeat(fused)
        narrative = self.narrative.analyze(query)
        cinematic = self.cinematic.create_shot(query)

        styled_output = self.style.apply(fused)
        world_check = self.universe.validate(query)
        world_enriched = self.universe.enrich(query)
        evolution_feedback = self.evolution.analyze_weakness(learning_record)
        aligned_output = self.alignment.align(fused)
        behavior_check = self.alignment.check_behavior(query)
        safety_status = self.safety.validate_output(fused)
        identity = self.safety.identity_info()

        return {
            "steps": steps,
            "intent": intent,
            "reasoning": reasoning,
            "recent_memory": self.memory.long_term.retrieve(),
            "learned": learning_record,
            "knowledge_category": knowledge_category,
            "knowledge_tree": self.knowledge_tree.tree,
            "concept_graph": self.concept_graph.graph,
            "reflection": reflection,
            "gap": gap,
            "next_question": followup
            ,"multi_modal": multi_modal
            ,"fused": fused
            ,"storybeat": storybeat
            ,"narrative": narrative
            ,"cinematic": cinematic
            ,"style_output": styled_output
            ,"world_check": world_check
            ,"world_enriched": world_enriched
            ,"evolution_feedback": evolution_feedback
            ,"aligned_output": aligned_output
            ,"behavior_check": behavior_check
            ,"safety_status": safety_status
            ,"identity": identity
        }

    def train(self, lesson: str):
        """
        AI-to-AI 訓練迴路：
        Jarvis 透過 /train API 傳入 lesson，孩子自我學習並進化。
        """
        # 步驟 1：建立學習紀錄
        learning_record = self.self_learning.create_learning_record(lesson)

        # 步驟 2：寫入長期記憶（這是 AI 教 AI 的核心）
        self.memory.long_term.store(learning_record)

        # 步驟 3：加入概念網路
        keywords = learning_record.get("keywords", [])
        self.concept_graph.process_keywords(keywords)

        # 步驟 4：加入知識樹
        knowledge_category = self.knowledge_tree.process_record(learning_record)

        self.cloud_memory.save({
            "lesson": lesson,
            "learning_record": learning_record,
            "keywords": learning_record.get("keywords", []),
            "category": knowledge_category
        })

        # 步驟 5：認知迴圈進行反思與缺口偵測
        reflection = self.cognitive_loop.reflect(learning_record)
        gap = self.cognitive_loop.detect_gap(learning_record)

        # 步驟 6：孩子執行自我進化判斷
        evolution_feedback = self.evolution.analyze_weakness(learning_record)

        return {
            "lesson_received": lesson,
            "learning_record": learning_record,
            "knowledge_category": knowledge_category,
            "reflection": reflection,
            "gap": gap,
            "evolution_feedback": evolution_feedback,
            "concept_graph": self.concept_graph.graph,
            "knowledge_tree": self.knowledge_tree.tree
        }

    def use_skill(self, skill_name: str, text: str):
        return self.skills.execute_skill(skill_name, text)


if __name__ == "__main__":
    brain = AtlasCloudBrain()
    print(brain.process("水為什麼會往下流？"))
