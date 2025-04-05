import time
from selenium import webdriver
#Chrome Driver
from selenium.webdriver.chrome.service import Service
#By contains locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Chrome driver Service Selenium ->160 -> chrome driver
service_obj = Service(r"C:\Users\utkar\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()
#To identify the title of web page

#Locators in selenuim: ID, Xpath, CSSSelector, Classname, name, linkText

driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID,"exampleCheck1").click()

#Xpath and CSSSelector is used to construct and identify any element on page.
#ID, name, Classname is used to identify elements defined by developer
#XPATH -  //tagname[@attribute='value'] -> //input[@type = 'submit']
#CSSSelector -  //tagname[attribute='value'] -> //input[type = 'submit'], #id, .classname
(driver.find_element(By.CSS_SELECTOR,"input[name = 'name']").send_keys("Utkarsh"))
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

#static dropdown

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(5)
dropdown.select_by_index(0)

driver.find_element(By.XPATH,"//input[@type = 'submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys(" Krishna")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

time.sleep(5)