import time

from bs4 import BeautifulSoup
import requests


def bugs_song_chart():
    result = []
    artists_name_song = input("Enter the name of the singer or song you want (Korean) :")
    request = requests.get("https://music.bugs.co.kr/chart")
    html = request.text
    bsObj = BeautifulSoup(html, "html.parser")
    chart = bsObj.findAll("p", {"class": "title"})
    artists = bsObj.findAll("p", {"class": "artist"})

    print("This is the result of" + artists_name_song + " you want.")
    for i in range(len(chart)):
        artist = artists[i].text.strip()
        titles = chart[i].text.strip()

        if artists_name_song in artist or artists_name_song in titles:
            result += ["No.{0:3d} {1} - {2}".format((i + 1), artist, titles)]

    if len(result) > 0:
        for r in result:
            print(r)

    file = open('{}_to_belongings Rank_(bugs).txt'.format(artists_name_song), 'w', -1, 'UTF-8')
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
            from Bug_Attribute import mBugs
            first = mBugs()
            a_list.append(first)
            break

        elif a is '2':
            print("Terminated Program")
            exit(0)
            break
