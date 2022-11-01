

import requests


def get_data_Maroc():
    url = "https://tass.com/userApi/search"
    
    payload = {
    "type": [],
    "sections": [],
    "searchStr": "",
    "sort": "date",
    "range": None,
    "from": 0,
    "size": 20
    }
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json;charset=utf-8",
    "Origin": "https://tass.com",
    "Connection": "keep-alive",
    "Referer": "https://tass.com/search",
    "Cookie": "_ym_uid=1646058981717753304; _ym_d=1646058981; __gads=ID=f10233967d6dfc8e-227a9610a8d1004e:T=1647331590:S=ALNI_Mae9TMMo7bb4x27WprqGyDbK9ujhA; tass_uuid=40BB8381-52AA-4575-A463-6A7D2C6635C8; geo__country_code=RU; geo__city_id=2097; geo__ip_hash=5419f4e7c8921eed6456d6a29168756d; geo__region_id=42; PHPSESSID=a678erf55jj0uh1l0ofvk8sed2; __js_p_=702,1800,0,0; __jhash_=184; __jua_=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A98.0%29%20Gecko%2F20100101%20Firefox%2F98.0; __hash_=1f81593209850d867c98d33d95d3c3c1; _ym_isad=2",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Cache-Control": "max-age=0",
    "TE": "trailers"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    while response.status_code != 200:
        response = requests.request("POST", url, json=payload, headers=headers)
    data = response.json()
    return data 

        


import time

def Liens_TASS(jour,mois,Année,Mot_clef):
    results = []
    dict_funct = {"Maroc":get_data_Maroc}
    date_dict_m = {"janv.":"01", "févr.":"02","mars":"03","avr.":"04","mai":"05","juin":"06","juil.":"07","août":"08","sept.":"09","oct.":"10","nov.":"11","déc.":"12"}
    jour = str(jour)
    if len(jour)==1:
        jour = "0" + jour
    for x in Mot_clef:
        if x in dict_funct:
            D = dict_funct[x]()
            for y in D:
                date_sortie =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(y['date']))
                if jour == date_sortie[8:10] and date_dict_m[mois] == date_sortie[5:7]:
                    titre = y['title']
                    lien = "https://tass.com"+y['link']
                    date_sortie = date_sortie[8:10]+"/"+date_sortie[5:7]+"/"+str(Année)
                    results.append((date_sortie,"TASS",titre,lien))            
    return list(set(results))  


#res = Liens_TASS(20, "mars", 2022, ["Maroc"])


