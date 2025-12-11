from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from tutor import run_tutor
import os

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


# ➤ 提供 Cloud Tutor 前端
@app.get("/")
def serve_ui():
    if not os.path.exists(TUTOR_HTML):
        return JSONResponse({"error": "tutor.html not found"}, status_code=404)
    return FileResponse(TUTOR_HTML)


# ➤ Cloud Tutor API
@app.post("/tutor")
async def tutor_api(request: Request):
    try:
        body = await request.json()
        question = body.get("question", "").strip()

        if not question:
            return JSONResponse({"answer": "⚠️ 請輸入問題內容"}, status_code=200)

        # 執行 Tutor 腦袋
        answer = run_tutor(question)

        return JSONResponse({"answer": answer}, status_code=200)

    except Exception as e:
        return JSONResponse({"answer": f"伺服器錯誤：{str(e)}"}, status_code=500)
