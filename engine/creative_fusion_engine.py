# engine/creative_fusion_engine.py

class CreativeFusionEngine:
    """
    創作者融合核心：
    把「鏡頭」「動作」「情緒」「物理」「敘事」整合為單一創作輸出。
    """

    def fuse(self, multi_modal: dict, action_physics: dict, intent: str, reasoning: str):
        """
        接收來自主大腦的各種子輸出，
        將它們融合成一組創作建議。
        """

        shot = multi_modal.get("shot", "中景")
        action = multi_modal.get("action", "一般行為")
        emotion = multi_modal.get("emotion", "中性")

        action_type = action_physics.get("action_type", "一般動作")
        force_level = action_physics.get("force_level", 0)
        physics_effect = action_physics.get("physics_effect", "無明顯物理效果")

        return {
            "fused_shot": shot,
            "fused_action": action,
            "fused_emotion": emotion,
            "fused_action_type": action_type,
            "fused_force_level": force_level,
            "fused_physics_effect": physics_effect,
            "reasoning_used": reasoning,
            "intent_used": intent,
        }

    def create_storybeat(self, fused: dict):
        """
        根據融合結果產生「故事節奏點」建議（story beat）。
        """

        force = fused.get("fused_force_level", 0)
        emotion = fused.get("fused_emotion", "中性")
        shot = fused.get("fused_shot", "中景")

        beat = ""

        if force >= 4:
            beat += "節奏：強衝擊場面，需要快速剪輯 + 低角度。\n"
        elif force == 3:
            beat += "節奏：動作強烈，中景或移動跟拍。\n"
        elif force == 2:
            beat += "節奏：自然過渡，可加入中景敘事鏡頭。\n"
        else:
            beat += "節奏：平穩，適合角色互動或情緒鋪陳。\n"

        beat += f"鏡頭：建議使用 {shot} 來呈現。\n"
        beat += f"情緒：角色情緒呈現為 {emotion}。\n"

        return beat
