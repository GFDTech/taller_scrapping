import requests as rq

# Crear web session
wss = rq.Session()
wss.headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'
resp = wss.get("https://www.paris.cl")

resp = wss.get("https://www.paris.cl/tecnologia/computadores/notebooks/")

print(resp.text)

with open('salida_r_paris_notes.html', 'w', newline='', encoding="utf-8") as wfile:
    wfile.write(resp.text)
    wfile.close()

'''
    self.s.cookies.set(cookie[0], cookie[1])
    self.cookies_sesion.append({'name': cookie[0], 'value': cookie[1]})



from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from requests.exceptions import Timeout, SSLError
from urllib3.exceptions import MaxRetryError
        retry_strategy = Retry(
            total=15,
            backoff_factor=0.1
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.s = requests.Session()
        self.s.mount("https://", adapter)
        self.s.mount("http://", adapter)
response = self.s.post(self.url_base + 'login.php',
                                   data={'username': self.user, 'password': self.password, 'theAction': 'user_login'},
                                   headers=self.s.headers)
                                   
           if response.status_code == 200:
                # logging.debug('[Success!] ' + response.url)
                self.login_success = True
            elif response.status_code == 404:
                self.error = 'URL no encontrada 404 :' + response.url
                raise Exception(self.error)
        except SSLError:
            self.error = 'Problema para conectarse por error SSL'
            logging.error(self.error)
        except MaxRetryError:
            self.error = 'Problema para conectarse máximo numero de intentos superado'
            raise Exception(self.error)
        except Exception:
            self.error = 'Error en request'
            raise Exception(self.error)
                  
                  timeout=2000,
                                   )
        except Timeout:
            self.error = 'Petición no responde dentro de timeout'
            raise Exception('Petición no responde dentro de timeout: ' + response.url)                 
                                   
'''
