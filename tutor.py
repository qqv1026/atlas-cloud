import json
from engine.atlas_cloud_brain import AtlasCloudBrain

def run_tutor(user_text: str) -> str:
    brain = AtlasCloudBrain()
    result = brain.reason(user_text)
    if isinstance(result, dict):
        return json.dumps(result, ensure_ascii=False, indent=2)
    return result
