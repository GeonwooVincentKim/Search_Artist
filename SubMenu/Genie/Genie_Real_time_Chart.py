import time

from bs4 import BeautifulSoup
import requests


def genie_real_time():
    result = []
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    get_file_dir = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20190719&hh=21&rtm=Y&pg="

    for i in range(1, 5):
        link = '{}{}'.format(get_file_dir, i)
        genie_sites = requests.get(link, headers=header)
        html = genie_sites.text
        bsObj = BeautifulSoup(html, "html.parser")
        title_list = bsObj.findAll("a", {"class": {"title ellipsis"}})
        artist_list = bsObj.findAll("a", {"class": {"artist ellipsis"}})

        for j in range(len(title_list)):
            artist = artist_list[j + 5].text.strip()
            song = title_list[j].text.strip()
            # print("{0:3d}위 {1} - {2}".format((i-1) * 50 + j + 1, artist, song))
            result += ["No.{0:3d} {1} - {2}".format((i-1) * 50 + j + 1, artist, song)]

    if len(result) > 0:
        for r in result:
            print(r)

    else:
        print("Oops! Data could not be extracted.")
    
    file = open("Genie_RealTime_Rank_200.txt", 'w', -1, 'UTF-8')
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
