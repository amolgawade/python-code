from selenium import webdriver
from selenium.webdriver.common.by import By
import os
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://en.wikipedia.org/wiki/Parliament_of_India")

#driver.save_screenshot("E:\code\python_practise\src\selenium\some test case\homepage.png")
driver.save_screenshot(os.getcwd()+"\\homepage.png")

driver.quit()
