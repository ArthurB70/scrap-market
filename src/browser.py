from selenium import webdriver
from webdriver_manager.firefox import GeckoDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep
import logging

logger = logging.getLogger('log_application.browser')

class Browser:
    def __init__(self, config):        
        options = Options()
        #options.add_argument("-headless")
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.dir", config.path.download_default)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

        self.browser = webdriver.Firefox(options=options)
        self.browser.maximize_window()
    def BrowseUrl(self, url):
        try:
            self.browser.get(url)
        except:
            print(f"Erro ao acessar url: {url}")
            logger.warning(f"Erro ao acessar url: {url}")

    def WaitAndClickElement(self, xpath, element, time=5, time_sleep=0.25):
        try:
            WebDriverWait(self.browser,time).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath))).click()
            sleep(time_sleep)
        except:
            print(f"Erro ao clicar no elemento: {element}")
            logger.warning(f"Erro ao clicar no elemento: {element}")

    def WaitAndSendKeysElement(self, xpath, value, element, time=5, time_sleep=0.25):
        try:
            WebDriverWait(self.browser,time).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath))).send_keys(value)
            sleep(time_sleep)
        except:
            print(f"Erro ao preencher elemento: {element}")
            logger.warning(f"Erro ao preencher elemento: {element}")
    
    def FindTextElement(self, xpath, value, element):
        try:
            text = WebDriverWait(self.browser,5).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath))).text
            if(value in text):
                return True, text
            return False, ""
        except:
            print(f"Erro ao procurar texto: {element}")
            logger.warning(f"Erro ao procurar texto: {element}")
    
    def CloseBrowser(self):
        try:
            self.browser.quit()
        except:
            print("Erro ao tentar fechar o navegador!")
            logger.warning("Erro ao tentar fechar o navegador!")
    
    def FindElements(self, xpath, element):
        try:
            return self.browser.find_elements(By.XPATH, xpath)
        except:
            print(f"Erro ao procurar elemento: {element}")
            logger.warning(f"Erro ao procurar elemento: {element}")
    
    def WaitFindElement(self, xpath, element):
        try:
            element = WebDriverWait(self.browser,5).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return True, element
        except:
            print(f"Erro ao procurar elemento: {element}")
            logger.warning(f"Erro ao procurar elemento: {element}")
            return False, None
            