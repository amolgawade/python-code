from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def head_mode():
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(options=ops)
    return driver


driver = head_mode()
driver.get("https://demo.nopcommerce.com/")
driver.implicitly_wait(10)
print(driver.title)
print(driver.current_url)
cookies = driver.get_cookies()
print("total cookies are :-",len(cookies))
driver.close()