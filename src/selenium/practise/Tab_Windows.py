import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
#
# regi_link = Keys.CONTROL+Keys.RETURN
#
# driver.find_element(By.XPATH,"(//a[normalize-space()='Register'])[1]").send_keys(regi_link)
# time.sleep(3)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.switch_to.new_window("tab")
driver.get("https://en.wikipedia.org/wiki/Parliament_of_India")

