import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# Select attributes from dropdown dynamically
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for t in countries:
    if t.text == "India":
        t.click()
        break
print(driver.find_element(By.ID, "autosuggest").get_attribute('value'))
assert driver.find_element(By.ID, "autosuggest").get_attribute('value') == "India"
# Select check boxes dynamically
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
lst = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(lst))
for i in lst:
    # i.click()
    # print(i.get_attribute('value'))
    if i.get_attribute('value') == "option2":
        print(f"{i.get_attribute('value')} check box is selected")
        i.click()
        break
# Select radio buttons dynamically
radio_list = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radio_list))
radio_list[2].click()
# if we want to iterate through each and every list then use below
# for r in radio_list:
#     if r.get_attribute('value') == 'radio2':
#         print(f"{r.get_attribute('value')} radio button is selected")
#         r.click()
#         assert r.is_selected()
