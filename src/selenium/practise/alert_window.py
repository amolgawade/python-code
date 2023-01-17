import time

from selenium import webdriver
from selenium .webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

alert = driver.switch_to.alert
alert.send_keys("welcome")
print(alert.text)
#alert.accept()
alert.dismiss()
