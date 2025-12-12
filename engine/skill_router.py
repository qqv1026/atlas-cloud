# engine/skill_router.py
# ATLAS Skill Router v1 — 技能選擇中樞

from typing import Dict


class SkillRouter:
    """
    根據問題語意，選擇最適合的技能模組。
    """

    def __init__(self):
        # 技能關鍵字對應表
        self.rules: Dict[str, list] = {
            "style": ["語氣", "風格", "tone", "文風", "寫法"],
            "universe": ["世界觀", "世界", "宇宙", "設定", "universe"],
            "cinematic": ["分鏡", "鏡頭", "shot", "camera", "cut", "剪輯"],
            "emotion": ["情緒", "心情", "角色情緒"],
            "character": ["角色", "人設", "人物性格"],
            "concept": ["概念", "架構", "結構", "graph"],
            "memory": ["記住", "記憶", "學會", "store", "recall"],
            "general": []  # fallback
        }

    def match(self, query: str) -> str:
        q = query.lower()

        for skill, keywords in self.rules.items():
            if any(k.lower() in q for k in keywords):
                return skill

        return "general"
