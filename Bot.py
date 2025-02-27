from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class Bot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--user-data-dir=./profile")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.link = "https://web.whatsapp.com/"
        
        self.main()

    def login(self):
        print("Bot Inicializado")
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.link)
        print("Waiting for you to scan your QR code...")
        sleep(25)

        print("QR Code scanned. Keeping the session active...")
        try:
            while True:
                sleep(10)
        except KeyboardInterrupt:
            print("Bot encerrado manualmente.")
            self.driver.quit()
    def openUnread(self):
        pass
    def main(self):
        self.login()

bot = Bot()
