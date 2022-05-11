import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise")
# IMPLICIT WAIT
# driver.implicitly_wait(5)
# wait until 5 seconds if the object is not displayed
# Global wait
# 1.5 second to reach next page- execution will resume in 1.5 seconds
# if object doesn't show up at all, then max time your test waits for 5 seconds
driver.find_element(By.XPATH, "//input[@type = 'search']").send_keys("ber")
time.sleep(4)
lst = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(lst))
for l in lst:
    print()
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in buttons:
    button.click()
driver.find_element(By.XPATH, "//a[@class = 'cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# EXPLICIT WAIT
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class='promoCode']")))
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)



