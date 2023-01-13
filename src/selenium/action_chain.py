import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d = webdriver.Firefox()
d.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

d.implicitly_wait(5)
button = d.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
act = ActionChains(d)

act.context_click(button).perform()