import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://mojoaxel.github.io/bootstrap-select-country/index.html")

driver.find_element(By.XPATH, "//body[1]/div[1]/div[4]/div[3]/div[1]/div[1]").click()
country_list = driver.find_elements(By.XPATH, "//ul[@aria-expanded='true']/li")

print(len(country_list))

for country in country_list:
    if country.text == "India":
        country.click()
        break
time.sleep(3)