import requests
from datetime import datetime

# URL do serviço que retorna os dados em JSON
#url = 'http://172.16.248.9/status.json'
url = 'http://127.0.0.1:4087/status.json'

# Fazendo a requisição GET para obter os dados JSON
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse a resposta JSON
    
    # Obtendo a data e hora atuais formatadas
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%Y-%m-%d")  # Formato: YYYY-MM-DD
    current_time = current_datetime.strftime("%H:%M:%S")  # Formato: HH:MM:SS
    
    # Exibindo os dados
    print("Date:", current_date)
    print("Hour:", current_time)
    print("Temperature:", data['temp'])
    print("Humidity:", data['umid'])
else:
    print("Falha ao recuperar os dados. Código de status HTTP:", response.status_code)
