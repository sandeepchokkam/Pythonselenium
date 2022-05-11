# JS DOM can access any elements on web page just like how selenium does.
# Selenium have a method to execute javascript code on it.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Sandeep")
#here get_attribute('value') will inherit from document object model(DOM), there is no attribute called 'value' in that Xpath. but still it is extracting text field
print(driver.find_element(By.XPATH, "//input[@name='name']").get_attribute('value'))
print(driver.execute_script("return document.getElementsByName('name')[0].value"))
#python selenium directly don't have scroll feature, we have to use java script using execute_script
