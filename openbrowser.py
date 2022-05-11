from selenium import webdriver

# driver = webdriver.Chrome(executable_path="C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
from selenium.webdriver.chrome.service import Service

# from webdriver_manager.chrome import ChromeDriverManager
s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com")
# # driver.implicitly_wait(10)
driver.maximize_window()
print(driver.title)
driver.get("https://rahulshettyacademy.com//AutomationPractice/")
print(driver.title)
# driver.find_element(By.Name, "name")
driver.back()
driver.close()
