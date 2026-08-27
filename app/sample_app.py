import os
from flask import Flask

app = Flask(__name__)

# Ahora se lee desde variable de entorno, no está quemada en el código
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")

@app.route("/")
def home():
    return "Hello World", 200

if __name__ == "__main__":
    host = os.environ.get("FLASK_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_PORT", 5000))
    app.run(host=host, port=port, debug=False)