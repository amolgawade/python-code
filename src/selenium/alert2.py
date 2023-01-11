import time

from selenium import webdriver
from selenium .webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.find_element(By.XPATH, "//input[@title='Sign in']").click()
time.sleep(5)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()


