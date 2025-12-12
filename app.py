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
TEMPLATE_TUTOR = os.path.join(BASE_DIR, "templates", "tutor.html")
STATIC_TUTOR = TUTOR_HTML
reasoning_core = ReasoningCore()
memory_core = MemoryCore()
router = SkillRouter()

# ➤ 提供 Cloud Tutor 前端（新增 GET /tutor）
@app.get("/tutor")
def tutor_page():
    if os.path.exists(TEMPLATE_TUTOR):
        return FileResponse(TEMPLATE_TUTOR)
    elif os.path.exists(STATIC_TUTOR):
        return FileResponse(STATIC_TUTOR)
    return JSONResponse({"error": "tutor.html not found"}, status_code=404)

def run_tutor_pipeline(question: str):
    text = question.strip()
    if not text:
        return {"skill": "unknown", "result": []}
    return {"skill": "router", "result": [f"【孩子回應中】你剛剛說的是：{text}"]}

# ➤ Cloud Tutor API（容忍多種鍵名）
@app.post("/tutor")
async def tutor_api(request: Request):
    data = await request.json()
    user_text = (
        data.get("question")
        or data.get("message")
        or data.get("text")
        or ""
    ).strip()

    if not user_text:
        return JSONResponse({"error": "empty input"}, status_code=400)
    result = run_tutor_pipeline(user_text)
    return {
        "skill": result.get("skill", "unknown"),
        "result": result.get("result", [])
    }
