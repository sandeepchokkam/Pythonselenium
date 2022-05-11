import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(3)
lst = driver.find_elements(By.XPATH, "//h4[@class='product-name']")
items_selected = []
# for l in lst:
#     items_selected.append(l.text)
#     print(l.text)
# print(items_selected)
lst_btn = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for i in lst_btn:
    items_selected.append(i.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    i.click()
print(items_selected)
driver.find_element(By.XPATH, "//a[@class = 'cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class='promoCode']")))
proceed_lst = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
# print(len(proceed_lst))
items_payment = []
for p in proceed_lst:
    items_payment.append(p.text)
print(items_payment)
assert items_selected == items_payment
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
# checking whether discount is applied or not
amt_b_discount = float(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
amt_a_discount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)
assert amt_b_discount > amt_a_discount
i_amount_ele = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for i in i_amount_ele:
    sum = sum+float(i.text)
print(sum)
assert amt_b_discount == sum


