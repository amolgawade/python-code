from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

ele = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print("element no is :-"+str(len(ele)))
for i in ele:
    print(i.text)