from selenium import webdriver
import time


def bugs_artist_individual():
    result = []
    bugs = input("원하시는 가수, 또는 원하는 곡의 이름을 입력해주세요 : ")
    driver = webdriver.Chrome("D:/Utility/01.080.IDE/WebDriver/chromedriver_win32/chromedriver.exe")
    driver.get("https://music.bugs.co.kr/")
    time.sleep(1.2)
    # //*[@id="headerSearchInput"]

    driver.find_element_by_xpath('//*[@id="headerSearchInput"]').send_keys(bugs)
    # search_list = driver.find_elements_by_xpath('//*[@id="headerSearchInput"]').send_keys(bugs)
    driver.find_element_by_xpath('//*[@id="hederSearchFormButton"]').click()
    driver.find_element_by_xpath('//*[@id="container"]/section/div/fieldset/div/table/tbody/tr/td[2]/a').click()
    # //*[@id="DEFAULT0"]/table/tbody/tr[2]/th/p/a
    # //*[@id="DEFAULT0"]/table/tbody/tr[1]/th/p/a
    # //*[@id="DEFAULT0"]/table/tbody/tr[50]/th/p/a
    # //*[@id="DEFAULT0"]/table/tbody/tr[21]/td[4]/p/a
    print("원하시는 " + bugs + "에 대한 결과입니다.")
    for i in range(1, 50):
        # //*[@id="container"]/section/div/fieldset/div/table/tbody/tr/td[2]/a
        # //*[@id="DEFAULT0"]/table/tbody/tr[21]/td[4]/p/a
        # //*[@id="DEFAULT0"]/table/tbody/tr[50]/th/p/a
        # //*[@id="DEFAULT0"]/table/tbody/tr[1]/th/p/a
        # //*[@id="DEFAULT0"]/table/tbody/tr[1]/td[4]/p/a/mark
        bugs_path_title = '//*[@id="DEFAULT0"]/table/tbody/tr[%s]/th/p/a' % str(i)
        bugs_path_artist = '//*[@id="DEFAULT0"]/table/tbody/tr[%s]/td[4]/p/a/mark' % str(i)
        title = driver.find_element_by_xpath(bugs_path_title).text
        artist = driver.find_element_by_xpath(bugs_path_artist).text
        result += ["{0:3d}위  {1} - {2}".format(i+1, title, artist)]

    if len(result) > 0:
        for r in result:
            print(r)

    file = open("{}_rank_(bugs).txt".format(bugs), 'w', -1, 'UTF-8')
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
            from Bug_Attribute import mBugs
            first = mBugs()
            a_list.append(first)
            break

        elif a is '2':
            print("바로 종료!!!")
            exit(0)
            break
