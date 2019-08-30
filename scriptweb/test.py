import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

print("Hello world!!!")

# indicar la ruta
url_page = 'https://www.empanadasmalvon.com/menu/'

# tarda 480 milisegundos
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "html.parser")

print(soup.prettify())

# Se obtiene el elemento
menuitem = soup.find_all('a', attrs={'class': 'view-popup'})
print(menuitem)

with open('trad.csv', 'a') as csv_file:
    for item in menuitem:
        """ item = BeautifulSoup(item, "html.parser") """
        h3 = str(item.h3).replace("<h3>","").replace("</h3>","").replace("<br/>","")
        p = str(item.p).replace("<p>","").replace("</p>","").replace("<br/>","")
        
        print(h3)
        print(p)
        print("---------------------------------------------------")
        fila = h3 + ": " + p
        if fila != "":
            writer = csv.writer(csv_file)
            writer.writerow([fila])