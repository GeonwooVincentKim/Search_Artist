# from selenium import webdriver
# import time
# 
# 
# def mBug():
#     result = []
#     musician = input("원하는 가수 이름을 입력하세요 (한글) : ")
# 
#     driver = webdriver.Chrome("D:/Utility/01.080.IDE/WebDriver/chromedriver_win32/chromedriver.exe")
#     driver.get("https://music.bugs.co.kr/chart")
#     time.sleep(5)

from Bugs.Bugs_Artist_Rank import bugs_song_chart
from Bugs.Bugs_Real_Time_Rank import bugs_song_chart_real_time
from Bugs.Bugs_Artist_Individual_Search import bugs_artist_individual

import time
import ChatBotModel


def mBugs():
    print("Bugs 에 오신 고객님, 환영합니다!!!")
    print("1. 실시간 차트")
    print("2. 가수 이름")
    print("3. 가수별 순위")
    print("4. 메인 메뉴로")

    select_bugs = input("원하시는 메뉴를 선택하세요!!! : ")
    select_list = []

    while 1:
        if select_bugs is '1':
            print("잠시만요..")
            time.sleep(1.2)
            bugs = bugs_song_chart_real_time()
            select_list.append(bugs)
            break

        elif select_bugs is '2':
            print("잠시만요...")
            time.sleep(1.2)
            bugs = bugs_song_chart()
            select_list.append(bugs)
            break

        elif select_bugs is '3':
            print("잠시만요...")
            time.sleep(1.2)
            bugs = bugs_artist_individual()
            select_list.append(bugs)
            break

        elif select_bugs is '4':
            print("잠시만요..")
            time.sleep(1.5)
            from Chatbot import print_menu
            bugs = print_menu()
            select_list.append(bugs)
