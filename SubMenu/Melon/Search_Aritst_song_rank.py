from selenium import webdriver
import time


def Melon_Artist_individual_rank():
    result = []
    Individual_Singer_Rank = input("Enter the name of the singer or song you want (Korean) : ")
    driver = webdriver.Chrome('D:/Utility/01.080.IDE/WebDriver/chromedriver_win32/chromedriver.exe')
    time.sleep(4.5)
    driver.get("https://www.melon.com/")
    time.sleep(4.5)

    searched = driver.find_element_by_class_name("ui-autocomplete-input").send_keys(Individual_Singer_Rank)
    # searched = driver.find_element_by_xpath('//*[@id="top_search"]').send_keys(Individual_Singer_Rank)
    button = driver.find_element_by_xpath('//*[@id="gnb"]/fieldset/button[2]/span').click()

    driver.find_element_by_xpath('//*[@id="divCollection"]/ul/li[3]/a').click()
    song_titles = driver.find_elements_by_class_name('fc_gray')

    print("This is the result of " + Individual_Singer_Rank + " you want.")
    a = 1
    for title in song_titles:
        result += ["No.{0:3d} {1}".format(a, title.text)]
        a += 1

    if len(result) > 0:
        for r in result:
            print(r)

    else:
        print("Ah! There is no named " + Individual_Singer_Rank + " or a song.")

    file = open("{}'s_Song_Rank_(melon).txt".format(Individual_Singer_Rank), 'w', -1, 'UTF-8')
    for i in result:
        file.write(i + '\n')
    if len(result) > 0:
        print("Finished writing file!!!")
        file.close()
    else:
        print("Failed to save data..")

    print("Would you like to continue using other services?")
    print("1. Yes    2. No")
    is_continue = input("Please Select the Menu : ")
    is_list = []
    while 1:
        print("One moment, please.")
        time.sleep(2)
        if is_continue is '1':
            from Melon_Attribute import mMelon
            melon = mMelon()
            is_list.append(melon)
            break

        elif is_continue is '2':
            print("Terminated Program")
            exit(0)
            break
