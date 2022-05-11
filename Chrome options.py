from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
#https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
s=Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s,options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)