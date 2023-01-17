from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://onlineradiofm.in")
myDynamicElement = driver.find_element(By.NAME, "myDynamicElement")

