from flask import Flask, jsonify
import json, os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POLL_FILE = os.path.join(BASE_DIR, 'api_poll', 'polls.json')
VOTE_FILE = os.path.join(BASE_DIR, 'api_vote', 'votes.json')

@app.route('/')
def index():
    return "<h1>SERVICE RESULT AMAN (PORT 5004)</h1>"

@app.route('/result/<id>', methods=['GET'])
def result(id):
    judul = "Data Poll Kosong"
    opsi = []
    if os.path.exists(POLL_FILE):
        try:
            with open(POLL_FILE) as f:
                polls = json.load(f)
                if polls: 
                    judul = polls[0]['question']
                    opsi = polls[0]['options']
        except: pass

    total = 0
    skor = {}
    if os.path.exists(VOTE_FILE):
        try:
            with open(VOTE_FILE) as f:
                votes = json.load(f)
                for v in votes:
                    if str(v.get('poll_id')) == str(id):
                        pil = str(v.get('choice'))
                        skor[pil] = skor.get(pil, 0) + 1
                        total += 1
        except: pass
    
    hasil_akhir = {}
    for i, nama in enumerate(opsi):
        hasil_akhir[nama] = skor.get(str(i), 0)

    return jsonify({"soal": judul, "total": total, "hasil": hasil_akhir})

if __name__ == '__main__':
    app.run(port=5004)