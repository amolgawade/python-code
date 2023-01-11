import time
from selenium import webdriver
from selenium .webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("bomb")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//a[normalize-space()='Bomb']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Bombing of Dresden in World War II']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Bombardier CRJ700 series']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Bombardier Challenger 600 series']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Bomb disposal']").click()

windows = driver.window_handles

for win in windows:
    driver.switch_to.window(win)
    print((win.title), win)

driver.close()