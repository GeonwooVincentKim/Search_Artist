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
            result += ["{0:3d}위 {1} - {2}".format((i-1) * 50 + j + 1, artist, song)]

    if len(result) > 0:
        for r in result:
            print(r)

    else:
        print("앗! 데이터를 뽑아오지 못했어요ㅠㅠ")

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