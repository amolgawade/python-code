from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.implicitly_wait(10)

cookies = driver.get_cookies()
print('size of cookies:- ', len(cookies))

# for c in cookies:
#     print(c.get("name"),":", c.get('value'))
driver.add_cookie({"name":"mycookie", 'value': '12345'})
cookies = driver.get_cookies()
print("size of cookies after adding :- ", len(cookies))
for c in cookies:
    print(c)

driver.delete_cookie("mycookie")
cookies = driver.get_cookies()
print("size of cookies after deleting :- ", len(cookies))
for c in cookies:
    print(c)

driver.delete_all_cookies()
cookies = driver.get_cookies()
print("size of cookies after deleting all :- ", len(cookies))
for c in cookies:
    print(c)
