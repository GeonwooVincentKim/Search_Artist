import time

from bs4 import BeautifulSoup
import requests


def bugs_song_chart_real_time():
    result = []
    request = requests.get("https://music.bugs.co.kr/chart")
    html = request.text
    bsObj = BeautifulSoup(html, "html.parser")
    chart = bsObj.findAll("p", {"class": "title"})
    artists = bsObj.findAll("p", {"class": "artist"})

    for i in range(len(chart)):
        # # print(artists[i].text)
        artist = artists[i].text.strip().split("\n")[0]
        titles = chart[i].text.strip()
        result += ["No.{0:3d} {1} - {2}".format((i+1), artist, titles)]

    if len(result) > 0:
        for r in result:
            print(r)

    file = open('Bugs_RealTime_Rank_100.txt', 'w', -1, 'UTF-8')
    for i in result:
        file.write(i + '\n')

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
            from Bug_Attribute import mBugs
            first = mBugs()
            a_list.append(first)
            break

        elif a is '2':
            print("Terminated Program")
            exit(0)
            break
