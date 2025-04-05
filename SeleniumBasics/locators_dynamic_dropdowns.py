import time
from selenium import webdriver
#Chrome Driver
from selenium.webdriver.chrome.service import Service
#By contains locators
from selenium.webdriver.common.by import By

#Chrome driver Service Selenium ->160 -> chrome driver
service_obj = Service(r"C:\Users\utkar\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.maximize_window()
#To identify the title of web page

driver.find_element(By.ID, "autosuggest").send_keys("in")
time.sleep(5)

countries = (driver.find_elements
             (By.CSS_SELECTOR,"li[class='ui-menu-item'] a"))

print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

#Get Attribute Value is a Java Script DOM: The value gets updated when one add value to a edit box
#This is to get value entered dynamically using script
assert (driver.find_element
        (By.ID, "autosuggest").get_attribute("value") == "India")





time.sleep(5)