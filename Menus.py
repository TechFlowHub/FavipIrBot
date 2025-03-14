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

def invalidNumber(browser, input_box):
    messages = [
        "⚠️ *Opção inválida!* Por favor, digite um número de *1 a 9* para escolher uma pergunta ou *0 para encerrar* o atendimento."
    ]

    for message in messages:
        sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)
        time.sleep(0.3)

    input_box.send_keys(Keys.ENTER)

def evaluation(browser, input_box):
    messages = [
        "⭐ Avalie nosso atendimento! Escolha um número de *1 a 5*: ",
        "",
        "*5 - 🤩 Excelente*",
        "*4 - 😊 Bom*",
        "*3 - 😐 Regular*",
        "*2 - 🙁 Ruim*",
        "*1 - 😞 Péssimo*"
    ]

    for message in messages:
        sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)

def evaluationTy(browser, input_box):
    messages = [
        "🙏 Obrigado por avaliar nosso atendimento!",
        "",
        "Sua opinião é muito importante para nós. 💙",
        "",
        "Se precisar de mais alguma coisa, estamos à disposição! 😊"
    ]

    for message in messages:
        sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)

def evaluationError(browser, input_box):
    messages = [
       "⚠️ Valor inválido! Por favor, digite um número entre *1 e 5* para avaliar nosso atendimento."
    ]

    for message in messages:
        sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)

def optionError(browser, input_box):
    messages = [
       "⚠️ *Opção inválida!*",
       "",
       "🌟 Gostaria de ver o painel de opções novamente?",
       "",
       "Por favor digite [SIM] para *SIM*, [F] para *FINALIZAR* o atendimento 👇😊, ou escolha uma nova opção entre *1 e 9*."
    ]

    for message in messages:
        sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)