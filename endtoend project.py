from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
if driver.title == "Privacy error":
    driver.find_element(By.XPATH, "//button[@id='details-button']").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to rahulshettyacademy.com (unsafe)')]").click()

driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()
options = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
# /div/h4/a
print(len(options))
for l in options:
    if l.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
        l.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class='promoCode']")))
# driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul") //div[@class='suggestions']/ul/li/a
driver.find_element(By.LINK_TEXT, "India").click()
# print(len(lst))
# for lt in lst:
#     # print(lt.find_element(By.LINK_TEXT,"India"))
#     if lt.find_element(By.XPATH, "li/a").text == "India":
#         lt.find_element(By.XPATH, "li/a").click()
#     else:
#         continue
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
print(driver.find_element(By.CLASS_NAME,"alert-success").text)
driver.get_screenshot_as_file("screen.png")