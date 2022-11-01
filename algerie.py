from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import webbrowser


def get_data(link):
    r = requests.get(link, verify=False,stream=True,)#, proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content,'html.parser')
    return soup
def f(j,m,S):
    results = []
    for x,y in zip(S.findAll("dt",attrs = {"class":"result-title"}),S.findAll("dd",attrs = {"class":"result-created"})):
        if j == int(y.text[8:11]) and m in y.text: 
            results.append("https://www.aps.dz"+x.find("a").get("href")) 
    return results      

l1 = "https://www.aps.dz/recherche?searchword=maroc&searchphrase=all"
S1 = get_data(l1)
l2 ="https://www.aps.dz/recherche?searchword=sahara%20occidental&ordering=newest&searchphrase=all&limit=20"
S2 = get_data(l2)

def algerie_press(jour,mois):
    r1 = f(jour,mois,S1)
    r2 = f(jour,mois,S2)
    res = r1+r2
    res = list(set(res))
    return res 
L = algerie_press(16, "février")

    
    
    
