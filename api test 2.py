import requests
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
response = requests.get(url)
print(response.status_code)