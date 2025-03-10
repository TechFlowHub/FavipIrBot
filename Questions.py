import Menus 
from selenium.webdriver.common.keys import Keys

def questions(browser, input_box):
    messages = [
        "📢 Escolha uma opção! Digite um número de *1 a 9* para sua dúvida ou *0 para encerrar* o atendimento.",
        "",
        "*🚀 Digite 9 para fazer perguntas e conversar com nossa Inteligência Artificial! 🤖💬*",
        "",
        "*1* - 💰 Quem deve declarar o Imposto de Renda em 2025",
        "",
        "*2* - 🛑 Quem NÃO precisa declarar o Imposto de Renda em 2025?",
        "",
        "*3* - 📌 Para que serve o Imposto de Renda e por que ele é cobrado?",
        "",
        "*4* - 📉 O que é IRRF?",
        "",
        "*5* - 📊 Tabela do Imposto de Renda 2025",
        "",
        "*6* - 🏡 Declarar meu patrimônio vai aumentar meu imposto?",
        "",
        "*7* - 📝 Como declarar o Imposto de Renda?",
        "",
        "*8* - 🏠 Tenho mais de uma casa, preciso declarar todas?",
        "",
        "*0* - 👋 Para finalizar atendimento"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)

def questionsSendMessage(browser, input_box):
    messages = [
        "🔄 Para continuar, escolha uma opção de *1 a 9*! Para encerrar, *digite 0*.",
        "",
        "*1* - 💰 Quem deve declarar o Imposto de Renda em 2025",
        "",
        "*2* - 🛑 Quem *NÃO* precisa declarar o Imposto de Renda em 2025?",
        "",
        "*3* - 📌 Para que serve o Imposto de Renda e por que ele é cobrado?",
        "",
        "*4* - 📉 O que é IRRF?",
        "",
        "*5* - 📊 Tabela do Imposto de Renda 2025",
        "",
        "*6* - 🏡 Declarar meu patrimônio vai aumentar meu imposto?",
        "",
        "*7* - 📝 Como declarar o Imposto de Renda?",
        "",
        "*8* - 🏠 Tenho mais de uma casa, preciso declarar todas?",
        "",
        "*9* - *🚀 USE NOSSA IA! 🤖✨*",
        "",
        "*0* - 👋 Para finalizar atendimento"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)

def respQuestOne(browser, input_box):
    messages = [
        "✅ *Quem deve declarar o Imposto de Renda em 2025?*",
        "",
        "📌 *Se você teve:*",
        "",
        "💰 Rendimentos tributáveis acima de *R$ 30.639,90* no ano ou renda mensal superior a *R$ 2.824,00*;",
        "",
        "📈 Recebeu rendimentos *isentos ou tributados na fonte* acima de *R$ 200 mil*;",
        "",
        "🚜 Obteve receita anual rural acima de *R$ 153.199,50*;",
        "",
        "📊 Fez operações na *Bolsa de Valores* acima de *R$ 40 mil* ou teve lucro;",
        "",
        "🏠 Possui *bens acima de R$ 800 mil*;",
        "",
        "🏡 Obteve *ganho de capital* na venda de bens ou isenção ao vender imóvel para comprar outro;",
        "",
        "🛬 Se tornou *residente no Brasil em 2024* e permaneceu até o final do ano.",
        "",
        "⚠️ *Se você se encaixa em alguma dessas situações, precisa declarar! 📄💰*"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)


def respQuestTwo(browser, input_box):
    messages = [
        "🚫 *Quem NÃO precisa declarar o Imposto de Renda em 2025?*",
        "",
        "📌 *Você está isento se:*",
        "",
        "✅ *Não* se enquadra nos requisitos obrigatórios para declaração;",
        "",
        "👨‍👩‍👧 Foi declarado como *dependente* de outra pessoa que já faz a declaração;",
        "",
        "🏡 Possui *bens e direitos* mas *não ultrapassa R$ 800 mil* até 31/12/2024.",
        "",
        "⚠️ *Casos específicos de isenção:*",
        "",
        "🩺 Pessoas com *doenças graves* como HIV, cardiopatia grave, esclerose múltipla, entre outras;",
        "",
        "👵👴 Quem recebe *aposentadoria, pensão ou reforma*.",
        "",
        "📄 Para solicitar essa isenção, é necessário um *laudo pericial* comprovando a condição.",
        "",
        "⏳ *Fique atento!* Quem precisa declarar deve enviar até *31 de maio de 2025* para evitar multa! 💰⚠️"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)

