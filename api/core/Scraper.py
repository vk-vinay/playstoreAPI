import requests
import  json
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

responce=requests.get('https://play.google.com/store/search?q=bbc',headers=headers).content
soup=BeautifulSoup(responce,features="html.parser",from_encoding="utf8")
app_list=soup.select("div[class='b8cIId ReQCgd Q9MA7b']>a[href^='/store/apps/details?id=com.']")
for apps in app_list:
    print("name=",apps.text,"appid=",apps.get('href').split("=",1)[1])