from flask import Flask, jsonify
import sys
from flask_app.src.endpoints.wol import wol

app = Flask(__name__)

app.register_blueprint(wol)

if __name__ == "__main__":
    app.run(debug=True)