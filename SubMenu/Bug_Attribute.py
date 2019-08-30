from selenium import webdriver
import time


def Bug():
    result = []
    musician = input("원하는 가수 이름을 입력하세요 (한글) : ")

    driver = webdriver.Chrome("D:/Utility/01.080.IDE/WebDriver/chromedriver_win32/chromedriver.exe")
    driver.get("https://music.bugs.co.kr/chart")
    time.sleep(5)


