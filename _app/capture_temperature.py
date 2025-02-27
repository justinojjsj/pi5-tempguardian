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

url = 'http://172.16.248.9/status.json'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    
    # Print the extracted data
    print("Firmware:", data['firmware'])
    print("Name:", data['name'])
    print("Description:", data['description'])
    print("MAC Address:", data['mac'])
    print("Temperature:", data['temp'])
    print("Humidity:", data['umid'])
    print("External Temperature:", data['temp_ext'])
    print("Dew Point:", data['dew'])
    print("Input 1:", data['input1'])
    print("Input 2:", data['input2'])
    print("Output Alarm:", data['ouput_alarm'])
    print("Max Temperature:", data['max_temp'])
    print("Max Humidity:", data['max_umid'])
    print("Max External Temperature:", data['max_temp_ext'])
    print("Min Temperature:", data['min_temp'])
    print("Min Humidity:", data['min_umid'])
    print("Min External Temperature:", data['min_temp_ext'])
    print("S1 History:", data['s1hist'])
    print("S2 History:", data['s2hist'])
    print("S3 History:", data['s3hist'])
    print("Input 1 Mode:", data['input1_mode'])
    print("Input 2 Mode:", data['input2_mode'])
else:
    print("Failed to retrieve data. HTTP Status code:", response.status_code)