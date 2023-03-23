import time
import telebot
import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from personal_data import login, password, token, user_id

url = 'https://edu.21-school.ru'
code_review = 'https://edu.21-school.ru/projects/code-review'


def WebMonitoring(login, password):
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
        login.send_keys(login)
        password.send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[2]/div/div/form/div[3]/button').click()
        time.sleep(2)
        driver.get(code_review)
        time.sleep(3)
        bot.send_message(user_id, "Running script...")
        bot.send_sticker(user_id, 'CAACAgEAAxkBAAEGb51jdBQL2R9NbRGUcG2Gd_gM3g06LwACTgoAAiz32gVR8cPwsFhtAAErBA')

        while True:
            time.sleep(50)
            driver.refresh()
            time.sleep(10)
            elem = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/section/div/section[2]/h4')

    except selenium.common.NoSuchElementException:
        driver.quit()
        bot.send_message(user_id, "Code review on board, let's do it!")
        bot.send_sticker(user_id, 'CAACAgEAAxkBAAEGb5tjdBPTt6YzR7Y4LnQZF1eBzgESGgACOQoAAiz32gWg-EZjbaI7dysE')
        time.sleep(3)
        WebMonitoring(login, password)


if __name__ == "__main__":
    WebMonitoring(login, password)
