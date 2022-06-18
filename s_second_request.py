
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wd = webdriver.Firefox()

wd.get("https://www.paris.cl")
wd.get("https://www.paris.cl/tecnologia/computadores/notebooks/")
print(wd.page_source)

with open('salida_s_paris_notes.html', 'w', newline='', encoding="utf-8") as wfile:
    wfile.write(wd.page_source)
    wfile.close()
