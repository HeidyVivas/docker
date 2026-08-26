from flask import Flask

app = Flask(__name__)

# Vulnerabilidad intencional: credencial quemada en el código
MYSQL_PASSWORD = "super_secret_123"

@app.route("/")
def home():
    return "Hello World"

if __name__ == "__main__":
    # Vulnerabilidad intencional: debug=True en producción
    app.run(host="0.0.0.0", port=5000, debug=True)