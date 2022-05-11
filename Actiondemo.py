from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\chokk\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# ActionChains class is useful to perform operations like mouse movements, mouse button actions, key press, and context menu interactions
action = ActionChains(driver)
# when we use action, definitely we have to use perform menthon(perform())
action.move_to_element(driver.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
#delete comments by sandeep
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
#context_click is to right click and select the appropriate option
action.context_click(driver.find_element(By.ID, 'double-click')).perform()
action.double_click(driver.find_element(By.ID, 'double-click')).perform()
act1 = driver.switch_to.alert
print(act1.text)
act1.accept()
