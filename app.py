from flask import Flask, render_template, request, jsonify
from main import AtlasCloudBrain

app = Flask(__name__)
brain = AtlasCloudBrain()


@app.route("/")
def index():
    return render_template("academy.html")


@app.route("/teach", methods=["POST"])
def teach():
    data = request.json
    query = data.get("query", "")

    output = brain.process(query)

    return jsonify(output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
