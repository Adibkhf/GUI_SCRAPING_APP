import requests
from bs4 import BeautifulSoup
import concurrent.futures


def get_data(link):
    r = requests.get(link,stream=True,verify = False)#, proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content,'html.parser')
    return soup

#S = get_data("https://www.africa-press.net/algeria/?s=%D8%A7%D9%84%D8%AC%D9%8A%D8%B4")


def traiter_arabic(x,res,jour,mois,Année):
    date_sortie = x.find('time').text
    lien = x.find('a').get('href')
    j = date_sortie[8:10]
    m = date_sortie[5:7]
    Ann = date_sortie[0:4]
    if jour == j and mois == m and Année == Ann:
        titre = x.find('h3').text
        date_sortie = date_sortie[0:10]
        date_sortie = j + '/' + m + '/' +date_sortie[0:4]
        res.append((date_sortie,"AFRICA_PRESSE_AR",titre,lien))
        
def traiter(x,res,jour,mois,Année):
    date_sortie = x.find('time').text
    lien = x.find('a').get('href')
    j = date_sortie[0:2]
    m = date_sortie[3:5]
    Ann = date_sortie[6:10]
    if jour == j and mois == m and Année == Ann:
        titre = x.find('h3').text
        date_sortie = date_sortie.replace('-','/')[0:10]
        res.append((date_sortie,"AFRICA_PRESSE",titre,lien))
    
def Liens(S,res,jour,mois,Année,i):
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for x in S.findAll("div",attrs = {'class':'td_module_16 td_module_wrap td-animation-stack'}):
            executor.submit(traiter,x=x,res = res, jour = jour,mois = mois,Année=Année)    
    if S.find('i',attrs = {'class':'td-icon-menu-right'})!=None:
        i = i + 1
        i = str(i)
        S = get_data(S.findAll('a',attrs = {'title':i})[0].get('href'))
        Liens(S,res,jour,mois,Année,int(i))
        
def Liens_AR(S,res,jour,mois,Année,i):
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for x in S.findAll("div",attrs = {'class':'td_module_16 td_module_wrap td-animation-stack'}):
            executor.submit(traiter_arabic,x=x,res = res, jour = jour,mois = mois,Année=Année)    
    if S.find('i',attrs = {'class':'td-icon-menu-right'})!=None and i<5:
        i = i + 1
        i = str(i)
        S = get_data(S.findAll('a',attrs = {'title':i})[0].get('href'))
        Liens_AR(S,res,jour,mois,Année,int(i))
     
def Exec_english(jour,mois,Année,nom_agence,Mot_clé,res_fi):
    dict_mot = {"Maroc":"Morocco","sahara":"sahara"}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for x in Mot_clé:
            i = 1
            l = "https://www.africa-press.net/"+nom_agence+"/?s="+dict_mot[x]
            S = get_data(l)
            executor.submit(Liens(S = S,res = res_fi,jour = jour,mois= mois,Année=Année,i = i))

def Exec_french(jour,mois,Année,nom_agence,Mot_clé,res_fi):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for x in Mot_clé:
            i = 1
            l = "https://www.africa-press.net/"+nom_agence+"/?s="+x
            S = get_data(l)
            executor.submit(Liens(S = S,res = res_fi,jour = jour,mois= mois,Année=Année,i = i))

def Exec_arabic(jour,mois,Année,nom_agence,Mot_clé,res_fi):
    dict_mot = {"Maroc":"المغرب","sahara":"الصحراء"}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for x in Mot_clé:
            i = 1
            l = "https://www.africa-press.net/"+nom_agence+"/?s="+dict_mot[x]
            S = get_data(l)
            executor.submit(Liens_AR(S = S,res = res_fi,jour = jour,mois= mois,Année=Année,i = i))

def Liens_French(jour,mois,Année,Mot_clé,res_f):
    French_agence = ['Bénin', 'Burundi','Centrafricaine','Tchad','Comores','Congo Brazzaville','Congo Kinshasa','Djibouti','Guinée équatoriale ','Guinée Conakry','Gabon','Guinée Bissau',"Côte d'Ivoire",'Madagascar','Mali','Niger','Sao Tomé et Principe','Sénégal','Cameroun','Togo','Burkina Faso']
    with concurrent.futures.ThreadPoolExecutor(max_workers=42) as executor:
        for x in French_agence:
            executor.submit(Exec_french, jour = jour,mois = mois,Année = Année,nom_agence = x,Mot_clé = Mot_clé,res_fi = res_f)

def Liens_English(jour,mois,Année,Mot_clé,res_f):
    English_agence = ['Nigeria','Namibia','Rwanda','Seychelles', 'Sierra Leone','South Africa','South Sudan','Tanzania','Uganda','Zambia','Zimbabwe','Ghana','Gambia','Malawi','Liberia','Eritrea','Kenya','Botswana','Eswatini','Mauritius','Lesotho','Ethiopia','Angola','Mozambique','Cape Verde']
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for x in English_agence:            
            executor.submit(Exec_english, jour = jour,mois = mois,Année=Année,nom_agence = x,Mot_clé = Mot_clé,res_fi = res_f)

def Liens_Arabic(jour,mois,Année,Mot_clé,res_f):
    Arabic_agence = ['Algeria','Egypt','Libya','Morocco','Mauritania','Western Sahara','Somalia','Sudan','Tunisia','Somaliland']
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for x in Arabic_agence:            
            executor.submit(Exec_arabic, jour = jour,mois = mois,Année = Année,nom_agence = x,Mot_clé = Mot_clé,res_fi = res_f)


def filtre_doublon_par_titre(res):
    seen = set()
    result = []
    for a,b,c,d in res:
        if not c in seen:
            seen.add(c)
            result.append((a,b,c,d))
    return result     


def Liens_AFRICA_PRESS(jour,mois,Année,Mot_clé):
    jour = str(jour)
    Année = str(Année)
    if len(jour)==1:
        jour = "0" + jour
    date_dict_m = {1:"01",2:"02",3:"03",4:"04",5:"05",6:"06",7:"07",8:"08",9:"09",10:"10",11:"11",12:"12"}
    res_FRENCH = []
    res_ENGLISH = [] 
    res_ARABIC= []
    with concurrent.futures.ThreadPoolExecutor(10) as executor:
        executor.submit(Liens_English,jour = jour,mois = date_dict_m[mois],Année=Année,Mot_clé = Mot_clé,res_f = res_ENGLISH)
        executor.submit(Liens_French,jour = jour,mois = date_dict_m[mois],Année=Année,Mot_clé = Mot_clé,res_f = res_FRENCH)
        executor.submit(Liens_Arabic,jour = jour,mois = date_dict_m[mois],Année = Année,Mot_clé = Mot_clé,res_f = res_ARABIC)
    RES_F = res_FRENCH + res_ARABIC + res_ENGLISH
    RES_F = filtre_doublon_par_titre(RES_F)
    return RES_F 


#jour = 27
#mois = "mars"
#Mot_clé = ["Maroc","Sahara"]
#☻lien_africa_presse = Liens_AFRICA_PRESS(22,'avr.',2022, Mot_clé)