from selenium import webdriver       #.....d=driver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.get("https://demo.nopcommerce.com/")
d.maximize_window()

d.find_element(By.XPATH, "//input[@id='small-searchterms']").send_keys("Asus N551JK-XO076H Laptop")
d.find_element(By.XPATH, "//button[@type='submit']").click()
d.implicitly_wait(10)
