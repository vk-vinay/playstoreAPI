import requests
from api.models import app_db
import  json
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def get_search(appname):
    responce=requests.get('https://play.google.com/store/search?q='+str(appname)+"'",headers=headers).content
    soup=BeautifulSoup(responce,features="html.parser",from_encoding="utf8")
    app_list=soup.select("div[class='b8cIId ReQCgd Q9MA7b']>a[href^='/store/apps/details?id=com.']")
    appd=[]
    for apps in app_list:
        a={"name=":apps.text,"appid=":apps.get('href').split("=",1)[1]}
        appd.append(a)
    return appd



def get_details(app_id):
    url='https://play.google.com/store/apps/details?id='+str(app_id)
    responce= requests.get(url, headers=headers).content
    soup = BeautifulSoup(responce, features="html.parser", from_encoding="utf8")
    app_details= soup.select(".AHFaub span, div[jsname='sngebd'],div[class='hAyfc']>span[class='htlgb']")
    deatils=[]
    if app_details.__len__()>0:


        for i in range(0, 7):
            a=app_details[i].text
            deatils.append(a)

        return deatils
    else:
        deatils='app not found use app id =com.example.xyz'
        return deatils



