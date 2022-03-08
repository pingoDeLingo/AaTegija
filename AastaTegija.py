from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import json


url = "http://192.168.22.172/menu-example/"
sisu = requests.get(url).text
doc = BeautifulSoup(sisu, "html.parser")
toidud = []
toit = {}
lisainfod = []
hinnad = []
pealkirjad = []

pealkirjad = doc.select("strong")
for pealkiri in pealkirjad:
    print(pealkiri.text)
    

lisainfo = doc.select("small")
for info in lisainfo:
    lisainfod.append(info.text)
    
hind = doc.select("")
    
    
for i in range(11):
    toit = {
        "hind": hinnad[i]
        "lisainfo": lisainfod[i]
}

    json_object = json.dumps(toit, indent = 4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

# "nimetus": toidunimetus[i]
#             "hind": hinnad[i]


