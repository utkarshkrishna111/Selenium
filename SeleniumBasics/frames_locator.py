import time
from selenium import webdriver
#Chrome Driver
from selenium.webdriver.chrome.service import Service
#By contains locators
from selenium.webdriver.common.by import By

#Chrome driver Service Selenium ->160 -> chrome driver
service_obj = Service(r"C:\Users\utkar\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Frames.html")

driver.maximize_window()
#To identify the title of web page

#implicit wait: Here 5 seconds is maximum wait time. If it completes in 2 sec, 3 sec is saved
driver.implicitly_wait(10)

driver.switch_to.frame("singleframe")

driver.find_element(By.CSS_SELECTOR,"input[type='text']").clear()

driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("I am able to automate frames")

driver.switch_to.default_content()

print(driver.find_element(By.CSS_SELECTOR,'h1').text)

time.sleep(5)