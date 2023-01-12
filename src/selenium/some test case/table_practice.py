import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(10)
no_rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
print("the no of row are:-", len(no_rows))
no_col = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")
print("the no of column are :-", len(no_col))

# data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]")
# print(data.text)

# print("all rows and column:  ")
#
# for r in range(2,len(no_rows)+1):
#     for c in range(1,len(no_col)+1):
#         info = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]")
#         print(info.text)
#     print( )
#

for r in range(2, len(no_rows)+1):
    author = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author == "Mukesh":
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        print(bookname,".......",author)


driver.close()