def respQuestThree(browser, input_box):
    messages = [
        "💰 *Para que serve o Imposto de Renda e por que ele é cobrado?*",
        "",
        "📢 O *Imposto de Renda* tem uma função *social e econômica*!",
        "",
        "🔹 Quem ganha mais, contribui mais, ajudando a financiar serviços essenciais como:",
        "",
        "🏥 *Saúde* (hospitais e remédios gratuitos);",
        "",
        "📚 *Educação* (escolas e universidades públicas);",
        "",
        "🚧 *Infraestrutura* (estradas, transportes e segurança).",
        "",
        "📊 Desde *1979*, o IR é uma das principais fontes de receita do governo. Em *2021*, a arrecadação federal atingiu *R$ 1,878 trilhão*! 📈💸",
        "",
        "⚠️ Ou seja, o imposto é essencial para manter o funcionamento do país e garantir investimentos para toda a população! 🇧🇷✅"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)


def respQuestFour(browser, input_box):
    messages = [
        "📌 *O que é IRRF?*",
        "",
        "💰 O *IRRF (Imposto de Renda Retido na Fonte)* é um imposto que já é descontado do seu salário antes mesmo de você recebê-lo.",
        "🏢 A empresa calcula e retém o imposto diretamente do seu pagamento e repassa para o governo. ✅",
        "",
        "🔎 *Por que o IRRF é descontado?*",
        "🔹 Para facilitar o pagamento do Imposto de Renda;",
        "🔹 Para garantir que você esteja em dia com suas obrigações fiscais.",
        "",
        "📊 *Como é calculado o IRRF?*",
        "🧮 O valor do imposto é calculado sobre o *salário bruto*, mas alguns descontos podem reduzir a base de cálculo:",
        "➖ INSS (contribuição previdenciária);",
        "➖ Pensão alimentícia (se houver);",
        "➖ Dependentes (R$ 189,59 por dependente).",
        "",
        "⚠️ Ou seja, o IRRF já é um adiantamento do seu Imposto de Renda, para que você não tenha que pagar tudo de uma vez depois! 💵📑"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)

def respQuestFive(browser, input_box):
    messages = [
        "📌 *Tabela do Imposto de Renda 2025*",
        "",
        "📊 O cálculo do IRPF é *progressivo*, ou seja, quanto maior a renda, maior o percentual de imposto pago. 🔄💰",
        "📅 Em 2025, a tabela *ainda não foi atualizada* e mantém os mesmos valores de 2023.",
        "",
        "💡 *Quem está isento?*",
        "✅ Quem recebe até *R$ 2.259,20* por mês não paga Imposto de Renda;",
        "✅ Quem recebe até *R$ 2.824,00* pode continuar isento se optar pelo *desconto simplificado* de *R$ 564,80*.",
        "",
        "📈 *Alíquotas do Imposto de Renda 2025:*",
        "💰 Até *R$ 2.259,20* ➝ *Isento*",
        "💰 De *R$ 2.259,21 a R$ 2.826,65* ➝ *7,5%* de imposto",
        "💰 De *R$ 2.826,66 a R$ 3.751,05* ➝ *15%* de imposto",
        "💰 De *R$ 3.751,06 a R$ 4.664,68* ➝ *22,5%* de imposto",
        "💰 Acima de *R$ 4.664,68* ➝ *27,5%* de imposto",
        "",
        "⚠️ *Atenção!* A tabela deveria ser ajustada conforme a inflação, mas sem atualização oficial, mais pessoas acabam pagando imposto devido a reajustes salariais. 📉",
        "",
        "❗ Existe uma proposta para aumentar a faixa de isenção para *R$ 5.000*, mas até o momento *não há confirmação oficial* pela Receita Federal. 🚨"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)

