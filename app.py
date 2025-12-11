from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from tutor import run_tutor
import os, json
from modules.reasoning_core import ReasoningCore
from modules.memory_core import MemoryCore
from modules.skill_router import SkillRouter
from modules.auto_init import brain_registry

app = FastAPI()

# CORS（避免跨域錯誤）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔍 找到 static/tutor.html 的真正路徑（雲端 + 本地都能用）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TUTOR_HTML = os.path.join(STATIC_DIR, "tutor.html")
reasoning_core = ReasoningCore()
memory_core = MemoryCore()
router = SkillRouter()


# ➤ 提供 Cloud Tutor 前端
@app.get("/")
def serve_ui():
    if not os.path.exists(TUTOR_HTML):
        return JSONResponse({"error": "tutor.html not found"}, status_code=404)
    return FileResponse(TUTOR_HTML)


# ➤ Cloud Tutor API
@app.post("/tutor")
async def tutor_api(request: Request):
    body = await request.json()
    question = body.get("question", "").strip()

    memory_core.add("user", question)

    skill = router.route(question)

    engine = brain_registry.get(skill)

    if engine:
        result = engine.run(question)
    else:
        result = [f"大腦模組 '{skill}' 尚未實作"]

    return JSONResponse({
        "skill": skill,
        "result": result,
        "memory": memory_core.get_context()
    })
