from flask import Flask, jsonify
import os, random, string

app = Flask(__name__)
DATA_PATH = "/data"

@app.route("/")
def home():
    return "AKS PV/PVC App Running"

@app.route("/generate")
def generate():
    os.makedirs(DATA_PATH, exist_ok=True)

    filename = "file_" + ''.join(random.choices(string.ascii_letters, k=6)) + ".txt"
    filepath = os.path.join(DATA_PATH, filename)

    with open(filepath, "w") as f:
        f.write("Random dummy file stored using AKS PV/PVC")

    return jsonify({"file": filename, "path": filepath})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
