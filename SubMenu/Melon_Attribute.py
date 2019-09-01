# from Main.ManageAllFile.ManageFile import *
from Melon.Search_Real_time import Melon_Real_time
from Melon.Singers_name import Melon_Singer
from Melon.Search_Aritst_song_rank import Melon_Artist_individual_rank
import time
import ChatBotModel


def mMelon():
    print("Welcome to Melon")
    print("1. Real Chart")
    print("2. Singer Name")
    print("3. Rank for each Singer Group")
    print("4. Back to the Main File")
    # print("Melon에 오신 고객님, 환영합니다.")
    # print("1. 실시간 차트")
    # print("2. 가수 이름")
    # print("3. 가수별 순위")

    # print("4. BBAK-GU Bro!!!!")
    select_melon = input("Please Select the Menu : ")
    select_list = []
    while 1:
        if select_melon is '1':
            print("Hold on Please..")
            time.sleep(1.2)
            Melon = Melon_Real_time()
            select_list.append(Melon)
            break

        elif select_melon is '2':
            print("Hold on Please..")
            time.sleep(1.2)
            kelon = Melon_Singer()
            select_list.append(kelon)
            break

        elif select_melon is '3':
            print("Hold on Please..")
            time.sleep(1.2)
            Melon = Melon_Artist_individual_rank()
            select_list.append(Melon)
            break

        elif select_melon is '4':
            print("Hold on Please..")
            from Chatbot import print_menu
            # melon = print_menu('', print_menu)
            # select_list.append(melon)
            # cjw = ChatBotModel.BotCK()
            kkw = print_menu()
            select_list.append(kkw)
            break







