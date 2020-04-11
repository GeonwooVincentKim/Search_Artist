import time

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


def Melon_Singer():
    Singer = input("Enter the name of the singer or the song you want (Korean)")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    get_singers = requests.get("https://www.melon.com/chart/index.htm", headers=headers)

    html = get_singers.text
    bsObj = BeautifulSoup(html, "html.parser")

    singers = bsObj.findAll("span", {"class": "checkEllipsis"})
    song_title = bsObj.findAll("div", {"class": "ellipsis rank01"})
    result = []

    print("This is the result of " + Singer + " you want.")
    for i in range(len(singers)):
        singer = singers[i].text.strip()
        title = song_title[i].text.strip()

        if Singer in singer or Singer in title:
            result += ["No.{0:3d} {1} - {2}".format(i+1, singer, title)]

    if len(result) > 0:
        for r in result:
            print(r)

    else:
        print("Ah! There is no named " + Singer + " named A or a song.")

    file = open("{}_to belongings Rank_100_(melon)".format(Singer), 'w', -1, 'UTF-8')
    for i in result:
        file.write(i + "\n")
    if len(result) > 0:
        print("Finished writing file!!!")
        file.close()
    else:
        print("Failed to save data..")

    print("Would you like to continue using other services?")
    print("1. Yes    2. No")
    a = input("Please Select the Menu : ")
    a_list = []
    while 1:
        print("One moment, please.")
        time.sleep(2)
        if a is '1':
            from Melon_Attribute import mMelon
            melon = mMelon()
            a_list.append(melon)
            break

        elif a is '2':
            print("Terminated Program")
            exit(0)
            break
