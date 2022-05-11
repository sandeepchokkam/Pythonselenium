from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://test.salesforce.com/")
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("sandeep")
driver.find_element(By.CSS_SELECTOR, ".password").send_keys("password")
# driver.find_element(By.CSS_SELECTOR, "#Login").click()
# By using CSS selector for ID we can use dot(.) and then ID name ex.(.password)
# By using CSS selector for name we can use hash(#) and then name ex.(#username)
driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
driver.find_element(By.XPATH, "//input[@value='Cancel']").click()
print(driver.find_element(By.XPATH, "//form[@name='login']/div[1]/label").text)
print(driver.find_element(By.XPATH, "//form[@name='login']/label").text)
print(driver.find_element(By.CSS_SELECTOR, "form[name='login'] label:nth-child(2)").text)
# print(driver.find_element(By.XPATH, "//form[@name='login']/div[2]/label").text)
print(driver.find_element(By.XPATH, "//label[contains(text(),'Remember me')]").text)

