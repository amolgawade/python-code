from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from command_parc import XLutils


driver = webdriver.Chrome()
driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
driver.implicitly_wait(10)
driver.maximize_window()

file = r"E:\code\python_practise\src\selenium\textcase1.xlsx"
row = XLutils.getrowsCount()
