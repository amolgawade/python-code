from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com")
driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
driver.implicitly_wait(15)
print("test is passed")
driver.close()


