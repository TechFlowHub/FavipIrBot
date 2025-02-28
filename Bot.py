from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

from database import dbConfig

class Bot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--user-data-dir=./profile")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.link = "https://web.whatsapp.com/"
        self.xpaths = {
            "unread": "/html/body/div[1]/div/div/div[3]/div/div[3]/div/div[2]/button[2]",
            "phone": "/html/body/div[1]/div/div/div[3]/div/div[4]/div/header/div[2]/div[1]/div/div/span[1]"
        }
        self._class = {
            "input_chat": "selectable-text copyable-text x15bjb6t x1n2onr6",
            "last_message": "_akbu",
            "unread_bubble": "_ahlk"
        }
        
        self.main()

    def login(self):
        print("Bot Inicializado")
        self.driver.get(self.link)
        print("Waiting for you to scan your QR code...")
        sleep(10)
        print("QR Code scanned. Keeping the session active...")

    def savingPhoneInDatabase(self):
        try:
            phone_element = self.driver.find_element(By.XPATH, self.xpaths["phone"])
            phone_number = phone_element.text
            dbConfig.insertPhone(phone_number)
            return "Phone saved"
        except Exception as e:
            print(f"Error in saving phone in db: {e}")
            return None

    def openUnread(self):
        try:
            unread_button = self.driver.find_element(By.XPATH, self.xpaths["unread"])
            unread_button.click()
            sleep(5)
            print("Unread message opened.")
        except Exception as e:
            print(f"Error in openUnread: {e}")
    
    def openUnreadMessage(self):
        try:
            unread_bubble = self.driver.find_element(By.CLASS_NAME, self._class["unread_bubble"])
            unread_bubble.click()
            sleep(5)
            print("unread_bubble cliked")
            self.savingPhoneInDatabase()
        except Exception as e:
            print(f"error in unread_bubble: {e}")

    def sendMenssage(self):
        try:
            sendMessage_v = self.driver.find_element(By.CLASS_NAME, self._class["input_chat"])
            sendMessage_v.click()
            print("menssage sent")
        except Exception as e:
            print(f"error in sendMessage: {e}")
    
    def readLastMessage(self):
        try:
            readLastMessage_v = self.driver.find_elements(By.CLASS_NAME, self._class["last_message"])
            if readLastMessage_v:
                last_element = readLastMessage_v[-1]
                last_text = last_element.text
                print(f"Last message: {last_text}")
                return last_text
            else:
                print("No elements found with the specified class.")
                return None
        except Exception as e:
            print(f"Error in getLastMessage: {e}")
            return None
        
    def main(self):
        try:
            self.login()
            self.openUnread()
            self.openUnreadMessage()
            self.readLastMessage()
            while True:
                sleep(10)
        except KeyboardInterrupt:
            print("Bot encerrado manualmente.")
        finally:
            self.driver.quit()

bot = Bot()
