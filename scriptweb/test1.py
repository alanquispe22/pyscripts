import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

print("Hello world!!!")

# indicar la ruta
url_page = 'https://www.malvon.es/donde-estamos/'

# tarda 480 milisegundos
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "html.parser")

texto = soup.get_text() 
# Eliminar todos los numeros, correos
f = open('temp.txt','a')
f.write(texto)
f.close()