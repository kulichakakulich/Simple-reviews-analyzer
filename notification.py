import requests
import time
import hashlib

import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url = 'https://edu.21-school.ru'
CodeReview = 'https://edu.21-school.ru/projects/code-review'


def WebMonitoring(MyName, MyPass):
    try:
        driver = webdriver.Chrome('C:\\chromedriver\chromedriver.exe')
        time.sleep(2)
        driver.get(url)
        time.sleep(5)
        login = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login.send_keys(MyName)
        password.send_keys(MyPass)
        driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[2]/div/div/form/div[3]/button').click()
        time.sleep(5)
        driver.get(CodeReview)
        time.sleep(5)
        elem = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/section/div/section[2]')
        # цикл для проверки нахождения элемента

        time.sleep(100)
        driver.quit()
    except selenium.common.NoSuchElementException:
        WebMonitoring()


if __name__ == "__main__":
    WebMonitoring(MyName, MyPass)


