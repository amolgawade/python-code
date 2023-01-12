import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Firefox()
d.get("https://jqueryui.com/datepicker/")

d.switch_to.frame(0)
# d.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("06/08/1995")

year = "2025"
month = "August"
date = "6"

d.find_element(By.XPATH, "//input[@id='datepicker']").click()
time.sleep(3)
while True:
    mon = d.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yea = d.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yea == year:
        break;
    else:
        d.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

dates = d.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text == date:
        ele.click()
        break
