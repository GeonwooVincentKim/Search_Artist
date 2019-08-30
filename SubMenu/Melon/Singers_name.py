import time

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


def Melon_Singer():
    Singer = input("원하시는 가수, 또는 원하시는 곡 명을 입력하세요 (한글)")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    get_singers = requests.get("https://www.melon.com/chart/index.htm", headers=headers)

    html = get_singers.text
    bsObj = BeautifulSoup(html, "html.parser")

    singers = bsObj.findAll("span", {"class": "checkEllipsis"})
    song_title = bsObj.findAll("div", {"class": "ellipsis rank01"})

    result = []

    print("입력하신 " + Singer + "에 대한 내용을 뽑아왔어요!!")
    singer = []
    for i in range(len(singers)):
        singer = singers[i].text.strip()
        title = song_title[i].text.strip()

        if Singer in singer or Singer in title:
            result += ["{0:3d}위 {1} - {2}".format(i+1, singer, title)]

    if len(result) > 0:
        for r in result:
            print(r)

    else:
        print("앗!" + Singer + "라는 가수, 또는 노래가 존재하지 않습니다.")

    print("계속해서 다른 서비스들도 이용하시겠습니까?")
    print("1. 예    2. 아니오")
    a = input("메뉴 선택 : ")
    a_list = []
    while 1:
        if a is '1':
            print("잠시만 기다려주세요!!!")
            time.sleep(1.2)
            from Melon_Attribute import mMelon
            melon = mMelon()
            a_list.append(melon)
            break

        elif a is '2':
            print("종료 중...")
            time.sleep(3)
            exit(0)
            break
