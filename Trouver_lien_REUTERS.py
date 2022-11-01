import requests


def get_data_Maroc():

    url = "https://www.reuters.com/pf/api/v3/content/fetch/articles-by-search-v2"

    querystring = {"query":"{\"keyword\":\"morocco\",\"offset\":0,\"orderby\":\"display_date:desc\",\"size\":10,\"website\":\"reuters\"}","d":"90","_website":"reuters"}
    
    payload = ""
    headers = {
    "cookie": "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept": "*/*",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.reuters.com/site-search/?query=morocco",
    "Connection": "keep-alive",
    "Cookie": "_cb_ls=1; ajs_anonymous_id=%22cfb3c23b-cb7f-41ca-b584-af0ee6cf249c%22; sophiTagid.23dd=7740cb3b-4395-4ad6-b402-a96ccdc72b4d.1644585437.38.1650953108.1650757873.1bf46c85-0773-40a0-9e0f-db185fc8ec03; _sp_duid=7740cb3b-4395-4ad6-b402-a96ccdc72b4d; _fssid=db29bbe8-1722-4dac-be55-4132716f7b5a; usprivacy=1---; _ga=GA1.2.1884861730.1644585439; permutive-id=704ab9ea-cd90-446d-829a-620862dcf5fd; _cb=73f14DuCmqzD9L7c4; _chartbeat2=.1644585439477.1650953084220.0000000000011101.D5UqVuDiV_qBDCE9BPDGjHUB97Ip-.2; _pbjs_userid_consent_data=3524755945110770; _pubcid=77d7bdc0-2caa-4f98-a378-6da66e5f5f74; _fbp=fb.1.1644585439679.1691172359; __gads=ID=760b8bfccea96a2c-228a9142e0cf0081:T=1644585439:S=ALNI_MY3zWE7BylxLJVZnrSpPQQ5cNUHmA; __qca=P0-470171409-1644585442087; cto_bundle=i8uNp18zUnVJQzNQN0VpYVVOZWtlTWZrJTJGNm1rUXhSUzJEZks3TDBjJTJCU05BRGlPZ1hBa1h4VTZrd0ZjdXAlMkZrSU0yRHQ3OFhtTDdCMUtTdzdzQXZabjl3Q3hLWXdNblo4OUNsM0lWWkZRUVE2ODh4ZVJadXRzcEhnTXNrQ3klMkY4OWdYZmt4V3l4RldXZkFWYzdudHBKUkhVdjEwUSUzRCUzRA; _lr_env_src_ats=false; _cc_id=d4f836318fbbd48a440853bf3799cee6; cookie=%7B%22id%22%3A%2201FVMEWW42D57545TX2PKCS9EY%22%2C%22ts%22%3A1648800972661%7D; _gaexp=GAX1.2.vZkhuqNjQKGTE-0Yuo3BiA.19118.1!x-ljBQjWS0q2X5034LeLUw.19126.1; ta-octane.id=c9fb89c4-c31b-406c-bb62-f7ddc122ee48|50376aac-d125-49b9-8f3f-c89a5758e663|1650953108360|; _gcl_au=1.1.654277529.1644912957; sailthru_hid=be7fcffdbcedd4e3084e7ebf1763820a620b61a4978fae18967cb5ae57d3e7e23135f10adbdf7ba7ce143adf; RT=z=1&dm=reuters.com&si=u75euwigmuh&ss=l2a5jmav&sl=0&tt=0; cleared-onetrust-cookies=Thu, 17 Feb 2022 19:17:07 GMT; OptanonConsent=isIABGlobal=false&datestamp=Tue+Apr+26+2022+08%3A04%3A41+GMT%2B0200+(heure+d%E2%80%99%C3%A9t%C3%A9+d%E2%80%99Europe+centrale)&version=6.31.0&hosts=&consentId=c72405db-cd24-4c23-8980-56b58594880b&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2CSPD_BG%3A1%2C2%3A1%2C4%3A1&AwaitingReconsent=false&geolocation=MA%3B04; OptanonAlertBoxClosed=2022-04-26T06:04:41.493Z; reuters-geo={country:MA, region:-}; fsbotchecked=true; sophiTagses.23dd=*; _cb_svref=null; _gid=GA1.2.1798249872.1650953079; _lr_geo_location=MA; _gat=1; _chartbeat4=t=Du-R1kBkxDaSC-NsnIBJFK6XCSv8ou&E=4&x=0&c=0.4&y=2554&w=358",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    while response.status_code != 200:
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = response.json()
    return data


def get_data_Sahara():
    url = "https://www.reuters.com/pf/api/v3/content/fetch/articles-by-search-v2"

    querystring = {"query":"{\"keyword\":\"sahara\",\"offset\":0,\"orderby\":\"display_date:desc\",\"size\":10,\"website\":\"reuters\"}","d":"90","_website":"reuters"}

    payload = ""
    headers = {
    "cookie": "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept": "*/*",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.reuters.com/site-search/?query=sahara&offset=0",
    "Connection": "keep-alive",
    "Cookie": "_cb_ls=1; ajs_anonymous_id=%22cfb3c23b-cb7f-41ca-b584-af0ee6cf249c%22; sophiTagid.23dd=7740cb3b-4395-4ad6-b402-a96ccdc72b4d.1644585437.38.1650953273.1650757873.1bf46c85-0773-40a0-9e0f-db185fc8ec03; _sp_duid=7740cb3b-4395-4ad6-b402-a96ccdc72b4d; _fssid=db29bbe8-1722-4dac-be55-4132716f7b5a; usprivacy=1---; _ga=GA1.2.1884861730.1644585439; permutive-id=704ab9ea-cd90-446d-829a-620862dcf5fd; _cb=73f14DuCmqzD9L7c4; _chartbeat2=.1644585439477.1650953110517.0000000000011101.D5UqVuDiV_qBDCE9BPDGjHUB97Ip-.3; _pbjs_userid_consent_data=3524755945110770; _pubcid=77d7bdc0-2caa-4f98-a378-6da66e5f5f74; _fbp=fb.1.1644585439679.1691172359; __gads=ID=760b8bfccea96a2c-228a9142e0cf0081:T=1644585439:S=ALNI_MY3zWE7BylxLJVZnrSpPQQ5cNUHmA; __qca=P0-470171409-1644585442087; cto_bundle=LRoFRl8lMkZkWWZvRlhJd2VJMmdTZmpLcEtxTURzaGxJQSUyQnVkVllDSDZYbFlEMXdHM2lGcnphc0pLTDk3ZDhINnY1a21HZHAlMkZabktOSERjbFolMkJUZDlPMWhvSHlOdWR6TkhaNlFtJTJCTHFaWm9lcHA1RW9XeU5vRFNmV2RNSmgxUElCckh0eXd0cWZ0VG1tTzdZM01rQlFwJTJGaEZ2U0ElM0QlM0Q; _lr_env_src_ats=false; _cc_id=d4f836318fbbd48a440853bf3799cee6; cookie=%7B%22id%22%3A%2201FVMEWW42D57545TX2PKCS9EY%22%2C%22ts%22%3A1648800972661%7D; _gaexp=GAX1.2.vZkhuqNjQKGTE-0Yuo3BiA.19118.1!x-ljBQjWS0q2X5034LeLUw.19126.1; ta-octane.id=c9fb89c4-c31b-406c-bb62-f7ddc122ee48|50376aac-d125-49b9-8f3f-c89a5758e663|1650953273630|; _gcl_au=1.1.654277529.1644912957; sailthru_hid=be7fcffdbcedd4e3084e7ebf1763820a620b61a4978fae18967cb5ae57d3e7e23135f10adbdf7ba7ce143adf; RT=z=1&dm=reuters.com&si=3vl86ev48wo&ss=l2a5jmav&sl=0&tt=0; cleared-onetrust-cookies=Thu, 17 Feb 2022 19:17:07 GMT; OptanonConsent=isIABGlobal=false&datestamp=Tue+Apr+26+2022+08%3A05%3A09+GMT%2B0200+(heure+d%E2%80%99%C3%A9t%C3%A9+d%E2%80%99Europe+centrale)&version=6.31.0&hosts=&consentId=c72405db-cd24-4c23-8980-56b58594880b&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2CSPD_BG%3A1%2C2%3A1%2C4%3A1&AwaitingReconsent=false&geolocation=MA%3B04; OptanonAlertBoxClosed=2022-04-26T06:05:09.363Z; reuters-geo={country:MA, region:-}; fsbotchecked=true; sophiTagses.23dd=*; _cb_svref=null; _gid=GA1.2.1798249872.1650953079; _lr_geo_location=MA; _gali=main-content; _gat=1; _chartbeat4=t=BIw-Ize1qobBqtjTAFJud7D2Wjig&E=8&x=165&c=2.72&y=2532&w=358",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    while response.status_code != 200:
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = response.json()
    return data



def Liens_REUTERS(jour,mois,Année,Mot_clef):
    results = []
    dict_funct = {"Maroc":get_data_Maroc, "Sahara":get_data_Sahara}
    date_dict_m = {"janv.":"01", "févr.":"02","mars":"03","avr.":"04","mai":"05","juin":"06","juil.":"07","août":"08","sept.":"09","oct.":"10","nov.":"11","déc.":"12"}
    jour = str(jour)
    if len(jour)==1:
        jour = "0" + jour
    for x in Mot_clef:
        D = dict_funct[x]()
        for y in D['result']['articles']:
            date_sortie = y['published_time'][0:10]
            if jour == date_sortie[8:10] and date_dict_m[mois] == date_sortie[5:7]:
                titre = y['title']
                lien = "https://www.reuters.com"+y['canonical_url']
                date_sortie = date_sortie[8:10]+"/"+date_sortie[5:7]+"/"+str(Année)
                results.append((date_sortie,"REUTERS",titre,lien))            
    return list(set(results))  

#ress = Liens_REUTERS(25,"avr.",2022,["Sahara","Maroc"])



