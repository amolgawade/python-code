import time

from selenium import webdriver
from selenium.webdriver.common.by import By


d = webdriver.Firefox()
d.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)

d.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
d.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
d.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

time.sleep(3)
d.find_element(By.CSS_SELECTOR, "a[href='/web/index.php/admin/viewAdminModule']").click()


no_rows = d.find_elements(By.XPATH,"(//div[@role='row'])")
enabled = d.find_elements(By.XPATH, "(//div[contains(text(),'Enabled')])")
disabled = d.find_elements(By.XPATH, "(//div[contains(text(),'Disabled')])")
print("total enabled status:-", len(enabled))
print("total disabled status:-", len(disabled))
print("total no of rows:-", len(no_rows))
