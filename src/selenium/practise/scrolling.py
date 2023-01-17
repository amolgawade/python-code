from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d = webdriver.Firefox()
d.get("https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags")

d.execute_script("window.scrollBy(0,3000)","")
value = d.execute_script("return window.pageYoffset;")
print("no of pixels moved:-",value)

