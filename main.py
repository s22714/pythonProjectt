import webbrowser
import requests

#pageurl = 'http://github.com'
#date = 20150101

pageurl = input("podaj adres: ")
date = input("podaj date format YYYYMMDD: ")

for a in range (3):
    url ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date)
    response = requests.get(url)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)

