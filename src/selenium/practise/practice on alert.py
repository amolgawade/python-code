import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium .webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
driver.switch_to.alert.accept()

speed = driver.find_element(By.XPATH, "//select[@id='speed']")
list = speed.text.split('\n')
move = Select(speed)

print(len(list))

move.select_by_visible_text('Medium')


for sp in list:
    if sp == 'Slow':
        move.select_by_visible_text('Slow')
    else:
        pass
driver.close()