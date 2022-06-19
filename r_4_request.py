import requests as rq
from requests.adapters import HTTPAdapter
from urllib3 import Retry

# Crear web session
wss = rq.Session()
retry_strategy = Retry(
            total=15,
            backoff_factor=0.1
        )
adapter = HTTPAdapter(max_retries=retry_strategy)
wss = rq.Session()
wss.mount("https://", adapter)
wss.mount("http://", adapter)

headers = dict()
headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'

resp_1 = wss.get("https://www.lider.cl/", headers=headers)

resp_2 = wss.get("https://www.lider.cl/catalogo/category/Computaci%C3%B3n/Computadores/Notebooks", headers=headers)

print(resp_2.text)

with open('salida_r_lider_notes_ie8.html', 'w', newline='', encoding="utf-8") as wfile:
    wfile.write(resp_2.text)
    wfile.close()
