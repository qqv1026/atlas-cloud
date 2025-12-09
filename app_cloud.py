# app_cloud.py
# Patch 35：Cloud API 大腦介面

from flask import Flask, request, jsonify
from main import AtlasCloudBrain

app = Flask(__name__)
brain = AtlasCloudBrain()


@app.route("/process", methods=["GET"])
def process_get():
    query = request.args.get("query", "")
    result = brain.process(query)
    return jsonify(result)


@app.route("/process", methods=["POST"])
def process_post():
    data = request.json
    query = data.get("query", "")
    result = brain.process(query)
    return jsonify(result)


@app.route("/train", methods=["POST"])
def train():
    data = request.json
    lesson = data.get("lesson", "")
    result = brain.train(lesson)
    return jsonify(result)


@app.route("/memory", methods=["GET"])
def get_memory():
    result = brain.cloud_memory.get_all()
    return jsonify({"cloud_memory": result})


@app.route("/memory", methods=["POST"])
def save_memory():
    data = request.json
    result = brain.cloud_memory.save(data)
    return jsonify(result)


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
    app.run(host="0.0.0.0", port=7000, debug=True)
