import time
from selenium import webdriver
from selenium.webdriver import ActionChains
#Chrome Driver
from selenium.webdriver.chrome.service import Service
#By contains locators
from selenium.webdriver.common.by import By

#Runs the chrome browser in headless mode, ie, without opening te browser on screen
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

#To Ignore the warning while opening a website
chrome_options.add_argument("--ignore-certificate-errors")

#Chrome driver Service Selenium ->160 -> chrome driver
service_obj = Service(r"C:\Users\utkar\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options = chrome_options)



driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
#To identify the title of web page

#implicit wait: Here 5 seconds is maximum wait time. If it completes in 2 sec, 3 sec is saved
driver.implicitly_wait(10)

#window.scrollBy(0,document.body.scrollHeight) Javascript to scroll to bottom

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

driver.get_screenshot_as_file("screen.png")














time.sleep(5)