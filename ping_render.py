import time
import requests
import random
from datetime import datetime

URL = "https://ticker-fullstack.onrender.com/"  # Altere para sua URL se necessário

while True:
    try:
        response = requests.get(URL)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] Ping: {response.status_code}")
    except Exception as e:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] Erro ao pingar: {e}")
    intervalo = random.randint(480, 720)  # entre 8 e 12 minutos
    print(f"Próximo ping em {intervalo // 60} min")
    time.sleep(intervalo)
