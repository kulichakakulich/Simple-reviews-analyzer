import requests
import time
import hashlib
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://edu.21-school.ru'
CodeReview = 'https://edu.21-school.ru/projects/code-review'

driver = webdriver.Chrome('C:\\chromedriver\chromedriver.exe')
time.sleep(2)
driver.get(url)
time.sleep(5)
login = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login.send_keys("name")
password.send_keys("pass")
driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[2]/div/div/form/div[3]/button').click()

time.sleep(100)
driver.quit()


# response = urlopen(url).read()
# encode = 'utf-8'
# dec = response.decode(encode)
# f = open("pages.txt", "w")
# f.write(dec)
# f.close()

# currentHash = hashlib.sha224(response).hexdigest()
# print("running")
# time.sleep(10)
# while True:
#     try:
#         response = urlopen(url).read()
#
#         # create a hash
#         currentHash = hashlib.sha224(response).hexdigest()
#
#         # wait for 30 seconds
#         time.sleep(30)
#
#         # perform the get request
#         response = urlopen(url).read()
#
#         # create a new hash
#         newHash = hashlib.sha224(response).hexdigest()
#
#         # check if new hash is same as the previous hash
#         if newHash == currentHash:
#             continue
#         else:
#             print("something changed")
#             response = urlopen(url).read()
#
#     # create a hash
#             currentHash = hashlib.sha224(response).hexdigest()
#
#     # wait for 30 seconds
#             time.sleep(30)
#             continue
#     except Exception as e:
#         print("error")