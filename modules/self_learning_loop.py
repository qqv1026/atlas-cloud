class SelfLearningLoop:
    def plan(self, *, query, meta, reasoning=None, world=None):
        need = bool(meta.get("need_clarification")) or meta.get("sufficiency") == "low"
        goal = "補足理解缺口"
        state = meta.get("current_state", "general")
        if state == "explaining_world":
            goal = "理解現實規律與其背後原因"
        elif state == "reasoning":
            goal = "強化因果推理與解釋能力"
        elif state == "recalling_memory":
            goal = "梳理並統整相關關鍵資訊"
        method = "step_by_step"
        if meta.get("need_clarification"):
            method = "example"
        elif meta.get("sufficiency") == "low":
            method = "step_by_step"
        elif state == "explaining_world":
            method = "analogy"
        prompt_parts = [f"請用{('生活範例' if method=='example' else ('逐步講解' if method=='step_by_step' else '類比說明'))}方式解釋：{query}"]
        if world is not None:
            prompt_parts.append(f"並參照世界模型判斷結果：{world}")
        if reasoning is not None:
            prompt_parts.append(f"同時整合推理結論：{reasoning}")
        suggested_prompt = "；".join(prompt_parts)
        return {
            "gap_detected": need,
            "learning_goal": goal if need else "目前無需補課程",
            "recommended_method": method,
            "suggested_prompt": suggested_prompt
        }
