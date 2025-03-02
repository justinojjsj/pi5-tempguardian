# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
# from datetime import date
# from datetime import datetime
# import mysql.connector
# import time
# db_connection = mysql.connector.connect(host='127.0.0.1', user='root', password='tX84c=7OljSX', database='db_tempguardian')

# #Setando opções do driver firefox
# f_options=Options()
# f_options.add_argument("-headless")  
# options = webdriver.FirefoxOptions()  
# webBrowser = webdriver.Firefox(options=f_options)

# #Site dos dados para serem capturados
# webBrowser.get('http://172.16.248.9/status.json')

# #Tempo de espera para carregar os dados na página adequadamente
# #time.sleep(10)

# #Classe a ser capturada
# #conteudo = webBrowser.find_element(By.CLASS_NAME, "cmp-modalCamera__alerts").text
# webBrowser.close()

#Separa o conteúdo em vetor
#conteudo = conteudo.splitlines()
#tamanho = len(conteudo)

import requests

#url = 'http://172.16.248.9/status.json'
url = 'http://127.0.0.1:4087/example_data.php'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    
    # Print the extracted data
    print("Temperature:", data['temp'])
    print("Humidity:", data['umid'])
else:
    print("Failed to retrieve data. HTTP Status code:", response.status_code)