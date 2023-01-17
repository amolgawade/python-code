import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.selenium.command_parc import XLutils

driver = webdriver.Chrome()
driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
driver.implicitly_wait(10)
driver.maximize_window()

file = r"E:\code\python_practise\src\selenium\textcase1.xlsx"
row = XLutils.getrowsCount(file,"Sheet2")

for r in range(2, row+1):
    prin = XLutils.readData(file, "Sheet2", r, 1)
    Ra_In = XLutils.readData(file, "Sheet2", r, 2)
    period = XLutils.readData(file, "Sheet2", r, 3)
    type = XLutils.readData(file, "Sheet2", r, 4)
    interest = XLutils.readData(file, "Sheet2", r, 5)
    expected = XLutils.readData(file, "Sheet2", r, 6)
    year = XLutils.readData(file, "Sheet2", r, 7)

    principal = driver.find_element(By.XPATH, "//input[@id='c']")
    principal.clear()
    principal.send_keys(prin)
    rate = driver.find_element(By.XPATH, "//input[@id='d']")
    rate.clear()
    rate.send_keys(Ra_In)
    duration = driver.find_element(By.XPATH, "//input[@id='e']")
    duration.clear()
    duration.send_keys(period)

    unit = Select(driver.find_element(By.XPATH, "//select[@id='f']"))
    unit.select_by_visible_text("Years")

    int_type = Select(driver.find_element(By.XPATH, "//select[@id='a']"))
    int_type.select_by_visible_text(type)
    actual_result = driver.find_element(By.XPATH, "//div[8]//div[1]//span[1]").text.replace("₹ ", "").replace(",", "")

    if float(expected) == float(int(actual_result)):
        print("test pass")
        XLutils.writeData(file, "Sheet2", r, 7, "pass")
        XLutils.fillgreencolor(file, "Sheet2", r, 7)
    else:
        print("failed")
        XLutils.writeData(file, "Sheet2", r, 7, "fail")
        XLutils.fillredcolor(file, "Sheet2", r, 7)
    time.sleep(10)

driver.close()

