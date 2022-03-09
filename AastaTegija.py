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
listinumber = 0
kategoorianumber = 0


reLink = urlopen("http://192.168.22.172/menu-example/")
baidid = reLink.read()
tekst = baidid.decode()

pealkirjad = doc.select("strong")
for pealkiri in pealkirjad:
    pealkirjad_json.append(pealkiri.text)
    
    
praed = doc.find("div", {"id": "P"})
praed_sisu = praed.contents[0].ul.contents[0].h2.contents[0]

supid = doc.find("div", {"id": "S"})
supid_sisu = supid.contents[0].ul.contents[0].h2.contents[0]

magustoidud = doc.find("div", {"id": "M"})
magustoidud_sisu = magustoidud.contents[0].ul.contents[0].h2.contents[0]

joogid = doc.find("div", {"id": "J"})
joogid_sisu = joogid.contents[0].ul.contents[0].h2.contents[0]
joogid = joogid.text[7:-1]
joogid_full = []
for jook in joogid:
    if jook.isdigit() == False:
        
        joogid_full.append(jook)
print("".join(joogid_full))
kategooriad = ["praed", "supid", "magustoidud", "joogid"]

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
    
json_data.append({"nimetus": "PRAED", "toidud": []})
json_data.append({"nimetus": "SUPID", "toidud": []})
json_data.append({"nimetus": "MAGUSTOIDUD", "toidud": []})
json_data.append({"nimetus": "JOOGID", "toidud": []})
for i in range(0, len(nimetused_json)):
    try:
        json_data[listinumber]["toidud"].append({"nimetus": f'{kategooriad[kategoorianumber].contents[0].ul.contents[i].h2.contents[0]}', "hind": f'{hinnad_json[i]}', "lisainfo": f'{lisainfo_json[i]}'})
    except:
        if listinumber != 3:
            listinumber += 1
            kategoorianumber += 1
            i = 0
            continue


    with open("sample.json", "w") as f:
        json.dump(json_data, f, indent=4)