def respQuestSix(browser, input_box):
    messages = [
        "🏡 *Declarar meu patrimônio vai aumentar meu imposto?*",
        "",
        "🧐 *Não necessariamente!* O Imposto de Renda incide sobre a sua renda (salários, aluguéis, investimentos), não sobre os bens que você possui.",
        "",
        "💡 *Por que devo declarar meu patrimônio?*",
        "✔️ Evita problemas com a Receita Federal e possíveis malha-finas;",
        "✔️ Mantém seu histórico financeiro transparente;",
        "✔️ É essencial para comprovar evolução patrimonial e justificar sua renda.",
        "",
        "⚠️ *Mas atenção!* Se seu patrimônio for vendido com lucro, pode haver tributação sobre o ganho de capital. Nesse caso, é importante se informar para evitar surpresas! 📊💰"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)

def respQuestSeven(browser, input_box):
    messages = [
        "📝 *Como declarar o Imposto de Renda?*",
        "",
        "📍 *Dica:* Se você preferir ter o auxílio de profissionais para preencher sua declaração, a Unifavip Wyden, em Caruaru, oferece esse serviço sem custo! estudantes de contabilidade irão te ajudar a preencher a declaração corretamente e tirar todas as suas dúvidas. 💼👨‍💻",
        "📍 *Endereço da unidade:* Av. Adjar da Silva Casé, 800 - Indianópolis 55.024-740 Caruaru, PE · Brasil. 🏢"
        "",
        "1️⃣ *Acesse o programa da Receita Federal* – Baixe o programa no site oficial ou use o aplicativo 'Meu Imposto de Renda'. 📲💻",
        "",
        "2️⃣ *Reúna seus documentos* – Tenha em mãos informes de rendimento, recibos médicos, dados bancários e informações de bens e imóveis. 📑📌",
        "",
        "3️⃣ *Preencha os dados corretamente* – Informe seus rendimentos, despesas dedutíveis e patrimônio de forma detalhada. ✅",
        "",
        "4️⃣ *Escolha o modelo de declaração* – Veja se o modelo simplificado ou completo é mais vantajoso para você. 📊",
        "",
        "5️⃣ *Revise tudo e envie* – Erros podem levar à malha fina! Após conferir, envie e gere o DARF, se houver imposto a pagar. 🚀",
        "",
        "⏳ *Prazos e multas* – A entrega deve ser feita até 31 de maio de 2025. Quem atrasar pode pagar multa mínima de R$ 165,74! ⚠️💰"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)

def respQuestEight(browser, input_box):
    messages = [
        "🏡 *Tenho mais de uma casa, preciso declarar todas?*",
        "",
        "✅ *Sim!* A Receita Federal exige que todos os imóveis sejam declarados, independentemente da quantidade ou valor. Isso vale para casas, apartamentos, terrenos e até imóveis financiados. 🏠📋",
        "",
        "📌 *Como declarar?*",
        "1️⃣ Acesse a aba de 'Bens e Direitos' no programa da Receita;",
        "2️⃣ Selecione o código correspondente ao tipo do imóvel;",
        "3️⃣ Informe os dados, como endereço, data de aquisição e valor pago;",
        "4️⃣ Se for financiado, detalhe o saldo devedor e os valores pagos no ano. 🏦",
        "",
        "❗ *Imóveis alugados também devem ser informados, assim como a renda gerada!* Se houve valorização e venda com lucro, pode haver tributação sobre ganho de capital. 💰📊"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)


def respQuestZero(browser, input_box):
    messages = [
        "📴 Atendimento encerrado, volte sempre! 😊",
        "",
        "📍 Lembre-se: para um atendimento físico, você pode ir até a UniFAVIP! 🏢",
        "ℹ️ Na UniFAVIP Wyden, estudantes de contabilidade estarão prontos para lhe ajudar e orientar no preenchimento do seu imposto de renda! 📄💼",
        "📍 Endereço da unidade: Av. Adjar da Silva Casé, 800 - Indianópolis, 55.024-740 Caruaru, PE · Brasil. 🏢"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)


def respQuestNove(browser, input_box):
    messages = [
        "🌟 Nossa IA está pronta para analisar! 🤖✨",
        "",
        "❓ Manda uma pergunta aí! 👇😊"
    ]

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)

def continueQuestion(browser, input_box):
    messages = [
        "🌟 Gostaria de ver o painel de opções novamente?,"
        "",
        "❓ Digite [1] para SIM ou [2] para NÃO 👇😊"

    for message in messages:
        Menus.sendMessege(browser, input_box, message)
        input_box.send_keys(Keys.SHIFT, Keys.ENTER)

    input_box.send_keys(Keys.ENTER)
