from bs4 import BeautifulSoup
import requests


def bugs_song_chart():
    result = []

    artists_name_song = input("원하시는 가수의 이름 또는 곡을 선택하세요")
    request = requests.get("https://music.bugs.co.kr/chart")
    html = request.text
    bsObj = BeautifulSoup(html, "html.parser")
    chart = bsObj.findAll("p", {"class": "title"})
    artists = bsObj.findAll("p", {"class": "artist"})

    print("입력하신" + artists_name_song + "에 대한 결과입니다.")
    for i in range(len(chart)):
        artist = artists[i].text.strip()
        titles = chart[i].text.strip()

        if artists_name_song in artist or artists_name_song in titles:
            result += ["{0:3d}위 {1} - {2}".format((i + 1), artist, titles)]

    if len(result) > 0:
        for r in result:
            print(r)

    file = open('{}_to_belongings Rank_(bugs).txt'.format(artists_name_song), 'w', -1, 'UTF-8')
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
            from Bug_Attribute import mBugs
            first = mBugs()
            a_list.append(first)
            break

        elif a is '2':
            print("바로 종료!!!")
            exit(0)
            break
