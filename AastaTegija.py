from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import json
import re

url = "http://192.168.22.172/menu-example/"
sisu = requests.get(url).text
doc = BeautifulSoup(sisu, "html.parser")
json_data = []
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
    
    
nimetused = re.findall('(<h2>)(.*?)(<span class="label label-info pull-right">)', tekst)
nimetused1 = [nimetus[1] for nimetus in nimetused]
for nimetus in nimetused1:
    nimetused_json.append(nimetus)


hinnad = doc.find_all("span")
for hind in hinnad:
    ilushind = hind.text
    ilushind = ilushind[:-1]
    if ilushind.replace(",", "", 1).isdigit():
        hinnad_json.append(ilushind)
  
  
lisainfo = doc.select("small")
for info in lisainfo:
    lisainfo_json.append(info.text)
    
# json_data.append({"nimetus": "PRAED", "toidud": []})
# json_data.append({"nimetus": "SUPID", "toidud": []})
# json_data.append({"nimetus": "MAGUSTOIDUD", "toidud": []})
# json_data.append({"nimetus": "JOOGID", "toidud": []})
for i in range(0, len(nimetused_json)):
    
    toit = {
            "nimetus": nimetused_json[i],
            "hind": hinnad_json[i],
            "lisainfo": lisainfo_json[i]
            
}
    json_data.append(toit)


    with open("sample.json", "w") as f:
        json.dump(json_data, f, indent=4)
