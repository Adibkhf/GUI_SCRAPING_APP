from bs4 import BeautifulSoup
import requests
import concurrent.futures
import itertools


def get_data(link):
    r = requests.get(link,stream=True,verify = False)#, proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content,'html.parser')
    return soup
def titre(S):
    return S.find('h1').text


    
def traiter(x,res,j,m,i,Année):
    MCC = ['marruecos','Marruecos','marroquí','Marroquí','marroquíes','Marroquíes','Magrebíes','sáhara','Mohamed v','magrebíes','Sáhara','mohamed v','saharaui','Saharaui','saharauis','Saharauis']
    date_dic = {"1":"enero","2":"febrero","3":"marzo","4":"abril","5":"mayo","6":"junio","7":"julio","8":"agosto","9":"septiembre","10":"octubre","11":"noviembre","12":"dicembre"}
    S = get_data("https://www.efe.com/page/"+str(i)+"/?s="+x)
    for a in S.findAll("article"):
        if a.find("time",attrs = {"class":"entry-date published"})!=None:
            txt = a.find("time",attrs = {"class":"entry-date published"}).text
            #print(txt)
            #print(txt[0:2])
            if str(j)==txt[0:2].strip() and date_dic[str(m)] in txt:
                lien = a.find("a").get('href')
                SS = get_data(lien)
                P = SS.findAll('p')
                P = [x.text.split(' ') for x in SS.findAll('p') if x.text not in ["",' ','\n']]
                PP = []
                for x in P:
                    for y in x:
                        PP.append(y)
                PP = list(set(PP))
                if any(x in PP for x in MCC):
                    jour = str(j) 
                    mois = str(m)
                    titre = a.find("h2").text
                    if len(jour)==1:
                        jour = "0"+jour
                    date_sortie = jour+"/"+mois+"/"+str(Année)
                    res.append((date_sortie,"EFE",titre,lien))

                
def Lien(x,res,j,m,i,Année):
    traiter(x,res,j,m,i,Année)
    S = get_data("https://www.efe.com/page/"+str(i)+"/?s="+x)
    if S.find("a",attrs={"class":"next page-numbers"})!=None:
        i = i + 1
        Lien(x,res,j,m,i,Année)
       
#ress = []
#Lien("marruecos",ress,13,10,1,2022)      
#traiter("marruecos", ress, 13, 10, 1,2022)  

                
def Liens_EFEE(res,j,m,Année,Mot_cle):
    MC = ['marruecos','marroquí','marroquíes','magrebíes','Sáhara','mohamed v','saharaui','saharauis']
    for x in MC:  
        i = 1
        Lien(x,res,j,m,i,Année)
    

#S = get_data('https://efe.com/canarias/interior-expulsa-a-un-marfileno-a-marruecos-pese-a-haberlo-suspendido-un-juez/')
#S.find("div",attrs={"class":"entry-content"}).text

def Liens_EFE(j,m,Année,Mot_clé):
    res = [] 
    Liens_EFEE(res,j,m,Année,Mot_clé)
    res = list(set(res))
    return res

#S = Liens_EFE(13,10,2022,['Maroc','Sahara'])