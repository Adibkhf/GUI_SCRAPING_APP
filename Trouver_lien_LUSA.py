import requests
from bs4 import BeautifulSoup


def get_data(link):
    r = requests.get(link,stream=True,verify = False)#, proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content,'html.parser')
    return soup


def Liens_LUSA(jour,mois,Année,Mot_clef):
    results = []
    Mc = {"Maroc":"Marrocos"}
    date_dict_m = {"janv.":"01", "févr.":"02","mars":"03","avr.":"04","mai":"05","juin":"06","juil.":"07","août":"08","sept.":"09","oct.":"10","nov.":"11","déc.":"12"}
    jour = str(jour)
    if len(jour)==1:
        jour = "0" + jour
    for x in Mot_clef:
        if x in Mc:
            S = get_data("https://www.lusa.pt/search-results?kw="+Mc[x])
            for y in S.find("div",attrs = {"class":"col-sm-12 article-category"}):
                if type(y.find("a"))!=int and len(y.find('ul').text)>12:
                    date = y.find('ul').text.strip()
                    j = date[0:2]
                    m = date[3:5]
                    titre = y.find("a").text
                    Résumé = y.findAll("a")[2].text
                    if jour == j and m == date_dict_m[mois] and (Mc[x] in titre or Mc[x] in Résumé):    
                        lien = y.find("a").get('href')
                        date = date[0:10].replace('-','/')
                        results.append((date,"LUSA",titre,lien))            
    return list(set(results))


#r = Liens_LUSA(13, "mars", 2022, ["Maroc"])


