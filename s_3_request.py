from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wd = webdriver.Firefox()

wd.get("https://www.paris.cl")
# wd.implicitly_wait(10)
WebDriverWait(wd, 100000000).until(EC.presence_of_element_located((By.CLASS_NAME, 'cat-navbar'))).click()
# menu = wd.find_element(By.ID, "GTM_header_navbar")
# menu.click()


# wd.get("https://www.paris.cl/tecnologia/computadores/notebooks/")
print(wd.page_source)

with open('salida_s_paris.txt', 'w', newline='', encoding="utf-8") as wfile:
    wfile.write(wd.page_source)
    wfile.close()

'''
wd.execute_script("""
                     window.open = function(url, target) {
                        var newDiv = document.createElement("div");
                     };
                  """)
link = orden.find_element(By.TAG_NAME, 'a')
             
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", self.path_datos)
        profile.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
       
        # Modo Headless no levanta ventana Firefox
            options = Options()
            options.headless = True
            self.wd = webdriver.Firefox(firefox_profile=profile, options=options)     
            
self.wd.switch_to.frame('citeria')
            input_ape_pat = self.wd.find_element(By.ID, 'pcte_ape_pat')
            input_ape_pat.send_keys(filtro)
            self.wd.execute_script('goValidarDatos();')
            self.wd.switch_to.default_content()

self.wd.switch_to.window(self.wd.window_handles[1])
 menu = self.wd.find_element(By.XPATH, "//div[@tab_id='a0']")
 tabla_datos = solicitadas.find_element(By.CLASS_NAME, 'obj')
 rows = tabla_datos.find_elements(By.TAG_NAME, 'tr')
             

menu_ficha_demografica = self.wd.find_element(By.XPATH, "//div[@tab_id='a0']")                                     
                  
'''
