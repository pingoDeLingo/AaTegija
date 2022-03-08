from bs4 import BeautifulSoup
import requests

url = "http://192.168.22.172/menu-example/"
sisu = requests.get(url).text
doc = BeautifulSoup(sisu, "html.parser")
pealkirjad = doc.select('strong')
for pealkiri in pealkirjad:
    print(pealkiri.text)