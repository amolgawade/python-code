from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/")

driver.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Nested Frames']").click()


