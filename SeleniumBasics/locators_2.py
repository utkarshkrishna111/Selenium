import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome driver Service Selenium ->160 -> chrome driver
service_obj = Service(r"C:\Users\utkar\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
#driver = webdriver.Chrome()
driver.get("https://udemy.com")
#In order to maximize the window
driver.maximize_window()
#To identify the title of web page
print(driver.title)
#
print(driver.current_url)




























time.sleep(5)