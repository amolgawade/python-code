from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Firefox()
dr.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
dr.maximize_window()

elem = dr.find_element(By.XPATH, "//input[@id='FirstName']")
elem.send_keys("Amol Gawade")

print("result of text :-", elem.text)
print("get attribute :- ", elem.get_attribute("type"))

dr.close()
