from selenium import webdriver       #.....d=driver
from selenium.webdriver.common.by import By

d = webdriver.Firefox()
d.get("https://itera-qa.azurewebsites.net/home/automation")
d.maximize_window()

days = d.find_elements(By.XPATH, "//input[@type='checkbox' and contains (@id,'day')]")
print(len(days))


for i in range(len(days)):
    if i <= 3:
        days[i].click()



