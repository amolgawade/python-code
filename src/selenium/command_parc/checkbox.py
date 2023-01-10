import time

from selenium import webdriver       #.....d=driver
from selenium.webdriver.common.by import By

d = webdriver.Firefox()
d.get("https://itera-qa.azurewebsites.net/home/automation")
d.maximize_window()

days = d.find_elements(By.XPATH, "//input[@type='checkbox' and contains (@id,'day')]")
print(len(days))

for day in days:
    name = day.get_attribute("id")
    if name == 'sunday' or name == 'friday':
        day.click()
time.sleep(5)
d.close()



