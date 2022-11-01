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

def Trouver_lien(j,m,Année,S):
    results = []
    j = str(j)
    m = str(m)
    Année = str(Année)
     
    date_dict_m = {"1":"janvier", "2":"février","3":"mars","4":"avril","5":"mai","6":"juin","7":"juillet","8":"août","9":"septembre","10":"octobre","11":"novembre","12":"décembre"}
    for x in S.findAll("li",attrs = {"class":"timeline-post"}):
        dt = x.find("span",attrs = {"class":"timeline-date"}).text.split()
        if j == dt[0] and date_dict_m[m] == dt[1]:
            lien = x.find("a").get("href")
            titre = x.find("h2",attrs = {"class":"post-box-title"}).text
            jj = j
            mm = m
            if len(m)==1:
                mm = "0"+str(m)
            if len(j)==1:
                jj= "0"+str(j) 
            date_sortie =  jj+"/"+mm+"/"+Année
            results.append((date_sortie,"AgroMaroc",titre,lien))
    return results

def Lien_AgroMaroc(jour,mois,Année,Mot_clef):
    l = "https://www.agrimaroc.ma/actualite-agricole/actualites-agriculture-maroc/"
    S = get_data(l)
    r = Trouver_lien(jour,mois,Année,S)
    return r
    
R = Lien_AgroMaroc(11, 7, 2022, ["Sahara"])
