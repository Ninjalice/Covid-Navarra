import tweepy
import time
import requests
import json
import os

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])
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
        api.update_status("Casos Covid-19 en Navarra/Covid-19 kasuak Nafarroan:\n"+"Ultima actualización/Azken eguneratzea: " +
                          str(data["update"])+"\n"+"Casos/Kasuak: "+str(data["casos"]) + "\n" +
                          "Recuperados/Berreskuratuak: "+str(data["recuperados"])+"\n"+"Fallecimientos/Heriotzak: " +
                          str(data["muertes"])+"\n"+"\n"+"#KoronabirusaNafarroa ")
  
    except:
        print("Duplicated")
    
    time.sleep(3600)


