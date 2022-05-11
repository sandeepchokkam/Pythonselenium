from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# driver.find_element(By.NAME, "name").send_keys("Sandeep")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Sandeep")
driver.find_element(By.NAME, "email").send_keys("chokkamsandeep@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("sandeep@123")
driver.find_element(By.ID, "exampleCheck1").click()
d = driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']")
dropdown = Select(d)
dropdown.select_by_visible_text("Female")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
print(driver.find_element(By.CLASS_NAME,"alert-success").text)

