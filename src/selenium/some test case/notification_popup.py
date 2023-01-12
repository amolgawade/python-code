from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ops = webdriver.FirefoxOptions()
ops.add_argument("--disable-notification")

d = webdriver.Firefox(options=ops)
d.get("https://whatmylocation.com/")
