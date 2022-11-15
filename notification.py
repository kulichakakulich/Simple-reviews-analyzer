import time
import telebot
import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from personaldata import *

url = 'https://edu.21-school.ru'
CodeReview = 'https://edu.21-school.ru/projects/code-review'


def WebMonitoring(myname, mypass):
    bot = telebot.TeleBot(token)
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        time.sleep(2)
        driver.get(url)
        time.sleep(3)
        login = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login.send_keys(myname)
        password.send_keys(mypass)
        driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[2]/div/div/form/div[3]/button').click()
        time.sleep(2)
        driver.get(CodeReview)
        time.sleep(3)
        bot.send_message(userid, "Running script...")
        while True:
            time.sleep(60)
            driver.refresh()
            time.sleep(3)
            elem = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/section/div/section[2]/h4')

    except selenium.common.NoSuchElementException:
        bot.send_message(userid, "Пришло, ура ура")
        WebMonitoring(myname, mypass)


if __name__ == "__main__":
    WebMonitoring(myname, mypass)
