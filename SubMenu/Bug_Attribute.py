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
# import ChatBotModel


def mBugs():
    print("Welcome to Bugs")
    print("1. RealTime Chart")
    print("2. Singer' Name")
    print("3. Rank for each Singer's")
    print("4. Back to the Main File")

    select_bugs = input("Please Select the Menu : ")
    select_list = []

    while 1:
        print("Hold on Please..")
        time.sleep(2)
        if select_bugs is '1':
            bugs = bugs_song_chart_real_time()
            select_list.append(bugs)
            break

        elif select_bugs is '2':
            bugs = bugs_song_chart()
            select_list.append(bugs)
            break

        elif select_bugs is '3':
            bugs = bugs_artist_individual()
            select_list.append(bugs)
            break

        elif select_bugs is '4':
            from Chatbot import print_menu
            bugs = print_menu('name', '912709363:AAHx1AyZD1mfj-CQBDL-tUjk3nKfRHCZ568')
            select_list.append(bugs)
