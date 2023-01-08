from selenium import webdriver       #.....d=driver
from selenium.webdriver.common.by import By

d = webdriver.Firefox()
d.get("https://demo.nopcommerce.com/")
d.maximize_window()

#d.find_element(By.CSS_SELECTOR, "input#small-searchterms")
d.find_element(By.CSS_SELECTOR, "input[name=q]").send_keys("amol")

