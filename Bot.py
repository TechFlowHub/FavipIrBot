from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep

class Bot: 
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-logging")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.link = "https://web.whatsapp.com/"
        
        self.main()

    def main(self):
        print("Bot Inicializado")
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.link)
        print("Waiting for you scan your QRcode")
        sleep(25)

bot = Bot()
