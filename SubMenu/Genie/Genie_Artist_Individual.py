from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


def genie_artist_individual():
    result = []
    individual_artist = input("Enter the name of the singer or song you want (Korean) : ")

    driver = webdriver.Chrome("D:/Utility/01.080.IDE/WebDriver/chromedriver_win32/chromedriver.exe")
    driver.get("https://www.genie.co.kr")
    time.sleep(1.2)

    driver.find_element_by_xpath('//*[@id="sc-fd"]').send_keys(individual_artist)
    driver.find_element_by_xpath('//*[@id="frmGNB"]/fieldset/input[3]').click()
    # xpath_title = '//*[@id="body-content"]/div[4]/div[2]/div/table/tbody/tr[1]/td[5]/a[1]'

    for i in range(1, 15):
        xpath_title = '//*[@id="body-content"]/div[4]/div[2]/div/table/tbody/tr[%s]/td[5]/a[1]' % str(i)
        xpath_artist = '//*[@id="body-content"]/div[4]/div[2]/div/table/tbody/tr[%s]/td[5]/a[2]' % str(i)
        title = driver.find_element_by_xpath(xpath_title).text
        artist = driver.find_element_by_xpath(xpath_artist).text
        result += ["No.{0:3d}  {1} - {2}".format(i+1, title, artist)]
        # print(driver.find_element_by_xpath(xpath_title).text)
    if len(result) > 0:
        for r in result:
            print(r)

    file = open("{}_rank_(genie).txt".format(individual_artist), 'w', -1, 'UTF-8')
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
            from Genie_Attribute import mGenie
            first = mGenie()
            a_list.append(first)
            break

        elif a is '2':
            print("Terminated Program")
            exit(0)
            break
