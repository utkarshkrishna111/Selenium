import time
from selenium import webdriver
#Chrome Driver
from selenium.webdriver.chrome.service import Service
#By contains locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#Chrome driver Service Selenium ->160 -> chrome driver
service_obj = Service(r"C:\Users\utkar\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()
#To identify the title of web page

#implicit wait: Here 5 seconds is maximum wait time. If it completes in 2 sec, 3 sec is saved
driver.implicitly_wait(10)

expectedlist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actuallist = []

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='product']")
count = len(results)
print(count)
assert count > 0

#chaining of elements

for result in results:
    result.find_element(By.XPATH,"div/button").click()
    actuallist.append(result.find_element(By.XPATH, "h4").text)

print(actuallist)

assert expectedlist == actuallist

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#sum validation

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
print(prices)
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)

total_amount = int((driver.find_element(By.CSS_SELECTOR,".totAmt").text))
assert  sum == total_amount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
time.sleep(5)

discount_amt = float((driver.find_element(By.XPATH,"//span[@class = 'discountAmt']").text))
print(discount_amt)

assert discount_amt < sum

print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

