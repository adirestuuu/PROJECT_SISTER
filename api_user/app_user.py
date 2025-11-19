from flask import Flask, request, jsonify

app = Flask(__name__)

USERS = {
    "token_bos": "Pak Manajer",
    "token_koki": "Koki Cabang"
}

@app.route('/')
def index():
    return "<h1>SERVICE USER AMAN (PORT 5001)</h1>"

@app.route('/validate', methods=['POST'])
def validate():
    token = request.json.get('token')
    if token in USERS:
        return jsonify({"valid": True, "user": USERS[token]}), 200
    return jsonify({"valid": False}), 401

if __name__ == '__main__':
    app.run(port=5001)