from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

slider = driver.find_elements(By.CLASS_NAME, 'nivo-imageLink')
print("slides are = "+str(len(slider)))

link = driver.find_elements(By.TAG_NAME, "a")
print("total links on page ="+str(len(link)))
