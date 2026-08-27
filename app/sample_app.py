import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://987654hv.duckdns.org"])

MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")

@app.route("/")
def home():
    return "Hello World", 200

if __name__ == "__main__":
    host = os.environ.get("FLASK_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_PORT", 5000))
    app.run(host=host, port=port, debug=False)
