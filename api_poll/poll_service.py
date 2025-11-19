import json

DB_FILE = 'api_poll/database/polls.json'

def get_all_polls_logic():
    """
    membaca semua isinya
    """
    try:
        with open(DB_FILE, 'r') as f:
            # mengubah teks JSON menjadi array python
            return json.load(f)
    except FileNotFoundError:
        return []

def create_poll_logic(new_poll_data):
    """
    menambahkan data polling baru ke polls.json
    """
    # membaca semua data yang ada
    db = get_all_polls_logic()
    
    # membuat ID baru dengan mengambil ID terakhir + 1, atau mulai dari 1
    new_id = 1
    if db: # cek database kosong atau tidak
        new_id = db[-1]['id'] + 1
    
    # melengkapi data baru dengan id
    new_poll_data['id'] = new_id
    
    # menambahkan data baru ke daftar
    db.append(new_poll_data)
    
    # menulis ulang semua data ke file polls.json
    with open(DB_FILE, 'w') as f:
        # mengubah array menjadi teks JSON
        json.dump(db, f, indent=4)
    
    # mengembalikan data yang sudah lengkap
    return new_poll_data