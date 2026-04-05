import requests
from dotenv import load_dotenv
import os


load_dotenv()


WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
cidade = "São Paulo"

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

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
        await update.message.reply_text     (f"""
        🌍 {cidade}, {pais}
        🌤 {descricao}
        🌡 {temperatura}°C (sensação {sensacao_termica}°C)
        💧 Umidade: {umidade}%""")
    else:
        await update.message.reply_text(f"Não foi possível obter o clima para {cidade}. Verifique o nome da cidade e tente novamente.")
        
