import time
from selenium import webdriver
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

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("Value") == "option2":
        checkbox.click()
        time.sleep(2)
        assert checkbox.is_selected()
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR,
                                    ".radioButton")
radiobuttons[2].click()
time.sleep(2)
assert radiobuttons[2].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
print("Check 2")
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

#Alert
name = "Utkarsh"
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()

alert = driver.switch_to.alert
alertText = alert.text

print(alertText)

assert name in alertText
time.sleep(1)

alert.accept()
#alert.dismiss()
