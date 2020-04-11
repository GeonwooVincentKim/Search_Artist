from bs4 import BeautifulSoup
import urllib
from urllib.error import HTTPError
import requests


def Melon_Real_time():
    result = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    get_File = requests.get("https://www.melon.com/chart/index.htm", headers=headers)

    html = get_File.text
    bsObj = BeautifulSoup(html, "html.parser")

    charts = bsObj.findAll("div", {"class": "ellipsis rank01"})
    artists = bsObj.findAll("span", {"class": "checkEllipsis"})

    print("잠시만 기다려주세요...")
    # f = open("Result_Melon100.txt", 'w', -1, 'UTF-8')
    for i in range(len(charts)):
        chart = charts[i].text.strip()
        artist = artists[i].text.strip()
        result += ["{0:3d}위 {1} - {2}".format(i + 1, chart, artist)]
        # print("{0:3d}위 {1} - {2}".format(i+1, chart, artist))

    if len(result) > 0:
        for r in result:
            print(r)

    file = open("Melon_RealTime_Rank_100.txt", 'w', -1, 'UTF-8')
    for i in result:
        file.write(i + "\n")
    if len(result) > 0:
        print("파일 쓰기 완료!!!")
        file.close()
    else:
        print("데이터 저장 실패ㅠㅠ")

    print("계속해서 다른 서비스들도 이용하시겠습니까?")
    print("1. 예    2. 아니오")
    a = input("메뉴 선택 : ")
    a_list = []
    while 1:
        if a is '1':
            print("바로 뿅하고 갑니다!!!")
            from Melon_Attribute import mMelon
            first = mMelon()
            a_list.append(first)
            break

        elif a is '2':
            print("바로 종료!!!")
            first = exit(0)
            a_list.append(first)
            break

    # if len(result) > 0:
    #     for r in result:
    #         print(r)

    # else:
    #     print("앗! 인터넷에 연결이 되어 있지 않거나, ")
    #     print("아니면 정상적인 웹 페이지가 아닌 것 같아요ㅠㅠ")
    # except AttributeError as e:
    # print("정상적인 웹 페이지가 아닌 것 같아요..한 번 확인해보시겠어요??")
    # return None

    # for i in range(len(charts)):
    # chart = charts[i].text.strip()
    # artist = artists[i].text.strip()
    # data = "{0:3d}위 {1} - {2}".format(i+1, chart, artist)
    # f.write(data + "\n")
#
# if __name__ == "__main__":
#     Melon_Real_time()
