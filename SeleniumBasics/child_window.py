import time
from selenium import webdriver
#Chrome Driver
from selenium.webdriver.chrome.service import Service
#By contains locators
from selenium.webdriver.common.by import By

#Chrome driver Service Selenium ->160 -> chrome driver
service_obj = Service(r"C:\Users\utkar\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/windows")

driver.maximize_window()
#To identify the title of web page

#implicit wait: Here 5 seconds is maximum wait time. If it completes in 2 sec, 3 sec is saved
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"Click Here").click()

#This property will get links of all window names that are opened

windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)

time.sleep(5)

driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == (driver.find_element(By.TAG_NAME,"h3").text)

print(driver.find_element(By.TAG_NAME,"h3").text)
















time.sleep(5)