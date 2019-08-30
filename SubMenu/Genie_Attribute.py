from Genie.Genie_Real_time_Chart import genie_real_time
from Genie.Genie_Artist_rank_ import genie_artist_rank
from Genie.Genie_Artist_Individual import genie_artist_individual

import time
import ChatBotModel


def mGenie():
    print("Genie 에 오신 고객님, 환영합니다!!!!")
    print("1. 실시간 차트")
    print("2. 가수 이름")
    print("3. 가수별 순위")
    print("4. 빡구 하실??")
    select_genie = input("원하시는 메뉴를 선택하세요!!! : ")
    select_list = []

    while 1:
        if select_genie is '1':
            print("잠시만요.. ")
            time.sleep(1.2)
            genie = genie_real_time()
            select_list.append(genie)
            break

        elif select_genie is '2':
            print("잠시만요..")
            time.sleep(1.2)
            genie = genie_artist_rank()
            select_list.append(genie)
            break

        elif select_genie is '3':
            print("잠시만요..")
            time.sleep(1.2)
            genie = genie_artist_individual()
            select_list.append(genie)
            break

        elif select_genie is '4':
            print("잠시만요..")
            time.sleep(1.5)
            from Chatbot import print_menu
            genie = print_menu()
            select_list.append(genie)



