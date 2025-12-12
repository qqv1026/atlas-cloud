class StyleDriftController:
    def suggest(self, *, current_response, style_memory, meta):
        adjust_tone = "keep"
        adjust_length = "keep"
        risk = "low"
        if meta.get("overconfidence_check"):
            adjust_tone = "more_gentle"
        if meta.get("need_clarification"):
            adjust_tone = "more_structured"
        resp = str(current_response or "")
        if meta.get("sufficiency") == "low":
            adjust_length = "longer"
        elif len(resp) > 500:
            adjust_length = "shorter"
        preferred_tone = None
        preferred_length = None
        try:
            if hasattr(style_memory, "get"):
                preferred_tone = style_memory.get("tone")
                preferred_length = style_memory.get("length")
            elif isinstance(style_memory, dict):
                preferred_tone = style_memory.get("tone")
                preferred_length = style_memory.get("length")
        except Exception:
            preferred_tone = None
            preferred_length = None
        if adjust_tone == "keep" and preferred_tone in ["more_direct", "more_gentle", "more_structured"]:
            adjust_tone = preferred_tone
        if adjust_length == "keep" and preferred_length in ["shorter", "longer"]:
            adjust_length = preferred_length
        return {
            "adjust_tone": adjust_tone,
            "adjust_length": adjust_length,
            "risk": risk
        }
