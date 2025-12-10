from typing import Dict
from .skill_template import Skill as TemplateSkill

class SkillManagerEngine:
    def __init__(self):
        self.registry: Dict[str, object] = {}
        self.register_skill("template", TemplateSkill())

    def register_skill(self, name: str, skill: object):
        self.registry[name] = skill

    def execute_skill(self, skill_name: str, text: str):
        skill = self.registry.get(skill_name)
        if not skill or not hasattr(skill, "run"):
            return {"error": "skill_not_found", "name": skill_name}
        return {"name": skill_name, "result": skill.run(text)}
