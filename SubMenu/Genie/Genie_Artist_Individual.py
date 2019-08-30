from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


def genie_artist_individual():
    result = []
    individual_artist = input("원하시는 가수, 또는 원하는 곡의 이름을 입력해주세요 : ")
    driver = webdriver.Chrome("D:/Utility/01.080.IDE/WebDriver/chromedriver_win32/chromedriver.exe")
    driver.get("https://www.genie.co.kr")
    time.sleep(1.2)

    searched = driver.find_elements_by_class_name("ipt-search-placeholder").send_keys(individual_artist)
    clicked = driver.find_element_by_xpath('//*[@id="frmGNB"]/fieldset/input[3]').click()

    driver.find_element_by_xpath('//*[@id="body-content"]/div[2]/ul/li[3]/a').click()
    song_titles = driver.find_element_by_xpath('//*[@id="body-content"]/div[4]/div[2]/div/table/tbody/tr[1]/td[5]/a[1]')
    artist_titles = driver.find_element_by_xpath('//*[@id="body-content"]/div[4]/div[2]/div/table/tbody/tr[1]/td[5]/a[2]')

    # song_titles = driver.find_elements_by_class_name('title ellipsis')
    # artist_titles = driver.find_elements_by_class_name('artist ellipsis')

    print("원하시는 " + individual_artist + "에 관한 결과입니다.")
    for i in range(len(song_titles)):
        song = song_titles[i].text.strip()
        artist = artist_titles[i].text.strip()

        if individual_artist in song_titles or individual_artist in artist_titles:
            result += ["{0:3d}위 {1} - {2}".format(i+1, artist, song)]

    if len(result) > 0:
        for r in result:
            print(r)

    else:
        print("앗! " + individual_artist + "에 대한 데이터가 존재하지 않아요ㅠㅠ")

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
    # a = 1
    # for title in song_titles:
    #     result += ["{0:3d}위 {1} - {2}".format(a, title.text, artist_titles.text)]

    # header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    # get_link = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20190719&hh=21&rtm=Y&pg="

    # for i in range(1, 5):
    #     link = '{}{}'.format(get_link, i)
    #     get_link_2 = requests.get(link, headers=header)
    #     html = get_link_2.text
    #     bsObj = BeautifulSoup(html, "html.parser")
    #     artist_list = bsObj.findAll("a", {"class": {"artist ellipsis"}})
    #     song_list = bsObj.findAll("a", {"class": "title ellipsis"})
    #
    #     for j in range(len(song_list)):
    #         artist = artist_list[j+5].text.strip()
    #         song = artist_list[j].text.strip()
    #
    #         result += ["{0:3d}위 {1} - {2}".format((i-1) * 50 + j+1, artist, song)]
    #
    #     if len(result) > 0:
    #         for r in result:
    #             print(r)

