from bs4 import BeautifulSoup
import requests


def genie_artist_rank():
    result = []
    indi_rank = input("원하시는 가수, 또는 원하는 곡의 이름을 입력하세요 : ")
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
                result += ["{0:3d}위 {1} - {2}".format((i-1 * 50) + j + 1, artist, song)]

    if len(result) > 0:
        for r in result:
            print(r)

    else:
        print("앗! " +indi_rank + "에 관한 내용이 없다고 그래요ㅠㅠ 다시 한 번 확인해주세요")

    print("계속해서 다른 서비스들도 이용하시겠습니까?")
    print("1. 예    2. 아니오")
    a = input("메뉴 선택 : ")
    a_list = []
    while 1:
        if a is '1':
            print("바로 뿅하고 갑니다!!!")
            from Genie_Attribute import mGenie
            first = mGenie()
            a_list.append(first)
            break

        elif a is '2':
            print("바로 종료!!!")
            exit(0)
            break