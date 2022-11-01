from bs4 import BeautifulSoup
import requests
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
import re

#date_dict_m = {"janv.":"", "févr.":"","mars":"","avr.":"","mai":"","juin":"","juil.":"","août":"","sept.":"","oct.":"","nov.":"","déc.":""}

def get_data(link):
    r = requests.get(link,stream=True,verify = False)#, proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content,'html.parser')
    return soup

#Trouver les liens contenant les mots clé (Maroc, Sahara occidental)
def Trouver_lien(j,m,S):
    results = []
    date_dict_m = {"1":"janvier", "2":"février","3":"mars","4":"avril","5":"mai","6":"juin","7":"juillet","8":"août","9":"septembre","10":"octobre","11":"novembre","12":"décembre"}
    m = date_dict_m[str(m)]   
    date_dic = {"janvier":"01","février":"02","mars":"03","avril":"04","mai":"05","juin":"06","juillet":"07","août":"08","septembre":"09","octobre":"10","novembre":"11","décembre":"12"}
    for x,y in zip(S.findAll("dt",attrs = {"class":"result-title"}),S.findAll("dd",attrs = {"class":"result-created"})):
        if j == int(y.text.strip()[8:10]) and m in y.text:
            text_date = y.text.split()
            jour = text_date[2]
            if len(jour)==1:
                jour = "0"+jour
            date_sortie = jour+"/"+date_dic[text_date[3]]+"/"+text_date[4]
            lien = "https://www.aps.dz"+x.find("a").get("href")
            titre = x.find("a").text.strip()
            results.append((date_sortie,"Algérie Présse Service",titre,lien))   
    return list(set(results))  

def Liens_APS(jour,mois,Année,Mot_clef):
    res = []
    for x in Mot_clef:
        l = "https://www.aps.dz/recherche?searchword="+x+"&ordering=newest&searchphrase=any&limit=0"
        S = get_data(l)
        r = Trouver_lien(jour,mois,S)
        res = res + r
    return list(set(res))

#res = Liens_APS(10,10,2022,['Maroc','Sahara'])