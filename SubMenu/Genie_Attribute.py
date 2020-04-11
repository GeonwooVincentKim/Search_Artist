from Genie.Genie_Real_time_Chart import genie_real_time
from Genie.Genie_Artist_rank_ import genie_artist_rank
from Genie.Genie_Artist_Individual import genie_artist_individual

import time
import ChatBotModel


def mGenie():
    print("Welcome to Genie")
    print("1. Realtime Chart")
    print("2. Singer's name")
    print("3. Rank for each Singer's")
    print("4. Back to the Main File")
    select_genie = input("Please Select the Menu : ")
    select_list = []

    while 1:
        print("Hold on Please..")
        time.sleep(2)
        if select_genie is '1':
            genie = genie_real_time()
            select_list.append(genie)
            break

        elif select_genie is '2':
            genie = genie_artist_rank()
            select_list.append(genie)
            break

        elif select_genie is '3':
            genie = genie_artist_individual()
            select_list.append(genie)
            break

        elif select_genie is '4':
            from Chatbot import print_menu
            genie = print_menu('name', '912709363:AAHx1AyZD1mfj-CQBDL-tUjk3nKfRHCZ568')
            select_list.append(genie)



