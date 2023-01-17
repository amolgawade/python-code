from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d = webdriver.Firefox()
d.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")

d.switch_to.frame("iframeResult")

button = d.find_element(By.CSS_SELECTOR, "button[ondblclick='myFunction()']")

act = ActionChains(d)
act.double_click(button).perform()

