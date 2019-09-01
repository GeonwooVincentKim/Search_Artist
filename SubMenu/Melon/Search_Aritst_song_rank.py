from selenium import webdriver
import time


def Melon_Artist_individual_rank():
    result = []
    Individual_Singer_Rank = input("원하시는 가수를 입력하세요!!! : ")
    driver = webdriver.Chrome('D:/Utility/01.080.IDE/WebDriver/chromedriver_win32/chromedriver.exe')
    driver.get("https://www.melon.com/")
    time.sleep(4.5)

    searched = driver.find_element_by_class_name("ui-autocomplete-input").send_keys(Individual_Singer_Rank)
    # searched = driver.find_element_by_xpath('//*[@id="top_search"]').send_keys(Individual_Singer_Rank)
    button = driver.find_element_by_xpath('//*[@id="gnb"]/fieldset/button[2]/span').click()

    driver.find_element_by_xpath('//*[@id="divCollection"]/ul/li[3]/a').click()
    song_titles = driver.find_elements_by_class_name('fc_gray')

    print("원하시는 " + Individual_Singer_Rank + "에 대한 결과입니다.")
    a = 1
    for title in song_titles:
        result += ["{0:3d}위 {1}".format(a, title.text)]
        a += 1

    if len(result) > 0:
        for r in result:
            print(r)

    else:
        print("앗! " + Individual_Singer_Rank + "에 대한 정보가 없어요ㅠㅠ")

    file = open("{}_rank_(melon).txt".format(Individual_Singer_Rank), 'w', -1, 'UTF-8')
    for i in result:
        file.write(i + '\n')
    if len(result) > 0:
        print("파일 쓰기 완료!!!")
        file.close()
    else:
        print("데이터 저장 실패ㅠㅠ")

    print("계속해서 다른 서비스들도 이용하시겠습니까?")
    print("1. 예    2. 아니오")
    is_continue = input("메뉴 선택 : ")
    is_list = []
    while 1:
        if is_continue is '1':
            print("잠시만 기다려주세요..")
            time.sleep(1.2)
            from Melon_Attribute import mMelon
            melon = mMelon()
            is_list.append(melon)
            break

        elif is_continue is '2':
            print("종료 중...")
            time.sleep(1.2)
            exit(0)
            break
