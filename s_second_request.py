import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

# wd = webdriver.Firefox()

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "./")
profile.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")

# Modo Headless no levanta ventana Firefox
options = Options()
options.headless = False
wd = webdriver.Firefox(firefox_profile=profile, options=options)

wd.get("https://www.lider.cl/")
wd.get("https://www.lider.cl/catalogo/category/Computaci%C3%B3n/Computadores/Notebooks")
time.sleep(20)
print(wd.page_source)

wd.execute_script("""
    (function(proxied) {
        window.alert = function() {
            console.log(arguments)
            console.log = function() {}
            try{
                var request = new XMLHttpRequest();
                url = "http://127.0.0.1:8000/logs/?m="+arguments[0]
                request.open('GET', url, true);
                // request.setRequestHeader('X-CSRFToken', csrfToken);
                request.send();
            }catch{

            }
            return proxied.apply(this, arguments);
        };
    })(window.alert);
                  """)

wd.get_full_page_screenshot_as_file('lider_screen.png')

with open('salida_s_lider_notes_2.html', 'w', newline='', encoding="utf-8") as wfile:
    wfile.write(wd.page_source)
    wfile.close()
