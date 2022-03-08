from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import json
import re

url = "http://192.168.22.172/menu-example/"
sisu = requests.get(url).text
doc = BeautifulSoup(sisu, "html.parser")
toidud = []
toit = {}
lisainfo_json = []
hinnad_json = []
pealkirjad_json = []
nimetused_json = []

reLink = urlopen("http://192.168.22.172/menu-example/")
baidid = reLink.read()
tekst = baidid.decode()

pealkirjad = doc.select("strong")
for pealkiri in pealkirjad:
    pealkirjad_json.append(pealkiri.text)
    
nimetused = re.findall('(<h2>)(.*)(<span class="label label-info pull-right">)', tekst)
nimetused1 = [nimetus[1] for nimetus in nimetused]
print(nimetused1)

hinnad = doc.find_all("span")
for hind in hinnad:
    ilushind = hind.text
    ilushind = ilushind[:-1]
    if ilushind.replace(",", "", 1).isdigit():
        hinnad_json.append(ilushind)
        
lisainfo = doc.select("small")
for info in lisainfo:
    lisainfo_json.append(info.text)
    
    
# print(pealkirjad_json)
# print(hinnad_json)
# print(lisainfo_json)

for i in range(11):
    toit = {"hind": hinnad_json[i],
            "lisainfo": lisainfo_json[i]
}

    json_object = json.dumps(toit, indent=4, separators = (",", ": "))
    with open("sample.json", "a") as outfile:
        outfile.write(json_object)
    print(json_object)