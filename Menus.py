from selenium.webdriver.common.keys import Keys
import Questions
import time
from selenium.webdriver.common.by import By

def sendMessege(browser, element, content):
    browser.execute_script(
        f'''
    const text = `{content}`;
    const dataTransfer = new DataTransfer();
    dataTransfer.setData('text', text);
    const event = new ClipboardEvent('paste', {{
    clipboardData: dataTransfer,
    bubbles: true
    }});
    arguments[0].dispatchEvent(event)
    ''',
        element)

def firstMessagePhoneNew(browser, input_box, body):
    messages = [
        "🟢 Olá! Seja bem-vindo(a) ao Assistente Virtual do Imposto de Renda! 📊💰",
        "",
        "Eu estou aqui para tirar suas dúvidas sobre a declaração e te ajudar a evitar problemas com a Receita Federal! 🚀💡 Como posso ajudar você hoje?",
        "",
        "Pergunte o que quiser e eu te responderei rapidinho. Vamos começar? 😃👇"
    ]

    for message in messages:
        sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)
        time.sleep(0.3)

    input_box.send_keys(Keys.ENTER)


def firstMessagePhoneSaved(browser, input_box, body):
    messages = [
        "🟡 E aí! Quanto tempo! 😃👋",
        "",
        "Que bom te ver de novo por aqui! Pronto(a) para mais uma rodada de perguntas sobre o Imposto de Renda? 💵📄",
        "",
        "Me diz como posso te ajudar hoje! 🚀✨"
    ]

    for message in messages:
        sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)
        time.sleep(0.3)

    input_box.send_keys(Keys.ENTER)
    time.sleep(0.3)

    input_box.send_keys(Keys.ENTER)
