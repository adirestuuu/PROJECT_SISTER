from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
FILE_DB = 'votes.json'

@app.route('/')
def index():
    return "<h1>SERVICE VOTE AMAN (PORT 5003)</h1>"

@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    
    votes = []
    if os.path.exists(FILE_DB):
        with open(FILE_DB, 'r') as f:
            try: votes = json.load(f)
            except: pass
    
    votes.append(data)
    
    with open(FILE_DB, 'w') as f: json.dump(votes, f)
    return jsonify({"msg": "Suara Masuk"}), 201

if __name__ == '__main__':
    if not os.path.exists(FILE_DB):
        with open(FILE_DB, 'w') as f: json.dump([], f)
    app.run(port=5003)