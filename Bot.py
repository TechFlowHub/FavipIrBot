from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests

from database import dbConfig
import Menus
import Questions

import requests

from io import BytesIO
from PIL import Image
import pyzbar.pyzbar as pyzbar
import numpy as np
import qrcode_terminal

def sendResponseWithChatGpt(last_text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    calibration_prompts = [
        {
            "role": "system",
            "content": (
                "Você é um bot especializado em contabilidade. Responda apenas perguntas relacionadas a contabilidade. "
                "Se a pergunta não estiver dentro deste escopo, responda com: "
                "'Sou um bot auxiliar de contabilidade. Me pergunte apenas coisas do meu escopo.'"
                "lembre-se que todas as perguntas são relacionadas ao país BRASIL, responda sempre em português brasileiro, tente ser o maximo possivel amigavel para leigos no assunto e use emojis com moderação"
            )
        }
    ]
    
    user_message = {
        "role": "user",
        "content": last_text
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": calibration_prompts + [user_message]
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()

        if "choices" in response_data and len(response_data["choices"]) > 0:
            return response_data["choices"][0]["message"]["content"]
        else:
            return "Não foi possível processar a resposta."
    except requests.exceptions.RequestException as e:
        return f"Erro ao fazer a requisição: {e}"

    
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
            "phone": "/html/body/div[1]/div/div/div[3]/div/div[4]/div/header/div[2]/div[1]/div/div/span[1]",
            "input_box": "/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p",
            "body": "/html/body"
        }
        self._class = {
            "input_chat": "selectable-text copyable-text x15bjb6t x1n2onr6",
            "last_message": "_akbu",
            "unread_bubble": "_ahlk"
        }
        self.secondList = []
        
        self.main()

    def login(self):
        print("Abrindo WhatsApp Web...")
        self.driver.get(self.link)
        try:
            # Espera até que o elemento do QR Code (canvas) seja carregado
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, "canvas"))
            )

            # Captura a tela como imagem
            screenshot = self.driver.get_screenshot_as_png()
            screenshot_img = Image.open(BytesIO(screenshot))

            # Localiza o elemento do QR Code (canvas)
            qr_element = self.driver.find_element(By.TAG_NAME, "canvas")
            location = qr_element.location
            size = qr_element.size

            left = location['x']
            top = location['y']
            right = left + size['width']
            bottom = top + size['height']

            # Recorta a área do QR Code
            qr_code_img = screenshot_img.crop((left, top, right, bottom))

            # Converte para numpy array para leitura
            qr_np = np.array(qr_code_img)

            # Decodifica o QR Code
            qr_code = pyzbar.decode(qr_np)
          
            if qr_code:
                qr_text = qr_code[0].data.decode("utf-8")
                print("QR Code detectado!")

                # Exibir QR Code no terminal
                qrcode_terminal.draw(qr_text)
            else:
                print("Erro: QR Code não detectado.")

        except Exception as e:
            print(f"Erro ao capturar o QR Code: {e}")

        try:
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, self.xpaths["unread"]))
            )
            print("Login detectado! Continuando...")
        except:
            print("Tempo limite atingido. Certifique-se de escanear o QR Code a tempo.")
            self.driver.quit()

    def savingPhoneInDatabase(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.xpaths["phone"]))
            )

            for _ in range(3):
                try:
                    phone_element = self.driver.find_element(By.XPATH, self.xpaths["phone"])
                    phone_number = phone_element.text.strip()
                    break
                except StaleElementReferenceException:
                    print("Elemento do telefone ficou obsoleto. Tentando novamente...")
                    sleep(1)
            else:
                print("Falha ao capturar o telefone.")
                return None

            existing_phone = dbConfig.doesPhoneExist(phone_number)

            if existing_phone:
                print("Telefone já existe no banco.")
                self.phoneAlreadyExist()
            else:
                dbConfig.insertPhone(phone_number)
                print("Telefone salvo no banco.")
                self.phoneSaved()

        except Exception as e:
            print(f"Erro ao salvar telefone no banco: {e}")
            return None
        
    def phoneAlreadyExist(self):
        input_box = self.driver.find_element(By.XPATH, self.xpaths["input_box"])
        body = self.driver.find_element(By.XPATH, self.xpaths["body"])
        
        Menus.firstMessagePhoneSaved(self.driver, input_box, body)

    def phoneSaved(self):
        try:
            input_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.xpaths["input_box"]))
            )
            body = self.driver.find_element(By.XPATH, self.xpaths["body"])

            Menus.firstMessagePhoneNew(self.driver, input_box, body)
        except TimeoutException:
            print("Erro: Campo de entrada de mensagem não encontrado.")


    def openUnread(self):
        try:
            unread_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.xpaths["unread"]))
            )
            unread_button.click()
            sleep(2) 
            print("Mensagem não lida aberta.")
        except TimeoutException:
            print("Nenhuma mensagem não lida encontrada.")
        except Exception as e:
            print(f"Erro em openUnread: {e}")

    def openUnreadMessage(self):
        try:
            unread_bubble = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, self._class["unread_bubble"]))
            )
            unread_bubble.click()
            sleep(3) 
            print("Mensagens não lida clicada.")
            return True
        except TimeoutException:
            print("Nenhuma nova mensagem não lida foi encontrada.")
        except Exception as e:
            print(f"Erro em openUnreadMessage: {e}")
    
    def readLastMessage(self):
        try:
            readLastMessage_v = self.driver.find_elements(By.CLASS_NAME, self._class["last_message"])
            if readLastMessage_v:
                last_element = readLastMessage_v[-1]
                last_text = last_element.text
                print(f"Última mensagem: {last_text}")
                return last_text
            else:
                print("Nenhuma mensagem encontrada.")
                return None
        except Exception as e:
            print(f"Erro em readLastMessage: {e}")
            return None
    def getPhoneNumber(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.xpaths["phone"]))
            )
            for _ in range(3):
                try:
                    phone_element = self.driver.find_element(By.XPATH, self.xpaths["phone"])
                    return phone_element.text
                except:
                    print("não foi possivel conseguir o numero de telefone")
                    pass
                    
        except:
            print("algo deu errado")

    def endService(self, phone_number):
        dbConfig.deletePhoneFromCurrentService(phone_number)

    def verifyCurrentServiceList(self, phone_number):
        if dbConfig.doesPhoneExistInCurrentService(phone_number):
            return True
        else:
            return False
      
    def saveCurrentServicePhone(self, phone_number):
        body = self.driver.find_element(By.XPATH, self.xpaths["body"])
        input_box = self.driver.find_element(By.XPATH, self.xpaths["input_box"])
        if self.verifyCurrentServiceList(phone_number):
            return False
        elif self.verifyCurrentServiceList(phone_number) == False:
            dbConfig.insertPhoneToCurrentService(phone_number)
            Questions.questions(self.driver, input_box)
            body.send_keys(Keys.ESCAPE)
            return True
    
    def sendResponse(self, last_text, phone):
        questions = Questions
        menus = Menus
        body = self.driver.find_element(By.XPATH, self.xpaths["body"])
        input_box = self.driver.find_element(By.XPATH, self.xpaths["input_box"])
        
        question_map = {
            "1": questions.respQuestOne,
            "2": questions.respQuestTwo,
            "3": questions.respQuestThree,
            "4": questions.respQuestFour,
            "5": questions.respQuestFive,
            "6": questions.respQuestSix,
            "7": questions.respQuestSeven,
            "8": questions.respQuestEight,
        }

        if last_text in question_map:
            question_map[last_text](self.driver, input_box)
            
            input_box = self.driver.find_element(By.XPATH, self.xpaths["input_box"])
            questions.questionsSendMessage(self.driver, input_box)
            
            body.send_keys(Keys.ESCAPE)
        elif last_text == "9":
            questions.respQuestNove(self.driver, input_box)
            self.secondList.append(phone)
            print(f"Usuário adicionado na lista: {self.secondList}")
            body.send_keys(Keys.ESCAPE)
        elif last_text == "0":
            questions.respQuestZero(self.driver, input_box)
            self.endService(phone)
            body.send_keys(Keys.ESCAPE)
        else:
            input_box = self.driver.find_element(By.XPATH, self.xpaths["input_box"])
            menus.invalidNumber(self.driver, input_box)
            input_box = self.driver.find_element(By.XPATH, self.xpaths["input_box"])
            Questions.questions(self.driver, input_box)
            body.send_keys(Keys.ESCAPE)

    def main(self):
        try:
            self.login()
            self.openUnread()

            while True:
                message = self.openUnreadMessage()
                if message:
                    number = self.getPhoneNumber()
                    print(number)
                    verify = self.verifyCurrentServiceList(number)  

                    if verify:
                        print("numero ja esta salvo na lista de atendimentos")
                    elif verify != True:
                        print("numero nao está salvo na lista de atendimentos")
                        self.savingPhoneInDatabase()
                    
                    self.saveCurrentServicePhone(number)
                    last_text = self.readLastMessage()
                elif message != True:
                    continue
                if last_text and number not in self.secondList:
                    self.sendResponse(last_text, number)
                elif number in self.secondList and last_text != "0":
                    body = self.driver.find_element(By.XPATH, self.xpaths["body"])
                    input_box = self.driver.find_element(By.XPATH, self.xpaths["input_box"])
                    last_textIa = self.readLastMessage()
                    print(sendResponseWithChatGpt(last_textIa))
                    content = sendResponseWithChatGpt(last_textIa)
                    Menus.sendMessege(self.driver, input_box, content)
                    sleep(0.5)
                    input_box.send_keys(Keys.ENTER)
                    input_box = self.driver.find_element(By.XPATH, self.xpaths["input_box"])
                    Menus.sendMessege(self.driver, input_box, "digite 0 para sair")
                    sleep(0.5)
                    input_box.send_keys(Keys.ENTER)
                    
                    body.send_keys(Keys.ESCAPE)
                
                elif last_text == "0":
                    self.secondList.remove(number)
                    input_box = self.driver.find_element(By.XPATH, self.xpaths["input_box"])
                    Menus.sendMessege(self.driver, input_box, "Obrigado por usar nossa IA fique avontade para escolher qualquer outra opção")
                    input_box = self.driver.find_element(By.XPATH, self.xpaths["input_box"])
                    input_box.send_keys(Keys.ENTER)
                    input_box = self.driver.find_element(By.XPATH, self.xpaths["input_box"])
                    Questions.questions(self.driver, input_box)

                else:
                    print("nenhuma nova mensagem para responder")

                sleep(2)
        except KeyboardInterrupt:
            print("Bot encerrado manualmente.")
        finally:
            self.driver.quit()

bot = Bot()
