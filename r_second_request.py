import requests as rq

# Crear web session
wss = rq.Session()

resp = wss.get("https://www.paris.cl")

resp = wss.get("https://www.paris.cl/tecnologia/computadores/notebooks/")

print(resp.text)

with open('salida_r_paris_notes.html', 'w', newline='', encoding="utf-8") as wfile:
    wfile.write(resp.text)
    wfile.close()
