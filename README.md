# 🤖 Bot Telegram

Um bot para Telegram feito em Python com comandos úteis e divertidos.

## 💬 Comandos

| Comando | Descrição |
|---|---|
| `/start` | Apresentação do bot |
| `/ajuda` | Lista todos os comandos disponíveis |
| `/piada` | Conta uma piada aleatória |
| `/dado <número>` | Rola um dado com N lados (padrão: 6) |
| `/clima <cidade>` | Mostra o clima atual de uma cidade |
| `/moeda <valor> <moeda>` | Converte BRL para outra moeda (ex: USD, EUR) |
| `/encurtar <url>` | Encurta uma URL longa |

## 🛠️ Tecnologias

- [Python 3](https://www.python.org/)
- [python-telegram-bot](https://python-telegram-bot.org/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [AwesomeAPI](https://economia.awesomeapi.com.br/) (cotação de moedas)
- [TinyURL API](https://tinyurl.com/) (encurtador de URLs)

## ⚙️ Como rodar localmente

**1. Clone o repositório**
```bash
git clone https://github.com/Ccedilha/bot-telegram.git
cd bot-telegram
```

**2. Instale as dependências**
```bash
pip install python-telegram-bot python-dotenv requests
```

**3. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:
```
BOT_TOKEN=seu_token_aqui
WEATHER_API_KEY=sua_key_aqui
```

- O token do bot é obtido pelo [@BotFather](https://t.me/BotFather) no Telegram
- A API key do clima é obtida em [openweathermap.org](https://openweathermap.org)

**4. Rode o bot**
```bash
python bot.py
```

## 🚀 Deploy

O bot está configurado para deploy no [Railway](https://railway.app). Para fazer o deploy:

1. Suba o código para o GitHub
2. Conecte o repositório no Railway
3. Adicione as variáveis de ambiente (`BOT_TOKEN` e `WEATHER_API_KEY`) nas configurações do projeto
4. O Railway vai buildar e rodar o bot automaticamente

## 📁 Estrutura do projeto

```
bot-telegram/
├── bot.py          # Código principal do bot
├── .env            # Variáveis de ambiente (não versionado)
├── .gitignore      # Arquivos ignorados pelo Git
├── Procfile        # Configuração do Railway
├── requirements.txt
└── README.md
```