from urllib.request import urlopen
from bs4 import BeautifulSoup

from urllib.error import HTTPError


page =58
while True:
    print('page：', page)
    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
    try:
        response = urlopen(url)
    except HTTPError:
        print("no this page")
        break
    html = BeautifulSoup(response, "lxml")
    # find (找第一個符合條件)   find_all(找所有符合條件)
    for r in html.find_all("li", class_="list-rst"):
        en = r.find("a", class_="list-rst__name-main")
        ja = r.find("small", class_="list-rst__name-ja")
        rating = r.find_all("span", class_="c-rating__val")
        s = r.find("b", class_="c-rating__val")
        print(ja.text, en.text, en["href"], s.text, rating[0].text, rating[1].text)

    page += 1
