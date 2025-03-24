from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/chess/get-move")
def get_move():
  return jsonify({ "message": "Hello, World! From Flask..." })
