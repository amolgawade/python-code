import time

from selenium import webdriver
from selenium .webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#windowsid = driver.current_window_handle
#print(windowsid)     # id=c4b59644-e98f-4273-932b-57f51fb94ddc
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "a[href='http://www.orangehrm.com']").click()
windowIDs = driver.window_handles

#parent_id = windowIDs[0]
#child_id = windowIDs[1]

#print("the windows id are", parent_id,"& ", child_id)
#time.sleep(3 )
#driver.switch_to.window(child_id)
#print("the child windows title is :- ", driver.title)

#driver.switch_to.window(parent_id)
#print("the parent windows title is :- ", driver.title)

for win in windowIDs:
    driver.switch_to.window(win)
    print(driver.title)

#driver.close()