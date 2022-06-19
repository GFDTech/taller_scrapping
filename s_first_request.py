import time

from selenium import webdriver

wd = webdriver.Firefox()

wd.get("https://www.lider.cl/")
time.sleep(10)
print(wd.page_source)

with open('salida_s_lider.txt', 'w', newline='', encoding="utf-8") as wfile:
    wfile.write(wd.page_source)
    wfile.close()
