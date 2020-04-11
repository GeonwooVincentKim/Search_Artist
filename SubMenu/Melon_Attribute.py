# from Main.ManageAllFile.ManageFile import *
from Melon.Search_Real_time import Melon_Real_time
from Melon.Singers_name import Melon_Singer
from Melon.Search_Aritst_song_rank import Melon_Artist_individual_rank
import time
from Chatbot import print_menu
import ChatBotModel


def mMelon():
    print("Welcome to Melon")
    print("1. Realtime Chart")
    print("2. Singer's Name")
    print("3. Rank for each Singer's")
    print("4. Back to the Main File")

    select_melon = input("Please Select the Menu : ")
    select_list = []
    while 1:
        print("Hold on Please..")
        time.sleep(2)
        if select_melon is '1':
            Melon = Melon_Real_time()
            select_list.append(Melon)
            break

        elif select_melon is '2':
            Melon = Melon_Singer()
            select_list.append(Melon)
            break

        elif select_melon is '3':
            Melon = Melon_Artist_individual_rank()
            select_list.append(Melon)
            break

        if select_melon is '4':
            # melon = print_menu('', print_menu)
            # select_list.append(melon)
            # cjw = ChatBotModel.BotCK()
            from Chatbot import print_menu
            kkw = print_menu('name', '912709363:AAHx1AyZD1mfj-CQBDL-tUjk3nKfRHCZ568')
            select_list.append(kkw)







