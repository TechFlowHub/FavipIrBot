import Menus 
from selenium.webdriver.common.keys import Keys

def questions(browser, input_box):
    messages = [
        "1 - 💰 Quem precisa pagar Imposto de Renda?",
        "2 - 🛑 Quem está isento do Imposto de Renda?",
        "3 - 📌 Para que serve o Imposto de Renda?",
        "4 - 📉 O que é esse IRRF que aparece no meu contracheque?",
        "5 - 📊 Quantos % de imposto eu pago, dependendo do meu salário?",
        "6 - 🏡 Declarar meu patrimônio vai aumentar meu imposto?",
        "7 - 📝 Como declarar o Imposto de Renda?",
        "8 - 🏠 Tenho mais de uma casa, preciso declarar todas?",
        "0 - 🤔 Outra pergunta:"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)