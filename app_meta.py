from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from modules.skill_router import SkillRouter
from modules.cognitive_integration import CognitiveIntegration
from modules.meta_controller import MetaController
from modules.tutor_intelligence import TutorIntelligence
from modules.style_drift_controller import StyleDriftController
from modules.reasoning_core.reasoning_engine import ReasoningEngine
from modules.world_model.world_model import WorldModel
from modules.memory_core.memory_router import MemoryRouter

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/tutor", response_class=HTMLResponse)
async def tutor_page(request: Request):
    return templates.TemplateResponse("tutor.html", {"request": request})

@app.post("/tutor")
async def tutor_api(payload: dict):
    query = payload.get("message", "").strip()

    router = SkillRouter()
    route_info = router.route(query)

    intent = route_info.get("intent") if isinstance(route_info, dict) else None
    routes = route_info.get("route", []) if isinstance(route_info, dict) else []
    confidence = route_info.get("confidence", 0.5) if isinstance(route_info, dict) else 0.5

    world_out = None
    reasoning_out = None
    memory_out = None
    used_skill = "general_response"

    if "world_model" in routes and "reasoning" in routes:
        ci = CognitiveIntegration()
        ci_result = ci.run(query)
        world_out = ci_result.get("world")
        reasoning_out = ci_result.get("reasoning")
        used_skill = "world_model+reasoning"
    else:
        if "world_model" in routes:
            world_out = WorldModel().run(query)
            used_skill = "world_model"
        if "reasoning" in routes:
            reasoning_out = ReasoningEngine().run_v2(query)
            used_skill = "reasoning_engine"
        if "memory" in routes:
            memory_out = MemoryRouter().recall(query)
            used_skill = "memory_core"

    meta = MetaController().evaluate(query=query, skill=used_skill, world=world_out, reasoning=reasoning_out, memory=memory_out)
    ti = TutorIntelligence().teach(query=query, result=(reasoning_out or world_out or memory_out or []), meta=meta)
    style = StyleDriftController().suggest(current_response=ti.get("response", ""), style_memory={}, meta=meta)

    lines = [
        f"意圖：{intent}；路由：{', '.join(routes)}；信心：{confidence}",
        f"教學模式：{ti.get('mode')}",
        ti.get("response", ""),
    ]
    if ti.get("follow_up"):
        lines.append(ti["follow_up"])

    return JSONResponse({
        "skill": "meta_controller",
        "result": lines,
        "intent": intent,
        "route": routes,
        "router_confidence": confidence,
        "meta": meta,
        "tutor": ti,
        "style_suggestion": style
    })
