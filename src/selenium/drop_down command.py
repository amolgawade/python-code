
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://www.opencart.com/index.php?route=account/register")

country = driver.find_element(By.XPATH, "//select[@id='input-country']")
drpcountry = Select(country)

#drpcountry.select_by_visible_text("India")
#drpcountry.select_by_value("20")
#drpcountry.select_by_index(21)

all_option = drpcountry.options
print("total no of country :-", len(all_option))

#for opt in all_option:
#   print(opt.text)

for opt in all_option:
    if opt.text == "india":
        opt.click()
    break

