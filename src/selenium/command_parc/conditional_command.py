from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Fdigital-downloads")
driver.maximize_window()


print("Default search box status")
searchbox = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")

print("Display Status :- ", searchbox.is_displayed())
print("Enabled Status :- ", searchbox.is_enabled())
driver.implicitly_wait(30)

print("Default radio buttons status")
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("Selected male:-", rd_male.is_selected())
print("Selected female:-", rd_female.is_selected())

rd_male.click()
print("after selecting male ")
print("male:-", rd_male.is_selected())
print("female:-", rd_female.is_selected())

rd_female.click()
print("after selecting female :-")
print("male:-", rd_male.is_selected())
print("female:-", rd_female.is_selected())


driver.close()
