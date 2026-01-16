import requests
import json

# --- CONFIGURATION ---
SENSOR_ID = 14126423
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxx"
HEADERS = {"X-API-Key": API_KEY}

def inspect_sensor():
    url = f"https://api.openaq.org/v3/sensors/{SENSOR_ID}"
    
    print(f"🕵️‍♂️ Inspection BRUTE du capteur {SENSOR_ID}...")
    
    try:
        res = requests.get(url, headers=HEADERS)
        
        if res.status_code == 200:
            data = res.json()
            # On affiche le JSON de manière lisible (indentation)
            print(json.dumps(data, indent=4))
        else:
            print(f"❌ Erreur API : {res.status_code}")
            print(res.text)

    except Exception as e:
        print(f"❌ Erreur script : {e}")

if __name__ == "__main__":
    inspect_sensor()