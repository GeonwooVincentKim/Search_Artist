import time

from bs4 import BeautifulSoup
import requests


def genie_artist_rank():
    result = []
    indi_rank = input("Enter the name of the singer or song you want (Korean) : ")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    get_link = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20190719&hh=21&rtm=Y&pg="

    for i in range(1, 5):
        link = '{}{}'.format(get_link, i)
        genie_artist_site = requests.get(link, headers=headers)
        html = genie_artist_site.text
        bsObj = BeautifulSoup(html, "html.parser")

        artist_list = bsObj.findAll("a", {"class": "artist ellipsis"})
        song_list = bsObj.findAll("a", {"class": "title ellipsis"})

        for j in range(len(song_list)):
            artist = artist_list[j+5].text.strip()
            song = song_list[j].text.strip()
            if indi_rank in artist or indi_rank in song:
                result += ["No.{0:3d} {1} - {2}".format((i-1 * 50) + j + 1, artist, song)]

    if len(result) > 0:
        for r in result:
            print(r)

    else:
        print("Ah! There is no named " + indi_rank + " or a song.")

    file = open("{}_to belongings Rank_(genie).txt".format(indi_rank), 'w', -1, 'UTF-8')
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
            from Genie_Attribute import mGenie
            first = mGenie()
            a_list.append(first)
            break

        elif a is '2':
            print("Terminated Program")
            exit(0)
            break