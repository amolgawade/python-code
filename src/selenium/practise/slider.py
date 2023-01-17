from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d = webdriver.Firefox()
d.get("https://jqueryui.com/slider/#range")


min_slider = d.find_element(By.XPATH, "//span[1]")
max_slider = d.find_element(By.XPATH, "//span[2]")

print(" locations before the moving..... ")
print(min_slider.location)
print(max_slider.location)

act = ActionChains(d)

act.drag_and_drop_by_offset(min_slider,-200,0).perform()
act.drag_and_drop_by_offset(max_slider,10,0).perform()

print(" locations after the moving..... ")
print(min_slider.location)
print(max_slider.location)
