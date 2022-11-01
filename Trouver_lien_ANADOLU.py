import requests


def get_data_Maroc():

    url = "https://www.aa.com.tr/fr/Search/Search"

    payload = "PageSize=100&Keywords=maroc&CategoryId=&TypeId=1&Page=1&__RequestVerificationToken=XA_e7JoA2vBuUrjdv4NvDd5gXcDsNoLJJfxEg-XXY4u1OTpmpe2nCtbo_B-HFn8czLSpf59jkqIz1BozujsP-GnEqvzU1vpJ2D-q0btY7TE1"
    headers = {
    "cookie": "NSC_CFUB_TFBSDI=ffffffff09a57b4245525d5f4f58455e445a4a423660",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "*/*",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.aa.com.tr",
    "Connection": "keep-alive",
    "Referer": "https://www.aa.com.tr/fr/search/?s=maroc",
    "Cookie": "__auc=52a6ad8117ee2842c883e0cb669; _ga=GA1.3.402778288.1644477821; lang=fr; _gid=GA1.3.946520727.1648971192; __RequestVerificationToken=1U_joEPTD8oHALilsUQU4LaBeILAfazYw4Kpz3bWyVFGUzAjvN_Za2LIrjvnYlMG61UmJUcZZK7sVoxCpsdGbF6UdTf18_NZ_gzZdpouvEk1; NSC_CFUB_TFBSDI=ffffffff09a57b4245525d5f4f58455e445a4a423660; __asc=ac03656317fee83e7059f5d6d70",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Cache-Control": "max-age=0",
    "TE": "trailers"
}

    response = requests.request("POST", url, data=payload, headers=headers)
    while response.status_code != 200:
        response = requests.request("POST", url, data=payload, headers=headers)
    data = response.json()
    return data

def get_data_Sahara():
    url = "https://www.aa.com.tr/fr/Search/Search"

    payload = "PageSize=100&Keywords=sahara&CategoryId=&TypeId=1&Page=1&__RequestVerificationToken=P6gzt7LPO-6pzORlKrmPgKdHESJHVy42yeDsGlh3ZsuWZB_zbW-BDJ-6iV0N-3aFBDp6GMaCE-jGPM62O8RPaNO8w2fneGtzzI7qMdgDIwo1"
    headers = {
    "cookie": "NSC_CFUB_TFBSDI=ffffffff09a57b4245525d5f4f58455e445a4a423660",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "*/*",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.aa.com.tr",
    "Connection": "keep-alive",
    "Referer": "https://www.aa.com.tr/fr/search/?s=sahara",
    "Cookie": "__auc=52a6ad8117ee2842c883e0cb669; _ga=GA1.3.402778288.1644477821; lang=fr; _gid=GA1.3.946520727.1648971192; __RequestVerificationToken=1U_joEPTD8oHALilsUQU4LaBeILAfazYw4Kpz3bWyVFGUzAjvN_Za2LIrjvnYlMG61UmJUcZZK7sVoxCpsdGbF6UdTf18_NZ_gzZdpouvEk1; NSC_CFUB_TFBSDI=ffffffff09a57b4245525d5f4f58455e445a4a423660; __asc=ac03656317fee83e7059f5d6d70; _gat=1; _gat_aa_genel=1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

    response = requests.request("POST", url, data=payload, headers=headers)
    while response.status_code != 200:
        response = requests.request("POST", url, data=payload, headers=headers)
    data = response.json()
    return data


    
def Liens_ANADOLU(jour,mois,Année,Mot_clef):
    results = []
    dict_funct = {"Maroc":get_data_Maroc,"Sahara":get_data_Sahara}
    date_dict_m = {"janv.":"01", "févr.":"02","mars":"03","avr.":"04","mai":"05","juin":"06","juil.":"07","août":"08","sept.":"09","oct.":"10","nov.":"11","déc.":"12"}
    jour = str(jour)
    if len(jour)==1:
        jour = "0" + jour
    for x in Mot_clef:
        D = dict_funct[x]()
        for y in D["Documents"]:
            date_sortie = y['CreateDateString']
            if jour == date_sortie[0:2] and date_dict_m[mois] == date_sortie[3:5]:
                titre = y['Title']
                lien = "https://www.aa.com.tr"+y['Route']
                results.append((date_sortie.replace(".","/"),"ANADOLU",titre,lien))            
    return list(set(results))  


#res = Liens_ANADOLU(3, "avr.",2022 ,["Maroc","Sahara"])



