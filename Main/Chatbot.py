# import telegram
# kkw_token = '912709363:AAHx1AyZD1mfj-CQBDL-tUjk3nKfRHCZ568'
# kkw = telegram.Bot(token=kkw_token)
# updates = kkw.getUpdates()
# for u in updates:
#     print(u.message)
import time

import ChatBotModel

from Main.ManageAllFile.ManageFile import *
from SubMenu.Melon_Attribute import *
from SubMenu.Genie_Attribute import *
from SubMenu.Bug_Attribute import *
from SubMenu.Bugs import *

import sys


def print_menu(bot, update):
    # print("testtesttesttest")
    # print("Hello")
    # cjw.sendMessage("Hello\n Welcome to Music Chatbot")
    # cjw.sendMessage("안녕하세요\n 뮤직 챗봇에 오신 것을 환영합니다.")
    # cjw.sendMessage("1. Melon")
    # cjw.sendMessage("2. Bugs")
    # cjw.sendMessage("3. Genie")
    print("Hi. Welcome to Music Chatbot Application!!")
    print("1. Melon")
    print("2. Bugs")
    print("3. Genie")
    print("4. Terminate Program ")
    # cjw.sendMessage("무엇을 도와드릴까요? : ")
    select_menu = input("What Can I Help you? : ")
    # select_menu = input("무엇을 도와드릴까요? : ")
    select_list = []
    while 1:
        print("Hold on please..")
        if select_menu is '1':
            time.sleep(2)
            melon = mMelon()
            select_list.append(melon)
            break

        elif select_menu is '2':
            time.sleep(2)
            bugs = mBugs()
            select_list.append(bugs)
            break

        elif select_menu is '3':
            time.sleep(2)
            genie = mGenie()
            select_list.append(genie)
            break

        elif select_menu is '4':
            print("Thank you for using this Chatbot_WebCrawler Application")
            exit(0)


# def proc_rolling(bot, update):
#     cjw.sendMessage("펑!!!")
#     sound = firecracker()
#     cjw.sendMessage(sound)
#     cjw.sendMessage('쿠와아아앙ㄹ닝ㅁㄹㄴㅇㄹㄴ마렁니;ㅁㄹ나ㅣ러;')
#
#
# def proc_너_미쳤냐(bot, update):
#     cjw.sendMessage("지랄마")
#     sound = firecracker()
#     cjw.sendMessage(sound)
#     cjw.sendMessage('너가 또라이잖여 병x아')
#
#
# def proc_stop(bot, update):
#     cjw.sendMessage("잠을 쳐자기 시작합니다.")
#     cjw.stop()
#
#
# def firecracker():
#     return '쿠오아아ㅏ아앙!'

#
if __name__ == "__main__":
    # print("test")
    # print_menu()
    cjw = ChatBotModel.BotCK()
    cjw.add_handler('STTTAAARRT', print_menu)
    cjw.add_handler('WAIT', mMelon)
    # # cjw.add_handler('rolling', proc_rolling)
    # # cjw.add_handler('너_미쳤냐??', proc_너_미쳤냐)
    # cjw.add_handler('stop', proc_stop)
    cjw.start()
