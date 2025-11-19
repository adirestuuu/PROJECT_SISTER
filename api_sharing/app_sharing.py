from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>SERVICE SHARING AMAN (PORT 5005)</h1>"

@app.route('/generate_link', methods=['POST'])
def generate_link():
    data = request.json
    poll_id = data.get('poll_id')
    
    if not poll_id:
        return jsonify({"msg": "Mana ID Poll-nya?"}), 400
    
    unique_link = f"http://localhost:5000/koki?vote_id={poll_id}&source=share_wa"
    
    return jsonify({
        "poll_id": poll_id,
        "platform": "WhatsApp/Email",
        "link_hasil": unique_link
    }), 200

if __name__ == '__main__':
    app.run(port=5005)