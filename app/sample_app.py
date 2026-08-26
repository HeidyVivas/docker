MYSQL_PASSWORD = "super_secret_123"

from flask import Flask
from flask import request
from flask import render_template
sample = Flask (__name__)
@sample .route ("/")
def main():
 return render_template ("index.html"), 500
if __name__ == "__main__":
 sample.run(host="0.0.0.0", port=5050, debug=True)  # nosec B104
