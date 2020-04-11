from selenium import webdriver
import time


def bugs_artist_individual():
    result = []
    bugs = input("Enter the name of the singer or song you want (Korean) : ")
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
    print("This is the result of " + bugs + " you want.")
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
        result += ["No.{0:3d}  {1} - {2}".format(i+1, title, artist)]

    if len(result) > 0:
        for r in result:
            print(r)

    else:
        print("Ah! There is no named " + bugs + " named A or a song.")

    file = open("{}_rank_(bugs).txt".format(bugs), 'w', -1, 'UTF-8')
    for i in result:
        file.write(i + "\n")
    if len(result) > 0:
        print("Finished writing file!!!")
        file.close()
    else:
        print("Failed to save data..")

    print("Would you like to continue using other services?")
    print("1. Yes    2. No")
    a = input("Please Select the Menu : ")
    a_list = []
    while 1:
        print("One moment, please.")
        time.sleep(2)
        if a is '1':
            from Bug_Attribute import mBugs
            first = mBugs()
            a_list.append(first)
            break

        elif a is '2':
            print("Terminated Program")
            exit(0)
            break
