import json
import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/json")
def json_app():
    file_path = "dummy.json"
    if not os.path.exists(file_path):
        return jsonify({"error": f"{file_path} not found"}), 404

    with open(file_path, "r") as file:
        data = json.load(file)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
