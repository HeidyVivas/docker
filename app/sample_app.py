import os
from flask import Flask

app = Flask(__name__)

# Ahora se lee desde variable de entorno, no está en el código
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")

@app.route("/")
def home():
    return "Hello World", 200

if __name__ == "__main__":
    # debug desactivado para producción
    app.run(host="0.0.0.0", port=5000, debug=False)