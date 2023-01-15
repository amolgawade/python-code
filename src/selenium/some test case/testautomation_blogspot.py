from selenium import webdriver
from selenium .webdriver.common.by import By

d = webdriver.Firefox()
d.get("https://itera-qa.azurewebsites.net/home/automation")

d.find_element(By.XPATH, "//input[@id='name']").send_keys("Amol Gawade")
d.find_element(By.XPATH, "//input[@id='phone']").send_keys("1234567890")
d.find_element(By.XPATH, "//input[@id='email']").send_keys("abc@gmail.com")
d.find_element(By.XPATH, "//input[@id='password']").send_keys("0987654321")
d.find_element(By.XPATH, "//textarea[@id='address']").send_keys("007 vihana pride at keshav nagar"
                                                                "pune,maharastra")

d.find_element(By.XPATH, "//button[@name='submit']").click()

rd_female = d.find_element(By.XPATH, "//input[@id='female']")
rd_male = d.find_element(By.XPATH, "//input[@id='male']")

rd_female.click()
print(rd_female.is_selected())
print(rd_male.is_selected())
rd_male.click()
print(rd_female.is_selected())
print(rd_male.is_selected())

exp_rd = d.find_elements(By.XPATH, "//input[@name='customRadio' and contains(@id,'year')]")

print(len(exp_rd))






