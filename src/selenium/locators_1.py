from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

#driver.implicitly_wait(20)
#driver.maximize_window()
#driver.find_element(By.ID, "small-searchterms").send_keys("Asus N551JK-XO076H Laptop")

driver.find_element(By.LINK_TEXT, "Register").click()
driver.implicitly_wait(20)
driver.close()
