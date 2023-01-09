from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://www.amazon.in/")
driver.get("https://www.snapdeal.com/")

driver.back()
driver.forward()
driver.refresh()

driver.quit()