import time
from select import select

from selenium import webdriver
from selenium .webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
driver.switch_to.alert.accept()

speed = driver.find_element(By.XPATH, "//select[@id='speed']")
move = select(speed)

print(len(move))

for sp in move:
    if sp == 'Medium':
        print(sp)
    else:
        pass
driver.close()