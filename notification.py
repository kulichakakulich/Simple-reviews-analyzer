import time
import telebot
import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from personaldata import *

url = 'https://edu.21-school.ru'
codereview = 'https://edu.21-school.ru/projects/code-review'


def WebMonitoring(myname, mypass):
    bot = telebot.TeleBot(token)
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    try:
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
        driver.get(codereview)
        time.sleep(3)
        bot.send_message(userid, "Running script...")
        bot.send_sticker(userid, 'CAACAgEAAxkBAAEGb51jdBQL2R9NbRGUcG2Gd_gM3g06LwACTgoAAiz32gVR8cPwsFhtAAErBA')

        while True:
            time.sleep(60)
            driver.refresh()
            time.sleep(3)
            elem = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/section/div/section[2]/h4')

    except selenium.common.NoSuchElementException:
        bot.send_message(userid, "Code review on board, let's do it!")
        bot.send_sticker(userid, 'CAACAgEAAxkBAAEGb5tjdBPTt6YzR7Y4LnQZF1eBzgESGgACOQoAAiz32gWg-EZjbaI7dysE')
        WebMonitoring(myname, mypass)


if __name__ == "__main__":
    WebMonitoring(myname, mypass)
