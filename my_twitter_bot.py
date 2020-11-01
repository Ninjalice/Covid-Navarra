import tweepy
import time
import requests
import json


CONSUMER_KEY = 'iHKU9ChL3wfdwn358aH6FZKOO'
CONSUMER_SECRET = 'u3MzZXUq5mGZyeA04Gx3du4pR6H29k3ytjgsHDCigmOH85Crjg'
ACCESS_KEY = '1322639867847868416-leXYNVPnHupLiDWzdFeGrWg4ibwEXn'
ACCESS_SECRET = 'NfC5lcjmVjRKrZCh0dxlF8hxhHoaDJjc0dwq6PPlJr2ti'


print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

user = api.me()


def covid():
    covid_api = requests.get(
        "https://covid-api.com/api/reports?q=ESP%20Navarra&iso=ESP&region_name=Spain&region_province=Navarra")
    covid_data = json.loads(covid_api.content.decode('utf-8'))    

    Casos = covid_data["data"][0]["confirmed"]    
    Muertes = covid_data["data"][0]["deaths"]
    Recuperados = covid_data["data"][0]["recovered"]
    Date = covid_data["data"][0]["last_update"]

    Data = {"casos": Casos, "muertes": Muertes,
            "recuperados": Recuperados, "update": Date}

    return Data




while True:
    data = covid() 
    try:
        api.update_status("CASOS COVID EN NAVARRA/COVID kasuak Nafarroan:\n"+"Ultima actualización/Azken eguneratzea: " +
                          str(data["update"])+"\n"+"Casos/Kasuak: "+str(data["casos"]) + "\n" +
                          "Recuperados/Berreskuratuak: "+str(data["recuperados"])+"\n"+"Fallecimientos/Heriotzak: " +
                          str(data["muertes"])+"\n"+"\n"+"#KoronabirusaNafarroa ")
  
    except:
        print("Duplicated")
    
    time.sleep(3600)


