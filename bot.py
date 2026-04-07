import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
import requests

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
BOT_NAME = "Café e tapioca"
BOT_VERSION = "1.0"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
ENCURTADOR = "https://tinyurl.com/api-create.php?url="

piadas = [
    "Como faz para deixar um carteiro triste? Você mata a família dele.",
    "Por que os fantasmas são péssimos para contar mentiras? Porque são transparentes.",
    "Por que a plantinha não foi atendida no hospital? Porque só tinha médico de plantão."
]

async def comando_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text(f'Olá! eu sou o {BOT_NAME}. Use /ajuda para ver o que eu faço.')

async def comando_ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text(f'Comandos disponíveis: /start, /ajuda, /piada, /clima <cidade>, /encurtar <url>, /dado <número>, /moeda <valor> <moeda>')

async def comando_piada(update: Update, context: ContextTypes.DEFAULT_TYPE):
     print(f'[DEBUG] Enviando piada: {piadas}\n morrendo de rir')
     await update.message.reply_text(random.choice(piadas))

async def comando_clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cidade = " ".join(context.args)
    if not cidade:
        await update.message.reply_text("Por favor, forneça o nome da cidade. Exemplo: /clima São Paulo")
        return 
    url = f"{WEATHER_URL}?q={cidade}&appid={WEATHER_API_KEY}&units=metric&lang=pt_br"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        cidade = data["name"]
        pais = data["sys"]["country"]
        localizacao = cidade + ", " + pais
        temperatura = data["main"]["temp"]
        sensacao_termica = data["main"]["feels_like"]
        umidade = data["main"]["humidity"]
        descricao = data["weather"][0]["description"]
        await update.message.reply_text(f"🌍 {localizacao}\n🌤 {descricao}\n🌡 {temperatura}°C (sensação {sensacao_termica}°C)\n💧 Umidade: {umidade}%")
    else:
        print(f'[DEBUG] Erro ao obter clima para {cidade}: {data.get("message", "Sem detalhes")}')
        await update.message.reply_text(f"Não foi possível obter o clima para {cidade}. Verifique o nome da cidade e tente novamente.")


async def comando_encurtar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url_long = " ".join(context.args)
    if not url_long:
        await update.message.reply_text("Por favor, forneça a URL que deseja encurtar. Exemplo: /encurtar https://www.exemplo.com")
        return
    
    url_short = requests.get(ENCURTADOR + url_long).text
    print(f'[DEBUG] URL longa: {url_long} | URL encurtada: {url_short}')
    await update.message.reply_text(f"URL encurtada: {url_short}")
    
async def comando_dado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    numero = " ".join(context.args)
    if not numero.strip():
        numero = 6
    elif not numero.isdigit():
        print(f'[DEBUG] Entrada inválida para comando_dado: "{numero}"')
        await update.message.reply_text("Por favor, forneça um número válido. Exemplo: /dado 20")
        return
    resultado = random.randint(1, int(numero))
    print(f"[DEBUG] resultado: {resultado}")
    await update.message.reply_text(f'🎲 Você rolou um {resultado} (d{numero})')

async def comando_moeda(update: Update, contexto: ContextTypes.DEFAULT_TYPE):
    valor = contexto.args[0]
    moeda = contexto.args[1]
    if len(contexto.args) < 2:
        await update.message.reply_text("Exemplo: /moeda 100 USD")
        return
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}-BRL'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        cotacao = float(data[f"{moeda}BRL"]["bid"])
        resultado = float(valor) / cotacao
        await update.message.reply_text(f'💱{valor} BRL ={resultado:.2f} {moeda} ')

    else:
        print(f'[DEBUG] Erro ao obter cotação para {moeda}: {data.get("message", "Sem detalhes")}')
        await update.message.reply_text(f'Por favor, insira uma moeda válida. Exemplo: /moeda 100 USD')
        return

print(f'bot {BOT_NAME} {BOT_VERSION} iniciando...')
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", comando_start))
app.add_handler(CommandHandler("clima", comando_clima))
app.add_handler(CommandHandler("ajuda", comando_ajuda))
app.add_handler(CommandHandler("piada", comando_piada))
app.add_handler(CommandHandler("encurtar", comando_encurtar))
app.add_handler(CommandHandler("dado", comando_dado))
app.add_handler(CommandHandler("moeda", comando_moeda))

app.run_polling()