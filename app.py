from flask import Flask
import os
import uuid

app = Flask(__name__)

DATA_DIR = "/data"

@app.route("/")
def home():
    filename = f"file_{uuid.uuid4().hex}.txt"
    filepath = os.path.join(DATA_DIR, filename)

    with open(filepath, "w") as f:
        f.write("This is a dummy generated file.\n")

    return f"File created: {filename}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
