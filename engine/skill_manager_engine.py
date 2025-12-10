from typing import Dict
from .skill_template import Skill as TemplateSkill
from .style_engine import StyleEngine
from .atlas_universe_engine import AtlasUniverseEngine

class SkillManagerEngine:
    def __init__(self):
        self.registry: Dict[str, object] = {}

        # 登錄所有技能（避免找不到技能）
        self.register_skill("template", TemplateSkill())
        self.register_skill("style", StyleEngine())
        self.register_skill("universe", AtlasUniverseEngine())

    def register_skill(self, name: str, skill: object):
        self.registry[name] = skill

    def execute_skill(self, skill_name: str, text: str):
        skill = self.registry.get(skill_name)
        if not skill or not hasattr(skill, "run"):
            return {"error": "skill_not_found", "name": skill_name}
        return {"name": skill_name, "result": skill.run(text)}

    def match_skill(self, query: str) -> str:
        q = query.lower()

        # 語氣與寫作風格類
        if any(k in q for k in ["tone", "語氣", "風格", "寫法"]):
            return "style"

        # 世界模型、世界觀詢問
        if any(k in q for k in ["世界", "模型", "設定", "universe"]):
            return "universe"

        # 一般問答 → template（OpenAI 處理）
        return "template"
