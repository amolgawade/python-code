import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

d = webdriver.Firefox()
d.get("https://toponwardticket.com/")
time.sleep(5)
title = d.find_element(By.CSS_SELECTOR, "select[name='menu-title-1']")
drpdown = Select(title)
drpdown.select_by_visible_text("Mr")

f_name = d.find_element(By.CSS_SELECTOR, "input[name='text-first-name-1']")
f_name.send_keys("Amol")
l_named = d.find_element(By.CSS_SELECTOR, "input[name='text-last-name-1']")
l_named.send_keys('Gawade')
pasenger = Select(d.find_element(By.XPATH, "//select[@name='menu-passenger']"))
pasenger.select_by_visible_text("1")
trip = d.find_element(By.CSS_SELECTOR,"input[value='0'][name='onward-radio-flight']")
trip.click()
print(trip)
d.find_element(By.XPATH, "//input[@name='customer-email']").send_keys("abc@gmail.com")

# depart_from = Select(d.find_element(By.XPATH, '//*[@id="select2-menu-from-4y-container"]'))
# depart_from.select_by_visible_text("Pune-India(PNQ)")
#
# arrival_to = Select(d.find_element(By.XPATH, '//*[@id="select2-menu-to-sp-container"]'))
# arrival_to.select_by_visible_text("Delhi-Inda(DEL)")


d.find_element(By.XPATH, "//input[@id='my-date']").send_keys("18")

