
from selenium import webdriver

wd = webdriver.Firefox()

wd.get("https://www.paris.cl")
print(wd.page_source)

with open('salida_s_paris.txt', 'w', newline='', encoding="utf-8") as wfile:
    wfile.write(wd.page_source)
    wfile.close()