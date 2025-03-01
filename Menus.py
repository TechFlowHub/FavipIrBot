from selenium.webdriver.common.keys import Keys

def sendMessage(browser, element, content):
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

def firstMessagePhoneSaved():
    message = [
        "🟢 Olá! Seja bem-vindo(a) ao Assistente Virtual do Imposto de Renda! 📊💰",
        "Eu estou aqui para tirar suas dúvidas sobre a declaração e te ajudar a evitar problemas com a Receita Federal! 🚀💡Como posso ajudar você hoje?",
        "",
        "Pergunte o que quiser e eu te responderei rapidinho. Vamos começar? 😃👇"
    ]

    for message in messages:
        if message:
            sendMessage(browser, input_box, message)
            input_box.send_keys(Keys.SHIFT, Keys.ENTER)
          


def fisrtMessagePhoneAlreadyExist():
    return



