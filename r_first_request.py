import requests as rq

resp = rq.get("https://www.paris.cl")
print(resp.text)

with open('salida_r_paris.txt', 'w', newline='', encoding="utf-8") as wfile:
    wfile.write(resp.text)
    wfile.close()
