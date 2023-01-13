from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d = webdriver.Firefox()
d.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

act = ActionChains(d)

rome = d.find_element(By.XPATH, "//body//div//div[12]")
spain = d.find_element(By.XPATH, "//div[normalize-space()='Spain']")
act.drag_and_drop(rome, spain).perform()

