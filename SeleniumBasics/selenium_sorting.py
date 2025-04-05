import time
from selenium import webdriver
from selenium.webdriver import ActionChains
#Chrome Driver
from selenium.webdriver.chrome.service import Service
#By contains locators
from selenium.webdriver.common.by import By

#Runs the chrome browser in headless mode, ie, without opening te browser on screen
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")

#To Ignore the warning while opening a website
chrome_options.add_argument("--ignore-certificate-errors")

#Chrome driver Service Selenium ->160 -> chrome driver
service_obj = Service(r"C:\Users\utkar\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options = chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers/")

#driver.maximize_window()
#To identify the title of web page

#click on column header
#Collect all veg names in a list -> veggieList
#sort on Veggie list => newsortedList
#veggielist = newsortedList

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

veggieWebelement = driver.find_elements(By.XPATH,"//tr/td[1]")

browerSortveggies = []

for ele in veggieWebelement:
    browerSortveggies.append(ele.text)

#to create a copy of the list
original_browerSortveggies = browerSortveggies.copy()
browerSortveggies.sort()

print(browerSortveggies)

assert browerSortveggies == original_browerSortveggies














time.sleep(5)