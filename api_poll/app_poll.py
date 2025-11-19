from flask import Flask, request, jsonify
import requests, json, os

app = Flask(__name__)
FILE_DB = 'polls.json'

@app.route('/')
def index():
    return "<h1>SERVICE POLL AMAN (PORT 5002)</h1>"

@app.route('/create_poll', methods=['POST'])
def create():
    data = request.json
    
    try:
        res = requests.post('http://localhost:5001/validate', json={'token': data.get('token')})
        if res.status_code != 200: return jsonify({"msg": "Token Ditolak Satpam"}), 401
    except:
        return jsonify({"msg": "Service User Mati/Gak Nyambung"}), 500

    creator = res.json()['user']
    poll = {
        "id": 1, 
        "creator": creator,
        "question": data.get('question'), 
        "options": data.get('options')
    }
    
    with open(FILE_DB, 'w') as f: json.dump([poll], f)
    return jsonify({"msg": "Poll Sukses Dibuat", "data": poll}), 201

if __name__ == '__main__':
    if not os.path.exists(FILE_DB):
        with open(FILE_DB, 'w') as f: json.dump([], f)
    app.run(port=5002)