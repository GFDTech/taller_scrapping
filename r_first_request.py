import requests as rq

resp = rq.get("https://www.lider.cl/")
# resp = rq.post("https://www.lider.cl/")
print(resp.text)

with open('salida_r_lider.txt', 'w', newline='', encoding="utf-8") as wfile:
    wfile.write(resp.text)
    wfile.close()
