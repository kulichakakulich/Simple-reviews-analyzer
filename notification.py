import time
import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
import telebot
from personaldata import *

url = 'https://edu.21-school.ru'
CodeReview = 'https://edu.21-school.ru/projects/code-review'


def WebMonitoring(MyName, MyPass):
    Bot = telebot.TeleBot(token)
    try:
        driver = webdriver.Chrome('C:\\chromedriver\chromedriver.exe')
        time.sleep(2)
        driver.get(url)
        time.sleep(3)
        login = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login.send_keys(MyName)
        password.send_keys(MyPass)
        driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[2]/div/div/form/div[3]/button').click()
        time.sleep(3)
        driver.get(CodeReview)
        time.sleep(3)
        while True:
            time.sleep(20)
            driver.refresh()
            time.sleep(3)
            elem = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/section/div/section[2]')

    except selenium.common.NoSuchElementException:
        Bot.send_message(userid,"Пришло, ура ура")
        WebMonitoring(MyName, MyPass)


if __name__ == "__main__":
    WebMonitoring(MyName, MyPass)

