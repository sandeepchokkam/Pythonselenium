from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://test.salesforce.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id = 'username']").send_keys("sandeep.chokkam")
driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("password")
driver.find_element(By.XPATH, "//input[@id = 'Login']").click()

