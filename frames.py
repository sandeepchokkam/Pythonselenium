from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://the-internet.herokuapp.com/iframe")
# iframe, framset, frame are related to frames tag
# with the frameid or frame name or index value we can switch to that particular frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.XPATH, "//body[@id='tinymce']").clear()
driver.find_element(By.XPATH, "//body[@id='tinymce']").send_keys("I am sandeep")
driver.switch_to.default_content()
print(driver.find_element(By.XPATH,"//h3").text)
