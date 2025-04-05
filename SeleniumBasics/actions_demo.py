import time
from selenium import webdriver
from selenium.webdriver import ActionChains
#Chrome Driver
from selenium.webdriver.chrome.service import Service
#By contains locators
from selenium.webdriver.common.by import By

#Chrome driver Service Selenium ->160 -> chrome driver
service_obj = Service(r"C:\Users\utkar\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
#To identify the title of web page

#implicit wait: Here 5 seconds is maximum wait time. If it completes in 2 sec, 3 sec is saved
driver.implicitly_wait(10)

action = ActionChains(driver)

#action.drag_and_drop()
#action.context_click() Right Click
#action.double_click()

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(2)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()




















time.sleep(10)