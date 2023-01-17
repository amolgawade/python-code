from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

d = webdriver.Firefox()
d.get("https://text-compare.com/")

input_1 = d.find_element(By.XPATH, "//textarea[@id='inputText1']")
input_2 = d.find_element(By.XPATH, "//textarea[@id='inputText2']")

input_1.send_keys("welcome the page")

act = ActionChains(d)

act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()


act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB)

act.key_down(Keys.CONTROL).send_keys("v").key_down(Keys.CONTROL).perform()

