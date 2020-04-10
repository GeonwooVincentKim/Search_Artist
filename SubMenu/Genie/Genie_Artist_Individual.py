from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


def genie_artist_individual():
    result = []
    individual_artist = input("원하시는 가수, 또는 원하는 곡의 이름을 입력해주세요 : ")

    driver = webdriver.Chrome("D:/Utility/01.080.IDE/WebDriver/chromedriver_win32/chromedriver/chromedriver.exe")
    driver.get("https://www.genie.co.kr")
    time.sleep(1.2)

    driver.find_element_by_xpath('//*[@id="sc-fd"]').send_keys(individual_artist)
    driver.find_element_by_xpath('//*[@id="frmGNB"]/fieldset/input[3]').click()
    # xpath_title = '//*[@id="body-content"]/div[4]/div[2]/div/table/tbody/tr[1]/td[5]/a[1]'

    for i in range(1, 15):
        xpath_title = '//*[@id="body-content"]/div[4]/div[2]/div/table/tbody/tr[%s]/td[5]/a[1]' % str(i)
        xpath_artist = '//*[@id="body-content"]/div[4]/div[2]/div/table/tbody/tr[%s]/td[5]/a[2]' % str(i)
        title = driver.find_element_by_xpath(xpath_title).text
        artist = driver.find_element_by_xpath(xpath_artist).text
        result += ["{0:3d}위  {1} - {2}".format(i+1, title, artist)]
        # print(driver.find_element_by_xpath(xpath_title).text)
    if len(result) > 0:
        for r in result:
            print(r)

    file = open("{}_rank_(genie).txt".format(individual_artist), 'w', -1, 'UTF-8')
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
            from Genie_Attribute import mGenie
            first = mGenie()
            a_list.append(first)
            break

        elif a is '2':
            print("바로 종료!!!")
            exit(0)
            break
