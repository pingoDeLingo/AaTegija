from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import json
import re

nimetused_json = []
json_data = []
kategooriad = ["praed", "supid", "magustoidud", "joogid"]
url = "http://192.168.22.172/menu-example/"
sisu = requests.get(url).text
doc = BeautifulSoup(sisu, "html.parser")

reLink = urlopen("http://192.168.22.172/menu-example/")
baidid = reLink.read()
tekst = baidid.decode()
    
    
praed = doc.find("div", {"id": "P"})

supid = doc.find("div", {"id": "S"})

magustoidud = doc.find("div", {"id": "M"})

joogid = doc.find("div", {"id": "J"})
# joogid = joogid.text[7:-1]
# joogid_full = []
# for jook in joogid:
#     if jook.isdigit() == False:
#
#         joogid_full.append(jook)
# joogid_list = ("".join(joogid_full))
# joogid_list = joogid_list.replace("\u20ac", "")
# joogid_list = joogid_list[:-1].split(",")
# print(joogid_list)

nimetused = re.findall('(<h2>)(.*?)(<span class="label label-info pull-right">)', tekst)
nimetused1 = [nimetus[1] for nimetus in nimetused]
for nimetus in nimetused1:
    nimetused_json.append(nimetus)

    
json_data.append({"nimetus": "PRAED", "toidud": []})
json_data.append({"nimetus": "SUPID", "toidud": []})
json_data.append({"nimetus": "MAGUSTOIDUD", "toidud": []})
json_data.append({"nimetus": "JOOGID", "toidud": []})
for i in range(0, len(nimetused_json)):
    try:
        json_data[0]["toidud"].append({"nimetus": f'{praed.contents[0].ul.contents[i].h2.contents[0]}', "hind": f'{praed.contents[0].ul.contents[i].h2.contents[1].text[:-1]}', "lisainfo": f'{praed.contents[0].ul.contents[i].h2.contents[3].text}'})
        json_data[1]["toidud"].append({"nimetus": f'{supid.contents[0].ul.contents[i].h2.contents[0]}', "hind": f'{supid.contents[0].ul.contents[i].h2.contents[1].text[:-1]}', "lisainfo": f'{supid.contents[0].ul.contents[i].h2.contents[3].text}'})
        json_data[2]["toidud"].append({"nimetus": f'{magustoidud.contents[0].ul.contents[i].h2.contents[0]}', "hind": f'{magustoidud.contents[0].ul.contents[i].h2.contents[1].text[:-1]}', "lisainfo": f'{magustoidud.contents[0].ul.contents[i].h2.contents[3].text}'})
        json_data[3]["toidud"].append({"nimetus": f'{joogid.contents[0].ul.contents[i].h2.contents[0]}', "hind": f'{joogid.contents[0].ul.contents[i].h2.contents[1].text[:-1]}', "lisainfo": f'{joogid.contents[0].ul.contents[i].h2.contents[3].text}'})
    except:
            pass

    with open("sample.json", "w") as f:
        json.dump(json_data, f, indent=4)
f.close()