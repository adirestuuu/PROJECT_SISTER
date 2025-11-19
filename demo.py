import requests
import time
import json

# URL Service (Sesuai Port yang udah kita set)
URL_POLL = "http://localhost:5002/create_poll"
URL_VOTE = "http://localhost:5003/vote"
URL_RESULT = "http://localhost:5004/result/1"

def print_step(msg):
    print(f"\n{'='*50}\n{msg}\n{'='*50}")

# --- STEP 1: MANAJER BIKIN POLL ---
print_step("[STEP 1] Manajer login & bikin polling menu...")
payload_poll = {
    "token": "token_bos",  # Sesuai data di app_user.py
    "question": "Menu Spesial Bulan Depan?",
    "options": ["Nasi Goreng Kambing", "Sate Taichan", "Seblak Seafood"]
}

try:
    # Nembak ke API Poll (5002) -> Dia bakal nelfon API User (5001)
    resp = requests.post(URL_POLL, json=payload_poll)
    print(f"Status: {resp.status_code}")
    print("Response:", resp.json()['msg'])
except Exception as e:
    print("ERROR: Service Poll (5002) Mati!", e)
    exit()

time.sleep(2) # Jeda biar dramatis

# --- STEP 2: PARA KOKI VOTING ---
print_step("[STEP 2] 5 Kepala Koki mulai voting...")

# Simulasi 5 orang voting
# Pilihan: 0=Nasgor, 1=Sate, 2=Seblak
votes = [
    {"poll_id": 1, "choice": "0"}, # Pilih Nasgor
    {"poll_id": 1, "choice": "0"}, # Pilih Nasgor
    {"poll_id": 1, "choice": "1"}, # Pilih Sate
    {"poll_id": 1, "choice": "0"}, # Pilih Nasgor
    {"poll_id": 1, "choice": "2"}  # Pilih Seblak
]

for i, v in enumerate(votes):
    try:
        requests.post(URL_VOTE, json=v)
        print(f"- Koki Cabang {i+1} memilih opsi ke-{v['choice']}... Sukses!")
        time.sleep(0.5)
    except:
        print(f"- Koki Cabang {i+1} Gagal Vote (Service 5003 Mati)")

time.sleep(2)

# --- STEP 3: LIHAT HASIL REALTIME ---
print_step("[STEP 3] Manajer melihat rekap hasil...")

try:
    # Nembak API Result (5004) -> Dia baca file json tetangga
    resp = requests.get(URL_RESULT)
    data = resp.json()
    
    print(f"JUDUL: {data['soal']}")
    print(f"TOTAL SUARA: {data['total']}")
    print("DETAIL:")
    print(json.dumps(data['hasil'], indent=2))
    
except Exception as e:
    print("ERROR: Service Result (5004) Mati!", e)

print("\n=== DEMO SELESAI ===")