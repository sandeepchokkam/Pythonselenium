from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
text_fill = "Sandeep"
s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH, "//input[@id='name']").send_keys(text_fill)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alrt = driver.switch_to.alert
assert text_fill in alrt.text
print(alrt.text)
alrt.accept()
# continued without filling anything
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
alrt1 = driver.switch_to.alert
print(alrt1.text)
alrt.dismiss()


