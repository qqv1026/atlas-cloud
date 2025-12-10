# engine/skill_template.py

class Skill:
    """
    技能模板：
    所有技能 engine/skill_xxx.py 都用這個格式。
    """

    def run(self, text: str):
        return "這是技能模板（請自行擴展 run()）。"
