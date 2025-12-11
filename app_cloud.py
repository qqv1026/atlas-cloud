# app_cloud.py
# Patch 35：Cloud API 大腦介面
import os
import openai  # 如果已經有就不用再加
openai.api_key = os.getenv("OPENAI_API_KEY")

from flask import Flask, request, jsonify, render_template
from tutor import run_tutor

def decode_unicode(obj):
    if isinstance(obj, str):
        try:
            return obj.encode().decode('unicode_escape')
        except:
            return obj
    if isinstance(obj, dict):
        return {k: decode_unicode(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [decode_unicode(v) for v in obj]
    return obj

app = Flask(__name__, template_folder="static", static_folder="static")
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# 移除重複的 /tutor POST（統一於下方版本）


@app.route("/process", methods=["GET"])
def process_get():

    query = request.args.get("query", "")
    result = brain.process(query)
    result = decode_unicode(result)
    return jsonify(result)


@app.route("/process", methods=["POST"])
def process():
    data = request.json
    query = data.get("query", "")
    result = style.process(query)
    result = decode_unicode(result)
    return jsonify(result)

@app.route("/tutor", methods=["POST"])
def tutor_api():
    """
    這個路由負責處理 POST，並回傳 JSON。
    Tutor UI 的 fetch() 就是呼叫這個。
    """
    try:
        data = request.get_json()
        user_text = data.get("text", "")

        reply = run_tutor(user_text)

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/train", methods=["POST"])
def train():
    data = request.json
    text = data.get("text", "")
    result = universe.train(text)
    result = decode_unicode(result)
    return jsonify({"status": "ok", "response": result})


@app.route("/memory", methods=["GET"])
def get_memory():
    result = brain.cloud_memory.get_all()
    result = decode_unicode(result)
    return jsonify({"cloud_memory": result})


@app.route("/memory", methods=["POST"])
def save_memory():
    data = request.json
    result = brain.cloud_memory.save(data)
    result = decode_unicode(result)
    return jsonify(result)


@app.route("/memory/get", methods=["GET"])
def get_mem():
    result = universe.get_all()
    result = decode_unicode(result)
    return jsonify({"memory": result})

@app.route("/memory/save", methods=["POST"])
def save_mem():
    data = request.json
    result = universe.save(data)
    result = decode_unicode(result)
    return jsonify({"status": "ok", "response": result})

@app.route("/tutor/page", methods=["GET"])
def tutor_page():
    return render_template("tutor.html")

@app.route("/")
def home():
    return jsonify({"status": "ATLAS Cloud is running."})


@app.route("/", methods=["GET"])
def index():
    return {
        "status": "ATLAS-Cloud AI Core Online",
        "usage": {
            "GET": "/process?query=你的問題",
            "POST": "/process",
            "body格式": {"query": "..."}
        }
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
