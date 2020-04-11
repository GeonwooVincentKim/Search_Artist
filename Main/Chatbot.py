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


if __name__ == "__main__":
    cjw = ChatBotModel.BotCK()
    cjw.add_handler('STTTAAARRT', print_menu)
    cjw.add_handler('WAIT', mMelon)
    cjw.start()
