import os
from flask import Flask, send_from_directory, redirect

app = Flask(__name__, static_folder=None)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.get("/success")
@app.get("/success.html")
def success():
    return send_from_directory(BASE_DIR, "success.html")

@app.get("/failed")
@app.get("/failed.html")
def failed():
    return send_from_directory(BASE_DIR, "failed.html")

@app.get("/style.css")
def stylesheet():
    return send_from_directory(BASE_DIR, "style.css", mimetype="text/css")

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
