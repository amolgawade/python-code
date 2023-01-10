import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.nopcommerce.com/")

Links = driver.find_elements(By.TAG_NAME, "a")
print("total no of :- ",len(Links))

for link in Links:
    print(link.text)

driver.close()
